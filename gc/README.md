## Notes

### Java

Documentation on `finalize` being deprecated for removal: [JEP 421](https://openjdk.org/jeps/421).

Documentation on _cleaners_ as the replacement: [Class Cleaner](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/ref/Cleaner.html).

Documentation on how to use 

```Java
static String readFirstLineFromFile(String path) throws IOException {
    try (BufferedReader br =
                   new BufferedReader(new FileReader(path))) {
        return br.readLine();
    }
}
```
(taken from linked page)

in order to specify to Java that it destroy resources immediately: [The Try-with-resources Statement](https://dev.java/learn/exceptions/catching-handling/#try-with-resources).

### Python

Documentation on accessing reference count information: [`sys.getrefcount`](https://docs.python.org/3/library/sys.html#sys.getrefcount).
Documentation on accessing a list of objects that refer to a given object: [`sys.get_referrers`](https://docs.python.org/3/library/gc.html#gc.get_referrers).