#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>

#define fo(i,start,end) for( typeof(start) i = ( start ); i < ( end ); ++ i )
#define fr(i,end) fo( i, 0, ( end ) )
#define fi(a) fr( i, ( a ) )
#define fj(a) fr( j, ( a ) )
#define fk(a) fr( k, ( a ) )
#define mp make_pair
#define pb push_back
#define all(v) (v).begin( ), (v).end( )
#define _(a,b) memset( a, b, sizeof( a ) )
using namespace std;
int ri() { int a; scanf( "%d", &a ); return a; }
double rf() { double a; scanf( "%lf", &a ); return a; }
int rarr[10000];
int* ra(long long arr_size) {
    for(int i=0; i< arr_size; ++i) {
        scanf( "%d", rarr[i] );
    }
    return rarr;
}
char rbuf[100005];
string rs() { scanf( "%s", rbuf ); return rbuf; }
long long rll() { long long a; scanf( "%lld", &a ); return a; }

template <class T> void out( T a, T b ) {
    bool first = true;
    for( T i = a; i != b; ++ i ) {
        if( !first ) printf( " " );
        first = false; cout << i;
    }
    printf( "\n" );
}

template <class T> void outl( T a, T b ) { for( T i = a; i != b; ++ i ) { cout << * i << "\n"; } }
typedef long long ll;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef map<string,int> msi;

int n, m;

int main( )
{
	int i, j, k, t, tt;

	freopen( "input.txt", "r", stdin );
	//freopen( "output.txt", "w", stdout );

	//scanf( "%d\n", &tt );
	tt = ri();
	for( t = 1; t <= tt; ++ t )
	{
		printf( "Case #%d:", t );

        int credit = ri();
        int nuItems = ri();

        int t = 0;
        vi items;

        fi(nuItems) {
            items.push_back (ri());

//            int id = 0; if  (s == "B") id = 1;
//            int q = ni();
//
//            t = max(t, abs(q - lastP[id]) + lastT[id]) + 1;
//            lastP[id] = q;
//            lastT[id] = t;
        }
        fi(all(items)) {
            cout<<items[i];
        };
        //printf(" %d\n", t);
	}

	return 0;
}

