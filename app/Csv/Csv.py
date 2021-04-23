import csv
import random
from Config import Messages, Config
import traceback

messages = Messages()
config = Config().yaml_configuration()


class Csv:
    """
    Está clase esta diseñada para poder trabajar con los archivos CSV.

    Attributes:
    ----------
        read_method (): Esté atributo se utiliza para guardar la palabra "r",
        que se significa read.
        write_method (): Esté atributo se utiliza para guardar la palabra "w",
        que se significa write.

    Methods:
    -------
        get_csv_data_list(csv_file_name: str) -> list
        export_data_csv(data_list_xml: list, csv_file_name: str) -> None
        select_random_item(list_data: list) -> list
        select_keys_and_random_values(data_list_csv: list, amount: int) -> None
        compare_lists_of_data(master_list: list, data_list_two: list) -> list:
    """
    def __init__(self):
        """ El constructor de la clase Xml
        """
        self.read_method: str = 'r'
        self.write_method: str = 'w'

    def get_csv_data_list(self, csv_file_name: str) -> list:
        """ Este método se diseñó para poder leer los archivo CSV y poder guardar,
            los datos en una lista.

        Args:
            csv_file_name (str): Nombre del archivo csv con el cual se esté trabajando.

        Returns:
            list: Una lista con los datos.
        """
        try:
            with open(csv_file_name, self.read_method) as file_csv:
                reader = csv.reader(file_csv)
                data_list_csv = [''.join(item) for item in reader if item]
                return data_list_csv
        except Exception as error_message_when_getting_csv_data:
            print(f"uncaught exception {traceback.format_exc()}")
            print_possible_errors = messages.print_messages_in_colors(
                "Posible error:",
                "* El archivo no esté en el directorio que le especificaste.",
                "* El archivo no es el correcto.",
                color='yellow')
            print(f"{print_possible_errors[0]}\n"
                  f"{print_possible_errors[1]}\n"
                  f"{print_possible_errors[2]}\n")
            print(messages.print_error(
                programmer_error_message=f"No se pudo cargar los datos del archivo csv > {csv_file_name}",
                error_message_from_method=error_message_when_getting_csv_data))

    def export_data_csv(self, data_list_xml: list, csv_file_name: str) -> None:
        """ Este método se diseñó para poder exportar los datos que le indiquen.

        Args:
            data_list_xml (list): Lista con todos los datos a exportar.
            csv_file_name (str): Nombre del archivo csv en donde se guardara la información.
        """
        try:
            with open(csv_file_name, self.write_method, newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                [csv_writer.writerow([data]) for data in data_list_xml]
        except Exception as error_message_when_exporting_csv_data:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message=f"Error al exportar los datos xml al archivo > {csv_file_name}",
                error_message_from_method=error_message_when_exporting_csv_data))

    @staticmethod
    def select_random_item(list_data: list) -> list:
        """ Este método se diseñó para genera datos aleatorio de una lista que recibe.

        Args:
            list_data (list): Lista con datos para poder seleccionar un dato alzar.

        Returns:
            list: Una lista con un valor alzar
        """
        random_index = random.randrange(0, len(list_data))
        return list_data[random_index]

    def select_keys_and_random_values(self, data_list_csv: list, amount: int) -> None:
        """ Este método se diseñó para seleccionar las llaves y valores al azar.

        Args:
            data_list_csv (list): Lista con todas las llaves y valores.
            amount (int): Número de datos a buscar.
        """
        try:
            flag = True
            count = 0
            print(config['TITLE_KEY_VALUE'])
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
            print(messages.print_error(
                programmer_error_message=f"Error al intentar seleccionar las llaves y valores.",
                error_message_from_method=error_message_select_random_days))

    @staticmethod
    def compare_lists_of_data(master_list: list, data_list_two: list) -> list:
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
        except Exception as error_in_comparing_lists:
            print(messages.print_error(
                programmer_error_message="Al compara la lista de datos",
                error_message_from_method=error_in_comparing_lists))
