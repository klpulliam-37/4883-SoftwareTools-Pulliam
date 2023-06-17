from gui import buildWeatherURL
from extract import asyncGetWeather
from extract import parse_weekly
from bs4 import BeautifulSoup   

if __name__=='__main__':
    url = buildWeatherURL()
    page = asyncGetWeather(url)

    # parse the HTML
    soup = BeautifulSoup(page, 'html.parser')
    
    # find the appropriate tag that contains the weather data
    history = soup.find_all('lib-city-history-observation')

    tbody = history[0].find_all("tbody")

    tables = tbody[0].find_all("table")

    parse_weekly(tables)