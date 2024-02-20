import json
import requests
from stegano import lsb
import pandas as pd

image_path = "images/profileimg.png"
# decoded_data = lsb.reveal(image_path)
# decoded_data = json.loads(decoded_data)

# voting_system = decoded_data
# candidate_name = "Candidate2"
# vote_count = 0
# new_data = [candidate_name,vote_count]


# voting_system["Candidate"].append(new_data)

# json_data = json.dumps(voting_system)
# print("ENCODED",json_data)
# # Encode the JSON data into the image using least significant bit (LSB) method
# encoded_image = lsb.hide(image_path, json_data)
# encoded_image.save(image_path)

decoded_data = lsb.reveal(image_path)
decoded_data = json.loads(decoded_data)
new_data = decoded_data["users"]
print("NAME | CITIZENSHIP | PHONE |ADDRESS |EMAIL | ACCOUNT TYPE | ACCOUNT NUMBER | PIN  " ) 
for i in new_data:
    print(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            




