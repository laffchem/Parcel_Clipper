import arcpy

# If you are not me, you will have to define the database your project is using in the workspace variable.

# If you don't want to enable overwriting, remove the line arcpy.env.overwriteOutput which is false by default and save the script, or replace that value with False.

workspace = r"U:\Utilities Availability Requests\Utility_Map.gdb"
arcpy.env.workspace = workspace
arcpy.env.overwriteOutput = True
map_name = "JLaffey_Utility_Master_Map"
aprx = arcpy.mp.ArcGISProject(r"U:\Utilities Availability Requests\JLaffey_Utility_Master_Map.aprx")
map = aprx.listMaps()[0]


# Layer to clip, followed by the selection field name, followed by the dataset in your database location.
input_table = "Parcel"
table_field = "PARCEL"
input_geodataset = f"{workspace}\\Parcel"
