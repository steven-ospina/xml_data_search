import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM
from copy import deepcopy
import os


class Xml:
    """
    Está clase esta diseñada para poder trabajar con los archivos XML

    Attributes:
    ----------
        write_method (string): Esté atributo se utiliza para guardar la palabra "w" que se significa write.

    Methods:
    -------
        write_file_xml()-> str:
        get_xml_data_list(xml_file_name: str) -> list:
        search_the_index_in_the_list(data_list_csv: list, data_list_xml: list) -> list:
        build_xml(xml_file_name: str, name_of_the_new_xml_file: str, data_index_xml: list) -> None:
        build_root_xml(xml_file_name: str):
        check_and_format_xml(xml_file_name: str) -> None:
        remove_xml_values(xml_file_name: str, data_index_xml: list) -> None:
        print_error_xml(mesaage_error_method: str, message: Exception) -> None:
    """
    def __init__(self):
        """ El constructor de la clase Xml
        """
        self.write_method: str = 'w'

    # Método encargado de escribir los archivos en el sistema
    def write_file_xml(self) -> str:
        """ Este método se diseñó para que el usuario puede ingrear el nombre del,
            archivo xml por consola.

        Returns:
            str: Retornará el nombre que el usuario haya elegido.
        """
        print("Recuerda poner al final del nombre la extensión *.xml")
        xml_file_name = str(input(f"Nombre del archivo\n:"))
        try:
            answer = str(input(f"El nombre del archivo es: {xml_file_name} \n [si] o [no]\n:"))
            if answer.lower() == 'si':
                return xml_file_name
            else:
                print('El nombre del archivo es incorrecto\n')
        except ValueError as error:
            self.print_error_xml(mesaage_error_method="Al crear el nombre del archivo xml", message=error)

    # Método para buscar los todos los números de estado de cuenta en el xml a consular
    def get_xml_data_list(self, xml_file_name: str) -> list:
        """ Este método se diseñó para poder leer todas los estados de cuenta que tiene el archivo xml,
            con el que se esté trabajando.

        Args:
            xml_file_name (str): Nombre del archivo xml con el cual se esté trabajando.

        Returns:
            list: Una lista con todos los estados de cuenta que estén en el archivo xml.
        """
        try:
            root = ET.parse(xml_file_name).getroot()
            data_list_xml = [item.find('ESTADOCUENTA').text for item in root.findall(f"./OBLIGACION/ENCABEZADO")]

            return data_list_xml
        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"Al buscar los estados de cuenta en el archivo xml: {xml_file_name}", message=error)

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
            data_index_xml = [data_list_xml.index(item) for item in data_list_csv]
            return data_index_xml
        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"Al buscar el index en el xml, puede ser que los datos en el CSV tengan un espacio, o el dato no exista en el xml {data_list_csv}", message=error)

    # Método encargado de consultar y construir todos los datos del xml
    def build_xml(self, xml_file_name: str, name_of_the_new_xml_file: str, data_index_xml: list) -> None:
        """ Este método se diseñó para poder construir el documento final donde estara todos los datos,
            que se necesiten en xml.

        Args:
            xml_file_name (str): Nombre del archivo xml donde esta toda la información que se va a trabajar.
            name_of_the_new_xml_file (str): Nombre del archivo xml donde se almacenara toda la información.
            data_index_xml (list): Lista de los índices de los estados de cuenta que se van a copiar.
        """
        try:
            tree = self.build_root_xml(xml_file_name=name_of_the_new_xml_file)
            root_source_file = ET.parse(xml_file_name).getroot()
            counter = 0
            obligacion_source_file = [root_source_file[value] for value in data_index_xml]
            obligacion_copy = [deepcopy(value) for value in obligacion_source_file]
            for value in obligacion_copy:
                tree.append(value)
                counter = counter + 1
                print(f"Datos cargando: {counter}", end="\r")

            ET.ElementTree(tree).write(name_of_the_new_xml_file, encoding="UTF-8", xml_declaration=True)

            print(f"\nTotal datos: [{counter}] escritos en el archivo: {name_of_the_new_xml_file}\n")
        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"Al crear el archivo final xml: {name_of_the_new_xml_file}", message=error)

    # Método para crear la root de archivo xml
    def build_root_xml(self, xml_file_name: str):
        """ Este método se diseñó para poder agregar el root al archivo xml nuevo que se va a crear.

        Args:
            xml_file_name (str): Nombre del archivo que tendra los nuevos datos.

        Returns:
            [list]: El retorna una especie de lista con las que se pueden agregar los datos al nuevo,
                     archivo xml.
                     <class 'xml.etree.ElementTree.Element'>
        """
        try:
            ESTADODECUENTA = ET.Element('ESTADODECUENTA')
            ET.ElementTree(ESTADODECUENTA).write(xml_file_name, encoding="UTF-8", xml_declaration=True)
            return ET.parse(xml_file_name).getroot()
        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"No se pudo crear root del archivo: {xml_file_name}", message=error)

    # Método para chequear y dar formato al archivo xml
    def check_and_format_xml(self, xml_file_name: str) -> None:
        """ Este método se diseñó para poder chequear que el archivo esté formateado; si no está formateado,
            con este método podrás dar formato al archivo xml y que el usuario y el sistema lo pueda leer.

        Args:
            xml_file_name (str): Nombre del archivo xml

        Returns:
            [formatted file or message]: Retornara un archivo formateado o solo mandara un mensaje que indique,
                                         que el archivo ya está formateado.
        """
        try:
            with open(xml_file_name) as check_xml:
                reader = check_xml.readline()
                check_format = "\n" in reader
                if check_format is not True:
                    with open(xml_file_name) as xmldata:
                        print(f"Formateando el archivo {xml_file_name}")
                        xml = DOM.parseString(xmldata.read())
                        xml_pretty_byte = xml.toprettyxml(encoding="utf-8")
                        # Convertir bytes en una cadena y eliminar el extraño problema de la nueva línea
                        xml_pretty_str = os.linesep.join([item for item in xml_pretty_byte.decode("utf-8").splitlines() if item.strip()])
                        # Formatear el archivo xml
                        with open(xml_file_name, self.write_method) as file_out:
                            file_out.write(xml_pretty_str)
                else:
                    return print("El archivo ya esta formateado")
        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"No se pudo formatear el archivo xml {xml_file_name}", message=error)

    # Método para borra datos del archivo xml
    def remove_xml_values(self, xml_file_name: str, data_index_xml: list) -> None:
        """ Este método se diseñó para poder remover datos que el usuario quiera eliminar de un archivo xml

        Args:
            xml_file_name (str): Nombre del archivo xml con el que se va a trabajar.
            data_index_xml (list): Lista de los índices de los estados de cuenta que se van a eliminar.
        """
        try:
            root_file_xml = ET.parse(xml_file_name).getroot()
            value_to_remove = [root_file_xml[value] for value in data_index_xml]
            counter = 0
            for value in value_to_remove:
                root_file_xml.remove(value)
                counter = counter + 1
                print(f"Datos eliminados: {counter}", end="\r")

            ET.ElementTree(root_file_xml).write(xml_file_name, encoding="UTF-8", xml_declaration=True)
            print(f"\nTotal datos eliminados: [{counter}] del archivo: {xml_file_name}\n")

        except Exception as error:
            self.print_error_xml(mesaage_error_method=f"Al intentar eliminar los elementos del archivo xml: {xml_file_name}", message=error)

    # Método para imprimir errores del archivo xml
    def print_error_xml(self, mesaage_error_method: str, message: Exception) -> None:
        """ Este método se diseñó para imprimir en consola los errores que ocurren en la clase Xml y terminar de correr la aplicación

        Args:
            mesaage_error_method (str): Mensaje indicando el error que pudo haber pasado.
            message (Exception): Mensaje de error que describe lo que paso, esto lo genera el try except.
        """
        print(f"ERROR: {mesaage_error_method}")
        exit(f"ERROR: {message}")
