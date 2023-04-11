#!/usr/bin/node
const args = process.argv[2];
console.log(Number.isNaN(Number(args)) ? 'Not a Number'
	    :'My Number:${Number(args)}');
