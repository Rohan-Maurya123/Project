package service;

import exception.InvalidTaskException;
import model.Task;
import model.TaskCategory;
import model.TaskPriority;
import model.TaskStatus;
import repository.FileTaskRepository;
import utility.InputValidator;
import utility.TaskIdGenerator;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;


public class TaskService {


    private final FileTaskRepository repository;

    private List<Task> tasks;


    /**
     * Constructor
     */
    public TaskService() {

        repository = new FileTaskRepository();

        tasks = repository.loadTasks();

        TaskIdGenerator.initialize(tasks);

    }



    // =====================================================
    // CREATE OPERATIONS
    // =====================================================


    /**
     * Add a new task.
     */
    public Task addTask(
            String title,
            String description,
            TaskPriority priority,
            TaskCategory category,
            LocalDate dueDate
    ) throws InvalidTaskException {


        validateTaskData(
                title,
                description,
                priority,
                category,
                dueDate
        );


        String id =
                TaskIdGenerator.generateId();


        Task task =
                new Task(
                        id,
                        title,
                        description,
                        priority,
                        category,
                        dueDate
                );


        tasks.add(task);


        save();


        return task;

    }


    /**
     * Add existing task object.
     *
     * Useful for loading/importing tasks.
     */
    public void addExistingTask(Task task)
            throws InvalidTaskException {


        if(task == null){

            throw new InvalidTaskException(
                    "Task cannot be null"
            );

        }


        if(tasks.contains(task)){

            throw new InvalidTaskException(
                    "Task with same ID already exists"
            );

        }


        tasks.add(task);

        save();

    }



    // =====================================================
    // READ OPERATIONS
    // =====================================================



    /**
     * Returns all tasks.
     */
    public List<Task> getAllTasks(){

        return new ArrayList<>(tasks);

    }



    /**
     * Find task by ID.
     */
    public Task getTaskById(String taskId)
            throws InvalidTaskException{


        if(taskId == null ||
                taskId.trim().isEmpty()){


            throw new InvalidTaskException(
                    "Task ID cannot be empty"
            );

        }


        for(Task task : tasks){

            if(task.getTaskId()
                    .equalsIgnoreCase(taskId)){


                return task;

            }

        }


        throw new InvalidTaskException(
                "Task not found with ID : "
                        + taskId
        );

    }



    /**
     * Get total number of tasks.
     */
    public int getTotalTasks(){

        return tasks.size();

    }



    /**
     * Save current task list.
     */
    private void save(){

        repository.saveTasks(tasks);

    }



    /**
     * Validate task input.
     */
    private void validateTaskData(
            String title,
            String description,
            TaskPriority priority,
            TaskCategory category,
            LocalDate dueDate
    ) throws InvalidTaskException {



        if(!InputValidator.isValidTitle(title)){

            throw new InvalidTaskException(
                    "Title must contain 3-100 characters"
            );

        }


        if(!InputValidator
                .isValidDescription(description)){


            throw new InvalidTaskException(
                    "Description is too long"
            );

        }


        if(!InputValidator
                .isValidPriority(priority)){


            throw new InvalidTaskException(
                    "Priority is required"
            );

        }


        if(!InputValidator
                .isValidCategory(category)){


            throw new InvalidTaskException(
                    "Category is required"
            );

        }


        if(!InputValidator
                .isValidDueDate(dueDate)){


            throw new InvalidTaskException(
                    "Invalid due date"
            );

        }

    }

    // =====================================================
    // UPDATE OPERATIONS
    // =====================================================


    /**
     * Update complete task information.
     */
    public void updateTask(
            String taskId,
            String title,
            String description,
            TaskPriority priority,
            TaskCategory category,
            LocalDate dueDate
    ) throws InvalidTaskException {


        Task task = getTaskById(taskId);


        validateTaskData(
                title,
                description,
                priority,
                category,
                dueDate
        );


        task.setTitle(title);

        task.setDescription(description);

        task.setPriority(priority);

        task.setCategory(category);

        task.setDueDate(dueDate);


        save();

    }



    /**
     * Update only task title.
     */
    public void updateTitle(
            String taskId,
            String title
    ) throws InvalidTaskException {


        if(!InputValidator.isValidTitle(title)){

            throw new InvalidTaskException(
                    "Invalid task title"
            );

        }


        Task task =
                getTaskById(taskId);


        task.setTitle(title);


        save();

    }



    /**
     * Change task priority.
     */
    public void updatePriority(
            String taskId,
            TaskPriority priority
    ) throws InvalidTaskException {


        Task task =
                getTaskById(taskId);


        if(priority == null){

            throw new InvalidTaskException(
                    "Priority cannot be empty"
            );

        }


        task.setPriority(priority);


        save();

    }



    /**
     * Change task category.
     */
    public void updateCategory(
            String taskId,
            TaskCategory category
    ) throws InvalidTaskException {


        Task task =
                getTaskById(taskId);


        if(category == null){

            throw new InvalidTaskException(
                    "Category cannot be empty"
            );

        }


        task.setCategory(category);


        save();

    }



