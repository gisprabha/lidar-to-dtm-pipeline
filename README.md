# 🛰️ LiDAR to DTM Conversion Pipeline

**`lidar-to-dtm-pipeline`** is a streamlined, script-based workflow for converting raw `.laz` LiDAR tiles into a high-resolution **Digital Terrain Model (DTM)** using **Python** and **PDAL**.

This tool automates:
- 🗃️ Merging multiple `.laz` tiles  
- ✂️ Clipping the point cloud to a shapefile boundary  
- 🧹 Filtering only **ground points (Classification 2)**  
- 🗺️ Generating a **1-ft resolution DTM** as GeoTIFF

> Ideal for researchers, analysts, and developers working in terrain analysis, environmental monitoring, or GIS automation.

---

![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PDAL](https://img.shields.io/badge/Built%20with-PDAL-blueviolet)

---

## 📦 Requirements

Install the required Python libraries:

- pip install geopandas  
- pip install rasterio  
- pip install numpy  

🛠️ **PDAL must be installed separately (not available via pip):**

- **macOS**:  
  brew install pdal

- **Windows/Linux (via Conda)**:  
  conda install -c conda-forge pdal

---

## 🚀 How to Use

### 1. Prepare Your Files

- Place all your `.laz` LiDAR tiles (e.g. `771924.laz`, `766915.laz`, etc.) in the project folder  
- Include a polygon shapefile as `Boundary.shp` (with `.shx`, `.dbf`, and `.prj` files)

### 2. Run the Script

python lidar.py

---

## 📂 Input & Output Summary

### 📥 Input Files
- LiDAR tiles (`.laz`)
- Clipping boundary shapefile: `Boundary.shp` (+ .shx, .dbf, .prj)

### 📤 Output Files
- merged.las → all `.laz` tiles merged into one LAS
- clipped.las → merged LAS clipped to shapefile boundary
- dtm_clipped.tif → final 1-ft DTM raster

---

## 📁 Project Structure

lidar-to-dtm-pipeline/  
├── lidar.py              # Main processing script  
├── *.laz                 # Your LiDAR tiles  
├── Boundary.shp          # Shapefile boundary (plus .shx/.dbf/.prj)  
├── merged.las            # Merged LAS (intermediate)  
├── clipped.las           # Cropped LAS (intermediate)  
├── dtm_clipped.tif       # Final DTM output  
├── requirements.txt  
└── README.md  

---

## 🔄 Workflow Breakdown

1. Merge `.laz` tiles using PDAL readers + writers  
2. Clip to shapefile boundary (converted to WKT internally)  
3. Filter for ground points only (`Classification[2:2]`)  
4. Write a DTM raster (GeoTIFF) using PDAL’s `writers.gdal`

---

## 🧪 Use Cases

- Terrain modeling & slope analysis  
- Wildfire risk modeling  
- Floodplain & watershed mapping  
- Digital baseline generation for remote sensing

---

## 📜 License

This project is licensed under the **MIT License** — free to use, modify, and distribute.

---

## 🤝 Contributing

Have feedback or ideas?  
Pull requests are welcome!  
Please open an issue for bugs, enhancements, or improvements.

---

## 🌍 Author

**Prabhashini Manawardhana**  



