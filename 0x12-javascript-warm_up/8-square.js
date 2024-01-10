#!/usr/bin/node
if (isNaN(Number(process.argv[2])) || process.argv[2] === undefined) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('x');
  }
  for (let i = 0; i < process.argv[2]; i++) {
    console.log('x');
  }
}
