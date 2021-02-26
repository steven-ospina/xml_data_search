import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM
from copy import deepcopy
import os


class Xml:
    """
    Está clase esta diseñada para poder trabajar con los archivos XML

    Attributes:
        data_list_xml (list): Esté atributo se utiliza para guardar una lista con todas la información,
                              estén en la etiqueta OBLIGACION del archivo xml.
        data_index_xml (list): Esté atributo se utiliza para guardar los índices de los datos que están,
                               en la lista data_list_xml.
        name_file_xml (string): Esté atributo se utiliza guardar el nombre del archivo xml.
        write_method (string): Esté atributo se utiliza para guardar la palabra "w" que se significa write.
    """
    def __init__(self):
        """ El constructor de la clase Xml
        """
        self.data_list_xml: list = []
        self.data_index_xml: list = []
        self.name_file_xml: str = ""
        self.write_method: str = 'w'

    # Método encargado de escribir los archivos en el sistema
    def write_file_xml(self) -> str:
        """ Este método se diseñó para que el usuario puede ingrear el nombre del,
            archivo xml por consola.

        Returns:
            str: Retornará el nombre que el usuario haya elegido.
        """
        print("Recuerda poner al final del nombre la extensión *.xml")
        self.name_file_xml = str(input(f"Nombre del archivo\n:"))
        try:
            answer = str(input(f"El nombre del archivo es: {self.name_file_xml} \n [si] o [no]\n:"))
            if answer.lower() == 'si':
                self.name_file_xml = self.name_file_xml
            else:
                print('El nombre del archivo es incorrecto\n')
        except ValueError as error:
            self.print_error_xml(mesaage_error_method="Al crear el nombre del archivo xml", message=error)

        return self.name_file_xml

    # Método para buscar los todos los números de estado de cuenta en el xml a consular
    def get_xml_data_list(self, name_file: str) -> list:
        """ Este método se diseñó para poder leer todas los estados de cuenta que tiene el archivo xml,
            con el que se esté trabajando.

        Args:
            name_file (str): Nombre del archivo xml con el cual se esté trabajando.

        Returns:
            list: Una lista con todos los estados de cuenta que estén en el archivo xml.
        """
        try:
            root = ET.parse(name_file).getroot()
            self.data_list_xml = [item.find('ESTADOCUENTA').text for item in root.findall(f"./OBLIGACION/ENCABEZADO")]
            print(f"\nTotal estados de cuenta xml: {len(self.data_list_xml)}")

            return self.data_list_xml
        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"Al buscar los estados de cuenta en el archivo xml: {name_file}", message=error)

    # Método encargado de buscar el index en la lista de los datos consultados en el xml
    def search_the_index_in_the_list(self, data_list_csv: list, data_list_xml: list) -> list:
        """ Este método se diseñó para buscar los índices de los estados de cuenta con lo que se van,
            a trabajar.

        Args:
            data_list_csv (list): Lista de los números de estados de cuenta con lo que se estén trabajando.
            data_list_xml (list): Lista con todos los datos que tiene el xml.

        Returns:
            list: Una lista de índices para poder buscar más rápido los datos con los que se estén trabajando.
        """
        try:
            self.data_index_xml = [data_list_xml.index(item) for item in data_list_csv]
            print(f"\nTotal indexes encontrados: {len(self.data_index_xml)}\n")
        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"Al buscar el index en el xml, puede ser que los datos en el CSV tengan un espacio, o el dato no exista en el xml {data_list_csv}", message=error)

        return self.data_index_xml

    # Método encargado de consultar y construir todos los datos del xml
    def build_xml(self, name_file: str, name_file_xml: str, data_index_xml: list) -> None:
        """ Este método se diseñó para poder construir el documento final donde estara todos los datos,
            que se necesiten en xml.

        Args:
            name_file (str): Nombre del archivo xml donde esta toda la información que se va a trabajar.
            name_file_xml (str): Nombre del archivo xml donde se almacenara toda la información.
            data_index_xml (list): Lista de los índices de los estados de cuenta que se van a copiar.
        """
        try:
            tree = self.build_root_xml(name_file_xml)
            root_source_file = ET.parse(name_file).getroot()
            counter = 0
            obligacion_source_file = [root_source_file[value] for value in data_index_xml]
            obligacion_copy = [deepcopy(value) for value in obligacion_source_file]
            for value in obligacion_copy:
                tree.append(value)
                counter = counter + 1
                print(f"Datos cargando: {counter}", end="\r")

            ET.ElementTree(tree).write(name_file_xml, encoding="UTF-8", xml_declaration=True)
        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"Al crear el archivo final xml: {name_file_xml}", message=error)

        print(f"\nTotal datos: [{len(self.data_index_xml)}] escritos en el archivo: {name_file_xml}\n")
        # self.name_file = ""

    # Método para crear la root de archivo xml
    def build_root_xml(self, name_file_xml: str):
        """ Este método se diseñó para poder agregar el root al archivo xml nuevo que se va a crear.

        Args:
            name_file_xml (str): Nombre del archivo que tendra los nuevos datos.

        Returns:
            [Lista]: El retorna una especie de lista con las que se pueden agregar los datos al nuevo,
                     archivo xml.
                     <class 'xml.etree.ElementTree.Element'>
        """
        try:
            ESTADODECUENTA = ET.Element('ESTADODECUENTA')
            ET.ElementTree(ESTADODECUENTA).write(name_file_xml, encoding="UTF-8", xml_declaration=True)
            return ET.parse(name_file_xml).getroot()
        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"No se pudo crear root del archivo: {name_file_xml}", message=error)

    # Método para chequear y dar formato al archivo xml
    def check_and_format_xml(self, name_file_xml: str) -> None:
        """ Este método se diseñó para poder chequear que el archivo esté formateado; si no está formateado,
            con este método podrás dar formato al archivo xml y que el usuario y el sistema lo pueda leer.

        Args:
            name_file_xml (str): Nombre del archivo xml

        Returns:
            [formatted file or message]: Retornara un archivo formateado o solo mandara un mensaje que indique,
                                         que el archivo ya está formateado.
        """
        try:
            with open(name_file_xml) as check_xml:
                reader = check_xml.readline()
                check_format = "\n" in reader
                if check_format is not True:
                    with open(name_file_xml) as xmldata:
                        print(f"Formateando el archivo {name_file_xml}")
                        xml = DOM.parseString(xmldata.read())
                        xml_pretty_byte = xml.toprettyxml(encoding="utf-8")
                        # Convertir bytes en una cadena y eliminar el extraño problema de la nueva línea
                        xml_pretty_str = os.linesep.join([item for item in xml_pretty_byte.decode("utf-8").splitlines() if item.strip()])
                        # Formatear el archivo xml
                        with open(name_file_xml, self.write_method) as file_out:
                            file_out.write(xml_pretty_str)
                else:
                    return print("El archivo ya esta formateado")
        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"No se pudo formatear el archivo xml {name_file_xml}", message=error)

    # Método para borra datos del archivo xml
    def remove_xml_values(self, name_file: str, data_index_xml: list) -> None:
        """ Este método se diseñó para poder remover datos que el usuario quiera eliminar de un archivo xml

        Args:
            name_file (str): Nombre del archivo xml con el que se va a trabajar.
            data_index_xml (list): Lista de los índices de los estados de cuenta que se van a eliminar.
        """
        try:
            root_file_xml = ET.parse(name_file).getroot()
            value_to_remove = [root_file_xml[value] for value in data_index_xml]
            counter = 0
            for value in value_to_remove:
                root_file_xml.remove(value)
                counter = counter + 1
                print(f"Datos eliminados: {counter}", end="\r")

            ET.ElementTree(root_file_xml).write(name_file, encoding="UTF-8", xml_declaration=True)
            print(f"\nTotal datos eliminados: [{len(self.data_index_xml)}] del archivo: {name_file}\n")

        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"Al intentar eliminar los elementos del archivo xml: {name_file}", message=error)

    # Método para imprimir errores del archivo xml
    def print_error_xml(self, mesaage_error_method: str, message: Exception) -> None:
        """ Este método se diseñó para imprimir en consola los errores que ocurren en la clase Xml y terminar de correr la aplicación

        Args:
            mesaage_error_method (str): Mensaje indicando el error que pudo haber pasado.
            message (Exception): Mensaje de error que describe lo que paso, esto lo genera el try except.
        """
        print(f"ERROR: {mesaage_error_method}")
        exit(f"ERROR: {message}")
