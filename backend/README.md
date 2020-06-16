# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server in development , execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
export DATABASE_URL=postgres://{user}:{password}@localhost:5432/{db}
export FLASK_CONFIGURATION=dev
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

To run the server in production , execute:

```bash
export FLASK_APP=flaskr
export DATABASE_URL=postgres://{user}:{password}@localhost:5432/{db}
export FLASK_CONFIGURATION=prod
flask run
```

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

## API

GET `/categories/` 
Fetches a dictionary of all available categories
- *Request parameters:* none 
- *Example response:*  
```
{
  "categories": {
    "1": "Science", 
    "2": "Art", 
    "3": "Geography", 
    "4": "History", 
    "5": "Entertainment", 
    "6": "Sports"
  }, 
  "success": true
}

```

POST `/categories/` 
Add a new category to the repository of available categories
*Request body:* {type:string}
- *Example response:*  
```
{
  "created": 9,
  "success": true
}

```


GET `/categories/<category_id>/`
Fetches a specfic category from the available categories
- *Request parameters:* category_id:int
- *Example response:*  
```
{
  "category_type": "Science",
  "success": true
}

```

GET `/questions/?page=<page_number>/` 
Fetches a paginated dictionary of questions of all available categories
- *Request parameters (optional):* page:int 
- *Example response:*  
 ``` 
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "current_category": null,
  "questions": [
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 37
}
```

GET `/questions/<question_id>/`
Fetches a specfic question from the repository of a available questions
- *Request arguments:* question_id:int 
- *Example response:* 
```
{
  "category": "Geography",
  "question": {
    "answer": "Agra",
    "category": 3,
    "difficulty": 2,
    "id": 15,
    "question": "The Taj Mahal is located in which Indian city?"
  },
  "success": true
}
```


DELETE `/questions/<question_id>/`
Delete an existing questions from the repository of available questions
- *Request arguments:* question_id:int 
- *Example response:* 
```
{
  "deleted": "28", 
  "success": true
}
```

POST `/questions/`
Add a new question to the repository of available questions
- *Request body:* {question:string, answer:string, difficulty:int, category:string}
- *Example response:* 
```
{
  "created": 29, 
  "success": true
}
```
POST `/questions/search/`
Fetches all questions where a substring matches the search term (not case-sensitive)
- *Request body:* {search_term:string}
- *Example response:*
```
{
  "current_category": null,
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    }
  ],
  "success": true,
  "total_questions": 1
}
```

GET `/categories/<int:category_id>/questions`/
Fetches a dictionary of questions for the specified category
- *Request argument:* category_id:int
- *Example response:*
```
{
  "current_category": 2,
  "questions": [
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    }
  ],
  "success": true,
  "total_questions": 4
}
```
POST `/quizzes/`
Fetches one random question within a specified category. Previously asked questions are not asked again. 
- *Request body:* {previous_questions: arr, quiz_category: {id:int, type:string}}
- *Example response*: 
```
{
  "question": {
    "answer": "Apollo 13",
    "category": 5,
    "difficulty": 4,
    "id": 2,
    "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
  },
  "success": true
}
```


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
export FLASK_APP=flaskr
export FLASK_ENV=development
export DATABASE_TEST_URL=postgres://{user}:{password}@localhost:5432/{db}
export FLASK_CONFIGURATION=test
python test_flaskr.py -v
```