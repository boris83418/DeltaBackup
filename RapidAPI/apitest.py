import requests
import json
url = "https://sky-scanner3.p.rapidapi.com/flights/search-roundtrip"

querystring = {"fromEntityId":"HND","toEntityId":"TPE","departDate":"2024-09-02","returnDate":"2024-09-06","market":"US","locale":"en-US","currency":"TWD","stops":"direct","adults":"1","infants":"0","cabinClass":"economy"}

headers = {
	"x-rapidapi-key": "130dbd3002mshb0a1497759e83bep1b6bf3jsn46a0cd257b33",
	"x-rapidapi-host": "sky-scanner3.p.rapidapi.com"
}

# 發起request
response = requests.get(url, headers=headers, params=querystring)

# 檢查請求狀況
if response.status_code == 200:
    # 確認JSON響應狀況
    data = response.json()

    # JSON寫入數據
    with open('flight_data.json', 'w') as file:
        json.dump(data, file, indent=4)  # 格式化JSON輸出
else:
    print(f"Error: {response.status_code}")