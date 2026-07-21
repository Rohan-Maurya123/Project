package repository;


import model.Task;

import java.io.*;
import java.util.ArrayList;
import java.util.List;



public class FileTaskRepository {



    private final String storagePath =
            "data/tasks.dat";




    public FileTaskRepository(){


        createStorageLocation();


    }






    private void createStorageLocation(){


        try{


            File folder =
                    new File(
                            "data"
                    );


            if(!folder.exists()){


                folder.mkdirs();


            }


        }
        catch(Exception e){


            System.out.println(
                    "Unable to create data folder."
            );


        }

    }






    public void saveTasks(
            List<Task> tasks
    ){


        try(
                ObjectOutputStream output =
                        new ObjectOutputStream(
                                new FileOutputStream(
                                        storagePath
                                )
                        )
        ){


            output.writeObject(
                    tasks
            );


        }
        catch(IOException e){


            System.out.println(
                    "Error saving tasks: "
                            +
                            e.getMessage()
            );


        }


    }

    @SuppressWarnings("unchecked")
    public List<Task> loadTasks(){


        File file =
                new File(
                        storagePath
                );



        if(!file.exists()){


            return new ArrayList<>();


        }



        try(
                ObjectInputStream input =
                        new ObjectInputStream(
                                new FileInputStream(
                                        file
                                )
                        )
        ){



            Object data =
                    input.readObject();



            return (List<Task>) data;



        }
        catch(
                IOException |
                ClassNotFoundException e
        ){



            System.out.println(
                    "Storage file corrupted."
            );



            backupCorruptedFile();



            return new ArrayList<>();


        }


    }






    private void backupCorruptedFile(){


        try{


            File oldFile =
                    new File(
                            storagePath
                    );



            if(oldFile.exists()){


                File backup =
                        new File(
                                "data/tasks_backup.dat"
                        );



                oldFile.renameTo(
                        backup
                );


            }



        }
        catch(Exception e){


            System.out.println(
                    "Backup failed."
            );


        }


    }






    public boolean storageExists(){


        File file =
                new File(
                        storagePath
                );


        return file.exists();


    }






    public String getStoragePath(){


        return storagePath;


    }

    public void clearStorage(){


        File file =
                new File(
                        storagePath
                );



        if(file.exists()){


            file.delete();


        }


    }





    public int getSavedTaskCount(){


        List<Task> tasks =
                loadTasks();



        return tasks.size();


    }






    public void printStorageInfo(){


        System.out.println(
                "Storage Location : "
                        +
                        storagePath
        );


        System.out.println(
                "Saved Tasks : "
                        +
                        getSavedTaskCount()
        );


    }


}