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
package jshell.files;

import java.util.List;
import java.util.Stack;
import jshell.exceptions.InvalidArgException;
import jshell.exceptions.NotExistException;

/**
 * FileSystem of the JShell. The FileSystem is responsible for creating and
 * managing files/directories. All the files and directories are in virtual
 * environment, which means that when JShell is closed, all the files and
 * directories will be cleared and removed.<br>
 * 
 * FileSystem is designed to use Singleton Mode, which means only one instance
 * of FileSystem should exists. This design is actually very reasonable since
 * there should be only one system running and modifying files, multiple
 * instances may causes files interruptions.<br>
 * 
 * Way to access FileSystem: <code>FileSystem.getSystem()...</code>
 * 
 * @author danielxu
 *
 */
public class FileSystem {

  private Directory dir;
  private static final FileSystem instance = new FileSystem();
  private Stack<String> directoryStack;

  /*
   * FileSystem is using singleton mode, therefore, set constructor as private
   */
  private FileSystem() {
    dir = new Directory();
    directoryStack = new Stack<String>();
  }

  /**
   * Clean the whole file system, remove all files and directories and start by
   * a new root directory with nothing in it. Use with caution!
   */
  public void clean() {
    dir = new Directory();
    directoryStack.clear();
  }

  /**
   * Push the current directory into the stack and then change current directory
   * to the given directory
   */
  public void push(String path) {
    checkEmpty(path);
    checkExist(path);
    directoryStack.push(getCur());
    change(path);
  }

  /**
   * Remove the last stored directory from the stack and change current
   * directory to it.
   */
  public void pop() {
    change(directoryStack.pop());
  }

  /**
   * Get a boolean that tell if directory or file with given path exists in the
   * file system.
   * 
   * @param path String representation of the path
   * @return True if does exist, false otherwise
   */
  public boolean exist(String path) {
    return dir.isExist(generatePath(path));
  }

  /**
   * Get a boolean value that tells if the given path pointing to a file or a
   * directory
   * 
   * @param path String representation of the path
   * @return True if it is a file, false otherwise
   */
  public boolean isFile(String path) {
    return dir.isFile(generatePath(path));
  }

  /**
   * Get a file by path
   * 
   * @param path Path to the file
   */
  public File getFile(String path) {
    checkExist(path);
    return dir.getFile(generatePath(path));
  }
  
  /**
   * Get the tree view start from the root
   * @return
   */
  public String tree() {
    return dir.tree();
  }

  // /**
  // * Get all the files and directories under a given <b>relative path</b>
  // store
  // * in a string array
  // * @param path String representation of the path
  // * @return String array that stores all files and directories
  // */
  // public String[] relativelist(String path) {
  // List<Node> list = dir.list(new RelativePath(dir.getCurPath(), path));
  // String[] names = new String[list.size()];
  // for(int i=0;i<list.size();i++) {
  // names[i] = list.get(i).getName();
  // }
  // return names;
  // }
  //
  // /**
  // * Get all the files and directories under a given <b>absolute path</b>,
  // * store in a string array
  // * @param path String representation of the path
  // * @return String array that stores all files and directories
  // */
  // public String[] absoluteList(String path) {
  // List<Node> list = dir.list(new Path(path));
  // String[] names = new String[list.size()];
  // for(int i=0;i<list.size();i++) {
  // names[i] = list.get(i).getName();
  // }
  // return names;
  // }
  //
  // /**
  // * Get all the files and directories under current working directory,
  // * store in a string array.
  // * @return A string array that stores all the files and directories under
  // * current working directory
  // */
  // public String[] list() {
  // List<Node> list = dir.list();
  // String[] names = new String[list.size()];
  // for(int i=0;i<list.size();i++) {
  // names[i] = list.get(i).getName();
  // }
  // return names;
  // }

  /**
   * Get all the files and directories under current working directory, store in
   * a string array.
   * 
   * @return String array that stores all files and directories under current
   *         working directory
   */
  public String[] list() {
    return list(getCur());
  }
  
