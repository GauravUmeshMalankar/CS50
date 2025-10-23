


"""

import tkinter as tk

class NumberInputGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Number Input GUI")
        
        # Create input fields
        self.input_labels = []
        self.input_entries = []
        for i in range(5):
            label = tk.Label(self.window, text=f"Enter number {i+1}: ")
            label.grid(row=i, column=0)
            entry = tk.Entry(self.window)
            entry.grid(row=i, column=1)
            self.input_labels.append(label)
            self.input_entries.append(entry)
        
        # Create display fields
        self.result_labels = []
        for i, label_text in enumerate(["Numbers: ", "Addition: ", "Average: "]):
            label = tk.Label(self.window, text=label_text)
            label.grid(row=5, column=i*2)
            result_label = tk.Label(self.window, text="")
            result_label.grid(row=5, column=i*2+1)
            self.result_labels.append(result_label)
        
        # Create button to calculate results
        calculate_button = tk.Button(self.window, text="Calculate", command=self.calculate)
        calculate_button.grid(row=6, column=0)
        
        # Run GUI loop
        self.window.mainloop()
    
    def calculate(self):
        # Get input values
        numbers = []
        for entry in self.input_entries:
            try:
                number = int(entry.get())
            except ValueError:
                self.result_labels[0].config(text="Invalid input")
                self.result_labels[1].config(text="")
                self.result_labels[2].config(text="")
                return
            numbers.append(number)
        
        # Calculate and display results
        self.result_labels[0].config(text="Numbers: " + ", ".join(str(n) for n in numbers))
        self.result_labels[1].config(text="Addition: " + str(sum(numbers)))
        self.result_labels[2].config(text="Average: " + str(sum(numbers) / len(numbers)))

# Create and run the GUI
NumberInputGUI()


"""

import tkinter as tk

# Create window
window = tk.Tk()
window.title("Number Input GUI")

# Create input fields
input_labels = []
input_entries = []
for i in range(5):
    label = tk.Label(window, text=f"Enter number {i+1}: ")
    label.grid(row=i, column=0)
    entry = tk.Entry(window)
    entry.grid(row=i, column=1)
    input_labels.append(label)
    input_entries.append(entry)

# Create display fields
result_labels = []
for i, label_text in enumerate(["Numbers: ", "Addition: ", "Average: "]):
    label = tk.Label(window, text=label_text)
    label.grid(row=5, column=i*2)
    result_label = tk.Label(window, text="")
    result_label.grid(row=5, column=i*2+1)
    result_labels.append(result_label)

# Create button to calculate results
def calculate():
    # Get input values
    numbers = []
    for entry in input_entries:
        number = int(entry.get())
        numbers.append(number)

    # Calculate and display results
    result_labels[0].config(text="Numbers: " + ", ".join(str(n) for n in numbers))
    result_labels[1].config(text="Addition: " + str(sum(numbers)))
    result_labels[2].config(text="Average: " + str(sum(numbers) / len(numbers)))

calculate_button = tk.Button(window, text="Calculate", command=calculate)
calculate_button.grid(row=6, column=0)

# Run GUI loop
window.mainloop()
















      

