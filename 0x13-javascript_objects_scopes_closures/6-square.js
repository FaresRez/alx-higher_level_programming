#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (typeof c !== 'undefined') {
      for (let i = 1; i <= this.height; i++) {
        for (let j = 1; j <= this.width; j++) { process.stdout.write('C'); }
        console.log();
      }
    } else { this.print(); }
  }
}
module.exports = Square;
