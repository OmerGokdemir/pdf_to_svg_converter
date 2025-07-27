# 📄 PDF to SVG Converter

A lightweight and high-quality solution for converting multi-page PDF architectural plans into scalable SVG files using Python and Poppler. Ideal for web-based visualization and vector-friendly rendering in design or mapping projects.

****

## 🚀 Features

- ✅ Converts **multi-page PDFs** into **individual SVG files**
- ✅ Maintains **high visual quality** using `pdftocairo`
- ✅ Automatically names output files with a custom prefix
- ✅ Works smoothly on Windows (Poppler required)

****

## 📦 Requirements

- Python 3.7+
- Poppler for Windows (e.g. `pdftocairo.exe`)

### Python Dependencies

Install dependencies via:

```bash
pip install -r requirements.txt
```

Make sure Poppler is correctly installed and accessible. You can download it from:
*   https://github.com/oschwartz10612/poppler-windows/releases/

****

## 🛠️ How It Works

The script uses the command-line tool `pdftocairo` (part of Poppler) to convert each page of a PDF into a separate SVG file.

### Usage

```py
from utils import convert_pdf_to_svg

convert_pdf_to_svg(
    pdf_path="example.pdf",
    output_dir="output/",
    prefix="floorplan"
)
```

### Output

*   Input: example.pdf (3 pages)

*   Output:

```lua
    output/
    ├── floorplan-1.svg
    ├── floorplan-2.svg
    └── floorplan-3.svg
```

****

## 🖥️ Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/OmerGokdemir/pdf_to_svg_converter.git
cd pdf_to_svg_converter
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

3. Set Poppler path inside `utils.py` (modify if needed):

```py
    pdftocairo_path = r"C:\Path\To\poppler\bin\pdftocairo.exe"
```

****

## ✅ Example Use Case

Perfect for:

* Floor plan visualizations

* Digital maps

* Architectural previews

* SVG-based design integration

****

## 📁 Project Structure

```pgsql
pdf_to_svg_converter/
├── utils.py          # PDF to SVG conversion logic
├── requirements.txt  # Python dependencies
└── README.md         # Project documentation
```

****

## 📌 Roadmap / To-Do

* CLI support

* Drag-and-drop GUI interface

* MacOS/Linux path auto-detection

* SVG post-processing (compression, optimization)

****

## 🤝 Contributing

Contributions, ideas, and suggestions are welcome! Feel free to fork the project and open a pull request.

****

## 📄 License

This project is licensed under the [MIT LICENSE](LICENSE).

****

## 👨‍💻 Author

* 🛠 Developed with ❤️ by [Omer Gokdemir](https://github.com/OmerGokdemir)

* 📩 Reach me on [LinkedIn](https://www.linkedin.com/in/omer-gokdemir/) | [Upwork](https://www.upwork.com/freelancers/~01cf80f9e22cf120e3)
