# import requests
# import json
# URL="http://127.0.0.1:8000/studentapi"

# def get_data(id=None):          #if id is pass the it will be replace None to that id
#     data={}     #empty dictionary to hold value
#     if id is not None:    #if id id having value than it will go inside
#         data = {'id':id}   #ex:data={'id':2}


#     # python data converts into json data
#     json_data=json.dumps(data)
#     print(f'\n\n\n\n{json_data}\n\n\n\n ')
#     # extract the data
#     r=requests.get(url=URL , data=json_data)
#     print(f'\n\n\n\n{r}\n\n\n\n ')
#     # convert into json format
#     data=r.json()
#     print("data",data)

# get_data()
