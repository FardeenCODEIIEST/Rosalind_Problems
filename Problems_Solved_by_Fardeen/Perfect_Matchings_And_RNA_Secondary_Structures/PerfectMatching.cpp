#include <bits/stdc++.h>

using namespace std;

// Function to calculate factorial
long long factorial(int n) {
    if (n == 0 || n == 1)
        return 1;
    return n * factorial(n - 1);
}

// Function to count the number of perfect matchings
long long countPerfectMatchings(const string &s) {
    // Count the occurrences of A, U, C, and G
    map<char, int> baseCount;
    for (char base : s) {
        baseCount[base]++;
    }

    // Check if the counts of A and U, C and G are the same
    if (baseCount['A'] != baseCount['U'] || baseCount['C'] != baseCount['G']) {
        return 0;
    }

    // Calculate the number of perfect matchings
    long long perfectMatchings = factorial(baseCount['A']) * factorial(baseCount['C']);
    
    return perfectMatchings;
}

int main() {
    string filename = "rosalind_pmch.txt";
    ifstream file(filename);
    string s;
    string line;

    // Reading the RNA string from the file, ignoring any FASTA headers
    while (getline(file, line)) {
        if (line[0] != '>') {
            s += line;
        }
    }

    file.close();

    long long result = countPerfectMatchings(s);
    cout << result << endl;

    return 0;
}

