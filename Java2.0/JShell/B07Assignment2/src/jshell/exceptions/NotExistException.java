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
package jshell.exceptions;

/**
 * This exception will be thrown when trying to get to a
 * file or directory that does not exist.
 * @author danielxu
 *
 */
public class NotExistException extends RuntimeException{

	public NotExistException(String err) {
		super(err);
	}
	
}
