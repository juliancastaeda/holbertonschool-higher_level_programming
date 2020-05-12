#!/usr/bin/node

class Rectangle {
  constructor (h, w) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let count = 0; count < this.width; count++) {
      console.log('X'.repeat(this.height));
    }
  }
}
module.exports = Rectangle;
