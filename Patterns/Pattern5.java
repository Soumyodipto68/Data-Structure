package Patterns;
import java.util.Scanner;
public class Pattern5 {
  public static void main(String[] args) {
   int n = 0;
   Scanner sc = new Scanner(System.in);
   System.out.println("Enter the number of rows");
   n = sc.nextInt();
    if(n<=0){
      System.out.println("You are a fucking Idiot");
    }
    for(int i = 1; i<=n; i++){
      for(int j =1; j<=n; j++){
        System.out.print("* ");
      }
      System.out.println();
    } 
    sc.close();
  }
}