  /**
   * Recursively finding all the files or directories with the given name under
   * the gviven path
   * @param path The starting path
   * @param type Type that are looking for, f or d
   * @param name Name of the files or directories
   * @return A list that contains all matches paths
   */
  public List<String> find(String path, String type, String name) {
    checkEmpty(path);
    checkExist(path);
    checkIsFile(path);
    if(type.equals("d")) {
      return dir.findDir(generatePath(path), name);
    }
    else if(type.equals("f")) {
      return dir.findFile(generatePath(path), name);
    }
    else {
      throw new InvalidArgException("Unexpected type: "+type);
    }
  }

  /**
   * Get all the files and directories under a given path, store in a string
   * array. The given path can be either a relative path or absolute path
   * 
   * @param path String representation of the path
   * 
   * @return String array that stores all files and directories
   * 
   * @require Need to make sure that the path is in valid format, which means it
   *          can either be /a/b/c or b/c
   */
  public String[] list(String path) {
    checkExist(path);
    List<Node> list = dir.list(generatePath(path));
    String[] names = new String[list.size()];
    for (int i = 0; i < list.size(); i++) {
      names[i] = list.get(i).getName();
    }
    return names;
  }

  /**
   * Get the current directory in string format
   * 
   * @return Current working directory in string format
   */
  public String getCur() {
    return dir.getCurPath().toString();
  }

  // /**
  // * Change the current working directory to given directory
  // * by <b>relative path</b>
  // *
  // * @param path The string representation of the path
  // *
  // * @require Please make sure that the path is a valid
  // * path, for example, 'usr/daniel' is a valid relative
  // * path, which means change to directory 'daniel' in 'usr'
  // * folder, where 'usr' is one of the folders in current working
  // * directory.
  // */
  // public void changeRelative(String path) {
  // dir.change(new RelativePath(dir.getCurPath(), path));
  // }
  //
  // /**
  // * Change the current working directory to given directory
  // * by <b>absolute path</b>
  // *
  // * @param path The string representation of the path
  // *
  // * @reuqire Please make sure that the path is a valid
  // * path, for example, '/usr/CSCB07/Assignment' is
  // * a valid absolute path, which means change to directory
  // * 'Assignment' under '/usr/CSCB07/Assignment'.
  // */
  // public void changeAbsolute(String path) {
  // dir.change(new Path(path));
  // }

  /**
   * Change the current working directory to given directory by path, the given
   * path can be either a relative path or absolute path.
   * 
   * @param path The string representation of the path
   * 
   * @reuqire Need to make sure that the path is in valid format, which means it
   *          can either be /a/b/c or b/c
   */
  public void change(String path) {
    checkEmpty(path);
    checkExist(path);
    checkIsFile(path);
    dir.change(generatePath(path));
  }

  // /**
  // * Create a new <b>file</b> by given <b>relative path</b>
  // *
  // * @param path The string representation of the path
  // *
  // * @require Please make sure that the path is a valid
  // * path, for example, 'usr/README.txt' is a valid relative
  // * path, which means create a file named 'README.txt' inside 'usr'
  // * folder, where 'usr' is one of the folders in current working
  // * directory.
  // */
  // public void newRelativeFile(String path) {
  // dir.appendf(new RelativePath(dir.getCurPath(), path));
  // }
  //
  // /**
  // * Create a new <b>file</b> by given <b>absolute path</b>
  // *
  // * @param path The string representation of the path
  // *
  // * @require Please make sure that the path is a valid
  // * path, for example, 'CSCB07/Assignment' is
  // * a valid relative path, which means create directory
  // * 'Assignment' under folder 'CSCB07', where 'CSCB07'
  // * is one of the folders in current working directory
  // */
  // public void newAbsoluteFile(String path) {
  // dir.appendf(new Path(path));
  // }

  /**
   * Create a new <b>file</b> by given path, the path can be either relative
   * path or absolute path.
   * 
   * @param path The string representation of the path
   * 
   * @require Need to make sure that the path is in valid format, which means it
   *          can either be /a/b/c or b/c
   */
  public void makeFile(String path) {
    checkEmpty(path);
    Path p = generatePath(path);
    checkExist(p.getParent().toString());
    dir.appendf(p);
  }
  
