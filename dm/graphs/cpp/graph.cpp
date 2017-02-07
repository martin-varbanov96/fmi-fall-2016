#include "graph.h"
#include <iostream>
using namespace std;
void Graph::print_graph(){
	cout << "----------------------------" << endl;
	for(int i=0;i<number_vertc;i++){
		for(int j=0; j < number_vertc; j++){
			cout << matr[i][j];
			cout << "|";
		}
		cout << "|" << endl; 
	}
}
Graph::Graph(int n){
	number_vertc=n;
	matr.resize(n);
	for(int i=0;i<=n;i++){
		matr[i].resize(n);
	}	
}
Graph::~Graph(){}

