"""
3.16: Compute the area of an arbitrary triangle.
Authored by Mohammed Shartaz Mostafa.
Warning: This code has been delivered before by me, the only changes made were to 
translate the code from python 2.7 to python 3.
"""

# This takes in a list of the coordinates of the three points that comprise the triangle.
def triangle_area(vertices):  # Very obvious what happens in the function
    x1 = vertices[0][0]  # Takes in a list and extracts the desired number
    y1 = vertices[0][1]
    x2 = vertices[1][0]
    y2 = vertices[1][1]
    x3 = vertices[2][0]
    y3 = vertices[2][1]
    A = 0.5*abs(x2*y3 - x3*y2 - x1*y3 + x3*y1 + x1*y2 - x2*y1)  # Given function
    return A  # Returns A whenever called correctly

# Defines the test function, which tests the area calculated by the function above with the exact
def test_triangle_area():
    v1 = (0,0); v2 = (1,0); v3 = (0,2)  # Coordinates of my choosing
    vertices = [v1, v2, v3]  # Apply to a list
    expected = 1  # Expected area
    computed = triangle_area(vertices)  # Area calculated
    tol = 1e-14  # Tolerance 
    success = abs(expected - computed) < tol  # The condition for success
    msg = "computed area = %g != %g (expected)" % \
    (computed, expected)

    assert success, msg  # testing the condition, which will print msg if False
    if success:
        print(triangle_area(vertices))

test_triangle_area()


"""
C:Users\moham\Google Drive\PHYSX\PYTHON FLS\IN1900\Oblig3>python area_triangle.py
1.0
"""
