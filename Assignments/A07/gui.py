""" 
Description:
    This is an example gui that allows you to enter the appropriate parameters to get the weather from wunderground.
TODO:
    - You will need to change the text input boxes to drop down boxes and add the appropriate values to the drop down boxes.
    - For example the month drop down box should have the values 1-12.
    - The day drop down box should have the values 1-31.
    - The year drop down box should have the values ??-2023.
    - The filter drop down box should have the values 'daily', 'weekly', 'monthly'.
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

    codes = parse_codes()
    codes_combo = sg.Combo(codes[1:], font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-CODES-')

    filters = ['daily', 'weekly', 'monthly']
    lst = sg.Combo(filters, font=('Arial Bold', 14),  expand_x=True, enable_events=True,  readonly=False, key='-FILTERS-')
    
    # Create the gui's layout using text boxes that allow for user input without checking for valid input
    layout = [
        [sg.Text('Month')],[sg.InputText(month)],
        [sg.Text('Day')],[sg.InputText(day)],
        [sg.Text('Year')],[sg.InputText(year)],
        [sg.Text('Code')],[codes_combo],
        [sg.Text('Daily / Weekly / Monthly')],[lst],
        [sg.Submit(key='-SUBMIT-'), sg.Cancel(key='-CANCEL-')]
    ]      

    window = sg.Window('Get The Weather', layout)    

    while True:
        event, values = window.read()
        # print(event, values)
        if event in (sg.WIN_CLOSED, 'Exit'):
            values = None
            break
        # if event == '-COMBO-':
        #     print("combo")
        if event == '-SUBMIT-':
            break
        if event == '-CANCEL-':
            values = None
            break
    window.close()

    if values:
        month = values[0]
        day = values[1]
        year = values[2]
        code = values['-CODES-']
        filter = values['-FILTERS-']

        link = f'https://www.wunderground.com/history/{filter}/{code}/date/{year}-{month}-{day}'

        sg.popup('You entered', f"Month: {month}, Day: {day}, Year: {year}, Code: {code}, Filter: {filter}")

        return link
    else:
        sg.popup('Farewell')

def create_table(toprow, rows):
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
    window = sg.Window("Table Demo", layout, size=(1200, 500), resizable=True)
    while True:
        event, values = window.read()
        print("event:", event, "values:", values)
        if event == sg.WIN_CLOSED:
            break
        # if '+CLICKED+' in event:
        #     sg.popup("You clicked row:{} Column: {}".format(event[2][0], event[2][1]))
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

    create_table(toprow, rows)

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
        print("Invalid filter type given.")
    
    for key in observations.keys():
        toprow.append(key)

    # for each row, we need to add the corrisponding element accross each category.
    # Might have to get the number of rows by counting the number of time entries.
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

    create_table(toprow, rows)

    
    
    


if __name__=='__main__':
    # url = buildWeatherURL()
    # print(url)
    # display_daily_results()
    display_weekly_monthly_results("m")