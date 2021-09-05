package test.jshell.files;

import static org.junit.Assert.assertEquals;

import org.junit.jupiter.api.Test;

import jshell.files.Path;

/**
 * This is the test case for {@link Path}. It tested the
 * properties of path.
 * @author danielxu
 *
 */
class PathTest {

	@Test
	void test() {
		Path p = new Path("/usr/daniel/me");
		Path p2 = new Path(p, "bin");
		
		// Path compare
		assertEquals("/usr/daniel/me", p.toString());
		assertEquals("/usr/daniel/me/bin", p2.toString());
		
		// Name compare
		assertEquals("me", p.getName());
		assertEquals("bin", p2.getName());
		
		// Parent path
		assertEquals("/usr/daniel/me", p2.getParent().toString());
		assertEquals("/usr/daniel", p.getParent().toString());
		
		// Parent name
		assertEquals("daniel", p.getParent().getName());
		assertEquals("me", p2.getParent().getName());
		
		// Edge cases
		Path root = new Path("/");
		Path child = new Path(root, "usr/daniel");
		
		// Parent path
		assertEquals("", root.getName());
		assertEquals("daniel", child.getName());
		
		// Path compare
		assertEquals("/usr/daniel", child.toString());
	}

}
