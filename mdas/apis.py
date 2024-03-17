from config import *

class MdasAPI:
    method_mapping = [
        {GET, "/common/auxInfo"},
        {GET, "/common/auxState"},
        {GET, "/serial/log"},
        {GET, "/hyperuart/getPinCode"},
        {GET, "/hyperuart/savePinCode"}
    ]