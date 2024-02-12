#!/usr/bin/node
if (isNaN(Number(process.argv[2])) || process.argv[2] === undefined) {
    console.log('Missing size');
  } else {
    for (let i = 0; i < process.argv[2]; i++) {
      for (let i = 0; i < process.argv[2]; i++) {
        process.stdout.write('X');
      }
      console.log();
    }
  }