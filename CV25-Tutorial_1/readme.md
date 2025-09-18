# Python Image Processing Tutorial  

This repository provides a hands-on tutorial on Python-based image processing. It covers data loading, filter implementation, plotting, argument handling, and debugging using **VS Code**.  

## Main points
1. How to load images and create a separate DataLoader class.
2. Define various types of filters in a dedicated Filters class and apply them to images.
3. Implement a Plotter class responsible for visualizations and plotting.
4. Plotting 2D and 3D Gaussian filters with both discrete and continuous gaps.
5. How to define arguments in your main.py to make interface user-friendly, and how to run Python files through the terminal using command-line arguments.
6. How to debug and perform step-by-step execution of your code using the VS Code Debugger.
7. 👉 [Watch Tutorial Video](youtube.com/watch?reload=9&v=JSAecH669C8&authuser=0)

---

## 📍Clone the repository:  

```bash
git clone https://github.com/nimradilawar/ComputerVision-2025
cd "ComputerVision-2025/CV25-Tutorial_1"
```

## ⚡ Requirements
```bash
pip install -r requirements.txt
```

## 💻 Commands
### Basic Run:
```bash
python main.py --input_folder "./images" --output_folder "./results"
```
### Custom paths:
```bash
python main.py --input_folder "path/to/input/folder" --output_folder "path/to/save/output/results"
```

### Help Menu:
```bash
python main.py --help
```

## 📂 Project Structure
``` bash
python-image-tutorial/
│── main.py                 # Entry point of the tutorial
│── Dataloader.py           # DataLoader class
│── Filters.py              # Filters class
│── Plotter.py              # Plotter class
│── images/                 # Input folder
│── results/                # Output folder
│── readme.md               # Documentation
│── requirements.txt        # Dependencies
```
