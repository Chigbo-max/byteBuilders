import java.util.Scanner;

public class ReverseAndPalindrome{

	public static void main(String... args){
		Scanner userInput = new Scanner(System.in);
		System.out.print("Enter a number: ");
		int number = userInput.nextInt();

		System.out.print(is_palindrome(number));
	}

	public static int reverse(int number){
	int reverse = 0;
	while(number != 0){
		reverse = (reverse * 10) + (number % 10);
		number = number/10;
		}
	return reverse;
	}


	public static String is_palindrome(int number){
	return (reverse(number) == number)? "Number is a palindrome" : "Number is not a palindrome";

	}



}
