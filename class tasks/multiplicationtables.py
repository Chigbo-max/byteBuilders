def multiplication_table(choice):

	print('\t''\t''\t\t\t\t\t\tMULTIPLICATION TABLE')
	print('\t   2 \t\t   3 \t\t   4 \t\t   5  \t\t   6  \t\t   7  \t\t   8  \t\t   9  \t\t   10  \t\t   11  \t\t   12')

	print(                                           )


	for column in range(1, 13, 1):
		for row in range(2, choice, 1):
			print('\t'f'{column:>2} - {column * row:<3}', end = '')
		print()	

multiplication_table(13)