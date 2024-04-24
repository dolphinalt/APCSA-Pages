# Physics Calculator
import math
import os

"""
Define some Utility functions for the program:
print_subMenu() - Provides menu format for easier printing
"""
def print_subMenu(topic, textList):
    ## check to see if the input is valid
    if len(topic) > 34:
        raise ValueError("The topic and text must be less than 34 characters.")
    
    ## print the subMenu
    print("╭───────────────────────────────────╮")
    print(f"│ {topic}" + " "*(34-len(topic)) + "│")
    print("│───────────────────────────────────│")
    for text in textList:
        if len(text) > 34:
            raise ValueError("The topic and text must be less than 34 characters.")
        print(f"│ {text}" + " "*(34-len(text)) + "│")
    print("╰───────────────────────────────────╯")

def floatVarInput():
    try:
        val = float(input())
    except ValueError:
        val = "?"
    os.system('clear')
    return val

"""
Define the methods used by the main function
"""
def main():
    ### define a function for kinematics ###

    # Kinematics menu
    # [Vi, Vf, a, t, dX]
    var = [] # to make things easier, sort in a list. otherwise, we need to create individual variables for each value
    print_subMenu("Physics Kinematics Calculator", textList=["Enter a Vi (? for unknown) <", "Enter a Vf (? for unknown)", "Enter an a (? for unknown)", "Enter a t (? for unknown)", "Enter a dX (? for unknown)"])
    var.append(floatVarInput())
    
    print_subMenu("Physics Kinematics Calculator", textList=[f"Vi = {var[0]}", "Enter a Vf (? for unknown) <", "Enter an a (? for unknown)", "Enter a t (? for unknown)", "Enter a dX (? for unknown)"])
    var.append(floatVarInput())
    
    print_subMenu("Physics Kinematics Calculator", textList=[f"Vi = {var[0]}", f"Vf = {var[1]}", "Enter an a (? for unknown) <", "Enter a t (? for unknown)", "Enter a dX (? for unknown)"])
    var.append(floatVarInput())
    
    print_subMenu("Physics Kinematics Calculator", textList=[f"Vi = {var[0]}", f"Vf = {var[1]}", f"a = {var[2]}", "Enter a t (? for unknown) <", "Enter a dX (? for unknown)"])
    var.append(floatVarInput())
    
    print_subMenu("Physics Kinematics Calculator", textList=[f"Vi = {var[0]}", f"Vf = {var[1]}", f"a = {var[2]}", f"t = {var[3]}", "Enter a dX (? for unknown) <"])
    var.append(floatVarInput())

    print_subMenu("Physics Kinematics Calculator", textList=[f"Vi = {var[0]}", f"Vf = {var[1]}", f"a = {var[2]}", f"t = {var[3]}", f"dX = {var[4]}"])
    print("Calculating...")

    # calculations using kinematics equations: At most we can have 3 unknowns
    unknown = 0
    for value in var:
        if unknown >= 3:
            print_subMenu("Physics Kinematics Calculator", textList=[f"Vi = {var[0]}", f"Vf = {var[1]}", f"a = {var[2]}", f"t = {var[3]}", f"dX = {var[4]}", "Cannot be solved."])
            return 0
        if value == "?":
            unknown += 1

    # attempt to solve for Vi
    if var[0] == "?":
        try: var[0] = var[1] - var[2]*var[3]
        except:
            try: var[0] = ((var[4] / var[3]) * 2) - var[1]
            except:
                try: var[0] = (var[4] / var[3]) - (0.5 * var[2] * var[3])
                except:
                    try: var[0] = math.sqrt(var[1]**2 - 2*var[2]*var[4])
                    except: pass
    
    # attempt to solve for Vf
    if var[1] == "?":
        try: var[1] = var[0] + var[2]*var[3]
        except:
            try: var[1] = ((var[4] / var[3]) * 2) - var[0]
            except:
                try: var[1] = math.sqrt(var[0]**2 + 2*var[2]*var[4])
                except: pass
    
    # attempt to solve for a
    if var[2] == "?":
        try: var[2] = (var[1] - var[0]) / var[3]
        except:
            try: var[2] = var[4] - (var[0] * var[3]) / (0.5 * var[3]**2)
            except:
                try: var[2] = (var[1]**2 - var[0]**2) / (2 * var[4])
                except: pass
    
    # attempt to solve for t
    if var[3] == "?":
        try: var[3] = (var[1] - var[0]) / var[2]
        except:
            try: var[3] = var[4] / ((var[0] + var[1]) / 2)
            except:
                try: var[3] = var[4] - (var[0] * var[3]) - (0.5 * var[2])
                except: pass
    
    # attempt to solve for dX
    if var[4] == "?":
        try: var[4] = ((var[1] + var[0]) / 2) * var[3]
        except:
            try: var[4] = var[0] * var[3] + (0.5 * var[2] * var[3]**2)
            except:
                try: var[4] = (var[0]**2 - var[1]**2) / (2 * var[2])
                except: pass
    
    # print the results
    print_subMenu("Physics Kinematics Calculator", textList=[f"Vi = {var[0]}", f"Vf = {var[1]}", f"a = {var[2]}", f"t = {var[3]}", f"dX = {var[4]}", "System been solved."])

main()