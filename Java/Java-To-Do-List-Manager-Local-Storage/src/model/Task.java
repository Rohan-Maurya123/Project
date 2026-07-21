package model;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.Objects;

import utility.DateUtil;


public class Task implements Serializable {

    private static final long serialVersionUID = 1L;

    private String taskId;
    private String title;
    private String description;

    private TaskPriority priority;
    private TaskCategory category;
    private TaskStatus status;

    private LocalDate dueDate;
    private LocalDate createdDate;
    private LocalDate completedDate;

 
    public Task() {
        this.createdDate = LocalDate.now();
        this.status = TaskStatus.PENDING;
    }


    public Task(String taskId,
                String title,
                String description,
                TaskPriority priority,
                TaskCategory category,
                LocalDate dueDate) {

        this.taskId = taskId;
        this.title = title;
        this.description = description;
        this.priority = priority;
        this.category = category;
        this.dueDate = dueDate;

        this.status = TaskStatus.PENDING;
        this.createdDate = LocalDate.now();
        this.completedDate = null;
    }

    // ===========================
    // Getters
    // ===========================

    public String getTaskId() {
        return taskId;
    }

    public String getTitle() {
        return title;
    }

    public String getDescription() {
        return description;
    }

    public TaskPriority getPriority() {
        return priority;
    }

    public TaskCategory getCategory() {
        return category;
    }

    public TaskStatus getStatus() {
        return status;
    }

    public LocalDate getDueDate() {
        return dueDate;
    }

    public LocalDate getCreatedDate() {
        return createdDate;
    }

    public LocalDate getCompletedDate() {
        return completedDate;
    }

    // ===========================
    // Setters
    // ===========================

    public void setTaskId(String taskId) {
        this.taskId = taskId;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public void setPriority(TaskPriority priority) {
        this.priority = priority;
    }

    public void setCategory(TaskCategory category) {
        this.category = category;
    }

    public void setStatus(TaskStatus status) {

        this.status = status;

        if (status == TaskStatus.COMPLETED) {
            completedDate = LocalDate.now();
        } else {
            completedDate = null;
        }
    }

    public void setDueDate(LocalDate dueDate) {
        this.dueDate = dueDate;
    }

    public void setCreatedDate(LocalDate createdDate) {
        this.createdDate = createdDate;
    }

    public void setCompletedDate(LocalDate completedDate) {
        this.completedDate = completedDate;
    }

    // ===========================
    // Business Methods
    // ===========================

  
    public void markCompleted() {

        status = TaskStatus.COMPLETED;
        completedDate = LocalDate.now();

    }


    public void markPending() {

        status = TaskStatus.PENDING;
        completedDate = null;

    }

    public void markInProgress() {

        status = TaskStatus.IN_PROGRESS;
        completedDate = null;

    }


    public boolean isOverdue() {

        return status != TaskStatus.COMPLETED
                && dueDate != null
                && dueDate.isBefore(LocalDate.now());

    }


    public String getFormattedDueDate() {

        if (dueDate == null)
            return "";

        return DateUtil.format(dueDate);

    }


    public String getFormattedCreatedDate() {

        if (createdDate == null)
            return "";

        return DateUtil.format(createdDate);

    }


    public String getFormattedCompletedDate() {

        if (completedDate == null)
            return "-";

        return DateUtil.format(completedDate);

    }


    public boolean isCompleted() {
        return status == TaskStatus.COMPLETED;
    }


    public boolean isPending() {
        return status == TaskStatus.PENDING;
    }


    public boolean isInProgress() {
        return status == TaskStatus.IN_PROGRESS;
    }

    @Override
    public String toString() {

        return "Task{" +
                "taskId='" + taskId + '\'' +
                ", title='" + title + '\'' +
                ", description='" + description + '\'' +
                ", priority=" + priority +
                ", category=" + category +
                ", status=" + status +
                ", dueDate=" + dueDate +
                ", createdDate=" + createdDate +
                ", completedDate=" + completedDate +
                '}';
    }

    @Override
    public boolean equals(Object obj) {

        if (this == obj)
            return true;

        if (!(obj instanceof Task))
            return false;

        Task other = (Task) obj;

        return Objects.equals(taskId, other.taskId);

    }

    @Override
    public int hashCode() {
        return Objects.hash(taskId);
    }
}