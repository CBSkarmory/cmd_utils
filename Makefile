CC = gcc
JAVAC = javac

all: Average.class

Average.class:
	$(JAVAC) Average.java
clean:
	\rm -f *.class *~ *.x
