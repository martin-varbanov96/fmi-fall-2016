output: main.o graph.o
	g++  main.o graph.o -o output
main.o: main.cpp graph.h
	g++ -std=c++11 -c main.cpp
graph.o: graph.cpp graph.h
	g++ -std=c++11 -c graph.cpp

clean:
	rm *.o
