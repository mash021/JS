// Number Guessing Game
const randomNumber = Math.floor(Math.random() * 100) + 1;
let attempts = 0;

function guessNumber(userGuess) {
    attempts++;
    if (userGuess === randomNumber) {
        return `Correct! You guessed it in ${attempts} attempts.`;
    } else if (userGuess < randomNumber) {
        return "Too low! Try again.";
    } else {
        return "Too high! Try again.";
    }
}

console.log(guessNumber(50)); // Example guess
