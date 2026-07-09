package Patterns;

import java.util.Scanner;

public class Pattern17 {
  public static void main(String[] args) {
   Scanner sc = new Scanner(System.in);
   System.out.print("Enter the Number of People: ");
   int n = sc.nextInt();
   if(n<=0){
    System.out.println("You are a fucking Idiot!!!");
   } 
           for (int i = 1; i <= 3; i++) {
            for (int j = 1; j <= n; j++) {
                // Print star if position 
                // matches a zigzag condition
                if ((i + j) % 4 == 0 || (i == 2 && j % 4 == 0))
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.println();
        }
   sc.close();     
  }
}
