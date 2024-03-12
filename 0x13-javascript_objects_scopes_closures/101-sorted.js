#!/usr/bin/node
const dict = require('./101-data').dict;
const nDict = {};
for (const k in dict) {
  if (nDict[dict[k]] === undefined) {
    nDict[dict[k]] = [k];
  } else {
    nDict[dict[k]].push(k);
  }
}
console.log(nDict);
