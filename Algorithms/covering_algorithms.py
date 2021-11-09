def max_column(G, mr, mc):
    maxsize = 0
    c = list()
    i = 0
    j = 0
    for k in range(G.num_hedges()):
        if mc[k] == 0:
            e = G.get_hedges()[k]
            a = 0
            for x in e:
                if mr[x] == 0:
                    a = a + 1
            if a > maxsize:
                maxsize = a
                c = e
                j = i
            i = i + 1
    return c, j


def lovasz_stein_covering(G):
    mr = [0 for _ in range(G.num_points())]
    mc = [0 for _ in range(G.num_hedges())]
    num_uncovered = G.num_points()
    C = list()
    while num_uncovered != 0:
        c, i = max_column(G, mr, mc)
        for x in c:
            if mr[x] != 1:
                mr[x] = 1
                num_uncovered = num_uncovered - 1
        mc[i] = 1
        C.append(c)
    return C


"""
Check if the sets in F cover all the points in X.
"""
def is_covered_by(X, F):
    Y = set()
    for f in F:
        Y.add(f)
    return len(Y.intersection(X)) == len(X)


"""
Returns all subsets of X with exactly k elements.
"""
def __k_subset_aux(X, F, k, O):
    if k > 0:
        for i in range(len(F)):
            O.append(F[i])
            __k_subset_aux(X, F[i + 1:], k - 1, O)
            O.pop()
    else:
        if is_covered_by(X, F):
            return O

def optimal_covering(G):
    for subsize in range(1, len(G.num_hedges)):
        return __k_subset_aux(G.get_points(), G.get_hedges, subsize, [])
