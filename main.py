import tkinter as tk
from PIL import Image, ImageTk
import os

gravity_constants = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Earth": 1.0,
    "Mars": 0.38,
    "Jupiter": 2.34,
    "Saturn": 1.06,
    "Uranus": 0.92,
    "Neptune": 1.19,
}


def get_image_path(image_name):
    current_dir = os.path.dirname(__file__)
    image_path = os.path.join(current_dir, "imagesPlanets", image_name)
    return image_path


root = tk.Tk()
root.title("Astro Mass")

bgImage = Image.open(get_image_path("galaxy.png"))
bgImage = bgImage.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
bgPhoto = ImageTk.PhotoImage(bgImage)

bgLabel = tk.Label(root, image=bgPhoto)
bgLabel.place(x=0, y=0, relwidth=1, relheight=1)

weight_label = tk.Label(
    root, text="Enter your weight on Earth (kg):", font=("Arial", 16))
weight_label.grid(row=0, column=0, columnspan=4,
                  padx=10, pady=5, sticky="nsew")

weight_entry = tk.Entry(root, font=("Arial", 16))
weight_entry.grid(row=1, column=0, columnspan=4,
                  padx=10, pady=5, sticky="nsew")


planet_vars = {}
for i, planet in enumerate(["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]):
    var = tk.IntVar()
    planet_vars[planet] = var

    image = Image.open(get_image_path(f"{planet.lower()}.jpg"))
    image = image.resize((160, 160))
    photo = ImageTk.PhotoImage(image)

    checkbox = tk.Checkbutton(root, text=planet, variable=var,
                              image=photo, compound=tk.TOP, font=("Arial", 12, "bold"))
    checkbox.image = photo  # To prevent garbage collection of the image

    row = (i // 4) + 2
    column = i % 4
    checkbox.grid(row=row, column=column, padx=10, pady=5)


def calculate_weight():
    try:
        weight = float(weight_entry.get())
        selected_planets = [planet for planet,
                            var in planet_vars.items() if var.get() == 1]

        if selected_planets:
            result_text.delete(1.0, tk.END)  # Clear previous content
            for planet in selected_planets:
                gravity = gravity_constants[planet]
                new_weight = weight * gravity
                result_text.insert(
                    tk.END, f"Your weight on {planet} would be {new_weight:.2f} kg\n")
        else:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, "Please select at least one planet")

    except ValueError:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please enter a valid weight")


calculate_button = tk.Button(root, text="Calculate", font=(
    "Arial", 16), command=calculate_weight, bg="#4CAF50", fg="white", relief=tk.FLAT)
calculate_button.grid(row=4, column=0, columnspan=4,
                      padx=10, pady=10, sticky="nsew")

result_text = tk.Text(root, font=("Arial", 16), wrap=tk.WORD, height=8)
result_text.grid(row=5, column=0, columnspan=4, padx=10, pady=5, sticky="nsew")


root.mainloop()
