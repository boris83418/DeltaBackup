import requests
import json
url = "https://sky-scanner3.p.rapidapi.com/flights/search-roundtrip"

querystring = {"fromEntityId":"HND","toEntityId":"TPE","departDate":"2024-09-02","returnDate":"2024-09-06","market":"US","locale":"en-US","currency":"TWD","stops":"direct","adults":"1","infants":"0","cabinClass":"economy"}

headers = {
	"x-rapidapi-key": "130dbd3002mshb0a1497759e83bep1b6bf3jsn46a0cd257b33",
	"x-rapidapi-host": "sky-scanner3.p.rapidapi.com"
}

# 发起请求
response = requests.get(url, headers=headers, params=querystring)

# 检查请求是否成功
if response.status_code == 200:
    # 获取 JSON 响应
    data = response.json()

    # 将 JSON 数据写入文件
    with open('flight_data.json', 'w') as file:
        json.dump(data, file, indent=4)  # 格式化 JSON 输出
else:
    print(f"Error: {response.status_code}")