# Coarseload

The goal of this project is to create an alternative to UC San Diego's WebReg system for purposes of finding and planning classes. This is a personal project and is not affliated with nor endorsed by UC San Diego.

# How it works

This project is split up into two main sections: scraping data and displaying data.

## Scraping data

1. The URLs from each department page are scraped using `url_scraper.py` and are saved in a 1 column `.csv` called `courses_<department>.csv`. As of right now, you have to manually change the `url` variable in `url_scraper.py`.
2. The output file, `courses_<deptartment>.csv` is currently stored in `scrapers/` but eventually will be moved to `csv/`.`course_scraper_json.py` is then used to go through each URL listed in `courses_<department>.csv` and writes each section to individual json files stored in `scrapers/json/`.

The bash script `scrape.sh` runs the two python programs and creates a json schema for the specified department.

\*\*Do not have a new line at end of `courses.csv`

## Displaying data

The website using Next.js + Typescript to create a front end. There is a static backend made up of json files.

# Websites that helped along the way

moving files: https://www.learndatasci.com/solutions/python-move-file/

dump vs dumps: https://www.geeksforgeeks.org/python-difference-between-json-dump-and-json-dumps/

https://stackoverflow.com/questions/64926174/module-not-found-cant-resolve-fs-in-next-js-application for fs module

# Dev

Branch naming rules: `<Feature> or <Bug>/<username>/<small description>`

Run next.js app:

```
npm run dev
```

Activate virtual environment:

```
source env/bin/activate
```

Recrease the virtual environment:

```
 ~ pip install -r requirements.txt
```