    /**
     * Change due date.
     */
    public void updateDueDate(
            String taskId,
            LocalDate dueDate
    ) throws InvalidTaskException {


        Task task =
                getTaskById(taskId);


        if(!InputValidator
                .isValidDueDate(dueDate)){


            throw new InvalidTaskException(
                    "Invalid due date"
            );

        }


        task.setDueDate(dueDate);


        save();

    }



    // =====================================================
    // DELETE OPERATIONS
    // =====================================================


    /**
     * Delete task by ID.
     */
    public void deleteTask(String taskId)
            throws InvalidTaskException {


        Task task =
                getTaskById(taskId);


        tasks.remove(task);


        save();

    }



    /**
     * Delete all completed tasks.
     */
    public void deleteCompletedTasks(){


        tasks.removeIf(
                task ->
                        task.getStatus()
                                == TaskStatus.COMPLETED
        );


        save();

    }



    // =====================================================
    // STATUS OPERATIONS
    // =====================================================


    /**
     * Mark task completed.
     */
    public void markCompleted(
            String taskId
    ) throws InvalidTaskException {


        Task task =
                getTaskById(taskId);


        task.markCompleted();


        save();

    }



    /**
     * Mark task pending.
     */
    public void markPending(
            String taskId
    ) throws InvalidTaskException {


        Task task =
                getTaskById(taskId);


        task.markPending();


        save();

    }



    /**
     * Mark task as in progress.
     */
    public void markInProgress(
            String taskId
    ) throws InvalidTaskException {


        Task task =
                getTaskById(taskId);


        task.markInProgress();


        save();

    }



    /**
     * Change status manually.
     */
    public void changeStatus(
            String taskId,
            TaskStatus status
    ) throws InvalidTaskException {


        Task task =
                getTaskById(taskId);


        if(status == null){

            throw new InvalidTaskException(
                    "Status cannot be empty"
            );

        }


        task.setStatus(status);


        save();

    }

    // =====================================================
    // SEARCH OPERATIONS
    // =====================================================


    /**
     * Search tasks by title.
     */
    public List<Task> searchByTitle(String keyword) {


        List<Task> result =
                new ArrayList<>();


        if(keyword == null ||
                keyword.trim().isEmpty()){

            return result;

        }


        String search =
                keyword.toLowerCase();


        for(Task task : tasks){


            if(task.getTitle()
                    .toLowerCase()
                    .contains(search)){


                result.add(task);

            }

        }


        return result;

    }



    /**
     * Search tasks by description.
     */
    public List<Task> searchByDescription(
            String keyword
    ){

        List<Task> result =
                new ArrayList<>();


        if(keyword == null ||
                keyword.trim().isEmpty()){

            return result;

        }



        String search =
                keyword.toLowerCase();



        for(Task task : tasks){


            if(task.getDescription()
                    .toLowerCase()
                    .contains(search)){


                result.add(task);

            }

        }


        return result;

    }




    /**
     * Search title and description together.
     */
    public List<Task> search(String keyword){


        List<Task> result =
                new ArrayList<>();


        if(keyword == null ||
                keyword.trim().isEmpty()){


            return getAllTasks();

        }


        String search =
                keyword.toLowerCase();



        for(Task task : tasks){


            boolean titleMatch =
                    task.getTitle()
                            .toLowerCase()
                            .contains(search);


            boolean descriptionMatch =
                    task.getDescription()
                            .toLowerCase()
                            .contains(search);



            if(titleMatch ||
                    descriptionMatch){


                result.add(task);

            }

        }


        return result;

    }




    // =====================================================
    // FILTER OPERATIONS
    // =====================================================



    /**
     * Filter tasks by status.
     */
    public List<Task> filterByStatus(
            TaskStatus status
    ){


        List<Task> result =
                new ArrayList<>();



        for(Task task : tasks){


            if(task.getStatus()
                    == status){


                result.add(task);

            }

        }


        return result;

    }



    /**
     * Filter tasks by priority.
     */
    public List<Task> filterByPriority(
            TaskPriority priority
    ){


        List<Task> result =
                new ArrayList<>();



        for(Task task : tasks){


            if(task.getPriority()
                    == priority){


                result.add(task);

            }

        }


        return result;

    }



    /**
     * Filter tasks by category.
     */
    public List<Task> filterByCategory(
            TaskCategory category
    ){


        List<Task> result =
                new ArrayList<>();



        for(Task task : tasks){


            if(task.getCategory()
                    == category){


                result.add(task);

            }

        }


        return result;

    }



    /**
     * Get all pending tasks.
     */
    public List<Task> getPendingTasks(){


        return filterByStatus(
                TaskStatus.PENDING
        );

    }



    /**
     * Get all completed tasks.
     */
    public List<Task> getCompletedTasks(){


        return filterByStatus(
                TaskStatus.COMPLETED
        );

    }



    /**
     * Get all in progress tasks.
     */
    public List<Task> getInProgressTasks(){


        return filterByStatus(
                TaskStatus.IN_PROGRESS
        );

    }



