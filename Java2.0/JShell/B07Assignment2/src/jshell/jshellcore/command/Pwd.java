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

import jshell.files.FileSystem;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/***
 * The class pwd is a command and will print the current working directory.
 * 
 * @author lan tianfang
 * @author XianghuDai
 *
 */
public class Pwd implements Command {
	
  /** output is the output object store output */
  private Output output = new Output();

  /**
   * the method excute will print the current directory
   * 
   * @param the input arg could be any string
   */
  @Override
  public void excute(String arg) {
	this.output.overwriteOutput();
    this.output.addOutputContent(FileSystem.getSystem().getCur());
    this.output.addOutputContent("\r");
  }

  /**
   * getDoc is suppose to get the documentation of the class
   */
  @Override
  public String getDoc() {
    return "Print the path of current working directory";
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
