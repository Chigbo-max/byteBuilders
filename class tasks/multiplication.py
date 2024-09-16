print('\t''\t\tMultiplication Table')

print('\t''1 \t2 \t3 \t4  \t5  \t6  \t7  \t8  \t9')


print(                                           )

print('\t''-----------------------------------------------------------------')



for column in range(1, 10, 1):

	for row in range(1, 10, 1):
		print('\t'f'{column * row:<2}', end = '  ')
	print()
