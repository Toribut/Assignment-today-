# Step 1: Read smart meter readings from a file
with open('meter_readings.txt', 'r') as file_handle:
    readings = file_handle.readlines()

# Convert string readings to float
readings = [float(reading.strip()) for reading in readings]

# Step 2: Process the readings
average = sum(readings) / len(readings)

# Step 3: Write the average to a summary file
with open('summary.txt', 'w') as file_handle:
    file_handle.write(f'Average Meter Reading: {average:.2f}\n')