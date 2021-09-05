package AbstractClass;


public class MyLinkedList implements NodeList {

    private ListItem root = null;

    public MyLinkedList(ListItem root) {
        this.root = root;
    }

    @Override
    public ListItem getRoot() {
        return this.root;
    }

    @Override
    public boolean addItem(ListItem item) {
        // test the current linked list is empty or not
        if (root == null){
            root = item;
            return true;
        } else {
            // traverse the root and find the fitting place for the item
            ListItem currentNode = root;
            while (currentNode != null){
                // compare current node with the new item
                int comparison = currentNode.compareTo(item);
                if (comparison == 0){
                    // there is a same value in the list, exit and return false
                    return false;
                } else if (comparison < 0){
                    if (currentNode.next() != null){
                        // the current node is still smaller than the item and can move to the next item
                        currentNode = currentNode.next();
                    } else {
                        // the current node is the last node, append the node to the end of the list
                        currentNode.setNext(item).setPrevious(currentNode);
                        return true;
                    }
                } else{
                    if (currentNode.previous() != null){
                        // found the right place for the item
                        currentNode.setPrevious(item).setNext(currentNode);
                        item.setPrevious(currentNode.previous()).setNext(item);
                        return true;
                    } else {
                        // when the current node is the root node
                        item.setNext(root);
                        root.setPrevious(item);
                        root = item;
                        return true;
                    }
                }
            }
        }
        return false;
    }

    @Override
    public boolean removeItem(ListItem item) {
        ListItem currentNode = root;
        while (currentNode != null) {
            int comparison = currentNode.compareTo(item);
            if (comparison < 0){
                if (currentNode.next() == null){
                    // the item is not in the list, cannot delete it
                    return false;
                } else {
                    // the current item is smaller than the item, move to the next item
                    currentNode = currentNode.next();
                }
            } else if (comparison > 0){
                // the item is not in the list
                return false;
            } else {
                // when comparison == 0
                if (currentNode.previous() == null){
                    // deleting the root node
                    if (currentNode.next() != null){
                        // change the root then break the link
                        root = currentNode.next();
                        root.previous().setNext(null);
                        root.setPrevious(null);
                    } else {
                        // when currentNode.next() == null
                        // delete the only node in the list
                        root = null;
                    }
                } else {
                    // when the delete item is not the root node
                    if (currentNode.next() == null){
                        // when the item is at the end of the list
                        currentNode.previous().setNext(null);
                        currentNode.setPrevious(null);
                    } else {
                        // when the item is in between 2 nodes
                        currentNode.next().setPrevious(currentNode.previous());
                        currentNode.previous().setNext(currentNode.next());
                        currentNode.setNext(null);
                        currentNode.setPrevious(null);
                    }
                }
                return true;
            }
        }
        return false;
    }

    @Override
    public void traverse(ListItem root) {
        if (root == null) {
            System.out.println("The list is empty");
        } else {
            while (root != null) {
                System.out.println(root.getValue());
                root = root.next();
            }
        }
    }
}