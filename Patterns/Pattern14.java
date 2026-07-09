package Patterns;
import java.util.Scanner;
public class Pattern14 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the Number of Rows ");
    int n = sc.nextInt();
    if(n<=0){
      System.out.println("You are a Fucking Idiot!!!");
    }
  for (int i = 1; i <= n; i++) {
            
            // Print stars on the left
            for (int j = 1; j <= i; j++) 
                System.out.print("*");
                
            // Print spaces in the middle
            for (int j = 1; j <= 2 * (n - i); j++) 
                System.out.print(" ");
                
            // Print stars on the right
            for (int j = 1; j <= i; j++) 
                System.out.print("*");
                
            System.out.println();
        }

        // These nested loops print 
        // lower half of the pattern
        for (int i = n; i >= 1; i--) {
            for (int j = 1; j <= i; j++) 
                System.out.print("*");
            for (int j = 1; j <= 2 * (n - i); j++) 
                System.out.print(" ");
            for (int j = 1; j <= i; j++) 
                System.out.print("*");
            System.out.println();
        }
    }
  }

