<p>
  <a href="#">
    <img 
      alt="autocomplete" 
      src="https://raw.githubusercontent.com/natanaelfneto/django_rest_autocomplete_tree/master/assets/autocomplete-img.png"
      width="240"/>
  </a>
</p>

## Django REST Autocomplete Tree
Django app example with autocomplete suggestions based on query.\
Version: **0.4**
***

### Dependencies:
- Python 3 :snake:
- Django 2.1.3
- django-filter 2.0.0
- djangorestframework 3.9.0
- Markdown 3.0.1
- pytz 2018.7
- sortedcontainers 2.1.0

#### Deprecated dependencies:
- PyTrie 0.3.1

### API:

| URL Name      | Http Method   | Action    | URL Style             | Type of parameter |
| ---           | ---           | ---       | ---                   | ---               |
| autocomplete  | GET           | List      | /autocomplete/{query} | String            |

### How run locally:
##### :octocat: Clone the repository
```shell
git clone https://github.com/natanaelfneto/django_rest_autocomplete_tree.git
```
##### :space_invader: Create a virtual environment, activate it and install project dependencies
```shell
mkvirtualenv autocomplete
workon autocomplete
pip install -r requirements.ext
```
##### :chart_with_upwards_trend: test and run it
```shell
python src/manage.py test api
python src/manage.py runserver
```
##### :globe_with_meridians: Access url in browser:
- http://localhost:8000/autocomplete/query?format=api for REST Framework API format\
_or_
- http://localhost:8000/autocomplete/query?format=json for JSON format\
Obs: remember to channge the `query` with a string to receire autocomplete suggestions

### Example

#### Request:
```Shell
curl -X GET -H "Content-Type: application/json" http://localhost:8000/autocomplete/lee
```

#### Response:
```ShellSession
HTTP 200 OK
Allow: OPTIONS, GET
Content-Type: application/json
Vary: Accept
```
```json
{
    "patients": [
        "lee chambers",
        "lee chavez",
        "lee clark",
        "lee hanson",
        "lee price",
        "leevi anttila",
        "leevi takala"
    ]
}
```

### :clock8: :clock4: :clock7: Long runtime tests:
```shell
python src/manage.py test api --pattern="long_tests.py"
```
Obs: insted of default random values, run test on all possible values

### TODOS and possible implementations:
- :heavy_check_mark: API with Django 2 and REST Framework **[OK]**
- :heavy_check_mark: Django App to return suggestion for patients names based on query as JSON **[OK]**
- :heavy_check_mark: Implementation of automated tests **[OK]**
- :clock4: Replace csv object with a database structure **[PENDING]**
- :clock4: Replace virtual environment and requirements file with an automatic pyenv dependecies control **[PENDING]**
- :clock4: Improve tests for a broadspects sets of values **[PENDING]**

---
## CHANGELOG

### 0.4 2018-12-07
- Own implemented tree class function with inheritance of python mapping
- Node object class for tree nodes instancies
- Null class for not interesting (complete) but true results of autocomplete routine
- Replaced Pytrie library with own tree solution
- Removed unecessary migrate command from readme

### 0.3 2018-11-28
- Updated readme file
- Add requirements file
- Update commnetaries for better review on code
- Api app test to assert example request status value splited in single and all values
- Api app test to assert example request status value for all values commented due to its long runtime

## [Unreleased]

### 0.2 2018-11-27
- Added csv for patient data in ./assets/patient.csv
- Updated readme file

### 0.1 2018-11-27
- Django project created
- Django app created for api
- Api django app view for patient autocomplete suggestion created
- Api app class for patients csv data base instance created
- Api app url created
- Api app test to assert request status value created
- Api app test to assert example request data value created
- Api app test response function to reduce code repetition

### 0.0 2018-11-27
- Project folder created
- Django implemented
- Django REST Framework implemented
