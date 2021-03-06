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
package jshell.jshellcore;

import java.util.HashMap;
import java.util.Map;

/**
 * ArgParser is a class that is responsible for parsing the input of the
 * command. It will generate a map that maps keyword as key and the string
 * as value.
 * @author danielxu
 *
 */
public class ArgParser {

  /**
   * Parse the input from the command. It will generate a map that contains
   * keyword-value pairs. If the given input has no such optional keyword,
   * using <code>map.get()</code> will return null, otherwise it will return
   * the corresponding value. For example, parsing:
   * <center>/users/Desktop -type f -name "xyz"</center>
   * with given optional keywords: -type -name, -notexist.<br>
   * The returned map will contains:
   * <center>key: ""         value: /users/Desktop</center>
   * <center>key: -type:     value: f</center>
   * <center>key: -name:     value:"xyz"</center>
   * <center>key: -notexist: value:null</center>
   * @param input The input from command
   * @param keys Optional keywords
   * @return A Map that contains k-v pair as mentioned above
   */
  public static Map<String, String> parse(String input, String...keys){
    Map<String, String> map = new HashMap<String, String>();
    String pattern = "";
    for(String key : keys) {
      pattern += "("+key+")|";
    }
    pattern = pattern.substring(0, pattern.length()-1);
    String[] sp = input.split(pattern);
    for(int i=0;i<sp.length;i++) {
      if(i==0) {
        map.put("", sp[0].replaceAll("^\\s+", "").replaceAll("\\s+$", ""));
      }
      else {
        map.put(keys[i-1], sp[i].replaceAll("^\\s+", "").replaceAll("\\s+$", ""));
      }
    }
    return map;
  }
  
}
