package test.jshell.files;

import static org.junit.Assert.assertFalse;
import static org.junit.Assert.assertTrue;
import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNotEquals;
import java.util.List;
import org.junit.jupiter.api.Test;
import jshell.files.Directory;
import jshell.files.DirectoryNode;
import jshell.files.Node;
import jshell.files.Path;
import jshell.files.RelativePath;

/**
 * This is a test for {@link Directory}. It contains following
 * test cases:
 * <ol>
 * <li>Add/Change directories by absolute path</li>
 * <li>Add/Change directories by relative path</li>
 * <li>Add/Change directories by mixing path(either absolute path or relative path)</li>
 * <li>Add/Change directories and files, and listing all files/directories under current pointer</li>
 * </ol>
 * @author danielxu
 *
 */
class DirectoryTest {

	@Test
	void test() {
		/*
		 * The following test case can be described as:
		 * 				''
		 *             /  \
		 *           usr   bin
		 *          /
		 *       daniel
		 */
		// Empty dir only with root
		Directory dir = new Directory();
		
		// empty dir should have absolute path '/'
		assertEquals("/", dir.getCurPath().toString());
		
		Path usr = new Path("/usr");
		Path bin = new Path("/bin");
		Path dan = new Path("/usr/daniel");
		
		// Append usr to root
		dir.append(usr);
		dir.append(bin);
		dir.append(dan);
		
		// change to /usr
		dir.change(usr);
		assertEquals("/usr", dir.getCurPath().toString());
		
		// change to /usr/daniel
		dir.change(dan);
		assertEquals("/usr/daniel", dir.getCurPath().toString());
		
		// back to /usr
		dir.back();
		assertEquals("/usr", dir.getCurPath().toString());
		
		// back to /
		dir.back();
		assertEquals("/", dir.getCurPath().toString());
		
		// change to /bin
		dir.change(bin);
		assertEquals("/bin", dir.getCurPath().toString());
		
		// back to /
		dir.back();
		assertEquals("/", dir.getCurPath().toString());
	}
	
	@Test
	void relativeTest() {
		/*
		 * Same tree as above:
		 * 		 		''
		 *             /  \
		 *           usr   bin
		 *          /
		 *       daniel
		 */
		Directory dir = new Directory();
		
		// Created /usr
		Path usr = new RelativePath(dir.getCurPath(), "usr");
		// Created /bin
		Path bin = new RelativePath(dir.getCurPath(), "bin");
		
		// Add to directory
		dir.append(usr);
		dir.append(bin);
		
		// change to /usr
		dir.change(usr);
		assertEquals("/usr", dir.getCurPath().toString());
		
		// create /usr/daniel
		Path dan = new RelativePath(dir.getCurPath(), "daniel");
		dir.append(dan);
		
		// Change to /usr/daniel
		dir.change(dan);
		assertEquals("/usr/daniel", dir.getCurPath().toString());
		
		// back to /usr
		dir.back();
		assertEquals("/usr", dir.getCurPath().toString());
		
		// back to /
		dir.back();
		assertEquals("/", dir.getCurPath().toString());
		
		// change to /bin
		dir.change(bin);
		assertEquals("/bin", dir.getCurPath().toString());
		
		// back to /
		dir.back();
		assertEquals("/", dir.getCurPath().toString());
	}
	
	@Test
	void mixTest() {
		/*
		 * different tree:
		 * 		 		''
		 *             /  \
		 *           usr   bin
		 *          /		 \
		 *       daniel       xu
		 */
		Directory dir = new Directory();
		
		// Created /usr
		Path usr = new Path("/usr");
		// Created /bin
		Path bin = new RelativePath(dir.getCurPath(), "bin");
		
		// Add to directory
		dir.append(usr);
		dir.append(bin);
		
		// change to /usr
		dir.change(new RelativePath(dir.getCurPath(), "usr"));
		assertEquals("/usr", dir.getCurPath().toString());
		
		
		// create /usr/daniel by absolute path
		dir.append(new Path("/usr/daniel"));
		// change to /usr/daniel by relative path
		dir.change(new RelativePath(dir.getCurPath(), "daniel"));
		assertEquals("/usr/daniel", dir.getCurPath().toString());
		
		// back to /usr
		dir.back();
		assertEquals("/usr", dir.getCurPath().toString());
		
		// back to /
		dir.back();
		assertEquals("/", dir.getCurPath().toString());
		
		// create /bin/xu by relative path
		dir.append(new RelativePath(dir.getCurPath(), "bin/xu"));
		
		// change to '/bin'
		dir.change(bin);
		assertEquals("/bin", dir.getCurPath().toString());
		
		// change to '/bin/xu' by absolute path
		dir.change(new Path("/bin/xu"));
		assertEquals("/bin/xu", dir.getCurPath().toString());
	}
	
