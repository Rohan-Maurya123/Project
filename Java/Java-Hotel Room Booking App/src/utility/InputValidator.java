package utility;




public class InputValidator {



    // Check if text is empty

    public static boolean isEmpty(String value) {


        if(value == null || value.trim().isEmpty()) {

            return true;

        }


        return false;

    }





    // Validate phone number

    public static boolean isValidPhone(String phone) {




        return phone.matches("[0-9]{10}");


    }





    // Validate email

    public static boolean isValidEmail(String email) {



        return email.contains("@")
                &&
                email.contains(".");


    }





    // Validate guest capacity

    public static boolean isValidGuestCount(
            int guests,
            int capacity
    ) {


        return guests <= capacity;


    }




    // Validate date order

    public static boolean isValidDateOrder(
            java.time.LocalDate checkIn,
            java.time.LocalDate checkOut
    ) {

        return checkOut.isAfter(checkIn);


    }



}