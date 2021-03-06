// **********************************************************
// Assignment2:
// Student1: Tianfang Lan
// UTORID user_name:lantianf
// UT Student #: 1002687210
// Author: Tianfang Lan
//
//
// Honor Code: I pledge that this program represents my own
// program code and that I have coded on my own. I received
// help from no one in designing and debugging my program.
// I have also read the plagiarism section in the course info
// sheet of CSC B07 and understand the consequences.
// *********************************************************
package jshell.jshellcore.command;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import jshell.files.File;
import jshell.files.FileSystem;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/***
 * The class Get will get the Retrieve the file at the URL and add it to
 * the current working
 * directory.
 * 
 * @author lan tianfang
 *
 */
public class Get implements Command {
  /** output is the output object store output */
  private Output output = new Output();

  @Override
  public void excute(String input) {
    this.output.overwriteerror();
    try {
      // get the name of the file
      String[] dir = input.split("/");
      // get the length of the dir
      int length = dir.length;
      // get the name
      String name = dir[length - 1];
      if(name.contains(".")) {
        name = name.substring(0, name.indexOf("."));
      }
      // create the target URL
      URL url = new URL(input);
      // connect to the url
      HttpURLConnection urlConnection =
          (HttpURLConnection) url.openConnection();
      InputStreamReader read =
          new InputStreamReader(urlConnection.getInputStream());
      BufferedReader reader = new BufferedReader(read);
      // for saving the lines of the every line of the file
      String line;
      line = reader.readLine();
      // create a String for saving the whole content
      String content;
      // set a buffer for the whole content;
      StringBuffer buffer = new StringBuffer();
      while (line != null) {
        // append the line
        buffer.append(line);
        // append to another line
        buffer.append("\n");
        // read the next line
        line = reader.readLine();
      }
      // save the content
      content = buffer.toString();
      content = content.substring(0, content.length() - 1);
      if (FileSystem.getSystem().exist(name)) {
        // get the file
        File file = FileSystem.getSystem().getFile(name);
        file.overWrite(content);
      } else {
        FileSystem.getSystem().makeFile(name);
        FileSystem.getSystem().getFile(name).overWrite(content);
      }

    } catch (IOException e) {
      this.output.adderrorout(e.getMessage());
      this.output.adderrorout("\r");
    }

  }

  @Override
  public String getDoc() {
    return "the command will get the file from url and store"
        + "it at current working directory";
  }

  @Override
  public String getOutput() {
    return output.getOutput();
  }

  /**
   * the class will return the object error.
   * 
   * @return object error contains the error of the class.
   */
  @Override
  public String geterror() {
    // TODO Auto-generated method stub
    return output.geterror();
  }
}
