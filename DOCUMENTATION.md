#DOCUMENTATION
# Formats of requests and responses
1. `POST`: Create a person resource
    * `/api/`: with a payload `{"name": "example_name"}` in the body of the request 
    ```
    https://hngx-hiqu.onrender.com/api/

    # payload
    {"name": "example_name"}
    ```
    
    * `/api/examplename` : without data in the body of the request, but providing a name at the end of the URL
    ```
    https://hngx-hiqu.onrender.com/api/example_name
    ```

    If successful, we get a 201 CREATED response with the data we just created
    ```JSON
    {
      "id": 2,
      "name": "example_name"
    }
    ```
    Since each resource is unique, when a request with the same name is being requested to be created, we get an 400 BAD_REQUEST response
    ```JSON
    {
      "error": "Person already exists"
    }
    ```
2. `GET`: Retrieve a person resource by supplying the id or name of the person
    * `/api/user_id`
    ```
    https://hngx-hiqu.onrender.com/api/2
    ```
    * `/api/name`
    ```
    https://hngx-hiqu.onrender.com/api/example_name
    ```

    Positive result
    ```JSON
    {
      "id": 2,
      "name": "example_name"
    }
    ```
    If resource not found
    ```JSON
    {
      "detail": "Not found."
    }
    ```
3. `PUT`: Update a person resource with payload `{"name": "new_name"}` 
    * `/api/user_id`
    ```
    https://hngx-hiqu.onrender.com/api/2

    # payload
    {"name": "example_name"}
    
    ```
    * `/api/name`
     ```
    https://hngx-hiqu.onrender.com/api/example_name

    # payload
    {"name": "new_name"}
    
    ```

    Positive result
    ```JSON
    {
      "id": 2,
      "name": "new_name"
    }
    ```
    If resource not found
    ```JSON
    {
      "detail": "Not found."
    }
    ```
4. `PATCH`: Update a person resource partially with payload ` {"name": "new_name"}` 
    * `/api/user_id`
     ```
    https://hngx-hiqu.onrender.com/api/2

    # payload
    {"name": "new_name"}
    
    ```

    * `/api/name`
    ```
    https://hngx-hiqu.onrender.com/api/example_name

    # payload
    {"name": "new_name"}
    
    ```

    Positive result
    ```JSON
    {
      "id": 2,
      "name": "new_name"
    }
    ```
    If resource not found
    ```JSON
    {
      "detail": "Not found."
    }
    ```
5. `DELETE`: Delete a person resource
    * `/api/user_id`
     ```
    https://hngx-hiqu.onrender.com/api/2
    
    ```

    * `/api/name`
     ```
    https://hngx-hiqu.onrender.com/api/example_name
    
    ```

    If the resource has been delete, we receive a 204 NO_CONTENT response
  
    If resource not found
    ```JSON
    {
      "detail": "Not found."
    }
    ```

## Assumptions
* The name of each person is unique

## Known issues
* Django bypasses the validations implementated at the model level as well as serializer level when a name is sent as numbers, django automatically converts it into a string
* The app is deployed on render.com and it fails to take into account the static files at the moment

## Local setup

To set up the project in a development environment, follow the following instructions:
* Create a python virtual environment and activate it
* Go into your working directory and clone the project repository
```bash
git clone https://github.com/nabil2i/hngx-stage2.git
```
* Install the project dependencies
```bash
pip install -r requirements.txt
```
You can install the requirements if using pipenv as follow
```bash
pipenv install
```
* Make sure to add `DEBUG` and `DB_URL` as environment variables
For linux ubuntu
```bash
# In development environment,DEBUG needs to be a positive integer
export DEBUG=11

# DB_URL is a postgres database URL
export DB_URL=postgres://hngx_hmwo_user:wSD0ZwjnCQuF0iCkmPJqekUjtN5dTGpn@dpg-ck0vktkojvrs738rkvdg-a.oregon-postgres.render.com/hngx_hmwo
```
* In the project directory, run django commands
```bash
# Make migrations and commit them
python manage.py makemigrations
python manage.py migrate

# collect static files
python manage.py collectstatic
```
* Run the application
```bash
python manage.py runserver
```
## Conception Model
The resource available is a person resource, the model of which is available at this link (https://drive.google.com/file/d/1QOBEYO6phnhWr8QfzzG_98pLO-6q90NP/view?usp=sharing)

![diagrams](./assets/hgnx-stage2-diagram-Diagram.drawio.png)


## Tests
Tests have been done using postman to make live requests