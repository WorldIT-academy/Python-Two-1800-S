import requests
#
from .read_json import read_json
from .write_json import create_json
#
import json
#
data_api = read_json(name_file= 'config_api.json')
#
API_KEY = data_api['api_key']
#
def requests_api(count: int= 0):
    CITY_NAME = data_api['city_name'][count]
    #
    URL = data_api['config_weather'].format(CITY_NAME, API_KEY)
    #
    response = requests.get(URL)
    #
    if response.status_code == 200:
    
        #
        data_dict = json.loads(response.content)
        #
        create_json(name_file= f"config_weather_{CITY_NAME}.json", name_dict= data_dict)
        # print(json.dumps(data_dict, indent= 4, ensure_ascii= False))