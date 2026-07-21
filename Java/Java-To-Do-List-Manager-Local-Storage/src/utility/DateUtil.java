package utility;

import java.time.LocalDate;
import java.time.format.DateTimeFormatter;
import java.time.format.DateTimeParseException;


public class DateUtil {

    public static final DateTimeFormatter FORMATTER =
            DateTimeFormatter.ofPattern("dd-MM-yyyy");

    private DateUtil() {
    }


    public static LocalDate parse(String date) {

        try {
            return LocalDate.parse(date, FORMATTER);
        } catch (DateTimeParseException ex) {
            return null;
        }

    }

 
    public static String format(LocalDate date) {

        if (date == null)
            return "";

        return date.format(FORMATTER);
    }


    public static boolean isValidDueDate(LocalDate date) {

        if (date == null)
            return false;

        return !date.isBefore(LocalDate.now());

    }

}