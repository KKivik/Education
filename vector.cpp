#include <iostream>
#include <vector>
#include <string>

using namespace std;

class ListNode 
{
public:
    ListNode(int data)
    {
        this->value = data;
        this->prev = nullptr;
        this->next = nullptr;
    }

    void pushBack(int data) {
        ListNode* newNode = new ListNode(data);
        ListNode* head = this;
        while (head->next != nullptr) {
            head = head->next;
        }
        newNode->prev = head;
        head->next = newNode;
    }

    void printList(){
        ListNode* head = this;
        while (head != nullptr) {
            cout << head->value << endl;
            head = head->next;
        }
    }

    void deleteAtIndex(int x) {
        int cnt = 0;
        ListNode* head = this;
        while (head && cnt < x) {
                ++cnt;
                head = head->next;
        }
        if (head) {
            ListNode* nextNode = head->next;
            ListNode* prevNode = head->prev;
            prevNode->next = nextNode;
            if (head->next) {
                nextNode->prev = prevNode;
            }
            delete head;
        }
    }
    
    int value;
    ListNode* prev;
    ListNode* next;
};

int main()
{
    ListNode* head = new ListNode(5);
    head->pushBack(3);
    head->pushBack(10);
    head->deleteAtIndex(1);
    head->printList();
    
    return 0;
}
