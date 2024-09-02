age = int(input("Enter your age: "))

heart_rate_per_minute = 220 

maximum_heart_rate_per_minute = 220 - age

low_end_of_target_heart_rate = maximum_heart_rate_per_minute * 0.5
high_end_of_target_heart_rate = maximum_heart_rate_per_minute * 0.85

bpm = "beat per minute"

print("Your maximum heart rate is ", maximum_heart_rate_per_minute,"bpm")
print("The range of your target heart is ", low_end_of_target_heart_rate,"bpm", "-", high_end_of_target_heart_rate,"bpm")