import requests
import re

class CLIInterface:
    def __init__(self, name_node_url):
        self.name_node_url = name_node_url

    def interactuar_cli(self):
        print("Bienvenido al sistema de archivos distribuidos")
        print("Seleccione una opción:")
        print("1. GET")
        print("2. PUT")
        print("3. SEARCH")
        print("4. LIST")
        eleccion_usuario = input("Ingrese el número de su elección: ")

        if eleccion_usuario == "1":
            self.get_file(input("Ingrese el nombre del archivo: "))
        elif eleccion_usuario == "2":
            self.put_file(input("Ruta del archivo: "), input("Nombre de la máquina: "))
        elif eleccion_usuario == "3":
            self.search_files(input("Ingrese la expresión regular: "))
        elif eleccion_usuario == "4":
            self.list_files()
        else:
            print("Opción inválida. Intente de nuevo.")
            self.interactuar_cli()

    def _get_data_node_url(self, action, file_name=None):
        payload = {'action': action, 'file_name': file_name}
        response = requests.get(self.name_node_url, params=payload)
        if response.status_code == 200:
            return response.text
        else:
            print("Error: No se pudo obtener la URL del DataNode")
            self.interactuar_cli()

    def get_file(self, file_name):
        data_node_url = self._get_data_node_url('GET', file_name)
        response = requests.get(data_node_url)
        if response.status_code == 200:
            print(response.text)
        else:
            print("Error: No se pudo obtener el archivo")
            print("Status code: ", response.status_code)

    def put_file(self, file_path, machine_name):
        data_node_url = self._get_data_node_url('PUT')
        with open(file_path, 'rb') as file:
            payload = {'machine_name': machine_name}
            response = requests.put(data_node_url, files={'file': file}, data=payload)
            if response.status_code == 200:
                print(response.text)
            else:
                print("Error: No se pudo subir el archivo")
                print("Status code: ", response.status_code)

    def search_files(self, regex):
        response = requests.get(self.name_node_url  + '/search', params={'regex': regex})
        if response.status_code == 200:
            matches = re.findall(regex, response.text)
            print(matches)
        else:
            print("Error: No se pudo realizar la búsqueda")
            print("Status code: ", response.status_code)


    def list_files(self):
        response = requests.get(self.name_node_url  + '/list')
        if response.status_code == 200:
            print(response.text)
        else:
            print("Error: No se pudo listar los archivos")
            print("Status code: ", response.status_code)

if __name__ == "__main__":
    cli = CLIInterface("http://namenode_url")
    cli.interactuar_cli()
