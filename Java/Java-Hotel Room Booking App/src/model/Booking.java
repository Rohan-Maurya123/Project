package model;

import java.time.LocalDate;




public class Booking {


    // Unique booking ID
    private String bookingId;


    // Customer details
    private Guest guest;


    // Room details
    private Room room;


    // Booking dates
    private LocalDate checkInDate;

    private LocalDate checkOutDate;


    // Number of nights
    private int numberOfNights;


    // Total payment amount
    private double totalAmount;


    // Booking status
    // CONFIRMED / CANCELLED
    private String bookingStatus;



    // Constructor

    public Booking(
            String bookingId,
            Guest guest,
            Room room,
            LocalDate checkInDate,
            LocalDate checkOutDate
    ) {


        this.bookingId = bookingId;

        this.guest = guest;

        this.room = room;

        this.checkInDate = checkInDate;

        this.checkOutDate = checkOutDate;


        // Calculate number of nights

        this.numberOfNights =
                checkOutDate.getDayOfYear()
                -
                checkInDate.getDayOfYear();



        // Calculate total amount

        this.totalAmount =
                room.getPricePerNight()
                *
                numberOfNights;



        // Default status

        this.bookingStatus = "CONFIRMED";


    }





    // Getter for booking ID

    public String getBookingId() {

        return bookingId;

    }





    // Getter for guest

    public Guest getGuest() {

        return guest;

    }





    // Getter for room

    public Room getRoom() {

        return room;

    }





    // Getter for amount

    public double getTotalAmount() {

        return totalAmount;

    }





    // Getter for status

    public String getBookingStatus() {

        return bookingStatus;

    }





    // Cancel booking method

    public void cancelBooking() {


        bookingStatus = "CANCELLED";


        // Make room available again

        room.setAvailable(true);


    }





    // Display booking details

    public void displayBookingDetails() {


        System.out.println("\n========== BOOKING DETAILS ==========");


        System.out.println("Booking ID : " + bookingId);


        System.out.println("\nGuest Information:");

        guest.displayGuestDetails();



        System.out.println("\nRoom Information:");

        room.displayRoomDetails();



        System.out.println("Check-in Date : " + checkInDate);


        System.out.println("Check-out Date : " + checkOutDate);


        System.out.println("Number of Nights : " + numberOfNights);


        System.out.println("Total Amount : Rs." + totalAmount);


        System.out.println("Booking Status : " + bookingStatus);



        System.out.println("====================================");

    }


}