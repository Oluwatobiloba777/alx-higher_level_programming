#!/usr/bin/node
exports.esrever = function (list) {
    const tsilDesrever = [];
    for ( let i = (list.length - 1); i >= 0; i--) {
        tsilDesrever.push(list[i]);
    }
    return tsilDesrever;
};
