package ui;

import exception.InvalidTaskException;
import model.Task;
import model.TaskStatus;
import service.TaskService;
import theme.AppColors;
import theme.AppFonts;
import theme.RoundedButton;
import theme.UIConstants;

import javax.swing.*;
import javax.swing.table.DefaultTableCellRenderer;
import java.awt.*;
import java.util.List;


public class TaskManagementPanel extends JPanel {


    private TaskService taskService;



    private JTable taskTable;


    private TaskTableModel tableModel;



    private JTextField searchField;




    /**
     * Constructor
     */
    public TaskManagementPanel(
            TaskService taskService
    ){


        this.taskService =
                taskService;



        initializePanel();


        createUI();


    }





    /**
     * Panel configuration.
     */
    private void initializePanel(){


        setLayout(
                new BorderLayout()
        );



        setBackground(
                AppColors.BACKGROUND
        );



        setBorder(
                BorderFactory
                        .createEmptyBorder(
                                20,
                                20,
                                20,
                                20
                        )
        );


    }





    /**
     * Create complete UI.
     */
    private void createUI(){


        add(
                createTopPanel(),
                BorderLayout.NORTH
        );


        add(
                createTable(),
                BorderLayout.CENTER
        );


        add(
                createButtonPanel(),
                BorderLayout.SOUTH
        );


        loadTasks();

    }

        /**
     * Creates top toolbar.
     */
    private JPanel createTopPanel(){


        JPanel panel =
                new JPanel();



        panel.setOpaque(
                false
        );



        panel.setLayout(
                new BorderLayout()
        );



        JLabel title =
                new JLabel(
                        "Task Management"
                );



        title.setFont(
                AppFonts.TITLE
        );


        title.setForeground(
                AppColors.TEXT
        );



        panel.add(
                title,
                BorderLayout.WEST
        );





        JPanel searchPanel =
                new JPanel(
                        new FlowLayout(
                                FlowLayout.RIGHT
                        )
                );



        searchPanel.setOpaque(
                false
        );



        searchField =
                new JTextField(
                        20
                );



        searchField.setToolTipText(
                "Search task by title"
        );



        RoundedButton searchButton =
                new RoundedButton(
                        "Search"
                );



        searchPanel.add(
                searchField
        );



        searchPanel.add(
                searchButton
        );



        searchButton.addActionListener(
                e ->
                        searchTasks()
        );



        panel.add(
                searchPanel,
                BorderLayout.EAST
        );



        return panel;

    }





    /**
     * Creates task JTable.
     */
    private JScrollPane createTable(){


        tableModel =
                new TaskTableModel(
                        taskService
                                .getAllTasks()
                );



        taskTable =
                new JTable(
                        tableModel
                );



        taskTable.setRowHeight(
                UIConstants.TABLE_ROW_HEIGHT
        );



        taskTable.setFont(
                AppFonts.TABLE
        );



        taskTable.setBackground(
                AppColors.TABLE_ROW
        );



        taskTable.setForeground(
                AppColors.TEXT
        );



        taskTable
                .getTableHeader()
                .setBackground(
                        AppColors.TABLE_HEADER
                );



        taskTable
                .getTableHeader()
                .setForeground(
                        AppColors.TEXT
                );



        taskTable
                .getTableHeader()
                .setFont(
                        AppFonts.BUTTON
                );



        taskTable.setSelectionBackground(
                AppColors.TABLE_SELECTION
        );



        taskTable.setSelectionForeground(
                AppColors.TEXT
        );



        // Center align columns

        DefaultTableCellRenderer renderer =
                new DefaultTableCellRenderer();



        renderer.setHorizontalAlignment(
                SwingConstants.CENTER
        );



        for(int i = 0;
            i < taskTable.getColumnCount();
            i++){


            taskTable
                    .getColumnModel()
                    .getColumn(i)
                    .setCellRenderer(
                            renderer
                    );

        }



        return new JScrollPane(
                taskTable
        );

    }

