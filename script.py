import os
from pathlib import Path

from dotenv import load_dotenv
from pydantic.v1 import BaseModel
load_dotenv()

class DestinatarioDT(BaseModel):

    id: int
    nombre: str
    numero: str


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    load_dotenv()
    env_path = Path(__file__).resolve().parent.parent.parent.parent / "enviroment.env"
    load_dotenv(dotenv_path=env_path)
    print(os.getenv("HOST"))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
