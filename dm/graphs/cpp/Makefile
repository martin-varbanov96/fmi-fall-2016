output: main.o graph.o
	g++  main.o graph.o -o output
main.o: main.cpp graph.h
	g++ -c main.cpp
graph.o: graph.cpp graph.h
	g++ -c graph.cpp

clean:
	rm *.o
