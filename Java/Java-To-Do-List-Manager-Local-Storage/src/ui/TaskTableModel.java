package ui;


import model.Task;

import javax.swing.table.AbstractTableModel;
import java.util.ArrayList;
import java.util.List;



/**
 * Table model for displaying tasks.
 */
public class TaskTableModel extends AbstractTableModel {



    private List<Task> tasks;



    private final String[] columns = {


            "ID",

            "Title",

            "Priority",

            "Category",

            "Status",

            "Due Date"


    };





    /**
     * Constructor.
     */
    public TaskTableModel(
            List<Task> tasks
    ){


        this.tasks =
                new ArrayList<>(
                        tasks
                );


    }





    /**
     * Update table data.
     */
    public void setTasks(
            List<Task> tasks
    ){


        this.tasks =
                new ArrayList<>(
                        tasks
                );



        fireTableDataChanged();


    }





    /**
     * Get task object by row.
     */
    public Task getTaskAt(
            int row
    ){


        if(
                row < 0 ||
                row >= tasks.size()
        ){


            return null;


        }



        return tasks.get(
                row
        );


    }





    @Override
    public int getRowCount(){


        return tasks.size();


    }





    @Override
    public int getColumnCount(){


        return columns.length;


    }





    @Override
    public String getColumnName(
            int column
    ){


        return columns[column];


    }

        @Override
    public Object getValueAt(
            int rowIndex,
            int columnIndex
    ){



        Task task =
                tasks.get(
                        rowIndex
                );



        switch(columnIndex){



            case 0:

                return task.getTaskId();



            case 1:

                return task.getTitle();



            case 2:

                return task.getPriority();



            case 3:

                return task.getCategory();



            case 4:

                return task.getStatus();



            case 5:

                return task.getDueDate();



            default:

                return "";

        }


    }





    /**
     * Check if table has data.
     */
    public boolean isEmpty(){


        return tasks.isEmpty();


    }





    /**
     * Get total rows.
     */
    public int size(){


        return tasks.size();


    }



}