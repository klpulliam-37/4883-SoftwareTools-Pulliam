""" 
Description:
    This is an example gui that allows you to enter the appropriate 
    parameters to get the weather from wunderground.
"""
import PySimpleGUI as sg  
from codes import parse_codes
import json

def currentDate(returnType='tuple'):
    """ Get the current date and return it as a tuple, list, or dictionary.
    Args:
        returnType (str): The type of object to return.  Valid values are 'tuple', 'list', or 'dict'.
    """
    from datetime import datetime
    if returnType == 'tuple':
        return (datetime.now().month, datetime.now().day, datetime.now().year)
    elif returnType == 'list':
        return [datetime.now().month, datetime.now().day, datetime.now().year]

    return {
        'day':datetime.now().day,
        'month':datetime.now().month,
        'year':datetime.now().year
    }

def buildWeatherURL(month=None, day=None, year=None, airport=None, filter=None):
    """ A gui to pass parameters to get the weather from the web.
    Args:
        month (int): The month to get the weather for.
        day (int): The day to get the weather for.
        year (int): The year to get the weather for.
    Returns:
        Should return a URL like this, but replace the month, day, and year, filter, and airport with the values passed in.
        https://www.wunderground.com/history/daily/KCHO/date/2020-12-31
    """
    current_month,current_day,current_year = currentDate('tuple')
    
    if not month:
        month = current_month
    if not day:
        day = current_day
    if not year:
        year = current_year

    days = [i for i in range(1, 32)]
    # print(days)
    days_combo = sg.Combo(days, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-DAYS-')

    months = [i for i in range(1, 13)]
    # print(months)
    months_combo = sg.Combo(months, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-MONTHS-')

    years = [i for i in range(1990, 2024)]
    # print(years)
    years_combo = sg.Combo(years, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-YEARS-')

    codes = parse_codes()
    codes_combo = sg.Combo(codes[1:], font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-CODES-')

    filters = ['daily', 'weekly', 'monthly']
    lst = sg.Combo(filters, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-FILTERS-')
    
    # Create the gui's layout using text boxes that allow 
    # for user input without checking for valid input.
    layout = [
        [sg.Text('Month')],[months_combo],
        [sg.Text('Day')],[days_combo],
        [sg.Text('Year')],[years_combo],
        [sg.Text('Code')],[codes_combo],
        [sg.Text('Daily / Weekly / Monthly')],[lst],
        [sg.Submit(key='-SUBMIT-'), sg.Cancel(key='-CANCEL-')]
    ]      

    window = sg.Window('Get The Weather', layout, size=(400, 350))    

    # Start the event loop
    while True:
        event, values = window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            values = None
            break
        if event == '-SUBMIT-':
            break
        if event == '-CANCEL-':
            values = None
            break
    window.close()

    if values:
        month = values['-MONTHS-']
        day = values['-DAYS-']
        year = values['-YEARS-']
        code = values['-CODES-']
        filter = values['-FILTERS-']

        link = f'https://www.wunderground.com/history/{filter}/{code}/date/{year}-{month}-{day}'

        sg.popup('You entered', f"Month: {month}, Day: {day}, Year: {year}, Code: {code}, Filter: {filter}")

        return {"link": link, "filter": filter}
    else:
        sg.popup('Farewell')

        return None

def create_table(table_name, toprow, rows):
    sg.set_options(font=("Arial Bold", 14))
    tbl1 = sg.Table(values=rows, headings=toprow,
    auto_size_columns=False,
    col_widths=15,
    display_row_numbers=False,
    justification='center', key='-TABLE-',
    alternating_row_color='lightblue',
    selected_row_colors='red on yellow',
    enable_events=True,
    expand_x=True,
    expand_y=True,
    enable_click_events=True)
    layout = [[tbl1]]
    window = sg.Window(table_name, layout, size=(1200, 500), resizable=True)
    while True:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WIN_CLOSED:
            break
    window.close()

def display_daily_results():
    toprow = []
    rows = []

    with open('wunder_daily.json') as results:
        observations = json.load(results)
    
    for key in observations.keys():
        toprow.append(key)

    for i in range(0, len(observations["time"])):
        rows.append([
            observations["time"][i],
            observations["temp"][i],
            observations["dew"][i],
            observations["humidity"][i],
            observations["wind"][i],
            observations["wspeed"][i],
            observations["wgust"][i],
            observations["pressure"][i],
            observations["precip"][i],
            observations["condition"][i]
        ])

    create_table("Daily Observations", toprow, rows)

def display_weekly_monthly_results(filter):
    toprow = []
    rows = [['date', 
             ['max', 'avg', 'min'], 
             ['max', 'avg', 'min'], 
             ['max', 'avg', 'min'], 
             ['max', 'avg', 'min'], 
             ['max', 'avg', 'min'], 
             'total']]

    if filter == "w":
        with open('wunder_weekly.json') as results:
            observations = json.load(results)
    elif filter == "m":
        with open('wunder_monthly.json') as results:
            observations = json.load(results)
    else:
        print("Invalid filter type given for loading file.")
    
    for key in observations.keys():
        toprow.append(key)

    # For each row, add the corrisponding element accross each category.
    for i in range(0, len(observations["time"])):
        rows.append([
            observations['time'][i], 
            [observations['temp']['max'][i], observations['temp']['avg'][i], observations['temp']['min'][i]],
            [observations['dew']['max'][i], observations['dew']['avg'][i], observations['dew']['min'][i]],
            [observations['humidity']['max'][i], observations['humidity']['avg'][i], observations['humidity']['min'][i]],
            [observations['wind']['max'][i], observations['wind']['avg'][i], observations['wind']['min'][i]],
            [observations['pressure']['max'][i], observations['pressure']['avg'][i], observations['pressure']['min'][i]],
            observations['precipitation'][i]
        ])

    if filter == "w":
        create_table("Weekly Observations", toprow, rows)
    elif filter == "m":
        create_table("Monthly Observations", toprow, rows)
    else:
        print("Invalid filter type given for table creation.")

# Testing
if __name__=='__main__':
    pass
    # url = buildWeatherURL()
    # print(url)
    # display_daily_results()
    # display_weekly_monthly_results("m")