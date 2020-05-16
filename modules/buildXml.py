from searchData import Data

class Build(Data):
    # Initializer / Instance Attributes
    def __init__(self):
        # super().__init__()
        Data.__init__(self)
        # self.archive_xml = archive_Xml
        # self.list_data_csv = list_data_csv
        self.reading_method = 'r'
        self.data_clean = []
        self.final_data = []
        self.count = 0
        self.count2 = 0
        self.flag = True
        self.account_statements = ''
        self.obligation = ''
    # instance method
    def getirectory(self):
        hola = super().self.get_the_current_working_directory()
        print(hola)

