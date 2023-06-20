"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""

import time                                             # needed for the sleep function
import json
from gui import display_daily_results
from gui import display_weekly_monthly_results

from bs4 import BeautifulSoup                           # used to parse the HTML
from selenium import webdriver                          # used to render the web page
# from seleniumwire import webdriver                      
from selenium.webdriver.chrome.service import Service   # Service is only needed for ChromeDriverManager


import functools                                        # used to create a print function that flushes the buffer
flushprint = functools.partial(print, flush=True)       # create a print function that flushes the buffer immediately

def asyncGetWeather(url):
    """Returns the page source HTML from a URL rendered by ChromeDriver.
    Args:
        url (str): The URL to get the page source HTML from.
    Returns:
        str: The page source HTML from the URL.
        
    Help:
    https://stackoverflow.com/questions/76444501/typeerror-init-got-multiple-values-for-argument-options/76444544
    """
    
    #change '/usr/local/bin/chromedriver' to the path of your chromedriver executable
    # service = Service(executable_path='C:/repos/4883-SoftwareTools/chromedriver_win32')
    # options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    
    # driver = webdriver.Chrome(service=service,options=options)  # run ChromeDriver
    driver = webdriver.Chrome()  # run ChromeDriver

    flushprint("Getting page...")
    driver.get(url)                                             # load the web page from the URL
    flushprint("waiting 10 seconds for dynamic data to load...")
    time.sleep(10)                                               # wait for the web page to load
    flushprint("Done ... returning page source HTML")
    render = driver.page_source                                 # get the page source HTML
    driver.quit()                                               # quit ChromeDriver
    return render                                               # return the page source HTML

# Function to be used as a filter in find_all
def has_ngcontent(tag):
    return tag.has_attr('_ngcontent-app-root-c210')

def print_html(html_data):
    if html_data is not None:
        print(html_data.prettify())
    else:
        print("There were no matches for the search")

def print_list(html_data_list):
    if html_data_list:
        for item in html_data_list:
            print(item.prettify())
    else:
        print("There were no matches for the search")

def parse_daily(page):
    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')

    history = soup.find_all('lib-city-history-observation')

    table = history[0].find('table')

    tbody = table.find('tbody')

    cat = {
        1: "time",
        2: "temp",
        3: "dew",
        4: "humidity",
        5: "wind",
        6: "wspeed",
        7: "wgust",
        8: "pressure",
        9: "precip",
        10: "condition"
    }

    observations = {
        "time": [

        ],
        "temp": [

        ],
        "dew": [

        ],
        "humidity": [

        ],
        "wind": [

        ],
        "wspeed": [

        ],
        "wgust": [

        ],
        "pressure": [

        ],
        "precip": [

        ],
        "condition": [

        ]
    }

    rows = tbody.find_all("tr") 

    # r = 0
    c = 1
    for row in rows:
        columns = row.find_all("td")
        for column in columns:
            if c == 1 or c == 5 or c == 10:
                data_tag = column.find("span")
                observations[cat[c]].append(data_tag.get_text().strip())
            if c >= 2 and c <= 4 or c >= 6 and c <= 9:
                lib = column.find("lib-display-unit")
                span = lib.find("span")
                data_tag = span.find("span")
                observations[cat[c]].append(data_tag.get_text().strip())
            c += 1
        c = 1
        # r += 1 # just for checking number of rows in table since they vary
    # print(f"There are {r} row(s)")

    with open("wunder_daily.json","w") as f:
        json.dump(observations,f,indent=4)
    
    display_daily_results()

    


def parse_weekly_monthly(page, filter):
    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')

    history = soup.find_all('lib-city-history-observation')

    tbody = history[0].find_all("tbody")

    tables = tbody[0].find_all("table")

    categories = {
        0: "time",
        1: "temp",
        2: "dew",
        3: "humidity",
        4: "wind",
        5: "pressure",
        6: "precipitation"
    }

    tags = {
        0: "max",
        1: "avg",
        2: "min"
    }

    observations = {
        "time": [

        ],
        "temp": {
            "max": [
            
            ],
            "avg": [
            
            ],
            "min": [
            
            ]
        },
        "dew": {
            "max": [
            
            ],
            "avg": [
            
            ],
            "min": [
            
            ]
        },
        "humidity": {
            "max": [
            
            ],
            "avg": [
            
            ],
            "min": [
            
            ]
        },
        "wind": {
            "max": [
            
            ],
            "avg": [
            
            ],
            "min": [
            
            ]
        },
        "pressure": {
            "max": [
            
            ],
            "avg": [
            
            ],
            "min": [
            
            ]
        },
        "precipitation": [

        ]
    }

    i_cat = 0
    i_tag = 0
    for table in tables:
        rows = table.find_all("tr")


        for row in rows[1:]:
            data_tags = row.find_all("td")
            for data_tag in data_tags:
                # print(data_tag.get_text())
                if i_cat == 0:
                    observations["time"].append(data_tag.get_text().strip())
                elif i_cat > 0 and i_cat < 6:
                    observations[categories[i_cat]][tags[i_tag]].append(data_tag.get_text().strip())
                    i_tag += 1
                else:
                    observations["precipitation"].append(data_tag.get_text().strip())
            i_tag = 0
        # print("Table " + str(i) + ":")
        # print_list(rows)
        # i += 1
        i_cat += 1

    if filter == "w":
        # Need to update this so it stores file in proper directory
        with open("wunder_weekly.json","w") as f:
            json.dump(observations,f,indent=4)
        display_weekly_monthly_results("w")
    elif filter == "m":
        # Need to update this so it stores file in proper directory
        with open("wunder_monthly.json","w") as f:
            json.dump(observations,f,indent=4)
        display_weekly_monthly_results("m")
    else:
        print("A valid filter type was not provided.")


    
if __name__=='__main__':

    # Could be a good idea to use the buildWeatherURL function from gui.py
    # url_daily = 'http://www.wunderground.com/history/daily/KCHO/date/2020-12-31'
    # url_weekly = 'http://www.wunderground.com/history/weekly/KCHO/date/2020-12-31'
    url_monthly = 'http://www.wunderground.com/history/monthly/KCHO/date/2020-12-31'


    # get the page source HTML from the URL
    page = asyncGetWeather(url_monthly)

    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')

    history = soup.find_all('lib-city-history-observation')

    # DAILY 
    # table = history[0].find('table')

    # tbody = table.find('tbody')

    # parse_daily(tbody)
    
    # WEEKLY and MONTHLY
    tbody = history[0].find_all("tbody")

    tables = tbody[0].find_all("table")

    parse_weekly_monthly(tables, "m")