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

import java.util.EmptyStackException;
import jshell.files.FileSystem;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;


/***
 * the class will remove the top entry from the directory stack, and use
 * command cd get into the top of the stack.
 * 
 * @author lan tianfang
 *
 */
public class Popd implements Command {
	
  /** output is the output object store output */
  private Output output = new Output();

  /**
   * the method excute will remove the top entry from the directory
   * strack and get into the directory.
   */
  @Override
  public void excute(String input) {
    // if the directory is not empty.
    try {
      FileSystem.getSystem().pop();
    }
    // throw the error if the direcotry is empty.
    catch (EmptyStackException e) {
      this.output.overwriteerror();
      this.output.adderrorout("popd: empty directory stack");
      this.output.adderrorout("\r");
    }
  }

  /**
   * getDoc is suppose to get the documentation of the class
   */
  @Override
  public String getDoc() {
    // TODO Auto-generated method stub
    return "Remove the top entry from the directory stack, and"
        + "cd into it.";
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
