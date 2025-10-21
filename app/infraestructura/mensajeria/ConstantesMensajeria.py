import os
from pathlib import Path

from dotenv import load_dotenv


class ConstantesMensajeria:
    env_path = Path(__file__).resolve().parent.parent.parent.parent / "enviroment.env"
    load_dotenv(dotenv_path=env_path)

    INSTANCIA = os.getenv("INSTANCIA")
    TOKEN = os.getenv("TOKEN")
    HOST = os.getenv("HOST")