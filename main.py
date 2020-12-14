# from modules.searchData import Data
from app.Menu import Menu
from sys import argv


def run():
    flag_format = "-f"
    flag_export = "-e"
    flag_remove_value_in_xml = "-r"
    arguments_length = len(argv)

    # menu = Menu

    if arguments_length >= 4:
        if flag_export in argv:
            # export_csv = Data().export_data_csv_arguments(argv)
            Menu.export_data_csv_arguments(argv)
        elif flag_remove_value_in_xml in argv:
            # remove_value_in_xml = Data().remove_xml_values_with_arguments(argv)
            Menu.remove_xml_values_with_arguments(argv)
        else:
            # build_arguments = Data().build_xml_with_arguments(argv)
            Menu.build_xml_with_arguments(argv)
    elif arguments_length >= 3:
        if flag_format in argv:
            # format_xml = Data().format_xml_with_arguments(argv)
            Menu.format_xml_with_arguments(argv)
    elif arguments_length > 1:
        # message_help = Data().print_message_help()
        Menu.print_message_help()
    else:
        # message = Data().print_message()
        Menu.print_message()
        # menu = Data().menu()
        Menu.menu()


if __name__ == '__main__':
    run()
