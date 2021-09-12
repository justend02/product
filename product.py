import os #operating system

def read_file(filename):
	products = []
	with open(filename, 'r', encoding='utf-8') as f:
		for line in f:
			if 'name,price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	return products
	
#讓使用者輸入
def user_input(products):
	while True:
		name = input('please enter product name: ')
		if name == 'q':
			break
		price = input('please enter the price: ') 
		price = int(price)
		products.append([name, price])
	print(products)
	return products

#印出所有購買紀錄
def print_product(products):
		for p in products:
			print(p[0], '的價格是', p[1])

#寫入檔案
def write_file(filename, products):
	with open(filename, 'w', encoding='utf-8') as f:
		f.write('name,price\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n')

def main(filename):
	if os.path.isfile(filename):
		print('yeah! found the file.')
		products = read_file(filename)
	else:
		print('We cannot find the file')

	products = user_input(products)
	print_product(products)
	write_file('products.csv', products)


main('products.csv')