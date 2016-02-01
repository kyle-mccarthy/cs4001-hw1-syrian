class Reader:

    def __init__(self):
        self.data = []

    # This method will take in a file name intended to be read, and then will proceed to parse the file line by
    # line and save the data to the object.
    def file_input(self, file_name):
        try:
            fp = open(file_name, 'r')
        except FileNotFoundError:
            print("The file could not be opened.")
        else:
            self.data = fp.read()
