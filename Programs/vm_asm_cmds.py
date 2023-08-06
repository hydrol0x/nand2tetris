pop = """
// pop local {i}
@sp
M=M-1

@i
D = A
@LCL
D = D+A 
@addr
M = D
 
@sp 
@M 
D = M 
@addr
@M
M = D
"""