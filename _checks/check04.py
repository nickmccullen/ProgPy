from math import sin, cos, pi


def test(newton, sinc):
    try: 
        assert sinc(0)==1.0
        print("Test 0: PASS")
    except NameError as e: print(e+'\nDid you name sinc correctly?')
    except ZeroDivisionError: print(f'''The test of sinc at x=0 failed
    * Check that you have a condition for x=0 in the sinc function''')
    except: print("Your sinc function returns the wrong value at x=0") 
    try: 
        test1 = round(newton(sin, 1), 10)
        model1 = round(-4.796274303743752e-26, 10)
        assert test1==model1
        print("Test 1: PASS")
    except NameError as e: print(e+'\nDid you name newton correctly?')
    except: print(f'''The root for sine was not found corrrectly
    Expected: {model1} (i.e. near zero)
    Actual: {test1}    
    * Check that functions are being named and used correctly in loops and functions
    * Check that your while loop is checking against the correct error value
    * check against previous examples that indentation is all correct''')
    try: 
        test2 = round( newton(sinc, 1), 10)
        model2 = round(3.1415926535897953, 10)
        assert test2==model2
        print("Test 2: PASS")
    except NameError as e: print(e+'\nDid you name newton correctly?')
    except: print(f'''The root for sinc was not found corrrectly
    Expected: {model2}
    Actual: {test2}
    * Check that functions are being named and used correctly in loops and functions
    * Check that your while loop is checking against the correct error value
    * check against previous examples that indentation is all correct''')
    try: 
        test3 = round( newton(cos,1), 10)
        model3 = round(1.5707963267948966, 10)
        assert model3==test3
        print("Test 3: PASS")
    except NameError as e: print(e+'\nDid you name newton correctly?')
    except: print(f'''The hidden test failed against another function
    * Check that functions are being named and used correctly in loops and functions
    * Check that your while loop is checking against the correct error value
    * check against previous examples that indentation is all correct''')