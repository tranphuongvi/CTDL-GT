class Nut:
    def __int__(self,gia_tri):
        self.gia_tri = gia_tri
        self.nut_ke_tiep = None

class DSLienKet:
    def __int__(self):
        self.dau = None
        self.duoi = None

    def __str__(self):
        kq = ''
        stt = 0
        hien_tai = self.dau
        while hien_tai != None:
            stt = stt + 1
            if stt ==0:
                kq = kq +str(hien_tai.gia_tri)
            else:
                kq = kq + '- ' + str(hien_tai.gia_tri)
            hien_tai = hien_tai.nut_ke_tiep
        return kq

    def them_dau(self,gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            nut.nut_ke_tiep = self.dau
            self.dau = nut

    def them_duoi(self, gia_tri):
        nut = Nut(gia_tri)
        if self.dau == None:
            self.dau = nut
            self.duoi = nut
        else:
            self.duoi.nut_ke_tiep = nut
            self.duoi = nut

    def lay_dau(self):
        if self.dau == None:
            return None
        else:
            return self.dau.gia_tri

    def xoa_dau(self):
        if self.dau == self.duoi:
            self.dau = None
            self.duoi = None
        else:
            self.dau = self.dau.nut_ke_tiep
#dslk kép
class Node:
    def __init__(self, data=None, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def add_node(self, data):
        new_node = Node (data)
        if self.head is None:
            self.head = new_node
        else:
            curr_node = self.head
            while curr_node.next:
                curr_node = curr_node.next
            curr_node.next = new_node
            new_node.prev = curr_node
    def print_list(self):
        curr_node = self.head
        while curr_node:
            print (curr_node.data)
            curr_node = curr_node.next
# tạo đối tượng linked list và thêm các nút vào
my_list = LinkedList ( )
my_list.add_node (1)
my_list.add_node (2)
my_list.add_node (3)
# in ra danh sách liên kết kép
my_list.print_list ( )

