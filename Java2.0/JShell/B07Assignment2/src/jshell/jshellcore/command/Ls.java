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

import jshell.exceptions.NotExistException;
import jshell.files.FileSystem;
import jshell.files.PathPreprocessor;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/***
 * the class print the contents for the input path
 * 
 * @author Jiahong Wang
 * @param null or the full path or the relative path
 * @return all the content inside the given path
 */

public class Ls implements Command {

  /** output is the output object store output */
  private Output output = new Output();

  @Override
  public void excute(String input) {
    this.output.overwriteOutput();
    try {
      if (input.equals("")) {
        print(FileSystem.getSystem().list());
      } else {
        String[] args = input.split("\\s+");
        if (args[0].equals("-R")) {
          if (args.length == 1) {
            recursively("");
          } else {
            for (int index = 1; index < args.length; index++) {
              recursively(args[index]);
            }
          }
        } else {
          for (String arg : args) {
            if (FileSystem.getSystem().isFile(arg)) {
              print(arg);
            } else {
              this.output.overwriteerror();
              try {
                FileSystem.getSystem().list(arg);
                print(PathPreprocessor.getName(arg) + ":");
                print(FileSystem.getSystem().list(arg));
              }catch(NotExistException e) {
                this.output.overwriteerror();
                this.output.adderrorout("ls: " + e.getMessage());
                this.output.adderrorout("\r");
              }
            }
          }
        }
      }
    } catch (NotExistException e) {
      this.output.overwriteerror();
      this.output.adderrorout("ls: " + e.getMessage());
      this.output.adderrorout("\r");
    }
  }

  private void recursively(String args) {
    if (args.equals("")) {
      String root = FileSystem.getSystem().getCur();
      print(root + ":");
      print(FileSystem.getSystem().list());
      if (FileSystem.getSystem().list().length > 0) {
        for (String m : FileSystem.getSystem().list()) {
          if(root.equals("/")) {
            m = root + m;
          }else {
            m = root + "/" +m;
          }
          recursively(m);
        }
      }
    } else {
      if (FileSystem.getSystem().isFile(args)) {
        print(args + ":");
        print(args);
      } else {
        if (FileSystem.getSystem().list(args).length != 0) {
          print(args + ":");
          print(FileSystem.getSystem().list(args));
          for (String arg : FileSystem.getSystem().list(args)) {
            arg = args +"/" + arg;
            recursively(arg);
          }
        } else {
          print(args + ":");
          print(FileSystem.getSystem().list(args));
          print("");
        }
      }
    }
  }

  private void print(String... msg) {
    for (String m : msg) {
      this.output.addOutputContent(m);
      this.output.addOutputContent("\r");
    }
  }

  @Override
  public String getDoc() {
    return "Command ls<path> to print the contents of the given <path>";
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
