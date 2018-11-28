<p>
  <a href="#">
    <img 
      alt="autocomplete" 
      src="https://raw.githubusercontent.com/natanaelfneto/django_rest_autocomplete_tree/master/assets/autocomplete.png"
      width="240"/>
  </a>
</p>

## Django REST Autocomplete Tree
Django app example with autocomplete suggestions based on query.\
Version: **0.2**
***

### Dependencies:
- Python 3 :snake:
- Django 2.1.3
- django-filter 2.0.0
- djangorestframework 3.9.0
- Markdown 3.0.1
- PyTrie 0.3.1
- pytz 2018.7
- sortedcontainers 2.1.0

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
##### :chart_with_upwards_trend: Migrate django app, test and run it
```shell
python src/manage.py migrate
python src/manage.py tests api
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

### TODOS and possible implementations:
- :heavy_check_mark: API with Django 2 and REST Framework **[OK]**
- :heavy_check_mark: Implementation of automated tests **[OK]**
- :clock4: Replace csv object with a database structure **[PENDING]**
- :clock4: Replace virtual environment and requirements file with an automatic pyenv dependecies control **[PENDING]**
