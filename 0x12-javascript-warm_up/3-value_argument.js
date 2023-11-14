#!/usr/bin/node
const argvL = process.argv.length - 2
const argv = process.argv

// A script to print.
if (argvL < 1) {
  console.log('No argument')
} else {
  console.log(argv[2])
}
