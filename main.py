from app.Menu.Menu import Menu
from sys import argv


def run():
    """Esta función está diseñada y en encargada para poder correr ejecutar la aplicación.
    """
    flag_format: str = "-f"
    flag_export: str = "-e"
    flag_remove_value_in_xml: str = "-r"
    flag_random_access_value: str = "-rav"
    arguments_length: int = len(argv)

    menu = Menu()

    if arguments_length >= 4:
        if flag_export in argv:
            menu.export_data_csv_arguments(arg_list=argv)
        elif flag_random_access_value in argv:
            menu.print_random_days(arg_list=argv)
        elif flag_remove_value_in_xml in argv:
            menu.remove_xml_values_with_arguments(arg_list=argv)
        else:
            menu.build_xml_with_arguments(arg_list=argv)
    elif arguments_length >= 3:
        if flag_format in argv:
            menu.format_xml_with_arguments(arg_list=argv)
    elif arguments_length > 1:
        menu.print_message_help()
    else:
        menu.print_message()
        menu.menu()


if __name__ == '__main__':
    run()
