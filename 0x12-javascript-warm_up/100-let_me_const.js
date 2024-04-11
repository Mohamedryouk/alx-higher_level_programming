#!/usr/bin/node

module.exports.change = function (myVar) {
  myVar = 333;
  return myVar;
};
myVar = this.change(myVar);
