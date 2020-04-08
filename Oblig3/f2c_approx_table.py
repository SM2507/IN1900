"""
2.2: Generate an approximate Farenheit-Celsius conversion table.
Authored by Mohammed Shartaz Mostafa.
Warning: This code has been delivered before by me, the only changes made were to 
translate the code from python 2.7 to python 3.
"""
# Defining the approximate conversion
def C_approx(F):
    C_approx = (F - 30)/2
    return C_approx

# Defining the exact conversion
def C(F):
    C = (F-32)*(5/9)
    return C

# Using list comprehension for converting the temperatures from -50F to 100F. 
Celsius_approx = [C_approx(F) for F in range (-50, 101, 10)]
Celsius = [C(F) for F in range (-50, 101, 10) ]
Farenheit = [F for F in range(-50, 101, 10)]

# Using the zip function to create tuples, which are then printed to the 
# terminal using string formatting. 
for F, C_approxF, CF in zip(Farenheit, Celsius_approx, Celsius):
    print ("|Farentheit = %6.2f| |Celsius_approx = %6.2f| |Celsius = %6.2f| " \
    %(F, C_approx(F), C(F)))



"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig3>python f2c_approx_table.py
|Farentheit = -50.00| |Celsius_approx = -40.00| |Celsius = -45.56|
|Farentheit = -40.00| |Celsius_approx = -35.00| |Celsius = -40.00|
|Farentheit = -30.00| |Celsius_approx = -30.00| |Celsius = -34.44|
|Farentheit = -20.00| |Celsius_approx = -25.00| |Celsius = -28.89|
|Farentheit = -10.00| |Celsius_approx = -20.00| |Celsius = -23.33|
|Farentheit =   0.00| |Celsius_approx = -15.00| |Celsius = -17.78|
|Farentheit =  10.00| |Celsius_approx = -10.00| |Celsius = -12.22|
|Farentheit =  20.00| |Celsius_approx =  -5.00| |Celsius =  -6.67|
|Farentheit =  30.00| |Celsius_approx =   0.00| |Celsius =  -1.11|
|Farentheit =  40.00| |Celsius_approx =   5.00| |Celsius =   4.44|
|Farentheit =  50.00| |Celsius_approx =  10.00| |Celsius =  10.00|
|Farentheit =  60.00| |Celsius_approx =  15.00| |Celsius =  15.56|
|Farentheit =  70.00| |Celsius_approx =  20.00| |Celsius =  21.11|
|Farentheit =  80.00| |Celsius_approx =  25.00| |Celsius =  26.67|
|Farentheit =  90.00| |Celsius_approx =  30.00| |Celsius =  32.22|
|Farentheit = 100.00| |Celsius_approx =  35.00| |Celsius =  37.78|
"""