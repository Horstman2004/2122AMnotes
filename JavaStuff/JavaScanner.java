import java.util.Scanner;

public class HelloScanner{
    public static void main(String[] args){
        //ui = input("message")
        Scanner ui = new Scanner(System.in);
        System.out.println("What's your name?");
        String name = ui.nextline();
        System.out.println("Howdy"+name);

    }
}