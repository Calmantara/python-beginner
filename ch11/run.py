from app.main import create_app, db
from flask_migrate import Migrate
from app import blueprint

app = create_app("dev")
app.register_blueprint(blueprint)
app.app_context().push()

migrate = Migrate(app, db)

if __name__ == "__main__":
    app.run()
