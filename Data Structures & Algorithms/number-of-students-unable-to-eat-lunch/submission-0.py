
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        sandwich_stack = sandwiches
        student_queue = students
        counter = 0
        while sandwich_stack and counter < len(student_queue):
            if sandwich_stack[0] == student_queue[0]:
                sandwich_stack.pop(0) 
                counter = 0
            else:
                student_queue.append(student_queue[0])
                counter += 1
            
            student_queue.pop(0)

        return len(student_queue)



        
        