#include "graph.h"
#include <iostream>
#include <vector>
using namespace std;

int main(){
	cout << "ahdhasd" << endl;
	Graph b(5);
  	b.print_graph();
		



	vector<vector<int> > v(3);
	for(int i =0;i<=3;i++){
		v[i].resize(3);
	}
	
	v[0]={2,3,1};
	
	v[1]={5,1,7};
	v[2]={7,1,9};
	for(int i = 0; i<3;i++){
		for(int j = 0; j < 3; j++){
			cout << v[i][j]  << endl;
		}
	}
	Graph c(v);
	c.print_graph();
	return 0;
}

