#!/usr/bin/node
if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else if (parseInt(process.argv[2]) > 0) {
  let square = '';
  for (let right = 0; right < (parseInt(process.argv[2])); right++) {
    for (let down = 0; down < (parseInt(process.argv[2])); down++) {
      square += 'X';
    }
    if (right < (parseInt(process.argv[2]) - 1)) {
      square += '\n';
    }
  }
  console.log(square);
}
