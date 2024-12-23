def bron_kerbosch(R, P, X, adjacency):
    """
    Bron–Kerbosch algorithm to find maximal cliques.
    R: the current clique (set)
    P: candidates to explore (set)
    X: nodes already excluded (set)
    adjacency: dict of sets, adjacency list for the graph
    """
    # If there are no more candidates (P) and no more exclusions (X),
    # then R is a maximal clique
    if not P and not X:
        yield R
    else:
        # Choose a pivot (pick any node in P ∪ X)
        # Then explore only the nodes in P that are NOT neighbors of that pivot.
        # This is an optimization to reduce branching.
        pivot = next(iter(P.union(X))) if P.union(X) else None
        
        # Explore each node v in P that is not in adjacency[pivot]
        # That is, skip the neighbors of the pivot.
        non_neighbors_of_pivot = P - adjacency[pivot] if pivot else P
        for v in list(non_neighbors_of_pivot):
            # Recurse with R ∪ {v}, restricting P and X to neighbors of v
            yield from bron_kerbosch(
                R.union({v}),
                P.intersection(adjacency[v]),
                X.intersection(adjacency[v]),
                adjacency
            )
            # Move v from P to X (we have explored it)
            P.remove(v)
            X.add(v)

def solve():
    # 1. Parse the input and build an adjacency list
    adjacency = {}
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            a, b = line.split("-")
            if a not in adjacency:
                adjacency[a] = set()
            if b not in adjacency:
                adjacency[b] = set()
            adjacency[a].add(b)
            adjacency[b].add(a)

    # 2. Run the Bron–Kerbosch algorithm to find the largest maximal clique
    largest_clique = set()
    all_nodes = set(adjacency.keys())
    for clique in bron_kerbosch(set(), all_nodes, set(), adjacency):
        if len(clique) > len(largest_clique):
            largest_clique = clique

    # 3. Sort the largest clique alphabetically and create the password
    password = ",".join(sorted(largest_clique))

    # 4. Print the result
    print("Password to get into the LAN party:", password)

if __name__ == "__main__":
    solve()