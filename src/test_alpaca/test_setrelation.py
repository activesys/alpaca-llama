"""
test_setrelation.py
unittesting for SetRelation
"""

import unittest
from alpacalib.setrelation import SetRelation
from alpacalib.setrelation import SetRelationError

class TestSetRelation(unittest.TestCase):
    def test_init(self):
        self.relation = SetRelation({1, 2, 3, 4})
        self.assertEqual((self.relation.start, self.relation.finish, len(self.relation.adjlist)), (0, [], 1))
        self.assertEqual(self.relation.adjlist[self.relation.start], [{1, 2, 3, 4}, False, {}])

    def test_init_none(self):
        self.relation = SetRelation()
        self.assertEqual((self.relation.start, self.relation.finish, len(self.relation.adjlist)), (0, [], 1))
        self.assertEqual(self.relation.adjlist[self.relation.start], [set(), False, {}])

    def test_in_true(self):
        self.relation = SetRelation({1, 2, 3})
        self.assertTrue({1, 2, 3} in self.relation)
    def test_in_false(self):
        self.relation = SetRelation({1, 2, 3})
        self.assertFalse({2, 3} in self.relation)

    def test_mark(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.mark({1, 2, 3})
        self.assertTrue(self.relation.adjlist[0][1])
    def test_mark_error_invalid_set(self):
        self.relation = SetRelation({1, 2, 3})
        self.assertRaises(SetRelationError, self.relation.mark, {1, 2})
    def test_mark_error_is_marked(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.mark({1, 2, 3})
        self.assertRaises(SetRelationError, self.relation.mark, {1, 2, 3})

    def test_get_non_marked(self):
        self.relation = SetRelation({1, 2, 3})
        self.assertEqual(self.relation.get_non_marked(), {1, 2, 3})
    def test_get_non_marked_error(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.mark({1, 2, 3})
        self.assertRaises(SetRelationError, self.relation.get_non_marked)

    def test_is_all_marked_true(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.mark({1, 2, 3})
        self.assertTrue(self.relation.is_all_marked())
    def test_is_all_marked_false(self):
        self.relation = SetRelation({1, 2, 3})
        self.assertFalse(self.relation.is_all_marked())

    def test_get_index(self):
        self.relation = SetRelation({1, 2, 3})
        self.assertEqual(self.relation._SetRelation__get_index({1, 2, 3}), 0)
    def test_get_index_error(self):
        self.relation = SetRelation({1, 2, 3})
        self.assertRaises(SetRelationError, self.relation._SetRelation__get_index, {1, 2})

    def test_add_relation(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.add_relation({1, 2, 3}, {4, 5}, 'a')
        self.relation.add_relation({1, 2, 3}, {7, 8, 9}, 'b')
        self.relation.add_relation({1, 2, 3}, {6}, 'c')
        self.relation.add_relation({4, 5}, {4, 5}, 'a')
        self.relation.add_relation({4, 5}, {7, 8, 9}, 'b')
        self.relation.add_relation({7, 8, 9}, {1, 2, 3}, 'e')
        self.relation.add_relation({7, 8, 9}, {6}, 'f')
        self.assertEqual(len(self.relation.adjlist), 4)
        self.assertEqual(self.relation.adjlist[0], [{1, 2, 3}, False, {'a': 1, 'b': 2, 'c': 3}])
        self.assertEqual(self.relation.adjlist[1], [{4, 5}, False, {'a': 1, 'b': 2}])
        self.assertEqual(self.relation.adjlist[2], [{7, 8, 9}, False, {'e': 0, 'f': 3}])
        self.assertEqual(self.relation.adjlist[3], [{6}, False, {}])
    def test_add_relation_error(self):
        self.relation = SetRelation({1, 2, 3})
        self.assertRaises(SetRelationError, self.relation.add_relation, {1, 2}, {4, 5}, 'a')

    def test_set_finish(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.add_relation({1, 2, 3}, {4, 5}, 'a')
        self.relation.add_relation({1, 2, 3}, {7, 8, 9}, 'b')
        self.relation.add_relation({1, 2, 3}, {6}, 'c')
        self.relation.add_relation({4, 5}, {4, 5}, 'a')
        self.relation.add_relation({4, 5}, {7, 8, 9}, 'b')
        self.relation.add_relation({7, 8, 9}, {1, 2, 3}, 'e')
        self.relation.add_relation({7, 8, 9}, {6}, 'f')
        self.relation.set_finish([1, 3, 6])
        self.assertEqual(self.relation.finish, [0, 3])
    def test_set_finish_all(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.add_relation({1, 2, 3}, {4, 5}, 'a')
        self.relation.add_relation({1, 2, 3}, {7, 8, 9}, 'b')
        self.relation.add_relation({1, 2, 3}, {6}, 'c')
        self.relation.add_relation({4, 5}, {4, 5}, 'a')
        self.relation.add_relation({4, 5}, {7, 8, 9}, 'b')
        self.relation.add_relation({7, 8, 9}, {1, 2, 3}, 'e')
        self.relation.add_relation({7, 8, 9}, {6}, 'f')
        self.relation.set_finish([1, 4, 6, 9])
        self.assertEqual(self.relation.finish, [0, 1, 2, 3])
    def test_set_finish_error(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.add_relation({1, 2, 3}, {4, 5}, 'a')
        self.relation.add_relation({1, 2, 3}, {7, 8, 9}, 'b')
        self.relation.add_relation({1, 2, 3}, {6}, 'c')
        self.relation.add_relation({4, 5}, {4, 5}, 'a')
        self.relation.add_relation({4, 5}, {7, 8, 9}, 'b')
        self.relation.add_relation({7, 8, 9}, {1, 2, 3}, 'e')
        self.relation.add_relation({7, 8, 9}, {6}, 'f')
        self.assertRaises(SetRelationError, self.relation.set_finish, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    def test_get_relations(self):
        self.relation = SetRelation({1, 2, 3})
        self.relation.add_relation({1, 2, 3}, {4, 5}, 'a')
        self.relation.add_relation({1, 2, 3}, {7, 8, 9}, 'b')
        self.relation.add_relation({1, 2, 3}, {6}, 'c')
        self.relation.add_relation({4, 5}, {4, 5}, 'a')
        self.relation.add_relation({4, 5}, {7, 8, 9}, 'b')
        self.relation.add_relation({7, 8, 9}, {1, 2, 3}, 'e')
        self.relation.add_relation({7, 8, 9}, {6}, 'f')
        L = [[(1, 'a'), (2, 'b'), (3, 'c')], [(1, 'a'), (2, 'b')], [(0, 'e'), (3, 'f')], []]
        for l in L:
            l.sort()
        relations = self.relation.get_relations()
        for l in relations:
            l.sort()
        self.assertEqual(relations, L)


