package model;

public class Feedback {

    private String complaintId;
    private String userId;
    private int rating;
    private String comment;


    public Feedback() {

    }


    public Feedback(String complaintId,
                    String userId,
                    int rating,
                    String comment) {

        this.complaintId = complaintId;
        this.userId = userId;
        this.rating = rating;
        this.comment = comment;

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


    public int getRating() {

        return rating;

    }


    public void setRating(int rating) {

        this.rating = rating;

    }


    public String getComment() {

        return comment;

    }


    public void setComment(String comment) {

        this.comment = comment;

    }

}