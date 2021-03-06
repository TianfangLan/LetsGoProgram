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

import java.util.ArrayList;
import java.util.List;

/**
 * Directory, can be represented by ways to travel {@link DirectoryNode}. For
 * instance, if node 'root' has children 'usr' and 'bin', 'root/usr' can be a
 * way travel from node root to node usr. And 'root/bin' can be a way travel
 * from node root to node bin. There is a node with empty string represents the
 * root node, therefore, the root node is consistant and always has an empty
 * string, which is not allowed for other nodes.
 * 
 * @author danielxu
 *
 */
public class Directory {

  /** The root node **/
  private Node root;
  /** A pointer to the current node **/
  private Node cur;

  /**
   * Construct a Directory, with a default root {@link DirectoryNode} with name
   * ''.
   */
  public Directory() {
    /*
     * Root node is the node with name '' and have no parent since it is on top
     * of every node.
     */
    root = new DirectoryNode("", null);
    cur = root;
  }

  /**
   * Move the current pointer to its parent, if the parent is null, i.e it is
   * the root node already, error might occur
   */
  public void back() {
    // TODO error checking
    cur = cur.getParent();
  }

  /**
   * Change the current pointer to a new node by given path, which can be
   * relative or absolute.
   * 
   * @param path Path to the node that will be the new current pointer
   */
  public void change(Path p) {
    cur = getByPath(p);
  }

  /**
   * Change the current pointer to the root directory
   */
  public void toRoot() {
    cur = root;
  }

  /**
   * Get a {@link File} by path
   * 
   * @param p Path to the file
   * @return The file
   */
  public File getFile(Path p) {
    Node n = getByPath(p);
    if (n.isFile()) {
      return ((FileNode) n).getFile();
    }
    // TODO raise error
    return null;
  }

  /**
   * Append a {@link DirectoryNode} by given path.
   * 
   * @param path Path of the newly create node
   */
  public void append(Path p) {
    Node parent = getByPath(p.getParent());
    if (parent.isFile()) {
      // // TODO raise error
    } else {
      ((DirectoryNode) parent).addChild(new DirectoryNode(p.getName(), parent));
    }
  }
  
  /**
   * Copy a {@link Node} to given path
   * 
   * @param n Node
   * @param p Path
   */
  public void copy(Node n, Path p) {
    Node parent = getByPath(p);
    if(parent.isFile()) {
      // TODO raise error
    }
    else {
      if(n.isFile()) {
        Node c = parent.getChild(n.getName());
        if(c == null) {
          ((DirectoryNode)parent).addChild(n);
        }
        else {
          DirectoryNode par = (DirectoryNode)parent;
          par.deleteChild(c);
          par.addChild(n);
        }
      }
      else {
        DirectoryNode par = (DirectoryNode)parent;
        for(Node node : n.getChildren()) {
          if(par.getChild(node.getName()) != null) {
            par.deleteChild(par.getChild(node.getName()));
          }
          par.addChild(node);
        }
      } 
     }
  }

  /**
   * Append a {@link FileNode} by given path.
   * 
   * @param p Path of the newly create node
   */
  public void appendf(Path p) {
    // TODO error checking
    Node parent = getByPath(p.getParent());
    if (parent.isFile()) {
      // TODO raise error
    } else {
      ((DirectoryNode) parent).addChild(new FileNode(p.getName(), parent));
    }
  }

  
/***
 * the method will link the node of item to the goal.
 * @param item
 * @param goal
 */
  public void move(Path item, Path goal) {
    // get the new parent Node
    Node newparent = getByPath(goal);
    // get the old parent Node
    Node oldparent = getByPath(item.getParent());
    // get the item Node(item could be file or directory node)
    Node itemnode = getByPath(item);
    if (newparent.isFile() && itemnode.isFile()) {
      // get the file node which should be deleted, because of overwrite.
      Node removenode = getByPath(goal);
      // delete the item in the old parent.
      ((DirectoryNode) oldparent).deleteChild(itemnode);
      newparent = newparent.getParent();
      // delete the old item since it should be overwritten.
      ((DirectoryNode) newparent).deleteChild(removenode);
      // set the itemnode's parent to the new parent.
      itemnode.setParent(newparent);
      // add the item to the goal path.(item could be file or directory node)
      ((DirectoryNode) newparent).addChild(itemnode);
    }

    else {
      String itemname = itemnode.getName();
      List<Node> children = newparent.getChildren();
      // set a boolean represent whether the item already exist.
      boolean exist = false;
      // create a node will be removed
      Node removenode = null;
      for (Node child : children) {
        if(child.getName().equals(itemname)) {
          exist = true;
          removenode = child;
          break;
        }
      }
      if(!exist) {
        // delete the item in the old parent.
        ((DirectoryNode) oldparent).deleteChild(itemnode);
        // set the itemnode's parent to the new parent.
        itemnode.setParent(newparent);
        // add the item to the goal path.(item could be file or directory node)
        ((DirectoryNode) newparent).addChild(itemnode);
      }
      else {
        // delete the item in the old parent.
        ((DirectoryNode) oldparent).deleteChild(itemnode);
        ((DirectoryNode) newparent).deleteChild(removenode);
        // set the itemnode's parent to the new parent.
        itemnode.setParent(newparent);
        // add the item to the goal path.(item could be file or directory node)
        ((DirectoryNode) newparent).addChild(itemnode);
      }
    }
    
  }
  
  public List<String> findDir(Path p, String name){
    List<String> list = new ArrayList<String>();
    findDirRecur(p, name, list);
    return list;
  }
  
