from fastapi import FastAPI, status
import random
import string

app = FastAPI()


def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


@app.get("/generate_password")
def get_password():
    password = generate_password()
    if password is None:
        return {"status": status.HTTP_400_BAD_REQUEST, "message": "something went worng"}
    else:
        return {"status": status.HTTP_200_OK, "message": "successfully generated", "password": password}
