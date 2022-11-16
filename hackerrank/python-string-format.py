def print_formatted(number):
    # your code goes here
    bin_len = len(f"{number:b}")
    for row in range(1, number+1, 1):
        hold = f'{row:{bin_len}} {row:{bin_len}o} {row:{bin_len}x} {row:{bin_len}b}'.upper()
        print(hold)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)