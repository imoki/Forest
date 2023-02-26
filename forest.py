import requests
import json
import re
import argparse
import random

config = {
	'url' : '',
	
	'headers' : {
		#'Accept': 'application/json, text/javascript, */*; q=0.01',
	},
	
	'data' : {},
	
	'url_2' : '',
	
	'headers_2' : {},
	
	
}

# 读取请求的url
def readUrl(url, configUrl):
	#config['url'] = url.strip()
	config[configUrl] = url.strip()
	#print(configUrl)
	#print(config['url'])
	
# 读取header
def readHeader(file, configHeaders):
	print("[+] 读取header")
	with open(file, 'r', encoding='utf-8') as f:
		items = f.readlines()
		#print(items)
		dict = {}
		for item in items:
			#str.split(str="",num=string.count(str))[n]
			#str：表示为分隔符，默认为空格，但是不能为空('')。若字符串中没有分隔符，则把整个字符串作为列表的一个元素
			#num：表示分割次数。如果存在参数num，则仅分隔成 num+1 个子字符串，并且每一个子字符串可以赋给新的变量[n]：表示选取第n个分片。注意：当使用空格作为分隔符时，对于中间为空的项会自动忽略
			#print(item.strip().split(":", 1))
			dict[item.split(":", 1)[0].strip()] = item.split(":", 1)[1].strip()
		#dict[] = 
		#print(dict)
		#config['headers'] = dict
		config[configHeaders] = dict
		#print(config['headers'])

# 读取data, json格式
def readData(file):
	print("[+] 读取data")
	with open(file, 'r', encoding='utf-8') as f:
		items = f.readlines()
		dict = items[0]
		config['data'] = dict.strip()
		#print(config['data'])

# 修改data中的字段
def changeData():
	print(config['data'])
	dictData = json.loads(config['data'])
	#{"plant":{"note":"","trees":[{"is_dead":false,"phase":4,"tree_type":81}],"end_time":"2022-07-22T11:00:36.995Z","has_left":true,"is_success":true,"tag":0,"start_time":"2022-07-22T10:50:36.995Z","room_id":0,"theme":0,"mode":"countdown"}}
	#print(dictData['plant']['end_time'])

# 修改data中的时间字段
def changeDataTime(year, month, day, hour, min, distance):
	#print(config['data'])
	dictData = json.loads(config['data'])	# 将字符串转json
	#hour = 12
	#min = 10
	second = random.randint(0,59) + round(random.random(), 3)# 随机生成妙
	dictData['plant']['start_time'] = str(year) + "-" + str(month) + "-" + str(day) + "T" + str(hour) + ":" + str(min) + ":" + str(second) + "Z" 
	dictData['plant']['end_time'] = str(year) + "-" + str(month) + "-" + str(day) + "T" + str(hour + distance) + ":" + str(min) + ":" + str(second) + "Z"
	print(dictData['plant']['start_time']) 
	config['data'] = json.dumps(dictData)	# 将json转为字符串


# 读取Cookie
def readCookie():
	print("[+] 读取Cookie")
	with open('Cookie.txt', 'r', encoding='utf-8') as f:
		global Cookie
		Cookie = f.readline().strip()
		#print(Cookie)

# 种植
def Plant():
	#print("[+] 种植")
	#print(config['url'])
	#print(config['headers'])
	#print(config['data'])
	
	response = requests.post(url = config['url'], headers = config['headers'], data = config['data'], timeout=(2,4))	#data = json.dumps(data)
	#print(response)
	if response.status_code == 200:
		pass
		#print("[+] 种植成功")
	else:
		print("[-] 种植失败")

# 获取最新的金币数目
def getCoin():
	print("[+] 金币数量：", end = " ")
	response = requests.get(url = config['url_2'], headers = config['headers_2'], timeout=(2,4))
	if response.status_code == 200:
		response = response.text
		#print(response)
		coin = json.loads(response)['coin']
		print(str(coin))
	else:
		print("[-] 获取失败")

# 购买植物
def Purchase():
	pass

# 植物id,名字，gid
def Plantname(file):
	print("[+] 读取植物参数")
	with open(file, 'r', encoding='utf-8') as f:
		items = f.readline()
		#print(items)
		#dict = {}
		all_products = json.loads(items)['all_products']
		#print(all_products)
		print("title-price-id-productable_gid")
		for product in all_products:
			#print(product)
			title = product["title"].strip()
			price = product["price"]
			id = product["id"]
			productable_gid = product["productable_gid"]
			print(title + "-" + str(price) + "-" + str(id) + "-" + str(productable_gid))

def juiceDay(year, month):
	if month in [1, 3, 5, 7, 8, 10, 12]:
		return 31
	elif month in [4, 6, 9, 11]:
		return 30
	elif month in [2]:
		if year % 4 == 0:
			return 29
		else:
			return 28
	else:
		return 0

if __name__ == '__main__':
	readUrl('https://forest-china.upwardsware.com/api/v1/plants/?seekruid=2292294&seekrua=ios-4.53.2', 'url')
	readHeader('header.txt', 'headers')
	readData('data.txt')
	readUrl('https://forest-china.upwardsware.com/api/v1/users/2292294/coin?seekruid=2292294&seekrua=ios-4.53.2', 'url_2')
	readHeader('header_2.txt', 'headers_2')
	#print(config)
	distance = 3	# 间隔3小时
	# 2h-43金币，3h-65金币
	# 请自行修改，下列参数
	# year:填写需要种植的年份，month填写从几月份到几月份，
	# 例如(12, 0, -1)代表从12月到1月。(3, 0, -1)代表从3月到1月
	year = 2022
	for month in range(12, 0, -1):
		day = juiceDay(year, month)
		#day = 28
		for day in range(day, 0, -1):
			for hour in range(0, 21, distance):
				for min in range(0, 1): #35):
					print("[+] 种植开始 ", end =" ")
					changeDataTime(year, month, day, hour, min, distance)
					Plant()
					getCoin()
	print("[+] 种植结束")
