# lidar-to-dtm-pipeline
lidar-to-dtm-pipeline
# 🛰️ LiDAR to DTM Conversion Pipeline

This project provides a complete, reproducible script to convert raw `.laz` LiDAR tiles into a high-resolution **Digital Terrain Model (DTM)** using only **Python** and **PDAL**.

It merges multiple tiles, clips them to a shapefile boundary, filters ground points (classification 2), and generates a **1-ft resolution** DTM GeoTIFF — all in one streamlined script.

---

![License: MIT](https://img.shields.io/badge/license-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![PDAL](https://img.shields.io/badge/Built%20with-PDAL-blueviolet)

---

## 💡 Why This Script Is Unique

Unlike traditional GUI-based GIS workflows, this solution is:
- 🔁 **Fully automated** — ideal for batch processing and cloud environments
- ⚙️ **Minimal in dependencies** — no need for ArcGIS or QGIS
- 🧩 **Easily portable** — run it on any system with Python + PDAL
- 🧠 **Educational** — great for learning LiDAR processing pipelines

---

## 📦 Requirements

Install these Python libraries:

```bash
pip install geopandas rasterio numpy

Install PDAL separately (not available via pip):
	•	macOS:brew install pdal
	•	Windows/Linux (via Conda):conda install -c conda-forge pdal

🚀 How to Use

1. Prepare Your Files
	•	Place your .laz LiDAR tiles (e.g. 771924.laz, 766915.laz, etc.) in the same folder as the script
	•	Include your polygon clip boundary as Boundary.shp (also include .shx, .dbf, and .prj)

2. Run the script
python lidar.py

📂 Input & Output

📥 Input Files
	•	.laz LiDAR tiles
	•	Boundary.shp (polygon shapefile)

📤 Output Files
	•	merged.las — all .laz tiles merged into one LAS
	•	clipped.las — merged LAS clipped to shapefile boundary
	•	dtm_clipped.tif — 1-ft DTM generated from ground points

lidar-to-dtm-pipeline/
├── lidar.py              # Main processing script
├── Boundary.shp          # Shapefile boundary (with .shx/.dbf/.prj)
├── *.laz                 # Your LiDAR tiles
├── dtm_clipped.tif       # Final DTM output
├── merged.las            # Intermediate file
├── clipped.las           # Intermediate file
├── requirements.txt
└── README.md

🔄 Workflow Breakdown
	1.	Merge all .laz tiles using PDAL readers + writers
	2.	Clip to a shapefile boundary (converted to WKT inside script)
	3.	Filter for ground points only (Classification[2:2])
	4.	Generate a 1-ft resolution DTM using writers.gdal

🧪 Use Cases
	•	Terrain modeling
	•	Wildfire risk mapping
	•	Floodplain analysis
	•	Environmental change detection

⸻

📜 License

MIT License — free to use, modify, and distribute.

⸻

🤝 Contributing

Pull requests and suggestions welcome!
If you find a bug or want to enhance the workflow, feel free to open an issue or contribute directly.

⸻

🌍 Author

Prabhashini M.
📫 [Your contact or GitHub profile here]
