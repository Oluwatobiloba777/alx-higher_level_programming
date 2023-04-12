#!/usr/bin/node
function add (a, b) {
    return a + b;
}
const args1 = parseInt(process.argv[2]);
const args2 = parseInt(process.argv[3]);
console.log(add(args1, args2));
