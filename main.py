from inspect import signature
from typing import Optional, List
from app.Menu.Menu import Menu
import argparse

menu = Menu()


class StartApp:
    """ Clase para iniciar la aplicación.
    """

    @staticmethod
    def get_arguments() -> dict:
        my_parser = argparse.ArgumentParser(
            description='Aplicación para trabajar con archivos XML y CSV',
            epilog='Espero que con esta aplicación pueda ahorrarte tiempo.',
            allow_abbrev=False)

        my_parser.version = '1.15.20'
        my_parser.add_argument('-version', '-v', action='version')
        my_parser.add_argument(
            '-clone', '-c',
            nargs=3,
            metavar=('sample-CSV.csv', 'sample-XML.xml', 'name-of-new-XML-file.xml'),
            help="Buscara los datos que le indiquen en el CSV y lo exportara en uno nuevo archivo XML.",
            default=False)
        my_parser.add_argument(
            '-format', '-f',
            nargs=1,
            metavar='XML-file-to-format.xml',
            help="Dar formato al archivo XML.",
            default=False)
        my_parser.add_argument(
            '-export', '-e',
            nargs=2,
            metavar=('sample-XML.xml', 'name-of-new-CSV-file.csv'),
            help="Exportar los datos del XML al archivo CSV que le indiquen.",
            default=False)
        my_parser.add_argument(
            '-remove', '-r',
            nargs=2,
            metavar=('sample-CSV.csv', 'sample-XML.xml'),
            help="Eliminar datos del archivo XML indicando los datos en el archivo CSV.",
            default=False)
        my_parser.add_argument(
            '-random-access-value', '-rav',
            nargs=2,
            metavar=('sample-key-value.csv', 'number <- int'),
            help="Seleccionar llaves y valores al azar indicando la cantidad que necesite.",
            default=False)
        my_parser.add_argument(
            '-export-csv', '-ec',
            nargs=1,
            metavar='PATH-DIRECTORY',
            help="Exportar los datos que tengan los archivos XML en el directorio, que le indiquen, y luego los "
                 "exporta en archivos CSV.",
            default=False)
        my_parser.add_argument(
            '-export-xml', '-ex',
            nargs=2,
            metavar=('PATH-DIRECTORY', 'sample-csv.csv'),
            help="Exportar N cantidad de archivos XML del directorio, especificado, y especificando los datos a "
                 "exportar en el archivo CSV.",
            default=False)
        my_parser.add_argument(
            '-export-all', '-ea',
            nargs=2,
            metavar=('PATH-DIRECTORY', 'name-of-new-CSV-file.csv'),
            help="Exportar un solo archivo CSV con N cantidad de datos, de archivos XML del directorio especificado.",
            default=False)
        my_parser.add_argument(
            '-merge-csv-files', '-mcf',
            nargs=2,
            metavar=('PATH-DIRECTORY', 'name-of-new-CSV-file.csv'),
            help="Unir N cantidad de archivos CSV del directorio, especificado.",
            default=False)
        my_parser.add_argument(
            '-search-data', '-sd',
            nargs=2,
            metavar=('PATH-DIRECTORY', 'DATA-TO_SEARCH'),
            help="Lee N cantidad de archivos XML y buscar un el dato que le indique.",
            default=False)
        my_parser.add_argument(
            '-compare', '-C',
            nargs=2,
            metavar=('FIRST-CSV-FILE.csv', 'SECOND-CSV-FILE.csv'),
            help="Comparar dos lista de datos CSV y exporta datos duplicados a archivo CSV.",
            default=False)
        my_parser.add_argument(
            '-manual', '-man',
            help="Manual que explica las posiciones de los argumentos.",
            action='store_true',
            default=False)
        args = my_parser.parse_args()
        dict_args = vars(args)
        return dict_args

    @staticmethod
    def filter_values(dictionary: dict) -> list:
        convert_to_list = list(dictionary.values())
        return list(filter(lambda values: values is not False, convert_to_list))

    @staticmethod
    def get_the_dictionary_key(dictionary: dict, search) -> list:
        return [key for key, value in dictionary.items() if value == search]

    @staticmethod
    def menu_method(select_method: str, value: Optional[List[str]]) -> None:
        choose = {
            'clone': menu.build_xml_with_arguments,
            'format': menu.format_xml_with_arguments,
            'export': menu.export_data_csv_arguments,
            'remove': menu.remove_xml_values_with_arguments,
            'random_access_value': menu.print_random_days,
            'export_csv': menu.exporting_multiple_csv_files,
            'export_xml': menu.export_multiple_xml_files,
            'export_all': menu.export_csv_data_united,
            'compare': menu.lists_of_data_to_compare,
            'merge_csv_files': menu.merge_csv_files,
            'search_data': menu.search_data_with_parameters,
            'manual': menu.print_message_help
        }
        select = choose.get(select_method, "Method not found.")
        method_length = signature(select)
        if len(method_length.parameters):
            select(value)
        else:
            select.__call__()


if __name__ == '__main__':
    get_dictionary = StartApp.get_arguments()
    get_value = StartApp.filter_values(dictionary=get_dictionary)
    if get_value:
        get_key = StartApp.get_the_dictionary_key(dictionary=get_dictionary, search=get_value[0])
        StartApp.menu_method(select_method=get_key[0], value=get_value[0])
    else:
        menu.menu()
