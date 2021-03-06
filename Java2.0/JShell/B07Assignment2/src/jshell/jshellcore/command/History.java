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

import java.util.ArrayList;
import java.util.List;
import jshell.jshellcore.Command;
import jshell.jshellcore.Input;
import jshell.jshellcore.Output;

/***
 * the class store all the command, and return the when it been called
 * 
 * @author Jiahong Wang
 * @author danielxu
 * @param null or number of commands tried to print
 *
 */
public class History implements Command {
  private List<Input> command;
  private List<String> save_command;
  private List<String> load_command;
  /** output is the output object store output */
  private Output output = new Output();

  public History() {
    command = new ArrayList<Input>();
    save_command = new ArrayList<String>();
    load_command = new ArrayList<String>();
  }

  public void add(Input input) {
    command.add(input);
    String content = input.GetInputContent();
    save_command.add(content);
  }

  public void addload(String input) {
    load_command.add(input);
  }

  @Override
  public void excute(String input) {
    if (input.equals("")) {
      printout(command.size());
    } else {
      printout(Integer.parseInt(input));
    }
  }

  public void printout(int number) {
    if (number < 0 || number > command.size()) {
      this.output.overwriteerror();
      this.output.adderrorout("history: Number out of range: " + number);
      this.output.adderrorout("\r");
      return;
    }
    this.output.overwriteOutput();
    for (int index = command.size() - number; index < command.size(); index++) {
      String output = command.get(index).toString();
      this.output.addOutputContent(output);
      this.output.addOutputContent("\r");
    }
  }

  public List<String> toList() {
    return save_command;
  }

  public List<String> loadtoList() {
    return load_command;
  }

  @Override
  public String getDoc() {
    // TODO Auto-generated method stub
    return "Command history <int> to print out recent <int> command, "
        + " if <int> is not given or <int> is greater than the number of"
        + "commands, all the commands will be displayed. If <int> is"
        + "less than or equal 0, nothing will be displayed.";
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
