#!/usr/bin/node

function nbOccurences (list, searchElement) {
  let count = 0;

  for (const each of list) {
    if (each === searchElement) {
      count += 1;
    }
  }

  return count;
}

module.exports = { nbOccurences };
