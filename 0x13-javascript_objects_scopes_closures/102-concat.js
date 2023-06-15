#!/usr/bin/node

const fs = require('fs').promises;
const argv = require('process').argv;

// File paths
const file1 = argv[2];
const file2 = argv[3];
const dest = argv[4];

// Read files
fs.readFile(file1, 'utf-8')
  .then(function (data) {
    fs.writeFile(dest, data, 'utf-8');
  })
  .catch(function (error) {
    console.error(error);
  });

fs.readFile(file2, 'utf-8')
  .then(function (data) {
    fs.writeFile(dest, data, 'utf-8');
  })
  .catch(function (error) {
    console.error(error);
  });
