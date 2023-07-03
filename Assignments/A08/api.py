
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from helpers import *




description = """
## 4883-SoftwareTools
### Data on COVID-19
"""


app = FastAPI(

    description=description,

)

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

@app.get("/max_deaths")
async def max_deaths():
    """Gets the country with the most deaths, and how many there were."""

    return get_max_deaths()

@app.get("/max_deaths_by_years/{year1}/{year2}")
async def max_deaths_by_years(year1: int, year2: int):
    """Gets the country with the most deaths, and how many there were between given years. Year order does not matter."""

    return get_max_deaths_by_years(year1, year2)

@app.get("/min_deaths")
async def min_deaths():
    """Gets the country with the least deaths, and how many there were."""

    return get_min_deaths()

@app.get("/min_deaths_by_years/{year1}/{year2}")
async def min_deaths_by_years(year1: int, year2: int):
    """Gets the country with the least deaths, and how many there were between given years. Year order does not matter."""

    return get_min_deaths_by_years(year1, year2)

@app.get("/avg_deaths")
async def avg_deaths():
    """Gets the average deaths between all countries."""

    return get_avg_deaths()


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