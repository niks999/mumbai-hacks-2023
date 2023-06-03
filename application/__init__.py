import os

from flask import Flask


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY="e0357289a3f687facd0ee8b2ec9ed2901ff553de30823b283af178ad6ecf7e75",
        DATABASE_URI="mysql://root:root@127.0.0.1/mumbai_hacks",
        APP_ENV="development",
    )

    if test_config is None:
        app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Database
    with app.app_context():
        from application import db

    @app.teardown_appcontext
    def shutdown_session(exception=None):
        db.session.remove()

    # Blueprints
    from application import routes

    app.register_blueprint(routes.bp)

    return app
