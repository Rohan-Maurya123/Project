package ui;

import service.TaskService;
import theme.AppColors;
import theme.AppFonts;
import theme.RoundedButton;
import theme.RoundedPanel;
import theme.UIConstants;

import javax.swing.*;
import java.awt.*;

public class MainFrame extends JFrame {


    private TaskService taskService;


    private JPanel contentPanel;

    private DashboardPanel dashboardPanel;

    private TaskManagementPanel taskManagementPanel;


    private JLabel titleLabel;



    /**
     * Constructor
     */
    public MainFrame() {


        taskService =
                new TaskService();



        initializeFrame();


        createLayout();


    }





    /**
     * Configure JFrame.
     */
    private void initializeFrame() {


        setTitle(
                "To-Do List Manager - Local Storage"
        );


        setSize(
                UIConstants.WINDOW_WIDTH,
                UIConstants.WINDOW_HEIGHT
        );


        setMinimumSize(
                new Dimension(
                        1000,
                        650
                )
        );


        setLocationRelativeTo(null);
        setResizable(true);


        setDefaultCloseOperation(
                JFrame.EXIT_ON_CLOSE
        );


        getContentPane()
                .setBackground(
                        AppColors.BACKGROUND
                );

    }






    /**
     * Create main layout.
     */
    private void createLayout() {


        setLayout(
                new BorderLayout()
        );




        JPanel sidebar =
                createSidebar();




        add(
                sidebar,
                BorderLayout.WEST
        );




        contentPanel =
                new JPanel(
                        new BorderLayout()
                );


        contentPanel.setBackground(
                AppColors.BACKGROUND
        );




        add(
                contentPanel,
                BorderLayout.CENTER
        );




        showDashboard();

    }





    /**
     * Create left navigation sidebar.
     */
    private JPanel createSidebar() {


        JPanel sidebar =
                new JPanel();



        sidebar.setPreferredSize(
                new Dimension(
                        240,
                        getHeight()
                )
        );



        sidebar.setBackground(
                AppColors.SIDEBAR
        );



        sidebar.setLayout(
                new BoxLayout(
                        sidebar,
                        BoxLayout.Y_AXIS
                )
        );



        JLabel logo =
                new JLabel(
                        " TASK MANAGER "
                );


        logo.setFont(
                AppFonts.TITLE
        );


        logo.setForeground(
                AppColors.TEXT
        );


        logo.setAlignmentX(
                Component.CENTER_ALIGNMENT
        );


        sidebar.add(
                Box.createVerticalStrut(
                        30
                )
        );


        sidebar.add(logo);


        sidebar.add(
                Box.createVerticalStrut(
                        40
                )
        );

                RoundedButton dashboardButton =
                createMenuButton(
                        "Dashboard"
                );


        RoundedButton tasksButton =
                createMenuButton(
                        "All Tasks"
                );


        RoundedButton addButton =
                createMenuButton(
                        "Add New Task"
                );


        RoundedButton completedButton =
                createMenuButton(
                        "Completed"
                );


        RoundedButton settingsButton =
                createMenuButton(
                        "Settings"
                );




        sidebar.add(
                dashboardButton
        );


        sidebar.add(
                Box.createVerticalStrut(
                        15
                )
        );


        sidebar.add(
                tasksButton
        );


        sidebar.add(
                Box.createVerticalStrut(
                        15
                )
        );


        sidebar.add(
                addButton
        );


        sidebar.add(
                Box.createVerticalStrut(
                        15
                )
        );


        sidebar.add(
                completedButton
        );


        sidebar.add(
                Box.createVerticalStrut(
                        15
                )
        );


        sidebar.add(
                settingsButton
        );



        dashboardButton.addActionListener(
                e ->
                        showDashboard()
        );



        tasksButton.addActionListener(
                e ->
                        showTasks()
        );



        addButton.addActionListener(
                e ->
                        openAddTaskDialog()
        );



        completedButton.addActionListener(
                e ->
                        showCompletedTasks()
        );



        return sidebar;

    }





    /**
     * Create sidebar menu button.
     */
    private RoundedButton createMenuButton(
            String text
    ) {


        RoundedButton button =
                new RoundedButton(
                        text
                );




        button.setMaximumSize(
                new Dimension(
                        200,
                        45
                )
        );


        button.setAlignmentX(
                Component.CENTER_ALIGNMENT
        );

        button.setForeground(
        AppColors.TEXT
);


        return button;

    }






    /**
     * Change center panel content.
     */
    private void setContent(
            JPanel panel
    ) {


        contentPanel.removeAll();


        contentPanel.add(
                panel,
                BorderLayout.CENTER
        );


        contentPanel.revalidate();


        contentPanel.repaint();

    }






/**
 * Display dashboard screen.
 */
private void showDashboard(){


    if(dashboardPanel == null){


        dashboardPanel =
                new DashboardPanel(
                        taskService
                );

    }


    dashboardPanel.refresh();


    setContent(
            dashboardPanel
    );

}
/**
 * Display task management screen.
 */
private void showTasks(){


    if(taskManagementPanel == null){


        taskManagementPanel =
                new TaskManagementPanel(
                        taskService
                );

    }


    taskManagementPanel.refresh();


    setContent(
            taskManagementPanel
    );


}



/**
 * Display completed tasks.
 */
private void showCompletedTasks(){


    JPanel panel =
            new RoundedPanel();




    panel.setLayout(
            new BorderLayout()
    );




    panel.setBorder(
            BorderFactory
                    .createEmptyBorder(
                            25,
                            25,
                            25,
                            25
                    )
    );




    JLabel heading =
            new JLabel(
                    "Completed Tasks"
            );




    heading.setFont(
            AppFonts.TITLE
    );


    heading.setForeground(
            AppColors.TEXT
    );




    panel.add(
            heading,
            BorderLayout.NORTH
    );




    JTextArea area =
            new JTextArea();




    area.setEditable(false);


    area.setFont(
            AppFonts.NORMAL
    );


    area.setForeground(
            AppColors.TEXT
    );


    area.setBackground(
            AppColors.BACKGROUND
    );




    StringBuilder data =
            new StringBuilder();




    taskService
            .getCompletedTasks()
            .forEach(
                    task -> {


                        data.append(
                                task.getTitle()
                        );


                        data.append(
                                "\n"
                        );

                    }
            );




    area.setText(
            data.toString()
    );




    panel.add(
            new JScrollPane(area),
            BorderLayout.CENTER
    );




    setContent(
            panel
    );

}



/**
 * Open add task dialog.
 */
private void openAddTaskDialog(){


    AddTaskDialog dialog =
            new AddTaskDialog(
                    this,
                    taskService
            );


    dialog.setVisible(
            true
    );




    if(dashboardPanel != null){

        dashboardPanel.refresh();

    }




    if(taskManagementPanel != null){

        taskManagementPanel.refresh();

    }


}






    /**
     * Get service instance.
     */
    public TaskService getTaskService(){


        return taskService;

    }

/**
 * Refresh all screens.
 */
public void refresh(){


    if(dashboardPanel != null){

        dashboardPanel.refresh();

    }




    if(taskManagementPanel != null){

        taskManagementPanel.refresh();

    }




    showDashboard();

}





/**
 * Application entry point.
 */
public static void main(String[] args){


    SwingUtilities.invokeLater(
            () -> {


                try {


                    UIManager
                            .setLookAndFeel(
                                    UIManager
                                            .getSystemLookAndFeelClassName()
                            );


                }
                catch(Exception e){


                    e.printStackTrace();


                }




                MainFrame frame =
                        new MainFrame();




                frame.setVisible(
                        true
                );


            }
    );


}
}
