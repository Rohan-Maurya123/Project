package model;

import java.io.Serializable;
import java.time.LocalDateTime;

public class ComplaintHistory implements Serializable {

    private String complaintId;
    private ComplaintStatus status;
    private String remarks;
    private LocalDateTime updatedOn;

    public ComplaintHistory() {
    }

    public ComplaintHistory(String complaintId,
                            ComplaintStatus status,
                            String remarks,
                            LocalDateTime updatedOn) {

        this.complaintId = complaintId;
        this.status = status;
        this.remarks = remarks;
        this.updatedOn = updatedOn;
    }

    public String getComplaintId() {
        return complaintId;
    }

    public void setComplaintId(String complaintId) {
        this.complaintId = complaintId;
    }

    public ComplaintStatus getStatus() {
        return status;
    }

    public void setStatus(ComplaintStatus status) {
        this.status = status;
    }

    public String getRemarks() {
        return remarks;
    }

    public void setRemarks(String remarks) {
        this.remarks = remarks;
    }

    public LocalDateTime getUpdatedOn() {
        return updatedOn;
    }

    public void setUpdatedOn(LocalDateTime updatedOn) {
        this.updatedOn = updatedOn;
    }
}