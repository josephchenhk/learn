import com.opencsv.CSVReader;
import com.opencsv.exceptions.CsvException;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import java.util.Arrays;
import java.util.List;

public class DataReader {

    public List<String[]> r;

    public DataReader(String fileName) throws IOException, CsvException {
        try (CSVReader reader = new CSVReader(new FileReader(fileName))) {
            r = reader.readAll();
//            r.forEach(x -> System.out.println(Arrays.toString(x)));
        }
    }
}
