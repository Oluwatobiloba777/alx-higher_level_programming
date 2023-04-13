#!/usr/bin/node
module.exports = class Rectangle {
    constructor (w, h) {
	if ((w !== 0 && w > 0) && (h !== 0 && h > 0)) {
	    this.width = w;
	    this.height = h;
	} 
    }

    print () {
        let character = 'X';
        for (let i = 0; i < this.height; i++) {
            for (let j = 1; j < this.width; j++) {
                character = character.concat('X');
            }
            console.log(character);
            character = 'X';
        }
    }

    rotate () {
        [this.width, this.height] = [this.height, this.width];
    }

    double () {
        this.width = this.width * 2;
        this.height = this.height * 2;
    }
};
