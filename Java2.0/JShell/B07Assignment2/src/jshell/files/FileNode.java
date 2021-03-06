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

import java.util.List;

/**
 * A FileNode is a kind of node in the FileSystem tree, it inherits {@link Node}
 * since it is also a node. However, the main difference is, FileNode class has
 * no children since it is a file but not a directory/
 * 
 * @author danielxu
 *
 */
public class FileNode extends Node {

  private File file;

  public FileNode(String name, Node parent) {
    super(name, parent);
    file = new File();
  }

  /**
   * Get the file of that stores in the FileNode
   * 
   * @return
   */
  public File getFile() {
    return file;
  }
  
  /**
   * Set the File that stores in this node to the given
   * file.
   * @param f {@link File}
   */
  public void setFile(File f) {
    this.file = f;
  }
  
  @Override
  public FileNode copy() {
    FileNode fn = new FileNode(name, parent.copy());
    fn.setFile(file.copy());
    return fn;
  }

  @Override
  public boolean isFile() {
    return true;
  }

  @Override
  public List<Node> getChildren() {
    return null;
  }

  @Override
  public Node getChild(String name) {
    return null;
  }

}
