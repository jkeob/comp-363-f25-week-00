min_heapTree = []
element_counter = 0

def add(text: str) -> None:
    global element_counter
    min_heapTree.append(text)
    element_counter += 1
    if(element_counter>1):
        restore_afterAdd(element_counter - 1)
    

def return_element_count() -> int:
    return element_counter

def remove_return() -> str | None:
    global element_counter
    if element_counter == 0:
        return None
    
    smallest = min_heapTree[0]

    # move last element to the front of the array (after popping)
    lastElement = min_heapTree.pop()
    element_counter -= 1

    if element_counter > 0:
        min_heapTree[0] = lastElement
        restore_afterRemove(0)

    return smallest

def return_smallest() -> str | None:
    # safe when heap is empty
    return None if element_counter == 0 else min_heapTree[0]

def restore_afterAdd(child_index: int) -> None:
    #to make sure it doesn't go past 0
    if child_index <= 0:
        return

    #get parent index
    parent_index = parent(child_index)
    
    #swap when child is smaller than parent
    if min_heapTree[child_index] < min_heapTree[parent_index]:
        # swap
        temp = min_heapTree[parent_index]
        min_heapTree[parent_index] = min_heapTree[child_index]
        min_heapTree[child_index] = temp
        # continue from the new position
        restore_afterAdd(parent_index)



def restore_afterRemove(index_observed: int) -> None:
    # recursively shift down:
    # pick smaller child; if child < parent, swap and recurse on that child

    # if index_observed has no left child, it's a leaf
    leftChild = left_child(index_observed)
    if leftChild >= element_counter:
        return

    # compute right child and choose the smaller child
    rightChild = right_child(index_observed)
    smallest_child = leftChild
    if rightChild < element_counter and min_heapTree[rightChild] < min_heapTree[leftChild]:
        smallest_child = rightChild

    # if heap property is violated, swap and continue
    if min_heapTree[smallest_child] < min_heapTree[index_observed]:
        min_heapTree[index_observed], min_heapTree[smallest_child] = min_heapTree[smallest_child], min_heapTree[index_observed]
        # recursion
        restore_afterRemove(smallest_child)

# helpers
def left_child(parent: int) -> int:
    return 2 * parent + 1

def right_child(parent: int) -> int:
    return 2 * (parent + 1)

def parent(child: int) -> int:
    return (child - 1) // 2

def main():
    add("fgd")
    add("dap")
    add("zzz")
    add("abc")
    element_counter2  = return_element_count()
    #print(element_counter2)
    print("heap:", min_heapTree)
    print("min:", return_smallest())
    print("pop:", remove_return())
    print("heap after pop:", min_heapTree)

if __name__ == "__main__":
    main()