    /**
     * Get overdue tasks.
     */
    public List<Task> getOverdueTasks(){


        List<Task> result =
                new ArrayList<>();



        for(Task task : tasks){


            if(task.isOverdue()){


                result.add(task);

            }

        }


        return result;

    }

    // =====================================================
    // SORTING OPERATIONS
    // =====================================================


    /**
     * Sort tasks by due date.
     * Earliest date comes first.
     */
    public List<Task> sortByDueDate(){


        List<Task> sorted =
                new ArrayList<>(tasks);


        sorted.sort(
                (task1, task2) -> {


                    if(task1.getDueDate() == null)
                        return 1;


                    if(task2.getDueDate() == null)
                        return -1;


                    return task1.getDueDate()
                            .compareTo(
                                    task2.getDueDate()
                            );

                }
        );


        return sorted;

    }



    /**
     * Sort tasks by priority.
     * Critical tasks appear first.
     */
    public List<Task> sortByPriority(){


        List<Task> sorted =
                new ArrayList<>(tasks);



        sorted.sort(
                (task1, task2) -> {


                    return Integer.compare(

                            task2.getPriority()
                                    .getLevel(),

                            task1.getPriority()
                                    .getLevel()

                    );

                }
        );


        return sorted;

    }



    /**
     * Sort tasks alphabetically by title.
     */
    public List<Task> sortByTitle(){


        List<Task> sorted =
                new ArrayList<>(tasks);



        sorted.sort(
                (task1, task2) ->


                        task1.getTitle()
                                .compareToIgnoreCase(
                                        task2.getTitle()
                                )

        );


        return sorted;

    }




    // =====================================================
    // STATISTICS
    // =====================================================




    /**
     * Count completed tasks.
     */
    public int getCompletedCount(){


        int count = 0;


        for(Task task : tasks){


            if(task.isCompleted()){

                count++;

            }

        }


        return count;

    }



    /**
     * Count pending tasks.
     */
    public int getPendingCount(){


        int count = 0;


        for(Task task : tasks){


            if(task.isPending()){

                count++;

            }

        }


        return count;

    }



    /**
     * Count in progress tasks.
     */
    public int getInProgressCount(){


        int count = 0;


        for(Task task : tasks){


            if(task.isInProgress()){

                count++;

            }

        }


        return count;

    }



    /**
     * Count overdue tasks.
     */
    public int getOverdueCount(){


        return getOverdueTasks()
                .size();

    }




    /**
     * Returns task completion percentage.
     */
    public double getCompletionPercentage(){


        if(tasks.isEmpty()){

            return 0;

        }



        return
                ((double)getCompletedCount()
                        /
                        tasks.size())
                        * 100;

    }




    /**
     * Returns summary text for dashboard.
     */
    public String getTaskSummary(){


        return
                "Total Tasks : "
                        + getTotalTasks()

                        + "\nCompleted : "
                        + getCompletedCount()

                        + "\nPending : "
                        + getPendingCount()

                        + "\nIn Progress : "
                        + getInProgressCount()

                        + "\nOverdue : "
                        + getOverdueCount();

    }




    /**
     * Reload tasks from storage.
     */
    public void reload(){


        tasks =
                repository.loadTasks();


        TaskIdGenerator.initialize(tasks);

    }



    /**
     * Manually save tasks.
     */
    public void saveChanges(){

        save();

    }

    // =====================================================
    // ADDITIONAL UTILITY OPERATIONS
    // =====================================================



    /**
     * Check whether task list is empty.
     */
    public boolean isEmpty(){

        return tasks.isEmpty();

    }




    /**
     * Remove all tasks.
     */
    public void removeAllTasks(){


        tasks.clear();


        save();

    }




    /**
     * Get number of tasks by category.
     */
    public int countByCategory(
            TaskCategory category
    ){


        int count = 0;


        for(Task task : tasks){


            if(task.getCategory()
                    == category){


                count++;

            }

        }


        return count;

    }



    /**
     * Get number of tasks by priority.
     */
    public int countByPriority(
            TaskPriority priority
    ){


        int count = 0;


        for(Task task : tasks){


            if(task.getPriority()
                    == priority){


                count++;

            }

        }


        return count;

    }




    /**
     * Get number of tasks by status.
     */
    public int countByStatus(
            TaskStatus status
    ){


        int count = 0;


        for(Task task : tasks){


            if(task.getStatus()
                    == status){


                count++;

            }

        }


        return count;

    }



    /**
     * Returns a copy of current task list.
     */
    public List<Task> getTasksCopy(){


        return new ArrayList<>(tasks);

    }




    /**
     * Refresh data after external changes.
     */
    public void refresh(){


        reload();

    }




    /**
     * Returns repository storage location.
     */
    public String getStorageLocation(){


        return repository.getStoragePath();

    }




    /**
     * Check if storage file exists.
     */
    public boolean storageAvailable(){


        return repository.storageExists();

    }


}
