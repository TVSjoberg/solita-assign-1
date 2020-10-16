import requests
import datetime as dt
import pandas as pd


TOKEN = 'Q0A6ArPu8Ra4dqRSXTppIrZcJrlhb2P65UnqJ2gc'

# Enter time as (year, month, day)
start_time = dt.datetime(2019, 1, 1)
end_time = dt.datetime(2019, 5, 1)

# Find out how to format date to the following format: '2019-05-06T10:15:27Z'
start_time_formatted = 0
end_time_formatted = 1

#tjohotjohej

def get_data_from_api():
    '''
    Use this function to get data from the API and returns it as dict
    '''
    fingrid_url = 'https://api.fingrid.fi/v1/variable/75/events/json?start_time={}&end_time={}'.format(
        start_time_formatted, end_time_formatted)
    token = TOKEN
    headers = {'x-api-key': '{}'.format(token)}
    response = requests.get(fingrid_url, headers=headers)
    return response.json()
