#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(Number(argv[2])) || argv[2] === undefined) 
  console.log('Not a number');
else
  console.log(`My number: ${argv[2]}`);
