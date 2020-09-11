from modules.searchData import Data
from sys import argv


def run():
    flag_format = "-f"
    flag_export = "-e"
    arguments_length = len(argv)

    if arguments_length >= 4:
        if flag_export in argv:
            # print(f"encotrado {argv}")
            export_csv = Data().export_data_csv_arguments(argv)
        else:
            # pass
            build_arguments = Data().build_xml_with_arguments(argv)
    elif arguments_length >= 3:
        if flag_format in argv:
            format_xml = Data().format_xml_with_arguments(argv)
    elif arguments_length > 1:
        message_help = Data().print_message_help()
    else:
        message = Data().print_message()
        menu = Data().menu()


if __name__ == '__main__':
    run()
