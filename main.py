from app.Menu.Menu import Menu
from sys import argv


def run():
    """Está función está diseñada y encargada de correr la aplicación.
    """
    flag_format: str = "-f"
    flag_export: str = "-e"
    flag_remove_value_in_xml: str = "-r"
    flag_random_access_value: str = "-rav"
    flag_export_csv_files: str = "-export-csv"
    flag_to_export_a_single: str = "-export-all"
    flag_export_xml_files: str = "-export-xml"
    flag_compare_lists: str = "-compare"
    flag_merge_csv_files: str = "-merge-csv-files"
    flag_search_data: str = "-sd"
    arguments_length: int = len(argv)

    menu = Menu()

    if arguments_length >= 3:
        if flag_export in argv:
            menu.export_data_csv_arguments(arg_list=argv)
        elif flag_export_csv_files in argv:
            menu.exporting_multiple_csv_files(arg_list=argv)
        elif flag_export_xml_files in argv:
            menu.export_multiple_xml_files(arg_list=argv)
        elif flag_to_export_a_single in argv:
            menu.export_csv_data_united(arg_list=argv)
        elif flag_merge_csv_files in argv:
            menu.merge_csv_files(arg_list=argv)
        elif flag_random_access_value in argv:
            menu.print_random_days(arg_list=argv)
        elif flag_compare_lists in argv:
            menu.lists_of_data_to_compare(arg_list=argv)
        elif flag_remove_value_in_xml in argv:
            menu.remove_xml_values_with_arguments(arg_list=argv)
        elif flag_format in argv:
            menu.format_xml_with_arguments(arg_list=argv)
        elif flag_search_data in argv:
            menu.search_data_with_parameters(arg_list=argv)
        else:
            menu.build_xml_with_arguments(arg_list=argv)
    elif arguments_length > 1:
        menu.print_message_help()
    else:
        menu.print_message()
        menu.menu()


if __name__ == '__main__':
    run()
