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

import java.util.LinkedList;
import java.util.List;

/**
 * DirectoryNode is a node that stores a name
 * and has properties <code>name</code>, <code>children</code>
 * and <code>parent</code>. Each {@link Directory}
 * can be represented by a way of walking from root
 * node to a specific node.
 * @author danielxu
 *
 */
public class DirectoryNode extends Node{

	/** A list of childrens(DirectoryNode)**/
	private List<Node> children;
	
	/**
	 * Construct a DirectoryNode with no parent given, which
	 * will be represented by <b>null</b>
	 * @param name Name of the directory node
	 */
	public DirectoryNode(String name) {
		this(name, null);
	}
	
	/**
	 * Construct a DirectoryNode with given parent, which means
	 * this node is a child of the given node.
	 * @param name Name of the directory node
	 * @param parent Parent {@link DirectoryNode}
	 */
	public DirectoryNode(String name, Node parent) {
		super(name, parent);
		children = new LinkedList<Node>();
	}
	
	/**
	 * Get a list of children that this node has, if there
	 * is no child, the return list will have size 0
	 * @return List of children {@link DirectoryNode}
	 */
	public List<Node> getChildren(){
		return children;
	}
	
	/**
	 * Get a {@link DirectoryNode} that is a child of this
	 * node by name. If there is no such node that matches
	 * the given name, return <b>null</b>
	 * @param name Name of the child node that is being looking for
	 * @return {@link DirectoryNode} if the given name can be found
	 * or null if it does not exist
	 */
	public Node getChild(String name) {
		for(Node node : children) {
			if(node.getName().equals(name)) {
				return node;
			}
		}
		return null;
	}
	
	/**
	 * Add a child node to this node
	 * @param node {@link DirectoryNode}
	 */
	public void addChild(Node node) {
	    node.setParent(this);
		children.add(node);
	}
	
	@Override
	public DirectoryNode copy() {
	  return new DirectoryNode(name, null);
	}
	
	//new for the mv
	/**
	 * 
	 */
	public void deleteChild(Node node) {
	  children.remove(node);
	}
	
	@Override
	public boolean isFile() {
		return false;
	}
}