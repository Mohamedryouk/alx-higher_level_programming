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

    function fetchCharacterName(url) {
        return new Promise((resolve, reject) => {
            request(url, (charError, charResponse, charBody) => {
                if (charError) {
                    reject(charError);
                    return;
                }

                if (charResponse.statusCode !== 200) {
                    reject(new Error('Failed to fetch character details'));
                    return;
                }

                const characterData = JSON.parse(charBody);
                resolve(characterData.name);
            });
        });
    }

    const characterPromises = characterUrls.map(url => fetchCharacterName(url));

    Promise.all(characterPromises)
        .then(names => {
            names.forEach(name => console.log(name));
        })
        .catch(err => {
            console.error('Error fetching character names:', err);
        });
});
