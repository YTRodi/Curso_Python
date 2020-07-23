# --------------------------------------------------- FUNCIONES
def binary_search(numbers,number_to_find,low,high):
    # Si el index bajo es mas grande que el alto, el número no existe.
    if low > high:
        return False

    mid = (low + high) / 2
    mid = round(mid)

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers,number_to_find,low,mid - 1)
    else:
        return binary_search(numbers,number_to_find,mid + 1, high)
    

# --------------------------------------------------- ENTRY POINT
if __name__ == "__main__":

    numbers = [5,2,13,17,33,42,10,7,6,14,22,80]
    numbers.sort()
    #numbers = [1,3,4,5,6,9,10,11,25,27,28,34,36,49,51]
    
    print('B Ú S Q U E D A  B I N A R I A')
    print('Lista: {}'.format(numbers))
    number_to_find = int(input('Ingrese un número: '))

    result = binary_search(numbers,number_to_find,0,len(numbers) - 1) # 3param = índice del array

    if result:
        print('El número SI está en la lista.')
    else:
        print('El número NO está en la lista.')