# ai_example.rb - Simple Neural Network for XOR problem (2-2-1) using backpropagation
#

#
def sigmoid(x)
  1.0 / (1.0 + Math.exp(-x))
end
#
def dsigmoid(y)
  y * (1 - y)
end
#
class NeuralNetwork
  def initialize(input_nodes, hidden_nodes, output_nodes, learning_rate=0.5)
    @input_nodes = input_nodes
    @hidden_nodes = hidden_nodes
    @output_nodes = output_nodes
    @learning_rate = learning_rate
    @weights_ih = Array.new(hidden_nodes) { Array.new(input_nodes) { rand(-1.0..1.0) } }
    @weights_ho = Array.new(output_nodes) { Array.new(hidden_nodes) { rand(-1.0..1.0) } }
    @bias_h = Array.new(hidden_nodes) { rand(-1.0..1.0) }
    @bias_o = Array.new(output_nodes) { rand(-1.0..1.0) }
  end
  #
  def feedforward(input_array)
    hidden = Array.new(@hidden_nodes, 0)
    @weights_ih.each_with_index do |weights, i|
      sum = 0
      input_array.each_with_index { |input, j| sum += input * weights[j] }
      sum += @bias_h[i]
      hidden[i] = sigmoid(sum)
    end
    #
    output = Array.new(@output_nodes, 0)
    @weights_ho.each_with_index do |weights, i|
      sum = 0
      hidden.each_with_index { |h, j| sum += h * weights[j] }
      sum += @bias_o[i]
      output[i] = sigmoid(sum)
    end
    return output, hidden
  end
  #
  def train(input_array, target_array)
    outputs, hidden = feedforward(input_array)
    output_errors = target_array.each_with_index.map { |t, i| t - outputs[i] }
    gradients = outputs.each_with_index.map { |o, i| dsigmoid(o) * output_errors[i] * @learning_rate }
    #
    @weights_ho.each_index do |i|
      @weights_ho[i].each_index do |j|
        @weights_ho[i][j] += gradients[i] * hidden[j]
      end
      @bias_o[i] += gradients[i]
    end
    #
    hidden_errors = Array.new(@hidden_nodes, 0)
    @weights_ho.each_with_index do |weights, i|
      weights.each_with_index do |w, j|
        hidden_errors[j] += w * output_errors[i]
      end
    end
    #
    hidden_gradients = hidden.each_with_index.map { |h, i| dsigmoid(h) * hidden_errors[i] * @learning_rate }
    @weights_ih.each_index do |i|
      @weights_ih[i].each_index do |j|
        @weights_ih[i][j] += hidden_gradients[i] * input_array[j]
      end
      @bias_h[i] += hidden_gradients[i]
    end
  end
end
#
# XOR training data
training_data = [
  {input: [0,0], target: [0]},
  {input: [0,1], target: [1]},
  {input: [1,0], target: [1]},
  {input: [1,1], target: [0]}
]
#
nn = NeuralNetwork.new(2, 2, 1, 0.5)
#
# TRAINING LOOP
10000.times do
  data = training_data.sample
  nn.train(data[:input], data[:target])
end
#
# TESTING
training_data.each do |data|
  output, _ = nn.feedforward(data[:input])
  puts "Input: #{data[:input]} => Output: #{output.map {|o| o.round(3)}} (Expected: #{data[:target]})"
end
#
# End of neural network demonstration
# Dependencies: None (pure Ruby, no external gems)
nil
