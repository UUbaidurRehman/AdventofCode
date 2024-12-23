def next_secret_number(secret):
    """
    Given a current secret number, produce the next secret number
    using the three-step pseudorandom procedure:

      1) Multiply by 64, XOR with secret, then mod 16777216
      2) Floor-divide by 32, XOR with secret, then mod 16777216
      3) Multiply by 2048, XOR with secret, then mod 16777216
    """
    # --- Step 1 ---
    # multiply by 64
    multiplied = secret * 64
    # mix (XOR)
    secret ^= multiplied
    # prune (mod 16777216)
    secret %= 16777216

    # --- Step 2 ---
    # integer divide by 32
    divided = secret // 32
    # mix (XOR)
    secret ^= divided
    # prune (mod 16777216)
    secret %= 16777216

    # --- Step 3 ---
    # multiply by 2048
    multiplied = secret * 2048
    # mix (XOR)
    secret ^= multiplied
    # prune (mod 16777216)
    secret %= 16777216

    return secret


def secret_after_n_steps(initial_secret, n):
    """ Compute the nth secret number starting from `initial_secret`. """
    secret = initial_secret
    for _ in range(n):
        secret = next_secret_number(secret)
    return secret


def main():
    buyers = []
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            if line:  # skip empty lines just in case
                buyers.append(int(line))

    # For each buyer, we want to compute the 2000th new secret number.
    # Note: "2000th new secret number" means applying the transformation 2000 times
    # starting from the given initial secret.
    total = 0
    for initial_secret in buyers:
        secret_2000 = secret_after_n_steps(initial_secret, 2000)
        total += secret_2000

    print(total)


if __name__ == "__main__":
    main()