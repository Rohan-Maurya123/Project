package repository;


import model.Booking;

import java.io.*;

import java.util.ArrayList;
import java.util.List;





public class FileManager {



    private static final String FILE_PATH =
            "data/bookings.txt";




    // Save booking data into file

    public static void saveBooking(Booking booking) {



        try {


            FileWriter writer =
                    new FileWriter(
                            FILE_PATH,
                            true
                    );


            BufferedWriter buffer =
                    new BufferedWriter(writer);



            String data =
                    booking.getBookingId()
                    + ","
                    + booking.getGuest().getName()
                    + ","
                    + booking.getGuest().getPhoneNumber()
                    + ","
                    + booking.getRoom().getRoomType()
                    + ","
                    + booking.getRoom().getRoomId()
                    + ","
                    + booking.getTotalAmount()
                    + ","
                    + booking.getBookingStatus();



            buffer.write(data);


            buffer.newLine();


            buffer.close();



            System.out.println(
                    "Booking saved successfully!"
            );



        }

        catch(IOException e) {


            System.out.println(
                    "Error saving booking data"
            );


            e.printStackTrace();

        }


    }


    public static void updateBookingFile(List<Booking> bookings) {


    try {


        FileWriter writer =
                new FileWriter(FILE_PATH);



        BufferedWriter buffer =
                new BufferedWriter(writer);



        for(Booking booking : bookings) {


            String data =
                    booking.getBookingId()
                    + ","
                    + booking.getGuest().getName()
                    + ","
                    + booking.getGuest().getPhoneNumber()
                    + ","
                    + booking.getRoom().getRoomType()
                    + ","
                    + booking.getRoom().getRoomId()
                    + ","
                    + booking.getTotalAmount()
                    + ","
                    + booking.getBookingStatus();


            buffer.write(data);

            buffer.newLine();

        }


        buffer.close();


    }


    catch(IOException e) {


        e.printStackTrace();

    }


}



    // Read booking history

    public static List<String> readBookings() {



        List<String> bookings =
                new ArrayList<>();



        try {


            FileReader reader =
                    new FileReader(
                            FILE_PATH
                    );



            BufferedReader buffer =
                    new BufferedReader(reader);



            String line;



            while(
                    (line = buffer.readLine())
                    != null
            ) {


                bookings.add(line);


            }



            buffer.close();



        }


        catch(IOException e) {



            System.out.println(
                    "No booking history found"
            );


        }



        return bookings;



    }






    // Display all bookings

    public static void displayBookingHistory() {



        List<String> bookings =
                readBookings();



        if(bookings.isEmpty()) {


            System.out.println(
                    "No bookings available."
            );


            return;

        }



        System.out.println(
                "\n===== BOOKING HISTORY ====="
        );



        for(String booking : bookings) {


            System.out.println(booking);


        }



        System.out.println(
                "==========================="
        );


    }


}