#!/usr/bin/node
if (isNaN(Number(process.argv[2])) || process.argv[2] === undefined) {
    console.log('Not a number');
  } else {
    console.log(`My number: ${process.argv[2]}`);
  }