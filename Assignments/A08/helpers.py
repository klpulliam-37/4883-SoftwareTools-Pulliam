from math import floor
import csv

db = []

# Open the CSV file
with open('data.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.reader(file)

    i = 0
    # Read each row in the CSV file
    for row in reader:
        if i == 0:
            i += 1
            continue
        db.append(row)

def get_unique_countries():
    global db
    countries = {}

    for row in db:
        if not row[2] in countries:
            countries[row[2]] = 0

    return list(countries.keys())

def get_unique_regions():
    global db
    regions = {}

    for row in db:
        if not row[3] in regions:
            regions[row[3]] = 0
   
    return list(regions.keys())

# ============================== DEATHS HELPER ============================== #
def get_deaths():
    try:
        deaths = 0            

        for row in db:            
            deaths += int(row[6])

        return {"data":deaths,"success":True,"message":"Total Deaths"}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_deaths_by_all_countries():
    try:
        deaths = {}            

        for row in db:
            if not row[2] in deaths:
                deaths[row[2]] = 0
            
            deaths[row[2]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths by Country"}

    except Exception as e:
        return {"success":False,"error": str(e)}
    
def get_deaths_all_countries_by_years(year1, year2):
    try:
        years = [year1, year2]
        max_year = max(years)
        min_year = min(years)

        deaths = {}            

        for row in db:
            if not row[2] in deaths:
                deaths[row[2]] = 0
            
            if row[0][:4] >= str(min_year) and row[0][:4] <= str(max_year):
                deaths[row[2]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths by Country"}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_deaths_by_country(country):
    try:
        deaths = {f"{country}": 0}

        for row in db:
            if row[2] == country:
                deaths[country] += int(row[6])

        return {"data": deaths, "success": True, "message": "Deaths by Country", "params": {"country": f"{country}"}}

    except Exception as e:
        return {"success": False, "error": str(e)}
    
def get_deaths_by_all_regions():
    try:
        deaths = {}            

        for row in db:
            if not row[3] in deaths:
                deaths[row[3]] = 0
            
            deaths[row[3]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths by Region"}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_deaths_by_region(region):
    try:
        deaths = {"deaths": 0}

        for row in db:
            if row[3] == region:
                deaths["deaths"] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths by Region", "params": {"region": f"{region}"}}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_deaths_by_country_year(country, year):
    try:
        deaths = {"deaths": 0}

        for row in db:
            if row[2] == country and row[0][:4] == year:
                deaths["deaths"] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths by Country and Year", "params": {"region": f"{country}", "year": f"{year}"}}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_deaths_by_region_year(region, year):
    try:
        deaths = {"deaths": 0}

        for row in db:
            if row[3] == region and row[0][:4] == year:
                deaths["deaths"] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths by Region and Year", "params": {"region": f"{region}", "year": f"{year}"}}

    except Exception as e:
        return {"success":False,"error": str(e), "params": {"region": f"{region}", "year": f"{year}"}}
    
# ============================== CASES HELPER ============================== #
def get_cases():
    try:
        cases = 0            

        for row in db:            
            cases += int(row[4])

        return {"data":cases,"success":True,"message":"Total cases"}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_cases_by_all_countries():
    try:
        cases = {}            

        for row in db:
            if not row[2] in cases:
                cases[row[2]] = 0
            
            cases[row[2]] += int(row[4])

        return {"data":cases,"success":True,"message":"cases by Country"}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_cases_by_country(country):
    try:
        cases = {f"{country}": 0}

        for row in db:
            if row[2] == country:
                cases[country] += int(row[4])

        return {"data": cases, "success": True, "message": "cases by Country", "params": {"country": f"{country}"}}

    except Exception as e:
        return {"success": False, "error": str(e)}
    
def get_cases_by_all_regions():
    try:
        cases = {}            

        for row in db:
            if not row[3] in cases:
                cases[row[3]] = 0
            
            cases[row[3]] += int(row[4])

        return {"data":cases,"success":True,"message":"cases by Region"}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_cases_by_region(region):
    try:
        cases = {"cases": 0}

        for row in db:
            if row[3] == region:
                cases["cases"] += int(row[4])

        return {"data":cases,"success":True,"message":"cases by Region", "params": {"region": f"{region}"}}

    except Exception as e:
        return {"success":False,"error": str(e), "params": {"region": f"{region}"}}

def get_cases_by_country_year(country, year):
    try:
        cases = {"cases": 0}

        for row in db:
            if row[2] == country and row[0][:4] == year:
                cases["cases"] += int(row[4])

        return {"data":cases,"success":True,"message":"cases by Country and Year", "params": {"region": f"{country}", "year": f"{year}"}}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_cases_by_region_year(region, year):
    try:
        cases = {"cases": 0}

        for row in db:
            if row[3] == region and row[0][:4] == year:
                cases["cases"] += int(row[4])

        return {"data":cases,"success":True,"message":"cases by Region and Year", "params": {"region": f"{region}", "year": f"{year}"}}

    except Exception as e:
        return {"success":False,"error": str(e), "params": {"region": f"{region}", "year": f"{year}"}}
    
# ============================== AGGREGATE HELPER ============================== #
def get_max_deaths():
    try:
        countries = get_deaths_by_all_countries()
        data = countries["data"]

        _max = max(data, key = data.get)
        
        return {_max: data[_max]}
    except Exception as e:
        return {"success":False,"error": str(e)}

def get_max_deaths_by_years(year1, year2):
    try:
        countries = get_deaths_all_countries_by_years(year1, year2)
        data = countries["data"]

        _max = max(data, key = data.get)
        
        return {_max: data[_max]}
    except Exception as e:
        return {"success":False,"error": str(e)}


def get_min_deaths():
    try:
        countries = get_deaths_by_all_countries()
        data = countries["data"]

        _min = min(data, key = data.get)
        
        return {_min: data[_min]}
    except Exception as e:
        return {"success":False,"error": str(e)}

def get_min_deaths_by_years(year1, year2):
    try:
        countries = get_deaths_all_countries_by_years(year1, year2)
        data = countries["data"]

        _min = min(data, key = data.get)
        
        return {_min: data[_min]}
    except Exception as e:
        return {"success":False,"error": str(e)}

def get_avg_deaths():
    try:
        countries = get_deaths_by_all_countries()
        data = countries["data"]

        sum = 0
        
        for country in data:
            sum += data[country]
      
        return {"avg_deaths": floor(sum / len(data))}
    except Exception as e:
        return {"success":False,"error": str(e)}