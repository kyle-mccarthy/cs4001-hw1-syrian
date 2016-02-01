from parser import Parser

# import the data from a csv and save it to and html table
r = Parser()
r.file_input('../data/SyriaIDPSites2015LateJunHIUDoS.csv', 'latin-1')
r.import_csv()
r.export_html_table('../data/SyrianIDP.html')

# import the data as html and export it to json
r = Parser()
r.file_input('../data/SyrianIDP.html')
r.import_html()
