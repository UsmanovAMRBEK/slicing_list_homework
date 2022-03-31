def main(list1,n):
    """
    A list of several elements is given. Return all elements in reverse order except n elements from the beginning.
    Args:
        list1(list): parameter
        n(int): parameter
    Returns:
        list: return answer.
    """
    return list1[:n-1:-1]

list1=['a', 'b', 'c', 'd', 'e', 'f']  ;n = 3
print(main(list1,n))