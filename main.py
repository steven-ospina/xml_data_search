from modules.searchData import Data
from sys import argv


def run():
    arguments_lent= len(argv)

    if arguments_lent >= 4:
        bulid_arguments = Data().build_xml_with_arguments(argv)
    elif arguments_lent > 1:
        message_help = Data().print_message_help()
    else:
        message = Data().print_message()
        menu = Data().menu()


if __name__ == '__main__':
    run()