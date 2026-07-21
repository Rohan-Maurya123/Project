package client;

import common.Constants;

import java.io.PrintWriter;
import java.util.Scanner;

public class ClientSender implements Runnable {

    private final PrintWriter writer;
    private final Scanner scanner;

    public ClientSender(PrintWriter writer) {
        this.writer = writer;
        this.scanner = new Scanner(System.in);
    }

    @Override
    public void run() {

        try {

            while (true) {

                String message = scanner.nextLine();

                if (message == null) {
                    continue;
                }

                message = message.trim();

                if (message.isEmpty()) {
                    continue;
                }

                writer.println(message);

                if (message.equalsIgnoreCase(Constants.EXIT_COMMAND)) {
                    break;
                }
            }

        } catch (Exception e) {

            System.out.println("Unable to send message.");

        } finally {

        
            writer.close();

        }
    }

}