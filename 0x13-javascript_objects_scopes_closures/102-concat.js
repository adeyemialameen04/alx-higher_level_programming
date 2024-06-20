#!/usr/bin/node

const fs = require('fs')
const argv = process.argv.slice(2);
const fileC = argv[2]
const fileA = argv[0]
const fileB = argv[1]

const dataA = fs.readFileSync(fileA, 'utf-8');

const dataB = fs.readFileSync(fileB, 'utf-8');

fs.writeFileSync(fileC, dataA + dataB);
