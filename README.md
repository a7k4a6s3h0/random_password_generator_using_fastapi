
# Password Generator using Fast API


The project is designed to make a password generator, a modern web framework for building APIs with Python. The project's primary function is to generate highly secure passwords by combining various elements such as numbers, letters, and symbols.


## Features

- Users can generate highly secure passwords




## Installation

Follow these steps to set up and run the Random Password Generator using FastAPI project on your system:

1) Clone the Repository:
Open your terminal and execute the following command to clone the project repository from GitHub:
```bash
  git clone https://github.com/a7k4a6s3h0/random_password_generator_using_fastapi.git
```
2) Then access to the Project Directory using cd command

```bash
cd your_project_directory_name
```
3) Install dependencies

```bash
pip install -r requirements.txt
```
4) run the project

```bash
uvicorn pass_generator:app --reload
```
The server will start, and you'll see output indicating that the FastAPI app is running and listening for incoming requests.

5) Shutdown the Server:
To stop the FastAPI server, press Ctrl+C in the terminal where it's running.

    
## Documentation

API Endpoint
Generate Password
Request
- Method: GET
- Endpoint: /generate_password
Query Parameters:
length (optional): Specifies the length of the generated password. Default is 8 characters.

Response
- Status Code: 200 OK
- Response Body:

```bash
{
    "status": 200,
    "message": "successfully generated",
    "password": "Xy9!pAbZ2"
}
```
Error Response:
- Status Code: 400 Bad Request
- Response Body:

```bash
{
    "status": 400,
    "message": "something went wrong"
}
```

# Usage
- Generate a Password:
    To generate a random password, make a GET request to generate_password. You can optionally provide the length query parameter to specify the desired length of the password. If no length is provided, the default length of 8 characters will be used.
- Important Notes :
    The generated passwords are strong and random, containing a mix of uppercase and lowercase letters, digits, and special characters.
    The project ensures that the generated passwords are suitable for security purposes and can be used to enhance the protection of accounts and sensitive data.
    While the default password length is 8 characters, users can customize the length by providing the length query parameter.

- Error Handling :
    The project handles errors and exceptions using appropriate HTTP status codes and response messages. If something goes wrong during password generation, a 400 Bad Request response is returned.

- Conclusion :
    The Password Generator project provides a quick and reliable way to create strong and secure passwords. By leveraging FastAPI, the project delivers a straightforward API for generating random passwords with varying lengths, enhancing the security of user accounts and sensitive information.
