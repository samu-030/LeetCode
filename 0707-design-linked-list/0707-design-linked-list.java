class MyLinkedList {
    Node head, tail;
    int size = 0;
    
    public class Node{
        int data;
        Node next;
        Node prev;
        Node(int value){
            data = value;
            next = null;
            prev = null;
        }
    }

    public MyLinkedList() {
        head = null;
        tail = null;
    }
    
    public int get(int index) {
        if(index < 0 || index >= size){
            return -1;
        }
        Node temp = head;
        for(int i = 0; i < index; i++){
            temp = temp.next;
        }
        return temp.data;
    }
    
    public void addAtHead(int val) {
        Node newNode = new Node(val);
        if(head == null){
            head = newNode;
            tail = newNode;
        }else{
            newNode.next = head;
            head.prev = newNode;
            head = newNode;
        }
        size++;
    }
    
    public void addAtTail(int val) {
        Node newNode = new Node(val);
        if(head == null){
            head = newNode;
            tail = newNode;
        }else{
            tail.next = newNode;
            newNode.prev = tail;
            tail = newNode;
        }
        size++;
    }
    
    public void addAtIndex(int index, int val) {
        if(index < 0 || index > size){
            return;
        }
        if(index == 0){
            addAtHead(val);
            return;
        }
        if(index == size){
            addAtTail(val);
            return;
        }
        Node temp = head;
        Node newNode = new Node(val);
        for(int i = 0; i < index-1; i++){
            temp = temp.next;
        }
        newNode.next = temp.next;
        temp.next.prev = newNode;
        temp.next = newNode;
        newNode.prev = temp;
        size++;
    }
    
    public void deleteAtIndex(int index) {
        if(index < 0 || index >= size){
            return;
        }
        if(index == 0){
            head = head.next;
            if(size == 1) //if (size == 1){tail = null};
            {
                tail = null;
            }
            size--;
            return;
        }
    
        Node temp = head;
        for(int i = 0; i < index - 1; i++){
            temp = temp.next;
        }
        if(temp.next == tail){
            tail = temp;
        }
        temp.next = temp.next.next;
        size--;
    }        
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */