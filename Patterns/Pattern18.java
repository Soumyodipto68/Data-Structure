package Patterns;

import java.util.Scanner;

public class Pattern18 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the Number of Rows: ");
    int n = sc.nextInt();
    if(n<=0){
      System.out.println("You are a fucking idiot!!!");
    }

   for(int i = n; i >= 1; i--) { 

  // Print leading spaces 
  for(int s = 0; s < n - i; s++) 
     System.out.print(" "); 

  // Print stars and inner spaces 
  for(int j = 1; j <= 2 * i - 1; j++) { 

  // Print stars at the borders and top row 
  if(j == 1 || j == 2 * i - 1 || i == n) 
     System.out.print("*"); 
  else 
    System.out.print(" "); 

  } 

  System.out.println(); 
            } 

  // Print the lower half of the hourglass 
for(int i = 2; i <= n; i++) { 
     // Print leading spaces 
for(int s = 0; s < n - i; s++) 
System.out.print(" "); 

// Print stars and inner spaces 
 for(int j = 1; j <= 2 * i - 1; j++) { 
// Print stars at the borders and bottom row 
 if(j == 1 || j == 2 * i - 1 || i == n) 
    System.out.print("*"); 
 else 
     System.out.print(" "); 

  } 

  System.out.println(); 
   }
   sc.close(); 
  }
}
