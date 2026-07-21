package service;

import constants.AppConstants;
import exception.AuthenticationException;
import model.User;
import model.UserRole;
import utility.IdGenerator;

public class AuthenticationService {

    private final UserService userService;

    public AuthenticationService() {
        userService = new UserService();
        createDefaultAdmin();
    }

  
    private void createDefaultAdmin() {

        if (userService.getUserByEmail(AppConstants.DEFAULT_ADMIN_EMAIL) == null) {

            User admin = new User(
                    IdGenerator.generateUserId(),
                    AppConstants.DEFAULT_ADMIN_NAME,
                    AppConstants.DEFAULT_ADMIN_EMAIL,
                    AppConstants.DEFAULT_ADMIN_PASSWORD,
                    UserRole.ADMIN
            );

            try {
                userService.registerUser(admin);
            } catch (Exception ignored) {
            }

        }

    }

    public User login(String email, String password)
            throws AuthenticationException {

        User user = userService.getUserByEmail(email);

        if (user == null) {
            throw new AuthenticationException("User not found.");
        }

        if (!user.getPassword().equals(password)) {
            throw new AuthenticationException("Invalid password.");
        }

        return user;

    }


    public boolean isAdmin(User user) {

        return user != null &&
                user.getRole() == UserRole.ADMIN;

    }

}