#!/usr/bin/node

function factorial (x) {
  if (x === 0 || x === 1) {
    return 1;
  } else if (isNaN(x)) {
    return 1;
  } else {
    return x * factorial(x - 1);
  }
}
const input = parseInt(process.argv[2]);

console.log(factorial(input));
