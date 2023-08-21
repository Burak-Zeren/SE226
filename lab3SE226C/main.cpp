#include <iostream>
using namespace std;

struct node {
    int data;
    node *next;
};

node *front=NULL;
node *rear=NULL;

int enqueue(int data1){
    if(front==NULL){
        node *root=(node *)malloc(sizeof(node));
        root->data=data1;
        root->next=NULL;
        front=rear=root;
    }
    else{
     node *root=(node *)malloc(sizeof(node));
     root->data=data1;
     root->next=NULL;
     rear->next=root;
     rear=root;
    }
}

int display(){

    if(front==NULL){
        cout<<"Queue is empty!\n";
        return 0;
    }
    node *index=front;
    cout<<"Linklist : ";
    while (index!=NULL){
        cout<<index->data<<" ";
        index=index->next;
    }
    cout<<endl;
}

int dequeue(){
    if(front==NULL){
        cout<<"Queue is empty!\n";
        return 0;
    }
    node *temp=front;
    front=front->next;
    free(temp);
    return 0;
}

int isEmpty(){
    if(front==NULL){
        return true;
    }
    else{
        return false;
    }
}

int top(){
    if(front==NULL){
        cout<<"Top element does not exits in this queue.."<<endl;
        return 0;
    }
    else{
        cout<<front->data<<" is the top element of this queue."<<endl;
    }
}

int size(){
    node *index=front;
    int count=0;
    while (index!=NULL){
        count+=1;
        index=index->next;
    }
    cout<<"This queue has "<<count<<" items.."<<endl;
    return 0;
}

int main() {
    if(isEmpty()==1){
        cout<<"True it means that queue is empty..\n";
    }
    else{
        cout<<"False it means that queue has value..\n";
    }

    enqueue(5);
    enqueue(10);
    enqueue(7);
    enqueue(54);
    enqueue(17);
    top();
    if(isEmpty()==1){
        cout<<"True it means that queue is empty..\n";
    }
    else{
        cout<<"False it means that queue has value..\n";
    }
    dequeue();
    top();
    display();
    size();
    return 0;
}
