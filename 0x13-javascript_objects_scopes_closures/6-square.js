#!/usr/bin/node
const square = require('./5-square');
class Square extends square {
  charPrint (c) {
    if (c === undefined) { c = 'X'; }
    for (let count = 0; count < this.height; count++) {
      console.log(c.repeat(this.width));
    }
  }
}
module.exports = Square;
