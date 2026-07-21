package server;

import common.Constants;
import common.MessageFormatter;
import common.UsernameValidator;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.PrintWriter;
import java.net.Socket;

public class ClientHandler implements Runnable {

    private final Socket socket;
    private final ServerManager serverManager;

    private BufferedReader reader;
    private PrintWriter writer;

    private String username;

    public ClientHandler(Socket socket, ServerManager serverManager) {
        this.socket = socket;
        this.serverManager = serverManager;
    }

    @Override
    public void run() {

        try {

            reader = new BufferedReader(
                    new InputStreamReader(socket.getInputStream())
            );

            writer = new PrintWriter(
                    socket.getOutputStream(),
                    true
            );

            requestUsername();

            String message;

            while ((message = reader.readLine()) != null) {

                message = message.trim();

                if (message.isEmpty()) {
                    continue;
                }

                if (message.equalsIgnoreCase(Constants.EXIT_COMMAND)) {
                    break;
                }

                if (message.equalsIgnoreCase(Constants.USER_LIST_COMMAND)) {
                    serverManager.sendUserList(this);
                    continue;
                }

                if (message.startsWith(Constants.PRIVATE_MESSAGE_COMMAND + " ")) {
                    handlePrivateMessage(message);
                    continue;
                }

                serverManager.broadcast(
                        MessageFormatter.formatChatMessage(
                                username,
                                message
                        )
                );
            }

        } catch (IOException e) {

            System.out.println(
                    "Connection lost with "
                            + username
            );

        } finally {

            cleanup();

        }
    }


    private void requestUsername() throws IOException {

        while (true) {

            writer.println("Enter Username:");

            String input = reader.readLine();

            if (!UsernameValidator.isValid(input)) {

                writer.println(
                        "Invalid username. Use 3-20 letters, numbers or underscore."
                );

                continue;
            }

            if (!serverManager.addClient(input, this)) {

                writer.println(Constants.USER_ALREADY_EXISTS);

                continue;
            }

            username = input;

            writer.println("Welcome " + username + "!");

            break;
        }
    }

    private void handlePrivateMessage(String message) {

        String[] parts = message.split(" ", 3);

        if (parts.length < 3) {

            writer.println(
                    "Usage: /msg username message"
            );

            return;
        }

        String receiver = parts[1];
        String privateMessage = parts[2];

        serverManager.sendPrivateMessage(
                username,
                receiver,
                privateMessage
        );
    }

    public void sendMessage(String message) {

        writer.println(message);

    }


    public String getUsername() {

        return username;

    }


    private void cleanup() {

        if (username != null) {

            serverManager.removeClient(username);

        }

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

        } catch (IOException ignored) {

        }

        System.out.println(
                username + " disconnected."
        );
    }

}