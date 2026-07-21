package theme;


import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;




public class RoundedButton extends JButton {



    private boolean hover = false;





 
    public RoundedButton(
            String text
    ){


        super(text);



        setFont(
                AppFonts.BUTTON
        );



        setForeground(
                AppColors.TEXT
        );



        setBackground(
                AppColors.BUTTON
        );



        setFocusPainted(
                false
        );



        setBorderPainted(
                false
        );



        setContentAreaFilled(
                false
        );



        setCursor(
                new Cursor(
                        Cursor.HAND_CURSOR
                )
        );



        setPreferredSize(
                new Dimension(
                        140,
                        UIConstants.BUTTON_HEIGHT
                )
        );



        addMouseListener(
                new MouseAdapter(){



                    @Override
                    public void mouseEntered(
                            MouseEvent e
                    ){


                        hover =
                                true;


                        repaint();


                    }



                    @Override
                    public void mouseExited(
                            MouseEvent e
                    ){


                        hover =
                                false;


                        repaint();


                    }


                }
        );

    }





    @Override
    protected void paintComponent(
            Graphics graphics
    ){


        Graphics2D g =
                (Graphics2D)
                        graphics.create();



        g.setRenderingHint(
                RenderingHints.KEY_ANTIALIASING,
                RenderingHints.VALUE_ANTIALIAS_ON
        );



        if(hover){


            g.setColor(
                    AppColors.BUTTON_HOVER
            );


        }
        else{


            g.setColor(
                    AppColors.BUTTON
            );


        }



        g.fillRoundRect(
                0,
                0,
                getWidth(),
                getHeight(),
                UIConstants.BUTTON_RADIUS,
                UIConstants.BUTTON_RADIUS
        );



        g.dispose();



        super.paintComponent(
                graphics
        );


    }

}