import java.util.Random;
import java.util.Scanner;

public class Inputs {
    public static void main(String[] args){
        Scanner sc=new Scanner(System.in);
        System.out.print("Enter the some input: ");
        int rno = sc.nextInt();
        System.out.println("Your roll no is: "+rno);

        String Name = sc.next();
        System.out.print(Name);
    }
}
