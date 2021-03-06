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

import java.util.HashMap;
import java.util.Map;
import jshell.jshellcore.command.Cat;
import jshell.jshellcore.command.Cd;
import jshell.jshellcore.command.Cp;
import jshell.jshellcore.command.Echo;
import jshell.jshellcore.command.Exit;
import jshell.jshellcore.command.Find;
import jshell.jshellcore.command.Get;
import jshell.jshellcore.command.History;
import jshell.jshellcore.command.Load;
import jshell.jshellcore.command.Ls;
import jshell.jshellcore.command.Man;
import jshell.jshellcore.command.Mkdir;
import jshell.jshellcore.command.Mv;
import jshell.jshellcore.command.Popd;
import jshell.jshellcore.command.Pushd;
import jshell.jshellcore.command.Pwd;
import jshell.jshellcore.command.Save;
import jshell.jshellcore.command.Tree;

/**
 * Mapper map is used to map the input command of
 * users to the corresponding command class.
 * It is designed to use singleton mode, since we
 * don't need more than one Mapper.
 * @author XianghuDai
 *
 */
public class Mapper {
	
	private Map<String, Command> map;
	
	private static final Mapper instance = new Mapper();
	
	private Mapper() {
		map = new HashMap<String, Command>();
		init();
	}
	
	/**
	 * Add all k-v pair to the map
	 */
	private void init() {
		map.put("exit", new Exit());
		map.put("cat", new Cat());
		map.put("echo", new Echo());
		map.put("cd", new Cd());
		map.put("ls", new Ls());
		map.put("mkdir", new Mkdir());
		map.put("pushd", new Pushd());
		map.put("popd", new Popd());
		map.put("pwd", new Pwd());
		map.put("man", new Man());
		map.put("history", new History());
		map.put("cp", new Cp());
		map.put("mv", new Mv());
		map.put("get", new Get());
		map.put("save", new Save());
		map.put("load", new Load());
		map.put("tree", new Tree());
		map.put("find", new Find());
	}
	
	
	/**
	 * Get a boolean value that tells if the keyword
	 * exists in the map. If key does not exist, it
	 * also means that there is no such command.
	 * @param key The keyword of a command
	 * @return True if the key exists, false otherwise
	 */
	public boolean isExist(String key) {
		return map.get(key) != null;
	}
	
	/**
	 * Get the {@link Command} by its keyword, please
	 * notice that if the key does not exist in the map,
	 * null will be returned. Therefore, it is recommended
	 * to check existance of the commnad by {@link #isExist(String)}
	 * first before getting command.
	 * @param key The keyword of a command
	 * @return Command if key exists, null if it does not
	 */
	public Command getCommand(String key) {
		return map.get(key);
	}
	
	/**
	 * Get the instance of {@link CommandMapper}, this is
	 * the only way to get the instance.
	 * @return Instance of CommandMapper
	 */
	public static Mapper getMapper() {
		return instance;
	}
	
}
