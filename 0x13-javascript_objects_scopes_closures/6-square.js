#!/usr/bin/node
const Sqquare = require('./5-square')

class Square extends Sqquare {
  constructor (size) {
    super(size, size)
  }

  charPrint (c) {
    if (!c) {
      this.print('X')
      return
    }

    this.print(c)
  }
}

module.exports = Square
