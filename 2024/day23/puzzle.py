def solve():
    # 1. Read input and build adjacency list
    adjacency = {}
    with open("input.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            a, b = line.split("-")
            
            # Insert into adjacency dict
            if a not in adjacency:
                adjacency[a] = set()
            if b not in adjacency:
                adjacency[b] = set()
            adjacency[a].add(b)
            adjacency[b].add(a)

    # 2. Find all triangles (sets of 3 computers that are all interconnected)
    # We'll store them as frozensets to avoid duplicates
    triangles = set()
    
    # A quick approach to find triangles:
    # For each node n, look at all pairs of neighbors (x, y).
    # If x and y are also neighbors of each other, then {n, x, y} is a triangle.
    for n in adjacency:
        neighbors = sorted(adjacency[n])
        # We'll consider pairs (x, y) with x < y to avoid double counting
        for i in range(len(neighbors)):
            for j in range(i+1, len(neighbors)):
                x = neighbors[i]
                y = neighbors[j]
                # Check if x and y are also connected
                if y in adjacency[x]:
                    # We have a triangle: n, x, y
                    triangle = frozenset([n, x, y])
                    triangles.add(triangle)

    # 3. Filter those triangles so at least one name starts with 't'
    triangles_with_t = [
        tri for tri in triangles 
        if any(computer.startswith('t') for computer in tri)
    ]

    # 4. Print results
    print("Total number of triangles:", len(triangles))
    print("Number of triangles containing a computer starting with 't':", len(triangles_with_t))

    # If desired, you could also print them out (uncomment if needed):
    # print("All triangles:")
    # for tri in sorted(triangles, key=lambda s: sorted(s)):
    #     print(",".join(sorted(tri)))
    # print()
    # print("Triangles with a 't':")
    # for tri in sorted(triangles_with_t, key=lambda s: sorted(s)):
    #     print(",".join(sorted(tri)))

if __name__ == "__main__":
    solve()