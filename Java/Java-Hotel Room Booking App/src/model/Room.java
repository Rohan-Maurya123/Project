package model;


public class Room {

    // Room unique number
    private int roomId;

    // Single, Double, Deluxe, Suite
    private String roomType;

    // Price for one night
    private double pricePerNight;

    // true = available
    // false = booked
    private boolean available;

    // Maximum people allowed
    private int capacity;


    // Constructor
    public Room(int roomId, String roomType, double pricePerNight, int capacity) {

        this.roomId = roomId;
        this.roomType = roomType;
        this.pricePerNight = pricePerNight;
        this.capacity = capacity;

        // Initially every room is available
        this.available = true;
    }


    // Getter for room ID
    public int getRoomId() {
        return roomId;
    }


    // Getter for room type
    public String getRoomType() {
        return roomType;
    }


    // Getter for price
    public double getPricePerNight() {
        return pricePerNight;
    }


    // Getter for availability
    public boolean isAvailable() {
        return available;
    }


    // Change room status
    public void setAvailable(boolean available) {
        this.available = available;
    }


    // Getter for capacity
    public int getCapacity() {
        return capacity;
    }


    // Display room information
    public void displayRoomDetails() {

        System.out.println("----------------------------");

        System.out.println("Room ID : " + roomId);

        System.out.println("Room Type : " + roomType);

        System.out.println("Price/Night : Rs." + pricePerNight);

        System.out.println("Capacity : " + capacity + " guests");


        if (available) {
            System.out.println("Status : Available");
        } 
        else {
            System.out.println("Status : Booked");
        }

        System.out.println("----------------------------");
    }
}