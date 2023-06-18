"""
Overview:
This program uses Selenium to render a web page and then uses BeautifulSoup to parse the HTML.
The program then prints the parsed HTML to the console.
"""

import time                                             # needed for the sleep function
import json

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

def parse_weekly(tables):
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

        # Need to update this so it stores file in proper directory
        with open("wunder_weekly.json","w") as f:
            json.dump(observations,f,indent=4)

    # Iterate over each row in each category of the table

    
if __name__=='__main__':

    # Could be a good idea to use the buildWeatherURL function from gui.py
    url = 'http://www.wunderground.com/history/weekly/KCHO/date/2020-12-31'

    # get the page source HTML from the URL
    page = asyncGetWeather(url)

    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')
    
    # find the appropriate tag that contains the weather data
    history = soup.find_all('lib-city-history-observation')
    # history = soup.find(attrs={"class" : "observation-table ng-star-inserted"})
    # history = soup.find_all('tr', has_ngcontent)
    # history_list = soup.find_all("table")

    # table = history.find_all("tbody")

    tbody = history[0].find_all("tbody")

    tables = tbody[0].find_all("table")

    


    # print the parsed HTML
    parse_weekly(tables)
    # print_list(history)
    # print_list(tbody)
    # print_list(tables)