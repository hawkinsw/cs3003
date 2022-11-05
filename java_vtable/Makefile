JAVAC=/home/hawkinsw/code/uc/cs3003/jdk/install/bin/javac
JAVA=/home/hawkinsw/code/uc/cs3003/jdk/install/bin/java
all:
	${JAVAC} *.java
run:
	#${JAVA} -Xlog:vtables=trace,class=info Deep
	${JAVA} -Xlog:vtables=trace -Xlog:class*=trace Deep
debug:
	gdb --args ${JAVA} -Xlog:vtables=trace -Xlog:class=info Deep
