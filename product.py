products = []
while True:
	name = input('product name: ')
	if name == 'q':
		break
	price = input('please enter the price: ') 
	num = int(price)
	products.append([name, price])
print(products)

for p in products:
	print(p[0], "'s' price is", p[1])

with open('products.csv', 'w', encoding='utf-8') as f:
	f.write('product, price\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) +'\n') #有逗號會分成兩格


