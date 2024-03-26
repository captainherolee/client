from config import *

class MdasAPI:
    method_mapping = [
        {"method": POST, "api": "/common/updateBinary", "requiredData": True},
        {"method": GET, "api": "/common/updateBinaryStatus", "requiredData": True},
        {"method": GET, "api": "/common/auxInfo", "requiredData": False},
        {"method": GET, "api": "/common/auxState", "requiredData": False},
        {"method": GET, "api": "/serial/log", "requiredData": False},
        {"method": GET, "api": "/hyperuart/getPinCode", "requiredData": False},
        {"method": GET, "api": "/hyperuart/savePinCode", "requiredData": False}
    ]