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
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/***
 * the Echo contains 3 ways to edit a file first, it will be able to append the
 * input string to the file at the path. Second, it will overwrite the file at
 * path with the input content. These two ways will both create a new empty
 * file if the path does not exist a file. The last way is when no
 * path is given, then the shell will print the input string.
 * 
 * @author lan tianfang
 * @author XianghuDai
 *
 */
public class Echo implements Command {
  /** output is the output object store output */
  private Output output = new Output();

  @Override
  public void excute(String arg) {
    this.output.overwriteerror();
    if(arg.equals("")) {
      System.err.println("echo: No arg given");
      return;
    }
    try {
      int sindex = arg.indexOf("\"");
      int lindex = arg.lastIndexOf("\"");
      if(sindex == -1 || lindex == -1 || sindex==lindex) {
        System.err.println("echo: Wrong quotation");
        return;
      }
      String quote = arg.substring(sindex+1, lindex);
      // save the output
      this.output.overwriteOutput();
      this.output.addOutputContent(quote);
      this.output.addOutputContent("\r");
    }
    // if the error occurs print the error message.
    catch (NotExistException e) {
      this.output.adderrorout("echo: " + e.getMessage());
      this.output.adderrorout("\r");
    }
  }

  /**
   * getDoc is suppose to get the documentation of the class
   */
  @Override
  public String getDoc() {
    return "the method will print the input if there if no path in put"
        + ", if > is given the method will create new file at path if"
        + "otherwise method will overwirte the file with content at path"
        + "if >> is given the method will append instead of overwrite.";
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
