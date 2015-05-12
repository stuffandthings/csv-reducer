from collections import defaultdict
import csv

# The dictionary used for making the data in the wanted format
# key = age-group (e.g. '18-24')
# value = dictionary with key as year, and value as number of
#         occurrences of disease in that year
dictionary = dict()

# Open the csv file and parse it to reduce the dataset
with open('diseases.csv', 'rU') as csvfile:
	reader = csv.reader(csvfile, delimiter=',')
	for row in reader:
		# The key here is the age-group
		key = row[3]
		# The year for the data
		year = row[4]

		# Since we have some missing data, we are
		# dealing with that and assuming 0 for missing
		# data.
		if len(row[5]) != 0:
			val = int(row[5])
		else: val = 0

		if key in dictionary:
			if year in dictionary[key]:
				dictionary[key][year] += val
			else:
				dictionary[key][year] = val
		else:
			dictionary[key] = dict()
			dictionary[key][year] = val

		# At this point we have a dictionary of the form:
		# {'18-24' : {'1998': 100, '1999':200, '2000':300}}
		# NOTE: The above is just an example

# Write results from the dictionary of values we parsed
# to a new csv file
with open('result.csv', 'wb') as writefile:
	# List of the years, we iterate over these so the resulting
	# csv file is sorted by year, since the dictionary doesn't
	# add the years in order.
	years = ['1998','1999','2000','2001','2002','2003','2004']

	writer = csv.writer(writefile, delimiter=',')
	for age in dictionary:
		for year in years:
			# Each row is of this form:
			data = [age, year, dictionary[age][year]]

			writer.writerow(data)
