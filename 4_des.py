SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

PC2 = [
    14, 17, 11, 24,  1,  5,
     3, 28, 15,  6, 21, 10,
    23, 19, 12,  4, 26,  8,
    16,  7, 27, 20, 13,  2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32,
]

def rotate_left(bits: str, n: int) -> str:
    """Circular left shift of a bit string."""
    return bits[n:] + bits[:n]

def permute(bits: str, table: list[int]) -> str:
    return "".join(bits[i - 1] for i in table)

def round_keys(k_plus: str) -> list[str]:
    k_plus = k_plus.replace(" ", "")
    assert len(k_plus) == 56 and set(k_plus) <= {"0", "1"}, "K+ must be 56 bits"

    c, d = k_plus[:28], k_plus[28:]
    keys = []
    for shift in SHIFTS:
        c, d = rotate_left(c, shift), rotate_left(d, shift)
        keys.append(permute(c + d, PC2))
    return keys


def fmt(bits: str, group: int = 6) -> str:
    return " ".join(bits[i:i + group] for i in range(0, len(bits), group))

if __name__ == "__main__":
    K_PLUS = input("Enter a valid 56-bit key:\n")

    # 1111000 0110011 0010101 0101111 0101010 1011001 1001111 0001111

    for i, k in enumerate(round_keys(K_PLUS), start=1):
        print(f"K{i:<2} = {fmt(k)}")
