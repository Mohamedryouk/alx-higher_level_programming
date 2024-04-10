#!/usr/bin/node
const args = process.argv.slice(2);

if (args.length <= 1) {
  console.log(0);
  process.exit(0);
}

let largest = -Infinity;
let secondLargest = -Infinity;
for (let i = 0; i < args.length; i++) {
  const num = parseInt(args[i]);
  if (num > largest) {
    secondLargest = largest;
    largest = num;
  } else if (num > secondLargest && num !== largest) {
    secondLargest = num;
  }
}
console.log(secondLargest);
