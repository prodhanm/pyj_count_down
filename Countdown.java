import java.util.Scanner;

class Countdown {
    public static int countDown(int num){
        if(num == 0){
            return 0;
        }
        else if(num < 0){
            System.out.println(num);
            return countDown(num+1);
        }
        else{
            System.out.println(num);
            return countDown(num-1);
        }
    }

    public static void main(String[] args){
        Scanner inp = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = inp.nextInt();
        System.out.println("Blastoff: ");
        int result = countDown(num);
        System.out.printf("%d\n", result);
        System.out.println("Countdown complete.");
        inp.close();
    }
}