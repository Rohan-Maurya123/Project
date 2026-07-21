package utility;

import java.io.*;
import java.util.ArrayList;
import java.util.List;

public class FileManager {

    private FileManager() {
    }

    public static void writeLines(String filePath, List<String> lines) {

        try (BufferedWriter writer = new BufferedWriter(new FileWriter(filePath))) {

            for (String line : lines) {
                writer.write(line);
                writer.newLine();
            }

        } catch (IOException e) {
            System.out.println("Error writing file: " + e.getMessage());
        }
    }

    public static List<String> readLines(String filePath) {

        List<String> lines = new ArrayList<>();

        File file = new File(filePath);

        if (!file.exists()) {
            return lines;
        }

        try (BufferedReader reader = new BufferedReader(new FileReader(file))) {

            String line;

            while ((line = reader.readLine()) != null) {
                lines.add(line);
            }

        } catch (IOException e) {
            System.out.println("Error reading file: " + e.getMessage());
        }

        return lines;
    }

}