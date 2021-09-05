// **********************************************************
// Assignment2:
// Student3: Jiahong Wang
// UTORID user_name: wangj398
// UT Student #: 1002695933
// Author: Jiahong Wang
//
//
// Honor Code: I pledge that this program represents my own
// program code and that I have coded on my own. I received
// help from no one in designing and debugging my program.
// I have also read the plagiarism section in the course info
// sheet of CSC B07 and understand the consequences.
// *********************************************************
package jshell.jshellcore.command;

/***
 * the class will create a new directory
 * 
 * @author Jiahong Wang
 * @param the target directory
 */
import jshell.exceptions.NotExistException;
import jshell.files.FileSystem;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

public class Mkdir implements Command {


  /** output is the output object store output */
  private Output output = new Output();

  @Override
  public void excute(String input) {   
    if (input.equals("")) {
      this.output.overwriteerror();
      this.output.adderrorout("mkdir: No arg given");
      this.output.adderrorout("\r");
      return;
    }
    try {
      String[] args = input.split(" ");
      for (String arg : args) {
        if (FileSystem.getSystem().exist(arg)) {
          this.output.overwriteerror();
          this.output.adderrorout(arg + " already exists");
          this.output.adderrorout("\r");
        } else {
          FileSystem.getSystem().makeDir(arg);
        }
      }
    } catch (NotExistException e) {
      this.output.overwriteerror();
      this.output.adderrorout("mkdir: " + e.getMessage());
      this.output.adderrorout("\r");
    }


  }

  @Override
  public String getDoc() {
    return "Command mkdir <br> to create directories";
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
