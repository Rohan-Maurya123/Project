package utility;

public class ConsoleHelper {

    private ConsoleHelper() {
    }

    public static void printLine() {

        System.out.println("---------------------------------------------");
    }

    public static void printHeading(String heading) {

        printLine();
        System.out.println(heading);
        printLine();
    }

}