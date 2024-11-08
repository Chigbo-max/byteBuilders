print('''

0 Sunday
1 Monday
2 Tuesday
3 Wednesday
4 Thursday
5 Friday
6 Saturday

''')

number = int(input("Enter a number: "))

def display_days_of_the_week(number):
	days = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

	if(number < 0 ):
		number = -(number)

	future_day = number % 7

	return days[future_day]


print(display_days_of_the_week(number))
