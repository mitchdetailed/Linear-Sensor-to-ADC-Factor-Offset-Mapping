import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("CAN Expander Conversion Tool")

# Create a tab control

map_tab = ttk.Frame(root)
map_tab.pack(pady=10)
slope_offset_tab = ttk.Frame(root)
slope_offset_tab.pack(pady=10)

# Map Function content for the first tab
def map_value():
    s_inv_low = float(s_in_v_lowpoint_entry.get())
    s_in_peripheralunit_low = float(s_in_peripheralunit_low_entry.get())
    s_inv_high = float(s_in_v_highpoint_entry.get())
    s_in_peripheralunit_high = float(s_in_peripheralunit_high_entry.get())
    in_min = float(expander_vin_min_entry.get())
    in_max = float(expander_vin_max_entry.get())
    out_min = float(expander_adc_min_entry.get())
    out_max = float(expander_adc_max_entry.get())
    lowpoint_CAN_result = int(round(((s_inv_low - in_min) * (out_max - out_min) / (in_max - in_min) + out_min), 0))
    highpoint_CAN_result = int(round(((s_inv_high - in_min) * (out_max - out_min) / (in_max - in_min) + out_min), 0))
    m = (s_in_peripheralunit_high - s_in_peripheralunit_low) / (highpoint_CAN_result - lowpoint_CAN_result)
    b = s_in_peripheralunit_low - m * lowpoint_CAN_result

    result_label.config(text=f"Factor: {m:.8f}, Offset: {b:.8f}")

labels_texts = ["Sensor Input Voltage Low Point Value","Sensor Input Scaled Unit Low Point Value", "Sensor Input Voltage High Point Value","Sensor Input Scaled Unit High Point Value", "Expander Input Voltage Minimum", "Expander Input Voltage Maximum", "Expander CAN Output Minimum", "Expander CAN Output Maximum"]
entries = []

for index, text in enumerate(labels_texts):
    label = ttk.Label(map_tab, text=text)
    label.grid(row=index, column=0, padx=20, pady=10)
    
    entry = ttk.Entry(map_tab)
    entry.grid(row=index, column=1, padx=20, pady=10)
    entries.append(entry)

s_in_v_lowpoint_entry, s_in_peripheralunit_low_entry, s_in_v_highpoint_entry, s_in_peripheralunit_high_entry, \
    expander_vin_min_entry, expander_vin_max_entry, expander_adc_min_entry, expander_adc_max_entry = entries
map_button = ttk.Button(map_tab, text="Map", command=map_value)
map_button.grid(row=11, column=0, columnspan=2, pady=20)
result_label = ttk.Label(map_tab, text="Slope and Offset:")
result_label.grid(row=12, column=0, columnspan=2, pady=20)

root.mainloop()