#! /usr/bin/python
#
#  

import bs4, requests, csv

with open('article_scrapings.csv', mode = 'w') as article_file:
	article_writer = csv.writer(article_file, delimiter = ',')
	article_writer.writerow(['Article Title', 'Article URL', 'Article Type', 'Publication Date', 'Open', 'Article Text'])
	
	res = requests.get('https://www.nature.com/search?q=HIV')
	res.raise_for_status()
	natureSoup = bs4.BeautifulSoup(res.text, 'lxml')
	articles = natureSoup.select('ol > li > div > h2 > a')
	articlesInfo = natureSoup.select('ol > li > p')
	for number in range(len(articles)):
		title = articles[number].getText().strip() # Gets title of articles as a string with whitespace stripped
		articleURL = 'https://www.nature.com' + articles[number].get('href') # Gets url of articles as a string
		info = articlesInfo[number].getText().strip().split('|')
		articleType = info[0].strip() # Collects article type
		articleDate = info[1].strip() # Collects date of publication
		# Collects whether or not the article is open
		if len(info) == 3:
			articleOpen = 'yes'
			article = requests.get(articleURL) # use url extracted from above
			article.raise_for_status()
			articleSoup = bs4.BeautifulSoup(article.text, 'lxml')
			articleText = articleSoup.getText().split('Abstract')[1].split('References')[0].split('Experimental Procedures')[0]
			articleText = articleText.lower()
			articleText = articleText.replace('introduction', 'introduction ')
			articleText = articleText.replace('discussion', 'discussion ')
			articleText = articleText.replace('conclusion', 'conclusion ')
		elif len(info) == 2:
			articleOpen = 'no'
			articleText = ''
		article_writer.writerow([title, articleURL, articleType, articleDate, articleOpen, articleText])

