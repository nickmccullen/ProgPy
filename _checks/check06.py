def test(plotter):
    import numpy as np
    import matplotlib
    xdata = np.arange(300)
    ydata = np.random.normal(50, 15, 300)
    
    
    try: 
        fig = plotter(xdata, ydata)
    
        try: figprops = fig.properties()
        except AttributeError as e: print("It doesn't look like you generated a figure (fig) object properly using .subplots()")
        except Exception as e: 
            print(e)
        
        try: 
            aXs = fig.axes

            print("Feedback:\n")

            fw,fh = figprops["figwidth"],figprops["figheight"]

            if (fw,fh)!=(10.0,4.0): print(f"Your figure is size {fw} x {fh}, I was expecting it to be 10 wide by 4 high")

            if len(aXs)==1: print("Your Figure only has one set of axes")
            if len(aXs)!=2: print("Your Figure should have exactly two sets of axes")
            (nr,nc,n) = aXs[0].get_geometry()
            if (nr,nc)!=(1,2): print(f'''Your figure canvas has {nr} rows and {nc} columns,
            but it should be a 1x2 grid of axes, specify the correct nrows and ncols in plt.subplots()\n''') 
            else:
                props0 = aXs[0].properties()
                props1 = aXs[1].properties()                 
                lines1 = [p for p in props0["children"] if type(p)==matplotlib.lines.Line2D]
                if len(lines1)==0:
                    print("The first (left) axes contain no plotted lines\n")
                else:    
                    prop1 = lines1[0].properties()

                    if prop1["xdata"].all() != xdata.all():
                        print("You have not plotted the correct x-values in the left plot.\n")
                    if prop1["ydata"].all() != ydata.all():
                        print("You have not plotted the correct y-values in the left plot.\n")

                    props = { 
                        "linewidth": 0.2,
                        "color": 'red',
                        'marker': '*',
                        'markerfacecolor': 'green',
                        'markersize': 10.0
                    }

                    for p in props:
                        v = props[p]
                        if prop1[p]!=v: print(f"The {p} is not set to {v}\n")
                            
                    if aXs[0].get_xlabel()=='': print("You have no xlabel on the first Axes\n")
                    if aXs[0].get_ylabel()=='': print("You have no ylabel on the first Axes\n")
                    if aXs[0].get_title() =='': print("You have no title on the first Axes\n")
                    if props0['autoscalex_on']==True: print("You have not set the x-axis limits to the correct range\n")

                rect2 = [p for p in props1["children"] if type(p)==matplotlib.patches.Rectangle]

                if len(rect2)==1: print("There are no histogram boxes plotted on right second (right hand) axes\n")
                else: 
                    boxprops = rect2[len(rect2)//2].properties()
                    if boxprops["width"] < boxprops["height"]:
                        print("Your histogram has the wrong orientation, it should be horizontal\n")
                    if boxprops['edgecolor']!=(0.0, 0.0, 0.0, 1.0): print(f"The edgecolor is not set to black\n")
                       
                    if aXs[1].get_xlabel()=='': print("You have no xlabel on the second Axes\n")  
                    if aXs[1].get_title() =='': print("You have no title on the second Axes\n")

                        
                print("""Check the figure below looks as it should.
Also check that you have saved an image file to the 
same folder as your are running the notebook or python script\n
Output:""")

        except AttributeError as e: print("You need to generate separate axes using fig, ax = ... or fig, (ax1, ax2) = ...")

    except NameError as e: 
        print(e)
        if str(e)=="name 'plt' is not defined":
            print("NameError: "+str(e))
            print("\nDid you import the matplotlib.pyplot library correctly?")
        if str(e)=="name 'fig' is not defined":
            print("NameError: "+str(e))
            print("\nIt doesn't look like you generated a figure (fig) object properly using .subplots()")
            
                        