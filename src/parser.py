import csv
from bs4 import BeautifulSoup


class Parser:

    def __init__(self):
        self.file = None
        self.data = []
        self.field_names = ('Description', 'Country', 'ADM1', 'ADM2', 'ADM3', 'ADM4', 'Latitude', 'Longitude', 'Name',
                          'pcode', 'fips', 'iso_alpha2', 'iso_alpha3', 'iso_num', 'stanag', 'tld')

    def __exit__(self, exc_type, exc_val, exc_tb):
        # close the file on exit
        if self.file is not None:
            self.file.close()

    # This method will take in a file name intended to be read, and then will proceed to parse the file line by
    # line and save the data to the object.
    def file_input(self, file_name, enc=None):
        try:
            self.file = open(file_name, 'r', encoding=enc)
            return True
        except FileNotFoundError:
            print("The file could not be opened.")
            return False

    # import the data from the file that is of type csv, this will iterate the file, drop the header, and then map the
    # key-value data
    def import_csv(self):
        # ensure that the file exists and is open
        if self.file is not None:
            # we need to use reader as it uses a list instead of dict, keeping the order of the filed intact, which
            # becomes very important when exporting the file information.  Additionally, we will need to skip the first
            # line of the CSV since it is the header.
            dr = csv.reader(self.file, self.field_names)
            next(dr)
            for line in dr:
                self.data.append(line)
            return True
        print("Could not import CSV, no file.")
        return False

    def import_html(self):
        if self.file is not None:
            soup = BeautifulSoup(self.file.read, 'html.parser')
            print(soup.prettify())

    def export_html_table(self, file_name):
        if len(self.data) != 0:
            html = "<table>\n"

            # fill in the header
            html += "\t<thead>\n\t<tr>\n"
            # insert header cols
            for col in self.field_names:
                html += "\t\t<th>" + col + "</th>\n"
            html += "\t</thead>\n"

            # fill in the table data
            html += "\t<tbody>\n"
            for row in self.data:
                html += "\t\t<tr>"
                for col in row:
                    html += "<td>" + col + "</td>"
                html += "<tr>\n"
            html += "\t</tbody>\n"

            html += "</table>"

            # export the data in HTML format
            try:
                fp = open(file_name, 'w')
            except Exception:
                print("Could not write the table data, could not create file.")
            else:
                fp.write(html)
                fp.close()
            return True
        else:
            print("Could not print the table, no data imported.")
            return False

