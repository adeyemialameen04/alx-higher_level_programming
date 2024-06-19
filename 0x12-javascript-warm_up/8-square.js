#!/usr/bin/node

const args = process.argv.slice(2);
const size = Number(args[0]);

if (isNaN(size) || size <= 0) {
  console.log('Missing size');
} else {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
}
