// -----------------------------------------------
// Assignment 2
// Written by: James Ferreira-Fernandez 21964216
// For COMP 248 Section P - Fall 2015
// -----------------------------------------------

import java.util.Scanner;
public class assignment2 {

	public static void main(String[] args) {
		
		Scanner kb = new Scanner(System.in);
		Scanner kb2 = new Scanner(System.in);
		Scanner kb3 = new Scanner(System.in);				// user inputs
		Scanner kb4 = new Scanner(System.in);
		Scanner kb5 = new Scanner(System.in);
		
		
		String answer, size;
		int height, width, i, j, k, w2, w3, w4, l, m, n, o, p, q, r;          //variables used in the code
		kb3.useDelimiter(" ");
		String[] splitter;
		
		i = 0;			//counter for number of houses created
		k = 1;			//starting value for a loop
		j = 1;			//starting value for a future loop
		
		//below is the header to the program
		System.out.println("--------------------------------------------------------------------------------");
		System.out.println("                   James' Silly house drawing program");				
		System.out.println("--------------------------------------------------------------------------------");
		System.out.println();
		System.out.print("What is your name? ");			//prompt for user input of their name
		
		String name = kb.nextLine();		//user's name
		System.out.println("Well " + name + ", welcome to my silly house drawing program.");
		
		do{ 		//do while loop for asking if the user wants to have a house drawn for them
			System.out.print("Do you want me to draw a simple house for you? (yes/no) ");
			answer = kb2.nextLine();
			
		} while(!answer.equals("yes") && !answer.equals("no")); 
		
		if (answer.equals("no"))		//if negative, ends the program
			{System.out.println();
			System.out.println("Sorry you decided not to have any houses drawn!");}
			
		if (answer.equals("yes"))		// if positive, begins a series of loops
			do{			//starting main outer loop, will loop every time the user wants to draw a house, will end once the user answers something other than yes at the final prompt
				System.out.print("Enter height and width of the house you want me to draw (must be even numbers): ");
				
				size = kb3.nextLine();
				
				splitter = size.split(" ");
				height = Integer.parseInt(splitter[0]);			//splitting the user inputs into 2 different variables, height and width
				width = Integer.parseInt(splitter[1]);
				
				while (height % 2 != 0 && k <=4 ){			//making sure the height is an even number, %2 = 0 means even, =/= means odd
					
					if (k == 4){ System.out.println("-->" + name + ", it seems you are having trouble entering even numbers! Program ending now.");
					System.exit(4);
					}
					System.out.println("you entered " + height + " for the height. Not an even number!");		//statements if an odd number was entered for height
					System.out.print("Please enter an even number for the height of the house ");
					height = kb4.nextInt();
					System.out.println();
					
					k++;				//gives 3 chances to input a proper height before closing the program
				}
				
				while (width % 2 != 0 && j <=4 ){			//making sure the width is an even number, same as with height
					
					if (j == 4){ System.out.println("-->" + name + ", it seems you are having trouble entering even numbers! Program ending now.");
					System.exit(4);
					}
					System.out.println("you entered " + width + " for the width. Not an even number!");
					System.out.print("Please enter an even number for the width of the house ");		//statements if an odd number was entered for the width
					width = kb5.nextInt();
					System.out.println();
						
						j++;			// gives 3 chances to input a proper width before closing the program
					}
				
				w2 = ((width / 2) - 1);		// gives the number of spaces necessary for the top of the roof to be properly centered, one less than half to account for the space taken up by the **
				
				while (w2 > 0){ 
					System.out.print(" ");		//spacing for the top of the roof
					w2--;
				}
				System.out.println("**");			//top of the roof
				
				w3 = ((width / 2) -2);			//the minus 2 accounts for the top of the roof (w2)
				w4 = ((width / 2) - 2);			//important for determining spacing between roof panels
				l = 1;							//starting value for upcoming loop
				
				
				while (l <= w3){				//outer loop for the roof
					
					m = 1;
					n = 1;
					
					while (m <= w4){ 			//first inner loop of the roof
						System.out.print(" ");		//prints out necessary spaces for left roof panel to be aligned properly
						m++;
					}
			
					System.out.print("/");			//left roof panel
					
					while (n <= (l * 2)){			//second inner loop of the roof
					System.out.print(" ");			// prints out appropriate spaces for right roof panel to be aligned
					n++;							//with every outer loop 2 extra spaces are created
					}
					
					System.out.println("\\");		//right roof panel
					l++;
					w4--;
				}
				
				o = 1;
				p = 1;				//starting points for loops for the main body of the house
				r = 1;
				

				
				while ( o <= width){			//loop for the ceiling of the main body of the house
					System.out.print("-");		//prints out appropriate number of ceiling tiles
					o++;
				}
				
				System.out.println();
				
				while (p <= height){			//outer loop for the walls of the main body
					System.out.print("|");		//left wall of the house
					
					q = 1;						//starting point of the loop, which resets with every outer loop
					
					while (q <= (width - 2)){		//inner loop for determining spaces between walls
						System.out.print(" ");		
					q++;}
					
					System.out.println("|");	//right wall of the house
					p++;
				}
					
				
				
				while ( r <= width){
					System.out.print("-");		///floor of the house
					r++;
				}
				
				System.out.println();
															
				
			i++;		//increases house count by 1 for each loop
			System.out.print(name + ", do you want me to draw another house for you (yes to continue)?");	//prompt for the creation of another house	
			answer = kb2.nextLine();
			System.out.println();
			}while(answer.equals("yes"));		//if yes will re-do the loop, if anything else, it will end the loop
	
	
			if (i == 1)
				System.out.println("Hope you like your house!");		//closing statement if one house was made
			if (i > 1)
				System.out.println("Hope you like your " + i + " houses!");		//closing statement if more than one houses were made
			System.out.println();
			System.out.println("Come back soon " + name + "...");				//farewell statement
		
		kb.close();
		kb2.close();
		kb3.close();
		kb4.close();		//closing of scanners
		kb5.close();
		
	}	



	}
