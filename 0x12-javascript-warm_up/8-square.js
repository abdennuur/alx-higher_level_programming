#!/usr/bin/node
const { argv } = require('process');
const sizeOfSquare = Number(argv[2]);
const Xtimes = 'X'.repeat(sizeOfSquare);
if (isNaN(sizeOfSquare)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < sizeOfSquare; i++) {
    console.log(Xtimes);
  }
}
