package service;

import exception.DuplicateUserException;
import model.User;
import repository.UserRepository;

import java.util.List;

public class UserService {

    private final UserRepository userRepository;
    private final List<User> users;

    public UserService() {

        userRepository = new UserRepository();
        users = userRepository.loadUsers();

    }


    public void registerUser(User user)
            throws DuplicateUserException {

        if (getUserByEmail(user.getEmail()) != null) {
            throw new DuplicateUserException(
                    "Email already registered."
            );
        }

        users.add(user);

        userRepository.saveUsers(users);

    }


    public User getUserByEmail(String email) {

        for (User user : users) {

            if (user.getEmail().equalsIgnoreCase(email)) {
                return user;
            }

        }

        return null;

    }

 
    public User getUserById(String userId) {

        for (User user : users) {

            if (user.getUserId().equalsIgnoreCase(userId)) {
                return user;
            }

        }

        return null;

    }


    public List<User> getAllUsers() {

        return users;

    }

}