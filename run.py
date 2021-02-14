from flask_caching import Cache
from app import create_app
import os

get_config_mode = os.environ.get("GENTELELLA_CONFIG_MODE", "Debug")

app = create_app()

if __name__ == "__main__":
    cache = Cache()
    config = {
        "DEBUG": True,
        "CACHE_TYPE": "simple",
        "CACHE_DEFAULT_TIMEOUT": 0,
    }
    cache.init_app(app, config=config)
    
    # development only
    os.environ["FLASK_ENV"] = "development"
    app.run()