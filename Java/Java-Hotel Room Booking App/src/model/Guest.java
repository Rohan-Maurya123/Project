package model;


public class Guest {


    // Customer name
    private String name;


    // Customer phone number
    private String phoneNumber;


    // Customer email
    private String email;


    // Identity proof details
    private String idProof;



    // Constructor

    public Guest(String name, String phoneNumber, String email, String idProof) {

        this.name = name;
        this.phoneNumber = phoneNumber;
        this.email = email;
        this.idProof = idProof;

    }



    // Getter for name

    public String getName() {

        return name;

    }



    // Getter for phone number

    public String getPhoneNumber() {

        return phoneNumber;

    }



    // Getter for email

    public String getEmail() {

        return email;

    }



    // Getter for ID proof

    public String getIdProof() {

        return idProof;

    }



    // Display guest details

    public void displayGuestDetails() {


        System.out.println("----------------------------");

        System.out.println("Guest Name : " + name);

        System.out.println("Phone Number : " + phoneNumber);

        System.out.println("Email : " + email);

        System.out.println("ID Proof : " + idProof);

        System.out.println("----------------------------");


    }


}