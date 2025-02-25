// Generate and sort random numbers
function generateRandomArray(size) {
    let arr = Array.from({ length: size }, () => Math.floor(Math.random() * 100));
    return arr.sort((a, b) => a - b);
}

console.log("Sorted Random Array:", generateRandomArray(10));
