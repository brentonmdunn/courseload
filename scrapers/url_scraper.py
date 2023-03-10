from bs4 import BeautifulSoup
import requests
import re
from csv import writer
import sys

# sys.path.append('../')

# from scrapers.constant import constant

# Department URL
url = "http://courses.ucsd.edu/courselist.aspx?name=CSE"

url_list = ["http://courses.ucsd.edu/courselist.aspx?name=CSE",
            "http://courses.ucsd.edu/courseList.aspx?name=DSC"]
with open("scrapers/courses.csv", 'w', encoding='utf8', newline='') as f:
    for dept_link in url_list:
        print("Run")

        dept_name_start = dept_link.find("name=")

        dept = dept_link[dept_name_start+5:]

        page = requests.get(dept_link)

        soup = BeautifulSoup(page.content, "html.parser")

        # Need this to change based in dept
        # file_name = "csv/courses_" + dept + ".csv"
        file_name = "scrapers/courses_" + dept + ".csv"

        # with open(file_name, 'w', encoding='utf8', newline='') as f:

        thewriter = writer(f)
        # header = ['Course']
        # thewriter.writerow(header)

        for link in soup.find_all('a', attrs={'href': re.compile("^coursemain.aspx")}):

            fullURL = "http://courses.ucsd.edu/" + str(link.get('href'))

            info = [fullURL]

            thewriter.writerow(info)
