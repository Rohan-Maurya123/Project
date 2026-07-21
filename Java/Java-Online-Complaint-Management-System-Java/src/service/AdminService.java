package service;

import model.Complaint;
import model.ComplaintCategory;
import model.ComplaintPriority;
import model.ComplaintStatus;

import java.util.List;

public class AdminService {

    private final ComplaintService complaintService;

    public AdminService() {

        complaintService = new ComplaintService();

    }


    public List<Complaint> getAllComplaints() {

        return complaintService.getAllComplaints();

    }


    public Complaint searchComplaint(String complaintId) {

        return complaintService.getComplaintById(complaintId);

    }


    public List<Complaint> filterByStatus(
            ComplaintStatus status) {

        return complaintService.getComplaintsByStatus(status);

    }


    public List<Complaint> filterByCategory(
            ComplaintCategory category) {

        return complaintService.getComplaintsByCategory(category);

    }


    public List<Complaint> filterByPriority(
            ComplaintPriority priority) {

        return complaintService.getComplaintsByPriority(priority);

    }


    public boolean assignComplaint(
            String complaintId,
            String assignedPerson) {

        return complaintService.assignComplaint(
                complaintId,
                assignedPerson
        );

    }


    public boolean updatePriority(
            String complaintId,
            ComplaintPriority priority) {

        return complaintService.updatePriority(
                complaintId,
                priority
        );

    }


    public boolean updateStatus(
            String complaintId,
            ComplaintStatus status) {

        return complaintService.updateStatus(
                complaintId,
                status
        );

    }


    public boolean resolveComplaint(
            String complaintId,
            String resolution) {

        return complaintService.addResolution(
                complaintId,
                resolution
        );

    }


    public boolean closeComplaint(
            String complaintId) {

        return complaintService.closeComplaint(
                complaintId
        );

    }

}