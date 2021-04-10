import xml.etree.ElementTree as elementTree
import xml.dom.minidom as dom
import os
import traceback
from copy import deepcopy
from Config import Messages, Config

messages = Messages()
config = Config()
basename = config.basename
config_xml = config.yaml_configuration()


class Xml:
    """
    Está clase está diseñada para poder trabajar con los archivos XML.

    Attributes:
    ----------
        write_method (string): Esté atributo se utiliza para guardar la palabra "w",
        que se significa write.

    Methods:
    -------
        write_file_xml()-> str
        get_xml_data_list(xml_file_name: str) -> list
        search_the_index_in_the_list(data_list_csv: list, data_list_xml: list) -> list
        build_xml(xml_file_name: str, name_of_the_new_xml_file: str, data_index_xml: list) -> None
        _build_root_xml(xml_file_name: str) -> elementTree.Element:
        check_and_format_xml(xml_file_name: str) -> None
        remove_xml_values(xml_file_name: str, data_index_xml: list) -> None
        get_the_root_of_the_xml_file(xml_file: str) -> elementTree.Element:
        _copy_root_data_from_xml_file_private(root_xml_file: list, data_index_xml: list) -> list
        get_the_text_of_a_tag(xml_file_name: str) -> str:
        get_data_from_several_xml_files(path_of_archives: str) -> dict:
        recursive_filter_by_xml_files(path_of_archives: str) -> list:
        filter_data_in_xml_files(search: str, list_of_the_file_paths: list) -> dict:
        search_and_filter_data(self, data_dictionary: dict, data_list: list) -> tuple
    """
    def __init__(self):
        self.write_method: str = 'w'

    @staticmethod
    def write_file_xml() -> str:
        """ Este método se diseñó para que el usuario puede ingresar el nombre del,
            archivo XML por consola.

        Returns:
            str: Retornará el nombre que el usuario haya elegido.
        """
        print("Recuerda poner al final del nombre la extensión *.xml")
        xml_file_name = str(input("Nombre del archivo\n:"))
        try:
            answer = str(input(f"El nombre del archivo es: {xml_file_name} \n [si] o [no]\n:"))
            if answer.lower() == 'si':
                return xml_file_name
            else:
                print('El nombre del archivo es incorrecto\n')
        except ValueError as error_message_when_creating_file_name:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message="Al crear el nombre del archivo XML",
                error_message_from_method=error_message_when_creating_file_name))

    def get_xml_data_list(self, xml_file_name: str) -> list:
        """ Este método se diseñó para poder leer la etiqueta "TAG_TO_SEARCH" y la ruta "XML_DOM_PATH" que,
            está en el archivo configXML.yaml, y buscar en el archivo XML con el que se esté trabajando,
            los datos que quiera exportar el usuario.

        Args:
            xml_file_name (str): Nombre del archivo XML con el cual se esté trabajando.

        Returns:
            list: Una lista con todos datos de la etiqueta "TAG_TO_SEARCH" que estén en el archivo XML.
        """
        try:
            tag_to_search = config_xml['TAG_TO_SEARCH']
            xml_dom_path = config_xml['XML_DOM_PATH']
            root = self.get_the_root_of_the_xml_file(xml_file=xml_file_name)
            data_list_xml = [item.find(tag_to_search).text for item in root.findall(xml_dom_path)]
            return data_list_xml
        except Exception as error_in_getting_list_information:
            print(f"uncaught exception {traceback.format_exc()}")
            print_possible_errors = messages.print_messages_in_colors(
                "Posibles errores:",
                f"* El archivo {xml_file_name} no existe en el directorio, o no es un archivo XML.",
                "* La estructura del archivo XML no es conocida por la aplicación.",
                "* En el archivo 'configXML.yaml' están mal escritas las rutas o las etiquetas.",
                color='yellow')
            print(f"{print_possible_errors[0]}\n"
                  f"{print_possible_errors[1]}\n"
                  f"{print_possible_errors[2]}\n"
                  f"{print_possible_errors[3]}\n")
            print(messages.print_error(
                programmer_error_message=f"Al buscar los datos en el archivo xml > {xml_file_name}",
                error_message_from_method=error_in_getting_list_information))

    @staticmethod
    def search_the_index_in_the_list(data_list_csv: list, data_list_xml: list) -> list:
        """ Este método se diseñó para buscar los índices de los datos lo que se van,
            a trabajar.

        Args:
            data_list_csv (list): Lista de los datos CSV con lo que se estén trabajando.
            data_list_xml (list): Lista con todos los datos que tiene el XML.

        Returns:
            list: Una lista de índices para poder buscar más rápido los datos con los que se estén trabajando.
        """
        try:
            data_index_xml = [data_list_xml.index(item) for item in data_list_csv]
            return data_index_xml
        except Exception as error_message_for_list_indexes:
            # import pdb; pdb.set_trace()
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_messages_in_colors(
                "Verifica que el archivo CSV que no tenga datos erróneos o desconocidos.", color='yellow'))
            print(messages.print_error(
                programmer_error_message="Al buscar el índice en los datos XML," 
                                         "puede ser que los datos en el CSV tengan un espacio," 
                                         "o el dato no exista en el XML",
                error_message_from_method=error_message_for_list_indexes))

    def build_xml(self, xml_file_name: str, name_of_the_new_xml_file: str, data_index_xml: list) -> int:
        """ Este método se diseñó para poder construir el documento final donde estará todos los datos,
            que se necesiten en XML.

        Args:
            xml_file_name (str): Nombre del archivo XML donde esta toda la información que se va a trabajar.
            name_of_the_new_xml_file (str): Nombre del archivo XML donde se almacenara toda la información.
            data_index_xml (list): Lista de los índices de los datos que se van a copiar.
        """
        try:
            file_size_in_bit = os.stat(xml_file_name).st_size
            ten_million_bit = 10000000
            if file_size_in_bit > ten_million_bit:
                print(messages.print_messages_in_colors(
                    f"> El archivo → {basename(path_dir=xml_file_name)}" 
                    " es un poco pesado, puede demorarse unos segundos en crear el nuevo archivo XML.",
                    color='yellow'))
            tree = self._build_root_xml_private(xml_file_name=name_of_the_new_xml_file)
            root_source_file = self.get_the_root_of_the_xml_file(xml_file=xml_file_name)
            copy_data_from_xml_file = self._copy_root_data_from_xml_file_private(
                root_xml_file=root_source_file,
                data_index_xml=data_index_xml)
            total_data = [tree.append(value) for value in copy_data_from_xml_file]
            elementTree.ElementTree(tree).write(name_of_the_new_xml_file, encoding="UTF-8", xml_declaration=True)
            return len(total_data)
        except Exception as error_message_build_xml_file:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message=f"Al crear el archivo final XML → {name_of_the_new_xml_file}",
                error_message_from_method=error_message_build_xml_file))

    def _build_root_xml_private(self, xml_file_name: str) -> elementTree.Element:
        """ Este método se diseñó para poder agregar el root al archivo XML nuevo que se va a crear.

            NOTA: Esté método es privado, solo se debe utilizar en esta clase, si sé instancia por fuera de esta clase,
            puede que no trabaje correctamente o lance excepciones.

        Args:
            xml_file_name (str): Nombre del archivo que tendrá el nuevo root de datos.

        Returns:
            class: Él retorna una especie de lista con las que se pueden agregar los datos al nuevo,
            archivo xml.
            <class 'xml.etree.ElementTree.Element'>
        """
        try:
            root_xml = config_xml['ROOT_XML']
            root_tag = elementTree.Element(root_xml)
            elementTree.ElementTree(root_tag).write(xml_file_name, encoding="UTF-8", xml_declaration=True)
            root = self.get_the_root_of_the_xml_file(xml_file=xml_file_name)
            return root
        except Exception as error_message_of_building_root:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message=f"No se pudo crear root del archivo → {xml_file_name}",
                error_message_from_method=error_message_of_building_root))

    def check_and_format_xml(self, xml_file_name: str) -> None:
        """ Este método se diseñó para poder chequear que el archivo XML esté formateado; si no está formateado,
            con este método podrás dar formato al archivo XML y que el usuario y el sistema lo pueda leer.

        Args:
            xml_file_name (str): Nombre del archivo XML.

        Returns:
            [formatted file or message]: Retornara un archivo formateado o solo mandara un mensaje que indique,
            que el archivo ya está formateado.
        """
        try:
            with open(xml_file_name) as check_xml:
                reader = check_xml.readline()
                check_format = "\n" in reader
                if check_format is not True:
                    with open(xml_file_name) as xml_data:
                        print_file = messages.print_messages_in_colors(
                            "> Formateando el archivo →",
                            str(basename(path_dir=xml_file_name)), color1='blue', color2='yellow')
                        print(print_file[0], print_file[1])
                        xml = dom.parseString(xml_data.read())
                        xml_pretty_byte = xml.toprettyxml(encoding="utf-8")
                        # Convertir bytes en una cadena y eliminar el extraño problema de la nueva línea
                        xml_pretty_str = os.linesep.join([
                            item for item in xml_pretty_byte.decode("utf-8").splitlines() if item.strip()])
                        # Formatear el archivo xml
                        with open(xml_file_name, self.write_method) as file_out:
                            file_out.write(xml_pretty_str)
                else:
                    print(messages.print_messages_in_colors(
                        f"> El archivo → {basename(path_dir=xml_file_name)} ya está formateado.",
                        color='green'))
        except Exception as error_message_when_formatting_xml_file:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message=f"No se pudo formatear el archivo XML → {xml_file_name}",
                error_message_from_method=error_message_when_formatting_xml_file))

    def remove_xml_values(self, xml_file_name: str, data_index_xml: list) -> int:
        """ Este método se diseñó para poder remover datos que el usuario quiera eliminar de un archivo XML.

        Args:
            xml_file_name (str): Nombre del archivo XML con el que se va a trabajar.
            data_index_xml (list): Lista de los índices de los estados de cuenta que se van a eliminar.

        Returns:
            int: La cantidad de datos eliminados.
        """
        try:
            root_file_xml = self.get_the_root_of_the_xml_file(xml_file=xml_file_name)
            value_to_remove = [root_file_xml[value] for value in data_index_xml]
            remove_data = [root_file_xml.remove(value) for value in value_to_remove]
            elementTree.ElementTree(root_file_xml).write(xml_file_name, encoding="UTF-8", xml_declaration=True)
            return len(remove_data)
        except Exception as error_message_when_removing_values:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message=f"Al intentar eliminar los elementos del archivo XML → {xml_file_name}",
                error_message_from_method=error_message_when_removing_values))

    @staticmethod
    def get_the_root_of_the_xml_file(xml_file: str) -> elementTree.Element:
        """  Este método se diseñó para obtener el root de los archivos XML

        Args:
            xml_file (str): Recibe el nombre del archivo XML al que se le va a obtener el root.

        Returns:
            elementTree.Element: Retorna el root del archivo XML.
        """
        try:
            root = elementTree.parse(xml_file).getroot()
            return root
        except Exception as error_in_xml_root:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message=f"Al intentar obtener la raíz del archivo → {xml_file}",
                error_message_from_method=error_in_xml_root))

    @staticmethod
    def _copy_root_data_from_xml_file_private(root_xml_file: elementTree.Element, data_index_xml: list) -> list:
        """ Este método se diseñó para copiar los datos del archivo XML desde el "root" que tiene el archivo XML,
            indicándole por medio del índice en que posición están los datos.

            NOTA: Esté método es privado, solo se debe utilizar en esta clase, si sé instancia por fuera de esta clase,
            puede que no trabaje correctamente o lance excepciones.

        Args:
            root_xml_file (list): Recibe le "root" del archivo XML.
            data_index_xml (list): Recibe la lista con los índices de las posiciones de los datos en el "root" del,
            archivo XML.

        Returns:
            list: Retorna una lista con los datos copiados del "root".
        """
        try:
            get_data_from_xml_file = [root_xml_file[value] for value in data_index_xml]
            copy_data_from_xml_file = [deepcopy(value) for value in get_data_from_xml_file]
            return copy_data_from_xml_file
        except Exception as error_copy_root_data_from_xml_file:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message='Al intentar copiar los datos del "root" del archivo XML',
                error_message_from_method=error_copy_root_data_from_xml_file))

    def get_the_text_of_a_tag(self, xml_file_name: str) -> str:
        """ Este método se diseñó para obtener el contenido de una etiqueta XML

        Args:
            xml_file_name (str): Recibe el nombre del archivo XML al que se le va a obtener el contenido de la etiqueta.

        Returns:
            str: Retorna el contenido de la etiqueta XML.
        """
        try:
            product_path = config_xml['PRODUCT_PATH']
            root = self.get_the_root_of_the_xml_file(xml_file=xml_file_name)
            name = root.find(product_path).text
            return name
        except Exception as error_when_obtaining_the_text_of_a_label:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_messages_in_colors(
                "Posible error es porque no existe las etiquetas en el archivo XML.", color='yellow'))
            print(messages.print_error(
                programmer_error_message=f"Al intentar obtener el texto de una etiqueta del archivo → {xml_file_name}",
                error_message_from_method=error_when_obtaining_the_text_of_a_label))

    def get_data_from_several_xml_files(self, path_of_archives: str, add_path_to_data: bool = False) -> list:
        """ Este método se diseñó para exportar múltiples datos que están en los archivos XML,
            que se indiquen en el directorio de trabajo de la aplicación.

        Args:
            add_path_to_data (): Parámetro para agregar a la información la ruta del archivo XML.
            path_of_archives (str): Recibe el nombre del la ruta completa donde están los archivos XML.

        Returns:
            dict: Retorna un diccionario con todos los datos organizados por:
            {key = nombre contenido de una etiqueta : value = lista con los datos}

        """
        try:
            xml_file_list = self.recursive_filter_by_xml_files(
                path_of_archives=path_of_archives)
            [self.check_and_format_xml(item_xml) for item_xml in xml_file_list]

            counter_name = 0
            keys_dictionary = set()
            list_data = []
            for item_xml in xml_file_list:
                print(f"XML → {messages.print_messages_in_colors(basename(item_xml), color='yellow')}")
                xml_list = self.get_xml_data_list(xml_file_name=item_xml)
                print_info_xml = messages.print_messages_in_colors(
                    "└──>Total datos xml →",
                    str(len(xml_list)), color1='blue', color2='green')
                print(print_info_xml[0], print_info_xml[1])
                obtained_text = self.get_the_text_of_a_tag(xml_file_name=item_xml)
                data_name = obtained_text.replace(" ", "")
                check_the_file = data_name in keys_dictionary
                if check_the_file:
                    counter_name += 1
                    data_name = f"{data_name}{counter_name}"
                if add_path_to_data:
                    dictionary = {
                        data_name: xml_list,
                        "PATH-XML": item_xml
                    }
                else:
                    dictionary = {data_name: xml_list}
                list_data.append(dictionary)
                keys_dictionary.add(data_name)

            return list_data
        except Exception as error_in_exporting_multiple_data:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message="Al intentar exportar múltiples datos XML.",
                error_message_from_method=error_in_exporting_multiple_data))

    @staticmethod
    def recursive_filter_by_xml_files(path_of_archives: str) -> list:
        """ Este método se diseñó para exportar la ruta y el nombre del XML de directorio,
            que le especifiquen en modo recursivo.

        Args:
            path_of_archives (str): Recibe el nombre del la ruta completa donde están los archivos XML.

        Returns:
            list: Retorna una lista con la ruta y el nombre del archivo XML unidos.
        """
        try:
            root_data = []
            for item in os.walk(path_of_archives):
                join_data = [f"{item[0]}/{value}" for value in item[2] if value.endswith('.xml')]
                if any(join_data):
                    root_data.extend(join_data)
            return root_data
        except Exception as error_in_recursive_filter_by_xml_files:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message=f"Al buscar recursivamente los archivos XML en la ruta → {path_of_archives}",
                error_message_from_method=error_in_recursive_filter_by_xml_files))

    def filter_data_in_xml_files(self, search: str, list_of_the_file_paths: list) -> dict:
        """ Este método se diseñó para buscar entre "N" cantidad de archivos XML,
            y filtrar y devolver el dato que esté buscado el usuario.

        Args:
            search (str): Recibe el dato que se a buscar.
            list_of_the_file_paths (list): Recibe la lista con los nombres de los archivos XML,
            y sus rutas en el sistema.

        Returns:
            dict: Retorna un diccionario con los datos encontrados.
        """
        try:
            number = config_xml['NUMBER']
            product = config_xml['PRODUCT']
            name = config_xml['NAME']
            reference = config_xml['REFERENCE']
            user_id = config_xml['ID']
            [self.check_and_format_xml(item_xml) for item_xml in list_of_the_file_paths]
            data_structure = {}
            for item in list_of_the_file_paths:
                root = self.get_the_root_of_the_xml_file(xml_file=item)
                data_list_xml = self.get_xml_data_list(xml_file_name=item)
                check = search in data_list_xml
                if check:
                    data_index_xml = self.search_the_index_in_the_list(
                        data_list_csv=[search],
                        data_list_xml=data_list_xml)
                    copy_data_from_xml_file = self._copy_root_data_from_xml_file_private(
                        root_xml_file=root, data_index_xml=data_index_xml)
                    for value in copy_data_from_xml_file:
                        data_structure.update({
                            "NÚMERO": value.find(number).text,
                            "REFERENCIA": value.find(reference).text,
                            "PRODUCTO": value.find(product).text,
                            "NOMBRE": value.find(name).text,
                            "ID": value.find(user_id).text,
                            "XML-PATH": item
                        })
                    return data_structure
        except Exception as error_in_filter_data_in_xml_files:
            print(f"uncaught exception {traceback.format_exc()}")
            print(error_in_filter_data_in_xml_files)
            print(messages.print_error(
                programmer_error_message=f"Al buscar recursivamente el dato → {search}",
                error_message_from_method=error_in_filter_data_in_xml_files))

    @staticmethod
    def search_and_filter_data(data_dictionary: list, data_list: list) -> tuple:
        """  Este método se diseñó para buscar y filtrar datos de un "dictionary" y una "list".

        Args:
            data_dictionary (dict): Recibe el diccionario con los datos que se deben filtrar.
            data_list (list): Recibe la lista de datos que se van a filtrar.

        Returns:
            tuple: Retorna una "tuple" con el diccionario con los datos filtrados y las rutas,
            de los archivos.
        """
        try:
            father_dictionary = {}
            dict_path = {}
            for value in data_list:
                for dictionary_value in data_dictionary:
                    key = list(dictionary_value.keys())[0]
                    key_path = list(dictionary_value.keys())[1]
                    path_xml = dictionary_value[key_path]
                    list_of_data = dictionary_value[key]
                    check = value in list_of_data
                    if check:
                        check_key_dict = key in father_dictionary
                        if check_key_dict:
                            father_dictionary[key].extend([value])
                        else:
                            father_dictionary.update({key: [value]})
                        dict_path.update({key: path_xml})
                        break
            return father_dictionary, dict_path
        except Exception as error_when_searching_and_filtering_data:
            print(f"uncaught exception {traceback.format_exc()}")
            print(messages.print_error(
                programmer_error_message="Al filtrar los datos del diccionario y la lista",
                error_message_from_method=error_when_searching_and_filtering_data))
