#include <bits/stdc++.h>

using namespace std;

int lis(vector<int>&arr,int n)
{
	vector<int>dp(n,1);
	vector<int>hash(n,1);

	for(int i=0;i<n;i++)
	{
		hash[i]=i;
		for(int j=0;j<i;j++)
		{
			if(arr[j]<arr[i]&&1+dp[j]>dp[i])
			{
				dp[i]=1+dp[j];
				hash[i]=j;
			}
		}
	}
    int ans = -1;
    int lastIndex =-1;
    
    for(int i=0; i<=n-1; i++){
        if(dp[i]> ans){
            ans = dp[i];
            lastIndex = i;
        }
    }
    
    vector<int> temp;
    temp.push_back(arr[lastIndex]);
    
    while(hash[lastIndex] != lastIndex){
        lastIndex = hash[lastIndex];
        temp.push_back(arr[lastIndex]);    
    }
    
    // reverse the array 
    reverse(temp.begin(),temp.end());
    
    for(int i=0; i<temp.size(); i++){
        cout<<temp[i]<<" ";
    }
    cout<<"\n";
    
    return ans;
}

int lds(vector<int>&arr,int n)
{
	vector<int>dp(n,1);
	vector<int>hash(n,1);

	for(int i=0;i<n;i++)
	{
		hash[i]=i;
		for(int j=0;j<i;j++)
		{
			if(arr[j]>arr[i]&&1+dp[j]>dp[i])
			{
				dp[i]=1+dp[j];
				hash[i]=j;
			}
		}
	}
    int ans = -1;
    int lastIndex =-1;
    
    for(int i=0; i<=n-1; i++){
        if(dp[i]> ans){
            ans = dp[i];
            lastIndex = i;
        }
    }
    
    vector<int> temp;
    temp.push_back(arr[lastIndex]);
    
    while(hash[lastIndex] != lastIndex){
        lastIndex = hash[lastIndex];
        temp.push_back(arr[lastIndex]);    
    }
    
    // reverse the array 
    reverse(temp.begin(),temp.end());
    
    for(int i=0; i<temp.size(); i++){
        cout<<temp[i]<<" ";
    }
    cout<<"\n";
    
    return ans;
}


int main(int argc,char*argv[])
{
	freopen(argv[1],"r",stdin);
	int n;
	cin>>n;
	vector<int>arr(n);
	for(int i=0;i<n;i++)
	{
		cin>>arr[i];
	}
	
	lis(arr,n);
	lds(arr,n);

	return 0;
}
