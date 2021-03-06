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
package jshell.files;

import java.util.ArrayList;

/** The class File. The class will read the file and store the whole
 *  file into the class in the form of list string. The class contains
 *  a <code>path</code> to point which file will be open or operated. <br>
 *  The class File is used to solve the write, append and get content
 *  problems.
 *
 * @author tianfang Lan
 */
public class File {
  /***path is the path for the file, store in the form of <code>path</code>*/
  private Path path;
  /***content will store String in a List, each element is a line of String*/
  private ArrayList<String> content = new ArrayList<>();
  /** File must contain a path and a String for content.
   * 
   * @param target is the path of the File
   * @param file is the content in the File.
   */
  public File(String content){
    this.content = stringToList(content);
  }

  public File() {
  }
  
  /** 
   * stringToList will trans a whole string into a list
   * each element of the list is a line of the string
   * 
   * @param string input string
   * @return the list of the input string
   */
  private ArrayList<String> stringToList(String string) {
    // split the input string into array of string
    String[] array = string.split("\n");
    // al is the return arraylist
    ArrayList<String> al = new ArrayList<String>();
    for (String line :array) {
      // add every line as an element into al
      al.add(line);
    }
    return al;
  }

  /**
   * listToString will trans a list back to a whole string.
   * @param list is the list of the string
   * @return the whole string back
   */
  private String listToString(ArrayList<String> list) {
    // create a empty string to store the returning string
    String string = "";
    int index = 0;
    while (index <= list.size() - 1) {
      if (index != 0){
        // append the element in the the list to the string
        string += "\n" + list.get(index);
      }
      else {
        string += list.get(index);
      }
      index ++;
    }
    return string;
  }
  
  
  /** 
   * the getContent will return the content in the current File
   * 
   * @return the content of the file in the form of string.
   */

  public String getContent(){
    return listToString(content);
  }
  
  /**
   * Get a copy of this file object 
   * @return A deep copy of this file
   */
  public File copy() {
    File f = new File(getContent());
    return f;
  }

  
  /** the getFilePath will return the path in the current File
   * 
   * @return the path of the file as a <code>path</code>.
   */
  public Path getFilePath(){
    return path;
  }

  
  /** 
   * overWrite will take in a String then overwrite the original content
   * in the File
   * @param newcontent
   */
  public void overWrite(String newcontent) {
    // change the string into list, and overwrite the content
    content = stringToList(newcontent);
  }
  
  /**
   * append will add the input content at the end of the string but not
   * overwrite it.
   * @param newstring is the String will be append to the end of the content
   */
  public void append(String newstring) {
    String newcont;
    newcont = listToString(content) + "\n"+ newstring;
    content = stringToList(newcont);
  }
}
