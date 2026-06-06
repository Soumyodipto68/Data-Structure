package Patterns;

import java.util.Scanner;

public class Pattern6 {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    System.out.println("Enter the Rows: ");
    int n = sc.nextInt();
    if(n <= 0){
      System.out.println("You are a Fucking Idiot!!!");
    }
    for(int i=1;i<=n;i++){
      for(int j=1;j<=n;j++){
        if(i == 1 || j == 1 || j == n || i == n){
          System.out.print("*");
        }else{
          System.out.print(" ");
        }
      }
      System.out.println();
    }
    sc.close();
  }
}
