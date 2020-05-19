from modules.searchData import Data


def run():
    message = Data().print_message()
    menu = Data().menu()

if __name__ == '__main__':
    run()