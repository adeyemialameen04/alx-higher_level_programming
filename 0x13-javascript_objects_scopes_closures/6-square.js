#!/usr/bin/node
const SquareBase = require('./5-square');

class Square extends SquareBase {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }
    if (this.width && this.height) {
      let result = '';
      for (let i = 0; i < this.height; i++) {
        result += c.repeat(this.width);
        if (i < this.height - 1) {
          result += '\n';
        }
      }
      console.log(result);
    }
  }
}

module.exports = Square;
