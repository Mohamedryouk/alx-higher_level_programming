#!/usr/bin/node
let arg = 'No argument'
let Arg = 'Argument found'
if (process.argv.length === 2) {
  console.log(arg);
} else if (process.argv.length === 3) {
  console.log(Arg);
} else {
  console.log('Argument found');
}
