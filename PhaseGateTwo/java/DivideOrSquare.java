public class DivideOrSquare{

	public static void main(String... args){
	
	double number = -5;

	System.out.printf("%.2f", divideOrSquare(number));
		
	}



	public static double divideOrSquare(double number){

		if (number < 0) number = -number;
		
	
		return (number % 5 == 0) ? Math.pow(number, 0.5) : number % 5;
		
	}

}