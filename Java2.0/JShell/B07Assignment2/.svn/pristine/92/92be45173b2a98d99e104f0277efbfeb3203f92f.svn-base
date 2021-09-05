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

import jshell.exceptions.InvalidArgException;
import jshell.exceptions.NotExistException;
import jshell.files.FileSystem;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/***
 * the class Pushd will push the working directory onto directory stack
 * and change the new current working directory to the input directory.
 * 
 * @author lan tianfang
 *
 */
public class Pushd implements Command {
	
  /** output is the output object store output */
  private Output output = new Output();

  /**
   * the method will push the working directory to the input directory.
   * 
   * @param arg is a path in the form of string.
   */
  @Override
  public void excute(String arg) {
    try {
      FileSystem.getSystem().push(arg);
    } catch (NotExistException e) {
      this.output.overwriteerror();
      this.output.adderrorout("pushd: " + e.getMessage());
      this.output.adderrorout("\r");
    } catch (InvalidArgException e) {
      this.output.overwriteerror();
      this.output.adderrorout("pushd: "+e.getMessage());
      this.output.adderrorout("\r");
    }
  }


  /**
   * getDoc is suppose to get the documentation of the class
   */
  @Override
  public String getDoc() {
    return "Push the working directory onto directory stack"
        + "and then changes the current working directory to the"
        + "input directory";
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
