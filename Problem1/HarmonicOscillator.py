#%%
n = int(input("principle quantum number? "))

if n>=0:
    E = (n+1/2)
    E = str(E)
    print("E_n="+E+"h")
    h = 6.626069934*(10**(-34))
    E = float(E)
    EC = h*E
    EC = str(EC)
    print(EC+"eV")
    
else:
    print("input a posivite value")

