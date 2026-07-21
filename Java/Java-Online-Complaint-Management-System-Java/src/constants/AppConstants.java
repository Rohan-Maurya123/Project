package constants;

public final class AppConstants {

    private AppConstants() {
        // Prevent object creation
    }

   

    public static final String USERS_FILE =
            "data/users.txt";

    public static final String COMPLAINTS_FILE =
            "data/complaints.txt";

    public static final String HISTORY_FILE =
            "data/history.txt";

    public static final String FEEDBACK_FILE =
            "data/feedback.txt";




    public static final String DEFAULT_ADMIN_EMAIL =
            "admin@ocms.com";

    public static final String DEFAULT_ADMIN_PASSWORD =
            "admin123";

    public static final String DEFAULT_ADMIN_NAME =
            "System Administrator";



    public static final String WELCOME_MESSAGE =
            "===== Online Complaint Management System =====";

    public static final String EXIT_MESSAGE =
            "Thank you for using the Online Complaint Management System.";

    public static final String INVALID_CHOICE =
            "Invalid choice. Please try again.";

    public static final String LOGIN_SUCCESS =
            "Login successful.";

    public static final String LOGIN_FAILED =
            "Invalid email or password.";

    public static final String REGISTRATION_SUCCESS =
            "Registration completed successfully.";

    public static final String COMPLAINT_SUBMITTED =
            "Complaint submitted successfully.";

    public static final String COMPLAINT_NOT_FOUND =
            "Complaint not found.";

    public static final String ACCESS_DENIED =
            "Access denied.";

}