# Project Structure and Process

1. I created 2 folders: app, test.
2. APP
   - router folder with the file called user.py -> here we have all the methods of user API like create, update, delete.
   - crud.py-> all 4 functions are here.
   - database.py-> here we connect the DB URL in .env.
   - models.py-> this project has 3 columns: `id`, `name`, `email`.
   - schemas.py-> request and response format, used Pydantic model.
   - main.py-> this is the main file where it will start the backend and routers.

3.TEST
   - 1 file called `test_users.py` used to test the APIs by creating and getting the users.

# How to Run Backend

Clone repo -> create environment -> activate -> install requirements -> run:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload  # run the app
```
# Test
```bash
pytest test/  # run tests
```

I used Postman to test, but with routes and schema, *Swagger UI* is here:  
[http://127.0.0.1:8000/docs]
