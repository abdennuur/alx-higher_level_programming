#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let cnt = 0;
  list.map(
    (x) => {
      if (x === searchElement) {
        cnt += 1;
        return 1;
      } else {
        return 0;
      }
    }
  );
  return cnt;
};
