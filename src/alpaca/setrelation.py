"""
setrelation.py
Set Relation
"""

#
# adjlist
# +-----+
# |  [{1, 2, 3, 4}, is_marked, {'a': 1, 'b': 4, 'c': 5}]
# +-----+
# |  [{8, 9}, is_marked, {'a': 2, 'e': 7}]
# +-----+
# | ... 
# +-----+
#

class SetRelationError(Exception):
    pass


class SetRelation:
    def __init__(self, init_set=None):
        self.start = 0
        self.finish = []
        if init_set == None:
            self.adjlist = [[set(), False, {}]]
        else:
            self.adjlist = [[init_set, False, {}]]


    def __contains__(self, in_set):
        for relation in self.adjlist:
            if in_set in relation:
                return True
        return False


    def mark(self, mark_set):
        index = self.__get_index(mark_set)
        if not self.adjlist[index][1]:
            self.adjlist[index][1] = True
        else:
            raise SetRelationError('set is already marked!')


    def get_non_marked(self):
        for relation in self.adjlist:
            if not relation[1]:
                return relation[0]
        raise SetRelationError('all marked')


    def is_all_marked(self):
        for relation in self.adjlist:
            if not relation[1]:
                return False
        return True


    def add_relation(self, src_set, dst_set, r):
        src_index = self.__get_index(src_set)

        dst_index = -1
        if dst_set not in self:
            self.adjlist.append([dst_set, False, {}])
            dst_index = len(self.adjlist) - 1
        else:
            dst_index = self.__get_index(dst_set)

        self.adjlist[src_index][2][r] = dst_index


    def set_finish(self, finish_list):
        flag_list = [False for i in range(len(finish_list))]

        for i in range(len(self.adjlist)):
            for j in range(len(finish_list)):
                if finish_list[j] in self.adjlist[i][0]:
                    flag_list[j] = True
                    if i not in self.finish:
                        self.finish.append(i)

        if False in flag_list:
            raise SetRelationError


    def __get_index(self, s):
        for relation in self.adjlist:
            if relation[0] == s:
                return self.adjlist.index(relation)
        raise SetRelationError('invalid set!')


    def get_relations(self):
        return [[(v, e) for e, v in l[2].items()] for l in self.adjlist]

