package common;


public final class UsernameValidator {

    private UsernameValidator() {
    }


    public static boolean isValid(String username) {

        if (username == null) {
            return false;
        }

        username = username.trim();

        if (username.isEmpty()) {
            return false;
        }

        if (username.length() < 3 || username.length() > 20) {
            return false;
        }

        return username.matches("[A-Za-z0-9_]+");
    }

}