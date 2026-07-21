package common;


public final class MessageFormatter {

    private MessageFormatter() {
    }

   
    public static String formatChatMessage(String username, String message) {
        return "[" + TimeUtil.getCurrentTime() + "] "
                + username + " : " + message;
    }


    public static String formatSystemMessage(String message) {
        return "[" + TimeUtil.getCurrentTime() + "] "
                + "[SYSTEM] " + message;
    }


    public static String formatPrivateMessage(String sender,
                                              String receiver,
                                              String message) {

        return "[" + TimeUtil.getCurrentTime() + "] "
                + "[PRIVATE] "
                + sender
                + " -> "
                + receiver
                + " : "
                + message;
    }

}