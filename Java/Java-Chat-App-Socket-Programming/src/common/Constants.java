package common;


public final class Constants {

    // Prevent object creation
    private Constants() {
    }

    // Server Configuration
    public static final String HOST = "localhost";
    public static final int PORT = 5000;

    // File Paths
    public static final String CHAT_LOG_FILE = "logs/chat_history.txt";

    // Commands
    public static final String EXIT_COMMAND = "/exit";
    public static final String PRIVATE_MESSAGE_COMMAND = "/msg";
    public static final String USER_LIST_COMMAND = "/users";

    // System Messages
    public static final String SERVER_STARTED =
            "Chat Server started successfully...";

    public static final String SERVER_STOPPED =
            "Server stopped.";

    public static final String CONNECTION_CLOSED =
            "Connection closed.";

    public static final String INVALID_COMMAND =
            "Invalid command.";

    public static final String USER_ALREADY_EXISTS =
            "Username already exists.";

    public static final String USER_NOT_FOUND =
            "User not found.";

}