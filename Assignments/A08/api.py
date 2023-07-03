
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv
from datetime import datetime



description = """
## 4883-SoftwareTools
### Data on COVID-19
"""


app = FastAPI(

    description=description,

)

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
                deaths[region] += int(row[6])

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
    
def get_cases():
    try:
        cases = 0            

        for row in db:            
            cases += int(row[6])

        return {"data":cases,"success":True,"message":"Total cases"}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_cases_by_all_countries():
    try:
        cases = {}            

        for row in db:
            if not row[2] in cases:
                cases[row[2]] = 0
            
            cases[row[2]] += int(row[6])

        return {"data":cases,"success":True,"message":"cases by Country"}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_cases_by_country(country):
    try:
        cases = {f"{country}": 0}

        for row in db:
            if row[2] == country:
                cases[country] += int(row[6])

        return {"data": cases, "success": True, "message": "cases by Country", "params": {"country": f"{country}"}}

    except Exception as e:
        return {"success": False, "error": str(e)}
    
def get_cases_by_all_regions():
    try:
        cases = {}            

        for row in db:
            if not row[3] in cases:
                cases[row[3]] = 0
            
            cases[row[3]] += int(row[6])

        return {"data":cases,"success":True,"message":"cases by Region"}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_cases_by_region(region):
    try:
        cases = {"cases": 0}

        for row in db:
            if row[3] == region:
                cases[region] += int(row[6])

        return {"data":cases,"success":True,"message":"cases by Region", "params": {"region": f"{region}"}}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_cases_by_country_year(country, year):
    try:
        cases = {"cases": 0}

        for row in db:
            if row[2] == country and row[0][:4] == year:
                cases["cases"] += int(row[6])

        return {"data":cases,"success":True,"message":"cases by Country and Year", "params": {"region": f"{country}", "year": f"{year}"}}

    except Exception as e:
        return {"success":False,"error": str(e)}

def get_cases_by_region_year(region, year):
    try:
        cases = {"cases": 0}

        for row in db:
            if row[3] == region and row[0][:4] == year:
                cases["cases"] += int(row[6])

        return {"data":cases,"success":True,"message":"cases by Region and Year", "params": {"region": f"{region}", "year": f"{year}"}}

    except Exception as e:
        return {"success":False,"error": str(e), "params": {"region": f"{region}", "year": f"{year}"}}

"""
 
   /$$$$$$                                          /$$                 /$$$$$$$                        /$$                        
  /$$__  $$                                        |__/                | $$__  $$                      | $$                        
 | $$  \__/  /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$  /$$  /$$$$$$$      | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$$
 | $$ /$$$$ /$$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$ /$$_____/      | $$$$$$$/ /$$__  $$| $$  | $$|_  $$_/   /$$__  $$ /$$_____/
 | $$|_  $$| $$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/| $$| $$            | $$__  $$| $$  \ $$| $$  | $$  | $$    | $$$$$$$$|  $$$$$$ 
 | $$  \ $$| $$_____/| $$  | $$| $$_____/| $$      | $$| $$            | $$  \ $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/ \____  $$
 |  $$$$$$/|  $$$$$$$| $$  | $$|  $$$$$$$| $$      | $$|  $$$$$$$      | $$  | $$|  $$$$$$/|  $$$$$$/  |  $$$$/|  $$$$$$$ /$$$$$$$/
  \______/  \_______/|__/  |__/ \_______/|__/      |__/ \_______/      |__/  |__/ \______/  \______/    \___/   \_______/|_______/ 
                                                                                                                                   
                                                                                                                                   
                                                                                                                                   
 
"""

@app.get("/")
async def docs_redirect():
    """Api's base route that displays the information created above in the ApiInfo section."""
    return RedirectResponse(url="/docs")

@app.get("/countries/")
async def countries():

    return get_unique_countries()


@app.get("/regions/")
async def regions():

    return get_unique_regions()

@app.get("/casesByRegion/")
async def casesByRegion(year:int = None):
    """
    Returns the number of cases by region.
    """

    cases = {}
    
    for row in db:
        if year != None and year != int(row[0][:4]):
            continue
            
        if not row[3] in cases:
            cases[row[3]] = 0
        cases[row[3]] += int(row[4])    

    return {"data":cases,"success":True,"message":"Cases by Region","size":len(cases),"year":year}


"""
 
  /$$$$$$$                        /$$     /$$             /$$$$$$$                        /$$                        
 | $$__  $$                      | $$    | $$            | $$__  $$                      | $$                        
 | $$  \ $$  /$$$$$$   /$$$$$$  /$$$$$$  | $$$$$$$       | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$$
 | $$  | $$ /$$__  $$ |____  $$|_  $$_/  | $$__  $$      | $$$$$$$/ /$$__  $$| $$  | $$|_  $$_/   /$$__  $$ /$$_____/
 | $$  | $$| $$$$$$$$  /$$$$$$$  | $$    | $$  \ $$      | $$__  $$| $$  \ $$| $$  | $$  | $$    | $$$$$$$$|  $$$$$$ 
 | $$  | $$| $$_____/ /$$__  $$  | $$ /$$| $$  | $$      | $$  \ $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/ \____  $$
 | $$$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/| $$  | $$      | $$  | $$|  $$$$$$/|  $$$$$$/  |  $$$$/|  $$$$$$$ /$$$$$$$/
 |_______/  \_______/ \_______/   \___/  |__/  |__/      |__/  |__/ \______/  \______/    \___/   \_______/|_______/ 
                                                                                                                     
                                                                                                                     
                                                                                                                     
 
"""

