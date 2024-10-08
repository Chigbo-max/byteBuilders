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

def display_days_of_the_week(number: int):
	days = ["Sunday","Monday", "Tcuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

	if type(number) not in [int]:
		return "Invalid input"
	if(number < 0 ):
		number = -(number)

	future_day = number % 7

	return days[future_day]


print(display_days_of_the_week(number))
