import json
import requests
from stegano import lsb
import pandas as pd

image_path = "images/profileimg.png"
decoded_data = lsb.reveal(image_path)
decoded_data = json.loads(decoded_data)
new_data = decoded_data["users"]
print("NAME | CITIZENSHIP | PHONE |ADDRESS |EMAIL | ACCOUNT TYPE | ACCOUNT NUMBER | PIN  " ) 
for i in new_data:
    print(i[0],i[1],i[2],i[3],i[4],i[5],i[6],i[7])
            




