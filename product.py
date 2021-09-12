import os #operating system

products = []
if os.path.isfile('products.csv'):
	print('yeah! found the file.')
	with open('products.csv', 'r', encoding='utf-8') as f:
		for line in f:
			if 'name,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)

else:
	print('We cannot find the file')

#讓使用者輸入
while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('please enter the price: ') 
	price = int(price)
	products.append([name, price])

#印出所有購買紀錄
for p in products:
	print(p[0], '的價格是', p[1])

#寫入檔案
with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('name,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
