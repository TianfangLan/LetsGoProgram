package test.jshell.files;

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

import jshell.files.PathPreprocessor;

/**
 * This is a test for {@link PathPreprocessor}. It contains
 * test cases that test three methods in the PathPreprocessor.
 * @author danielxu
 *
 */
class PreprocessorTest {

	@Test
	void test() {
		String p ="/usr////daniel//xu";
		assertEquals("/usr/daniel/xu", PathPreprocessor.trim(p));
		
		p = "////usr/daniel//xu";
		assertEquals("/usr/daniel/xu", PathPreprocessor.trim(p));
		
		p = "/usr/daniel/xu/";
		assertEquals("/usr/daniel/xu", PathPreprocessor.trim(p));
		
		p = "/usr/daniel/xu//////";
		assertEquals("/usr/daniel/xu", PathPreprocessor.trim(p));
		
		p = "/";
		assertEquals("/", PathPreprocessor.trim(p));
		
		p = "//////";
		assertEquals("/", PathPreprocessor.trim(p));
	}
	
	@Test
	void stayTest(){
		String p = "/usr/././././";
		assertEquals("/usr", PathPreprocessor.stay(p));
		
		p = "/usr/./daniel/./xu/.";
		assertEquals("/usr/daniel/xu", PathPreprocessor.stay(p));
		
		p = "/.";
		assertEquals("/", PathPreprocessor.stay(p));
		
		p = "/usr/././././././xu/./././";
		assertEquals("/usr/xu", PathPreprocessor.stay(p));
		
		p = "/././././././.";
		assertEquals("/", PathPreprocessor.stay(p));
	}
	
	@Test
	void parentTest() {
		String p = "/usr/..";
		assertEquals("/", PathPreprocessor.parent(p));
		
		p = "/usr/daniel/../xu/";
		assertEquals("/usr/xu", PathPreprocessor.parent(p));
		
		p = "/usr/daniel/xu/../../..";
		assertEquals("/", PathPreprocessor.parent(p));
		
		p = "/usr/daniel/xu/../..";
		assertEquals("/usr", PathPreprocessor.parent(p));
		
		p = "/usr/daniel/xu/../admin/../../test";
		assertEquals("/usr/test", PathPreprocessor.parent(p));
	}
	
	@Test
	void preTest() {
		String p = "/./usr/..";
		assertEquals("/", PathPreprocessor.preprocessing(p));
		
		p = "/usr/daniel/././../admin/me/..";
		assertEquals("/usr/admin", PathPreprocessor.preprocessing(p));
		
		p = "/usr/./././././../admin";
		assertEquals("/admin", PathPreprocessor.preprocessing(p));
		
		p = "/./usr/../././usr/temp";
		assertEquals("/usr/temp", PathPreprocessor.preprocessing(p));
	}

}
