from .Csv import Csv
import traceback


def search_all_stowaways(csv_file_bd: str, csv_file_compare: str) -> None:
    """
    Args:
        csv_file_bd (): Archivo CSV con los datos principales a comparar.
        csv_file_compare (): Archivo CSV con los dato que pueden tener un polizón.

    Returns: None
    """
    try:
        csv = Csv()
        list_bd = csv.get_csv_data_list(csv_file_bd)
        list_compare = csv.get_csv_data_list(csv_file_compare)
        set_difference = set(list_compare) - set(list_bd)
        list_difference = list(set_difference)
        if any(list_difference):
            print('Datos encontrados:')
            print(' , '.join(list_difference))
        else:
            print('No se encontraron datos :(')
    except Exception as error:
        print(f'uncaught exception {traceback.format_exc()}')
        print('No se pudo encontrar el dato único.')
        print(error)
