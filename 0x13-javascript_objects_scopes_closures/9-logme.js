#!/usr/bin/node
let counter = 0;
exports.logMe = function (item) {
    console.log('${counter[counter.length - 1]}: ${item}');
    counter.push(counter[counter.length - 1] + 1);
};
