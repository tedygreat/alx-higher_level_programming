#!/usr/bin/node
// prints the first argument passed to

const process = require('process');
let arg = process.argv[2];
if (arg === undefined) {
  console.log('No argument');
} else {
  console.log(arg);
}
