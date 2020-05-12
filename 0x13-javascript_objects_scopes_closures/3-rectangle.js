#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    for (let count = 1; count <= this.height; count++) {
	console.log('X'.repeat(parseInt(this.width)));
    }
  }
}
module.exports = Rectangle;
