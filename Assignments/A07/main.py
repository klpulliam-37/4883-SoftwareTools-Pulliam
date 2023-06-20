"""
Desription:
    This program allows a user to input a day, month, and year to view the weather data of that day.
    The user can also specify a filter to apply to the data such as daily, weekly, or monthly.
    All of the data comes from wunderground.com.
"""

from gui import buildWeatherURL
from extract import asyncGetWeather
from extract import parse_daily
from extract import parse_weekly_monthly

if __name__=='__main__':
    # Get the url from the user
    url = buildWeatherURL()

    # Parse the data and display the results in a table
    if url:
        page = asyncGetWeather(url["link"])

        if url["filter"] == "daily":
            parse_daily(page)
        elif url["filter"] == "weekly":
            parse_weekly_monthly(page, "w")
        elif url["filter"] == "monthly":
            parse_weekly_monthly(page, "m")
        else:
            print("There was an invalid filter used in the url creation.")