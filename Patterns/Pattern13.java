package Patterns;

import java.util.Scanner;

public class Pattern13 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.print("Enter the Number of Rows: ");
    int n = sc.nextInt();
    if(n<=0){
      System.out.print("You are a Fucking Idiot!!!");
    }
    for(int i=0;i<n;i++){
      for(int j=n-i;j>1;j--){
        System.out.print(" ");
      }
      for(int j=0;j<=i;j++){
        System.out.print("* ");
      }
      System.out.println();
    }
    sc.close();
  }
}
