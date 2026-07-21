package main;

import ui.MainFrame;

import javax.swing.SwingUtilities;



public class Main {


  
    public static void main(String[] args){


        SwingUtilities.invokeLater(
                () -> {


                    MainFrame application =
                            new MainFrame();



                    application.setVisible(
                            true
                    );


                }
        );


    }


}