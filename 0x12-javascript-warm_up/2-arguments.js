#!/usr/bin/node

// A script to print.
if ((process.argv.length - 2) < 1) {
  console.log('No argument')
} else if ((process.argv.length - 2) === 1) {
  console.log('Argument found')
} else {
  console.log('Arguments found')
}
