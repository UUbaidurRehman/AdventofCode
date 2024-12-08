def parse_rules_and_updates(input_data):
    rules_section, updates_section = input_data.strip().split("\n\n")
    rules = []
    for rule in rules_section.split("\n"):
        x, y = map(int, rule.split("|"))
        rules.append((x, y))

    updates = []
    for update in updates_section.split("\n"):
        updates.append(list(map(int, update.split(","))))

    return rules, updates


def is_update_valid(rules, update):
    for x, y in rules:
        if x in update and y in update:
            if update.index(x) > update.index(y):
                return False
    return True


def sort_update_with_rules(rules, update):
    # Create a graph based on the rules
    from collections import defaultdict, deque

    graph = defaultdict(list)
    in_degree = defaultdict(int)

    for x, y in rules:
        if x in update and y in update:
            graph[x].append(y)
            in_degree[y] += 1
            in_degree[x]  # Ensure all nodes are in in_degree

    # Topological Sort
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []

    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    return sorted_update


def middle_page(update):
    mid_idx = len(update) // 2
    return update[mid_idx]


def solve(input_data):
    rules, updates = parse_rules_and_updates(input_data)
    middle_pages_sum = 0

    for update in updates:
        if not is_update_valid(rules, update):
            corrected_update = sort_update_with_rules(rules, update)
            middle_pages_sum += middle_page(corrected_update)

    return middle_pages_sum


with open ("input.txt", "r") as file:
    input_data = file.read()


# Solution
result = solve(input_data)
print("Sum of middle page numbers:", result)
# -------------------------------
# def parse_rules_and_updates(input_data):
#     rules_section, updates_section = input_data.strip().split("\n\n")
#     rules = []
#     for rule in rules_section.split("\n"):
#         x, y = map(int, rule.split("|"))
#         rules.append((x, y))

#     updates = []
#     for update in updates_section.split("\n"):
#         updates.append(list(map(int, update.split(","))))

#     return rules, updates


# def is_update_valid(rules, update):
#     for x, y in rules:
#         if x in update and y in update:
#             if update.index(x) > update.index(y):
#                 return False
#     return True


# def middle_page(update):
#     mid_idx = len(update) // 2
#     return update[mid_idx]


# def solve(input_data):
#     rules, updates = parse_rules_and_updates(input_data)
#     valid_updates = []
#     for update in updates:
#         if is_update_valid(rules, update):
#             valid_updates.append(update)

#     middle_pages_sum = sum(middle_page(update) for update in valid_updates)
#     return middle_pages_sum

# with open ("input.txt", "r") as file:
#     input_data = file.read()


# # Solution
# result = solve(input_data)
# print("Sum of middle page numbers:", result)
