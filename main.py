from modules.searchData import Data

def run():
    menu = Data().menu()

if __name__ == '__main__':
    print('B I E N V E N I D O\n')
    print('Nota: verifica que en directorio del proyecto estén los archivos:')
    print('[*.csv y *.xml]')
    print('[Los datos del csv deben estar en una sola columna y solo numeros]')
    print('[cargar un archivo csv y xml a la ves]\n')
    run()