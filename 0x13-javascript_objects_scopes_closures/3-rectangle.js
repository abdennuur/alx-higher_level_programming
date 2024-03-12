#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }

  print () {
    for (let ix = 0; ix < this.height; ix++) {
      console.log('X'.repeat(this.width));
    }
  }
};
