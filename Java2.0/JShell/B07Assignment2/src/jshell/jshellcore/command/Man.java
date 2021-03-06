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

import jshell.jshellcore.Command;
import jshell.jshellcore.Mapper;
import jshell.jshellcore.Output;

/***
 * the class will return the documentation of the input
 * 
 * @author lan tianfang
 * @author XianghuDai
 *
 */
public class Man implements Command {
	
  /** output is the output object store output */
  private Output output = new Output();

  /**
   * the method excut will return the documenatation if the input is a formal
   * commmand, otherwise it will thorw a error.
   * 
   * @param command is a name of the command in the form of string
   */
  @Override
  public void excute(String command) {
    // if the input commmand is a formal command
    if (Mapper.getMapper().isExist(command)) {
      this.output.overwriteOutput();
      this.output.addOutputContent(Mapper.getMapper().
    		  getCommand(command).getDoc());
    }
    // if the input is not a commmand thorw the error.
    else {
      this.output.overwriteerror();
      this.output.adderrorout("man: " + command + ": command does not exist");
      this.output.adderrorout("\r");
    }
  }

  /**
   * getDoc is suppose to get the documentation of the class
   */
  @Override
  public String getDoc() {
    return "man method will return the documentation of the input command";
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
