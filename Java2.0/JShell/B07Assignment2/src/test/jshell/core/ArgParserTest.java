package test.jshell.core;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;
import java.util.Map;
import org.junit.jupiter.api.Test;
import jshell.jshellcore.ArgParser;

class ArgParserTest {

  @Test
  void test() {
    String input = "/users/Desktop -type f -name \"xyz\"";
    Map<String, String> map = ArgParser.parse(input, "-type", "-name");
    assertEquals(map.size(), 3);
    assertEquals("/users/Desktop", map.get(""));
    assertEquals("f", map.get("-type"));
    assertEquals("\"xyz\"", map.get("-name"));
    
    input = "   a/b a/c a/d a/e       >> file.txt";
    map = ArgParser.parse(input, ">>", ">", "-r", "-x");
    assertEquals(map.size(), 2);
    assertEquals("a/b a/c a/d a/e", map.get(""));
    assertEquals("file.txt", map.get(">>"));
    assertNull(map.get("-x"));
    
    input = "   a/b a/c a/d a/e    ";
    map = ArgParser.parse(input, ">>", ">", "-r", "-x");
    assertEquals(map.size(), 1);
    assertEquals("a/b a/c a/d a/e", map.get(""));
    assertNull(map.get(">>"));
    assertNull(map.get("-x"));
    
    input = "-type f -name";
    map = ArgParser.parse(input, "-type", "-name");
    assertEquals(2, map.size());
    assertEquals("", map.get(""));
    assertEquals("f", map.get("-type"));
    assertNull(map.get("-name"));
  }

}
