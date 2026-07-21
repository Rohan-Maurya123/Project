package service;

import model.Feedback;
import repository.FeedbackRepository;

// import java.util.ArrayList;
import java.util.List;

public class FeedbackService {

    private final FeedbackRepository feedbackRepository;
    private final List<Feedback> feedbackList;

    public FeedbackService() {

        feedbackRepository = new FeedbackRepository();
        feedbackList = feedbackRepository.loadFeedback();

    }


    public void submitFeedback(Feedback feedback) {

        feedbackList.add(feedback);

        feedbackRepository.saveFeedback(feedbackList);

    }


    public List<Feedback> getAllFeedback() {

        return feedbackList;

    }


    public Feedback getFeedbackByComplaintId(
            String complaintId) {

        for (Feedback feedback : feedbackList) {

            if (feedback.getComplaintId()
                    .equalsIgnoreCase(complaintId)) {

                return feedback;

            }

        }

        return null;

    }


    public boolean hasFeedback(
            String complaintId) {

        return getFeedbackByComplaintId(
                complaintId) != null;

    }

}