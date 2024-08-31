


riders_delivery = int(input("Enter number of successful delivery: "))

riders_wage_for_the_day = 0;
base_pay = 5000;
amount_per_parcel_for_deliveries_less_than_50 = 160
amount_per_parcel_for_deliveries_greater_than_or_equal_to_50_but_less_than_60 = 200
amount_per_parcel_for_deliveries_greater_than_or_equal_to_60_but_less_than_70 = 250
amount_per_parcel_for_deliveries_greater_than_or_equal_to_70 = 500

if riders_delivery < 50:
	riders_wage_for_the_day = (riders_delivery * 160) + base_pay
	print("Rider's wage for the day = ", riders_wage_for_the_day)

elif riders_delivery >= 50 and riders_delivery < 60:
	riders_wage_for_the_day = (riders_delivery * 200) + base_pay
	print("Rider's wage for the day = ", riders_wage_for_the_day)

elif riders_delivery >= 60 and riders_delivery < 70:
	riders_wage_for_the_day = (riders_delivery * 250) + base_pay
	print("Rider's wage for the day = ", riders_wage_for_the_day)

elif riders_delivery >= 70:
	riders_wage_for_the_day = (riders_delivery * 500) + base_pay
	print("Rider's wage for the day = ", riders_wage_for_the_day)




"""
PSEUDO CODE

1.prompt the accountant to enter the number of rider's successful delivery.
2.if successful delivery is less than 50%, multiply successful delivery by 160 + basepay(5k)
3.if successful delivery is greater than or equal to 50% and less than 60, multiply successful delivery by 200 + basepay(5k)
4.if successful delivery is greater than or equal to 60% and less than 70, multiply successful delivery by 250 + basepay(5k)
5.if successful delivery is greater than or equal to 70% multiply successful delivery by 500 + basepay(5k)
print the result as riders wage for the day.
"""


