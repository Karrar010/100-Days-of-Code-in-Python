# 1. Create an Account in Pixela Using Post Function
import requests

USERNAME = "yashkun321"
TOKEN = "thisissecret123"
GRAPH_ID = "graphid123"

pixela_Endpoint = "https://pixe.la/v1/users"
user_parameters = {
    "token": TOKEN, 
    "username": USERNAME, 
    "agreeTermsOfService": "yes", 
    "notMinor": "yes"
}
# response_post = requests.post(url=pixela_Endpoint, json=user_parameters)
# print(response_post.text)


# 2. Create a graph definition
pixela_graph_endpoint = f"{pixela_Endpoint}/{USERNAME}/graphs"
graph_parameters = {
    "id": GRAPH_ID,      # It is ID for pixelation graph
    "name": "Coding Graph",    # Name of graph
    "unit": "commit",    # Unit of quantity recorded in graph
    "type": "int",    # Type of quantity
    "color": "sora"    # Display Color of pixel(in japanese)
}
# For this we also need to provide Token in a Seperate Header dictionary 
# Tokens are provided in HTTP header as a security measure to secure token value
headers = {
    "X-USER-TOKEN": TOKEN 
}

# response_graph = requests.post(url=pixela_graph_endpoint,json=graph_parameters, headers = headers) # headers is a kwargs
# print(response_graph.text)


# 3. View Your Graph
# Go to https://pixe.la/v1/users/username/graphs/graph-id.html in browser and enter
# remember to enter proper username and graph-id
from datetime import datetime
current_date = datetime.now().strftime("%Y%m%d") # Here "%Y" are format codes to get certain string output
# IF to format in your desired date
desired_date = datetime(year= 2024,month=8,day=7).strftime("%Y%m%d")
# 4. Post Data into Graph
post_data_endpoint = f"{pixela_Endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
datapost_parameter = {
    "date": current_date, # format yyyyMMdd in str:  
    "quantity": input("How many hours did you code? Ans: ")  # from 0-9 in str
}
# response_data_post = requests.post(url=post_data_endpoint,json=datapost_parameter, headers=headers)
# print(response_data_post.text)

# 5. Can View Graph Again to See Change through step 3


# 6. USE PUT Function to Update a Certain Pixel data
update_pixel = f"{pixela_Endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{desired_date}"
put_parameters = {
    "quantity" : "9"
}

response_put = requests.put(url=update_pixel,json=put_parameters,headers=headers)
print(response_put.text)


# 6. TO DELETE a Pixel in Graph
delete_pixel_endpoint = f"{pixela_Endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{desired_date}"

response_delete = requests.delete(url=delete_pixel_endpoint,headers=headers)
print(response_delete.text)