##  Assignment 8 - Fast Api with Covid Data
### Kolten Pulliam

## <p>&nbsp;</p>

## Description
### This program creates an api using FastApi to allow the user to query information about COVID-19.

| Link                                                                                                          | Assignment Description |
| ------------------------------------------------------------------------------------------------------------- | ---------------------- |
| [api.py](https://github.com/klpulliam-37/4883-SoftwareTools-Pulliam/tree/main/Assignments/A08/api.py)         | Routes File            |
| [helpers.py](https://github.com/klpulliam-37/4883-SoftwareTools-Pulliam/tree/main/Assignments/A08/helpers.py) | Implementation File    |
| [data.csv](https://github.com/klpulliam-37/4883-SoftwareTools-Pulliam/tree/main/Assignments/A08/data.csv)     | COVID-19 Data          |

## <p>&nbsp;</p>

# Getting Started
## Start Uvicorn
{
    uvicorn api:app --reload
}
### Looking at the command above, 'api' is the name of your FastAPI python file, and 'app' is the name of the variable containing the instance of a FastAPI object.

## <p>&nbsp;</p>

# Deaths Routes

## Total Deaths
### Gets the total number of deaths.
- **Params:**
    - None
- **Returns:**
    - (dictionary) : Contains data on the total number of deaths

### Example:

[http://localhost:8000/deaths/](http://localhost:8000/deaths/)

### Response:

    {
        "data": 6945714,
        "success": true,
        "message": "Total Deaths"
    }

##### <p>&nbsp;</p>

## Deaths by Country
### Gets the total number of deaths given a country.
- **Params:**
    - country: string
- **Returns:**
    - (dictionary) : Contains data on the number of deaths for a given country.

### Example:

[http://localhost:8000/deaths_by_country/Ireland](http://localhost:8000/deaths_by_country/Ireland)

### Response:

    {
        "data": {
            "Ireland":  9028
        },
        "success":  true,
        "message":  "Deaths by Country",
        "params":   {
            "country":  "Ireland"
        }
    }

##### <p>&nbsp;</p>

## Deaths by Region
### Gets the total number of deaths given a region.
- **Params:**
    - region: string
- **Returns:**
    - (dictionary) : Contains data on the number of deaths for a given region.

### Example:

[http://localhost:8000/deaths_by_region/EURO](http://localhost:8000/deaths_by_region/EURO)

### Response:

    {
        "data": {
            "deaths":  2242877
        },
        "success":  true,
        "message":  "Deaths by Region",
        "params":  {
            "region":  "EURO"
        }
    }

##### <p>&nbsp;</p>

## Deaths by Country and Year
### Gets the total number of deaths given a country and year.
- **Params:**
    - country: string
    - year: integer
- **Returns:**
    - (dictionary) : Contains data on the number of deaths for a given country and year.

### Example:

[http://localhost:8000/deaths_by_country_year/Germany/2023](http://localhost:8000/deaths_by_country_year/Germany/2023)

### Response:

    {
        "data": {
            "deaths":  8093
        },
        "success":  true,
        "message":  "Deaths by Country and Year",
        "params":  {
            "region":  "Germany",
            "year":  "2023"
        }
    }

##### <p>&nbsp;</p>

## Deaths by Region and Year
### Gets the total number of deaths given a region and year.
- **Params:**
    - region: string
    - year: integer
- **Returns:**
    - (dictionary) : Contains data on the number of deaths for a given region and year.

### Example:

[http://localhost:8000/deaths_by_region_year/EURO/2023](http://localhost:8000/deaths_by_region_year/EURO/2023)

### Response:

    {
        "data": {
            "deaths":  59800
        },
        "success":  true,
        "message":  "Deaths by Region and Year",
        "params":  {
            "region":  "EURO",
            "year":  "2023"
        }
    }

##### <p>&nbsp;</p>

# Cases Routes
### The cases routes are exactly the same as the deaths routes, just with 'deaths' being replaced by 'cases'. <br>
### Here is an example:

## <p>&nbsp;</p>

## Total Cases
### Gets the total number of COVID-19 cases.
- **Params:**
    - None
- **Returns:**
    - (dictionary) : Contains data on the total number of cases

### Example:

[http://localhost:8000/cases/](http://localhost:8000/cases/)

### Response:

    {
        "data":  768187096,
        "success":  true,
        "message":  "Total cases"
    }

##### <p>&nbsp;</p>

# Aggregate Routes

## Max Deaths
### Gets the country with the most deaths, and returns how many deaths it had.
- **Params:**
    - None
- **Returns:**
    - (dictionary) : Contains data on the maximum deaths based on country.

### Example:

[http://localhost:8000/max_deaths/](http://localhost:8000/max_deaths/)

### Response:

    {
        "United States of America":  1127152
    }

##### <p>&nbsp;</p>

## Max Deaths by Years
### Given two years, get the country with the most deaths, and how many deaths, where the deaths occurred between the two years. It does not matter what order the years are in.
- **Params:**
    - year1: integer
    - year2: integer
- **Returns:**
    - (dictionary) : Contains data on the maximum deaths based on country and the years specified.

### Example:

[http://localhost:8000/max_deaths_by_years/2021/2023](http://localhost:8000/max_deaths_by_years/2021/2023)

### Response:

    {
        "United States of America":  775148
    }

##### <p>&nbsp;</p>

## Min Deaths
### Gets the country with the least deaths, and returns how many deaths it had.
- **Params:**
    - None
- **Returns:**
    - (dictionary) : Contains data on the minimum deaths based on country.

### Example:

[http://localhost:8000/min_deaths/](http://localhost:8000/min_deaths/)

### Response:

    {
        "Democratic People's Republic of Korea":  0
    }

##### <p>&nbsp;</p>

## Min Deaths by Years
### Given two years, get the country with the least deaths, and how many deaths, where the deaths occurred between the two years. It does not matter what order the years are in.
- **Params:**
    - year1: integer
    - year2: integer
- **Returns:**
    - (dictionary) : Contains data on the minimum deaths based on country and the years specified.

### Example:

[http://localhost:8000/min_deaths_by_years/2021/2023](http://localhost:8000/min_deaths_by_years/2022/2019)

### Response:

    {
        "Democratic People's Republic of Korea":  0
    }

##### <p>&nbsp;</p>

## Average Deaths
### Gets the average deaths between all countries.
- **Params:**
    - None
- **Returns:**
    - (dictionary) : Contains data on the average deaths based on country.

### Example:

[http://localhost:8000/avg_deaths](http://localhost:8000/avg_deaths)

### Response:

    {
        "avg_deaths":  29306
    }

##### <p>&nbsp;</p>