INSTRUMENTED_JDK_PATH=/home/hawkinsw/code/uc/cs3003/jdk/build/linux-x86_64-server-slowdebug/jdk/bin
all:
	python generate.py
	cd java/ && javac Demo.java
data: all
	cd java/ && ${INSTRUMENTED_JDK_PATH}/java Demo > ../result.csv
clean:
	rm -rf *.class java/*.class java/*.csv
