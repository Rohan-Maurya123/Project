package service;

import model.Complaint;
import model.ComplaintCategory;
import model.ComplaintPriority;
import model.ComplaintStatus;
import repository.ComplaintRepository;
import utility.DateUtil;
import utility.IdGenerator;

import java.util.ArrayList;
import java.util.List;

public class ComplaintService {

    private final ComplaintRepository complaintRepository;
    private final List<Complaint> complaints;

    public ComplaintService() {

        complaintRepository = new ComplaintRepository();
        complaints = complaintRepository.loadComplaints();

    }


    public Complaint submitComplaint(Complaint complaint) {

        complaint.setComplaintId(
                IdGenerator.generateComplaintId());

        complaint.setStatus(
                ComplaintStatus.OPEN);

        complaint.setCreatedDate(
                DateUtil.now());

        complaint.setUpdatedDate(
                DateUtil.now());

        complaints.add(complaint);

        complaintRepository.saveComplaints(complaints);

        return complaint;

    }


    public List<Complaint> getAllComplaints() {

        return complaints;

    }


    public Complaint getComplaintById(String complaintId) {

        for (Complaint complaint : complaints) {

            if (complaint.getComplaintId()
                    .equalsIgnoreCase(complaintId)) {

                return complaint;

            }

        }

        return null;

    }

    public List<Complaint> getComplaintsByUser(String userId) {

        List<Complaint> userComplaints =
                new ArrayList<>();

        for (Complaint complaint : complaints) {

            if (complaint.getUserId()
                    .equalsIgnoreCase(userId)) {

                userComplaints.add(complaint);

            }

        }

        return userComplaints;

    }


    public List<Complaint> getComplaintsByStatus(
            ComplaintStatus status) {

        List<Complaint> result = new ArrayList<>();

        for (Complaint complaint : complaints) {

            if (complaint.getStatus() == status) {
                result.add(complaint);
            }

        }

        return result;

    }


    public List<Complaint> getComplaintsByCategory(
            ComplaintCategory category) {

        List<Complaint> result = new ArrayList<>();

        for (Complaint complaint : complaints) {

            if (complaint.getCategory() == category) {
                result.add(complaint);
            }

        }

        return result;

    }

    public List<Complaint> getComplaintsByPriority(
            ComplaintPriority priority) {

        List<Complaint> result = new ArrayList<>();

        for (Complaint complaint : complaints) {

            if (complaint.getPriority() == priority) {
                result.add(complaint);
            }

        }

        return result;

    }


    public boolean updateStatus(
            String complaintId,
            ComplaintStatus status) {

        Complaint complaint =
                getComplaintById(complaintId);

        if (complaint == null) {
            return false;
        }

        complaint.setStatus(status);
        complaint.setUpdatedDate(DateUtil.now());

        complaintRepository.saveComplaints(complaints);

        return true;

    }


    public boolean updatePriority(
            String complaintId,
            ComplaintPriority priority) {

        Complaint complaint =
                getComplaintById(complaintId);

        if (complaint == null) {
            return false;
        }

        complaint.setPriority(priority);
        complaint.setUpdatedDate(DateUtil.now());

        complaintRepository.saveComplaints(complaints);

        return true;

    }


    public boolean assignComplaint(
            String complaintId,
            String assignedPerson) {

        Complaint complaint =
                getComplaintById(complaintId);

        if (complaint == null) {
            return false;
        }

        complaint.setAssignedPerson(assignedPerson);
        complaint.setStatus(ComplaintStatus.ASSIGNED);
        complaint.setUpdatedDate(DateUtil.now());

        complaintRepository.saveComplaints(complaints);

        return true;

    }

 
    public boolean addResolution(
            String complaintId,
            String resolution) {

        Complaint complaint =
                getComplaintById(complaintId);

        if (complaint == null) {
            return false;
        }

        complaint.setResolution(resolution);
        complaint.setStatus(ComplaintStatus.RESOLVED);
        complaint.setUpdatedDate(DateUtil.now());

        complaintRepository.saveComplaints(complaints);

        return true;

    }


    public boolean closeComplaint(
            String complaintId) {

        Complaint complaint =
                getComplaintById(complaintId);

        if (complaint == null) {
            return false;
        }

        complaint.setStatus(ComplaintStatus.CLOSED);
        complaint.setUpdatedDate(DateUtil.now());

        complaintRepository.saveComplaints(complaints);

        return true;

    }

}