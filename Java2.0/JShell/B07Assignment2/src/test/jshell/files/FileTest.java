package test.jshell.files;

import jshell.files.File;
import static org.junit.Assert.assertEquals;
import org.junit.jupiter.api.Test;
/**
 * this class is used to test the {@link File}
 * test the mutate methods in the class.
 * @author lan tianfang
 *
 */
public class FileTest {
  @Test
  void test() {
    // make the test on returning content for the file.
    File file1 = new File("asdfsdff");
    assertEquals("asdfsdff",file1.getContent());
    // make test for empty string
    File file2 = new File("");
    assertEquals("",file2.getContent());
    
    // make test on several lines.
    File file3 = new File("sdfsdf\nfdsf\nfsdf\nggeij");
    assertEquals("sdfsdf\nfdsf\nfsdf\nggeij",file3.getContent());
    
    // make test on overWrite with simple example
    file1.overWrite("bb");
    assertEquals("bb",file1.getContent());
    
    // make test on overWrite with empty string
    file1.overWrite("");
    assertEquals("",file1.getContent());
    
    // make test on overWrite string with several lines.
    file1.overWrite("sdfsdf\nfdsf\nfsdf\nggeij");
    assertEquals("sdfsdf\nfdsf\nfsdf\nggeij",file1.getContent());
    
    // make test on append with simple string.
    file1.append("ab");
    assertEquals("sdfsdf\nfdsf\nfsdf\nggeijab",file1.getContent());
    
    // make test on append string with several lines
    file2.append("AB");
    file2.append("abc\ncba\nbba");
    assertEquals("ABabc\ncba\nbba",file2.getContent());
    
    // make test on append nothing
    file2.append("");
    assertEquals("ABabc\ncba\nbba",file2.getContent());
    // add to a empty file
    File file4 = new File();
    file4.append("ABC");
    assertEquals("ABC",file4.getContent());

  }

}
