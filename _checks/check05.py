from math import sin, cos, pi



def test(quadmap):
    ### model code ###
    def MODEL_quadmap(c): 
        xvals=[]
        x = 0.5
        for i in range(10000):
            x = c - x**2
        for i in range(16):
            x = c - x**2
            xvals.append(x)
        return xvals
        ### end model code ###
    
    print("Test 1: quadmap(1.3)...\n")
    q1 = quadmap(1.3)
    p1 = MODEL_quadmap(1.3)
    try: 
        assert q1==p1
        print("Test 1: PASS")
    except NameError as e: print(e+'\nDid you name the quadmap function correctly?')
    except AssertionError: 
        print(f'''The wrong values were returned.\n''')
        if type(q1)!=type(p1):
            print("Your function does not return a list!\n")
        elif len(q1)!=len(p1):
            print(f"Your list has {len(q1)} elements not the expected {len(p1)}.\n")
        else:
            print(f'''Check the following:
        * Are you iterating for 10000 (ten thousand) iterations **before** saving any values to your list?

        The output of your function was:
        {q1}

        it should have been:
        {p1}''')
            
    print("\nTest 2: quadmap(1.6)...\n")
    q1 = quadmap(1.6)
    p1 = MODEL_quadmap(1.6)
    try: 
        assert q1==p1
        print("""Test 2: PASS\n\n Now try changing your initial value of x=0.4999999999999 
        then rerun both your code and this block to see how sensitive chaos is to initial conditions!""")
    except NameError as e: print(e+'\nDid you name the quadmap function correctly?')
    except AssertionError: 
        print(f'''The wrong values were returned.\n''')
        if type(q1)!=type(p1):
            print("Your function does not return a list!\n")
        elif len(q1)!=len(p1):
            print(f"Your list has {len(q1)} elements not the expected {len(p1)}.\n")
        else:
            print(f'''Check the following:
        * Are you iterating for 10000 (ten thousand) iterations **before** saving any values to your list?
        * Did you start from the initial value x=0.5. Chaos is sensitive to initial conditions so even a 
        very slight difference in the starting point quickly diverges to a different set of values!

        The output of your function was:
        {q1}

        it should have been:
        {p1}''')
            
                        