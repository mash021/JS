class Task
  attr_accessor :description, :completed

  def initialize(description)
    @description = description
    @completed = false
  end

  def mark_complete
    @completed = true
  end

  def to_s
    "#{completed ? '[✓]' : '[ ]'} #{description}"
  end
end

class TaskManager
  def initialize
    @tasks = []
  end

  def add_task(description)
    @tasks << Task.new(description)
    puts "Task added: #{description}"
  end

  def list_tasks
    if @tasks.empty?
      puts "No tasks available."
    else
      puts "\nYour Tasks:"
      @tasks.each_with_index do |task, index|
        puts "#{index + 1}. #{task}"
      end
    end
  end

  def remove_task(index)
    if index.between?(1, @tasks.length)
      removed_task = @tasks.delete_at(index - 1)
      puts "Task removed: #{removed_task.description}"
    else
      puts "Invalid task number!"
    end
  end

  def mark_task_complete(index)
    if index.between?(1, @tasks.length)
      @tasks[index - 1].mark_complete
      puts "Task marked as complete: #{@tasks[index - 1].description}"
    else
      puts "Invalid task number!"
    end
  end

  def menu
    loop do
      puts "\nTask Manager Menu"
      puts "1. Add Task"
      puts "2. List Tasks"
      puts "3. Remove Task"
      puts "4. Mark Task as Complete"
      puts "5. Exit"
      print "Choose an option: "
      
      choice = gets.chomp.to_i
      case choice
      when 1
        print "Enter task description: "
        description = gets.chomp
        add_task(description)
      when 2
        list_tasks
      when 3
        print "Enter task number to remove: "
        index = gets.chomp.to_i
        remove_task(index)
      when 4
        print "Enter task number to mark as complete: "
        index = gets.chomp.to_i
        mark_task_complete(index)
      when 5
        puts "Exiting Task Manager. Goodbye!"
        break
      else
        puts "Invalid choice! Try again."
      end
    end
  end
end

# Start the program
task_manager = TaskManager.new
task_manager.menu
