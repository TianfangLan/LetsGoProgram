package test.jshell.files;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertNotEquals;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

import java.util.List;

import org.junit.jupiter.api.Test;

import jshell.files.DirectoryNode;
import jshell.files.Node;

/**
 * Test case for {@link DirectoryNode}. Tested
 * properties and the relation between child
 * and parent.
 * @author danielxu
 *
 */
class DirectoryNodeTest {

	@Test
	void test() {
		DirectoryNode n = new DirectoryNode("root");
		
		// Name compare
		assertEquals(n.getName(), "root");
		
		// Not a file
		assertFalse(n.isFile());
		
		// Parent null
		assertNull(n.getParent());
		
		// No children yet
		assertEquals(n.getChildren().size(), 0);
		
		// No specific child could be found
		assertNull(n.getChild("name"));
		
		// Create new node with n as parent
		DirectoryNode c = new DirectoryNode("child", n);
		n.addChild(c);
		
		// Parent verify
		assertEquals(c.getParent(), n);
		
		// Child verify
		assertEquals(n.getChild("child"), c);
		
		// Children size
		List<Node> children = n.getChildren();
		assertEquals(1, children.size());
		
		for(int i=0;i<children.size();i++) {
			assertEquals(children.get(i), c);
		}
				
	}
	
	@Test
	void copyTest() {
	  DirectoryNode n = new DirectoryNode("root");
	  DirectoryNode c1 = new DirectoryNode("child");
	  DirectoryNode c2 = new DirectoryNode("child2");
	  n.addChild(c1);
	  n.addChild(c2);
	  
	  DirectoryNode nc = n.copy();
	  assertNotEquals(n, nc);
	  assertEquals(n.getName(), nc.getName());
	  
	  DirectoryNode cn1 = c1.copy();
	  assertNotEquals(cn1, c1);
	  assertEquals(cn1.getName(), c1.getName());
	  assertNull(cn1.getParent());
	}

}
