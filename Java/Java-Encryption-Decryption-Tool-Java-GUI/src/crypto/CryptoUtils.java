package crypto;


import exception.CryptoException;

import javax.crypto.*;
import javax.crypto.spec.GCMParameterSpec;
import javax.crypto.spec.PBEKeySpec;
import javax.crypto.spec.SecretKeySpec;

import java.nio.charset.StandardCharsets;
import java.security.SecureRandom;
import java.security.spec.KeySpec;
import java.util.Arrays;
import java.util.Base64;



public class CryptoUtils {


    private static final String AES = "AES";

    private static final String PBKDF2 =
            "PBKDF2WithHmacSHA256";


    private static final int KEY_LENGTH = 256;

    private static final int ITERATIONS = 65536;


    private static final int SALT_LENGTH = 16;

    private static final int IV_LENGTH = 12;


    private static final int TAG_LENGTH = 128;



    // Generate random bytes
    private static byte[] generateRandomBytes(int length){

        byte[] bytes = new byte[length];

        SecureRandom random = new SecureRandom();

        random.nextBytes(bytes);

        return bytes;
    }



    // Create AES key from password
    private static SecretKey generateKey(
            String password,
            byte[] salt
    ) throws Exception {


        KeySpec spec =
                new PBEKeySpec(
                        password.toCharArray(),
                        salt,
                        ITERATIONS,
                        KEY_LENGTH
                );


        SecretKeyFactory factory =
                SecretKeyFactory.getInstance(PBKDF2);


        byte[] key =
                factory.generateSecret(spec)
                        .getEncoded();


        return new SecretKeySpec(key,AES);

    }



    // Encrypt Text

    public static String encrypt(
            String plainText,
            String password
    )
            throws CryptoException {


        try {


            byte[] salt =
                    generateRandomBytes(SALT_LENGTH);


            SecretKey key =
                    generateKey(password,salt);



            byte[] iv =
                    generateRandomBytes(IV_LENGTH);



            Cipher cipher =
                    Cipher.getInstance(
                            "AES/GCM/NoPadding"
                    );



            GCMParameterSpec spec =
                    new GCMParameterSpec(
                            TAG_LENGTH,
                            iv
                    );


            cipher.init(
                    Cipher.ENCRYPT_MODE,
                    key,
                    spec
            );



            byte[] encrypted =
                    cipher.doFinal(
                            plainText.getBytes(
                                    StandardCharsets.UTF_8
                            )
                    );



            byte[] output =
                    new byte[
                            salt.length
                            +
                            iv.length
                            +
                            encrypted.length
                    ];



            System.arraycopy(
                    salt,
                    0,
                    output,
                    0,
                    salt.length
            );


            System.arraycopy(
                    iv,
                    0,
                    output,
                    salt.length,
                    iv.length
            );


            System.arraycopy(
                    encrypted,
                    0,
                    output,
                    salt.length+iv.length,
                    encrypted.length
            );



            return Base64
                    .getEncoder()
                    .encodeToString(output);



        }
        catch(Exception e){

            throw new CryptoException(
                    "Encryption failed",
                    e
            );

        }

    }






    // Decrypt Text


    public static String decrypt(
            String encryptedText,
            String password
    )
            throws CryptoException {


        try{


            byte[] data =
                    Base64
                    .getDecoder()
                    .decode(encryptedText);



            byte[] salt =
                    Arrays.copyOfRange(
                            data,
                            0,
                            SALT_LENGTH
                    );



            byte[] iv =
                    Arrays.copyOfRange(
                            data,
                            SALT_LENGTH,
                            SALT_LENGTH+IV_LENGTH
                    );



            byte[] encrypted =
                    Arrays.copyOfRange(
                            data,
                            SALT_LENGTH+IV_LENGTH,
                            data.length
                    );



            SecretKey key =
                    generateKey(
                            password,
                            salt
                    );



            Cipher cipher =
                    Cipher.getInstance(
                            "AES/GCM/NoPadding"
                    );


            GCMParameterSpec spec =
                    new GCMParameterSpec(
                            TAG_LENGTH,
                            iv
                    );


            cipher.init(
                    Cipher.DECRYPT_MODE,
                    key,
                    spec
            );



            byte[] decrypted =
                    cipher.doFinal(encrypted);



            return new String(
                    decrypted,
                    StandardCharsets.UTF_8
            );


        }
        catch(Exception e){

            throw new CryptoException(
                    "Decryption failed. Wrong password or corrupted data.",
                    e
            );

        }


    }


}