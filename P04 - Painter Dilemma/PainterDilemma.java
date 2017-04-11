import java.io.*;
import java.util.*;
//A painter has 2 brushes and must spend time to switch paint for each brush.
//He paints in multiple colors: 1-9. What's the least amount of times he needs to swap?
public class Solution
{

	//public static int swaps = 0;

	public static void main(String[] args)
	{
		int swaps = 0;
		int numberOfColors;
		int[] colors;
		int numberOfCases;
		Scanner reader = new Scanner(System.in);

		numberOfCases = Integer.parseInt(reader.nextLine());

		for (int i = 0; i < numberOfCases; i++) // iterator for cases
		{
			numberOfColors = Integer.parseInt(reader.nextLine());
			colors = new int[numberOfColors];
			String colorString = reader.nextLine();
			String[] items = colorString.split(" ");
			for (int k = 0; k < numberOfColors; k++)
			{
				colors[k] = Integer.parseInt(items[k]);
			}
			Brush holder = new Brush(colors[0]);
			swaps++;
			Brush swapper = new Brush(-1);
			for (int j = 0; j < numberOfColors; j++) // iterator for colors
			{
				if ((colors[j] == holder.getPaint()) || (colors[j] == swapper.getPaint()))
				{
					continue;
				}
				else
				{
					for (int k = 0; k < 20; k++) // iterator to check swap
					{
						try
						{
							if (holder.getPaint() == colors[j + k])
							{
								break;
							}
							else if (swapper.getPaint() == colors[j + k])
							{
								Brush temp = swapper;
								swapper = holder;
								holder = temp;
								break;
							}
						}
						catch (Exception ArrayIndexOutOfBoundsException)
						{
							break;
						}
					}
					swapper.setPaint(colors[j]);
					swaps++;
				}

			}
			System.out.println(swaps);
			swaps = 0;
		}

		/*
		 * Enter your code here. Read input from STDIN. Print output to STDOUT.
		 * Your class should be named Solution.
		 */
	}

	public static void swapBrushes(Brush brush1, Brush brush2)
	{
		int temp = brush1.getPaint();
		brush1.setPaint(brush2.getPaint());
		brush2.setPaint(temp);
	}
}

class Brush
{
	private int paint;

	public Brush(int paint)
	{
		this.paint = paint;
	}

	public void setPaint(int paint)
	{
		this.paint = paint;
	}

	public int getPaint()
	{
		return paint;
	}

	/**
	 * public void swapBrush(Brush brush1, Brush brush2) { int temp =
	 * this.getPaint(); this.setPaint(brush2.getPaint()); brush2.setPaint(temp);
	 * }
	 */
}