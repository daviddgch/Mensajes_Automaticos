from pydantic.v1 import BaseModel


class DestinatarioDT(BaseModel):

    id: int
    nombre: str
    numero: str


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    DESTINATARIO_DTO = DestinatarioDT()
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
