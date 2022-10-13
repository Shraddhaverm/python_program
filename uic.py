class fusionCreatures(object):
    """Regular Numbers Gen.
    """

    def _init_(self , value=[]):
        self.value = value
        self.ans = len(self.value)
        

    def fusion(self, fus_arr, i):
        color = ['R','G','B']
        color.remove(fus_arr[i])
        color.remove(fus_arr[i+1])
        fus_arr.pop(i)
        fus_arr.pop(i)
        fus_arr.insert(i, color[0])
        return fus_arr
        
        
    def fusionCreatures1(self, arr=None):
        # this method is to find the smallest number of creature in a row after fusion 
        if arr == None:
            arr = self.value
        for i in range (0,len(arr)-1):
            #print(arr)
            if len(arr) == 2 and i >= 1 or len(arr)<2:
                break
            if arr[i] != arr[i+ 1]:
                arr1 = self.fusion(arr, i)
                testlen = self.fusionCreatures1(arr)
                if len(arr) < self.ans:
                    self.ans = len(arr)
        return self.ans