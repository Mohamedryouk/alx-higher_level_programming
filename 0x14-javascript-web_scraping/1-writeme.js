#!/usr/bin/node

const fs = require('node:fs');

const content = process.argv[3];
const filePath = process.argv[2];

const options = {
  encoding: 'utf-8'
};

fs.writeFile(filePath, content, options, err => {
  if (err) {
    console.error(err);
  }
});
