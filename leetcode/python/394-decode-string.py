
class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char != ']':
                stack.append(char)
            else:
                str_buffer = ''
                while stack:
                    tmp_c = stack.pop()
                    if tmp_c == '[':
                        multi = ''
                        while stack and stack[-1].isdigit():
                            multi = stack.pop() + multi
                        stack.append(int(multi) * ''.join(str_buffer))
                        break
                    else:
                        str_buffer = tmp_c + str_buffer
                        
        return ''.join(stack)