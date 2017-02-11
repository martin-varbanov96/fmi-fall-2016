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
	for(int i=0;i<n;i++){
		matr[i].resize(n);
	}	
}

Graph::Graph(vector<vector<int> > arr){
	number_vertc =arr.size();
	matr.resize(number_vertc);
	 for(int i =0;i<number_vertc;i++){
		matr[i].resize(number_vertc);
		 for(int j=0;j<number_vertc;j++){	
			matr[i][j]=arr[i][j];
		}
	}
}
int* Graph::bfs(int i,int j){
	int var =3;
	int* visited(int arr[],int n){
			
	}
	return &var;

}

Graph::~Graph(){}

