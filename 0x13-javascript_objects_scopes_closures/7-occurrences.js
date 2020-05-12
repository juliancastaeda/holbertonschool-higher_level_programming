#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let saveelement = 0;
  list.forEach(function (element) {
    if (element === searchElement) { saveelement++; }
  });
  return saveelement;
};
