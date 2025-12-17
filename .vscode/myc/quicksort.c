#include<stdio.h>
int partitio(int arr[],int  st,int end){
    int pivot=arr[end-1];
    int temp;
    for(int j=st; j<end;j++){
        if(arr[j]<pivot){
            temp=arr[j];
            arr[j]=arr[st];
            arr[st]=temp;
            st++;
        }
    }
    temp=arr[st];
    arr[st]=arr[end-1];
    arr[end-1]=temp;
    for(int i=0;i<end;i++){
        if(arr[i]==pivot){
            return i;
        }
    }
    return 0;
    
}
void quicksor(int arr[],int st,int end){
       if(st<end){
        int k=partitio(arr,st,end);
    quicksor(arr,st,k);   
    quicksor(arr,k+1,end);  
 }
}
int main(){
    int arr[10];
    for(int i=0;i<10;i++){
        scanf("%d",&arr[i]);
    }
    quicksor(arr,0,10);
    
for(int i=0;i<10;i++){
    printf("%d ",arr[i]);
}
return 0;
}