@app.get("/deaths")
async def deaths():
    """Gets the total number of deaths."""

    return get_deaths()
    
@app.get("/deaths_by_country/{country}")
async def deaths_by_country(country: str):
    """Gets the total number of deaths by country."""

    return get_deaths_by_country(country)
    
    
@app.get("/deaths_by_region/{region}")
async def deaths_by_region(region: str):
    """Gets the total number of deaths by region."""

    return get_deaths_by_region(region)

@app.get("/deaths_by_country_year/{country}/{year}")
async def deaths_by_country_year(country: str, year: str):
    """Gets the total number of deaths by country and year."""

    return get_deaths_by_country_year(country, year)

@app.get("/deaths_by_region_year/{region}/{year}")
async def deaths_by_region_year(region: str, year: str):
    """Gets the total number of deaths by region and year."""

    return get_deaths_by_region_year(region, year)


"""
 
   /$$$$$$                                      /$$$$$$$                        /$$                        
  /$$__  $$                                    | $$__  $$                      | $$                        
 | $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$       | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$$
 | $$       |____  $$ /$$_____/ /$$__  $$      | $$$$$$$/ /$$__  $$| $$  | $$|_  $$_/   /$$__  $$ /$$_____/
 | $$        /$$$$$$$|  $$$$$$ | $$$$$$$$      | $$__  $$| $$  \ $$| $$  | $$  | $$    | $$$$$$$$|  $$$$$$ 
 | $$    $$ /$$__  $$ \____  $$| $$_____/      | $$  \ $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/ \____  $$
 |  $$$$$$/|  $$$$$$$ /$$$$$$$/|  $$$$$$$      | $$  | $$|  $$$$$$/|  $$$$$$/  |  $$$$/|  $$$$$$$ /$$$$$$$/
  \______/  \_______/|_______/  \_______/      |__/  |__/ \______/  \______/    \___/   \_______/|_______/ 
                                                                                                           
                                                                                                           
                                                                                                           
 
"""

@app.get("/cases")
async def cases():
    """Gets the total number of cases."""

    return get_cases()
    
@app.get("/cases_by_country/{country}")
async def cases_by_country(country: str):
    """Gets the total number of cases by country."""

    return get_cases_by_country(country)
    
    
@app.get("/cases_by_region/{region}")
async def cases_by_region(region: str):
    """Gets the total number of cases by region."""

    return get_cases_by_region(region)

@app.get("/cases_by_country_year/{country}/{year}")
async def cases_by_country_year(country: str, year: str):
    """Gets the total number of cases by country and year."""

    return get_cases_by_country_year(country, year)

@app.get("/cases_by_region_year/{region}/{year}")
async def cases_by_region_year(region: str, year: str):
    """Gets the total number of cases by region and year."""

    return get_deaths_by_region_year(region, year)

"""
 
   /$$$$$$                                                                /$$                     /$$$$$$$                        /$$                        
  /$$__  $$                                                              | $$                    | $$__  $$                      | $$                        
 | $$  \ $$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$  /$$$$$$    /$$$$$$       | $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$    /$$$$$$   /$$$$$$$
 | $$$$$$$$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ /$$__  $$ |____  $$|_  $$_/   /$$__  $$      | $$$$$$$/ /$$__  $$| $$  | $$|_  $$_/   /$$__  $$ /$$_____/
 | $$__  $$| $$  \ $$| $$  \ $$| $$  \__/| $$$$$$$$| $$  \ $$  /$$$$$$$  | $$    | $$$$$$$$      | $$__  $$| $$  \ $$| $$  | $$  | $$    | $$$$$$$$|  $$$$$$ 
 | $$  | $$| $$  | $$| $$  | $$| $$      | $$_____/| $$  | $$ /$$__  $$  | $$ /$$| $$_____/      | $$  \ $$| $$  | $$| $$  | $$  | $$ /$$| $$_____/ \____  $$
 | $$  | $$|  $$$$$$$|  $$$$$$$| $$      |  $$$$$$$|  $$$$$$$|  $$$$$$$  |  $$$$/|  $$$$$$$      | $$  | $$|  $$$$$$/|  $$$$$$/  |  $$$$/|  $$$$$$$ /$$$$$$$/
 |__/  |__/ \____  $$ \____  $$|__/       \_______/ \____  $$ \_______/   \___/   \_______/      |__/  |__/ \______/  \______/    \___/   \_______/|_______/ 
            /$$  \ $$ /$$  \ $$                     /$$  \ $$                                                                                                
           |  $$$$$$/|  $$$$$$/                    |  $$$$$$/                                                                                                
            \______/  \______/                      \______/                                                                                                 
 
"""



my_list = ['apple', 'banana', 'cherry', 'date', 'elderberry']

@app.get("/get_values1/")
def get_values1(index1: int=None, index2: int=None):
    try:
        value1 = my_list[index1]
        value2 = my_list[index2]
        return [value1, value2]
    except IndexError:
        return {"error": "Invalid index provided."}


@app.get("/get_values2/{index1}/{index2}")
def get_values2(index1: int, index2: int):
    try:
        value1 = my_list[index1]
        value2 = my_list[index2]
        return [value1, value2]
    except IndexError:
        return {"error": "Invalid index provided."}
    


if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=5000, log_level="debug", reload=True) #host="127.0.0.1"