package utility;

import java.util.Scanner;

public class InputUtil {


    private static final Scanner scanner =
            new Scanner(System.in);



    public static String getString(
            String message) {


        System.out.print(message);

        return scanner.nextLine().trim();

    }



    public static int getInt(
            String message) {


        while(true) {


            try {


                System.out.print(message);


                return Integer.parseInt(
                        scanner.nextLine()
                );


            }
            catch(NumberFormatException e) {


                System.out.println(
                        "Please enter a valid number."
                );


            }

        }

    }

}