import random
import os
import shutil

# Specify the file names
file_to_delete = "coalCloud1Positions"
source_file = "MTcoalCloud1Positions"
destination_file = "coalCloud1Positions"

# Get the current directory
current_directory = os.getcwd()

# Construct the file paths
delete_file_path = os.path.join(current_directory, file_to_delete)
source_file_path = os.path.join(current_directory, source_file)
destination_file_path = os.path.join(current_directory, destination_file)

# Delete the FOAMFile if it exists
if os.path.exists(delete_file_path):
    os.remove(delete_file_path)
    print(f"{file_to_delete} deleted successfully.")
else:
    print(f"{file_to_delete} not found in the directory.")

# Copy MTcoalCloud1Positions to coalCloud1Positions
shutil.copy2(source_file_path, destination_file_path)
print(f"{source_file} copied to {destination_file} successfully.")

def generate_random_point(x1, x2, y1, y2, z1, z2):
    x = round(random.uniform(x1, x2), 2)
    y = round(random.uniform(y1, y2), 2)
    z = round(random.uniform(z1, z2), 2)
    return (x, y, z)

def generate_random_point_in_trapezoid(x1, x2, y1, y2, z1, z2):
    while True:
        x = round(random.uniform(x1, x2), 2)
        y = round(random.uniform(y1, y2), 2)
        z = round(random.uniform(z1, z2), 2)
        # Check if the point is inside the trapezoid
        if y >= -1 and y <= 0:
            if x >= 0 and x <= 1 and y == 0:
                return (x, y, z)
            elif y == -1 and x >= 0.4 and x <= 0.6:
                return (x, y, z)
            elif y > -1 and y < 0:
                max_x = 0.4*y + 1
                min_x = -0.4*y
                if x >= min_x and x <= max_x:
                    return (x, y, z)
        else:
            return (x, y, z)

file_path = destination_file_path

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Find the position to insert the new data
insert_position = content.find('(') + 1

total_points = 1e4 


x1_cuboid, x2_cuboid = 0, 1
y1_cuboid, y2_cuboid = 0, 2
z1_cuboid, z2_cuboid = 0, 0

x1_trapezoid, x2_trapezoid = 0, 1
y1_trapezoid, y2_trapezoid = -1, 0
z1_trapezoid, z2_trapezoid = 0, 0


num_points_cuboid = int(total_points*2/3)
random_points_cuboid = [generate_random_point(x1_cuboid, x2_cuboid, y1_cuboid, y2_cuboid, z1_cuboid, z2_cuboid) for _ in range(num_points_cuboid)]

# Generate random points within the trapezoid volume
num_points_trapezoid = int(total_points*1/3)

random_points_trapezoid = [generate_random_point_in_trapezoid(x1_trapezoid, x2_trapezoid, y1_trapezoid, y2_trapezoid, z1_trapezoid, z2_trapezoid) for _ in range(num_points_trapezoid)]

# Format the random points between brackets
formatted_points_cuboid = [f"({point[0]} {point[1]} {point[2]})" for point in random_points_cuboid]
formatted_points_trapezoid = [f"({point[0]} {point[1]} {point[2]})" for point in random_points_trapezoid]

# Join the formatted points with newline and insert between brackets
modified_content = (
    content[:insert_position] +
    "\n" + '\n'.join(formatted_points_cuboid) +
    "\n" + '\n'.join(formatted_points_trapezoid) +
    "\n" + content[insert_position:]
)

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.write(modified_content)

print("Script executed successfully.", file_path)
