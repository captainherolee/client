import argparse,logging
from config import *
from mdas.apis import MdasAPI

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

def select_api(method_mapping):
    print("Available APIs:")
    for index, (method, api) in enumerate(method_mapping):
        print(f"{index}:{STRING_FORMATTER[method]} {api}")
    selected_api = input("Please enter the API you want to use: ")
    return selected_api

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', '--server', dest='server', default='10.113.54.119:5050', help='Host URL')
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
        method, api = MdasAPI.method_mapping[int(index)]
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