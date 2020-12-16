# from ..Archive import Archive
import xml.etree.ElementTree as ET
import xml.dom.minidom as DOM
from copy import deepcopy
import os


class Xml():

    def __init__(self):
        self.data_array_xml = []
        self.data_index_xml = []
        self.name_file_xml = ""
        self.write_method = 'w'

    # Método encargado de escribir los archivos en el sistema
    def write_file_xml(self):
        print("Recuerda poner al final del nombre la extensión *.xml")
        self.name_file_xml = str(input(f"Nombre del archivo\n:"))
        try:
            answer = str(input(f"El nombre del archivo es: {self.name_file_xml} \n [si] o [no]\n:"))
            if answer.lower() == 'si':
                self.name_file_xml = self.name_file_xml
            else:
                print('El nombre del archivo es incorrecto\n')
        except ValueError as error:
            self.print_error_xml(mesaage_error_methodo="Al crear el nombre del archivo xml", message=error)

        return self.name_file_xml

    # Método para buscar los todos los números de estado de cuenta en el xml a consular
    def xml_data_list(self, name_file):
        try:
            root = ET.parse(name_file).getroot()
            self.data_array_xml = [item.find('ESTADOCUENTA').text for item in root.findall(f"./OBLIGACION/ENCABEZADO")]
            print(f"\nTotal estados de cuenta xml: {len(self.data_array_xml)}")

            return self.data_array_xml
        except Exception as error:
            self.print_error_xml(mesaage_error_methodo=f"Al buscar los estados de cuenta en el archivo xml: {name_file}", message=error)

    # Método encargado de buscar el index en la lista de los datos consultados en el xml
    def search_the_index_in_the_list(self, data_array_csv, data_array_xml):
        try:
            self.data_index_xml = [data_array_xml.index(item) for item in data_array_csv]
            print(f"\nTotal indexes encontrados: {len(self.data_index_xml)}\n")
        except Exception as error:
            self.print_error_xml(mesaage_error_methodo=f"Al buscar el index en el xml, puede ser que los datos en el CSV tengan un espacio, o el dato no exista en el xml {data_array_csv}", message=error)

        return self.data_index_xml

    # Método encargado de consultar y construir todos los datos del xml
    def build_xml(self, name_file, name_file_xml, data_index_xml):
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

            root_fie_new = ET.ElementTree(tree).write(name_file_xml, encoding="UTF-8", xml_declaration=True)
        except Exception as error:
            self.print_error_xml(mesaage_error_methodo=f"Al crear el archivo final xml: {name_file_xml}", message=error)

        print(f"\nTotal datos: [{len(self.data_index_xml)}] escritos en el archivo: {name_file_xml}\n")
        # self.name_file = ""

    # Método para crear la root de archivo xml
    def build_root_xml(self, name_file_xml):
        try:
            ESTADODECUENTA = ET.Element('ESTADODECUENTA')
            ET.ElementTree(ESTADODECUENTA).write(name_file_xml, encoding="UTF-8", xml_declaration=True)
            return ET.parse(name_file_xml).getroot()
        except Exception as error:
            self.print_error_xml(mesaage_error_methodo=f"No se pudo crear root del archivo: {name_file_xml}", message=error)

    # Método para chequear y dar formato al archivo xml
    def check_and_format_xml(self, name_file_xml):
        try:
            with open(name_file_xml) as check_xml:
                reader = check_xml.readline()
                check_format = "\n" in reader
                if(check_format is not True):
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
            self.print_error_xml(mesaage_error_methodo=f"No se pudo formatear el archivo xml {name_file_xml}", message=error)

    # Método para borra datos del archivo xml
    def remove_xml_values(self, name_file, data_index_xml):
        try:
            root_file_xml = ET.parse(name_file).getroot()
            value_to_remove = [root_file_xml[value] for value in data_index_xml]
            counter = 0
            for value in value_to_remove:
                root_file_xml.remove(value)
                counter = counter + 1
                print(f"Datos eliminados: {counter}", end="\r")

            update_file_xml = ET.ElementTree(root_file_xml).write(name_file, encoding="UTF-8", xml_declaration=True)
            print(f"\nTotal datos eliminados: [{len(self.data_index_xml)}] del archivo: {name_file}\n")

        except Exception as error:
            self.print_error_xml(mesaage_error_methodo=f"Al intentar eliminar los elementos del archivo xml: {name_file}", message=error)

    # Método para imprimir errores del archivo xml
    def print_error_xml(self, mesaage_error_methodo, message):
        print(f"ERROR: {mesaage_error_methodo}")
        exit(f"ERROR: {message}")
