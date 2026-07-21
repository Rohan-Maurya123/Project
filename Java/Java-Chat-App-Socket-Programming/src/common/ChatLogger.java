package common;

import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintWriter;

public final class ChatLogger {

    private ChatLogger() {
    }

   
    public static synchronized void log(String message) {

        try (PrintWriter writer = new PrintWriter(
                new FileWriter(Constants.CHAT_LOG_FILE, true))) {

            writer.println("[" +
                    TimeUtil.getCurrentTimestamp() +
                    "] " +
                    message);

        } catch (IOException e) {

            System.out.println(
                    "Unable to write chat log : "
                            + e.getMessage());

        }

    }

}