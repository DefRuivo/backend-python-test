from todoapp import create_app



if __name__ == "__main__":
    create_app().run(load_dotenv=".flaskenv")