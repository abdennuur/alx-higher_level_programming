#!/usr/bin/node
const { argv } = require('process');
const toInt = Number(argv[2]);
if (isNaN(toInt)) { console.log('Not a number'); } else { console.log(`My number: ${toInt}`); }
