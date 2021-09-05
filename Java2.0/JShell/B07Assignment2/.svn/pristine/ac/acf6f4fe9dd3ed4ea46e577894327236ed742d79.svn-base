//**********************************************************
//Assignment2:
//Student1: Tianfang Lan
//UTORID user_name:lantianf
//UT Student #: 1002687210
//Author: Tianfang Lan
//
//
//Honor Code: I pledge that this program represents my own
//program code and that I have coded on my own. I received
//help from no one in designing and debugging my program.
//I have also read the plagiarism section in the course info
//sheet of CSC B07 and understand the consequences.
//*********************************************************
package jshell.jshellcore.command;


import jshell.exceptions.NotExistException;
import jshell.files.File;
import jshell.files.FileSystem;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/***
 * the class Cat can read the file at the input path and display the content.
 * 
 * @author lan tianfang
 *
 */
public class Cat implements Command {
  /** output is the output object store output */
  private Output output = new Output();

  /**
   * the excute will print the file at the path if the file exist. Otherwise
   * it will print error message.
   *
   * @param arg is a formal path in string .
   */
  @Override
  public void excute(String arg) {
    // split the path
    String[] paths = arg.split("\\s+");
    this.output.overwriteOutput();
    this.output.overwriteerror();
    for (String path : paths) {
      // try to get the file at the path
      try {
        // test whether the path exist
        FileSystem.getSystem().exist(path);
        if (!FileSystem.getSystem().isFile(path)) {
          System.err.println("cat: " + path +": Is a invalid path");
        }
        else {
          // get the at path and store it in a object
          File file = FileSystem.getSystem().getFile(path);
          // get the content in the file
          String content = file.getContent();
          // store the content into output
          this.output.addOutputContent(content);
          this.output.addOutputContent("\r\r\r");
        }
      }
      // when it causes error
      catch (NotExistException e) {
        this.output.adderrorout("cat: " + e.getMessage());
        this.output.adderrorout("\r");
      }
    }
  }

  /**
   * getDoc is suppose to get the documentation of the class
   */
  @Override
  public String getDoc() {
    return "Display the content of the file at the input path";
  }

  /**
   * the class will return the object output.
   * 
   * @return object output contains the output of the class.
   */
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
