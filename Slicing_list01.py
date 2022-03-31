def main(numbers):
    """
    A list called numbers is given. Return the items in the odd index.
    Args:
        numbers(list): parameter
    Returns:
        list: return answer.
    """
    return [ numbers[i] for i in range(len(numbers)) if i%2==0]
list1=[1, 2, 3, 4, 5]
print(main(list1))