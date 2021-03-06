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
package jshell.jshellcore;

/***
 * the class will set the command status of the input command
 * 
 * @author Jiahong Wang
 * @return the command status
 */
public class CommandStatus {
  private String commandStauts;

  public CommandStatus(String command) {

  }
  /**
   * set the commandStatus to be good if it excutes without error
   */
  public void SetGoodStatus() {
    this.commandStauts = "Good";
  }
  /**
   * set the commandStatus to be bad if the error occurs
   */
  public void SetBadStatus() {
    this.commandStauts = "Bad";
  }

  public String GetCommandStatus() {
    return this.commandStauts;
  }
}
