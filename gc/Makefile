JAVAC=/home/hawkinsw/code/uc/cs3003/jdk/install/bin/javac
JAVA=/home/hawkinsw/code/uc/cs3003/jdk/install/bin/java
all: GarbageCollection CleanerDemo destructable
GarbageCollection: GarbageCollection.java
	${JAVAC} GarbageCollection.java -Xlint:deprecation
CleanerDemo: CleanerDemo.java
	${JAVAC} CleanerDemo.java -Xlint:deprecation
RunCleanerDemo: CleanerDemo
	${JAVA} -XX:+UseParallelGC -Xlog:gc=trace CleanerDemo
DebugCleanerDemo: CleanerDemo
	gdb --args ${JAVA} -XX:+UseParallelGC -Xlog:gc=trace CleanerDemo
Simple: Simple.java
	${JAVAC} Simple.java -Xlint:deprecation
RunSimple: Simple
	${JAVA} -XX:+UseParallelGC -Xlog:gc=trace Simple
DebugSimple: Simple
	gdb --args ${JAVA} -XX:+UseParallelGC -Xlog:gc=trace Simple
RunGarbageCollection: GarbageCollection
	${JAVA} GarbageCollection
destructable: destructable.cpp
	g++ -o destructable destructable.cpp
clean:
	rm -rf *.class destructable
