import argparse,logging
from config import *
from mdas.apis import MdasAPI
import requests
import sys

def set_logger(log_level=''):
    log = logging.getLogger('mdas client')
    formatter = logging.Formatter(LOG_PREFIX)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    log.addHandler(stream_handler)
    if log_level == 'debug':
        log.setLevel(level=logging.DEBUG)
    elif log_level == 'info':
        log.setLevel(level=logging.INFO)
    else:
        pass
    
    return log

def select_api(maps):
    print("Available APIs:")
    for index, map in enumerate(maps):
        print(f"{index}:{STRING_FORMATTER[map['method']]} {map['api']}")
    selected_api = input("Please enter the API you want to use: ")
    return selected_api

def run(server, api, method, data):
    headers={"Content-Type": "application/json"}
    
    if method == GET:
        response = requests.get("http://"+server+api, headers=headers)
    elif method == POST:
        print("called post")
        response = requests.post("http://"+server+api, headers=headers)
    elif method == PUT:
        response = requests.put("http://"+server+api, headers=headers)
    else:
        sys.exit()
    
    print(response.status_code)
    print(response.text)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', dest='server', default='127.0.0.1:5050', help='Host URL')
    parser.add_argument('--api', dest='api', default='', help='API')
    parser.add_argument('-m', '--method', dest='method', default=0, help='Method')
    parser.add_argument('--log', dest='log_level', default='debug', help='Set logging level')
    parser.add_argument('-d', '--data', dest='data', default='', help='Data')
    
    args = parser.parse_args()
    
    log = set_logger(log_level=args.log_level)
    log.info('Start mdas client...')
    
    if args.server == '':
        server = input('''please input the server ip address: 
                          ex)10.113.54.119:5050 ''')
    else:
        server = args.server
        
    if args.api == '':
        index = select_api(MdasAPI.method_mapping)
        value = MdasAPI.method_mapping[int(index)]
        api = value['api']
        method = value['method']
    else:
        api = args.api
        method = args.method
    
    data = args.data
    
    print('''    ==============SYSTEM LOG==============
    Server URL: {}
    API: {}
    Method: {}
    Data: {}
    ======================================'''.format(server, api, STRING_FORMATTER[method], data))
    
    run(server, api, method, data)