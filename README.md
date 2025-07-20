# Transformation-Simulator



This repository contains a collection of Python scripts that demonstrate **2D geometric transformations** on points and shapes (especially triangles). It is designed for educational use, particularly in computer graphics, image processing, or linear algebra contexts.

All transformations are implemented using **NumPy** matrices and can be executed interactively from the terminal.

---

## 📂 Contents

| File Name               | Description |
|------------------------|-------------|
| `composite.py`         | Apply one or more transformations (scale, rotate, translate) to a point or triangle |
| `shear.py`             | Apply horizontal or vertical shearing transformation |
| `reflect.py`           | Reflect a shape over X-axis, Y-axis, or origin |
| `matrix_chain.py`      | Show how the order of matrix multiplication affects the final result |
| `draw_transform.py`    | Visualize original and transformed triangles using Matplotlib |
| `identity.py`          | Demonstrate the identity matrix (no transformation) |
| `centroid_translate.py`| Translate a shape so its centroid moves to the origin |
| `composite_sequence.py`| Apply a sequence of transformations step-by-step |
| `transform_anim.py`    | Animate rotation of a triangle using Matplotlib |
| `custom_matrix.py`     | Accept user-defined 3×3 transformation matrix and apply to a point |

---

## 🚀 Getting Started

### ✅ Requirements

- Python 3.x
- `numpy`
- `matplotlib` (only for visualization scripts)

Install them using:


pip install numpy matplotlib
🧪 Running the Scripts
You can run each script independently using:


python script_name.py
Example:


python composite.py
Each script will prompt you for the necessary input (coordinates, angles, scaling factors, etc.) and display the result in text or graphical form.

📘 Examples of Use
composite.py
→ Apply scaling, then rotation, then translation to a triangle.

shear.py
→ Apply X and Y shear to a triangle and observe coordinates.

draw_transform.py
→ See the triangle rotate in real time.

custom_matrix.py
→ Apply any custom 3×3 transformation matrix to a point.

🧠 Educational Objectives
This toolkit is ideal for:

Learning affine transformations

Understanding matrix multiplication

Practicing coordinate geometry

Visualizing the effect of combined transformations

📄 License
This project is open-source and released under the MIT License.

🙋‍♂️ Author
Developed as part of an academic assignment to demonstrate foundational concepts in 2D graphics and transformation mathematics using Python.
