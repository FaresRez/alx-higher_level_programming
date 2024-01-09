#!/usr/bin/node
const { argv } = require('node:process');
if (isNaN(Number(argv[2])) || argv[2] === undefined)
	  console.log('Missing size');
else
  for (let i = 0; i < argv[2]; i++)
    console.log('x');
    for (let i = 0; i < argv[2]; i++)
      console.log('x');
