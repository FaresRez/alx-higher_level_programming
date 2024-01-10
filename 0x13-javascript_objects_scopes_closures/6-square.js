#!/usr/bin/node
const Square_ = require('./5-square');

const Square = class Square extends Square_ {
  charPrint (c) {
    if (c === undefined) {
      super.print();
    }
    else {
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          process.stdout.write(c);
        }
        console.log();
      }
    }
  }
};

module.exports = Square;
