import csv
from collections import deque
from collections import OrderedDict
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

    # import the data from an html file, the headers are stored in <th> tags, while the main data is stored in <td> tags
    # this will call a helper static method that maps a list of list to a mapped data object
    def import_html(self):
        if self.file is not None:
            soup = BeautifulSoup(self.file.read(), 'html.parser')

            # extract all of the data from the tr rows, we can assume that the first row contains the headers, since
            # that is how our function outputs it
            rows = []
            for tags in soup.find_all("tr"):
                row = []
                for item in tags:
                    s = str(item.string).strip(' \t\n\r')
                    if (len(s) > 0):
                        row.append(s)
                rows.append(row)
            self.data = Parser.map_list_to_dict(rows)
            return True
        return False


    @staticmethod
    # the list that we passed is essentially a FIFO queue, the first row is the header and the other rows are the
    # data, we want to map the header to the data values
    def map_list_to_dict(list_data):
        data = []
        queue = deque(list_data)
        keys = queue.popleft()
        for item in queue:
            data.append(OrderedDict(zip(keys, item)))
        return data

    # export the data as an html table, the data is cleaned up a little bit to make it easier to read using new lines
    # and tabs, the file name that it will be exported to is passed as a parameter.
    def export_html_table(self, file_name):
        if len(self.data) != 0:
            html = "<table>\n"

            # fill in the header
            html += "<thead><tr>"
            # insert header cols
            for col in self.field_names:
                html += "<th>" + col + "</th>"
            html += "</tr></thead>"

            # fill in the table data
            html += "<tbody>"
            for row in self.data:
                html += "<tr>"
                for col in row:
                    html += "<td>" + col + "</td>"
                html += "<tr>"
            html += "</tbody>"

            html += "</table>"

            # export the data in HTML format
            try:
                fp = open(file_name, 'w')
            except Exception:
                print("Could not write the table data, could not create file.")
            else:
                fp.write(BeautifulSoup(html, "html.parser").prettify())
                fp.close()
            return True
        else:
            print("Could not print the table, no data imported.")
            return False

