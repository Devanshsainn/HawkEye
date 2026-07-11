import os
print("Running from:", os.getcwd())

from app import create_app

environment = os.getenv("FLASK_ENV", "development")

app = create_app(environment)

if __name__ == "__main__":
    app.run(
        host="127.0.0.1",
        port=5000,
        debug=app.config["DEBUG"]
    )