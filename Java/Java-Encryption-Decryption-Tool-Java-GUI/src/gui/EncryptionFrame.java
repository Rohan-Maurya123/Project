package gui;


import crypto.CryptoUtils;
import service.FileEncryptionService;
import utility.InputValidator;


import javax.swing.*;
import java.awt.*;
import java.awt.datatransfer.StringSelection;
import java.io.File;



public class EncryptionFrame extends JFrame {



    private JTextArea inputArea;
    private JTextArea outputArea;

    private JPasswordField passwordField;

    private JLabel statusLabel;


    private File selectedFile;




    public EncryptionFrame(){


        setTitle(
                "AES Encryption Decryption Tool"
        );


        setSize(
                900,
                600
        );


        setDefaultCloseOperation(
                JFrame.EXIT_ON_CLOSE
        );


        setLocationRelativeTo(null);



        createGUI();


    }





    private void createGUI(){


        setLayout(
                new BorderLayout(10,10)
        );



        // TEXT AREAS

        inputArea =
                new JTextArea();


        outputArea =
                new JTextArea();



        inputArea.setBorder(
                BorderFactory
                .createTitledBorder(
                        "Input Text"
                )
        );


        outputArea.setBorder(
                BorderFactory
                .createTitledBorder(
                        "Output Text"
                )
        );



        JPanel textPanel =
                new JPanel(
                        new GridLayout(1,2,10,10)
                );



        textPanel.add(
                new JScrollPane(inputArea)
        );


        textPanel.add(
                new JScrollPane(outputArea)
        );



        add(
                textPanel,
                BorderLayout.CENTER
        );





        // PASSWORD PANEL


        JPanel topPanel =
                new JPanel();



        topPanel.add(
                new JLabel("Password:")
        );


        passwordField =
                new JPasswordField(20);


        topPanel.add(
                passwordField
        );



        add(
                topPanel,
                BorderLayout.NORTH
        );






        // BUTTON PANEL


        JPanel buttonPanel =
                new JPanel();



        JButton encryptButton =
                new JButton("Encrypt");



        JButton decryptButton =
                new JButton("Decrypt");



        JButton copyButton =
                new JButton("Copy Output");



        JButton clearButton =
                new JButton("Clear");



        JButton selectFileButton =
                new JButton("Select File");



        JButton encryptFileButton =
                new JButton("Encrypt File");



        JButton decryptFileButton =
                new JButton("Decrypt File");





        buttonPanel.add(encryptButton);

        buttonPanel.add(decryptButton);

        buttonPanel.add(copyButton);

        buttonPanel.add(clearButton);

        buttonPanel.add(selectFileButton);

        buttonPanel.add(encryptFileButton);

        buttonPanel.add(decryptFileButton);



        add(
                buttonPanel,
                BorderLayout.SOUTH
        );






        statusLabel =
                new JLabel(
                        "Ready"
                );


        add(
                statusLabel,
                BorderLayout.WEST
        );






        // EVENTS



        encryptButton.addActionListener(e -> encryptText());



        decryptButton.addActionListener(e -> decryptText());



        copyButton.addActionListener(e -> copyOutput());



        clearButton.addActionListener(e -> clearAll());



        selectFileButton.addActionListener(
                e -> selectFile()
        );



        encryptFileButton.addActionListener(
                e -> encryptSelectedFile()
        );


        decryptFileButton.addActionListener(
                e -> decryptSelectedFile()
        );


    }






    private String getPassword(){


        return new String(
                passwordField.getPassword()
        );

    }





    private void encryptText(){


        try{


            String text =
                    inputArea.getText();



            String password =
                    getPassword();



            if(!InputValidator.validateText(text)){

                throw new Exception(
                        InputValidator.textErrorMessage()
                );

            }



            if(!InputValidator.validatePassword(password)){


                throw new Exception(
                        InputValidator.passwordErrorMessage()
                );

            }



            String encrypted =
                    CryptoUtils.encrypt(
                            text,
                            password
                    );



            outputArea.setText(
                    encrypted
            );


            statusLabel.setText(
                    "Encryption Successful"
            );



        }
        catch(Exception ex){

            statusLabel.setText(
                    ex.getMessage()
            );

        }


    }







    private void decryptText(){


        try{


            String encrypted =
                    inputArea.getText();



            String password =
                    getPassword();



            String decrypted =
                    CryptoUtils.decrypt(
                            encrypted,
                            password
                    );



            outputArea.setText(
                    decrypted
            );



            statusLabel.setText(
                    "Decryption Successful"
            );


        }
        catch(Exception ex){


            statusLabel.setText(
                    "Decryption Failed"
            );


        }


    }







    private void copyOutput(){


        StringSelection selection =
                new StringSelection(
                        outputArea.getText()
                );


        Toolkit.getDefaultToolkit()
                .getSystemClipboard()
                .setContents(
                        selection,
                        null
                );


        statusLabel.setText(
                "Copied"
        );


    }







    private void clearAll(){


        inputArea.setText("");

        outputArea.setText("");

        passwordField.setText("");

        statusLabel.setText(
                "Cleared"
        );


    }







    private void selectFile(){


        JFileChooser chooser =
                new JFileChooser();



        int result =
                chooser.showOpenDialog(this);



        if(result ==
                JFileChooser.APPROVE_OPTION){


            selectedFile =
                    chooser.getSelectedFile();



            statusLabel.setText(
                    selectedFile.getName()
            );

        }

    }







    private void encryptSelectedFile(){


    try {


        if(selectedFile == null){

            statusLabel.setText(
                    "Please select a file first"
            );

            return;
        }



        String password =
                getPassword();



        if(!InputValidator.validatePassword(password)){


            statusLabel.setText(
                    InputValidator.passwordErrorMessage()
            );


            return;
        }




        File outputFile =
                new File(
                "encrypted_files/"
                + selectedFile.getName()
                + ".enc"
                );



        FileEncryptionService.encryptFile(
                selectedFile,
                outputFile,
                password
        );



        statusLabel.setText(
                "File encrypted successfully"
        );



        JOptionPane.showMessageDialog(
                this,
                "Encrypted file saved:\n"
                +
                outputFile.getAbsolutePath()
        );



    }

    catch(Exception e){


        statusLabel.setText(
                "File encryption failed"
        );


        JOptionPane.showMessageDialog(
                this,
                e.getMessage()
        );


    }


}







    private void decryptSelectedFile(){


    try{


        if(selectedFile == null){


            statusLabel.setText(
                    "Please select encrypted file"
            );


            return;

        }



        String password =
                getPassword();



        File outputFile =
                new File(
                "decrypted_files/restored_"
                +
                selectedFile.getName()
                .replace(".enc","")
                );



        FileEncryptionService.decryptFile(
                selectedFile,
                outputFile,
                password
        );

        System.out.println(outputFile.getAbsolutePath());
System.out.println(outputFile.exists());


        statusLabel.setText(
                "File decrypted successfully"
        );



        JOptionPane.showMessageDialog(
                this,
                "Restored file saved:\n"
                +
                outputFile.getAbsolutePath()
        );



    }

    catch(Exception e){


        statusLabel.setText(
                "File decryption failed"
        );


        JOptionPane.showMessageDialog(
                this,
                "Wrong password or corrupted file"
        );


    }


}



}