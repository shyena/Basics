'''#---------------------------------------------------------------------------------------------------------------
Problem:
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21

Constraints:
    -231 <= x <= 231 - 1
'''#---------------------------------------------------------------------------------------------------------------
def reverse1(x):
    """
    :type x: int
    :rtype: int
    """
    if x < 0:
        return -reverse(-x)

    result = 0
    while x:
        result = result * 10 + x % 10
        x = x//10
    return result if result <= 0x7fffffff else 0  # Handle overflow.
    
    # every character of 7fffffff is representing 4 bits in hexadecimal form.
    


''' CPP my solution:
class Solution {
public:
    int reverse(int x) {
        
        bool flag = false;
        if (x<0)        // negate valueof x
        {   flag = true;
                        
            //runtype error converting -2147483648 to - (-2147483648), asking to typecast to an unsigned type
            //converting -2147483647 in int works fine
            if(x==-2147483648) {x =2147483648; }
            else {x=-x;}
        }
        int reversed = 0;
        int rem {0};
        
        while(x>0)
        {   if(will_it_overflow(reversed,flag)) { return 0;}
            rem = x%10;
            reversed = reversed*10 +rem;
            x = x/10;
        }
        
        if (flag) { return -reversed;}
        
        return reversed;
    }   
        private:
            
            bool will_it_overflow(int being_reversed, bool flag)
            {   static const int min {-2147483648};      // input 32-bit x can never be lesser than min
                static const int max {2147483647};       // input 32-bit x can never be greater than min
                
                if (flag)       // if x is negative
                {
                   if (-being_reversed<min/10)
                    {return true; }// means it will overflow in next iteration adding 1 more digit to number being_reversed.
                }
                else            // if else is positive
                {  
                    if(being_reversed>max/10)
                    {return true; }// means it will overflow in next iteration adding 1 more digit to number being_reversed.
                }
                return false;
            }
            
    
};
'''
#---------------------------------------------------------------------------------------------------------------

def reverse2(x):
    """
    :type x: int
    :rtype: int
    """
    s  =  (x > 0) - (x < 0) 
    '''
     works same as python2's cmp(x,0)
     x=-1:   F    -    T       # returns -1
     x= 0:   F    -    F       # returns 0, same for T - T
     x= 1:   T    -    F       # returns 1
    '''
    r = int(repr(s * x)[::-1])
    return s * r * (r < 2 ** 31)
    
#---------------------------------------------------------------------------------------------------------------
