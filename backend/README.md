# Setting up the backend

1. Go into the backend directory by using `cd backend`
2. If you have not already, create a virtual environment using `python -m venv venv`. A folder called `venv` should appear within the backend directory
3. Then, activate the virtual environment using:
   - `source venv/bin/activate` for macOS/Linux
   - `venv\Scripts\activate` for Windows
4. Once the virtual environment is activated, install the required python modules using `pip install -r requirements.txt`
5. Verify installation by using `pip freeze`. A list of installed module and their versions should pop up.

# Running the backend server

1. Run the backend server using `python server.py`
2. Once you are done working with the code, you can deactivate the virtual environment by running `deactivate`

NOTE: when you install new modules/dependencies, you must update the requirements.txt by running `pip freeze > requirements.txt`

# How to test connection to Database

## POST request

Once you have the backend server running, you can test a POST request by using the following command:

```shell
curl -X POST http://127.0.0.1:5000/add -H "Content-Type: application/json" -d '{"Name": <insert_name>, "age": <insert_age>}'
```

A successful request should return the following:

```
{
  "message": "Data added successfully"
}
```

## GET request

You can test a GET request by using the following command:

```shell
curl http://127.0.0.1:5000/get
```

A successful request should return something like:

```
[
  {
    "Name": "Harry",
    "_id": "66f4d62d29d84c20e5fa8f6e",
    "age": 20
  },
  {
    "Name": "Ian",
    "_id": "66f4d6ac47bd50974f2a9472",
    "age": 20
  },
  {
    "Name": "Jacky",
    "_id": "66f4d7f11728aa8c92a5bd92",
    "age": 20
  }
]
```
