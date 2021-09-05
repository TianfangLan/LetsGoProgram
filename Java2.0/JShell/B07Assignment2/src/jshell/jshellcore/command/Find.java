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

import java.util.List;
import java.util.Map;
import jshell.exceptions.InvalidArgException;
import jshell.exceptions.NotExistException;
import jshell.files.FileSystem;
import jshell.jshellcore.ArgParser;
import jshell.jshellcore.Command;
import jshell.jshellcore.Output;

/**
 * Receusively finding all files or directories with the given name
 * and under given directories.
 * @author danielxu
 *
 */
public class Find implements Command{

  private Output output = new Output();
  
  @Override
  public void excute(String input) {
    this.output.overwriteerror();
    Map<String, String> map = ArgParser.parse(input, "-type", "-name");
    String arg = map.get("");
    String type = map.get("-type");
    String name = map.get("-name");
    if(arg.equals("")){
      this.output.adderrorout("find: No paths given");
      this.output.adderrorout("\r");
    }
    else if(type == null) {
      this.output.adderrorout("find: No type given");
      this.output.adderrorout("\r");
    }
    else if(name == null) {
      this.output.adderrorout("find: No name given");
      this.output.adderrorout("\r");
    }
    else {
      String[] paths = arg.split("\\s+");
      int sindex = name.indexOf("\"");
      int lindex = name.lastIndexOf("\"");
      if(sindex == -1 || lindex == -1 || sindex==lindex) {
        this.output.adderrorout("echo: Wrong quotation");
        this.output.adderrorout("\r");
        return;
      }
      name = name.substring(sindex+1, lindex);
      output.overwriteOutput();
      for(String path : paths) {
        try {
          List<String> list = FileSystem.getSystem().find(path, type, name);
          output.addOutputContent("Under: " + path+"\n");
          if(list.size() == 0) {
            output.addOutputContent("No matches");
          }
          for(String s : list) {
            output.addOutputContent(s+"\n");
          }
          output.addOutputContent("\n");
        }
        catch(InvalidArgException e) {
          this.output.adderrorout("find: "+e.getMessage());
          this.output.adderrorout("\r");
        }
        catch(NotExistException e) {
          this.output.adderrorout("find: "+e.getMessage());
          this.output.adderrorout("\r");
        }
      }
    }
    System.out.println("\r");
  }

  @Override
  public String getDoc() {
    return "Receusively finding all files and directories with the given name"
        + "and under given directories";
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
