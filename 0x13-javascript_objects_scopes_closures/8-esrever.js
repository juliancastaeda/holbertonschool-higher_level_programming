#!/usr/bin/node

exports.esrever = function (list) {
  const list1 = [];
  for (let count = list.length - 1; count >= 0; count--) { list1.push(list[count]); }
  return list1;
};
