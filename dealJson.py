import json

# readJson
with open('flight_data.json', 'r') as file:
    data = json.load(file)


# # print(data['data']['itineraries'])
# print(len(data['data']['itineraries']))

print("test git")
# print(arriveport)
for i in range(len(data['data']['itineraries'])):
    go_departport = data['data']['itineraries'][i]['legs'][0]['origin']['displayCode']
    go_departtime = data['data']['itineraries'][i]['legs'][0]['departure']
    go_arriveport = data['data']['itineraries'][i]['legs'][0]['destination']['displayCode']
    go_arrivetime = data['data']['itineraries'][i]['legs'][0]['arrival']
    go_carrier = data['data']['itineraries'][i]['legs'][0]['carriers']['marketing'][0]['name']

    back_departport = data['data']['itineraries'][i]['legs'][1]['origin']['displayCode']
    back_departtime= data['data']['itineraries'][i]['legs'][1]['departure']
    back_arriveport = data['data']['itineraries'][i]['legs'][1]['destination']['displayCode']
    back_arrivetime=data['data']['itineraries'][i]['legs'][1]['arrival']
    back_carrier = data['data']['itineraries'][i]['legs'][1]['carriers']['marketing'][0]['name']
    formateprice=data['data']['itineraries'][i]['price']['formatted']
    print(go_carrier)
    print(go_departport+"->"+go_arriveport)
    print(go_departtime+"->"+go_arrivetime)
    print(back_carrier)
    print(back_departport+"->"+back_arriveport)
    print(back_departtime+"->"+back_arrivetime)
    print(formateprice)
    print('----------------------------------------------------------------')
    