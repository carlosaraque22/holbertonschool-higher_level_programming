#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let rectangle = '';
    for (let i = 0; i < this.height; i++) {
      for (let j = 0; j < this.width; j++) {
        rectangle += 'X';
      }
      if (i < this.height - 1) {
        rectangle += '\n';
      }
    }
    console.log(rectangle);
  }

  rotate () {
    const height2 = this.height;
    this.height = this.width;
    this.width = height2;
  }

  double () {
    this.height *= 2;
    this.width *= 2;
  }
}
module.exports = Rectangle;
