number = int(input("Enter a number between 0 and 1000: "))

thousand = number % 10
extracted_thousand = number // 10
hundred = extracted_thousand % 10
extracted_hundred = extracted_thousand // 10
ten = extracted_hundred % 10
last = number // 1000

sum = thousand + hundred + ten + last

print(sum)