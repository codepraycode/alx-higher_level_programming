#!/usr/bin/node

const dict = require('./101-data').dict;

const newDict = {};

Object.entries(dict).forEach(function (entry) {
  const [userId, occurence] = entry;

  if (!Array.isArray(newDict[occurence])) {
    newDict[occurence] = [userId];
  } else {
    newDict[occurence].push(userId);
  }
});

console.log(dict);
console.log(newDict);
