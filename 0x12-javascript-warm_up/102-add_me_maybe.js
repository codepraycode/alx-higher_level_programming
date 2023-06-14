#!/usr/bin/node

function addMeMaybe (x, func) {
  func(x + 1);
}

module.exports = { addMeMaybe };
