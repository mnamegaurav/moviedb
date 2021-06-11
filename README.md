# Movie DB
### This is a simple project created to show for hiring assignment of Skylarks Lab.

A simple REST API for a basic movie database interacting with external API. Here’s full specification of endpoints in this project:

- `POST /movies`:
    - Request body should contain only movie title, and its presence should be validated.
    - Based on passed title, other movie details should be fetched from [http://www.omdbapi.com/](http://www.omdbapi.com/) (or other similar, public movie database) - and saved to application database.
    - Request response should include full movie object, along with all data fetched from external API.

- `GET /movies`:
    - Should fetch list of all movies already present in application database.
    - Additional filtering, sorting is fully optional - but some implementation is a bonus.

- `POST /comments`:
    - Request body should contain ID of movie already present in database, and comment text body.
    - Comment should be saved to application database and returned in request response.

- `GET /comments`:
    - Should fetch list of all comments present in application database.
    - Should allow filtering comments by associated movie, by passing its ID.