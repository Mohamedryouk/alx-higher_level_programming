#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
if (!movieId) {
  console.error('Please provide a movie ID');
  process.exit(1);
}

const movieUrl = `https://swapi.dev/api/films/${movieId}/`;

request(movieUrl, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie details:', error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error('Failed to fetch movie details');
    return;
  }

  const movieData = JSON.parse(body);
  const characterUrls = movieData.characters;

  characterUrls.forEach(url => {
    request(url, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error fetching character details:', charError);
        return;
      }

      if (charResponse.statusCode !== 200) {
        console.error('Failed to fetch character details');
        return;
      }

      const characterData = JSON.parse(charBody);
      console.log(characterData.name);
    });
  });
});
