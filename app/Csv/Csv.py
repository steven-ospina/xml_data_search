# from ..Archive import Archive
import csv


class Csv():

    def __init__(self):
        self.data_array_csv = []
        self.read_method = 'r'
        self.write_method = 'w'
        # super().__init__()

    # Método encargado de leer los datos que están en el archivo csv
    def get_csv_data_list(self, name_file):
        try:
            with open(name_file, self.read_method) as (File):
                reader = csv.reader(File)
                self.data_array_csv = [''.join(item) for item in reader if item]
                print(f"\nTotal datos csv: {len(self.data_array_csv)}\n")
        except Exception as error:
            print('No se pudo cargar los datos del csv', error)

        return self.data_array_csv

    # Método para exportar los estados de cuenta a un archivo csv
    def export_data_csv(self, data_array_xml, name_file_csv):
        try:
            with open(name_file_csv, self.write_method, newline='') as csvfile:
                csvwriter = csv.writer(csvfile)
                for data in data_array_xml:
                    csvwriter.writerow([data])
        except Exception as error:
            print(f"Error al exportar los datos xml a csv: {error}")
