#!/usr/bin/node

const argv = process.argv.slice(2);
if (argv.length === 0 || argv.length === 1) {
  console.log(0);
} else {
  const numbers = argv.map(Number);
  const sortedNums = numbers.sort((a, b) => b - a);

  console.log(sortedNums[1]);
}
