package utility;

import java.util.Collection;
import model.Task;


public class TaskIdGenerator {

    private static final String PREFIX = "TSK-";
    private static int counter = 1001;

    private TaskIdGenerator() {
    }

    
    public static synchronized String generateId() {
        return PREFIX + counter++;
    }

    public static void initialize(Collection<Task> tasks) {

        int max = 1000;

        for (Task task : tasks) {

            try {

                String id = task.getTaskId();

                if (id != null && id.startsWith(PREFIX)) {

                    int value = Integer.parseInt(id.substring(PREFIX.length()));

                    if (value > max) {
                        max = value;
                    }

                }

            } catch (Exception ignored) {
            }

        }

        counter = max + 1;
    }

}