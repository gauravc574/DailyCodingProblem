'''
Given an array of integers, return a new array such that each element at index i of 
the new array is the product of all the numbers in the original array except the one 
at i.


For example, if our input was [ 1, 2, 3, 4, 5], the expected output would be [ 120, 
60, 40, 30, 24]. Ifourinputwas [3, 2, 1],theexpectedoutputwouldbe [2, 
3, 6].

'''

def products(nums): 
    # Generate prefix products. 
##    prefix_products = [] 
##    for num in nums: 
##        if prefix_products: 
##            prefix_products.append(prefix_products[-1] * num) 
##        else: 
##            prefix_products.append(num)

        
    # Generate suffix products. 
##    suffix_products = [] 
##    for num in reversed(nums): 
##        if suffix_products: 
##            suffix_products.append(suffix_products[-1] * num) 
##        else: 
##            suffix_products.append(num) 
##            suffix_products = list(reversed(suffix_products))
            
    # Generate result from the product of prefixes and suffixes. 
##    result= [] 
##    for i in range(len(nums)): 
##        if i == 0:
##            result.append(suffix_products[i + 1]) 
##        elif i == len(nums) - 1: 
##            result.append(prefix_products[i - 1]) 
##        else: 
##            result.append( 
##            prefix_products[i - 1] * suffix_products[i + 1] )
##    return result 
    print(len(nums))
    result = []
    for i in nums:
        temp = 1
        counter  = 0
        for j in nums:
            
            if i != j:
                print("before appending ",temp)
                temp *= j
                counter += 1
                print("after multiplying ",temp,)
                if counter == (len(nums)-1):
                    print('inside counter loop' , counter)
                    result.append(temp)
            print("after appending ",temp)
    return result
print(products([ 1, 2, 3, 4, 5]))
