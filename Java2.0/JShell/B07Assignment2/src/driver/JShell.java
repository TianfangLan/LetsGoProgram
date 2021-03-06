// **********************************************************
// Assignment2:
// Student1: Junxing Xu
// UTORID user_name:xujunxin
// UT Student #: 1004019028
// Author: Junxing Xu
//
// Student2: Tianfang Lan
// UTORID user_name: lantianf
// UT Student #: 1002687210
// Author: Tianfang Lan
//
// Student3: Jiahong Wang  
// UTORID user_name: wangj398
// UT Student #: 1002695933
// Author: Jiahong Wang
//
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
package driver;

import java.util.Scanner;
import jshell.jshellcore.Command;
import jshell.jshellcore.Input;
import jshell.jshellcore.Mapper;
import jshell.jshellcore.OutRedirector;
import jshell.jshellcore.Prompter;
import jshell.jshellcore.Spliter;
import jshell.jshellcore.command.History;
/**
 * this is the driver of JShell. Users can use command line
 * to interact with the mock file system
 */
public class JShell {

  public static void main(String[] args) {
	  new JShell().run();
  }

	private Prompter pp;
	private int line;
	
	/**
	 * the constructor of JShell
	 */
	public JShell() {
		pp = new Prompter();
		line = 1;
	}
	/**
	 * the way that JShell operates is prompt the path first
	 * and then take the input from the user, then Spliter and ArgParser
	 * analyze the input. OutRedirector and Mapper would execute the command
	 * and might redirect out the output or print the output directly.
	 */
	public void run() {
		@SuppressWarnings("resource")
		Scanner scan = new Scanner(System.in);
		while(true) {
			// print prompt
			pp.pirntPrompt();
			// scan the input typed by user	
			String input = scan.nextLine();
			if (input.length() != 0 && input != "\\s+") {
				// split the input
				String[] inputList = Spliter.commandSplit(input);
				String key = inputList[0];
				String arg = inputList[1];
				int redirectNeeded = OutRedirector.detectRedirectSign(input);
				String outFile = inputList[2];
				if (redirectNeeded != 0) {
					OutRedirector.createFile(outFile);
				}
				History hist = (History)(Mapper.getMapper().getCommand("history"));
				hist.add(new Input(line, input));
				line++;
				// check if the command is validate
				if (Mapper.getMapper().isExist(key)) {
					// map the command and execute it
					Command c = Mapper.getMapper().getCommand(key);
					c.excute(arg);
					String output = c.getOutput();
					String error = c.geterror();
					System.out.print(error);
					// decide if redirect output or not
					if (redirectNeeded == 1) {
						OutRedirector.appendOutput(outFile, output);
					} else if (redirectNeeded == 2) {
						OutRedirector.overwriteOutput(outFile, output);
					} else {
						System.out.print(output);
					}
				} else {
					System.out.println(input+": command does not exist");
				}
			}
		}
	}
  
}
