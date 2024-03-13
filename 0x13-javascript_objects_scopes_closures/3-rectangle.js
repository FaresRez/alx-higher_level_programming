#!/usr/bin/node
class Rectangle {
    constructor (w, h) {
      if (w > 0 && h > 0) {
        this.width = w;
        this.height = h;
      }
    }

    print(){
        for (let i=1;i<=this.height;i++)
            console.log("X");
            for (let j=1;j<=this.width;j++)
                console.log("X", end);
        
    }
  }
  module.exports = Rectangle;

  const r2 = new Rectangle(10, 5);
  r2.print();
