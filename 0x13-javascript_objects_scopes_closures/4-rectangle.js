#!/usr/bin/node

class Rectangle {
  constructor (h, w) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print() {
    for (let count = 0; count < this.width; count++) {
	console.log('X'.repeat(this.height));
    }
}
  rotate () {
     let save = this.height;
     this.height = this.width;
     this.width = save
  }
  double () {
     this.width *= 2;
     this.height *=2;
  }
}
module.exports = Rectangle;
