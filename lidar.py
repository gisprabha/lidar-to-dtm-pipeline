import subprocess
import json
import os
import geopandas as gpd

# --- Step 1: Input Files ---
input_files = [
    "first_file.laz",
    "second_file.laz",
    "third_file.laz"
]
boundary_shp = "Boundary.shp"

merged_file = "merged.las"
clipped_file = "clipped.las"
output_dtm = "dtm_clipped.tif"

# --- Step 2: Merge files using pdal pipeline ---
print("🔄 Merging LAZ files...")

merge_pipeline = {
    "pipeline": [
        {"type": "readers.las", "filename": os.path.abspath(f)} for f in input_files
    ] + [
        {"type": "writers.las", "filename": merged_file}
    ]
}

subprocess.run(
    ["pdal", "pipeline", "--stdin"],
    input=json.dumps(merge_pipeline).encode(),
    check=True
)
print(f"✅ Merged LAS written to {merged_file}")

# --- Step 3: Clip merged LAS using Boundary.shp (converted to WKT) ---
print("✂️  Clipping to boundary from shapefile...")

gdf = gpd.read_file(boundary_shp)
polygon_wkt = gdf.geometry.union_all().wkt  # Fixed deprecated warning

clip_pipeline = {
    "pipeline": [
        {
            "type": "readers.las",
            "filename": merged_file
        },
        {
            "type": "filters.crop",
            "polygon": polygon_wkt
        },
        {
            "type": "writers.las",
            "filename": clipped_file
        }
    ]
}

subprocess.run(
    ["pdal", "pipeline", "--stdin"],
    input=json.dumps(clip_pipeline).encode(),
    check=True
)
print(f"✅ Clipped LAS saved as {clipped_file}")

# --- Step 4: Generate DTM from clipped LAS ---
print("🌍 Generating DTM from ground points...")

dtm_pipeline = {
    "pipeline": [
        {
            "type": "readers.las",
            "filename": clipped_file
        },
        {
            "type": "filters.range",
            "limits": "Classification[2:2]"
        },
        {
            "type": "writers.gdal",
            "filename": output_dtm,
            "resolution": 0.3048,  # 1-ft resolution
            "output_type": "min",
            "nodata": -9999
        }
    ]
}

subprocess.run(
    ["pdal", "pipeline", "--stdin"],
    input=json.dumps(dtm_pipeline).encode(),
    check=True
)
print(f"✅ Final DTM raster saved as {output_dtm}")