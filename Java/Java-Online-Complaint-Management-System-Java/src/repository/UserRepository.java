package repository;

import constants.AppConstants;
import model.User;
import model.UserRole;
import utility.FileManager;

import java.util.ArrayList;
import java.util.List;

public class UserRepository {


    public List<User> loadUsers() {

        List<User> users = new ArrayList<>();

        List<String> lines =
                FileManager.readLines(AppConstants.USERS_FILE);

        for (String line : lines) {

            if (line.trim().isEmpty()) {
                continue;
            }

            String[] data = line.split("\\|");

            if (data.length < 5) {
                continue;
            }

            User user = new User(
                    data[0],
                    data[1],
                    data[2],
                    data[3],
                    UserRole.valueOf(data[4])
            );

            users.add(user);
        }

        return users;
    }


    public void saveUsers(List<User> users) {

        List<String> lines = new ArrayList<>();

        for (User user : users) {

            String record =
                    user.getUserId() + "|" +
                    user.getName() + "|" +
                    user.getEmail() + "|" +
                    user.getPassword() + "|" +
                    user.getRole();

            lines.add(record);
        }

        FileManager.writeLines(
                AppConstants.USERS_FILE,
                lines
        );
    }

}