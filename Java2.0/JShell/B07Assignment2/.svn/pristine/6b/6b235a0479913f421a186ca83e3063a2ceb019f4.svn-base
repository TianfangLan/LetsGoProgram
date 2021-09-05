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
 * A Node represents a node in the directory tree. There
 * are two different kinds of nodes, {@link DirectoryNode} and
 * {@link FileNode}. But they have one common, they both have
 * a properties <code>DirectoryNode parent</code>.
 * @author danielxu
 *
 */
public abstract class Node {
	
	protected String name;
	protected Node parent;
	
	/**
	 * Construct a Node with given parent, which means
	 * this node is a child of the given node.
	 * @param name Name of the directory node
	 * @param parent Parent {@link Node}
	 */
	public Node(String name,  Node parent) {
		this.name = name;
		this.parent = parent;
	}
	
	/**
	 * Get the name of this node.
	 * @return Name of this node
	 */
	public String getName() {
		return name;
	}
	
	/**
	 * Get the parent {@link DirectoryNode} of this node
	 * @return {@link DirectoryNode}
	 */
	public Node getParent() {
		return parent;
	}
	
	/**
	 * Set the name of this node to given name
	 * @param name New name of this node
	 */
	public void setName(String name) {
		this.name = name;
	}
	
	/**
	 * Set the parent of this node to a given node
	 * @param parent {@link DirectoryNode}
	 */
	public void setParent(Node parent) {
		this.parent = parent;
	}
	
	/**
	 * Get a copy of this node
	 * @return A deep copy of this node
	 */
	public abstract Node copy();

	/**
	 * Get a child of this node by name
	 * @param name Name of the child node
	 * @return {@link Node} child node if this node with given name,
	 * null if no child matches
	 */
	public abstract Node getChild(String name);
	
	/**
	 * Get children of this node, return null if there is no
	 * children, if it is a file node
	 * @return List of {@link Node}
	 */
	public abstract List<Node> getChildren();
	
	/**
	 * Get a boolean that tells if this node represents
	 * a file.
	 * @return True if it represents a file, false otherwise
	 */
	public abstract boolean isFile();
	
}
