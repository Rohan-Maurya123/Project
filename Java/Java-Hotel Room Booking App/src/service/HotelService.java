package service;


import model.*;
import repository.FileManager;


import java.time.LocalDate;
import java.util.ArrayList;
import java.util.List;





public class HotelService {



    // Stores all hotel rooms

    private List<Room> rooms;



    // Stores current bookings

    private List<Booking> bookings;



    // Booking counter

    private int bookingCounter = 1001;





    // Constructor

    public HotelService() {


        rooms = new ArrayList<>();

        bookings = new ArrayList<>();


        createRooms();

        loadLastBookingId();
    }



    private void loadLastBookingId() {

    List<String> records =
            FileManager.readBookings();


    if(!records.isEmpty()) {


        String lastRecord =
                records.get(records.size() - 1);


        String lastId =
                lastRecord.split(",")[0];


        int number =
                Integer.parseInt(
                        lastId.substring(2)
                );


        bookingCounter = number + 1;

    }

}



    // Creating default hotel rooms

    private void createRooms() {



        rooms.add(
                new Room(
                        101,
                        "Single",
                        1500,
                        1
                )
        );



        rooms.add(
                new Room(
                        102,
                        "Single",
                        1500,
                        1
                )
        );



        rooms.add(
                new Room(
                        201,
                        "Double",
                        2500,
                        2
                )
        );



        rooms.add(
                new Room(
                        202,
                        "Double",
                        2500,
                        2
                )
        );



        rooms.add(
                new Room(
                        301,
                        "Deluxe",
                        3000,
                        3
                )
        );



        rooms.add(
                new Room(
                        401,
                        "Suite",
                        5000,
                        5
                )
        );



    }







    // Display available rooms

    public void displayAvailableRooms() {



        System.out.println(
                "\n===== AVAILABLE ROOMS ====="
        );



        for(Room room : rooms) {


            if(room.isAvailable()) {


                room.displayRoomDetails();


            }


        }


    }








    // Search room by type

    public void searchRoom(String type) {



        boolean found = false;



        System.out.println(
                "\nSearch Result:"
        );



        for(Room room : rooms) {



            if(
                    room.getRoomType()
                            .equalsIgnoreCase(type)
                    &&
                    room.isAvailable()
            ) {



                room.displayRoomDetails();

                found = true;


            }



        }




        if(!found) {


            System.out.println(
                    "No room available."
            );


        }


    }







    // Find room using room ID

    public Room getRoomById(int id) {



        for(Room room : rooms) {



            if(room.getRoomId() == id) {


                return room;


            }


        }



        return null;


    }







    // Create booking

    public Booking createBooking(
            Guest guest,
            int roomId,
            LocalDate checkIn,
            LocalDate checkOut
    ) {



        Room room =
                getRoomById(roomId);




        if(room == null) {


            System.out.println(
                    "Room not found"
            );


            return null;


        }




        if(!room.isAvailable()) {


            System.out.println(
                    "Room already booked"
            );


            return null;


        }




        String bookingId =
                "BK"
                +
                bookingCounter++;





        Booking booking =
                new Booking(
                        bookingId,
                        guest,
                        room,
                        checkIn,
                        checkOut
                );




        room.setAvailable(false);



        bookings.add(booking);



        FileManager.saveBooking(booking);




        return booking;


    }








    // Find booking

    public Booking getBookingById(String id) {



        for(Booking booking : bookings) {



            if(
                    booking.getBookingId()
                            .equalsIgnoreCase(id)
            ) {


                return booking;


            }


        }



        return null;


    }







    // Cancel booking

    public void cancelBooking(String id) {



        Booking booking =
                getBookingById(id);



        if(booking == null) {



            System.out.println(
                    "Booking not found"
            );


            return;


        }




        booking.cancelBooking();


        FileManager.updateBookingFile(bookings);
        System.out.println(
                "Booking cancelled successfully"
        );


    }







    // Display booking details

    public void viewBooking(String id) {



        Booking booking =
                getBookingById(id);



        if(booking != null) {


            booking.displayBookingDetails();


        }

        else {


            System.out.println(
                    "Booking not found"
            );


        }


    }






    // Show all bookings

    public void showBookingHistory() {


        FileManager.displayBookingHistory();


    }



}