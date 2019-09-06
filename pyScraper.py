import requests
import re
import time
import yaml
from lxml import html


if __name__ == "__main__":

	with open("config.yml","r") as config_file:
		scraperCfg = yaml.load(config_file)

	page = requests.get(scraperCfg['url'])
	page_html = html.fromstring(page.content)
	scrapeGrab = page_html.xpath(scraperCfg['xpath'])

	output_file = open(scraperCfg['output'],"w")

	for sG in scrapeGrab:
		process = html.tostring(sG).decode("utf-8")
		process = process.split(">")[1]
		process = process.split("<")[0]
		output_file.write(process+'\n')
		
		


