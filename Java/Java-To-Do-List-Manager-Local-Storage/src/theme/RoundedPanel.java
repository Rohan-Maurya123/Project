package theme;


import javax.swing.*;
import java.awt.*;




public class RoundedPanel extends JPanel {




    public RoundedPanel(){


        setOpaque(
                false
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



        g.setColor(
                AppColors.CARD
        );



        g.fillRoundRect(
                0,
                0,
                getWidth(),
                getHeight(),
                UIConstants.CARD_RADIUS,
                UIConstants.CARD_RADIUS
        );



        g.dispose();



        super.paintComponent(
                graphics
        );


    }


}