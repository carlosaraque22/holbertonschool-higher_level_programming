#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nocurr = 0;
  for (let i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      nocurr += 1;
    }
  }
  return nocurr;
};
