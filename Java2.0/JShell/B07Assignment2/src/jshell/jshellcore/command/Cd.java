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

import jshell.exceptions.InvalidArgException;
import jshell.exceptions.NotExistException;
import jshell.files.FileSystem;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/***
 * the class will change the current working directory
 * 
 * @author Jiahong Wang
 * @param the target directory
 */

public class Cd implements Command {
	
  /** output is the output object store output */
  private Output output = new Output();

  @Override
  public void excute(String input) {
    this.output.overwriteerror();
    try {
      FileSystem.getSystem().change(input);
    } catch (NotExistException e) {
      this.output.adderrorout("cd: " + e.getMessage());
      this.output.adderrorout("\r");
    } catch (InvalidArgException e) {
      this.output.adderrorout("cd: "+e.getMessage());
      this.output.adderrorout("\r");
    }
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

  @Override
  public String getDoc() {
    return "Command cd <dir> to change the current working directory to <dir>";
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
