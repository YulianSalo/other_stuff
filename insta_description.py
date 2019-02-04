from bs4 import BeautifulSoup
import requests
import re

page_link = input("Input Instagram page link to get your photos descrpition:")
# this is the url that we've already determined is safe and legal to scrape from.

page_response = requests.get(page_link)
# here, we fetch the content from the url, using the requests library

page_content = BeautifulSoup(page_response.content, 'html.parser')

fields = []
page_content.prettify()

pattern = '"Image may contain:(.*?)\"}'
pattern = re.compile(pattern)
for script in page_content.find_all('script', text = pattern):

	fields = re.findall(pattern, script.text)

for i in range(len(fields)):
	print(i+1,":", fields[i])
