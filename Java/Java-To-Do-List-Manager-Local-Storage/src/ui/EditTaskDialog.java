package ui;

import model.Task;
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


/**
 * Dialog used to edit existing tasks.
 */
public class EditTaskDialog extends JDialog {


    private TaskService taskService;


    private Task task;



    private JTextField titleField;


    private JTextArea descriptionArea;


    private JComboBox<TaskPriority> priorityBox;


    private JComboBox<TaskCategory> categoryBox;


    private JTextField dueDateField;





    /**
     * Constructor
     */
    public EditTaskDialog(
            JFrame parent,
            TaskService taskService,
            Task task
    ){


        super(
                parent,
                "Edit Task",
                true
        );



        this.taskService =
                taskService;


        this.task =
                task;



        initializeDialog();


        createUI();


        loadTaskData();

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
     * Create form UI.
     */
    private void createUI(){


        JPanel panel =
                new JPanel(
                        new GridBagLayout()
                );



        panel.setBackground(
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



        JLabel title =
                new JLabel(
                        "Update Task"
                );


        title.setFont(
                AppFonts.TITLE
        );


        title.setForeground(
                AppColors.TEXT
        );


        gbc.gridx = 0;

        gbc.gridy = 0;


        gbc.gridwidth = 2;



        panel.add(
                title,
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


        panel.add(
                titleLabel,
                gbc
        );



        titleField =
                new JTextField();



        gbc.gridx = 1;



        panel.add(
                titleField,
                gbc
        );






        // =========================
        // Description
        // =========================


        gbc.gridx = 0;

        gbc.gridy++;



        JLabel descriptionLabel =
                new JLabel(
                        "Description"
                );



        descriptionLabel.setForeground(
                AppColors.TEXT
        );


        panel.add(
                descriptionLabel,
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



        JScrollPane scroll =
                new JScrollPane(
                        descriptionArea
                );



        gbc.gridx = 1;



        panel.add(
                scroll,
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


        panel.add(
                priorityLabel,
                gbc
        );



        priorityBox =
                new JComboBox<>(
                        TaskPriority.values()
                );



        gbc.gridx = 1;



        panel.add(
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


        panel.add(
                categoryLabel,
                gbc
        );



        categoryBox =
                new JComboBox<>(
                        TaskCategory.values()
                );



        gbc.gridx = 1;



        panel.add(
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


        panel.add(
                dateLabel,
                gbc
        );



        dueDateField =
                new JTextField();



        gbc.gridx = 1;



        panel.add(
                dueDateField,
                gbc
        );






        // =========================
        // Buttons
        // =========================


        JPanel buttons =
                new JPanel();



        buttons.setOpaque(
                false
        );



        RoundedButton save =
                new RoundedButton(
                        "Update"
                );



        RoundedButton cancel =
                new RoundedButton(
                        "Cancel"
                );



        buttons.add(
                save
        );


        buttons.add(
                cancel
        );



        gbc.gridx = 0;

        gbc.gridy++;


        gbc.gridwidth = 2;



        panel.add(
                buttons,
                gbc
        );



        add(
                panel
        );



        save.addActionListener(
                e ->
                        updateTask()
        );



        cancel.addActionListener(
                e ->
                        dispose()
        );


    }





    /**
     * Load existing task information.
     */
    private void loadTaskData(){


        if(task == null){

            return;

        }



        titleField.setText(
                task.getTitle()
        );



        descriptionArea.setText(
                task.getDescription()
        );



        priorityBox.setSelectedItem(
                task.getPriority()
        );



        categoryBox.setSelectedItem(
                task.getCategory()
        );



        if(task.getDueDate()!=null){


            dueDateField.setText(
                    task.getDueDate()
                            .toString()
            );

        }

    }

        /**
     * Update task information.
     */
    private void updateTask(){


        try {


            LocalDate date =
                    LocalDate.parse(
                            dueDateField.getText()
                    );



            taskService.updateTask(

                    task.getTaskId(),

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
                    "Task updated successfully!"
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
     * Set task manually.
     */
    public void setTask(Task task){


        this.task =
                task;


        loadTaskData();

    }





    /**
     * Get current task.
     */
    public Task getTask(){


        return task;

    }


}