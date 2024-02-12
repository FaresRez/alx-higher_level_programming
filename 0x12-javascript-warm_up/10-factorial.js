#!/usr/bin/node
function factorial (a, b) {
    if (b == NaN || a == 0 || a == NaN)
    return 1;
else
    return a*factorial(a-1, b);
}
  
  console.log(factorial(Number(process.argv[2]), Number(process.argv[3])));
