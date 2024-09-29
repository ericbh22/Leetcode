class Solution:
    def isPalindrome(self, s: str) -> bool:
        # #comvert by getting rid of upper and white spaces and any alphanumeric letters
        # #o(n), where n is the number of elements in the string
        # base = s.lower().strip()
        # clean_text = ''.join(char for char in base if char.isalnum()) # need the whitespace at the start and join to make sure its a string and account for empty case
        # p1= 0 
        # p2= len(clean_text)-1
        # for _ in range(len(clean_text)//2):
        #     if clean_text[p1] != clean_text[p2]:
        #         return False
        #     p1+=1
        #     p2-=1
        # return True

        p1 = 0 
        p2 = len(s)-1
        while p1 < p2:
            if s[p1].isalnum() == False:
                p1+=1
                continue 
            elif s[p2].isalnum() == False:
                p2-=1 
                continue 
            elif s[p1].lower() != s[p2].lower():
                return False
            else:
                p1 +=1 
                p2-=1
        return True
