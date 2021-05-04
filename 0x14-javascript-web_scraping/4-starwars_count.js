#!/usr/bin/node
const request = require('request');
request.get(process.argv[2], function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    let count = 0;
    for (const film of JSON.parse(body).results) {
      for (const chr of film.characters) {
        if (chr.search('/18/') > 0) { count++; }
      }
    }
    console.log(count);
  }
});
