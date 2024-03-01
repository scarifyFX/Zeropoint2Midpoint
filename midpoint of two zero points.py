def quadratic_equation(x, x1, x2, y0):
      """
  This function defines a quadratic equation with shifted and scaled components.

  Args:
      x: The independent variable (x-coordinate).
      x1: The first x-coordinate for the zero point.
      x2: The second x-coordinate for the zero point.
      y0: The y-level for x = 0.

  Returns:
      The value of the quadratic equation at the given x.
  """

X1 = float(input("Enther the first X coordinate for the zero point: "))
X2 = float(input("Enther the second X coordinate for the zero point: "))

print("The midpoint of those two x coords are:", (X1 + X2) / 2)
