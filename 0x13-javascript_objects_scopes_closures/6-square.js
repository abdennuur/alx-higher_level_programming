#!/usr/bin/node
module.exports = class Square extends require('./5-square') {
  charPrint (c) {
    if (c === undefined) { this.print(); } else {
      for (let ix = 0; ix < this.height; ix++) { console.log(c.repeat(this.width)); }
    }
  }
};
