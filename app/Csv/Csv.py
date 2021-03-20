import csv
import random
from Config import Messages
import traceback


class Csv:
    """
    Está clase esta diseñada para poder trabajar con los archivos CSV.

    Attributes:
    ----------
        read_method (): Esté atributo se utiliza para guardar la palabra "r",
        que se significa read.
        write_method (): Esté atributo se utiliza para guardar la palabra "w",
        que se significa write.
        messages (class): Esté atributo se utiliza para poder instancia la,
        clase Messages y poder invocar los métodos.

    Methods:
    -------
        get_csv_data_list(csv_file_name: str) -> list
        export_data_csv(data_list_xml: list, csv_file_name: str) -> None
        select_random_item(list_data: list) -> list
        select_days(data_list_csv: list, amount: int) -> None
        compare_lists_of_data(master_list: list, data_list_two: list) -> list:
    """
    def __init__(self):
        """ El constructor de la clase Xml
        """
        self.read_method: str = 'r'
        self.write_method: str = 'w'
        self.messages = Messages()

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
        except Exception as error_message_when_getting_csv_data:
            print(f"uncaught exception {traceback.format_exc()}")
            print(self.messages.print_message_yellow(message="Posible error:"))
            print(self.messages.print_message_yellow(message="* El archivo no esté en el directorio que le especificaste."))
            print(self.messages.print_message_yellow(message="* El archivo no es el correcto."))
            print(self.messages.print_error(
                programmer_error_message=f"No se pudo cargar los datos del archivo csv > {csv_file_name}",
                error_message_from_method=error_message_when_getting_csv_data))

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
                [csv_writer.writerow([data]) for data in data_list_xml]
        except Exception as error_message_when_exporting_csv_data:
            print(f"uncaught exception {traceback.format_exc()}")
            print(self.messages.print_error(
                programmer_error_message=f"Error al exportar los datos xml al archivo > {csv_file_name}",
                error_message_from_method=error_message_when_exporting_csv_data))

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
        except TypeError as error_message_select_random_days:
            print(f"uncaught exception {traceback.format_exc()}")
            print(self.messages.print_error(
                programmer_error_message=f"Error al intertar seleccionar los días de mora",
                error_message_from_method=error_message_select_random_days))

    def compare_lists_of_data(self, master_list: list, data_list_two: list) -> list:
        """ Este método se diseñó para comparar dos listas de datos y retornar los datos duplicados.

        Args:
            master_list (list): Recibe la lista principal para comparar.
            data_list_two (list): Recibe la segunda lista para comparar.

        Returns:
            list: Retorna una lista con los datos duplicados.
        """
        try:
            search = [value for value in master_list if value in data_list_two]
            return search
        except Exception as error_comparasion_of_list:
            print(self.messages.print_error(
                programmer_error_message="Al compara la lista de datos",
                error_message_from_method=error_comparasion_of_list))