  /**
   * Recursively finding all files with given name
   * @param p Starting path
   * @param name Name that is searching for
   * @return A list of matches files
   */
  public List<String> findFile(Path p, String name) {
    List<String> list = new ArrayList<String>();
    findFileRecur(p, name, list);
    return list;
  }
  
  private void findDirRecur(Path p, String name, List<String> list) {
    Node n = getByPath(p);
    if(n == null) {
      return;
    }
    for(Node node : n.getChildren()) {
      Path path = new Path(p, node.getName());
      if(!node.isFile() && node.getName().equals(name)) {
        list.add(path.toString());
        findDirRecur(path, name, list);
      }
      if(!node.isFile()) {
        findDirRecur(path, name, list);
      }
    }
  }
  
  private void findFileRecur(Path p, String name, List<String> list) {
    Node n = getByPath(p);
    if(n == null) {
      return;
    }
    for(Node node : n.getChildren()) {
      Path path = new Path(p, node.getName());
      if(node.isFile() && node.getName().equals(name)) {
        list.add(path.toString());
      }
      else if(!node.isFile()) {
        findFileRecur(path, name, list);
      }
    }
  }
  
  
  /**
   * Get the tree representation of the Directory
   * @return A string that represents the directory tree structure
   */
  public String tree() {
    StringBuilder sb = new StringBuilder();
    traversal(root, sb, 0);
    return sb.toString();
  }
  
  private void traversal(Node n, StringBuilder sb, int indent) {
    if(n == null)
      return;
    String sindent = "";
    for(int i=0;i<indent;i++) {
      sindent += "\t";
    }
    if(n.isFile()) {
      sb.append(sindent+n.getName()+"\n");
      return;
    }
    if(n.getName().equals("")) {
      sb.append(sindent+"\\"+"\n");
    }
    else {
      sb.append(sindent+n.getName()+"\n");
    }
    for(Node child : n.getChildren()) {
      traversal(child, sb, indent+1);
    }
  }
  
  
  /**
   * Get a list of children by given path
   * 
   * @param p {@link} Path to the directory
   * @return List of {@link Node} can be {@link DirectoryNode} or
   *         {@link FileNode}
   */
  public List<Node> list(Path p) {
    Node n = getByPath(p);
    return n.getChildren();
  }

  /**
   * Get a list of children that current pointer has
   * 
   * @return List of {@link Node} can be {@link DirectoryNode} or
   *         {@link FileNode}
   */
  public List<Node> list() {
    return cur.getChildren();
  }

  /**
   * Get the absolute path of the current pointer, i.e the working directory.
   * The format will be like: /a/b/c, where c is the current working directory.
   * 
   * @return Absolute path of current pointer in {@link Path}
   */
  public Path getCurPath() {
    return reverseTravel(cur);
  }

  /**
   * Get a boolean that tell if directory or file with given path exists in the
   * file system.
   * 
   * @param path {@link Path} to the diretcory/file
   * @return True if does exist, false otherwise
   */
  public boolean isExist(Path p) {
    return getByPath(p) != null;
  }

  /**
   * Get a boolean value that tells if the given path pointing to a file or a
   * directory
   * 
   * @param path {@link Path} to the diretcory/file
   * @return True if it is a file, false otherwise
   */
  public boolean isFile(Path p) {
    return getByPath(p) != null && getByPath(p).isFile();
  }
  
  /**
   * Get a copy of a node with the same tree structure as original node, using
   * deep copy.
   * @param p Path to the node
   * @return A deep copy of the node at given path
   */
  public Node copy(Path p) {
    return copyByNode(getByPath(p));
  }
  
  /*
   * Deep copy Node
   */
  private Node copyByNode(Node n) {
    Node nCopy = n.copy();
    if(n.isFile()) {
      return nCopy;
    }
    else {
      List<Node> children = n.getChildren();
      for(Node child : children) {
        ((DirectoryNode)nCopy).addChild(copyByNode(child));
      }
      return nCopy;
    }
  }


  /*
   * Reverse travel, from a child node to its parent to construct a path.
   */
  private Path reverseTravel(Node n) {
    Node c = n;
    StringBuilder sb = new StringBuilder();
    /*
     * While current node is not null, stores its name and travel backward by
     * accessing the parent
     */
    if (n == root) {
      return new Path("/");
    }
    while (c != null) {
      sb.insert(0, c.getName());
      if (c != root) {
        sb.insert(0, "/");
      }
      c = c.getParent();
    }
    return new Path(sb.toString());
  }

  /*
   * Get DirectoryNode by a path, remember that there is some cases that the
   * path does not exist
   */
  private Node getByPath(Path p) {
    String[] nodeNames = p.toString().split("/");
    // Start searching from root
    Node n = root;
    for (int i = 1; i < nodeNames.length; i++) {
      Node temp = n.getChild(nodeNames[i]);
      if (temp != null) {
        n = temp;
      } else {
        return null;
      }
    }
    return n;
  }

  /**
   * This is a debug method and will be removed. Print the tree from the root
   */
  public void debug() {
    travel(root);
  }

  private void travel(Node n) {
    if (n == null) {
      return;
    }
    if (!n.isFile()) {
      DirectoryNode d = (DirectoryNode) n;
      List<Node> c = d.getChildren();
      for (Node node : c) {
        System.out
            .print(n.getName() + " has child => " + node.getName() + "\t");
      }
      System.out.println();
      for (Node node : c) {
        travel(node);
      }
    }
  }
}
