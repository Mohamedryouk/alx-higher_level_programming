#!/usr/bin/node
const firstArgument = process.argv[2];
if (firstArgument === undefined) {
  console.log('Missing size');
}
for (let i = 0; i < firstArgument; i++) {
  let row = '';
  for (let j = 0; j < firstArgument; j++) {
    row += 'X';
  }
  process.stdout.write(row + '\n');
}
