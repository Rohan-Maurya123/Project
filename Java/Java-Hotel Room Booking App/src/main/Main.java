package main;


import model.*;

import service.HotelService;

import utility.InputValidator;


import java.time.LocalDate;

import java.util.Scanner;





public class Main {



    public static void main(String[] args) {



        Scanner scanner =
                new Scanner(System.in);



        HotelService hotelService =
                new HotelService();



        boolean running = true;




        while(running) {



            System.out.println(
                    "\n========== HOTEL BOOKING SYSTEM =========="
            );


            System.out.println(
                    "1. View Available Rooms"
            );


            System.out.println(
                    "2. Search Room"
            );


            System.out.println(
                    "3. Book Room"
            );


            System.out.println(
                    "4. View Booking"
            );


            System.out.println(
                    "5. Cancel Booking"
            );


            System.out.println(
                    "6. Booking History"
            );


            System.out.println(
                    "7. Exit"
            );



            System.out.print(
                    "Enter choice: "
            );



            int choice =
                    scanner.nextInt();


            scanner.nextLine();





            switch(choice) {



                case 1:


                    hotelService.displayAvailableRooms();

                    break;





                case 2:


                    System.out.print(
                            "Enter room type: "
                    );


                    String type =
                            scanner.nextLine();



                    hotelService.searchRoom(type);


                    break;







                case 3:


                    System.out.println(
                            "\nEnter Guest Details"
                    );



                    System.out.print(
                            "Name: "
                    );


                    String name =
                            scanner.nextLine();



                    if(InputValidator.isEmpty(name)) {


                        System.out.println(
                                "Name cannot be empty"
                        );


                        break;

                    }






                    System.out.print(
                            "Phone: "
                    );


                    String phone =
                            scanner.nextLine();




                    if(!InputValidator.isValidPhone(phone)) {


                        System.out.println(
                                "Invalid phone number"
                        );


                        break;

                    }





                    System.out.print(
                            "Email: "
                    );


                    String email =
                            scanner.nextLine();




                    System.out.print(
                            "ID Proof: "
                    );


                    String id =
                            scanner.nextLine();





                    Guest guest =
                            new Guest(
                                    name,
                                    phone,
                                    email,
                                    id
                            );





                    System.out.print(
                            "Enter Room ID: "
                    );


                    int roomId =
                            scanner.nextInt();


                    scanner.nextLine();





                    System.out.print(
                            "Check-in date (YYYY-MM-DD): "
                    );


                    LocalDate checkIn =
                            LocalDate.parse(
                                    scanner.nextLine()
                            );






                    System.out.print(
                            "Check-out date (YYYY-MM-DD): "
                    );


                    LocalDate checkOut =
                            LocalDate.parse(
                                    scanner.nextLine()
                            );





                    if(!InputValidator.isValidDateOrder(checkIn,checkOut)) {


                        System.out.println(
                                "Invalid date selection"
                        );


                        break;


                    }






                    Booking booking =
                            hotelService.createBooking(
                                    guest,
                                    roomId,
                                    checkIn,
                                    checkOut
                            );




                    if(booking != null) {


                        booking.displayBookingDetails();


                    }




                    break;









                case 4:


                    System.out.print(
                            "Enter Booking ID: "
                    );


                    String bookingId =
                            scanner.nextLine();



                    hotelService.viewBooking(
                            bookingId
                    );


                    break;








                case 5:


                    System.out.print(
                            "Enter Booking ID: "
                    );


                    String cancelId =
                            scanner.nextLine();



                    hotelService.cancelBooking(
                            cancelId
                    );


                    break;








                case 6:


                    hotelService.showBookingHistory();


                    break;








                case 7:


                    running = false;


                    System.out.println(
                            "Thank you for using Hotel Booking System"
                    );


                    break;







                default:


                    System.out.println(
                            "Invalid choice"
                    );



            }




        }





        scanner.close();


    }


}