	@Test
	void fileAndListTest() {
		/*
		 * See tree:
		 *            	  root
		 *          	/      \
		 *        	  usr	    bin
		 *       	/    \
		 * 	README.txt    temp
		 */
		Directory dir = new Directory();
		
		// usr and bin
		Path usr = new RelativePath(dir.getCurPath(), "usr");
		Path bin = new RelativePath(dir.getCurPath(), "bin");
		// append to directory
		dir.append(usr);
		dir.append(bin);
		
		// create /root/usr/README.txt
		Path read = new RelativePath(dir.getCurPath(), "usr/README.txt");
		dir.appendf(read);
		
		// at '/'
		assertEquals("/", dir.getCurPath().toString());
		
		// create /usr/temp
		Path tem = new Path("/usr/temp");
		dir.append(tem);
		
		// change to /usr/temp
		dir.change(tem);
		assertEquals("/usr/temp", dir.getCurPath().toString());
		
		// back to /usr
		dir.back();
		assertEquals("/usr", dir.getCurPath().toString());
		
		List<Node> children = dir.list();
		// usr has two children, README.txt and temp
		assertEquals(2, children.size());
		for(Node c : children) {
			if(c.getName().equals("temp")) {
				assertFalse(c.isFile());
			}
			if(c.getName().equals("README.txt")){
				assertTrue(c.isFile());
			}
		}
		
		dir.toRoot();
		assertEquals("/", dir.getCurPath().toString());
	}
	
	@Test
	void copyTest() {
	  /*
	   * Tree:
	   *       ''
	   *      /    \
	   *     a      b
	   *             \
	   *              c.txt
	   */
	  Directory dir = new Directory();
	  Path a = new Path("/a");
	  Path b = new Path("/b");
	  Path c = new Path("/b/c.txt");
	  dir.append(a);
	  dir.append(b);
	  dir.appendf(c);
//	  dir.debug();
	  
	  // copy root
	  Node n = dir.copy(new Path("/"));
	  assertEquals(n.getName(), "");
	  assertEquals(n.getChildren().size(), 2);
	  assertEquals(n.getChildren().get(0).getName(), "a");
	  assertEquals(n.getChildren().get(1).getName(), "b");
	  
	  Node cb = n.getChild("b");
	  assertEquals(cb.getChildren().size(), 1);
	  assertEquals(cb.getChildren().get(0).getName(), "c.txt");
	  assertTrue(cb.getChildren().get(0).isFile());
	  
	  // Reference
	  ((DirectoryNode)n).addChild(new DirectoryNode("d", n));
	  assertEquals(n.getChildren().size(), 3);
	  assertEquals(dir.list().size(), 2);
	  
	  dir.copy(cb, a);
	  dir.change(a);
	  assertEquals(dir.list().size(), 1);
//	  dir.debug();
	  assertNotEquals(dir.getFile(new Path("/a/c.txt")),
	       dir.getFile(new Path("/b/c.txt")));
	}
	
	@Test
	void copyExistTest() {
	   /*
       * Tree:
       *        ''
       *      /    \
       *     a      b
       *    /        \
       *   c          c
       *  /            \
       * e              d
       */
	  Directory dir = new Directory();
	  Path a = new Path("/a");
	  Path b = new Path("/b");
	  Path ab = new Path("/a/c");
	  Path bc = new Path("/b/c");
	  Path bcd = new Path("/b/c/d");
	  Path ace = new Path("/a/c/e");
	  dir.append(a);
	  dir.append(b);
	  dir.append(ab);
	  dir.append(bc);
	  dir.append(bcd);
	  dir.append(ace);
//	  dir.debug();
	  
	  Node bCopy = dir.copy(b);
	  assertEquals(bCopy.getChildren().size(), 1);
	  assertEquals(bCopy.getChildren().get(0).getName(), "c");
	  
	  dir.copy(bCopy, a);
//	  dir.debug();
//	  System.out.println(dir.tree());
	}
}
