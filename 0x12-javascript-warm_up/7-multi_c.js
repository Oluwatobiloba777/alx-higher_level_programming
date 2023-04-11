#!/usr/bin/node

//A script thats prints x times C is fun using for loop
const args = process.argv[2];
const x = parseInt(args);
if (!x){
    console.log("Missing number of occurrences");
}else {
    for (let i = 0; i < x; i++){
	console.log("C is fun");
    }
}
