
def to_string(n, b, convTab='0123456789abcdef'):
    # base case
    if n < b:
        return convTab[n]

    # // -> integer division ; % -> reminder of the division
    return to_string(n // b, b, convTab) + convTab[n % b]



# run example case if script is run from CLI
if __name__ == "__main__":
	print(to_string(1453, 16))  # => 5ad
