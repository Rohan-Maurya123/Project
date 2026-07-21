package server;

import common.ChatLogger;
import common.Constants;
import common.MessageFormatter;

import java.util.Map;
import java.util.Set;
import java.util.concurrent.ConcurrentHashMap;


public class ServerManager {

    // username -> ClientHandler
    private final Map<String, ClientHandler> clients;

    public ServerManager() {
        clients = new ConcurrentHashMap<>();
    }


    public synchronized boolean addClient(String username,
                                          ClientHandler clientHandler) {

        if (clients.containsKey(username)) {
            return false;
        }

        clients.put(username, clientHandler);

        String joinMessage =
                MessageFormatter.formatSystemMessage(
                        username + " joined the chat."
                );

        broadcast(joinMessage);

        ChatLogger.log(username + " joined.");

        return true;
    }


    public synchronized void removeClient(String username) {

        if (clients.remove(username) != null) {

            String leaveMessage =
                    MessageFormatter.formatSystemMessage(
                            username + " left the chat."
                    );

            broadcast(leaveMessage);

            ChatLogger.log(username + " left.");
        }
    }


    public void broadcast(String message) {

        for (ClientHandler client : clients.values()) {
            client.sendMessage(message);
        }

        ChatLogger.log(message);
    }


    public void sendPrivateMessage(String sender,
                                   String receiver,
                                   String message) {

        ClientHandler target = clients.get(receiver);

        if (target == null) {

            ClientHandler senderClient = clients.get(sender);

            if (senderClient != null) {
                senderClient.sendMessage(Constants.USER_NOT_FOUND);
            }

            return;
        }

        String formattedMessage =
                MessageFormatter.formatPrivateMessage(
                        sender,
                        receiver,
                        message
                );

        target.sendMessage(formattedMessage);

        ClientHandler senderClient = clients.get(sender);

        if (senderClient != null) {
            senderClient.sendMessage(formattedMessage);
        }

        ChatLogger.log(formattedMessage);
    }


    public void sendUserList(ClientHandler client) {

        Set<String> usernames = clients.keySet();

        client.sendMessage(
                MessageFormatter.formatSystemMessage(
                        "Active Users : " + usernames
                )
        );
    }

    public boolean usernameExists(String username) {
        return clients.containsKey(username);
    }


    public int getClientCount() {
        return clients.size();
    }

}