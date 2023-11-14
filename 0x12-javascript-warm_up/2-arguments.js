#!/usr/bin/node
const argvL = process.argv.length - 2

// A script to print.
if (argvL < 1) {
  console.log('No argument')
} else if (argvL === 1) {
  console.log('Argument found')
} else {
  console.log('Arguments found')
}
