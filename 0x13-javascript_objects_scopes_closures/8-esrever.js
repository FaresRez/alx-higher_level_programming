#!/usr/bin/node
exports.esrever = function (list) {
  const reversedlist = [];
  while (list.length > 0) {
    reversedlist.push(list.pop());
  }
  return reversedlist;
};
