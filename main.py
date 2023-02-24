import requests
import json
import sys
import os


src_lang = "EN"
dst_lang = "JA"
input_text = None

def setFileOption(s):
	global input_text
	path = os.getcwd() + "/" + s
	if not os.path.exists(path):
		print("file doesn't exist.")
		exit(1)
	if not os.path.isfile(path):
		print("invalid file.")
		exit(2)
	with open (path) as f:
		input_text = f.read()

def setReverseOption():
	global src_lang
	global dst_lang
	src_lang = "JA"
	dst_lang = "EN"

def checkOptions(argv):
	for i in range(len(argv)):
		option = argv[i][:2]
		if option == "-r":
			setReverseOption()
		if option == "-f":
			setFileOption(argv[i + 1])

def httpReq(input_text):
	url = "https://api-free.deepl.com/v2/translate"
	headers = {'Authorization': 'DeepL-Auth-Key b8f8bde9-4816-53cf-5bdd-b13bcc57f0e7:fx'}
	data = {'text': input_text, 'target_lang': dst_lang}
	res = requests.post(url=url, headers=headers, data=data)
	res_json = res.json()
	return res_json['translations'][0]['text']

def output(ret):
#	print("---------- translations ----------")
	print(ret)

def main():
	global input_text
	checkOptions(sys.argv)
	if input_text is None:
		input_text = input()
	ret = httpReq(input_text)
	output(ret)

if __name__ == "__main__":
	main()

