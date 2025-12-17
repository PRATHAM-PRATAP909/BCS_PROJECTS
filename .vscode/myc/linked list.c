#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
struct point{
    int data;
    struct point *next;
};
struct list{
    struct point *head;
};
void insertk(int data,struct list *hea){
    struct point *newd=(struct point *)malloc(sizeof(struct point));
    if(newd==NULL){
        return;
    }
    newd->data=data;
    newd->next=hea->head;
    hea->head=newd;
}
int search(int data,struct list *head){
    if(head->head==NULL){
        return -1;
    }
    struct point *currnode=head->head;
    int t=-1;
    while(currnode!=NULL&&currnode->data!=data){
            currnode=currnode->next;
    }
    if(currnode!=NULL){
        return 1;
    }
    return -1;
    
}
void traverse(struct list *hea){
    static int  p=0;
    p++;
    struct point *pt=hea->head;
    while(pt!=NULL){
         printf("%d ",pt->data);
         pt=pt->next;
    }
}
void deleter( int k,struct list *hea){
     struct point *pt=hea->head;
     int p=0;
     p=search(k,hea);
     if(pt->data==k){
        hea->head=pt->next;
     }
     if(p==1){
         while(pt->next->data!=k){
            pt=pt->next;
         }
         struct point *kt=pt->next->next;
         pt->next=kt;
         traverse(hea);

     }
     if(p==-1){
        printf("does not exist");
     }


}
int main(){
    struct list *head=(struct list *)malloc(sizeof(struct list));
    head->head=NULL;
    insertk(10,head);
    insertk(11,head);
    insertk(12,head);
    int k=search(13,head);
    printf("%d ",k);
    traverse(head);
    deleter(10,head);
    traverse(head);
    return 0;
 
}