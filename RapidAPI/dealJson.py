import json
from datetime import datetime

# 時間格式轉換
def format_datetime(iso_string):
    dt = datetime.fromisoformat(iso_string.replace('Z', '+00:00'))
    return dt.strftime('%Y-%m-%d %I:%M %p')

# readJson
with open('RapidAPI\\flight_data.json', 'r') as file:
    data = json.load(file)


#另一個list for後續排序
list=[]
#航空公司名字置換
replace_dict={
    "Tigerair Taiwan":"虎航",
    "Peach":"樂桃"
}


for i in range(len(data['data']['itineraries'])):
    dic={}
    dic['go_departport'] = data['data']['itineraries'][i]['legs'][0]['origin']['displayCode']
    dic['go_departtime'] = format_datetime(data['data']['itineraries'][i]['legs'][0]['departure'])
    dic['go_arriveport'] = data['data']['itineraries'][i]['legs'][0]['destination']['displayCode']
    dic['go_arrivetime'] = format_datetime(data['data']['itineraries'][i]['legs'][0]['arrival'])
    dic['go_carrier'] = data['data']['itineraries'][i]['legs'][0]['carriers']['marketing'][0]['name']

    dic['back_departport'] = data['data']['itineraries'][i]['legs'][1]['origin']['displayCode']
    dic['back_departtime']= format_datetime(data['data']['itineraries'][i]['legs'][1]['departure'])
    dic['back_arriveport'] = data['data']['itineraries'][i]['legs'][1]['destination']['displayCode']
    dic['back_arrivetime']=format_datetime(data['data']['itineraries'][i]['legs'][1]['arrival'])
    dic['back_carrier'] = data['data']['itineraries'][i]['legs'][1]['carriers']['marketing'][0]['name']
    dic['formateprice']=data['data']['itineraries'][i]['price']['formatted']
    dic['rawprice']=data['data']['itineraries'][i]['price']['raw']
    list.append(dic)

#用raw price進行排序
list_sort=sorted(list,key=lambda x:x['rawprice'])


for i in list_sort:
    # 用dict來get value值找不到的話返回原始值
    go_carrier=replace_dict.get(i['go_carrier'],i['go_carrier'])
    back_carrier=replace_dict.get(i['back_carrier'],i['back_carrier'])
    
    print('去程班機:',go_carrier)
    print(i['go_departport']+"->"+i['go_arriveport'])
    print(i['go_departtime']+"->"+i['go_arrivetime'])
    print('回程班機:',back_carrier)
    print(i['back_departport']+"->"+i['back_arriveport'])
    print(i['back_departtime']+"->"+i['back_arrivetime'])
    print(i['formateprice'])
    print('----------------------------------------------------------------')





    