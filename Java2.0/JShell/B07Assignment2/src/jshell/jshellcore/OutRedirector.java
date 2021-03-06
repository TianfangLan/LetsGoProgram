// **********************************************************
// Assignment2:
// Student4: Xianghu Dai
// UTORID user_name: daixian1
// UT Student #: 1004029623
// Author: Xianghu Dai
//
//
// Honor Code: I pledge that this program represents my own
// program code and that I have coded on my own. I received
// help from no one in designing and debugging my program.
// I have also read the plagiarism section in the course info
// sheet of CSC B07 and understand the consequences.
// *********************************************************
package jshell.jshellcore;

import jshell.files.File;
import jshell.files.FileSystem;

/**
 * OutRedirector is used to redirect out the output
 * of a command to a file, it might be used to redirect
 * error in the future.
 * It is designed to make every method static, since
 * we don`t need an OutRedirector instance.
 * @author XianghuDai
 *
 */
public class OutRedirector {
	
	/**
	 * check if the user entered redirect Sign, and analyze it is
	 * append or overwrite
	 * 
	 * @param input is the command line entered by the user
	 * @return an integer to record the redirect sign
	 */
	public static int detectRedirectSign(String input) {
		int result;
		if (input.contains(">>")){
			// when the redirect sign is >>, return 1
			result = 1;
		} else if (input.contains(">")) {
			// when the redirect sign is >, return 2
			result = 2;
		} else {
			// when there is no redirect sign, returns 0
			result = 0;
		}
		return result;
	}
	
	/**
	 * if the user entered redirect out sign with a file name,
	 * then create the file.
	 * @param fileName is the file that used to
	 * record the output
	 */
	public static void createFile(String fileName) {
        // append only when the file does not exist
        if (FileSystem.getSystem().exist(fileName) == false) {
          FileSystem.getSystem().makeFile(fileName);
        }
	}
	
	/**
	 * used to append output to the file
	 * @param fileName is the file used to redirect the output
	 * @param output is the content used to append to the file
	 */
	public static void appendOutput(String fileName, String output) {
      try{
    	  File file = FileSystem.getSystem().getFile(fileName);
	      // append the content.
	      file.append(output);
      } catch (NullPointerException e) {
    	  System.err.println("No file name is given.");
      }
	}
	
	/**
	 * used to overwrite output to the file
	 * @param fileName is the file used to redirect the output
	 * @param output is the content used to overwrite to the file
	 */
	public static void overwriteOutput(String fileName, String output) {
		try{
			File file = FileSystem.getSystem().getFile(fileName);
			// append the content.
			file.overWrite(output);
		} catch (NullPointerException e) {
			System.err.println("No file name is given.");
		}
        
	}
}
