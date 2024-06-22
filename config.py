from dynaconf import Dynaconf

settings = Dynaconf(
    settings_files=["settings.yml"],  # List of configuration files to load
    environments=True,  # Enable environments (e.g., development, production)
    envvar_prefix="Geolocation"  
)