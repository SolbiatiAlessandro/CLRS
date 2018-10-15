"""implementation of disjoin-set forest as in CLRS pg. 508,
Chapter 12 - Data Structures for Disjoint Sets"""


class DisjointSets(object):
    """implementation of disjoint-sets data structure with rooted
    tree forest

    Attributes:
        parent: dict[int] to store parents information
        rank: dict[int] to store ranks for 'union by rank' heuristic
    """
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def make_set(self, elem):
        """make a new set with a single elem

        Args:
            elem: element for the set
        """
        self.parent[elem] = elem
        self.rank[elem] = 0

    def link(self, first, second):
        """merge together two disjoint sets,
        implement union by rank heuristic

        Args:
            first: representative for the first set
            second: representative for the second set
        """
        first_rank, second_rank = self.rank[first], self.rank[second]
        if first_rank > second_rank:
            self.parent[second] = first
        else:
            self.parent[first] = second
            if first_rank == second_rank:
                self.rank[second] = second_rank + 1

    def find_set(self, elem):
        """given an elem of a set, returns its representative
        implements path compression heuristic in a recursive
        fashion

        Args:
            elem: query to find the set
        """
        if elem != self.parent[elem]:
            self.parent[elem] = self.find_set(self.parent[elem])
        return self.parent[elem]

    def union(self, first, second):
        """merge two disjoint sets

        Args:
            first: element from the first set
            second: element from the second set
        """
        first_representative = self.find_set(first)
        second_representative = self.find_set(second)
        self.link(first_representative, second_representative)
