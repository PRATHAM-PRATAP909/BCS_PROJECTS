#include<stdio.h>
void mergesor(int arr[],int st,int mid,int end){
    int i=st;
    int j=mid+1;
    int p=end-st+1;
    int temp[9999];
    int k=0;
    while(i<=mid&& j<=end){
         if(arr[i]<=arr[j]){
            temp[k++]=arr[i++];
         }
         if(arr[i]>=arr[j]){
            temp[k++]=arr[j++];
         }
    }
    while(i<=mid){
 temp[k++]=arr[i++];
    }while(j<=end){
temp[k++]=arr[j++];
    }
    for(int i=0;i<k;i++){
        arr[i+st]=temp[i];
    }

    
}
void merge(int arr[],int st,int end){
    int mid;
    if(st<end){
    mid=st+(end-st)/2;
    merge(arr,st,mid);
    merge(arr,mid+1,end);
    mergesor(arr,st,mid,end);}
}

int main(){
    int arr[5];
    for(int i=0;i<5;i++){
        scanf("%d",&arr[i]);
    }
    merge(arr,0,4);
    for(int i=0;i<5;i++){
        printf("%d",arr[i]);
    } 

    return 0;
}