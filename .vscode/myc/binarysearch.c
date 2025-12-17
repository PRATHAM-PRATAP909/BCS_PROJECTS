#include <stdio.h>
int bsearch(int a[],int key,int st,int end){
    int left,mid,right;
    int found=0;
    right=end-1;
    if((left<=right)&&found==0){
        mid=(left+right)/2;}
        if(a[mid]==key){
            return mid;
        }
        if(a[mid]>key){
            end=mid-1;
            bsearch(a,key,st,end);
        }
        if(a[mid]<key){
            st=mid+1;
            bsearch(a,key,st,end);

    }
    printf("%d",mid);
    return -1;
}
int main(){
    int key;
    int n;
    int a[10];
    scanf("%d",&key);
    for(int i=0;i<10;i++){
        scanf("%d",&a[i]);
    }
    int m;
    m= bsearch(a,key,0,10);
    printf("%d",m);
}