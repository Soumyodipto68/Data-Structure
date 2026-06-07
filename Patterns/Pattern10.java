package Patterns;

import java.util.Scanner;

public class Pattern10 {
   public static void main(String[] args) {
      Scanner sc = new Scanner(System.in);
      System.out.print("Enter The Number of Rows:");
      int n = sc.nextInt();
      if(n<=0){
        System.out.println("You are a Fucking Idiot!!!");
      }
      System.out.print("The Pattern is...");
      for(int i =0;i<=n;i++){
        for(int j=0;j<=n-i;j++){
          System.out.print(" ");
        }
        for(int j=0;j<i;j++){
          System.out.print("* ");
        }
        System.out.println();
      }
      sc.close();
   }
}
