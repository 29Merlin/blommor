#!/usr/bin/env python
import os

from flask import Flask
from pymongo import MongoClient

import pkgutil
import blueprints

def register_blueprints(app: Flask) -> None:

    path: Sequence[str] = getattr(blueprints, "__path__")
    modules = pkgutil.iter_modules(path)

    for _, module_name, __ in modules:
        module = __import__(f"blueprints.{module_name}", fromlist=[""])
        blueprint = module.create_blueprint()
        app.register_blueprint(blueprint)



def create_app() -> Flask:
    app = Flask(__name__)

    # Configuration
    app.secret_key = os.getenv("APP_SECRET")

    # MongoDB connection
    client = MongoClient("mongo:27017")

    register_blueprints(app)

    @app.route("/")
    def todo():
        try:
            client.admin.command("ismaster")
        except Exception:
            return "Server not available"

        return "Hello from the MongoDB client!\n"

    return app


def main() -> None:
    app = create_app()
    app.run(host='0.0.0.0', port=os.environ.get("FLASK_SERVER_PORT", 9090), debug=os.getenv("FLASK_DEBUG", False))


if __name__ == "__main__":
    main()