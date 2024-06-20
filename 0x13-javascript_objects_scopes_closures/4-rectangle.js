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

  rotate () {
    if (this.height && this.width) {
      const tmp = this.height;
      this.height = this.width;
      this.width = tmp;
    }
  }

  double () {
    if (this.height && this.width) {
      this.height = this.height * 2;
      this.width = this.width * 2;
    }
  }
}

module.exports = Rectangle;
