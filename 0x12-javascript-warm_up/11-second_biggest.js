#!/usr/bin/node
const argvL = process.argv.length - 2
const argv = process.argv
let sum = 0

// A script to print.
if (argvL > 1) {
  for (const each of argv.slice(2)) {
    sum += parseInt(each)
  }
}

console.log(sum)
