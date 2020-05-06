#!/usr/bin/node
exports.callMeMoby = (x, action) => {
  for (let min = 1; min <= x; min++) {
    action();
  }
};
