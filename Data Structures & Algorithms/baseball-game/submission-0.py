class Solution:
    def calPoints(self, operations: List[str]) -> int:
        N = len(operations)
        score = 0   
        score_arr = []
        
        for i in range(N):

            operation = operations[i]

            match operation:

                case "+":
                    current_op = int(score_arr[len(score_arr) - 1]) + int(score_arr[ len(score_arr) - 2])
                    score_arr.append(current_op)
                    score += current_op

                
                case "D":
                    current_op = 2*int(score_arr[len(score_arr)- 1])
                    score_arr.append(current_op)
                    score += current_op
                
                case "C":
                    score -= score_arr[len(score_arr) - 1]
                    score_arr.pop()


                case _:
                    current_op = int(operation)
                    score_arr.append(current_op)
                    score += current_op

        return score
                    

            


        