package service;


import crypto.CryptoUtils;
// import exception.CryptoException;

import java.io.File;
import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.nio.charset.StandardCharsets;
import java.util.Base64;


public class FileEncryptionService {



    /*
        Encrypt file and save output
     */

    public static void encryptFile(
            File inputFile,
            File outputFile,
            String password
    )
            throws Exception {


        byte[] fileData =
                readFile(inputFile);



        String encodedData =
                Base64.getEncoder()
                        .encodeToString(fileData);



        String encrypted =
                CryptoUtils.encrypt(
                        encodedData,
                        password
                );



        writeFile(
                outputFile,
                encrypted.getBytes(
                        StandardCharsets.UTF_8
                )
        );

    }





    /*
        Decrypt file and restore original
     */

    public static void decryptFile(
            File encryptedFile,
            File outputFile,
            String password
    )
            throws Exception {



        byte[] encryptedBytes =
                readFile(encryptedFile);



        String encryptedText =
                new String(
                        encryptedBytes,
                        StandardCharsets.UTF_8
                );



        String decryptedBase64 =
                CryptoUtils.decrypt(
                        encryptedText,
                        password
                );



        byte[] originalData =
                Base64.getDecoder()
                        .decode(decryptedBase64);



        writeFile(
                outputFile,
                originalData
        );

    }





    /*
        Read file bytes
     */

    private static byte[] readFile(
            File file
    )
            throws Exception {


        FileInputStream fis =
                new FileInputStream(file);



        byte[] data =
                fis.readAllBytes();



        fis.close();


        return data;

    }





    /*
        Write bytes to file
     */

    private static void writeFile(
            File file,
            byte[] data
    )
            throws Exception {


        FileOutputStream fos =
                new FileOutputStream(file);



        fos.write(data);


        fos.close();

    }



}