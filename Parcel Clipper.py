# Set the workspace for the database you are working with.

# Note this is probably better to use a local datbase and not the Apopka database to avoid writing clips to it.
import arcpy
from clip_function import clip_parcel, apply_symbo
from config import map, input_table, input_geodataset, table_field

# Setting Project Files and Map Name
program_running = True
instructions = """
Instructions: To use the parcel clipper, enter a 15 character parcel id. Note this id must be all integers!. This program runs on a loop to allow you to clip multiple parcels. If you would like to exit the script, simply type 'q' to quit.
"""
print(instructions)
# This makes sure you're in the correct map.
print(map.name)

while program_running:
    # This line is how you input the parcel id in the command prompt.
    parcel_id = input("Enter the parcel utility request number. Enter q to quit!\n")
    print(len(parcel_id))
    if parcel_id.lower() == "q":
        print("Quitting Program!")
        program_running = False
    elif len(parcel_id) == 15:
        try:
            parcel_id = int(parcel_id)
        except ValueError:
            print(f"Error: Your entry: '{parcel_id}' is invalid. You need to enter a 15 numeric character parcel id!")
        else:
            parcel_id = str(parcel_id)
            clipped_parcel = clip_parcel(
                parcel_id=parcel_id, input_table=input_table, table_field=table_field, input_geodataset=input_geodataset
            )
            apply_symbo(clipper_function=clipped_parcel)
    else:
        print(f"Input error... Your entry: '{parcel_id}' needs to be 15 numeric characters.")
