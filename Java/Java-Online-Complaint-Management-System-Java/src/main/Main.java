package main;

import utility.InputUtil;

import constants.AppConstants;
import service.AdminService;
import service.AuthenticationService;
import service.ComplaintService;
import service.FeedbackService;
import service.UserService;

import exception.DuplicateUserException;
import exception.InvalidInputException;
import model.User;
import model.UserRole;
import utility.IdGenerator;
import utility.InputValidator;

// import model.User;
import exception.AuthenticationException;

import java.util.Scanner;

import model.Complaint;
import model.ComplaintCategory;
import model.ComplaintPriority;
import model.ComplaintStatus;
import model.Feedback;

import java.util.List;

public class Main {

    private static final Scanner scanner =
            new Scanner(System.in);


    private static UserService userService;
    private static AuthenticationService authenticationService;
    private static ComplaintService complaintService;
    private static AdminService adminService;
    private static FeedbackService feedbackService;
    private static User currentUser;


    public static void main(String[] args) {

        initializeServices();

        showWelcomeMessage();

        mainMenu();

        scanner.close();

    }


    /**
     * Initialize all services.
     */
    private static void initializeServices() {

        userService = new UserService();

        authenticationService =
                new AuthenticationService();

        complaintService =
                new ComplaintService();

        adminService =
                new AdminService();

        feedbackService =
                new FeedbackService();

    }


    /**
     * Display welcome message.
     */
    private static void showWelcomeMessage() {

        System.out.println();

        System.out.println(
                AppConstants.WELCOME_MESSAGE
        );

        System.out.println();

    }

