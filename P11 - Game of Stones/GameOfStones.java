import java.io.*;
import java.util.*;
//A game with multiple stones in multiple piles
//Each player takes stones until there are none left
public class Solution {

    public static void main(String[] args) {
		Scanner reader = new Scanner(System.in);
		int t = Integer.parseInt(reader.nextLine());
		for (int caseCount = 0; caseCount < t; caseCount++)
		{
			String currentWinner = "Bob";
			int gameCount = Integer.parseInt(reader.nextLine());
			for (int games = 0; games < gameCount; games++)
			{
				long pileCount = Long.parseLong(reader.nextLine());
		        String[] inputArr = reader.nextLine().split(" ");
		        long[] numArr = new long[(int) pileCount];
		        for (int i = 0; i < pileCount; i++)
		        {
		        	numArr[i] = Long.parseLong(inputArr[i]);
		        }
		        
		        for (int i = 0; i < pileCount; i++)
		        {
		        	long pileAmount = numArr[i];
		        	if ( (pileAmount - 1) % 4 == 0)
		        	{
		        		//current winner unchanged
		        	}
		        	else if ( (pileAmount - 1) % 4 == 2)
		        	{
		        		if (currentWinner.equals("Bob"))
		        			currentWinner = "Alice";
		        		else currentWinner = "Bob";
		        	}
		        	else
		        	{
		        		System.out.println("\"Error\"");
		        	}
		        }
			}
			System.out.println(currentWinner);
		}
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
    }
}