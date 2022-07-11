all: GarbageCollection CleanerDemo destructable
GarbageCollection: GarbageCollection.java
	javac GarbageCollection.java -Xlint:deprecation
CleanerDemo: CleanerDemo.java
	javac CleanerDemo.java -Xlint:deprecation
destructable: destructable.cpp
	g++ -o destructable destructable.cpp
clean:
	rm -rf *.class
