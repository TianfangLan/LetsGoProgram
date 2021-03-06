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

import java.io.BufferedWriter;
import java.io.FileWriter;
import java.io.IOException;
import java.util.List;
import jshell.jshellcore.Command;
import jshell.jshellcore.Mapper;
import jshell.jshellcore.Output;

/***
 * the class print the contents for the input path
 * 
 * @author Jiahong Wang
 * @param the filename
 * @return null
 */
public class Save implements Command {

  /** output is the output object store output */
  private Output output = new Output();

  @Override
  public void excute(String input) {
    // TODO Auto-generated method stub
    if (input.equals("")) {
      this.output.overwriteerror();
      this.output.adderrorout("save: No filename arg");
      this.output.adderrorout("\r");
      return;
    }

    History hist = (History) (Mapper.getMapper().getCommand("history"));
    List<String> loadtext = hist.loadtoList();
    List<String> text = hist.toList();
    try {
      BufferedWriter writer = new BufferedWriter(new FileWriter(input));
      for (String y : loadtext) {
        writer.write(y);
        writer.newLine();
      }
      for (String x : text) {
        writer.write(x);
        writer.newLine();
      }
      writer.close();
    } catch (IOException e) {
      // TODO Auto-generated catch block
      this.output.overwriteerror();
      this.output.adderrorout(e.getMessage());
      this.output.adderrorout("\r");
    }
  }

  @Override
  public String getDoc() {
    // TODO Auto-generated method stub
    return "Command save <filename> to save the "
        + "current session of JShell to " + "the <filename>";
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
