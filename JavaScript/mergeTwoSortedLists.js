/*
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
 

Constraints:

The number of nodes in both lists is in the range [0, 50].
-100 <= Node.val <= 100
Both list1 and list2 are sorted in non-decreasing order.


*/

/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} list1
 * @param {ListNode} list2
 * @return {ListNode}
    @param {ListNode} sortedList
 */

list1 = [1, 2, 4],
    list2 = [1, 3, 4]

// var mergeTwoLists = function (l1, l2) {
//     if (!l1) return l2;
//     else if (!l2) return l1;
//     else if (l1.val <= l2.val) {
//         l1.next = mergeTwoLists(l1.next, l2);
//         return l1;
//     } else {
//         l2.next = mergeTwoLists(l1, l2.next);
//         return l2
//     }

// };

// const mergeTwoLists = (list1, list2) => {

//     var sortedList = new ListNode(0, null); 

//     while (list1 && list2)
//     {



//     }
//     if(list1.val <= list2.val)
//     {
//         list1.next = list2.val
//     }
//     else {
//         list1.next = list1.val
//     }



// };



// Ok so how to proceed: 
class ListNode {
    constructor(value, next = null) {
        this.value = value;
        this.next = next;
    }
}

/*

Basically NodeLists type function as a val: "", next "", type thing like a dictionary.
For instance we have the head pointing at the, say, first value. And then we keep iterating trought these values with
either .val (ref to value) or .next (move to next value). This iteration permits us modify each individual pointer
with the statements we want.

*/

var mergeTwoLists = function (list1, list2) {
    var sortedNodeList = new ListNode(0, null); // We basically create a "Head" value pointing at position 0..
    var currentNode = sortedNodeList; // This will be a copy of the NodeList we will end up with sorted.

    while(list1 && list2) //This means while both lists are True (meaning containing any value to iterate being not null) it will keep looping 
    {
        if(list1.val < list2.val) // Check values, if current of first list is less than current of lis2..
        {
            currentNode.next = list1; // ..we add that current value for the future sortedNodeList 
            list1 = list1.next // We jump to the next value for the iteration
        }
        else {
            currentNode.next = list2; // Same as before but to keep the current list2 value in the sortedNodeList
            list2 = list2.next
        }

        currentNode = currentNode.next; // Move pointer to the next iteration
    }
     // At last, we add up the remaining..
    if (currentNode) {
        currentNode.next = list1 || list2;
    }

    return sortedNodeList.next


};


console.log(mergeTwoLists(list1, list2))