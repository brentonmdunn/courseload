from bs4 import BeautifulSoup
import requests
import re
from csv import writer
import sys

# sys.path.append('../')

# from scrapers.constant import constant

# Department URL
url = "http://courses.ucsd.edu/courselist.aspx?name=CSE"

dept_name_start = url.find("name=")

dept = url[dept_name_start+5:]

page = requests.get(url)


soup = BeautifulSoup(page.content, "html.parser")

# Need this to change based in dept
# file_name = "csv/courses_" + dept + ".csv"
file_name = "scrapers/courses_" + dept + ".csv"

with open(file_name, 'w', encoding='utf8', newline='') as f:

    thewriter = writer(f)
    # header = ['Course']
    # thewriter.writerow(header)

    for link in soup.find_all('a', attrs={'href': re.compile("^coursemain.aspx")}):

        fullURL = "http://courses.ucsd.edu/" + str(link.get('href'))

        info = [fullURL]

        thewriter.writerow(info)
