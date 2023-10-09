# This file will contain functions for the parcel clipper script.
import arcpy
from config import *


def clip_parcel(parcel_id, input_table, table_field, input_geodataset):
    # Query the database
    cursor = arcpy.da.SearchCursor(
        in_table=input_table, field_names=table_field, where_clause=f"{table_field} = '{parcel_id}'"
    )
    # Get the parcel id from the created tuple
    for row in cursor:
        parcel_id = row[0]

    if len(parcel_id) == 15 and parcel_id is not None:
        # Create the SQL expression for selection
        selection_sql = f"{table_field} = '{parcel_id}'"
        parcel_clip_name = f"Parcel_{parcel_id}"
        output_clip = f"{workspace}\\{parcel_clip_name}"

        # Select the desired parcel using the SelectLayerByAttribute
        # arcpy.MakeFeatureLayer_management(input_geodataset, parcel_clip_name)
        selection_from_dataset = arcpy.SelectLayerByAttribute_management(
            input_geodataset, "NEW_SELECTION", selection_sql
        )

        # Clip the geographic dataset using the Clip Analysis Tool
        arcpy.Clip_analysis(selection_from_dataset, input_geodataset, output_clip)
        print(f"Parcel ID: {parcel_id} successfully clipped!")

        # Delete the temporary Parcel_Layer1 that is created in clipping analysis.
        arcpy.Delete_management("Parcel_Layer1")

        return parcel_clip_name

    else:
        print("Parcel not found")


def apply_symbo(clipper_function):
    # Update the symbology of the clipped layer
    arcpy.management.ApplySymbologyFromLayer(clipper_function, "Parcel", "VALUE_FIELD PARCEL PARCEL", "DEFAULT")
