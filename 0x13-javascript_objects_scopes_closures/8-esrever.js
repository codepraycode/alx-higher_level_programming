#!/usr/bin/node

function esrever(list) {
	let res = [];

	for (let each of list) {
		res.unshift(each);
	}

	return res;
}

module.exports = { esrever };
