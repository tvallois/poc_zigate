from poc_zigate.application import create_flask_app

if __name__ == "__main__":
    app = create_flask_app("development")
    app.run()
