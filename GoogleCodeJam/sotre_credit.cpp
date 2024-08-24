#include<iostream>
#include<stdio.h>
#include<vector>

using namespace std;

#define fo(i,start,end) for( i = ( start ); i < ( end ); ++ i )
#define fr(i,end) fo( i, 0, ( end ) )

#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define ft(a) fr( t, ( a ) )

template <class T> void out( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }

#define ov() out(v.begin(),v.end())

int ri() { int a; cin>>a; return a; }

vector<int> rv(int nElements) {
    vector<int> v;
    int temp;
    for(int i=0;i<nElements; ++i) {
        cin>>temp;
        v.push_back(temp);
    }
    return v;
}

int main() {

    int tt, t;
    vector<int> v;

    freopen( "input.txt", "r", stdin );
    tt = ri();
    ft(tt) {
        cout<<"Case #"<<t<<":";
        int nItems = ri();
        v= rv(nItems);
        ov();


    }
    cin>>t;



}
