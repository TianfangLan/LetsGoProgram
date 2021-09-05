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
 * A path is just a class that stores a path
 * from root to some nodes.
 * @author danielxu
 *
 */
public class Path {

	/**Path in string**/
	private String path;
	/***Parent*/
	private Path parent;
	
	public Path(Path parent, String child) {
		if(!parent.toString().equals("/")) {
			this.path = parent.toString() + "/" + child;
		}
		else {
			this.path = "/" + child;
		}
		this.path = PathPreprocessor.preprocessing(path);
	}
	
	/**
	 * Construct a new Path, by passing the
	 * string representation of the path
	 * @param path
	 */
	public Path(String path) {
		this.path = PathPreprocessor.preprocessing(path);
	}
	
	/**
	 * Get the parent path of this path. For
	 * instance, /a/b/c will have parent path
	 * /a/b.
	 * @return {@link Path}, parent path of this path
	 */
	public Path getParent() {
		if(parent == null) {
			StringBuilder sb = new StringBuilder();
			String[] splitted = path.split("/");
			for(int i=0;i<splitted.length-1;i++) {
				sb.append(splitted[i]);
				if(i != splitted.length-2) {
					sb.append("/");
				}
			}
			parent = new Path(sb.toString());
		}
		return parent;
	}
	
	/**
	 * Get the name of the path, which means for example:
	 * path /a/b/c has name c
	 * @return
	 */
	public String getName() {
		String[] s = path.split("/");
		if(s.length == 0) {
			return "";
		}
		return s[s.length-1];
	}
	
	/**
	 * Overrided parent toString method, return
	 * the String representation of the path
	 */
	@Override
	public String toString() {
		return path;
	}
	
}
