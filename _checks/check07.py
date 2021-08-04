import numpy as np

def test():
    ##################
    ### MODEL CODE ###
    data = np.loadtxt("Files/houseenergy.csv", delimiter=",", skiprows=1)
    elec = data[:, 3]
    gas = data[:, 4]
    total = elec + gas
    output = []
    for day in range(365):
        start = day*24
        end = start+24
        daytotals = total[start:end]
        sumday = sum(daytotals)
        output.append(round(sumday, 3))
    ### END OF MODEL CODE ###
    #########################
    
    so=False
    try: 
        so = np.loadtxt("energy_totals.txt") 
        try: 
            assert output==list(so)
            print("The file contents look correct!")
        except TypeError as e: 
            if str(e)=="iteration over a 0-d array":
                print("It looks like your data only has one entry.\n",
                      "Did you .write() to the file *inside* the for loop block?")
        except AssertionError:
            so3 = so.round(3)
            if output==list(so3):
                print("It might be better to round your data to neaten it up a bit.",
                      "\nBut otherwise everything looks fine!")
            else: 
                print(f"""The data in your file are not as expected!
        Expected:\n{output[:5]} ... \n
        Found:\n{list(so)[:5]} ... """
                )
    except ValueError as e: 
        if str(e)[:34]=="could not convert string to float:":
            print("The format of your file is not as expected! Please check the following:\n")
            print('1. You should be writing **only** numbers to the file (*not* commas or any other text)')
            print('2. Did you remember to start a new line each time using something like print("\\n")')
            print("\nNumpy sees this first entry when reading in your file:\n\n"+str(e)[34:])
        else: print(e)
    except Exception as e: print("Something unexpected went wrong!:\n"+str(e))
    