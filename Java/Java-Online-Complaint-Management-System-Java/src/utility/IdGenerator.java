package utility;

import java.util.UUID;

public class IdGenerator {

    private IdGenerator() {
        // Prevent object creation
    }

    public static String generateUserId() {
        return "USR-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
    }

    public static String generateComplaintId() {
        return "CMP-" + UUID.randomUUID().toString().substring(0, 8).toUpperCase();
    }

}