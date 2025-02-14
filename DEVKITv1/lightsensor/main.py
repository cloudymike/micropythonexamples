
from machine import Pin, SPI, ADC
from time import sleep, sleep_ms

# Initialize ADC (Analog to Digital Converter)
adc = ADC(Pin(36))  # The ESP32 pin GPIO36 (ADC0) connected to the light sensor
# Set the ADC width (resolution) to 12 bits
adc.width(ADC.WIDTH_12BIT)
# Set the attenuation to 11 dB, allowing input range up to ~3.3V
adc.atten(ADC.ATTN_11DB)

while True:
    # Read the input on analog pin ADC0 (value between 0 and 4095)
    value = adc.read()  # Read the 12-bit ADC value directly
    print(f"Analog reading: {value} ")
    sleep_ms(1000)  # delay for 500 milliseconds
