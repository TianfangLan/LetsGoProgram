package test.jshell.files;

import static org.junit.Assert.assertEquals;
import static org.junit.Assert.assertTrue;

import org.junit.jupiter.api.Test;

import jshell.files.DirectoryNode;
import jshell.files.FileNode;

/**
 * This is a test for {@link FileNode}, which tested
 * whether a filenode can properly presents as a node
 * with no children.
 * @author danielxu
 *
 */
class FileNodeTest {

	@Test
	void test() {
		// README.txt file under directory 'root'
		DirectoryNode n = new DirectoryNode("root");
		FileNode f = new FileNode("README.txt", n);
		n.addChild(f);
		
		assertEquals(n, f.getParent());
		assertEquals(f, n.getChild("README.txt"));
		assertTrue(f.isFile());
	}

}
