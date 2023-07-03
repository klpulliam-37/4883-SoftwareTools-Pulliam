##  Assignment 8 - Fast Api with Covid Data
### Kolten Pulliam

## Description
### This program creates an api using FastApi to allow the user to query information about COVID-19.

| Link                                                                                                          | Assignment Description |
| ------------------------------------------------------------------------------------------------------------- | ---------------------- |
| [api.py](https://github.com/klpulliam-37/4883-SoftwareTools-Pulliam/tree/main/Assignments/A08/api.py)         | Routes File            |
| [helpers.py](https://github.com/klpulliam-37/4883-SoftwareTools-Pulliam/tree/main/Assignments/A08/helpers.py) | Implementation File    |
| [data.csv](https://github.com/klpulliam-37/4883-SoftwareTools-Pulliam/tree/main/Assignments/A08/data.csv)     | COVID-19 Data          |

# Getting Started
## Installing Uvicorn

# Routes Explained
## Total Deaths

### Gets the total number of deaths.
  - **Params:**
    - None
  - **Returns:**
    - (dictionary) : Contains data on the total number of deaths

  ### Example 1:

  [http://localhost:8000/deaths/](http://localhost:8000/deaths/)

  ### Response 1:

    {
        "data": 6945714,
        "success": true,
        "message": "Total Deaths"
    }

  #### Example 2:

  [http://localhost:8080/deaths/?country=Brazil&year=2023](http://localhost:8080/deaths/?country=Brazil&year=2023)

  #### Response 2:

      {
          "total": 42,
          "params": {
              "country": "Brazil",
              "year": 2023
          }
          "success": true,
      }




```
    This method will return a total death count or can be filtered by country and year.
    - **Params:**
      - country (str) : A country name
      - year (int) : A 4 digit year
    - **Returns:**
       - (dictionary) : Contains data on the total number of deaths

    # Example 1:

    [http://localhost:8080/deaths/](http://localhost:8080/deaths/)

    # Response 1:

        {
            "total": 1000000,
            "params": {
                "country": null,
                "year": null
            }
            "success": true,
        }

    #### Example 2:

    [http://localhost:8080/deaths/?country=Brazil&year=2023](http://localhost:8080/deaths/?country=Brazil&year=2023)

    #### Response 2:

        {
            "total": 42,
            "params": {
                "country": "Brazil",
                "year": 2023
            }
            "success": true,
        }

```