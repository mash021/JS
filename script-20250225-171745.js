// Count occurrences of each character in a string
function countChars(str) {
    const charMap = {};
    for (let char of str) {
        charMap[char] = (charMap[char] || 0) + 1;
    }
    return charMap;
}

console.log(countChars("hello world"));
