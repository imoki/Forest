# 显示植物名称及对应价格的脚本
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

if __name__ == '__main__':
	Plantname("plant.txt")
	
