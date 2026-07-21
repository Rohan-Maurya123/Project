package common;

import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;


public final class TimeUtil {

    private static final DateTimeFormatter FORMATTER =
            DateTimeFormatter.ofPattern("yyyy-MM-dd HH:mm:ss");

    private TimeUtil() {
    }

  
    public static String getCurrentTimestamp() {
        return LocalDateTime.now().format(FORMATTER);
    }


    public static String getCurrentTime() {
        return LocalDateTime.now().format(
                DateTimeFormatter.ofPattern("HH:mm:ss")
        );
    }

}