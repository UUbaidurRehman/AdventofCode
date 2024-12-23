MOD = 16777216

def next_secret_number(secret):
    """
    Given a current secret number, produce the next secret number
    using the three-step pseudorandom procedure:

      1) Multiply by 64, XOR with secret, then mod 16777216
      2) Floor-divide by 32, XOR with secret, then mod 16777216
      3) Multiply by 2048, XOR with secret, then mod 16777216
    """
    # --- Step 1 ---
    multiplied = secret * 64
    secret ^= multiplied
    secret %= MOD

    # --- Step 2 ---
    divided = secret // 32
    secret ^= divided
    secret %= MOD

    # --- Step 3 ---
    multiplied = secret * 2048
    secret ^= multiplied
    secret %= MOD

    return secret


def get_price_arrays(buyers):
    """
    For each buyer's initial secret, compute:
      - a list of 2001 secret numbers (the initial + 2000 more)
      - then map to prices (last digit)
    Return a list (one element per buyer) of the prices array.
    """
    all_prices = []
    for initial_secret in buyers:
        secrets = [initial_secret]
        s = initial_secret
        # generate 2000 more
        for _ in range(2000):
            s = next_secret_number(s)
            secrets.append(s)
        prices = [x % 10 for x in secrets]  # last digit
        all_prices.append(prices)
    return all_prices


def solve_part_two(filename='input.txt'):
    # Read buyers' initial secrets
    buyers = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                buyers.append(int(line))

    # Get the 2001 prices for each buyer
    all_prices = get_price_arrays(buyers)

    # We will store earliest sell price for each (buyer, pattern_of_4_changes).
    # But we only actually need to store it once per pattern across all buyers:
    # pattern_dict[4-tuple-of-changes] = list of length = number_of_buyers
    # (where each slot is 0 if never occurs, or earliest sell price if it does).
    # Then we can sum up at the end.

    from collections import defaultdict

    # Initialize for each pattern a *list* or *array* to accumulate buyer sells
    # but we don't know patterns beforehand, so we default-dict them.
    # We'll do: pattern_dict[(c1,c2,c3,c4)][b] = sell_price_for_buyer_b
    pattern_dict = defaultdict(lambda: [0]*len(buyers))

    for b_idx, prices in enumerate(all_prices):
        # Compute changes:
        changes = []
        for i in range(len(prices) - 1):
            diff = prices[i+1] - prices[i]
            changes.append(diff)

        # Now find earliest occurrence of each 4-change pattern:
        # We have 2000 changes => can form up to 1997 4-change windows.
        for i in range(len(changes) - 3):
            c1, c2, c3, c4 = changes[i], changes[i+1], changes[i+2], changes[i+3]
            pattern = (c1, c2, c3, c4)
            # If we haven't recorded a sell price for this pattern & this buyer yet:
            if pattern_dict[pattern][b_idx] == 0:
                # The sell price is the price right *after* those 4 changes:
                # changes[i] corresponds to going from prices[i] to prices[i+1],
                # so the 4th change ends at prices[i+4].
                sell_price = prices[i+4]
                pattern_dict[pattern][b_idx] = sell_price
                # We only care about the *earliest* occurrence, so do NOT update again
                # break after we found earliest occurrence?  No, we want earliest occurrence
                # for each pattern, but there are many patterns. Just continue.
                # We'll keep scanning to record earliest occurrences of *other* patterns.

        # Done scanning for that buyer

    # Now we have, for each pattern, an array of length #buyers with that buyer's earliest
    # sell price (or 0 if never occurs). Summing it up gives total bananas for that pattern.
    best_sum = 0
    # (We won't store the best pattern in this puzzle solution, only the best sum.)
    for pattern, buyer_sells in pattern_dict.items():
        total_for_pattern = sum(buyer_sells)
        if total_for_pattern > best_sum:
            best_sum = total_for_pattern

    return best_sum


if __name__ == "__main__":
    answer = solve_part_two("input.txt")
    print(answer)