#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Extracts molecule synonyms from one csv file, chemblids from another
# csv file, and puts them together in a third csv file.

import csv

chemblids_dict = {} # Empty dictionary to hold molregno and chemblids
with open('chemblids.csv', mode = 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter = '\t')
	line_count = 0
	for row in csv_reader:
		if line_count > 0:
			# Omits first line
			# Enters each row into the dictionary where the key is the molregno
			# and the value is the CHEMBL ID number
			chemblids_dict[row[1]] = row[0]
		line_count += 1

synonyms_dict = {} # Empty dictionary to hold synonyms and molregnos
with open('synonyms.csv', mode = 'r') as csv_file:
	csv_reader = csv.reader(csv_file, delimiter = '\t')
	line_count = 0
	for row in csv_reader:
		if line_count > 0:
			# Omits first line
			# Enters each row into the dictionary where the key is the Synonym
			# and the value is the molregno
			synonyms_dict[row[1]] = row[0]
		line_count += 1

with open('synonyms_chemblids.csv', mode = 'w') as csv_file:
	csv_writer = csv.writer(csv_file, delimiter = ',')
	# Write first line/heading
	csv_writer.writerow(['Synonym', 'Chembl ID'])
	for synonym in synonyms_dict:
		# Write the synonym in the first column and the Chembl ID in the second column
		csv_writer.writerow([synonym.lower(), chemblids_dict[synonyms_dict[synonym]]])
		

