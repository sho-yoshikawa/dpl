import requests
import json
import sys

input_text = input()

for argv in sys.argv:
	option = argv[:2]
	if option == "-s":
		print(option)
	if option == "-d":
		print(option)
	if option == "-f"
		print(option)

src_lang = "EN"
dst_lang = "JA"

url = "https://api-free.deepl.com/v2/translate"
headers = {'Authorization': 'DeepL-Auth-Key ???????????????????????????'}
data = {'text': input_text, 'target_lang': dst_lang}

res = requests.post(url=url, headers=headers, data=data)

res_json = res.json()
print("---------- translations ----------")
print(res_json['translations'][0]['text'])

