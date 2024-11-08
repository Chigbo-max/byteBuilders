print("""

0 Sunday
1 Monday
2 Tuesday
3 Wedneday
4 Thursday
5 Friday
6 Saturday

"""
)


todays_day = int(input("Enter today's day: "))

number_of_days_after_today = int(input("Enter future day: "))

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]


future_day = (todays_day + number_of_days_after_today) % 7 

print(f'Today is {days[todays_day]} and the future day is {days[future_day]}')



