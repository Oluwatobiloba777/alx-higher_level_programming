#!/usr/bin/node

//A script that prints a message depending on the number of arguments passed
if (process.argv.length === 2){
    console.log("No Argument");
}else if (process.argv.length === 3){
    console.log("Argument found");
}else {
    console.log("Arguments found");
}
