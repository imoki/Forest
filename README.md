# Forest（抱歉，已不再更新）
Forest专注森林无限金币脚本

## 声明  
仅供学习，不得用于其他用途  

## 原理  
通过向过去的时间段种植树木（完成学习的时间）来获取金币。

## 脚本  
* forest.py  
获取金币的脚本  
* plant.py（可忽略）  
显示植物名称及对应价格的脚本  

## 参数修改  
* data.txt(可忽略)  
专注所处的周期，用于判断是否种植了植物  
* header.txt(必填)  
填入抓包获取到的header  
* forest.py（自行修改，已有默认配置）  
种植的时间：自行修改，默认种植2022年全年植物  
```
# year:填写需要种植的年份，month填写从几月份到几月份，
# 例如(12, 0, -1)代表从12月到1月。(3, 0, -1)代表从3月到1月
year = 2022
for month in range(12, 0, -1):
```  
种植的时间间隔（可忽略）：默认3小时。2h则获取43金币，3h则获取65金币  
```
distance = 3	# 间隔3小时
```
用户id：请修改为抓包获取到的id。例如下列的id为：seekruid=2381495  
```
readUrl('https://forest-china.upwardsware.com/api/v1/plants/?seekruid=2381495&seekrua=ios-4.53.2', 'url')
readUrl('https://forest-china.upwardsware.com/api/v1/users/2381495/coin?seekruid=2381495&seekrua=ios-4.53.2', 'url_2')
```

