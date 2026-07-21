package repository;

import constants.AppConstants;
import model.Feedback;
import utility.FileManager;

import java.util.ArrayList;
import java.util.List;

public class FeedbackRepository {


    public List<Feedback> loadFeedback() {

        List<Feedback> feedbackList = new ArrayList<>();

        List<String> lines =
                FileManager.readLines(AppConstants.FEEDBACK_FILE);

        for (String line : lines) {

            if (line.trim().isEmpty()) {
                continue;
            }

            String[] data = line.split("\\|", -1);

            if (data.length < 3) {
                continue;
            }

            Feedback feedback = new Feedback();

            feedback.setComplaintId(data[0]);
            feedback.setRating(Integer.parseInt(data[1]));
            feedback.setComment(data[2]);

            feedbackList.add(feedback);
        }

        return feedbackList;
    }


    public void saveFeedback(List<Feedback> feedbackList) {

        List<String> lines = new ArrayList<>();

        for (Feedback feedback : feedbackList) {

            String record =
                    feedback.getComplaintId() + "|" +
                    feedback.getRating() + "|" +
                    feedback.getComment();

            lines.add(record);
        }

        FileManager.writeLines(
                AppConstants.FEEDBACK_FILE,
                lines
        );
    }

}