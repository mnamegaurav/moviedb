# Movie DB
### This is a simple project created to show for hiring assignment of Skylarks Lab.

You can find the project [Live](https://mnamegaurav-moviedb.herokuapp.com) here.

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



### Set this project locally (docker process) :computer:

1. Open terminal / command prompt and Clone the project using 
    ```bash
    $ git clone https://github.com/mnamegaurav/moviedb.git
    ```

2. Install docker and run this command in your system:
    ```bash
    # docker build -t moviedb:latest .     
    ```

3. Run this project:
    ```bash
    # docker run --name moviedb -d -p 8000:8000 moviedb:latest
    ```

### Set this project locally (manual process) :computer:

1. Open terminal / command prompt and Clone the project using 
    ```bash
    git clone https://github.com/mnamegaurav/moviedb.git
    ```
  
2. Create a python3 virtual environment:

    ```bash
    $ python3 -m venv venv
    ```

    Or, use [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html):

    ```bash
    $ virtualenv venv
    ```

3. Activate the virtual environment:

    On Linux or Mac or any Unix based system-
    
    ```bash
    $ source venv/bin/activate
    ```
    
    On Windows-
    ```
    > venv\Scripts\activate
    ```

4. Now Install the dependecies:

    ```bash
    $ pip install -r requirements.txt
    ```

    
5. Rename the `.env.example` file to `.env`:
    ```
    Do not forget to put your values in the new `.env` file to run the project without any issues.
    ```

6. Run the `migrate` command:

    ```bash
    $ python manage.py migrate
    ```

7. Now you are ready to go:

    #### Run the application

    ```bash
    $ python manage.py runserver
    ```

# Thanks