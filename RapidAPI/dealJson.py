import json

# readJson
with open('flight_data.json', 'r') as file:
    data = json.load(file)


# # print(data['data']['itineraries'])
# print(len(data['data']['itineraries']))
list=[]
# print(arriveport)
for i in range(len(data['data']['itineraries'])):
    dic={}
    dic['go_departport'] = data['data']['itineraries'][i]['legs'][0]['origin']['displayCode']
    dic['go_departtime'] = data['data']['itineraries'][i]['legs'][0]['departure']
    dic['go_arriveport'] = data['data']['itineraries'][i]['legs'][0]['destination']['displayCode']
    dic['go_arrivetime'] = data['data']['itineraries'][i]['legs'][0]['arrival']
    dic['go_carrier'] = data['data']['itineraries'][i]['legs'][0]['carriers']['marketing'][0]['name']

    dic['back_departport'] = data['data']['itineraries'][i]['legs'][1]['origin']['displayCode']
    dic['back_departtime']= data['data']['itineraries'][i]['legs'][1]['departure']
    dic['back_arriveport'] = data['data']['itineraries'][i]['legs'][1]['destination']['displayCode']
    dic['back_arrivetime']=data['data']['itineraries'][i]['legs'][1]['arrival']
    dic['back_carrier'] = data['data']['itineraries'][i]['legs'][1]['carriers']['marketing'][0]['name']
    dic['formateprice']=data['data']['itineraries'][i]['price']['formatted']
    dic['rawprice']=data['data']['itineraries'][i]['price']['raw']
    list.append(dic)

# print(list)
list_sort=sorted(list,key=lambda x:x['rawprice'])
print(list_sort)

for i in list_sort:
    
    print(i['go_carrier'])
    print(i['go_departport']+"->"+i['go_arriveport'])
    print(i['go_departtime']+"->"+i['go_arrivetime'])
    print(i['back_carrier'])
    print(i['back_departport']+"->"+i['back_arriveport'])
    print(i['back_departtime']+"->"+i['back_arrivetime'])
    print(i['formateprice'])
    print('----------------------------------------------------------------')





    