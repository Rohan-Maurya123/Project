package utility;

public class InputValidator {

    private InputValidator() {
    }

    public static boolean isValidEmail(String email) {

        if (email == null) {
            return false;
        }

        return email.matches("^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$");
    }

    public static boolean isValidPassword(String password) {

        return password != null && password.length() >= 6;
    }

    public static boolean isNotBlank(String value) {

        return value != null && !value.trim().isEmpty();
    }

}