package Patterns;

import java.util.Scanner;

public class Pattern1 {
  public static void main(String[] args) {
  Scanner scanner = new Scanner(System.in);
  System.out.print("Enter the Number of Lines: ");
  int n = scanner.nextInt();
    if(n<=0){
      System.out.println("You are a fucking Idiot");
    }
    for(int i=0;i<n;i++ ){
       for(int j=0;j<=i;j++){
          System.out.print("* ");
       }
       System.out.println();
    }
     scanner.close();
  }

}
