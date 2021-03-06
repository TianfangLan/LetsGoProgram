//**********************************************************
//Assignment2:
//Student1: Junxing Xu
//UTORID user_name:xujunxin
//UT Student #: 1004019028
//Author: Junxing Xu
//
//
//Honor Code: I pledge that this program represents my own
//program code and that I have coded on my own. I received
//help from no one in designing and debugging my program.
//I have also read the plagiarism section in the course info
//sheet of CSC B07 and understand the consequences.
//*********************************************************
package jshell.files;

/**
 * PathPreprocessor is a static class that responsible for
 * modifying and trimming path. No instance is required for
 * this PathProcessor, just call methods by
 * <code>PathPreprocessor.method()</code>
 * @author danielxu
 *
 */
public class PathPreprocessor {
	
	private PathPreprocessor() {}
	
	public static String getName(String path) {
	  String[] t = path.split("/");
	  return t[t.length-1];
	}

	/**
	 * Remove all unnecessary / in the path.
	 * For example: /usr/////daniel//xu////
	 * will be trimed to: /usr/daniel/xu
	 * @param path String representation of the path
	 * @return The trimed path
	 */
	public static String trim(String path) {
		// Remove duplicated /
		path = path.replaceAll("\\/+", "/");
		// If only one /, it is root path
		if(path.equals("/")) {
			return path;
		}
		// Remove / after the path
		return path.replaceAll("\\/+$", "");
	}

	/**
	 * Replace all . to empty, since . represents current
	 * directory, therefore, it is unnecessary to be a 
	 * part of the path.
	 * For example:
	 * /usr/./daniel/./xu/././././ will be modified to:
	 * /usr/daniel/xu
	 * @param path String representation of the path
	 * @return The modified path
	 */
	public static String stay(String path) {
		String[] splitted = path.split("/");
		String result = "";
		for(int i=0;i<splitted.length;i++) {
			if(!splitted[i].equals(".")) {
				result += splitted[i] + "/";
			}
		}
		return trim(result);
	}
	
	/**
	 * Replace all .. to corresponding path. For example:
	 * /usr/daniel/.. will be modified to /usr
	 * @param path String representation of the path
	 * @return The modified path
	 */
	public static String parent(String path) {
		// /usr/daniel/../xu
		String[] splitted = path.split("/");
		for(int i=0;i<splitted.length;i++) {
			if(splitted[i].equals("..")) {
				splitted[i] = null;
				int j = i;
				while(j >= 0 && splitted[j] == null) {
					j -- ;
				}
				if(splitted[j] == null) {
					// TODO raise error
				}
				else {
					splitted[j] = null;
				}
			}
		}
		String result = "";
		for(int i=0;i<splitted.length;i++) {
			if(splitted[i] != null) {
				result += splitted[i] + "/";
			}
		}
		return trim(result);
	}
	
	/**
	 * Combine all preprocessing steps:
	 * <ol>
	 * <li>{@link #trim(String)}</li>
	 * <li>{@link #stay(String)}</li>
	 * <li>{@link #parent(String)}</li>
	 * </ol>
	 * @param path String representation of the path
	 * @return The path that is valid and ready to use
	 */
	public static String preprocessing(String path) {
		return parent(stay(trim(path)));
	}
	
}
