products = []
while True:
	name = input('product name: ')
	if name == 'q':
		break
	price = input('please enter the price: ') 
	products.append([name, price])
print(products)

for p in products:
	print(p[0], 's price is', p[1])