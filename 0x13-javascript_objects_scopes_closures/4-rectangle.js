#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print (chr = 'X') {
    for (let i = 0; i < this.height; i++) {
      let str = '';

      for (let j = 0; j < this.width; j++) {
        str += chr;
      }
      console.log(str);
    }
  }

  rotate () {
    const _tmp = this.width;

    this.width = this.height;
    this.height = _tmp;
  }

  double () {
    this.width *= 2;
    this.height *= 2;
  }
}

module.exports = Rectangle;
