#!/usr/bin/node
const arg = 'C is fun';
const num = process.argv[2];
if (num === undefined) {
  console.log('Missing number of occurences');
}
for (let i = 0; i < num; i++) {
  console.log(arg);
}
