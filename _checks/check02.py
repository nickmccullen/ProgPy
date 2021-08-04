def test(rho, A_g):
    theta=57
    tau=0.64
    r_c=0.7; r_s=0.4; r_g=0.1; r_f=0.2
    width=4; length=8; height=3
    A_g_original = 6.9
    A_s = 2*width*height + 2*length*height - A_g_original
    A_c = length*width
    A_f = A_c
    A = A_c + A_f + A_s + A_g_original
    MODEL_rho = (A_c*r_c + A_f*r_f + A_s*r_s + A_g_original*r_g)/(A)
    MODEL_D_old = A_g_original*(theta*tau)/(A*(1-rho**2))
    D = 5
    MODEL_A_g = D*A*(1-rho**2)/(theta*tau)#write the formula for the new glazing area here
    try: 
        assert round(rho,10)==round(MODEL_rho,10)
        print("Test 1: PASS")
    except NameError as e: print(e+'\nDid you name rho correctly?')
    except: print(f'''Your value for rho is incorrectly calculated
    Expected: {MODEL_rho}
    Actual:''', rho)
    #try: 
    #    assert D_old==MODEL_D_old
    #    print("Test 2: PASS")
    #except NameError as e: print(e+'\nDid you name D_old correctly?')
    #except: print(f'''Your value for D_old is incorrectly calculated
    #Expected: {MODEL_D_old}
    #Actual:''', D_old)
    try: 
        assert round(A_g,2)==round(MODEL_A_g,2)
        print("Test 2: PASS")
    except NameError as e: print(e+'\nDid you name A_g correctly?')
    except: print(f'''Your rounded value for A_g is incorrect
    Expected: 15.53
    Actual:''', round(A_g, 2))
