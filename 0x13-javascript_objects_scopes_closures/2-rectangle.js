#!/usr/bin/node
module.exports = class Rectangle {
  cstrctr (w, h) {
    if (w > 0 && h > 0) { [this.width, this.height] = [w, h]; }
  }
};
