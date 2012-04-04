import csv
from operator import itemgetter

censusRecords = csv.reader(open('../transcriptions/sd36_ed59-25_sheet1a.csv', 'rb'), delimiter=';', quotechar='|')

for records in sorted(censusRecords, key=itemgetter(7)):
	print records[7];