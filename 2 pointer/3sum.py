# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]: 
#         sortednums = sorted(nums)
#         answerarray=[]
#         for i in range(len(sortednums)):
#             oneanswer=[]
#             toFind = 0- sortednums[i]
#             # now  we use 2 sum to find 2 numbers that add up to this, can use sorted or hashset approach 
#             # i reckon sorting is better and then looking thru, but the issue is u gotta consider to not use ur self again, how can we do that? maybe sort first
#             ia = 0
#             ib = len(sortednums)-1
#             while ia < ib : 
#                 if ia == i :
#                     ia +=1
#                     continue
#                 elif ib == i:
#                     ib-= 1 
#                     continue 
#                 elif sortednums[ia] + sortednums[ib] == toFind:
#                     oneanswer.append(sortednums[ia])
#                     oneanswer.append(sortednums[ib])
#                     oneanswer.append(sortednums[i])
#                     oneanswer = sorted(oneanswer)
#                     if oneanswer not in answerarray:
#                         answerarray.append(oneanswer)
#                     ia+=1
#                     oneanswer = []
#                 elif sortednums[ia] + sortednums[ib] < toFind:
#                     ia+=1
#                 else:
#                     ib-=1
            
#         return answerarray
# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         sortednums = sorted(nums)
#         answerarray = []
#         for i in range(len(sortednums)):
#             # Skip duplicates for the first number
#             if i > 0 and sortednums[i] == sortednums[i - 1]:
#                 continue

#             toFind = -sortednums[i]
#             ia, ib = i + 1, len(sortednums) - 1

#             while ia < ib:
#                 current_sum = sortednums[ia] + sortednums[ib]
#                 if current_sum == toFind:
#                     answerarray.append([sortednums[i], sortednums[ia], sortednums[ib]])
#                     ia += 1
#                     ib -= 1
#                     # Skip duplicates for the second and third numbers
#                     while ia < ib and sortednums[ia] == sortednums[ia - 1]:
#                         ia += 1
#                     while ia < ib and sortednums[ib] == sortednums[ib + 1]:
#                         ib -= 1
#                 elif current_sum < toFind:
#                     ia += 1
#                 else:
#                     ib -= 1
        
#         return answerarray

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]: 
        sortednums = sorted(nums)
        answerarray=[]
        for i in range(len(sortednums)):
            toFind = 0- sortednums[i]
            # now  we use 2 sum to find 2 numbers that add up to this, can use sorted or hashset approach 
            # i reckon sorting is better and then looking thru, but the issue is u gotta consider to not use ur self again, how can we do that? maybe sort first
            ia = i+1
            ib = len(sortednums)-1
            while ia < ib : 
                if sortednums[ia] + sortednums[ib] == toFind:
                    answerarray.append([sortednums[i], sortednums[ia], sortednums[ib]])
                    oneanswer = sorted(oneanswer)
                    if oneanswer not in answerarray:
                        answerarray.append(oneanswer)
                    ia+=1
                    oneanswer = []
                elif sortednums[ia] + sortednums[ib] < toFind:
                    ia+=1
                else:
                    ib-=1
            # strat is to move this out
        return answerarray