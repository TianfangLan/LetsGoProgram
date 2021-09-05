package AbstractClass;


import java.util.List;

public class SearchTree implements NodeList {

    private ListItem root = null;

    public SearchTree(ListItem item) {
        this.root = item;
    }

    @Override
    public ListItem getRoot() {
        return this.root;
    }

    @Override
    public boolean addItem(ListItem item) {
        if (item == null) {
            // if enter nothing return false
            return false;
        }

        // if the tree is empty, then add it to the root of the tree
        if (this.root == null) {
            this.root = item;
            return true;
        } else {
            // when the tree is not empty;
            ListItem currentNode = this.root;
            while (currentNode != null) {
                int comparison = currentNode.compareTo(item);
                // traverse the tree until find the position
                if (comparison < 0) {
                    if (currentNode.next() != null) {
                        // if the current node has the left child then move to the left child
                        currentNode = currentNode.next();
                    } else {
                        // if current node has no left child, append to left
                        currentNode.setNext(item);
                        // return true since the new item is added to the list
                        return true;
                    }
                } else if (comparison > 0) {
                    // when the current node is greater than the input node
                    if (currentNode.previous() != null) {
                        // when the node has the right child then move to the right child
                        currentNode = currentNode.previous();
                    } else {
                        // if the current node has no right child
                        currentNode.setPrevious(item);
                        // return true since the new item is added to the list
                        return true;
                    }
                } else {
                    // when the new item is already in the list, return false and do nothing
                    return false;
                }
            }
        }
        return false;
    }

    @Override
    public boolean removeItem(ListItem item) {
        if (item == null) {
            // if the input item is null, return false
            return false;
        }

        ListItem currentNode = this.root;
        ListItem parentNode = currentNode;
        while (currentNode != null) {
            int comparison = currentNode.compareTo(item);
            if (comparison < 0) {
                // save the current node and move to the right
                parentNode = currentNode;
                // if there is no right node then the loop is over, then return false
                currentNode = currentNode.next();
            } else if (comparison > 0) {
                parentNode = currentNode;
                currentNode = currentNode.previous();
            } else {
                // when the node is found.
                performRemoval(currentNode, parentNode);
                return true;
            }
        }
        return false;
    }

    @Override
    public void traverse(ListItem Root) {
        // in order traverse
        if (Root != null) {
            traverse(Root.previous());
            System.out.println(Root.getValue());
            traverse(Root.next());
        }
    }

    public void preTraverse(ListItem Root) {
        System.out.println(Root.getValue());
        preTraverse(Root.previous());
        preTraverse((Root.next()));
    }

//    public void iterateInorder(ListItem Root) {
//        ListItem currentNode = Root;
//
//    }

    public void postTraverse(ListItem Root) {
        preTraverse(Root.previous());
        preTraverse((Root.next()));
        System.out.println(Root.getValue());
    }




    private void performRemoval(ListItem item, ListItem parent) {
        if (item.next() == null) {
            // when there is no right tree, directly add the left tree to the parent (could be null)
            if (parent.next() == item) {
                // if the item is parent's right child
                parent.setNext(item.previous());
            } else if (parent.previous() == item) {
                // if the item is parent's left child
                parent.setPrevious(item.previous());
            } else {
                // parent must be the item, which means we were looking at the root of tree.
                this.root = item.previous();
            }
        } else if (item.previous() == null) {
            // no left tree, so make parent point to right tree (which may be null)
            if (parent.next() == item) {
                // item is right child of its parent
                parent.setNext(item.next());
            } else if (parent.previous() == item) {
                // item is left child of its parent
                parent.setPrevious(item.next());
            } else {
                // again, we are deleting the root
                this.root = item.next();
            }
        } else {
            // when neither right sub-tree or left sub tree is null
            // From the right sub-tree, find the smallest value (i.e, the leftmost)
            ListItem current = item.next();
            ListItem leftmostParent = item;
            while (current != null) {
                item = current;
                current = current.previous();
            }
            // put the smallest value into the node to be deleted
            item.setValue(current.getValue());
            // delete the smallest
            if (leftmostParent == item) {
                // there was no leftmost node, so 'current' points to the smallest
                // node (the one that must now be deleted).
                item.setNext(current.next());
            } else {
                // set the smallest node's parent to point to
                // the smallest node's right child (which may be null).
                leftmostParent.setPrevious(current.next());
            }
        }
    }
}
