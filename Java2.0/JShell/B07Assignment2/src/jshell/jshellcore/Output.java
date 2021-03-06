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
 * the class will store the output message of 
 * every command Output would be printed or be used to
 * redirect
 * 
 * @author Jiahong Wang
 * @author XianghuDai
 * 
 */
public class Output {

  private String outputcontent;
  private String erroroutput;

  /***
   * the constructor set default output as empty string
   */

  public Output() {
    this.outputcontent = "";
    this.erroroutput = "";
  }

  /***
   * addOutputContent() allows every command 
   * to add String into their output and then save them
   * 
   * @param content is the contents that needs to be add into the output
   */
  public void addOutputContent(String content) {
    this.outputcontent += content;
  }

  public void adderrorout(String content) {
    this.erroroutput += content;
  }

  /**
   * this method allows every command to renew the Output and the error
   */
  public void overwriteOutput() {
    this.outputcontent = "";
  }

  public void overwriteerror() {
    this.erroroutput = "";
  }

  /**
   * this method allows commands that need to 
   * recursively append output to delete the last empty
   * line
   */
  public void deleteLastEmptyLine() {
    outputcontent = outputcontent.substring(0, outputcontent.length() - 1);
  }

  /***
   * this method allows classes in jshellcore to get the output of each command
   * 
   * @return the output of each command
   */
  public String getOutput() {
    return this.outputcontent;
  }

  /***
   * this method allows classes in jshellcore to get the error of each command
   * 
   * @return the error of each command
   */
  public String geterror() {
    return this.erroroutput;
  }
}
