#!/usr/bin/node

let count = 0;
function logMe (item) {
  console.log(`${count}: ${item}`);
  count++;
}
module.exports = { logMe };
