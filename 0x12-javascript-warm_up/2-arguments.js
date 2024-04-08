#!/usr/bin/node
const arg = 'No argument';
const Arg = 'Argument found';
if (process.argv.length === 2) {
  console.log(arg);
} else if (process.argv.length === 3) {
  console.log(Arg);
} else {
  console.log(Arg);
}
