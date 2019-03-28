#!/usr/bin/env python
# -*- coding: utf-8 -*-
#  

import csv, bs4, requests

# Open the files containing the article data, chemical reference list,
# and the file where the chemicals mentioned in the articles and their
# associated data will be stored

articles ={}
with open('article_scrapings.csv', mode = 'r') as article_file:
	article_reader = csv.reader(article_file, delimiter = ',')
	for article_entry in article_reader:
		if article_entry[0] != 'Article Title':
			articles[article_entry[0]] = article_entry[5]

chemicals = {}
with open('synonyms_chemblids.csv', mode = 'r') as chemical_reference:
	chemical_reader = csv.reader(chemical_reference, delimiter = ',')
	for chemical_entry in chemical_reader:
		if chemical_entry[0] != 'Synonym':
			chemicals[chemical_entry[0].lower()] = chemical_entry[1]

results = {}
with open('chemical_scrapings_hiv.csv', mode = 'w') as chemical_scrapings:
	chemical_writer= csv.writer(chemical_scrapings, delimiter = ',')
	for chemical_name in chemicals:
		chembl_id = chemicals[chemical_name]
		for article_title in articles:
			article_text = articles[article_title]
			if chemical_name in article_text:
				if chembl_id not in results:
					chembl_url = 'https://www.ebi.ac.uk/chembl/compound/inspect/' + chembl_id
					results[chembl_id] = [1, [chemical_name], [article_title], chembl_url]
				elif chembl_id in results:
					results[chembl_id][0] += 1
					if chemical_name not in results[chembl_id][1]:
						results[chembl_id][1].append(chemical_name)
					if article_title not in results[chembl_id][2]:
						results[chembl_id][2].append(article_title)
	chemical_writer.writerow(['chembl id', 'Number of Articles Mentioned', 'Names Used', 'Mentioned in Articles', 'chembl url'])
	for chem_id in results:
		chemical_writer.writerow([chem_id, results[chem_id][0], results[chem_id][1], results[chem_id][2], results[chem_id][3]])
				
