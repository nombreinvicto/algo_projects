def product_of_array(array: list):
    temp_product = array[0]
    if len(array) == 1:
        return temp_product
    else:
        array.pop(0)
        return temp_product * product_of_array(array)

if __name__ == '__main__':
    print(product_of_array([1,2,3]))
    print(product_of_array([1,2,3,10]))
