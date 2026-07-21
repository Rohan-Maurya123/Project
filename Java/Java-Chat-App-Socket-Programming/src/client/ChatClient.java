package client;

import common.Constants;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ChatClient {

    private Socket socket;
    private BufferedReader reader;
    private PrintWriter writer;


    public void connect() {

        try {

            socket = new Socket(Constants.HOST, Constants.PORT);

            System.out.println("======================================");
            System.out.println("      JAVA CHAT CLIENT");
            System.out.println("======================================");
            System.out.println("Connected to Server");
            System.out.println("Host : " + Constants.HOST);
            System.out.println("Port : " + Constants.PORT);
            System.out.println();
            System.out.println("Commands:");
            System.out.println("/users           -> Show active users");
            System.out.println("/msg USER TEXT   -> Private message");
            System.out.println("/exit            -> Disconnect");
            System.out.println();

            reader = new BufferedReader(
                    new InputStreamReader(socket.getInputStream())
            );

            writer = new PrintWriter(
                    socket.getOutputStream(),
                    true
            );

            Thread receiverThread =
                    new Thread(new ClientReceiver(reader));

            Thread senderThread =
                    new Thread(new ClientSender(writer));

            receiverThread.start();
            senderThread.start();

            senderThread.join();

        } catch (IOException e) {

            System.out.println(
                    "Unable to connect to server."
            );

        } catch (InterruptedException e) {

            Thread.currentThread().interrupt();

        } finally {

            disconnect();

        }

    }


    private void disconnect() {

        try {

            if (reader != null) {
                reader.close();
            }

            if (writer != null) {
                writer.close();
            }

            if (socket != null && !socket.isClosed()) {
                socket.close();
            }

            System.out.println("Disconnected successfully.");

        } catch (IOException e) {

            System.out.println(
                    "Error while closing connection."
            );

        }

    }


    public static void main(String[] args) {

        ChatClient client = new ChatClient();

        client.connect();

    }

}