        /**
     * Creates bottom action buttons.
     */
    private JPanel createButtonPanel(){


        JPanel panel =
                new JPanel();



        panel.setOpaque(
                false
        );



        panel.setLayout(
                new FlowLayout(
                        FlowLayout.CENTER,
                        15,
                        15
                )
        );



        RoundedButton addButton =
                new RoundedButton(
                        "Add Task"
                );



        RoundedButton editButton =
                new RoundedButton(
                        "Edit Task"
                );



        RoundedButton deleteButton =
                new RoundedButton(
                        "Delete Task"
                );



        RoundedButton completeButton =
                new RoundedButton(
                        "Complete"
                );



        RoundedButton refreshButton =
                new RoundedButton(
                        "Refresh"
                );





        panel.add(
                addButton
        );


        panel.add(
                editButton
        );


        panel.add(
                deleteButton
        );


        panel.add(
                completeButton
        );


        panel.add(
                refreshButton
        );





        addButton.addActionListener(
                e ->
                        openAddDialog()
        );



        editButton.addActionListener(
                e ->
                        openEditDialog()
        );



        deleteButton.addActionListener(
                e ->
                        deleteSelectedTask()
        );



        completeButton.addActionListener(
                e ->
                        completeSelectedTask()
        );



        refreshButton.addActionListener(
                e ->
                        loadTasks()
        );



        return panel;

    }





    /**
     * Load tasks into table.
     */
    public void loadTasks(){


        if(tableModel == null){

            return;

        }



        tableModel.setTasks(
                taskService
                        .getAllTasks()
        );

    }





    /**
     * Search tasks.
     */
    private void searchTasks(){


        String keyword =
                searchField
                        .getText();



        List<Task> result =
                taskService
                        .search(
                                keyword
                        );



        tableModel.setTasks(
                result
        );


    }
        /**
     * Open add task dialog.
     */
    private void openAddDialog(){


        AddTaskDialog dialog =
                new AddTaskDialog(
                        (JFrame)
                                SwingUtilities
                                        .getWindowAncestor(
                                                this
                                        ),

                        taskService
                );



        dialog.setVisible(
                true
        );



        loadTasks();

    }





    /**
     * Open edit task dialog.
     */
    private void openEditDialog(){


        int row =
                taskTable
                        .getSelectedRow();



        if(row == -1){


            JOptionPane.showMessageDialog(
                    this,
                    "Please select a task first."
            );


            return;

        }



        Task task =
                tableModel
                        .getTaskAt(
                                row
                        );



        EditTaskDialog dialog =
                new EditTaskDialog(
                        (JFrame)
                                SwingUtilities
                                        .getWindowAncestor(
                                                this
                                        ),

                        taskService,

                        task
                );



        dialog.setVisible(
                true
        );



        loadTasks();

    }





    /**
     * Delete selected task.
     */
    private void deleteSelectedTask(){


        int row =
                taskTable
                        .getSelectedRow();



        if(row == -1){


            JOptionPane.showMessageDialog(
                    this,
                    "Select a task first."
            );


            return;

        }



        Task task =
                tableModel
                        .getTaskAt(
                                row
                        );



        int choice =
                JOptionPane.showConfirmDialog(
                        this,
                        "Delete selected task?",
                        "Confirm Delete",
                        JOptionPane.YES_NO_OPTION
                );



        if(choice ==
                JOptionPane.YES_OPTION){

            try {
                taskService.deleteTask(
                        task.getTaskId()
                );
            } catch (InvalidTaskException e) {
                JOptionPane.showMessageDialog(
                        this,
                        "Error deleting task: " + e.getMessage()
                );
            }



            loadTasks();

        }

    }





    /**
     * Mark selected task completed.
     */
    private void completeSelectedTask(){


        int row =
                taskTable
                        .getSelectedRow();



        if(row == -1){


            JOptionPane.showMessageDialog(
                    this,
                    "Select a task first."
            );


            return;

        }



        Task task =
                tableModel
                        .getTaskAt(
                                row
                        );

        try {
            taskService
                    .markCompleted(
                            task.getTaskId()
                    );
        } catch (InvalidTaskException e) {
            JOptionPane.showMessageDialog(
                    this,
                    "Error completing task: " + e.getMessage()
            );
        }



        loadTasks();

    }
        /**
     * Refresh table data.
     */
    public void refresh(){


        loadTasks();


    }





    /**
     * Get current selected task.
     */
    public Task getSelectedTask(){


        int row =
                taskTable
                        .getSelectedRow();



        if(row == -1){

            return null;

        }



        return tableModel
                .getTaskAt(
                        row
                );

    }





    /**
     * Get table reference.
     */
    public JTable getTaskTable(){


        return taskTable;


    }


}
