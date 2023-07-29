import tkinter as tk
from PIL import Image, ImageTk

# Initialize the Tkinter window
window = tk.Tk()
window.title("Choose Your Own Adventure")
window.geometry("600x700")  # Adjust window size

# Function to load and resize an image
def load_image(filename):
    image = Image.open(filename)
    image = image.resize((500, 500), Image.BICUBIC)  # Adjust image size
    return ImageTk.PhotoImage(image)

# Load all images
start_img = load_image("Photos/Start.jpg")
middle1_img = load_image("Photos/Middle1.jpg")
middle2_img = load_image("Photos/Middle2.jpg")
good_ending_img = load_image("Photos/GoodEnding.jpg")
bad_ending_img = load_image("Photos/BadEnding.jpg")

# Create canvas and add Start image
canvas = tk.Canvas(window, width=500, height=500)  # Adjust canvas size
canvas.pack()
img_on_canvas = canvas.create_image(250, 250, anchor="center", image=start_img)  # Center image

# Create label for story text
story_text = tk.Label(window, text="", width=70, wraplength=600)  # Adjust text width
story_text.pack()

# Function to handle Start stage
def start():
    canvas.itemconfig(img_on_canvas, image=start_img)
    story_text.config(text="You are a detective trying to solve a mystery in a small town.")
    button1.config(text="Go to the Old Library", command=middle1)
    button2.config(text="Go to the Abandoned Mansion", command=middle2)
    button1.pack()
    button2.pack()

# Function to handle Middle1 stage
def middle1():
    canvas.itemconfig(img_on_canvas, image=middle1_img)
    story_text.config(text="You go to the Old Library and find an old map which you believe will lead you to the treasure.")
    button1.config(text="Follow the map", command=good_ending)
    button2.pack_forget()#Only one optoin at this stage

# Function to handle Middle2 stage
def middle2():
    canvas.itemconfig(img_on_canvas, image=middle2_img)
    story_text.config(text="You go to the Abandoned Mansion and get caught in a trap set by the thief.")
    button1.config(text="Continue investigating", command=bad_ending)
    button2.pack_forget()  # Only one option in this stage

# Function to handle GoodEnding stage
def good_ending():
    canvas.itemconfig(img_on_canvas, image=good_ending_img)
    story_text.config(text="You uncover hidden clues that lead you to the treasure and the thief.")
    button1.config(text="Start Again", command=start)
    button2.pack_forget()  # Only one option in this stage

# Function to handle BadEnding stage
def bad_ending():
    canvas.itemconfig(img_on_canvas, image=bad_ending_img)
    story_text.config(text="You end up in a trap or following a false map and the thief gets away with the treasure.")
    button1.config(text="Start Again", command=start)
    button2.pack_forget()  # Only one option in this stage

# Create option buttons
button1 = tk.Button(window)
button2 = tk.Button(window)

# Start the game
start()

# Start the Tkinter event loop
tk.mainloop()
