#!/usr/bin/node
exports.esrever = function (list) {
  const nList = [];
  for (let ix = list.length - 1; ix >= 0; ix--) {
    nList.push(list[ix]);
  }
  return nList;
};
