
CODE = "1"


class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __repr__(self):
        return f'Node [{self.value}]'


class Tree:
    def __init__(self):
        self.root = None

    def __iter__(self):
        self.itr_node= self.root
        return self

    def __next__(self, res=None):
        if self.itr_node.value is None:
            StopIteration
            return
        res = {self.itr_node.left: 'left', self.itr_node.right: 'right'}
        return res
    def get_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root)
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    def find_code(self, root, alpha):
        code = ''
        find_way = self.root
        while len(find_way.value[0]) != 1 :

            tmp_list_r = list(find_way.right.value[0])
            tmp_list_l = list(find_way.left.value[0])
            print(tmp_list_r)
            print(tmp_list_l)
            break

            if alpha in tmp_list_r:
                code+='1'
                find_way = find_way.right
                continue
            if alpha in tmp_list_l:
                code+='0'
                find_way = find_way.left
                continue
        return code



    def new_node(self, value):
        return Node(value, None, None)

    def heigth(self, node):
        if node is None:
            return 0
        else:
            left_heigth = self.heigth(node.left)
            right_heigth = self.heigth(node.right)
        if left_heigth > right_heigth:
            return left_heigth + 1
        else:
            return right_heigth + 1

    def print_given_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root, end=' ')
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    def print_level_order(self, root):
        h = self.heigth(root)
        i = 1
        while i <= h:
            self.print_given_level(self.root, i)
            print()
            i += 1

    def get_max_width(self, root):
        max_width = 0
        i = 1
        h = self.heigth(root)
        while i <= h:
            width = self.get_width(root, i)
            if width > max_width:
                max_width = width
            i += 1
        return max_width

    def get_width(self, root, level):
        if root is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return (self.get_width(root.left, level - 1) +
                    self.get_width(root.right, level - 1))


#t.print_level_order(t.root)
#print(f'высота: {t.heigth(t.root)}')
#print(f'ширина: {t.get_max_width(t.root)}')

my_tree= Tree()
my_tree.root = my_tree.new_node(1)
my_tree.root.left = my_tree.new_node(2)
my_tree.root.right = my_tree.new_node(3)
my_tree.root.right.right = my_tree.new_node(4)
my_tree.print_level_order(my_tree.root)
print(my_tree.heigth(my_tree.root))
#print('path to values',my_tree.root.left.value)


import  collections

def haffman_alg(stri):
    my_code = ''
    beeb_tree = Tree()
    sort_list = collections.Counter(list(stri))
    #print(sort_list)
    #print('ff',get_deque(sort_list.most_common()))
    nodes = (get_deque(sort_list.most_common()))
    print('узлы',(nodes))
    first_bra = nodes.popitem()
    beeb_tree.root = beeb_tree.new_node(first_bra()[0])
    beeb_tree.root.left = beeb_tree.new_node(first_bra()[1][0])
    beeb_tree.root.right = beeb_tree.new_node(first_bra()[1][1])

    start_point = beeb_tree.root
    l = 'beeb_tree.root.left'
    r = 'beeb_tree.root.right'
    while len(nodes) != 0 :
        new_bra = nodes.popitem()
        for sign in  new_bra[0][0]:
            h = beeb_tree.heigth(beeb_tree.root)
            i = 1

            if sign in list(start_point.left.value()[0]):
                while i <=h:
                    start_point.left.left = beeb_tree.new_node(new_bra[1][1])
                    start_point.left.right = beeb_tree.new_node(new_bra[1][2])

            elif sign in list(start_point.right.value()[0]):
                start_point.right.left = beeb_tree.new_node(new_bra[1][1])
                start_point.right.right = beeb_tree.new_node(new_bra[1][2])

                i+=1
        if new_bra[0] == start_point.left.value():
            start_point.left.left = beeb_tree.new_node(new_bra[1][1])
            start_point.left.right = beeb_tree.new_node(new_bra[1][2])

            if new_bra2[0] == r.value():
                r += '.right'
                exec(f'{r} = beeb_tree.new_node(new_bra[1])')
                continue
            else:
                continue
        elif new_bra[0] == r.value():
            r +='.right'
            exec(f'{r} = beeb_tree.new_node(new_bra[1])')
        #print(all_nodes)
        exec(f'{l} = beeb_tree.new_node(nodes.pop())')
        exec(f'{r} = beeb_tree.new_node(nodes.pop())')
        l += '.left'
        r += '.right'




    beeb_tree.print_level_order(beeb_tree.root)

    print(beeb_tree.find_code(beeb_tree.root, 'b'))
    print('i am here',CODE)

    return CODE

def get_deque(s_l):
    deq = {}
    while len(s_l) !=1:
        #print(s_l)
        s_l.sort(key= lambda x: x[1], reverse=True)
        #print(s_l)
        r_branch = s_l.pop()
        l_branch = s_l.pop()
        res = ((l_branch[0]+r_branch[0], l_branch[1]+r_branch[1]))
        deq[res]=(l_branch,r_branch)

        s_l.append((l_branch[0]+r_branch[0], l_branch[1]+r_branch[1]))

        deq
    else:
        return deq


def new_try(stri):
    sort_list = collections.Counter(list(stri))
    nodes = (get_deque(sort_list.most_common()))
    code = ''
    for alpha in list(stri):

        code_d = nodes.copy()
        code_alpha = ''
        while len(code_d)!=0:
            tmp = code_d.popitem()[1]
            if alpha in tmp[0][0]:
                code_alpha += '0'
                if len(tmp[0][0]) == 1:
                    break
                continue

            elif alpha in tmp[1][0]:
                code_alpha += '1'
                if len(tmp[1][0]) == 1:
                    break
                continue
        code += code_alpha

    return  code

print(new_try('beep boop beer!'))

# Извините за полынй бардак. Я пытался как мог через дерево, но разбился о его создание из списка или словаря.
# В результате сделал просто через словарь. Хардкод , но вроде работает.
