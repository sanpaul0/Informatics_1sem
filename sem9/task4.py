class Box:
    def __init__(self, cat=None):
        self.cat = cat
        self.nextcat = None
        self.prevcat = None
        self.index = -1


class LinkedList:
    def __init__(self):
        self.head = None

    def lenLL(self):
        head1 = self.head
        while head1.nextcat is not None:
            head1 = head1.nextcat
        return head1.index + 1

    def addFirstToList(self, newcat):
        if self.head is None:
            newbox = Box(newcat)
            self.head = newbox
            self.head.index = 0

    def addToPosition(self, catIndex, newcat):
        if catIndex == self.lenLL():
            n = self.head
            while n.nextcat is not None:
                n = n.nextcat
            newbox = Box(newcat)
            n.nextcat = newbox
            newbox.nextcat = None
            newbox.index = n.index + 1
            newbox.prevcat = n
        else:
            n = self.head
            while n is not None:
                if n.index == catIndex:
                    break
                n = n.nextcat
            newbox = Box(newcat)
            newbox.nextcat = n
            newbox.index = catIndex
            newbox.prevcat = n.prevcat
            if n.prevcat is not None:
                n.prevcat.nextcat = newbox
            n.prevcat = newbox

            while n is not None:
                n.index += 1
                n = n.nextcat

    def deleteFromList(self, catIndex):
        if catIndex == self.lenLL():
            n = self.head
            while n.nextcat is not None:
                n = n.nextcat
            n.index = None
            n.prevcat.nextcat = None

        else:
            n = self.head
            while n is not None:
                if n.index == catIndex:
                    break
                n = n.nextcat
            n.nextcat.prevcat = n.prevcat
            n.index = None
            n.prevcat.nextcat = n.nextcat
            while n.nextcat is not None:
                n.nextcat.index -= 1
                n = n.nextcat

    def LLprint(self):
        currentCat = self.head
        i = 0
        while currentCat is not None:
            print(str(i) + ": " + str(currentCat.cat))
            i += 1
            currentCat = currentCat.nextcat


list1 = LinkedList()
list1.addFirstToList(1)
list1.lenLL()
list1.addToPosition(1, 1)
list1.addToPosition(2, 2)
list1.addToPosition(3, 3)
list1.addToPosition(4, 4)
list1.addToPosition(5, 5)
# list1.addToPosition(5, 4)
list1.addToPosition(6, 6)
list1.addToPosition(4, 7)
list1.addToPosition(8, 8)
list1.addToPosition(4, 9)
list1.deleteFromList(4)
list1.LLprint()
print(list1.lenLL())
