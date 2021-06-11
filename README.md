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



### Set this project locally :computer:

1. Fork this Repository (or Download the Zip file directly and start from the step 3).

2. Open terminal / command prompt and Clone the project using 
    ```bash
    git clone https://github.com/mnamegaurav/moviedb.git
    ```
  
3. Create a python3 virtual environment:

    ```bash
    $ python3 -m venv venv
    ```

    Or, use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):

    ```bash
    $ virtualenv venv
    ```

4. Activate the virtual environment:

    On Linux or Mac or any Unix based system-
    
    ```bash
    $ source venv/bin/activate
    ```
    
    On Windows-
    ```
    > venv\Scripts\activate
    ```

5. Now Install the dependecies:

    ```bash
    $ pip install -r requirements.txt
    ```

    
6. Rename the `.env.example` file to `.env`:
    ```
    Do not forget to put your values in the new `.env` file to run the project without any issues.
    ```

7. Run the `migrate` command:

    ```bash
    $ python manage.py migrate
    ```

8. Now you are ready to go:

    #### Run the application

    ```bash
    $ python manage.py runserver
    ```

# Thanks