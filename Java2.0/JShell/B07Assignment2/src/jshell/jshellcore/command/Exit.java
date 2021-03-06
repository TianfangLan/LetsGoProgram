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

import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/***
 * the class Terminated the running program
 * 
 * @author Jiahong Wang
 * @return null
 */
public class Exit implements Command {

  /** output is the output object store output */
  private Output output = new Output();
  
  @Override
  public void excute(String input) {
    // TODO Auto-generated method stub
    //
    System.exit(0);
  }

  @Override
  public String getDoc() {
    // TODO Auto-generated method stub
    return "Command Exit to Quit the program";
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
  public String geterror() {
    // TODO Auto-generated method stub
    return null;
  }

}
