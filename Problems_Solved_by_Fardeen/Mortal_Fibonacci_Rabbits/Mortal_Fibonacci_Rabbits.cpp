#include <bits/stdc++.h>

using namespace std;

long long mortal_fibonacci_rabbits(int n, int m) {
    vector<long long> rabbits={1,1};
    
    int i = 2;
    while(i<n)
    {
	if(i<m)
	{
		rabbits.push_back(rabbits[i-2]+rabbits[i-1]);
	}
	else if(i==m||i==m+1)
	{
		rabbits.push_back(rabbits[i-2]+rabbits[i-1]-1);
	}
	else
	{
		rabbits.push_back(rabbits[i-2]+rabbits[i-1]-rabbits[i-m-1]);
	}
	i++;
    }
    return rabbits.back();
}

int main(int argc,char* argv[]) {
    freopen(argv[1],"r",stdin);
    int n,m;
    cin>>n>>m;
    long long result = mortal_fibonacci_rabbits(n, m);
    cout << result << endl;

    return 0;
}

