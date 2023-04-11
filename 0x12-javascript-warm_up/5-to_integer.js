#!/usr/bin/node

//A script thats prints if the first number can be converted to an integer
const args = process.argv[2];
console.log(Number.isNaN(Number(args)) ? 'Not a Number':'My Number:${Number(args)}');
