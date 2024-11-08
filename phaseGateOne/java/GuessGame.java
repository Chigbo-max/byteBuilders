import java.util.Scanner;

public class GuessGame{
	public static void main(String... args){
		Scanner userInput = new Scanner(System.in);
		System.out.println("Guess a number (Note that this number is the sum of two numbers): ");
		int guess = userInput.nextInt();
		System.out.print(playGame(guess));

		}

	
	public static boolean playGame(int input){
		
		return input == displayGuess()? true : false;


		}
		
		

	public static int displayGuess(){
	
		int firstInteger = 1 + (int) (100 * Math.random());
		int secondInteger = 1 + (int) (100 * Math.random());

		int sumOfTwoIntegers = firstInteger + secondInteger;
	
	return sumOfTwoIntegers;
	
		}

}


