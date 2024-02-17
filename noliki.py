def remove_zeroes(numbers: list[int]) -> int:
    non_zeros_count = 0

    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[non_zeros_count], numbers[i] = numbers[i], numbers[non_zeros_count]
            non_zeros_count += 1

    return non_zeros_count


nums = [0,  2, 10, 7, 1, 9,  5,  11]
new_len = remove_zeroes(nums)

assert new_len == 7