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

## 💡 Why This Script Is Unique

Unlike traditional GUI-based workflows (e.g., ArcGIS, QGIS), this pipeline is:
- 🔁 **Fully automated** — no clicking through menus
- 🧩 **Lightweight and portable** — just Python + PDAL
- 🧠 **Beginner-friendly** — well-commented and modular
- 🖥️ **Ideal for batch processing or headless environments**

---

## 📦 Requirements

Install the required Python libraries:

```bash
pip install geopandas rasterio numpy

🛠️ PDAL must be installed separately (not available via pip):
	•	macOS:  brew install pdal
	•	Windows/Linux (via Conda):  conda install -c conda-forge pdal



