package utility;


import java.io.File;


public class InputValidator {


    // Validate normal text input

    public static boolean validateText(String text) {

        return text != null &&
                !text.trim().isEmpty();

    }



    // Validate password

    public static boolean validatePassword(String password) {

        return password != null &&
                !password.trim().isEmpty();

    }




    // Validate file

    public static boolean validateFile(File file) {


        return file != null &&
                file.exists() &&
                file.isFile();

    }



    // Get error message for text

    public static String textErrorMessage() {

        return "Text input cannot be empty.";

    }



    // Get error message for password

    public static String passwordErrorMessage() {

        return "Password cannot be empty.";

    }



    // Get error message for file

    public static String fileErrorMessage() {

        return "Please select a valid file.";

    }


}