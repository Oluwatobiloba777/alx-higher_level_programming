#!/usr/bin/node
const args = process.argv[2];
console.log(Number.isNaN(Number(args)) ? 'Not a number'
	    :'My number: ${Number(args)}');
