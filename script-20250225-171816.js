//voice assistant

let userName = "";
let todos = [];

function getReply(command) {
    command = command.toLowerCase();
    
    if (command.startsWith("hello my name is")) {
        const nameParts = command.split(" ");
        userName = nameParts[nameParts.length - 1];
        return `Nice to meet you, ${userName.charAt(0).toUpperCase() + userName.slice(1)}`;
    }
    
    if (command === "what is my name?") {
        return userName ? `Your name is ${userName}` : "I don't know your name yet!";
    }
    
    if (command.startsWith("add")) {
        const task = command.replace("add", "").replace("to my todo", "").trim();
        todos.push(task);
        return `${task} added to your todo`;
    }
    
    if (command.startsWith("remove")) {
        const task = command.replace("remove", "").replace("from my todo", "").trim();
        todos = todos.filter(t => t !== task);
        return `Removed ${task} from your todo`;
    }
    
    if (command === "what is on my todo?") {
        return todos.length ? `You have ${todos.length} todos: ${todos.join(" and ")}` : "Your todo list is empty";
    }
    
    if (command === "what day is it today?") {
        const today = new Date();
        return today.toLocaleDateString("en-GB", { day: 'numeric', month: 'long', year: 'numeric' });
    }
    
    if (command.startsWith("what is")) {
        const mathExpression = command.replace("what is", "").trim();
        try {
            const result = eval(mathExpression);
            return `The answer is ${result}`;
        } catch {
            return "Sorry, I couldn't calculate that.";
        }
    }
    
    if (command.startsWith("set a timer for")) {
        const minutes = parseInt(command.match(/\d+/)[0]);
        setTimeout(() => console.log("Timer done!"), minutes * 60 * 1000);
        return `Timer set for ${minutes} minutes`;
    }
    
    return "Sorry, I don't understand that command.";
}
// Js commit 6 on Tue Feb 25 17:18:16 UTC 2025
