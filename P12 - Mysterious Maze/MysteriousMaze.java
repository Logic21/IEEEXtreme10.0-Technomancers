import java.util.ArrayList;
import java.util.Scanner;

public class Maze {

	
	public static void main(String[] args) 
	{
		Maze m= new Maze();
		m.read();
	}
	
	
	int [][] map;
	int map_size;
	
	void read()
	{
		Scanner scan = new Scanner(System.in);
		int n = scan.nextInt();
		map = new int[n][n];
		map_size = n;
		int counter = 0;
		int next1 = scan.nextInt();
		while(next1!=-1)
		{
			if(roomOpen(next1-1,scan.nextInt()-1,n))
			{
				System.out.println(counter+1);
				return;
			}
			
			counter++;
			next1 = scan.nextInt();
		}
		System.out.println(-1);

	}
	boolean roomOpen(int x, int y, int n)
	{
		if(x==0)
		{
			map[x][y] = 2;
		}
		else if(x==n-1)
		{
			map[x][y] = 3;
		}
		else
		{
			map[x][y] = 1;
		}
		
		calculate(x,y);
		
		return gameFinished;
	}
	boolean gameFinished = false;
	
	void calculate(int x, int y)
	{
		int self = map[x][y];
		for(int i = x-1; i<=x+1;i++)
		{

			if(!((i==x) || (i<0) ||(i>=map_size)  ))
			{
				if(self-1>0)
				{
					if(map[i][y]==1)
					{
						map[i][y] = self;
						calculate(i,y);
					}
					if((self==2 && map[i][y]==3) || (self==3 && map[i][y]==2))
					{
						gameFinished = true;
						return;
					}
				}
				else
				{
					if(map[i][y]-1>0)
					{
						map[x][y] = map[i][y];
						calculate(x,y);
						return;
					}
				}
			
			}	
		}
		
		
		for(int i = y-1; i<=y+1;i++)
		{

			if(!((i==y) || (i<0) ||(i>=map_size)  ))
			{
				if(self-1>0)
				{
					if(map[x][i]==1)
					{
						map[x][i] = self;
						calculate(x,i);
					}
					if((self==2 && map[x][i]==3) || (self==3 && map[x][i]==2))
					{
						gameFinished = true;
						return;
					}
				}
				else
				{
					if(map[x][i]-1>0)
					{
						map[x][y] = map[x][i];
						calculate(x,y);
						return;
					}
				}
			
			}	
		}
		
	}
	
	
}
