import random

# لیست پروژه‌های جاوا اسکریپت
projects = [
    '''// Simple Calculator
function calculator(a, b, operator) {
    switch (operator) {
        case '+': return a + b;
        case '-': return a - b;
        case '*': return a * b;
        case '/': return b !== 0 ? a / b : 'Cannot divide by zero';
        default: return 'Invalid operator';
    }
}
console.log(calculator(10, 5, '+'));''',

    '''// Random Password Generator
function generatePassword(length) {
    const chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()";
    let password = "";
    for (let i = 0; i < length; i++) {
        password += chars.charAt(Math.floor(Math.random() * chars.length));
    }
    return password;
}
console.log("Generated Password:", generatePassword(12));''',
]

# انتخاب تصادفی یک پروژه
random_project = random.choice(projects)

# نام فایل جدید
filename = f"script-{random.randint(1000, 9999)}.js"

# ذخیره کد در فایل جاوا اسکریپت
with open(filename, "w") as f:
    f.write("// Auto-generated JS Project\n")
    f.write(random_project + "\n")

print(f"Generated: {filename}")
