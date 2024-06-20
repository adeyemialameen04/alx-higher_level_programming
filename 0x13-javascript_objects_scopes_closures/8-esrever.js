#!/usr/bin/node

function esrever (list) {
  // const reversed = list.map((item, idx) => list[list.lenght - 1 - idx])
  // return reversed;
  const reversed = [];
  for (let i = list.length - 1; i >= 0; i--) {
    reversed.push(list[i]);
  }
  return reversed;
}

module.exports = { esrever };
