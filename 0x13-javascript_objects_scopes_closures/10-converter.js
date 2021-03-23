#!/usr/bin/node
exports.converter = function (base) {
  function tobase10 (number) {
    return number.toString(base);
  }
  return tobase10;
};
