#ifndef GRAPH_H
#define GRAPH_H
#include <vector>
using namespace std;

class Graph{
	private:
		vector<vector<int> > matr;
		int number_vertc;
	public:
		Graph(int = 0);
		Graph(vector<vector<int> >);
		~Graph();
		void setMatrix();
		vector<vector<int> > getMatrix();

		void setNumberVerticles();
		int getNumberVerticles();



		int* bfs(int=0,int=0);


		
		void print_graph();
};
#endif
