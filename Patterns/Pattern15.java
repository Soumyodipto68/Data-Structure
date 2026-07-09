package Patterns;
import java.util.Scanner;
public class Pattern15 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the Number of Rows: ");
    int n = sc.nextInt();
    if(n<=0){
      System.out.println("You are a fucking Idiot!!!");
    }
            for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                
                // Star is printed on diagonals
                // of nxn matrix
                if (i == j || i + j == n + 1)
                    System.out.print("*");
                else
                    System.out.print(" ");
            }
            System.out.println();
        }
      sc.close();  
    }
  }

