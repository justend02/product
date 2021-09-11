products = []
while True:
	name = input('please enter product name: ')
	if name == 'q':
		break
	price = input('please enter the price: ') 
	products.append([name, price])
print(products)

for p in products:
	print(p[0], '的價格是', p[1])
