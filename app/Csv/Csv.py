import csv
import random


class Csv:
    """
    Está clase esta diseñada para poder trabajar con los archivos CSV

    Attributes:
    ----------
        read_method (): Esté atributo se utiliza para guardar la palabra "r" que se significa read.
        write_method (): Esté atributo se utiliza para guardar la palabra "w" que se significa write.

    Methods:
    -------
        get_csv_data_list(csv_file_name: str) -> list:
        export_data_csv(data_list_xml: list, csv_file_name: str) -> None:
        select_random_item(list_data: list) -> list:
        select_days(data_list_csv: list, amount: int) -> None:
        print_error_csv(mesaage_error_method: str, message: Exception) -> None:
    """
    def __init__(self):
        """ El constructor de la clase Xml
        """
        self.read_method: str = 'r'
        self.write_method: str = 'w'

    # Método encargado de leer los datos que están en el archivo csv
    def get_csv_data_list(self, csv_file_name: str) -> list:
        """ Este método se diseñó para poder leer los archivo csv y poder guadar los número de estados de cuenta,
            en una lista.

        Args:
            csv_file_name (str): Nombre del archivo csv con el cual se esté trabajando.

        Returns:
            list: Una lista con los números de estados de cuenta.
        """
        try:
            with open(csv_file_name, self.read_method) as file_csv:
                reader = csv.reader(file_csv)
                data_list_csv = [''.join(item) for item in reader if item]

                return data_list_csv
        except Exception as error:
            self.print_error_csv(mesaage_error_method=f"No se pudo cargar los datos del archivo csv : {csv_file_name}", message=error)

    # Método para exportar los estados de cuenta a un archivo csv
    def export_data_csv(self, data_list_xml: list, csv_file_name: str) -> None:
        """ Este método se diseñó para poder exportar todos números de estados de cuenta que estén en archivo xml.

        Args:
            data_list_xml (list): Lista con todos los números de estados de cuenta.
            csv_file_name (str): Nombre del archivo csv en donde se guardara la información.
        """
        try:
            with open(csv_file_name, self.write_method, newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                for data in data_list_xml:
                    csv_writer.writerow([data])
        except Exception as error:
            self.print_error_csv(mesaage_error_method=f"Error al exportar los datos xml al archivo :{csv_file_name}", message=error)

    def select_random_item(self, list_data: list) -> list:
        """ Este método se diseñó para genera datos aleatorio de una lista que recibe.

        Args:
            list_data (list): Lista con datos para poder seleccionar un dato alzar.

        Returns:
            list: Una lista con un valor alzar
        """
        random_index = random.randrange(0, len(list_data))
        return list_data[random_index]

    def select_days(self, data_list_csv: list, amount: int) -> None:
        """ Este método se diseñó para seleccionar los días de mora alzar.

        Args:
            data_list_csv (list): Lista con todos los números de días de mora.
            amount (int): Número de días a buscar.
        """
        try:
            flag = True
            count = 0
            print('NÚMERO_OBLIGACIÓN | DÍAS_MORA')
            while flag:
                random_value = self.select_random_item(list_data=data_list_csv)
                split_value = random_value.split(";")

                if int(split_value[1]) > 0:
                    print(f"{split_value[0]} | {split_value[1]}")
                    count += 1
                if count == amount:
                    flag = False
                    print("\n")
        except TypeError as error:
            self.print_error_csv(mesaage_error_method="Error al intertar seleccionar los días de mora", message=error)

    # Método para imprimir errores del archivo Csv
    def print_error_csv(self, mesaage_error_method: str, message: Exception) -> None:
        """ Este método se diseñó para imprimir en consola los errores que ocurren en la clase Csv y terminar de correr la aplicación

        Args:
            mesaage_error_method (str): Mensaje indicando el error que pudo haber pasado.
            message (Exception): Mensaje de error que describe lo que paso, esto lo genera el try except.
        """
        print(f"ERROR: {mesaage_error_method}")
        exit(f"ERROR: {message}")
