class Roman():
    
    
    def __init__(self, num):
        

        if isinstance(num, str):
            roman_num = globals()[num].num
            self.num = roman_num
        
        else:
            self.num = num
            dig_len = len(str(self.num))
        
            

    
    def __str__(self):
        roman_dict = { 1 : 'I', 2 : 'V', 3 : 'X', 4 : 'L', 5 : 'C', 6 : 'D', 7 : 'M',
                      8 : '(V)', 9 : '(X)', 10 : '(L)', 11 : '(C)', 12 : '(D)', 13 : '(M)'}
        num = self.num
        
       
        if num > 0:
            

            digits = [int(x) for x in str(num)]
            dig_len = len(digits)

         

            roman_num = ""

            
            for i,j in enumerate(digits):
                
                counter = dig_len - 1
    
                if j in range(1,4):
        
                        roman_num = roman_num + (j * roman_dict[dig_len + counter])
              

                elif j == 4:
        
                    roman_num = roman_num + (roman_dict[dig_len + counter]) + (roman_dict[dig_len + counter + 1])
        
                elif j in range(5, 9):

                    m = j - 5
                    roman_num = roman_num + (roman_dict[dig_len + counter + 1]) + (m * (roman_dict[dig_len + counter]))
        
                elif j == 9:
        
                    roman_num = roman_num + (roman_dict[dig_len + counter ]) + (roman_dict[dig_len + counter + 2])
            
            
                dig_len = dig_len - 1
                
            return(roman_num)
        
        else:
                
                
        
                if num == 0: 
                    roman_num = "N"
            
                else:
                    num1 = str(num)
                    final_num = num1[1:]
                    digits = [int(x) for x in str(final_num)]
                    dig_len = len(digits)
                    roman_num = "-"
            
                    for i,j in enumerate(digits):
                        counter = dig_len - 1
                        if j in range(1,4):
                            roman_num = roman_num + (j * roman_dict[dig_len + counter])
                        
                        elif j == 4:
        
                             roman_num = roman_num + (roman_dict[dig_len + counter]) + (roman_dict[dig_len + counter + 1])
        
                        elif j in range(5, 9):
                            m = j - 5
                            roman_num = roman_num + (roman_dict[dig_len + counter + 1]) + (m * (roman_dict[dig_len + counter]))
        
                        elif j == 9:
        
                            roman_num = roman_num + (roman_dict[dig_len + counter ]) + (roman_dict[dig_len + counter + 2])
            
            
                        dig_len = dig_len - 1
                
                return(roman_num)
                
                
    
    def __mul__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num * other.num
            return Roman(res)
        else:
            res = self.num * other
            return Roman(res)
    
    def __truediv__(self, other):
        if type(other).__name__ == "Roman":
            quo = self.num // other.num
            rem = self.num % other.num
        
            return (Roman(quo), Roman(rem))
        else:
            quo = self.num // other
            rem = self.num % other
        
            return (Roman(quo), Roman(rem))
    
    def __floordiv__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num // other.num
            return Roman(res)
        else: 
            res = self.num // other
            return Roman(res)
    
    
    def __sub__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num - other.num
            return Roman(res)
        else:
            res = self.num - other
            return Roman(res)
    
    def __add__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num + other.num
            return Roman(res)
        else:
            res = self.num + other
            return Roman(res)
    
    def __neg__(self):
        
        return Roman(-self.num)
    def __pos__(self):
        
        return Roman(+self.num)
    
    def __pow__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num**other.num
            return Roman(res)
        else:
            res = self.num**other
            return Roman(res)
    
    def __lt__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num < other.num
            return res
        else:
            res = self.num < other
            return res
    
    def __le__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num <= other.num
            return res
        else:
            res = self.num <= other
            return res
    
    def __gt__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num > other.num
            return res
        else:
            res = self.num > other
            return res
    
    def __ge__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num >= other.num
            return res
        else:
            res = self.num >= other
            return res
    
    def __eq__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num == other.num
            return res
        else:
            res = self.num == other
            return res
    
    def __ne__(self, other):
        if type(other).__name__ == "Roman":
            res = self.num != other.num
            return res
        else:
            res = self.num != other
            return res
    
    
    def __repr__(self, *other):
        return "Roman(\'{}\')".format(Roman(self.num))
        
    def gen_rom():
        
        for i in range (0,1001):
            globals()[str(Roman(i))] = Roman(i)
    
    
    
Roman.gen_rom()