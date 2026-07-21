package server;

import common.Constants;

import java.io.IOException;
import java.net.ServerSocket;
import java.net.Socket;

public class ChatServer {

    private ServerSocket serverSocket;
    private final ServerManager serverManager;

    public ChatServer() {
        serverManager = new ServerManager();
    }

    public void startServer() {

        try {

            serverSocket = new ServerSocket(Constants.PORT);

            System.out.println("======================================");
            System.out.println("      JAVA CHAT SERVER STARTED");
            System.out.println("======================================");
            System.out.println("Host : " + Constants.HOST);
            System.out.println("Port : " + Constants.PORT);
            System.out.println(Constants.SERVER_STARTED);
            System.out.println("Waiting for clients...");
            System.out.println();

            while (true) {

                Socket clientSocket = serverSocket.accept();

                System.out.println(
                        "New client connected : "
                                + clientSocket.getInetAddress().getHostAddress()
                );

                ClientHandler clientHandler =
                        new ClientHandler(clientSocket, serverManager);

                Thread thread = new Thread(clientHandler);

                thread.start();
            }

        } catch (IOException e) {

            System.out.println(
                    "Server Error : " + e.getMessage()
            );

        } finally {

            stopServer();

        }
    }


    public void stopServer() {

        try {

            if (serverSocket != null && !serverSocket.isClosed()) {

                serverSocket.close();

                System.out.println(Constants.SERVER_STOPPED);
            }

        } catch (IOException e) {

            System.out.println(
                    "Unable to close server : "
                            + e.getMessage()
            );

        }

    }


    public static void main(String[] args) {

        ChatServer server = new ChatServer();

        server.startServer();

    }

}