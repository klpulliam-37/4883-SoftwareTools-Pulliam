
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import csv



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


def getUniqueCountries():
    global db
    countries = {}

    for row in db:
        # print(row)
        if not row[2] in countries:
            countries[row[2]] = 0

    return list(countries.keys())

def getUniqueWhos():
    global db
    whos = {}

    for row in db:
        # print(row)
        if not row[3] in whos:
            whos[row[3]] = 0
   
    return list(whos.keys())

def getTotalDeaths():
    try:
        deaths = {}            

        for row in db:
            if not row[3] in deaths:
                deaths[row[3]] = 0
            
            deaths[row[3]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths by Country"}

    except Exception as e:
        return {"success":False,"error": str(e)}

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

    return {"countries":getUniqueCountries()}


@app.get("/whos/")
async def whos():

    return {"whos":getUniqueWhos()}

@app.get("/casesByRegion/")
async def casesByRegion(year:int = None):
    """
    Returns the number of cases by region
    ## Hello world
    - 1
    - 2
    - 3
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

    return getTotalDeaths()
    
@app.get("/deaths_by_country")
async def deaths_by_country():
    """Gets the total number of deaths."""

    
    
@app.get("/deaths_by_country")
async def deaths_by_country():
    """Gets the total number of deaths."""

    try:
        deaths = {}            

        for row in db:
            if not row[3] in deaths:
                deaths[row[3]] = 0
            
            deaths[row[3]] += int(row[6])

        return {"data":deaths,"success":True,"message":"Deaths by Country"}

    except Exception as e:
        return {"success":False,"error": str(e)}


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