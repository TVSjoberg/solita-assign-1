import requests
import datetime as dt
import pandas as pd


TOKEN = 'Q0A6ArPu8Ra4dqRSXTppIrZcJrlhb2P65UnqJ2gc'

# Enter time as (year, month, day)
start_time = dt.datetime(2019, 1, 1)
end_time = dt.datetime(2020, 1, 1)

# Find out how to format date to the following format: '2019-05-06T10:15:27Z'
start_time_formatted = start_time.isoformat() + 'Z'
end_time_formatted = end_time.isoformat() + 'Z'

#tjohotjohej

def get_data_from_api(var_id):
    '''
    Use this function to get data from the API and returns it as dict
    '''
    fingrid_url = 'https://api.fingrid.fi/v1/variable/{}/events/json?start_time={}&end_time={}'.format(str(var_id),
        start_time_formatted, end_time_formatted)
    token = TOKEN
    headers = {'x-api-key': '{}'.format(token)}
    response = requests.get(fingrid_url, headers=headers)
    return response.json()
