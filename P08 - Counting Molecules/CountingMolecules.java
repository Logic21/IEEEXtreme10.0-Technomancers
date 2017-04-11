import java.io.*;
import java.util.*;
//Given a certain amount of carbon, hydrogen, and oxygen molecules...
//How many CO2, H2O, and Glucose molecules are there
public class Solution {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);
        String[] inputArr = reader.nextLine().split(" ");
        long[] numArr = new long[3];
        for (int i = 0; i < 3; i++)
        {
        	numArr[i] = Long.parseLong(inputArr[i]);
        }
    	
        double numC = numArr[0];
        double numH = numArr[1];
        double numO = numArr[2];
        
        double numCO2 = ((1.0/4.0) * (2 * numO - numH));
    	double numH2O = ((1.0/4.0) * (-4*numC + numH + 2*numO));
    	double numGluc = ((1.0/24.0) * (4 * numC + numH - 2*numO));
    	
    	if ( (numCO2 % 1 == 0) && (numH2O % 1 == 0) && (numGluc % 1 == 0) && (numCO2 >= 0) && (numH2O >= 0) && (numGluc >= 0) )
    	{
    		System.out.println( (long) numH2O + " " + (long) numCO2 + " " + (long) numGluc);
    	}
    	else
    	{
    		System.out.println("Error");
    	}
    	
    	/* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}