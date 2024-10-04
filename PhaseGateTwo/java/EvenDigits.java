public class EvenDigits{
	public static void main(String... args){


	

	for(int number = 1000; number <= 3000; number++){

	int firstNumber = number % 10;
	int firstNumberExtraction = number / 10;
	int secondNumber  = firstNumberExtraction % 10;
	int secondNumberExtraction = firstNumberExtraction / 10;
	int thirdNumber = secondNumberExtraction % 10;
	int thirdNumberExtraction = secondNumberExtraction / 10;
	int fourthNumber = thirdNumberExtraction % 10;

	if(firstNumber % 2 == 0 && secondNumber % 2 == 0 && thirdNumber % 2 == 0 && fourthNumber % 2 == 0) System.out.print(number + ",");


		}

	
	}

}