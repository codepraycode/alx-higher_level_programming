#!/usr/bin/node

let index = 0;

function logMe(item) {
	console.log(`${index}: ${item}`);
	index++;
}

module.exports = { logMe };
