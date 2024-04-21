import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
from tkinter import messagebox
def calculate_area(image_path):
    if not image_path:
        return 0
    image = cv2.imread(image_path)
    if image is None:
        return 0
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    total_area = 0
    for contour in contours:
        area = cv2.contourArea(contour)
        total_area += area
    return total_area
def calculate_seed_amount(area, seed_density):
    # Seed density is seeds per unit area
    seed_amount = area * seed_density
    return seed_amount
def browse_image():
    filename = filedialog.askopenfilename(title="Select Image", filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if filename:
        entry_image.delete(0, tk.END)
        entry_image.insert(0, filename)
        show_image(filename)
def show_image(image_path):
    if not image_path:
        return
    image = cv2.imread(image_path)
    if image is None:
        return
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    height, width, _ = image.shape
    image = cv2.resize(image, (int(width * 0.3), int(height * 0.3)))
    image = ImageTk.PhotoImage(image=Image.fromarray(image))
    label_image.config(image=image)
    label_image.image = image
def calculate():
    if entry_density.get() == "":
        messagebox.showerror("Error", "No density given")
        return
    image_path = entry_image.get()
    land_area = calculate_area(image_path)
    seed_density = int(entry_density.get())
    seed_amount = calculate_seed_amount(land_area, seed_density)
    label_result.config(text=f"Total area of the land: {land_area} square meters\nApproximate amount of seeds/plants needed: {seed_amount} seeds/plants")
root = tk.Tk()
root.title("Crop Seed Calculator")
root.geometry("900x300+300+200")
root.configure(bg="light cyan")
icon = ImageTk.PhotoImage(file="iconfinal.png")
root.iconphoto(True, icon)
label_image_path = tk.Label(root, text="Image Path:", font=("arial", 15), bg="yellow")
label_image_path.grid(row=0, column=0, padx=5, pady=5)
entry_image = tk.Entry(root, width=50)
entry_image.grid(row=0, column=1, padx=5, pady=5)
button_browse = tk.Button(root, text="Browse", command=browse_image, font=("arial", 10), bg="magenta", cursor="hand2", activebackground="black", activeforeground="white")
button_browse.grid(row=0, column=2, padx=5, pady=5)
label_image = tk.Label(root)
label_image.grid(row=1, column=0, columnspan=3, padx=5, pady=5)
label_density = tk.Label(root, text="Seed Density (seeds/square meter):", font=("arial", 15), bg="lemon chiffon")
label_density.grid(row=2, column=0, padx=5, pady=5)
entry_density = tk.Entry(root)
entry_density.grid(row=2, column=1, padx=5, pady=5)
button_calculate = tk.Button(root, text="Calculate", command=calculate, font=("arial", 10), bg="red", cursor="hand2", activeforeground="pink", activebackground="ghost white")
button_calculate.grid(row=2, column=2, padx=5, pady=5)
label_result = tk.Label(root, wraplength=300)
label_result.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
root.mainloop()



