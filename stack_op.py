
class Stack:
        
        def __init__(self,size):
                self.stack = []
                self.size = size
        def push(self,item):
                if len(self.stack) == self.size:
                        print("stack is overflow!....")
                else:
                        self.stack.append(item)
        def pop(self):
                result = -1
                if self.stack == []:
                        print("stack is empty")
                else:
                        result=self.stack.pop()
                return result
        def display(self):
                
                if self.stack == []:
                        print("stack is empty")
                else:
                        for item in reversed(self.stack):
                                print("the elements are:",item)




exit = False
stack =Stack(4)
while not exit:
        print("\n choose an operation")
        print("1.push")
        print("2.pop")
        print("3.display")
        s = input()
        def pushOp():
                num = input("insert a number")
                if num.isdigit():
                        stack.push(num)
                else:
                        print("invalid input")
        def displayOp():
                global stack
                stack.display()
                
        def popOp():
                global stack
                n = stack.pop()
                if n!=-1:
                        print(f,"deleted data:{n}")
        
        def exitOp():
                global exit
                exit = True
                print("exiting")
        switch = {
                '1':pushOp,
                '2':popOp,
                '3':displayOp
                
                }
        switch.get(s,exitOp)()
                
                
