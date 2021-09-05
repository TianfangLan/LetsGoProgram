// **********************************************************
// Assignment2:
// Student1: Junxing Xu
// UTORID user_name:xujunxin
// UT Student #: 1004019028
// Author: Junxing Xu
//
//
// Honor Code: I pledge that this program represents my own
// program code and that I have coded on my own. I received
// help from no one in designing and debugging my program.
// I have also read the plagiarism section in the course info
// sheet of CSC B07 and understand the consequences.
// *********************************************************
package jshell.jshellcore.command;

import jshell.exceptions.InvalidArgException;
import jshell.exceptions.NotExistException;
import jshell.files.FileSystem;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/**
 * 
 * Copying from one path to another, without removing the original content
 * @author danielxu
 *
 */
public class Cp implements Command{
  /** output is the output object store output */
  private Output output = new Output();

  @Override
  public void excute(String input) {
    this.output.overwriteerror();
    try {
      String[] s = input.split("\\s+");
      FileSystem.getSystem().copy(s[0], s[1]);
    }
    catch(InvalidArgException e) {
      this.output.adderrorout("cp: " + e.getMessage());
      this.output.adderrorout("\r");
    }
    catch(NotExistException e) {
      this.output.adderrorout("cp: " + e.getMessage());
      this.output.adderrorout("\r");
    }
  }

  @Override
  public String getDoc() {
    return "Copy contents from OLDPATH to NEWPATH";
  }

  @Override
  public String getOutput() {
    return this.output.getOutput();
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
