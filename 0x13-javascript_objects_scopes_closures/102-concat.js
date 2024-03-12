#!/usr/bin/node
const fs = require('fs');
const flsrc1 = fs.readFileSync(process.argv[2], 'utf8');
const flsrc2 = fs.readFileSync(process.argv[3], 'utf8');
fs.writeFileSync(process.argv[4], flsrc1 + flsrc2);
