'''
Problem:
Given an integer x, return true if x is a palindrome and false otherwise.


Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

Constraints:

    -231 <= x <= 231 - 1
'''
#------------------------------------------------------------------------------
# Solution:(1/2). My solution. 
# start checking extreme end divisor move both pointers towards center.

from math import log10
class Solution1:
    def isPalindrome(self, x: int) -> bool:
        
        if x <0: return False  # ignore -ve values
        if x==0 : return True
        
        i=0
        j=int(log10(x))   # total_divisor = int(math.log10(number))+1
        if j+1 == 1: return True    # 1 digit number is always palindrome

        x = str(x)
        while(i<j):
            
            if x[i] != x[j]:
                return False
            
            i+=1
            j-=1
            if i==j:
                return True
        return True


'''CPP
class Solution1 
{
    public:
        bool isPalindrome(int x) {
            if(x < 0) {
                return false;
            }
    
            int divisor = 1;
            int left, right;
            
            // to get left number, finding left place. example for x=45,154, divisor would be 10,000 
            while (x / divisor >= 10) {
                divisor = divisor * 10;
            }
            
            
            // compare if left digit == right digit
            while(x>0)
            {
                left = x/divisor;
                right = x % 10;
                x = (x % divisor)/10;
                divisor = divisor/100;
                
                std::cout<<left<<" "<<right<<std::endl;

                if (left != right)
                {
                    return false;
                }
            }
            return true;
        }
};
    
'''        

#------------------------------------------------------------------------------
# Solution:(2/2)
class Solution2:
    "checking if x == reversed or not"
    
    def isPalindrome(self, x):
        if x < 0: return False
            
        actual_number, reverse = x, 0
        rem=0
        while x:
            rem = x % 10
            reverse = reverse * 10 + rem
            x = x // 10

        return actual_number == reverse
    
'''
// Time:  O(logx) = O(1)
// Space: O(1)
// didn't get method: isOverflow()

class Solution2 
{
	public:
		bool isPalindrome(int x) 
		{
			if (x < 0) 
			{ return false;	}
		
			int actual_number = x;
			int reversed = 0;
            int temp =0;
			while (x != 0) 
            {   
                // say x = 1234567899 (with in 31 bit- signed int range)
                // then reversed = 998765432 * 10 +1 to become 9987654321 
                // will overflow MAX possible signed int value 2147483647
                
                if (isOverflow(reversed)) { return false;}
                    
                temp = x % 10;
				reversed = reversed * 10 + temp;
				x = x / 10;
			}
			return actual_number == reversed;
		}
    private:
        bool isOverflow(int q) 
        {
            static const int max_q = numeric_limits<int>::max()/10;
            return q > max_q;
        }
};


int main()
{
	Solution2 s1;
	std::cout << s1.isPalindrome(1234565899);
	
	return 0;
}
/*  compile and run for the first time:
	g++ -std=c++17 main.cpp -o output.exe		
	output   									
*/
'''

#------------------------------------------------------------------------------

