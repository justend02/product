products = []
while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('please enter the price: ') 
	price = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('name,price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + '\n')
