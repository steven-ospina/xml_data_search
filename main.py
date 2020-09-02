from modules.searchData import Data
from sys import argv


def run():
    arguments_length = len(argv)

    if arguments_length >= 4:
        build_arguments = Data().build_xml_with_arguments(argv)
    elif arguments_length > 1:
        message_help = Data().print_message_help()
    else:
        message = Data().print_message()
        menu = Data().menu()


if __name__ == '__main__':
    run()
