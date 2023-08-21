#include <iostream>
using namespace std;

struct node {
    int data;
    node *next;
};

node *front=NULL;

int enqueue(int data1){
    if(front==NULL){
        node *root=(node *)malloc(sizeof(node));
        root->data=data1;
        root->next=NULL;
        front=root;
    }
    else{
        node *root=(node *)malloc(sizeof (node));
        root->data=data1;
        root->next=front;
        front=root;
    }
}

int dequeue(){
    if(front==NULL){
        cout<< "Empty king !\n";
        return 0;
    }
    node *temp=front;
    front=front->next;
    free(temp);
    return 0;
}

int top(){
    node *index=front;
    cout<<index->data<<" is the top element."<<endl;
    return 0;
}

int isEmpty(){
    if(front==NULL){
        cout<< "Empty king !\n";
        return 0;
    }
    else{
        cout<<"It is not empty bro!\n";
        return 0;
    }
}

int size(){
    int count=0;
    node *index=front;
    while (index!=NULL){
        count+=1;
        index=index->next;
    }
    cout<<count<<" items in the stack.\n";
    return 0;
}
int display(){
    node *index=front;
    while (index!=NULL){
        cout<<index->data<<" ";
        index=index->next;
    }
    cout<<endl;
}
int main() {
    enqueue(5);
    enqueue(8);
    enqueue(14);
    enqueue(19);
    display();
    dequeue();
    display();
    isEmpty();
    size();
    top();

    return 0;
}
