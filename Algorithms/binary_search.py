class BinarySearch():

    def search_iterative(self, list, item):
        low = 0
        high = len(list) - 1

        while low <= high:
            mid = (low + high) // 2
            guess = list[mid]
            
            # found the solution
            if guess == item:
                return mid

            # guess too high
            if guess > item:
                high = mid - 1
            # guess too low
            else:
                low = mid + 1
            
        # doesnt exist
        return None
    
    def search_recursive(self, list, low, high, item):
        
        # check base case
        if high >= low:
            mid = (high + low) // 2
            guess = list[mid]

            if guess == item:
                return mid
            
            elif guess > item:
                return self.search_recursive(list, low, mid-1, item)
            
            else:
                return self.search_recursive(list, mid+1, high, item)
        
        else:
            # doesnt exist
            return None

    

if __name__ == "__main__":
    bs = BinarySearch()
    sample_list = [1, 3, 5, 7, 9, 11]

    print(bs.search_iterative(sample_list, 11))
    print(bs.search_recursive(sample_list, 0, 5, 11))