  /**
   * Copying content of old path to the new path.
   * @param opath The old path
   * @param npath The new path
   */
  public void copy(String opath, String npath) {
    checkExist(opath);
    checkExist(npath);
    // IF old path is file but new path is not file, raise error
    if(!isFile(opath) && isFile(npath)) {
      throw new InvalidArgException("Cannot copy from directory to file");
    }
    Node n = dir.copy(generatePath(opath));
    dir.copy(n, generatePath(npath));
  }

  // /**
  // * Create a new <b>directory</b> by given <b>relative path</b>
  // *
  // * @param path The string representation of the path
  // *
  // * @require Please make sure that the path is a valid
  // * path, for example, 'usr/daniel' is a valid relative
  // * path, which means create a folder named 'daniel' inside 'usr'
  // * folder, where 'usr' is one of the folders in current working
  // * directory.
  // */
  // public void newRelativeDir(String path) {
  // dir.append(new RelativePath(dir.getCurPath(), path));
  // }
  //
  // /**
  // * Create a new <b>directory</b> by given <b>absolute path</b>
  // *
  // * @param path The string representation of the path
  // *
  // * @require Please make sure that the path is a valid
  // * path, for example, '/usr/CSCB07/Assignment' is
  // * a valid absolute path, which means create directory
  // * 'Assignment' under '/usr/CSCB07/Assignment'.
  // */
  // public void newAbsoluteDir(String path) {
  // dir.append(new Path(path));
  // }

  /**
   * Create a new <b>directory</b> by given path, the path can be either a
   * relative path or absolute path.
   * 
   * @param path The string representation of the path
   * 
   * @require Need to make sure that the path is in valid format, which means it
   *          can either be /a/b/c or b/c
   */
  public void makeDir(String path) {
    checkEmpty(path);
    Path p = generatePath(path);
    checkExist(p.getParent().toString());
    dir.append(p);
  }

 /**
  * the method will move the item to the goal directory
  * @param item
  * @param goal
  */
  public void moveDir(String item, String goal) {
    checkEmpty(item);
    checkEmpty(goal);
    checkExist(item);
    checkExist(goal);
    // generate the paths
    Path itempath = generatePath(item);
    Path goalpath = generatePath(goal);
    dir.move(itempath, goalpath);
  }

 /**
  * check if the goalpath if the sub directory of the itempath.
  * @param item
  * @param goal
  * @return true if the goalpath is a sub directory of the itempath.
  */
  public boolean checkSub(String item, String goal) {
    checkEmpty(item);
    checkEmpty(goal);
    checkExist(item);
    checkExist(goal);
    // generate the paths
    Path itempath = generatePath(item);
    Path goalpath = generatePath(goal);
    return goalpath.toString().startsWith(itempath.toString());
  }
  /*
   * Generate a Path based on the given string representation of the path. If
   * the path starts with "/", it means that it is always an absolute path,
   * otherwise, it is a relative path. Since RelativePath extends Path,
   * therefore, we only need to return Path and it does not matter which kind of
   * path we are returning.
   */
  private Path generatePath(String path) {
    Path p;
    // starts with / means it is always an absolute path
    if (path.startsWith("/")) {
      p = new Path(path);
    } else {
      p = new RelativePath(dir.getCurPath(), path);
    }
    return p;
  }

  /*
   * Internal method, check if a given path is exist, if not, throw
   * NotExistException
   */
  private void checkExist(String p) {
    Path path = generatePath(p);
    if (!dir.isExist(path)) {
      throw new NotExistException(p + ": no such file or directory");
    }
  }
  
  /*
   * Internal method, check if a given path is an empty string,
   * if yes throw exception
   */
  private void checkEmpty(String p) {
    if(p.equals("")) {
      throw new InvalidArgException("No arg given");
    }
  }
  
  /*
   * Internal method, check if a given path is a file,
   * if yes throw exception
   */
  private void checkIsFile(String p) {
    if(isFile(p)) {
      throw new InvalidArgException("Wrong arg type: file");
    }
  }


  /**
   * Get the instance of the {@link FileSystem}, there is only one instance
   * being shared accross the whole application.
   * 
   * @return Instance of the FileSystem
   */
  public static final FileSystem getSystem() {
    return instance;
  }

}
