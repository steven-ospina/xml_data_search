import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    """ Está clase está diseñada para cargar todas las configuraciones a la aplicación.

    Attributes:
    ----------
        BASE_DIR (string): Esté atributo se utiliza para poder guardar el directorio raíz de la aplicación
    """
    BASE_DIR = basedir


class Messages:
    """ Está clase está diseñada para imprimir mensajes en la terminal con colores.

    Attributes:
    ----------
        color_green_console (string): Esté atributo se utiliza para guardar Código escapé ANSI de color verde.
        color_blue_console (string): Esté atributo se utiliza para guardar Código escapé ANSI de color azul.
        color_yellow_console (string): Esté atributo se utiliza para guardar Código escapé ANSI de color amarillo.
        color_red_console (string): Esté atributo se utiliza para guardar Código escapé ANSI de color rojo.
        color_red_magenta (string): Esté atributo se utiliza para guardar Código escapé ANSI de color magenta.
        color_end_console (string): Esté atributo se utiliza para guardar Código escape ANSI que finaliza los colores.
        text_bold_console (string): Esté atributo se utiliza para guardar Código escapé ANSI convierte el texto en BOLD.

    Methods:
    -------
        print_message_yellow(message: str) -> str
        print_message_green(message: str) -> str
        print_message_blue(message: str) -> str
        print_message_red(message: str) -> str
        print_message_magenta(message: str) -> str
        print_error(message_error_method: str, message: Exception) -> None
    """
    def __init__(self) -> None:
        """ El constructor de la clase Messages
        """
        self.color_green_console: str = '\33[32m'
        self.color_blue_console: str = '\33[34m'
        self.color_yellow_console: str = '\33[33m'
        self.color_red_console: str = '\033[91m'
        self.color_red_magenta: str = '\033[95m'
        self.color_end_console: str = '\033[0m'
        self.text_bold_console: str = '\33[1m'

    def print_message_yellow(self, message: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color amarillo.

        Args:
            message (string): Recibe el mensaje que se va a convertir a color amarillo.

        Returns:
            str: El mensaje que envió el usuario, pero en color amarillo.
        """
        return f"{self.color_yellow_console}{self.text_bold_console}{message}{self.color_end_console}"

    def print_message_green(self, message: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color verde.

        Args:
            message (string): Recibe el mensaje que se va a convertir a color verde.

        Returns:
            str: El mensaje que envió el usuario, pero en color verde.
        """
        return f"{self.color_green_console}{self.text_bold_console}{message}{self.color_end_console}"

    def print_message_blue(self, message: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color azul.

        Args:
            message (string): Recibe el mensaje que se va a convertir a color azul.

        Returns:
            str: El mensaje que envió el usuario, pero en color azul.
        """
        return f"{self.color_blue_console}{self.text_bold_console}{message}{self.color_end_console}"

    def print_message_red(self, message: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color rojo.

        Args:
            message (string): Recibe el mensaje que se va a convertir a color rojo.

        Returns:
            str: El mensaje que envió el usuario, pero en color rojo.
        """
        return f"{self.color_red_console}{self.text_bold_console}{message}{self.color_end_console}"

    def print_message_magenta(self, message: str) -> str:
        """ Esté método se diseñó para poder imprimir en la terminal de color magenta.

        Args:
            message (string): Recibe el mensaje que se va a convertir a color magenta.

        Returns:
            str: El mensaje que envió el usuario, pero en color magenta.
        """
        return f"{self.color_red_magenta}{self.text_bold_console}{message}{self.color_end_console}"

    # Método para imprimir errores
    def print_error(self, programmer_error_message: str, error_message_from_method: Exception) -> None:
        """ Esté método se diseñó para poder imprimir en la terminal de color rojo lo errores de la aplicación, romper la ejecución del código.

        Args:
            programmer_error_message (str): Recibe el mensaje que haya dejado el programador para entender el problema que surja.
            error_message_from_method (Exception):  Recibe el mensaje de error que haya lanzado el método.
        """
        print(f"{self.color_red_console}ERROR: {programmer_error_message}{self.color_end_console}")
        exit(f"{self.color_red_console}ERROR: {error_message_from_method}{self.color_end_console}")
