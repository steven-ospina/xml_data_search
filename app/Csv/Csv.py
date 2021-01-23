# from ..Archive import Archive
import csv


class Csv:

    def __init__(self):
        self.data_list_csv: list = []
        self.read_method: str = 'r'
        self.write_method: str = 'w'

    # Método encargado de leer los datos que están en el archivo csv
    def get_csv_data_list(self, name_file: str) -> list:
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
        try:
            with open(name_file_csv, self.write_method, newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                for data in data_list_xml:
                    csvwriter.writerow([data])
        except Exception as error:
            self.print_error_csv(mesaage_error_method=f"Error al exportar los datos xml al archivo :{name_file_csv}", message=error)

    # Método para imprimir errores del archivo Csv
    def print_error_csv(self, mesaage_error_method: str, message: Exception) -> None:
        print(f"ERROR: {mesaage_error_method}")
        exit(f"ERROR: {message}")
