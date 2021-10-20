class FileManager:
    def __init__(self, file_name):
        self.file_name = file_name

    def read_file(self, file_name):
        uchwyt = open(file_name, 'r')
        dane = uchwyt.read()
        print(dane)
        uchwyt.close()

    def update_file(self, file_name, text_data):
        uchwyt = open(file_name, 'a')
        uchwyt.write(text_data)
        uchwyt.close()