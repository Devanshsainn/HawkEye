import os
print("Running from:", os.getcwd())

from app import create_app

environment = os.getenv("FLASK_ENV", "development")

app = create_app(environment)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app.run(
        host="0.0.0.0",
        port=port,
        debug=app.config["DEBUG"]
    )