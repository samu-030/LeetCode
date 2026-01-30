/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int pairSum(ListNode head) {
        ListNode slow = head;
        ListNode fast = head;
        while(fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        ListNode temp = slow;
        ListNode prev = null;
        ListNode next = null;
        while(temp != null){
            next = temp.next;
            temp.next = prev;
            prev = temp;
            temp = next;
        }
        int sum = 0, max = 0;
        ListNode temp1 = head;
        ListNode temp2 = prev;
        while(temp2 != null){
            sum = temp1.val + temp2.val;
            if(sum > max){
                max = sum;
            }
            temp1 = temp1.next;
            temp2 = temp2.next;
        }
        return max;
    }
}