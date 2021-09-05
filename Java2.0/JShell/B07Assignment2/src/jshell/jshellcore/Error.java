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
package jshell.jshellcore;

/***
 * the class will return the error message
 * 
 * @author Jiahong Wang
 * @return the error message 
 */
public class Error {

  public Error() {

  }

  public static String NoSuchFile() {
    return "NO SUCH FILE";
  }

  public static String WrongDirectory() {
    return "NO SUCH DIRECTORY";
  }

  public static String ThisIsNotFile() {
    return "THIS IS NOT FILE";
  }
}
