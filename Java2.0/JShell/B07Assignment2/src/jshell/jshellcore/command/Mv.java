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
import jshell.files.FileSystem;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/***
 * The class is the command move, it will move the item OLDPATH to NEWPATH.
 * 
 * @author lan tianfang
 *
 */
public class Mv implements Command{
  /** output is the output object store output */
  private Output output = new Output();
  
  
  @Override
  public void excute(String input) {
    // split the input into 2.
    String[] paths = input.split("\\s+");
    // first part is the oldpath and second is the newpath with no whitespace.
    if (paths.length != 2) {
      System.err.println("mv should only have 2 paths");
      return;
    }
    String oldpath = paths[0];
    String newpath = paths[1].replaceAll("\\s+", "");
      try {
      if (FileSystem.getSystem().checkSub(oldpath, newpath)) {
        throw new NotExistException("cannot move item to sub directory");
      }
      else if(FileSystem.getSystem().exist(oldpath)
          && FileSystem.getSystem().exist(newpath)
          && ((FileSystem.getSystem().isFile(newpath)
              && FileSystem.getSystem().isFile(oldpath))
              || (!FileSystem.getSystem().isFile(newpath)))) {
        FileSystem.getSystem().moveDir(oldpath, newpath);
      }
      // when both newpath and oldpath are file
      else if (FileSystem.getSystem().isFile(newpath)
          && FileSystem.getSystem().isFile(oldpath)) {
        
      }
      // when new path is file and oldpath is a directory
      else if(FileSystem.getSystem().isFile(newpath)
          && !FileSystem.getSystem().isFile(oldpath)){
        throw new NotExistException("cannot move directory into a file.");
      }
      else{
        throw new NotExistException("The input path does not exist.");
      }
      
    }
    catch (NotExistException e) {
      this.output.overwriteerror();
      this.output.adderrorout("mv: " + e.getMessage());
      this.output.adderrorout("\r");
    }

  }

  @Override
  public String getDoc() {
    return "The command will move the item Oldpath to the newpath.";
  }

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
