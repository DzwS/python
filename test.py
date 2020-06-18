import requests
import time
requests.adapters.DEFAULT_RETRIES = 8
# try:
#     print(time.time())
#     requests.get("http://test.com", timeout=2)
# except:
#     print(time.time())

# from requests.adapters import HTTPAdapter

# s = requests.Session()
# s.mount('http://', HTTPAdapter(max_retries=5))
# s.get("http://test.com")

lis = [
    {'x': 3, 'y': 2, 'z': 1},
    {'x': 2, 'y': 1, 'z': 3},
    {'x': 1, 'y': 3, 'z': 2},
]
print(sorted(lis, key=lambda k: k.keys()))