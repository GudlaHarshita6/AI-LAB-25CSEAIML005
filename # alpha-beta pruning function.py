import math
def alpha_beta(depth, nodeIndex, maximizingPlayer, values, alpha, beta, height):
    
    if depth == height:
        return values[nodeIndex]
    if maximizingPlayer:
        best =-math.inf
        
        for i in range(2):
            val = alpha_beta(depth + 1,nodeIndex * 2 + i,False,values,alpha,beta,height)
            best=max(best,val)
            alpha=max(alpha,best)
            if beta<=alpha:
                break
        return best
    else:
        best=math.inf
        
        for i in range(2):
            val=alpha_beta(depth+1,nodeIndex*2+i,True,values,alpha,beta,height)
            best=min(best,val)
            beta=min(beta,best)
            
            # alpha cut-off
            if beta<=alpha:
                break
        return best    
    # main program                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           
values=list(map(int, input("Enter 8 leaf node values: ").split()))
height = 3
result = alpha_beta(
    0,
    0,
    True,
    values,
    -math.inf,
    math.inf,
    height
)
print("\nOptimal value:", result)
