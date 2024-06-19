#!/usr/bin/node

const args = process.argv.slice(2);
function add (a, b) {
  // console.log(isNaN(a) || isNaN(b) ? "NaN" : a + b);
  console.log(Number(a) + Number(b));
}

add(args[0], args[1]);
