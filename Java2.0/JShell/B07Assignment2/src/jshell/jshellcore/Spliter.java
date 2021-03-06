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
/**
 * This class is used to split the input of the user.
 * Each input would be split to 3 parts. The first is
 * the command, the second part is the option and 
 * argument, the third part is the redirect file.
 * Every method is static since we
 * @author XianghuDai
 *
 */
public class Spliter {
	
	public static String[] commandSplit(String command) {
		return split(trim(command));
	}
	
	/**
	 * This method split a string to exactly two parts.
	 * the first part is command, the second part is argument
	 */
	
	private static String[] split(String command) {
		String[] result = {"", "", ""};
		String[] sp = command.split("\\s+", 2);
		if (command.contains(">>")) {
			String[] sp2 = sp[1].split(">>", 2);
			result[0] = sp[0];
			result[1] = sp2[0].replaceAll("\\s+", "");
			result[2] = sp2[1].replaceAll("\\s+", "");
		} else if (command.contains(">")) {
			String[] sp2 = sp[1].split(">", 2);
			result[0] = sp[0];
			result[1] = sp2[0].replaceAll("\\s+", "");
			result[2] = sp2[1].replaceAll("\\s+", "");
		} else {
			for(int i=0;i<sp.length;i++) {
				result[i] = sp[i];
			}
		}
		return result;
	}
	
	/**
	 * This method is to trim spaces on left hand side
	 * and right hand side of the command.
	 */
	private static String trim(String command) {
		return command.replaceAll("^\\s+", "").replaceAll("\\s+$", "");
	}
	
}
