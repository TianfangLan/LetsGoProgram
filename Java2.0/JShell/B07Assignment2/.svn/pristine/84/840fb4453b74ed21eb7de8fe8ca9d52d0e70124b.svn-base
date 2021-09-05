package test.jshell.files;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import jshell.files.FileSystem;

/**
 * This is a test for {@link FileSystem}, it contains a
 * real life example, jumping forward and backward between
 * directories, create files or directories by using 
 * relative path or absolute path.
 * @author danielxu
 *
 */
class FileSystemTest {

	@Test
	void test() {
		/*
		 * The following system will produce:
		 *                    ''
		 *          /                       \
		 *        usr     					bin
		 *       /    \				            \
		 *  READ.txt   Assignment               temp
		 *  			\                         \
		 *  			CSCB07					CSCB07
		 *  			 \							\
		 *               test.java					test.java
		 *          
		 */
		FileSystem sys = FileSystem.getSystem();
		sys.clean();
		assertEquals("/", sys.getCur());
		
		// create usr, bin under root
		sys.makeDir("/usr");
		sys.makeDir("bin");
		assertEquals(2, sys.list().length);
		assertEquals("usr", sys.list()[0]);
		assertEquals("bin", sys.list()[1]);
		
		// create READ.txt in usr
		sys.makeFile("usr/READ.txt");
		// create Assignment in usr
		sys.makeDir("/usr/Assignment");
		
		// list
		assertEquals(2, sys.list("usr").length);
		assertEquals("READ.txt", sys.list("usr")[0]);
		assertEquals("Assignment", sys.list("usr")[1]);
		
		// current working at root
		assertEquals("/", sys.getCur());
		
		// change to usr
		sys.change("usr");
		assertEquals("/usr", sys.getCur());
		assertEquals(2, sys.list().length);
		assertEquals("READ.txt", sys.list()[0]);
		assertEquals("Assignment", sys.list()[1]);
		
		// create CSCB07 in Assignment
		sys.makeDir("/usr/Assignment/CSCB07");
		
		// change to Assignment
		sys.change("Assignment");
		assertEquals("/usr/Assignment", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("CSCB07", sys.list()[0]);
		
		// create test.java in CSCB07
		sys.makeFile("CSCB07/test.java");
		
		// change to CSCB07
		sys.change("CSCB07");
		assertEquals("/usr/Assignment/CSCB07", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("test.java", sys.list()[0]);
		
		// back to root
		sys.change("/");
		assertEquals("/", sys.getCur());
		assertEquals(2, sys.list().length);
		assertEquals("usr", sys.list()[0]);
		assertEquals("bin", sys.list()[1]);
		
		// change to bin
		sys.change("bin");
		assertEquals("/bin", sys.getCur());
		
		// create /bin/temp
		sys.makeDir("/bin/temp");
		assertEquals(1, sys.list().length);
		assertEquals("temp", sys.list()[0]);
		
		// create /bin/temp/CSCB07
		sys.makeDir("/bin/temp/CSCB07");
		
		// change to temp/CSCB07
		sys.change("temp/CSCB07");
		assertEquals("/bin/temp/CSCB07", sys.getCur());
		assertEquals(0, sys.list().length);
		
		// create /bin/temp/CSCB07/test.java
		sys.makeFile("/bin/temp/CSCB07/test.java");
		assertEquals(1, sys.list().length);
		assertEquals("test.java", sys.list()[0]);
		
		// jump to /usr/Assignemnt
		sys.change("/usr/Assignment///");
		assertEquals("/usr/Assignment", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("CSCB07", sys.list()[0]);
		
		// list
		assertEquals(1, sys.list("/bin/temp/CSCB07").length);
		assertEquals("test.java", sys.list("/bin/temp/CSCB07")[0]);
		
		sys.clean();
		assertEquals("/", sys.getCur());
		assertEquals(0, sys.list().length);
	}
	
	@Test
	void curLastTest() {
		/*
		 * Produce:
		 * 			''
		 *        /    \
		 *      usr     bin
		 *     /          \
		 *   READ.txt      example.java
		 */
		FileSystem sys = FileSystem.getSystem();
		// remove tests from previous test
		sys.clean();
		
		// create /usr involve .
		sys.makeDir("./usr");
		assertEquals(1, sys.list().length);
		assertEquals("usr", sys.list()[0]);
		
		// create /bin involve more .
		sys.makeDir("/./././bin");
		assertEquals(2, sys.list().length);
		assertEquals("bin", sys.list()[1]);
		
		// change dir involve .
		sys.change("/usr/././././");
		assertEquals("/usr", sys.getCur());
		
		// create READ.txt involve both . and ..
		sys.makeFile("/././usr/../usr/READ.txt");
		assertEquals(1, sys.list().length);
		assertEquals("READ.txt", sys.list()[0]);
		
		// change back to root by ..
		sys.change("..");
		assertEquals("/", sys.getCur());
		
	}
	
	@Test
	void dotsTest() {
		/*
		 * Produce:
		 * 			''
		 *        /    \
		 *      usr     bin
		 *     /          \
		 *   temp        exmaple.java
		 *   /  
		 *  READ.txt    
		 */
		FileSystem sys = FileSystem.getSystem();
		// remove tests from previous test
		sys.clean();
		
		// create /usr, /bin
		sys.makeDir("/usr");
		sys.makeDir("/bin");
				
		// create temp
		sys.makeDir("/usr/.././usr/././temp");
		sys.change("usr");
		assertEquals("/usr", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("temp", sys.list()[0]);
		
		// create READ.txt
		sys.makeFile(".././usr/./temp/../temp/READ.txt");
		sys.change("../usr/temp");
		assertEquals("/usr/temp", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("READ.txt", sys.list()[0]);
		
		// change back to root
		sys.change("../..");
		assertEquals("/", sys.getCur());
		assertEquals(2, sys.list().length);
		assertEquals("usr", sys.list()[0]);
		assertEquals("bin", sys.list()[1]);
		
		// change to bin
		sys.change("/bin/.././bin");
		assertEquals("/bin", sys.getCur());
		assertEquals(0, sys.list().length);
		
		// create example.java
		sys.makeFile("../bin/./example.java");
		assertEquals(1, sys.list().length);
		assertEquals("example.java", sys.list()[0]);
	}
	
	@Test
	void stackTest() {
		/*
		 * Produce:
		 * 			''
		 *        /    \
		 *      usr     bin
		 *     /          \
		 *   temp        exmaple.java
		 *   /  
		 *  READ.txt    
		 */
		FileSystem sys = FileSystem.getSystem();
		// remove tests from previous test
		sys.clean();
		
		// create /usr, /bin
		sys.makeDir("/usr");
		sys.makeDir("/bin");
				
		// create temp
		sys.makeDir("/usr/.././usr/././temp");
		sys.change("usr");
		assertEquals("/usr", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("temp", sys.list()[0]);
		
		// create READ.txt
		sys.makeFile(".././usr/./temp/../temp/READ.txt");
		sys.change("../usr/temp");
		assertEquals("/usr/temp", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("READ.txt", sys.list()[0]);
		
		// change back to root
		sys.change("../..");
		assertEquals("/", sys.getCur());
		assertEquals(2, sys.list().length);
		assertEquals("usr", sys.list()[0]);
		assertEquals("bin", sys.list()[1]);
		
		// change to bin
		sys.change("/bin/.././bin");
		assertEquals("/bin", sys.getCur());
		assertEquals(0, sys.list().length);
		
		// create example.java
		sys.makeFile("../bin/./example.java");
		assertEquals(1, sys.list().length);
		assertEquals("example.java", sys.list()[0]);
		
		// back to root
		sys.change("/");
		assertEquals("/", sys.getCur());
		assertEquals(2, sys.list().length);
		assertEquals("usr", sys.list()[0]);
		assertEquals("bin", sys.list()[1]);
		
		// save root and to usr
		sys.push("usr");
		assertEquals("/usr", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("temp", sys.list()[0]);
		
		// save usr and change to bin
		sys.push("/bin");
		assertEquals("/bin", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("example.java", sys.list()[0]);
		
		// save bin and change to temp
		sys.push("../usr/temp");
		assertEquals("/usr/temp", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("READ.txt", sys.list()[0]);
		
		// pop back to bin
		sys.pop();
		assertEquals("/bin", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("example.java", sys.list()[0]);
		
		// pop back to usr
		sys.pop();
		assertEquals("/usr", sys.getCur());
		assertEquals(1, sys.list().length);
		assertEquals("temp", sys.list()[0]);
		
		// pop back to root
		sys.pop();
		assertEquals(2, sys.list().length);
		assertEquals("usr", sys.list()[0]);
		assertEquals("bin", sys.list()[1]);
	}
	
}
