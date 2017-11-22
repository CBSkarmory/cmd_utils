CC = gcc
JC = javac

all: Average.class

Average.class:
	$(JC) Average.java

clean:
	\rm -f *.class *~ *.x
