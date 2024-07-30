#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    const wedgeMovies = films.filter(film =>
      film.characters.includes('https://swapi-api.alx-tools.com/api/people/18/')
    ).length;
    console.log(wedgeMovies);
  }
});
