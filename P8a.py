import math

def ball_collides(ball1, ball2):
    """
    Takes two balls as parameters and computes if they are colliding.
    Returns a boolean representing whether or not the balls are colliding.
    """
    # Extract the coordinates and radius of each ball
    x1, y1, r1 = ball1
    x2, y2, r2 = ball2
    
    # Compute the distance between the centers of the balls using the Pythagorean theorem
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
    # Determine if the balls are colliding by comparing the distance to the sum of their radii
    if distance <= r1 + r2:
        return True
    else:
        return False
