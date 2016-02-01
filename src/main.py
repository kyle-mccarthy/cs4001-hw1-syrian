from reader import Reader

r = Reader()
r.file_input('../data/SyriaIDPSites2015LateJunHIUDoS.csv', 'latin-1')
r.import_csv()
r.export_html_table('../data/SyrianIDP.html')
