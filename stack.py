def stack_function(s1):
    s2=Stack(5)
    while not s1.is_empty():
        if (s1.pop()%5==0) :
            break
        else:
            if (not s1.is_empty()):
                s2.push(s1.pop()*2)
                if s2.is_empty():
                    s1.pop()
                else:
                    s2.push(10)
    return s2               
