#!/usr/bin/node

const dict = require('./101-data').dict;

const new_dict = {};

Object.entries(dict).forEach(function (entry) {
  const [userId, occurence] = entry;

  if (!Array.isArray(new_dict[occurence])) {
    new_dict[occurence] = [userId];
  } else {
    new_dict[occurence].push(userId);
  }
});

console.log(dict);
console.log(new_dict);
