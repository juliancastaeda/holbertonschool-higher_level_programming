#!/usr/bin/node
const Rectangle = require('./4-rectangle');
class Square extends Rectangle {
    constructor (size) {
	super (size, size);
    }
    charPrint(c) {
	if (c === undefined) {c = 'X';}
	for (let count = 0; count < this.height; count++) {
	    console.log(c.repeat(this.width));
	}
    }
}
module.exports = Square;
