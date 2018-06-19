/*

Code for probability of knight in C++ with same logic used in python gives better runtime

*/
#include<iostream>

using namespace std;

double a[101][101][101];
int n;
int u[]={-2,-2,2,2,-1,-1,1,1};
int v[]={-1,1,-1,1,2,-2,2,-2};

int main(){
    int t,x,y,i,j,k,z,l;
    cin>>t;
    double d;
    while(t--){
        d=0;
        cin>>n>>x>>y>>z;
        if(k=0){
            cout<<1<<endl;
            continue;
        }
        for(i=0;i<n;i++){
            for(j=0;j<n;j++){
                for(k=0;k<=z;k++){
                    a[i][j][k]=0;
                }
            }
        }
        a[x][y][0]=1;
        for(k=0;k<z;k++){
            for(i=0;i<n;i++){
                for(j=0;j<n;j++){
                    for(l=0;l<8;l++){
                     if(u[l]+i<n && u[l]+i>=0 && v[l]+j<n && v[l]+j>=0){
                         a[u[l]+i][v[l]+j][k+1]+=(1/8.0)*a[i][j][k];
                     }   
                    }
                }
            }
        }
         for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                d += a[i][j][z];
        printf("%.6lf\n",d);
    }
    return 0;
}
