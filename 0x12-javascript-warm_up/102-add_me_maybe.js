#!/usr/bin/node
exports.addMeMaybe = (num, action) => {
  action(num + 1);
};
