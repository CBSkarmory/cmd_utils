CC = gcc
JC = javac

all: Average.class

Average.class: Average.java
	$(JC) Average.java

clean:
	\rm -f *.class *~ *.x
