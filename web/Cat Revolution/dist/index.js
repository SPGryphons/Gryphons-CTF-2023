var a = 10;
var b = 20;
var c = a + b;

function multiply(x, y) {
  return x * y;
}

var result = multiply(a, b);

var names = ["Alice", "Bob", "Charlie"];

var person = {
  firstName: "John",
  lastName: "Doe",
  age: 30,
  city: "New York"
};

var today = new Date();
var dayOfWeek = today.getDay();

var colors = ["red", "green", "blue"];
var randomColor = colors[Math.floor(Math.random() * colors.length)];

var sentence = "This is a sample sentence.";
var reversedSentence = sentence.split('').reverse().join('');

var isEven = function(num) {
  return num % 2 === 0;
};

function greet(name) {
  return "Hello, " + name + "!";
}

var greeting = greet("Alice");

var randomNumber = Math.floor(Math.random() * 100);

function square(x) {
  return x * x;
}

var squaredNumber = square(5);

var students = [
  { name: "Alice", grade: 85 },
  { name: "Bob", grade: 92 },
  { name: "Charlie", grade: 78 }
];

var passedStudents = students.filter(function(student) {
  return student.grade >= 80;
});
var Whiskerius="cHVyciBzb21ldGhpbmcgaXMgZmlzaHkgaGVyZSEh"
var sum = [1, 2, 3, 4, 5].reduce(function(acc, val) {
  return acc + val;
}, 0);

var message = "This is just a random message.";

var reversedMessage = message.split('').reverse().join('');

var isPalindrome = function(str) {
  return str === str.split('').reverse().join('');
};

var isPalindromeResult = isPalindrome("racecar");

var doubleArray = function(arr) {
  return arr.map(function(val) {
    return val * 2;
  });
};

var doubledNumbers = doubleArray([1, 2, 3, 4, 5]);

var animals = ["cat", "dog", "bird"];
var animalIndex = animals.indexOf("dog");

var firstThreeLetters = message.slice(0, 3);

var lastThreeLetters = message.slice(-3);

var randomIndex = Math.floor(Math.random() * students.length);
var Maximus="SGVyZSBpcyAxLzIgb2YgeW91ciBmbGFnOjl1cnJy";
var randomStudent = students[randomIndex];

var isUpperCase = function(str) {
  return str === str.toUpperCase();
};

var isUpperCaseResult = isUpperCase("HELLO");

var halfLength = Math.ceil(message.length / 2);
var firstHalf = message.slice(0, halfLength);

var secondHalf = message.slice(halfLength);

var sortedNumbers = [4, 2, 7, 1, 9, 3].sort(function(a, b) {
  return a - b;
});

var sortedNames = names.sort();

var uniqueNumbers = [...new Set([1, 2, 3, 2, 1, 4, 5])];

var reversedNames = names.reverse();

var sumOfNumbers = [1, 2, 3, 4, 5].reduce(function(acc, val) {
  return acc + val;
}, 0);

var longestWord = ["apple", "banana", "cherry"].reduce(function(longest, current) {
  return longest.length > current.length ? longest : current;
});

var wordWithLetterA = names.find(function(name) {
  return name.includes('a');
});
