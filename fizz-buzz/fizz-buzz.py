class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answer=[]
        for current in range(1,n+1):
            answer.append('Fizz'*(not current%3)+'Buzz'*(not current%5) or str(current))
        return answer
