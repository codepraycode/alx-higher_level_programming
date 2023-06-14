#!/usr/bin/node

const argv = process.argv;

// A script to print.
const num1 = parseInt(argv[2]);

function factorial (value) {
  const num = parseInt(value);

  if (!num || num <= 1) {
    return 1;
  }

  const ans = num * factorial(num - 1);

  return ans;
}

console.log(factorial(num1));
