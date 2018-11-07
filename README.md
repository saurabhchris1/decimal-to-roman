This homework will test your ability to make use of Python’s objects and magic methods. Think before you code: A bad design will waste your time and lead to buggy and hard-to-test code.

Reminder: This assignment is to be your own work. You are not to “borrow” code from any source apart from the textbook.
**1. [ 100 points ] Implement a class Roman in a module roman.py that adds Roman numeral functionality to Python. The basic digits are:**

**numeral      decimal equivalent**

    I            1 
    V            5    
    X            10    
    L            50    
    C            100   
    D            500   
    M            1000


**In addition, a bar could be put over or parentheses put around any of these except I that would multiply it by 1000. Using the latter, we have:**

 **numeral      decimal equivalent**
 
    (V)            5000
    (X)            10000
    (L)            50000
    (C)            100000
    (D)            500000
    (M)            1000000
  
**There are specific rules for how to turn any positive integer up to several million into roman numerals. For example, 37 is XXXVII and 99 is XCIX. If you don’t remember these rules, the Wikipedia article “Roman Numerals” is a good review.**

Roman should implement the following operations:

   ``` x+y     x-y     x*y 
    x/y     x//y    x**y 
    x==y    x!=y    x<y 
    x<=y    x>=y    x>y 
    -x 
  ```
    
    
