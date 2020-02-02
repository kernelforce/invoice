import requests
from config import service_name, service_port

url = "http://localhost:{}/{}".format(service_port, service_name)

data = {'enctype': 'multipart/form-data'}
files = {'file': open('E:\\python\\invoice\\test-invoice\\test.jpg', 'rb')}

reponse = requests.post(url, data=data, files=files)

text = reponse.text

print(text)

