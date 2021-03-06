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

import java.io.BufferedReader;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;
import jshell.jshellcore.Command;
import jshell.jshellcore.Mapper;
import jshell.jshellcore.Output;
import jshell.jshellcore.Spliter;

/***
 * the class print the contents for the input path
 * 
 * @author Jiahong Wang
 * @param the filename of txt file
 * @return null
 */
public class Load implements Command {
  /** output is the output object store output */
  private Output output = new Output();

  @SuppressWarnings("resource")
  @Override
  public void excute(String input) {
    // TODO Auto-generated method stub
    if (input.equals("")) {
      System.err.println("save: No filename arg");
      return;
    }
    try {
      BufferedReader reader = new BufferedReader(new FileReader(input));
      String text;
      while ((text = reader.readLine()) != null) {
        loadCommand(text);
      }
    } catch (FileNotFoundException e) {
      // TODO Auto-generated catch block
      this.output.overwriteerror();
      this.output.adderrorout("load: can not find " + input);
      this.output.adderrorout("\r");
    } catch (IOException e) {
      // TODO Auto-generated catch block
      this.output.overwriteerror();
      this.output.adderrorout("load: "+e.getMessage());
      this.output.adderrorout("\r");
    }
  }

  public void loadCommand(String input) {
    String[] inputList = Spliter.commandSplit(input);
    String key = inputList[0];
    String arg = inputList[1];

    if (!(key.equals("load")) && !(key.equals("save"))) {
      History hist = (History) (Mapper.getMapper().getCommand("history"));
      hist.addload(input);
      if (Mapper.getMapper().isExist(key)) {
        // map the command and execute it
        Command c = Mapper.getMapper().getCommand(key);
        c.excute(arg);
      }
    }
  }

  @Override
  public String getDoc() {
    // TODO Auto-generated method stub
    return "Command load <filename> to load the saved filesystem";
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
