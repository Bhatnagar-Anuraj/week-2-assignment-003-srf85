"""
DIGM 131 - Assignment 2: Procedural Pattern Generator
======================================================

OBJECTIVE:
    Use loops and conditionals to generate a repeating pattern of 3D objects
    in Maya. You will practice nested loops, conditional logic, and
    mathematical positioning.

REQUIREMENTS:
    1. Use a nested loop (a loop inside a loop) to create a grid or pattern
       of objects.
    2. Include at least one conditional (if/elif/else) that changes an
       object's properties (type, size, color, or position offset) based
       on its row, column, or index.
    3. Generate at least 25 objects total (e.g., a 5x5 grid).
    4. Comment every major block of code explaining your logic.

GRADING CRITERIA:
    - [25%] Nested loop correctly generates a grid/pattern of objects.
    - [25%] Conditional logic visibly changes object properties based on
            position or index.
    - [20%] At least 25 objects are generated.
    - [15%] Code is well-commented with clear explanations.
    - [15%] Pattern is visually interesting and intentional.

TIPS:
    - A 5x5 grid gives you 25 objects. A 6x6 grid gives you 36.
    - Use the loop variables (row, col) to calculate X and Z positions.
    - The modulo operator (%) is great for alternating patterns:
          if col % 2 == 0:    # every other column
    - You can vary: primitive type, height, width, position offset, etc.

COMMENT HABITS (practice these throughout the course):
    - Add a comment before each logical section explaining its purpose.
    - Use inline comments sparingly and only when the code is not obvious.
    - Keep comments up to date -- if you change the code, update the comment.
"""

import maya.cmds as cmds

# for sin/cos equations
import math

# Clear the scene.
cmds.file(new=True, force=True)

# defining pillar amount per row, radius of each row, # of row, and height of pillars
def generate_pattern(object_count=12, circle_radius=10, row_count=3, pillar_height=10):

    # creating an altar or sphere at the origin, center point of pattern
    cmds.polySphere(name='altar_name', radius=2)
    cmds.move(0, 2.5, 0, 'altar_name')
    
    # setting up first loop with the separate rows
    for row in range(row_count):
        # defining the inner radius pillars are positioned around; smaller radius will be for the inner row
        current_radius = circle_radius - (row * 6)
        # second loop using sin/cos and the index to create circular pillars
        for i in range(object_count):
            angle = 2 * math.pi * i / object_count
            pos_x = math.cos(angle) * current_radius
            pos_z = math.sin(angle) * current_radius

            # defining and creating the pillar shapes; using the index + rows for the naming convention
            pillar_name = f"pillar_{row}_{i}"
            cmds.polyCylinder(name=pillar_name, radius=0.5, height=pillar_height)
            cmds.move(pos_x, 5, pos_z, pillar_name)

            # conditional statement to scale down the inner pillars; if its in the first row it will be scaled down by specified values.
            if row > 0:
                cmds.scale(0.5, 0.2, 0.5, pillar_name)
                cmds.move(pos_x, 0.75, pos_z, pillar_name)
                print("small pillar")

            # conditional statement to create the tops of the large pillars; if row is 0 then create the sphere and move it.
            if row == 0:
                orb_name = f"orb_{row}_{i}"
                cmds.polySphere(name=orb_name, radius=0.5)
                cmds.move(pos_x, 10, pos_z, orb_name)
                print("altar orbs")
                
# ---------------------------------------------------------------------------
# Run the generator
# ---------------------------------------------------------------------------
generate_pattern()

# Frame everything in the viewport.
cmds.viewFit(allObjects=True)
print("Pattern generated successfully!")
