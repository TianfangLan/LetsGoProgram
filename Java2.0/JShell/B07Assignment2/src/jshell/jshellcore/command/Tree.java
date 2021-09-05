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

import jshell.files.FileSystem;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/**
 * Display the tree view of the whole file system
 * @author danielxu
 * @author XianghuDai
 *
 */
public class Tree implements Command{

  /** output is the output object store output */
  private Output output = new Output();
  
  @Override
  public void excute(String input) {
	this.output.overwriteOutput();
    this.output.addOutputContent(FileSystem.getSystem().tree());
    this.output.addOutputContent("\r");
  }

  @Override
  public String getDoc() {
    return "Display the tree view of the whole file system";
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
