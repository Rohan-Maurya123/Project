package model;

import java.io.Serializable;
import java.time.LocalDateTime;

public class Complaint implements Serializable {

    private String complaintId;
    private String userId;

    private String title;
    private String description;

    private ComplaintCategory category;
    private ComplaintPriority priority;
    private ComplaintStatus status;

    private LocalDateTime createdDate;
    private LocalDateTime updatedDate;

    private String assignedPerson;
    private String resolution;

    public Complaint() {
    }

    public Complaint(String complaintId,
                     String userId,
                     String title,
                     String description,
                     ComplaintCategory category,
                     ComplaintPriority priority,
                     ComplaintStatus status,
                     LocalDateTime createdDate,
                     LocalDateTime updatedDate,
                     String assignedPerson,
                     String resolution) {

        this.complaintId = complaintId;
        this.userId = userId;
        this.title = title;
        this.description = description;
        this.category = category;
        this.priority = priority;
        this.status = status;
        this.createdDate = createdDate;
        this.updatedDate = updatedDate;
        this.assignedPerson = assignedPerson;
        this.resolution = resolution;
    }

    public String getComplaintId() {
        return complaintId;
    }

    public void setComplaintId(String complaintId) {
        this.complaintId = complaintId;
    }

    public String getUserId() {
        return userId;
    }

    public void setUserId(String userId) {
        this.userId = userId;
    }

    public String getTitle() {
        return title;
    }

    public void setTitle(String title) {
        this.title = title;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public ComplaintCategory getCategory() {
        return category;
    }

    public void setCategory(ComplaintCategory category) {
        this.category = category;
    }

    public ComplaintPriority getPriority() {
        return priority;
    }

    public void setPriority(ComplaintPriority priority) {
        this.priority = priority;
    }

    public ComplaintStatus getStatus() {
        return status;
    }

    public void setStatus(ComplaintStatus status) {
        this.status = status;
    }

    public LocalDateTime getCreatedDate() {
        return createdDate;
    }

    public void setCreatedDate(LocalDateTime createdDate) {
        this.createdDate = createdDate;
    }

    public LocalDateTime getUpdatedDate() {
        return updatedDate;
    }

    public void setUpdatedDate(LocalDateTime updatedDate) {
        this.updatedDate = updatedDate;
    }

    public String getAssignedPerson() {
        return assignedPerson;
    }

    public void setAssignedPerson(String assignedPerson) {
        this.assignedPerson = assignedPerson;
    }

    public String getResolution() {
        return resolution;
    }

    public void setResolution(String resolution) {
        this.resolution = resolution;
    }

    @Override
    public String toString() {

        return "Complaint{" +
                "complaintId='" + complaintId + '\'' +
                ", title='" + title + '\'' +
                ", category=" + category +
                ", priority=" + priority +
                ", status=" + status +
                '}';
    }
}