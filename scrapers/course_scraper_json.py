from bs4 import BeautifulSoup
import requests
import re
import csv
from csv import writer
import pandas as pd
# import scrapers.constant as constant
import json
import os
import shutil
from pathlib import Path


count = 1
file_to_open = "scrapers/courses_CSE.csv"

file = open(file_to_open)
url_list = file.readlines()

# Counts the number of lines
csv_file = pd.read_csv(file_to_open)
# idk why I add 1 but it undercounts, maybe 0 indexing?
number_of_lines = len(csv_file) + 1

# Iterates through every line in `coursedata.csv`
for index in range(number_of_lines):

    # Shows that output is running
    if count % 10 == 0:
        print("---")
    else:
        print(".")
    count += 1

    # csv files have a `\n` at the end of them except for the last line.
    # This if statement uses takes out `\n` of any line that is not the
    # last line.
    if (index < number_of_lines - 1):
        page = requests.get(str(url_list[index])[
                            0:len(str(url_list[index]))-1])
    else:
        page = requests.get(url_list[index])

    soup = BeautifulSoup(page.content, "html.parser")

    # A bunch of variables, not all are used. For discussions
    course_id = ''
    dept_code_section = ''
    instructor = ''
    lecture_days = ''
    lecture_time = ''
    lecture_location = ''
    discussion_days = ''
    discussion_time = ''
    discussion_location = ''
    days = ''
    time = ''
    location = ''
    category = ''
    section_code = ''
    department = ''
    course_code = ''
    class_section_code = ''
    start_time_num = ''
    start_time_ampm = ''
    end_time_num = ''
    end_time_ampm = ''
    building = ''
    room = ''
    quarter_season = ''
    quarter_year = ''
    disc_num = 0
    start_24 = ''
    end_24 = ''

    # Variables for lectures
    lect_dept_code_section = ''
    lect_instructor = ''
    lect_lecture_days = ''
    lect_lecture_time = ''
    lect_lecture_location = ''
    lect_discussion_days = ''
    lect_discussion_time = ''
    lect_discussion_location = ''
    lect_days = ''
    lect_time = ''
    lect_location = ''
    lect_category = ''
    lect_section_code = ''
    lect_department = ''
    lect_course_code = ''
    lect_class_section_code = ''
    lect_start_time_num = ''
    lect_start_time_ampm = ''
    lect_end_time_num = ''
    lect_end_time_ampm = ''
    lect_building = ''
    lect_room = ''
    lect_quarter_season = ''
    lect_quarter_year = ''
    lect_disc_num = ''
    lect_start_24 = ''
    lect_end_24 = ''

    # Scrapes the title of the course
    lect_dept_code_section = soup.find('h1').text
    lect_instructor = soup.find('a', id='instructor_HyperLink').text

    # Separates long name into specific data
    lect_dept_code_section_split = lect_dept_code_section.split()
    lect_department = lect_dept_code_section_split[0]
    lect_course_code = lect_dept_code_section_split[1]
    lect_class_section_code = lect_dept_code_section_split[2]
    lect_class_section_code = lect_class_section_code[1:len(
        lect_class_section_code)-1]
    lect_quarter_season = lect_dept_code_section_split[4]
    lect_quarter_year = lect_dept_code_section_split[5]

    # Research sections don't have times listed
    try:
        lect_category = soup.find(
            'span', id='sections_DataGrid_type_Label_0').text
        lect_section_code = soup.find(
            'span', id='sections_DataGrid_section_Label_0').text
        lect_days = soup.find(
            'span', id='sections_DataGrid_days_Label_0').text
        lect_time = soup.find(
            'span', id='sections_DataGrid_time_Label_0').text
        lect_location = soup.find(
            'span', id='sections_DataGrid_location_Label_0').text

        lect_time_split = lect_time.split()
        lect_location_split = lect_location.split()

        lect_start_time_num = lect_time_split[0]
        lect_start_time_ampm = lect_time_split[1]

        lect_end_time_num = lect_time_split[3]
        lect_end_time_ampm = lect_time_split[4]

        # Adjusts for 24-hr time
        if lect_start_time_ampm == 'PM':
            lect_colon_idx = lect_start_time_num.find(":")
            lect_int_hr = int(lect_start_time_num[0:lect_colon_idx])
            lect_int_hr += 12
            lect_start_time_num = str(
                lect_int_hr) + lect_start_time_num[lect_colon_idx:len(lect_start_time_num)]

        if lect_end_time_ampm == 'PM':
            lect_colon_idx = lect_end_time_num.find(":")
            lect_int_hr = int(lect_end_time_num[0:lect_colon_idx])
            lect_int_hr += 12
            lect_end_time_num = str(
                lect_int_hr) + lect_end_time_num[lect_colon_idx:len(lect_end_time_num)]

        lect_days = lect_days.strip()

        lect_building = lect_location_split[0]

        if len(lect_location_split) > 1:
            lect_room = lect_location_split[1]
        else:
            lect_room = ''
    except:
        pass

    # Cuts off graduate courses
    try:
        if int(lect_course_code) > 199:

            break
    except:
        pass

    isMidterm = False

    disc_list = []
    disc_details_dict = {}

    # seminars this doesn't happen
    # bad coding but idk what else to do
    try:
        discussion_list = soup.find_all('tr', class_='discussion')

        # adds an extra item in list to account for final
        discussion_list.append('')

        discussion_count = 1

        for discussion in discussion_list:

            category_section_num = "sections_DataGrid_type_Label_" + \
                str(discussion_count)
            section_code_section_num = "sections_DataGrid_section_Label_" + \
                str(discussion_count)
            days_section_num = "sections_DataGrid_days_Label_" + \
                str(discussion_count)
            time_section_num = "sections_DataGrid_time_Label_" + \
                str(discussion_count)
            location_section_num = "sections_DataGrid_location_Label_" + \
                str(discussion_count)

            category = soup.find('span', id=category_section_num).text

            if category == 'MI':
                isMidterm = True

            section_code = soup.find(
                'span', id=section_code_section_num).text
            days = soup.find('span', id=days_section_num).text
            time = soup.find('span', id=time_section_num).text
            location = soup.find('span', id=location_section_num).text

            discussion_count += 1

            time_split = time.split()
            location_split = location.split()

            start_time_num = time_split[0]
            start_time_ampm = time_split[1]
            end_time_num = time_split[3]
            end_time_ampm = time_split[4]

            building = location_split[0]

            if len(location_split) > 1:
                room = location_split[1]
            else:
                room = ''

            days = days.strip()

            disc_details_dict = {
                "department": "CSE",
                "course_code": course_code,
                "class_section_code": class_section_code,
                "section_code": section_code,
                "instructor": instructor,
                "category": category,
                "days": days,
                "start_time": start_time_num,
                "end_time": end_time_num,
                "building": building,
                "room": room,
            }

            disc_list.append(disc_details_dict)

    except:
        continue

    lect_file_name = lect_department + "_" + lect_course_code + \
        "_" + lect_class_section_code + ".json"

    course_id = lect_department + "_" + lect_course_code + \
        "_" + lect_class_section_code

    isDiscussion = False

    try:
        discussion_list
        isDiscussion = True
    except:
        pass

    if isDiscussion:
        disc_num = len(discussion_list)-1

    lect_this_dict = {
        "course_id": course_id,
        "department": lect_department,
        "course_code": lect_course_code,
        "class_section_code": lect_class_section_code,
        "section_code": lect_section_code,
        "instructor": lect_instructor,
        "category": lect_category,
        "days": lect_days,
        "start_time": lect_start_time_num,
        "end_time": lect_end_time_num,
        "building": lect_building,
        "room": lect_room,
        "disc_num": disc_num,
        "midterm": isMidterm,
        "discussions": disc_list
    }

    # Moves creates file in working dir then moves file into final directory
    newDirectory = "scrapers/json/" + str(lect_file_name)

    with open(lect_file_name, "w") as outfile:
        json.dump(lect_this_dict, outfile, indent=2)
    shutil.move(lect_file_name, newDirectory)