**Observe these additional constraints:
- The result of any unary arithmetic operation involving a Roman should be a Roman.
- The result of any binary arithmetic operation involving a Roman and an int should be a Roman.
CptS 481, Fall 2018 2 
- (Comparison operations still result in bools, of course.)
- Roman mathematicians did not have negative numbers, but Roman will indicate negative values with a - prefix.
- Roman mathematicians did not have a zero, but Roman will use ’N’ to stand for nulla (“nothing”). Note that N is never a placeholder: It is only used to indicate a value of 0.
- Floor (“//”) division returns a Roman, ignoring the remainder (as it should).
- True (“/”) division returns a tuple of two Romans “(quotient, remainder )”.
- Reuse magic methods wherever possible. E.g., __radd__() should call __add__()
- Values that are too big in absolute value to represent (let’s make it 2000000 or more for convenience), should raise a ValueError exception.
- Roman() should accept a mandatory int argument. Here is an interactive example of the working module:**
```
     >>> from roman import Roman
     >>> III = Roman(3)
     >>> VII = Roman(7)
     >>> print(III)
     III
     >>> III + VII
     Roman(10)
     >>> print(III + VII)
     X
     >>> print(VII + 2)
     IX
 ```
 
**Within the module, instantiate all roman numerals up to and including 1000 (i.e. M) as objects so that this (for instance) works:**

```
     >>> from roman import *
     >>> III*XI + CM*II
     Roman(1833)
```
     
**There’s an easy way to do this (hint: globals()) and a hard way. Credit will not be given for the hard way.
[ +10 pts. extra credit ] Make the constructor Roman() also accept a legal roman numeral (as a str) and convert it for use internally. (Any illegal roman numeral string should raise an exception of your own design.) Also make this the default display format for the __repr__() method. This would make the line in the above example:**
```
     >>> III + VII
     Roman(’X’)
```

Evaluation:

Homework #03 Evaluation: Saurabh Jaiswal



Test Results:

1. Roman(int) Comparison
------------------------

Roman(int)      str() result               expected                   okay?  repr() result                       
--------------  -------------------------  -------------------------  -----  ----------------------------------  
Roman(0)        N                          N                          yes    Roman('N')                          
Roman(1)        I                          I                          yes    Roman('I')                          
Roman(5)        V                          V                          yes    Roman('V')                          
Roman(9)        IX                         IX                         yes    Roman('IX')                         
Roman(10)       X                          X                          yes    Roman('X')                          
Roman(14)       XIV                        XIV                        yes    Roman('XIV')                        
Roman(50)       L                          L                          yes    Roman('L')                          
Roman(100)      C                          C                          yes    Roman('C')                          
Roman(500)      D                          D                          yes    Roman('D')                          
Roman(1000)     M                          M                          yes    Roman('M')                          
Roman(2037)     MMXXXVII                   MMXXXVII                   yes    Roman('MMXXXVII')                   
Roman(5000)     (V)                        (V)                        yes    Roman('(V)')                        
Roman(10000)    (X)                        (X)                        yes    Roman('(X)')                        
Roman(50000)    (L)                        (L)                        yes    Roman('(L)')                        
Roman(100000)   (C)                        (C)                        yes    Roman('(C)')                        
Roman(300157)   (C)(C)(C)CLVII             (C)(C)(C)CLVII             yes    Roman('(C)(C)(C)CLVII')             
Roman(500000)   (D)                        (D)                        yes    Roman('(D)')                        
Roman(1000000)  (M)                        (M)                        yes    Roman('(M)')                        
Roman(1999999)  (M)(C)(M)(X)(C)M(X)CMXCIX  (M)(C)(M)(X)(C)M(X)CMXCIX  yes    Roman('(M)(C)(M)(X)(C)M(X)CMXCIX')  


2. Built-In Values
------------------

symbol  got    okay?  
------  -----  -----  
I       I      yes    
XII     XII    yes    
CXIII   CXIII  yes    
DLIV    DLIV   yes    


3. Expressions
--------------

expression             non-Roman result    got                            okay?                   
---------------------  ------------------  -----------------------------  ----------------------  
Roman(98) + Roman(3)   101                 CI                             (determined by grader)  
Roman(98) + 3          101                 CI                             (determined by grader)  
98 + Roman(3)          101                 (TypeError raised)             no                      
Roman(98) - Roman(3)   95                  XCV                            (determined by grader)  
Roman(98) - 3          95                  XCV                            (determined by grader)  
98 - Roman(3)          95                  (TypeError raised)             no                      
Roman(98) * Roman(3)   294                 CCXCIV                         (determined by grader)  
Roman(98) * 3          294                 CCXCIV                         (determined by grader)  
98 * Roman(3)          294                 (TypeError raised)             no                      
Roman(98) / Roman(3)   32.666666666666664  (Roman('XXXII'), Roman('II'))  (determined by grader)  
Roman(98) / 3          32.666666666666664  (Roman('XXXII'), Roman('II'))  (determined by grader)  
98 / Roman(3)          32.666666666666664  (TypeError raised)             no                      
Roman(98) // Roman(3)  32                  XXXII                          (determined by grader)  
Roman(98) // 3         32                  XXXII                          (determined by grader)  
98 // Roman(3)         32                  (TypeError raised)             no                      
Roman(98) ** Roman(3)  941192              (C)(M)(X)(L)MCXCII             (determined by grader)  
Roman(98) ** 3         941192              (C)(M)(X)(L)MCXCII             (determined by grader)  
98 ** Roman(3)         941192              (TypeError raised)             no                      
Roman(98) == Roman(3)  False               False                          yes                     
Roman(98) == 3         False               False                          yes                     
98 == Roman(3)         False               False                          yes                     
Roman(98) != Roman(3)  True                True                           yes                     
Roman(98) != 3         True                True                           yes                     
98 != Roman(3)         True                True                           yes                     
Roman(98) < Roman(3)   False               False                          yes                     
Roman(98) < 3          False               False                          yes                     
98 < Roman(3)          False               False                          yes                     
Roman(98) <= Roman(3)  False               False                          yes                     
Roman(98) <= 3         False               False                          yes                     
98 <= Roman(3)         False               False                          yes                     
Roman(98) >= Roman(3)  True                True                           yes                     
Roman(98) >= 3         True                True                           yes                     
98 >= Roman(3)         True                True                           yes                     
Roman(98) > Roman(3)   True                True                           yes                     
Roman(98) > 3          True                True                           yes                     
98 > Roman(3)          True                True                           yes                     
-Roman(98)             -98                 -XCVIII                        (determined by grader)  


4. Extra Credit
---------------

Roman(str)      got             okay?  
--------------  --------------  -----  
Roman('I')      Roman('I')      yes    
Roman('XII')    Roman('XII')    yes    
Roman('CXIII')  Roman('CXIII')  yes    
Roman('DLIV')   Roman('DLIV')   yes    


