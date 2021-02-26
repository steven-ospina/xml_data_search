import csv


class Csv:
    """
    Está clase esta diseñada para poder trabajar con los archivos CSV

    Attributes:
        data_list_csv (): Esté atributo se utiliza para guadar la lista de los números de estados de cuenta
        read_method (): Esté atributo se utiliza para guardar la palabra "r" que se significa read.
        write_method (): Esté atributo se utiliza para guardar la palabra "w" que se significa write.

    """
    def __init__(self):
        """ El constructor de la clase Xml
        """
        self.data_list_csv: list = []
        self.read_method: str = 'r'
        self.write_method: str = 'w'

    # Método encargado de leer los datos que están en el archivo csv
    def get_csv_data_list(self, name_file: str) -> list:
        """ Este método se diseñó para poder leer los archivo csv y poder guadar los número de estados de cuenta,
            en una lista.

        Args:
            name_file (str): Nombre del archivo csv con el cual se esté trabajando.

        Returns:
            list: Una lista con los números de estados de cuenta.
        """
        try:
            with open(name_file, self.read_method) as (File):
                reader = csv.reader(File)
                self.data_list_csv = [''.join(item) for item in reader if item]
                print(f"\nTotal datos csv: {len(self.data_list_csv)}\n")
        except Exception as error:
            self.print_error_csv(mesaage_error_method=f"No se pudo cargar los datos del archivo csv : {name_file}", message=error)

        return self.data_list_csv

    # Método para exportar los estados de cuenta a un archivo csv
    def export_data_csv(self, data_list_xml: list, name_file_csv: str) -> None:
        """ Este método se diseñó para poder exportar todos números de estados de cuenta que estén en archivo xml.

        Args:
            data_list_xml (list): Lista con todos los números de estados de cuenta.
            name_file_csv (str): Nombre del archivo csv en donde se guardara la información.
        """
        try:
            with open(name_file_csv, self.write_method, newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                for data in data_list_xml:
                    csvwriter.writerow([data])
        except Exception as error:
            self.print_error_csv(mesaage_error_method=f"Error al exportar los datos xml al archivo :{name_file_csv}", message=error)

    # Método para imprimir errores del archivo Csv
    def print_error_csv(self, mesaage_error_method: str, message: Exception) -> None:
        """ Este método se diseñó para imprimir en consola los errores que ocurren en la clase Csv y terminar de correr la aplicación

        Args:
            mesaage_error_method (str): Mensaje indicando el error que pudo haber pasado.
            message (Exception): Mensaje de error que describe lo que paso, esto lo genera el try except.
        """
        print(f"ERROR: {mesaage_error_method}")
        exit(f"ERROR: {message}")
