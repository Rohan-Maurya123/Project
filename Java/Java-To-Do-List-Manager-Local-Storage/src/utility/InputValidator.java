package utility;

import java.time.LocalDate;
import model.TaskCategory;
import model.TaskPriority;


public class InputValidator {

    private InputValidator() {
    }


    public static boolean isValidTitle(String title) {

        return title != null
                && !title.trim().isEmpty()
                && title.trim().length() >= 3
                && title.trim().length() <= 100;

    }

 
    public static boolean isValidDescription(String description) {

        return description != null
                && description.trim().length() <= 500;

    }


    public static boolean isValidDueDate(LocalDate dueDate) {

        if (dueDate == null)
            return false;

        return !dueDate.isBefore(LocalDate.now());

    }


    public static boolean isValidPriority(TaskPriority priority) {

        return priority != null;

    }


    public static boolean isValidCategory(TaskCategory category) {

        return category != null;

    }

}