    /**
 * User registration.
 */
private static void registerUser() {

    try {

        System.out.println();
        System.out.println("===== USER REGISTRATION =====");


        System.out.print("Enter name: ");
        String name = scanner.nextLine();


        System.out.print("Enter email: ");
        String email = scanner.nextLine();


        System.out.print("Enter password: ");
        String password = scanner.nextLine();


        if (!InputValidator.isNotBlank(name)) {

            throw new InvalidInputException(
                    "Name cannot be empty."
            );

        }


        if (!InputValidator.isValidEmail(email)) {

            throw new InvalidInputException(
                    "Invalid email format."
            );

        }


        if (!InputValidator.isValidPassword(password)) {

            throw new InvalidInputException(
                    "Password must contain minimum 6 characters."
            );

        }


        User user = new User(
                IdGenerator.generateUserId(),
                name,
                email,
                password,
                UserRole.USER
        );


        userService.registerUser(user);


        System.out.println();

        System.out.println(
                "Registration successful."
        );

        System.out.println(
                "Your User ID: "
                + user.getUserId()
        );


    }
    catch (DuplicateUserException e) {

        System.out.println(
                e.getMessage()
        );

    }
    catch (InvalidInputException e) {

        System.out.println(
                e.getMessage()
        );

    }

}


/**
 * User login.
 */
private static void userLogin() {

    try {

        System.out.println();
        System.out.println("===== USER LOGIN =====");


        System.out.print("Enter email: ");
        String email = scanner.nextLine();


        System.out.print("Enter password: ");
        String password = scanner.nextLine();


        User user =
                authenticationService.login(
                        email,
                        password
                );


        if (user.getRole().name().equals("USER")) {

            currentUser = user;

            System.out.println();

            System.out.println(
                    "Login successful."
            );

            System.out.println(
                    "Welcome "
                    + user.getName()
            );


            userDashboard();

        }
        else {

            System.out.println(
                    "Please use Admin Login."
            );

        }


    }
    catch(AuthenticationException e) {

        System.out.println(
                e.getMessage()
        );

    }

}

/**
 * User dashboard.
 */
private static void userDashboard() {


    int choice;


    do {

        System.out.println();

        System.out.println(
                "===== USER DASHBOARD ====="
        );

        System.out.println(
        "1. View Profile"
);

System.out.println(
        "2. Register Complaint"
);

System.out.println(
        "3. View My Complaints"
);

System.out.println(
        "4. Give Feedback"
);

System.out.println(
        "5. Logout"
);


        System.out.print(
                "Enter choice: "
        );


        choice =
        InputUtil.getInt(
                "Enter choice: "
        );

        switch(choice) {


case 1:

    System.out.println();

    System.out.println(
            "User ID: "
            + currentUser.getUserId()
    );

    System.out.println(
            "Name: "
            + currentUser.getName()
    );

    System.out.println(
            "Email: "
            + currentUser.getEmail()
    );

    break;



case 2:

    submitComplaint();

    break;



case 3:

    viewMyComplaints();

    break;



case 4:

    submitFeedback();

    break;



case 5:

    currentUser = null;

    System.out.println(
            "Logged out successfully."
    );

    break;



default:

    System.out.println(
            "Invalid choice."
    );

}


    }
    while(currentUser != null);


}


/**
 * Submit new complaint.
 */
private static void submitComplaint() {


    System.out.println();

    System.out.println(
            "===== REGISTER COMPLAINT ====="
    );


    System.out.print(
            "Enter complaint title: "
    );

    String title =
            scanner.nextLine();



    System.out.print(
            "Enter complaint description: "
    );

    String description =
            scanner.nextLine();



    System.out.println();

    System.out.println(
            "Select Category:"
    );

    System.out.println(
            "1. Technical"
    );

    System.out.println(
            "2. Billing"
    );

    System.out.println(
            "3. Service"
    );

    System.out.println(
            "4. Product"
    );

    System.out.println(
            "5. Infrastructure"
    );

    System.out.println(
            "6. Other"
    );


    System.out.print(
            "Choice: "
    );


    int categoryChoice =
        InputUtil.getInt(
                "Choice: "
        );


    ComplaintCategory category =
            selectCategory(categoryChoice);



    System.out.println();

    System.out.println(
            "Select Priority:"
    );

    System.out.println(
            "1. Low"
    );

    System.out.println(
            "2. Medium"
    );

    System.out.println(
            "3. High"
    );

    System.out.println(
            "4. Critical"
    );


    System.out.print(
            "Choice: "
    );


    int priorityChoice =
        InputUtil.getInt(
                "Choice: "
        );


    ComplaintPriority priority =
            selectPriority(priorityChoice);



    Complaint complaint =
            new Complaint();


    complaint.setUserId(
            currentUser.getUserId()
    );

    complaint.setTitle(title);

    complaint.setDescription(description);

    complaint.setCategory(category);

    complaint.setPriority(priority);



    Complaint savedComplaint =
            complaintService.submitComplaint(
                    complaint
            );


    System.out.println();

    System.out.println(
            "Complaint submitted successfully."
    );


    System.out.println(
            "Your Complaint ID: "
            + savedComplaint.getComplaintId()
    );

}


private static ComplaintCategory selectCategory(
        int choice) {


    switch(choice) {

        case 1:
            return ComplaintCategory.TECHNICAL;

        case 2:
            return ComplaintCategory.BILLING;

        case 3:
            return ComplaintCategory.SERVICE;

        case 4:
            return ComplaintCategory.PRODUCT;

        case 5:
            return ComplaintCategory.INFRASTRUCTURE;

        default:
            return ComplaintCategory.OTHER;
    }

}


private static ComplaintPriority selectPriority(
        int choice) {


    switch(choice) {


        case 1:
            return ComplaintPriority.LOW;


        case 2:
            return ComplaintPriority.MEDIUM;


        case 3:
            return ComplaintPriority.HIGH;


        case 4:
            return ComplaintPriority.CRITICAL;


        default:
            return ComplaintPriority.MEDIUM;

    }

}

/**
 * View complaints created by logged-in user.
 */
private static void viewMyComplaints() {


    List<Complaint> complaints =
            complaintService.getComplaintsByUser(
                    currentUser.getUserId()
            );


    System.out.println();

    System.out.println(
            "===== MY COMPLAINTS ====="
    );


    if(complaints.isEmpty()) {

        System.out.println(
                "No complaints found."
        );

        return;

    }



    for(Complaint complaint : complaints) {


        System.out.println(
                "Complaint ID: "
                + complaint.getComplaintId()
        );


        System.out.println(
                "Title: "
                + complaint.getTitle()
        );


        System.out.println(
                "Status: "
                + complaint.getStatus()
        );


        System.out.println(
                "Priority: "
                + complaint.getPriority()
        );


        System.out.println(
                "--------------------------"
        );

    }

}


/**
 * Admin login.
 */
private static void adminLogin() {

    try {

        System.out.println();

        System.out.println(
                "===== ADMIN LOGIN ====="
        );


        System.out.print(
                "Enter email: "
        );

        String email =
                scanner.nextLine();


        System.out.print(
                "Enter password: "
        );

        String password =
                scanner.nextLine();



        User admin =
                authenticationService.login(
                        email,
                        password
                );


        if(authenticationService.isAdmin(admin)) {


            currentUser = admin;


            System.out.println();

            System.out.println(
                    "Admin login successful."
            );


            adminDashboard();


        }
        else {


            System.out.println(
                    "Access denied."
            );


        }


    }
    catch(AuthenticationException e) {


        System.out.println(
                e.getMessage()
        );


    }

}

/**
 * Admin dashboard.
 */
private static void adminDashboard() {


    int choice;


    do {


        System.out.println();

        System.out.println(
                "===== ADMIN DASHBOARD ====="
        );


        System.out.println(
        "1. View All Complaints"
);

System.out.println(
        "2. Search Complaint"
);

System.out.println(
        "3. Assign Complaint"
);

System.out.println(
        "4. Update Complaint Status"
);

System.out.println(
        "5. Change Priority"
);

System.out.println(
        "6. Add Resolution"
);

System.out.println(
        "7. Close Complaint"
);

System.out.println(
        "8. Logout"
);


        System.out.print(
                "Enter choice: "
        );


        choice =
        InputUtil.getInt(
                "Enter choice: "
        );



        switch(choice) {


    case 1:

        viewAllComplaints();

        break;


    case 2:

        searchComplaint();

        break;


    case 3:

        assignComplaint();

        break;


    case 4:

        updateComplaintStatus();

        break;


    case 5:

        updateComplaintPriority();

        break;


    case 6:

        addResolution();

        break;


    case 7:

        closeComplaint();

        break;


    case 8:

        currentUser = null;

        System.out.println(
                "Admin logged out."
        );

        break;


    default:

        System.out.println(
                "Invalid choice."
        );

}


    }
    while(currentUser != null);


}


/**
 * Display all complaints.
 */
private static void viewAllComplaints() {


    List<Complaint> complaints =
            adminService.getAllComplaints();



    System.out.println();

    System.out.println(
            "===== ALL COMPLAINTS ====="
    );


    if(complaints.isEmpty()) {


        System.out.println(
                "No complaints available."
        );


        return;

    }



    for(Complaint complaint : complaints) {


        System.out.println(
                "Complaint ID: "
                + complaint.getComplaintId()
        );


        System.out.println(
                "Title: "
                + complaint.getTitle()
        );


        System.out.println(
                "Category: "
                + complaint.getCategory()
        );


        System.out.println(
                "Priority: "
                + complaint.getPriority()
        );


        System.out.println(
                "Status: "
                + complaint.getStatus()
        );


        System.out.println(
                "---------------------------"
        );

    }

}

/**
 * Search complaint using ID.
 */
private static void searchComplaint() {


    System.out.print(
            "Enter Complaint ID: "
    );


    String complaintId =
            scanner.nextLine();



    Complaint complaint =
            adminService.searchComplaint(
                    complaintId
            );



    if(complaint == null) {


        System.out.println(
                "Complaint not found."
        );


        return;

    }



    System.out.println();

    System.out.println(
            "Complaint Details"
    );


    System.out.println(
            "ID: "
            + complaint.getComplaintId()
    );


    System.out.println(
            "Title: "
            + complaint.getTitle()
    );


    System.out.println(
            "Description: "
            + complaint.getDescription()
    );


    System.out.println(
            "Status: "
            + complaint.getStatus()
    );


    System.out.println(
            "Priority: "
            + complaint.getPriority()
    );

}

private static void assignComplaint() {


    System.out.print(
            "Enter Complaint ID: "
    );

    String complaintId =
            scanner.nextLine();



    System.out.print(
            "Assign to person: "
    );

    String person =
            scanner.nextLine();



    boolean result =
            adminService.assignComplaint(
                    complaintId,
                    person
            );



    if(result) {

        System.out.println(
                "Complaint assigned successfully."
        );

    }
    else {

        System.out.println(
                "Complaint not found."
        );

    }

}

private static void updateComplaintStatus() {


    System.out.print(
            "Enter Complaint ID: "
    );

    String complaintId =
            scanner.nextLine();



    System.out.println(
            "Select Status:"
    );


    System.out.println(
            "1. OPEN"
    );

    System.out.println(
            "2. ASSIGNED"
    );

    System.out.println(
            "3. IN_PROGRESS"
    );

    System.out.println(
            "4. RESOLVED"
    );

    System.out.println(
            "5. CLOSED"
    );


    int choice =
        InputUtil.getInt(
                "Enter choice: "
        );



    ComplaintStatus status;


    switch(choice) {

        case 1:
            status = ComplaintStatus.OPEN;
            break;


        case 2:
            status = ComplaintStatus.ASSIGNED;
            break;


        case 3:
            status = ComplaintStatus.IN_PROGRESS;
            break;


        case 4:
            status = ComplaintStatus.RESOLVED;
            break;


        case 5:
            status = ComplaintStatus.CLOSED;
            break;


        default:
            status = ComplaintStatus.OPEN;

    }



    boolean result =
            adminService.updateStatus(
                    complaintId,
                    status
            );



    if(result) {

        System.out.println(
                "Status updated successfully."
        );

    }
    else {

        System.out.println(
                "Complaint not found."
        );

    }

}

private static void updateComplaintPriority() {


    System.out.print(
            "Enter Complaint ID: "
    );

    String complaintId =
            scanner.nextLine();



    System.out.println(
            "Select Priority:"
    );


    System.out.println(
            "1. LOW"
    );

    System.out.println(
            "2. MEDIUM"
    );

    System.out.println(
            "3. HIGH"
    );

    System.out.println(
            "4. CRITICAL"
    );


    int choice =
        InputUtil.getInt(
                "Enter choice: "
        );


    ComplaintPriority priority;


    switch(choice) {


        case 1:
            priority = ComplaintPriority.LOW;
            break;


        case 2:
            priority = ComplaintPriority.MEDIUM;
            break;


        case 3:
            priority = ComplaintPriority.HIGH;
            break;


        case 4:
            priority = ComplaintPriority.CRITICAL;
            break;


        default:
            priority = ComplaintPriority.MEDIUM;

    }



    boolean result =
            adminService.updatePriority(
                    complaintId,
                    priority
            );



    if(result) {

        System.out.println(
                "Priority updated."
        );

    }
    else {

        System.out.println(
                "Complaint not found."
        );

    }

}

private static void addResolution() {


    System.out.print(
            "Enter Complaint ID: "
    );

    String complaintId =
            scanner.nextLine();



    System.out.print(
            "Enter resolution note: "
    );

    String resolution =
            scanner.nextLine();



    boolean result =
            adminService.resolveComplaint(
                    complaintId,
                    resolution
            );



    if(result) {

        System.out.println(
                "Complaint resolved successfully."
        );

    }
    else {

        System.out.println(
                "Complaint not found."
        );

    }

}

private static void closeComplaint() {


    System.out.print(
            "Enter Complaint ID: "
    );

    String complaintId =
            scanner.nextLine();



    boolean result =
            adminService.closeComplaint(
                    complaintId
            );



    if(result) {

        System.out.println(
                "Complaint closed successfully."
        );

    }
    else {

        System.out.println(
                "Complaint not found."
        );

    }

}


/**
 * Submit complaint feedback.
 */
private static void submitFeedback() {


    System.out.println();

    System.out.println(
            "===== SUBMIT FEEDBACK ====="
    );


    System.out.print(
            "Enter Complaint ID: "
    );


    String complaintId =
            scanner.nextLine();



    Complaint complaint =
            complaintService.getComplaintById(
                    complaintId
            );


    if(complaint == null) {


        System.out.println(
                "Complaint not found."
        );


        return;

    }



    if(!complaint.getUserId()
            .equals(currentUser.getUserId())) {


        System.out.println(
                "You cannot give feedback for this complaint."
        );


        return;

    }



    if(feedbackService.hasFeedback(
            complaintId)) {


        System.out.println(
                "Feedback already submitted."
        );


        return;

    }



    System.out.print(
            "Enter rating (1-5): "
    );


    int rating =
        InputUtil.getInt(
                "Enter rating (1-5): "
        );



    if(rating < 1 || rating > 5) {


        System.out.println(
                "Invalid rating."
        );


        return;

    }



    System.out.print(
            "Enter feedback comment: "
    );


    String comment =
            scanner.nextLine();



    Feedback feedback =
            new Feedback();


    feedback.setComplaintId(
            complaintId
    );


    feedback.setUserId(
            currentUser.getUserId()
    );


    feedback.setRating(
            rating
    );


    feedback.setComment(
            comment
    );



    feedbackService.submitFeedback(
            feedback
    );



    System.out.println();

    System.out.println(
            "Feedback submitted successfully."
    );

}


    /**
     * Main application menu.
     */
    private static void mainMenu() {

        int choice;


        do {

            System.out.println();
            System.out.println("===== MAIN MENU =====");
            System.out.println("1. Register User");
            System.out.println("2. User Login");
            System.out.println("3. Admin Login");
            System.out.println("4. Exit");


            System.out.print("Enter choice: ");

            choice =
        InputUtil.getInt(
                "Enter choice: "
        );

            switch(choice) {

                case 1:
                    registerUser();
                    break;


                case 2:
                    userLogin();
                    break;


                case 3:
                    adminLogin();
                    break;


                case 4:

                    System.out.println(
                            AppConstants.EXIT_MESSAGE
                    );

                    break;


                default:

                    System.out.println(
                            AppConstants.INVALID_CHOICE
                    );

            }


        } while(choice != 4);


    }

}