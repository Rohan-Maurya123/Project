package repository;

import constants.AppConstants;
import model.Complaint;
import model.ComplaintCategory;
import model.ComplaintPriority;
import model.ComplaintStatus;
import utility.FileManager;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.List;

public class ComplaintRepository {


    public List<Complaint> loadComplaints() {

        List<Complaint> complaints = new ArrayList<>();

        List<String> lines =
                FileManager.readLines(AppConstants.COMPLAINTS_FILE);

        for (String line : lines) {

            if (line.trim().isEmpty()) {
                continue;
            }

            String[] data = line.split("\\|", -1);

            if (data.length < 11) {
                continue;
            }

            Complaint complaint = new Complaint();

            complaint.setComplaintId(data[0]);
            complaint.setUserId(data[1]);
            complaint.setTitle(data[2]);
            complaint.setDescription(data[3]);

            complaint.setCategory(
                    ComplaintCategory.valueOf(data[4])
            );

            complaint.setPriority(
                    ComplaintPriority.valueOf(data[5])
            );

            complaint.setStatus(
                    ComplaintStatus.valueOf(data[6])
            );

            complaint.setCreatedDate(
                    LocalDateTime.parse(data[7])
            );

            complaint.setUpdatedDate(
                    LocalDateTime.parse(data[8])
            );

            complaint.setAssignedPerson(data[9]);
            complaint.setResolution(data[10]);

            complaints.add(complaint);
        }

        return complaints;
    }

    public void saveComplaints(List<Complaint> complaints) {

        List<String> lines = new ArrayList<>();

        for (Complaint complaint : complaints) {

            String record =
                    complaint.getComplaintId() + "|" +
                    complaint.getUserId() + "|" +
                    complaint.getTitle() + "|" +
                    complaint.getDescription() + "|" +
                    complaint.getCategory() + "|" +
                    complaint.getPriority() + "|" +
                    complaint.getStatus() + "|" +
                    complaint.getCreatedDate() + "|" +
                    complaint.getUpdatedDate() + "|" +
                    (complaint.getAssignedPerson() == null ? "" : complaint.getAssignedPerson()) + "|" +
                    (complaint.getResolution() == null ? "" : complaint.getResolution());

            lines.add(record);
        }

        FileManager.writeLines(
                AppConstants.COMPLAINTS_FILE,
                lines
        );
    }

}