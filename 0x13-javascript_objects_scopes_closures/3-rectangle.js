#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    if (this.height && this.width) {
      let result = '';
      for (let i = 0; i < this.height; i++) {
        for (let j = 0; j < this.width; j++) {
          result += 'X';
        }
        if (i < this.height - 1) {
          result += '\n';
        }
      }
      console.log(result);
    }
  }
}

module.exports = Rectangle;
