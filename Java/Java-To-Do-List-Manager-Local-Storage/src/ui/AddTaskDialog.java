package ui;

import model.TaskCategory;
import model.TaskPriority;
import service.TaskService;
import theme.AppColors;
import theme.AppFonts;
import theme.RoundedButton;
import theme.UIConstants;

import javax.swing.*;
import java.awt.*;
import java.time.LocalDate;
import java.time.format.DateTimeParseException;



public class AddTaskDialog extends JDialog {


    private TaskService taskService;


    private JTextField titleField;


    private JTextArea descriptionArea;


    private JComboBox<TaskPriority> priorityBox;


    private JComboBox<TaskCategory> categoryBox;


    private JTextField dueDateField;




    /**
     * Constructor
     */
    public AddTaskDialog(
            JFrame parent,
            TaskService taskService
    ) {


        super(
                parent,
                "Add New Task",
                true
        );


        this.taskService =
                taskService;



        initializeDialog();


        createUI();

    }





    /**
     * Configure dialog.
     */
    private void initializeDialog(){


        setSize(
                UIConstants.DIALOG_WIDTH,
                UIConstants.DIALOG_HEIGHT
        );



        setLocationRelativeTo(
                getParent()
        );



        getContentPane()
                .setBackground(
                        AppColors.BACKGROUND
                );


    }





    /**
     * Build form UI.
     */
    private void createUI(){


        JPanel mainPanel =
                new JPanel();



        mainPanel.setLayout(
                new GridBagLayout()
        );



        mainPanel.setBackground(
                AppColors.BACKGROUND
        );



        GridBagConstraints gbc =
                new GridBagConstraints();



        gbc.insets =
                new Insets(
                        10,
                        10,
                        10,
                        10
                );


        gbc.fill =
                GridBagConstraints.HORIZONTAL;



        JLabel heading =
                new JLabel(
                        "Create New Task"
                );


        heading.setFont(
                AppFonts.TITLE
        );


        heading.setForeground(
                AppColors.TEXT
        );


        gbc.gridx = 0;

        gbc.gridy = 0;

        gbc.gridwidth = 2;


        mainPanel.add(
                heading,
                gbc
        );


        gbc.gridwidth = 1;

                // =========================
        // Title
        // =========================


        gbc.gridx = 0;

        gbc.gridy++;


        JLabel titleLabel =
                new JLabel(
                        "Title"
                );


        titleLabel.setForeground(
                AppColors.TEXT
        );


        mainPanel.add(
                titleLabel,
                gbc
        );



        titleField =
                new JTextField();



        gbc.gridx = 1;



        mainPanel.add(
                titleField,
                gbc
        );





        // =========================
        // Description
        // =========================


        gbc.gridx = 0;

        gbc.gridy++;


        JLabel descLabel =
                new JLabel(
                        "Description"
                );


        descLabel.setForeground(
                AppColors.TEXT
        );


        mainPanel.add(
                descLabel,
                gbc
        );



        descriptionArea =
                new JTextArea(
                        4,
                        15
                );


        descriptionArea.setLineWrap(
                true
        );


        descriptionArea.setWrapStyleWord(
                true
        );



        JScrollPane descriptionScroll =
                new JScrollPane(
                        descriptionArea
                );



        gbc.gridx = 1;



        mainPanel.add(
                descriptionScroll,
                gbc
        );





        // =========================
        // Priority
        // =========================


        gbc.gridx = 0;

        gbc.gridy++;



        JLabel priorityLabel =
                new JLabel(
                        "Priority"
                );


        priorityLabel.setForeground(
                AppColors.TEXT
        );


        mainPanel.add(
                priorityLabel,
                gbc
        );



        priorityBox =
                new JComboBox<>(
                        TaskPriority.values()
                );



        gbc.gridx = 1;



        mainPanel.add(
                priorityBox,
                gbc
        );






        // =========================
        // Category
        // =========================


        gbc.gridx = 0;

        gbc.gridy++;



        JLabel categoryLabel =
                new JLabel(
                        "Category"
                );


        categoryLabel.setForeground(
                AppColors.TEXT
        );


        mainPanel.add(
                categoryLabel,
                gbc
        );



        categoryBox =
                new JComboBox<>(
                        TaskCategory.values()
                );



        gbc.gridx = 1;



        mainPanel.add(
                categoryBox,
                gbc
        );

                // =========================
        // Due Date
        // =========================


        gbc.gridx = 0;

        gbc.gridy++;



        JLabel dateLabel =
                new JLabel(
                        "Due Date"
                );


        dateLabel.setForeground(
                AppColors.TEXT
        );


        mainPanel.add(
                dateLabel,
                gbc
        );



        dueDateField =
                new JTextField();


        dueDateField.setToolTipText(
                "Format: YYYY-MM-DD"
        );



        gbc.gridx = 1;



        mainPanel.add(
                dueDateField,
                gbc
        );





        // =========================
        // Buttons
        // =========================


        JPanel buttonPanel =
                new JPanel();



        buttonPanel.setOpaque(
                false
        );



        RoundedButton saveButton =
                new RoundedButton(
                        "Save Task"
                );



        RoundedButton cancelButton =
                new RoundedButton(
                        "Cancel"
                );



        buttonPanel.add(
                saveButton
        );


        buttonPanel.add(
                cancelButton
        );



        gbc.gridx = 0;

        gbc.gridy++;


        gbc.gridwidth = 2;



        mainPanel.add(
                buttonPanel,
                gbc
        );



        add(
                mainPanel
        );



        saveButton.addActionListener(
                e ->
                        saveTask()
        );



        cancelButton.addActionListener(
                e ->
                        dispose()
        );

    }





    /**
     * Create task and save.
     */
    private void saveTask(){


        try {


            LocalDate date =
                    LocalDate.parse(
                            dueDateField.getText()
                    );



            taskService.addTask(

                    titleField.getText(),

                    descriptionArea.getText(),

                    (TaskPriority)
                            priorityBox.getSelectedItem(),

                    (TaskCategory)
                            categoryBox.getSelectedItem(),

                    date

            );



            JOptionPane.showMessageDialog(
                    this,
                    "Task added successfully!"
            );



            dispose();



        }
        catch(DateTimeParseException e){


            JOptionPane.showMessageDialog(
                    this,
                    "Invalid date format. Use YYYY-MM-DD"
            );


        }
        catch(Exception e){


            JOptionPane.showMessageDialog(
                    this,
                    e.getMessage()
            );


        }

    }

        /**
     * Clear all input fields.
     */
    public void resetForm(){


        titleField.setText(
                ""
        );


        descriptionArea.setText(
                ""
        );


        dueDateField.setText(
                ""
        );


        priorityBox.setSelectedIndex(
                0
        );


        categoryBox.setSelectedIndex(
                0
        );


    }





    /**
     * Set default date value.
     */
    public void setDefaultDate(){


        dueDateField.setText(
                LocalDate.now()
                        .toString()
        );


    }


}