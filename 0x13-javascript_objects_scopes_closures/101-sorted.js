#!/usr/bin/node

const dict = require('./101-data.js').dict;
const newDict = {};

for (const item in dict) {
  const occurrence = dict[item];

  if (!newDict[occurrence]) {
    newDict[occurrence] = [];
  }

  newDict[occurrence].push(item);
}

console.log(newDict);
