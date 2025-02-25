// Check if a word is a palindrome
function isPalindrome(word) {
    return word === word.split('').reverse().join('');
}

console.log("Is 'racecar' a palindrome?", isPalindrome("racecar"));
console.log("Is 'hello' a palindrome?", isPalindrome("hello"));// Js commit 2 on Tue Feb 25 17:16:13 UTC 2025
