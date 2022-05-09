class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        # # /home//foo/.././.../
        # # home, foo, .., ., ...
        splitedBySlash = path.split("/")
        for folder in splitedBySlash:
            if folder == "..":
                if stack:
                    stack.pop()
            elif folder == ".":
                continue
            elif folder:
                stack.append(folder)
            
        return "/" + "/".join(stack)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # /.
        # ./../
        # /../
        # /.../
        # //
        # /home/root/.././ -> /home
#         i = 0
#         previous = 0
#         while i<len(path):
#             if path[i] == ".":
#                 if i!=0 and i<len(path)-1:
#                     if path[i-1] == "/" and path[i+1] == "/":
#                         path = path[:i] + path[i+2:]
#                         i+=1
#                     elif i+2<len(path) and path[i-1] == "/" and path[i+1] == "."
#                         if path[i+2] == ".":
#                             if i+3<len(path) and path[i+3] == "/":
#                                 path = path[:i] + path[i+3:]
                                
#             elif path[i] == "/":
#                 if i<len(path)-1 and path[i+1] == "/":
#                     path = path[:i] + path[i+1:]
#                 elif i+3<len(path) and path[i+1] == "." and path[i+2] == "." and path[i+3] == ".":
#                     previous = i
#                 elif i+1<len(path) and path[i+1] != "." and path[i+1] != '/':
#                     previous = i
                    
                        
        
        