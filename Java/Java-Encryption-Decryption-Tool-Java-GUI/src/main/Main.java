package main;


import gui.EncryptionFrame;

import javax.swing.*;



public class Main {



    public static void main(String[] args) {


        try {


            // Apply system UI theme

            UIManager.setLookAndFeel(
                    UIManager
                    .getSystemLookAndFeelClassName()
            );



            // Start GUI

            SwingUtilities.invokeLater(
                    () -> {


                        EncryptionFrame frame =
                                new EncryptionFrame();



                        frame.setVisible(true);


                    }
            );


        }


        catch(Exception e){


            JOptionPane.showMessageDialog(
                    null,
                    "Application failed to start:\n"
                            +
                            e.getMessage(),
                    "Startup Error",
                    JOptionPane.ERROR_MESSAGE
            );


        }


    }


}