import java.util.Scanner;

public class HelloScanner{
    public static void main(String[] args){
        //ui = input("message")
        Scanner ui = new Scanner(System.in);
        System.out.println("What's your grade (number grade)?");
        int number1 = ui.nextInt();
        int number2 = ui.nextInt();
        int number3 = ui.nextInt();
        int number4 = ui.nextInt();
        int number5 = ui.nextInt();
        int total = number1+number2+number3+number4+number5/5;
        System.out.println("Your GPA is: "+total);

    }
}