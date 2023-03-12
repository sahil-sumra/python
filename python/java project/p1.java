import java.lang.*;
import java.util.Scanner;

public class p1
{
	public static void main (String[] args)
	{ 
		Scanner in = new Scanner(System.in);
		System.out.print("enter num1: ");
		int num1 = in.nextInt();
		System.out.print("enter num2: ");
		int num2=in.nextInt();
		System.out.println(num1+" + "+num2+" = " +(num1+num2));
		System.out.println(num1+" - "+num2+" = "+(num1 - num2));

	}
}