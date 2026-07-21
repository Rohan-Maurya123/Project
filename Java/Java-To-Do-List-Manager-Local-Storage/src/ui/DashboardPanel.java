package ui;


import service.TaskService;
import theme.AppColors;
import theme.AppFonts;
import theme.RoundedPanel;


import javax.swing.*;
import java.awt.*;



public class DashboardPanel extends JPanel {



    private TaskService taskService;



    private JLabel totalLabel;


    private JLabel completedLabel;


    private JLabel pendingLabel;


    private JLabel overdueLabel;





    public DashboardPanel(
            TaskService taskService
    ){


        this.taskService =
                taskService;



        initialize();


        createUI();


    }






    private void initialize(){


        setLayout(
                new BorderLayout()
        );



        setBackground(
                AppColors.BACKGROUND
        );



        setBorder(
                BorderFactory
                        .createEmptyBorder(
                                30,
                                30,
                                30,
                                30
                        )
        );


    }






    private void createUI(){


        JLabel title =
                new JLabel(
                        "Dashboard"
                );



        title.setFont(
                AppFonts.TITLE
        );



        title.setForeground(
                AppColors.TEXT
        );



        add(
                title,
                BorderLayout.NORTH
        );



        add(
                createCards(),
                BorderLayout.CENTER
        );


        refresh();


    }






    private JPanel createCards(){


        JPanel panel =
                new JPanel();



        panel.setOpaque(
                false
        );



        panel.setLayout(
                new GridLayout(
                        2,
                        2,
                        25,
                        25
                )
        );

                JPanel totalCard =
                createCard(
                        "Total Tasks",
                        totalLabel
                );



        JPanel completedCard =
                createCard(
                        "Completed",
                        completedLabel
                );



        JPanel pendingCard =
                createCard(
                        "Pending",
                        pendingLabel
                );



        JPanel overdueCard =
                createCard(
                        "Overdue",
                        overdueLabel
                );



        panel.add(
                totalCard
        );


        panel.add(
                completedCard
        );


        panel.add(
                pendingCard
        );


        panel.add(
                overdueCard
        );



        return panel;


    }






    private JPanel createCard(
            String title,
            JLabel valueLabel
    ){



        RoundedPanel card =
                new RoundedPanel();



        card.setLayout(
                new BorderLayout()
        );



        card.setBorder(
                BorderFactory
                        .createEmptyBorder(
                                20,
                                20,
                                20,
                                20
                        )
        );



        JLabel titleLabel =
                new JLabel(
                        title
                );



        titleLabel.setFont(
                AppFonts.BUTTON
        );



        titleLabel.setForeground(
                AppColors.TEXT
        );



        valueLabel =
                new JLabel(
                        "0",
                        SwingConstants.CENTER
                );



        valueLabel.setFont(
                AppFonts.TITLE
        );



        valueLabel.setForeground(
                AppColors.TEXT
        );



        if(title.equals("Total Tasks")){


            totalLabel =
                    valueLabel;


        }
        else if(
                title.equals("Completed")
        ){


            completedLabel =
                    valueLabel;


        }
        else if(
                title.equals("Pending")
        ){


            pendingLabel =
                    valueLabel;


        }
        else if(
                title.equals("Overdue")
        ){


            overdueLabel =
                    valueLabel;


        }



        card.add(
                titleLabel,
                BorderLayout.NORTH
        );



        card.add(
                valueLabel,
                BorderLayout.CENTER
        );



        return card;


    }

  
    public void refresh(){



        if(taskService == null){

            return;

        }



        if(totalLabel != null){


            totalLabel.setText(
                    String.valueOf(
                            taskService
                                    .getTotalTasks()
                    )
            );


        }





        if(completedLabel != null){


            completedLabel.setText(
                    String.valueOf(
                            taskService
                                    .getCompletedCount()
                    )
            );


        }





        if(pendingLabel != null){


            pendingLabel.setText(
                    String.valueOf(
                            taskService
                                    .getPendingCount()
                    )
            );


        }





        if(overdueLabel != null){


            overdueLabel.setText(
                    String.valueOf(
                            taskService
                                    .getOverdueCount()
                    )
            );


        }



    }



}