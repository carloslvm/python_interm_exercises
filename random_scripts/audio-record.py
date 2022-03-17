#!/usr/bin/python3

import os

"""
This script will record audio either from Mic or from
PC, or even from both devices.

Make sure to have ffmpeg on your system to use it.
"""


# Using pulseaudio and basic audio settings from system
use_pulse = "pulse "
device_input = "alsa_input.pci-0000_00_1b.0.analog-stereo "
device_monitor = "alsa_output.pci-0000_00_1b.0.analog-stereo.monitor "

# Specify Audio Channels
prompt_channel = "Enter the amount of audio channel (1 mono, 2 stereo): "
audio_channels = input(prompt_channel)

# Specify Audio rate
prompt_rate = "Enter audio sample rate: "
audio_rate = input(prompt_rate)

# Specify output format and name of the file
output = input("Enter output file name (i.e:file.wav, file.mp3, etc): ")

# Filter for mixing audio devices (input and output)
mix = " -filter_complex amix=inputs=2 "
ffmpeg = "ffmpeg -f "

########################################
# Recording audio from PC only
prompt_record = "Do you want to record your PC, Mic, or both? (p/m/b): "
record_mode = input(prompt_record)

# Audio monitoring properties section
monitoring_pro = "-ac " + audio_channels + " -ar " + audio_rate

# Device to record and output file
output_daudio = " -i " + device_monitor  + output

pc_record = ffmpeg + use_pulse + monitoring_pro + output_daudio
#print(pc_record)
########################################

########################################
# Recording Mic only

# Mic Properties
mic_pro = "-ac " + audio_channels + " -ar " + audio_rate

# Device to record and output file
output_maudio = " -i " + device_input + output

# Command to record audio from mic
mic_record = ffmpeg + use_pulse + mic_pro + output_maudio

########################################

########################################
# Recording both Mic and PC
mix_pc_mic = monitoring_pro + " -f " + use_pulse + mic_pro + mix

monitor = use_pulse + monitoring_pro + " -i " + device_monitor 
microphone = " -f " + use_pulse + mic_pro + " -i " + device_input

mix_record = ffmpeg + monitor + microphone + mix + output
########################################

# Executing command
if record_mode == "p":
    #print("\n" + pc_record)
    os.system(pc_record)
elif record_mode == "m":
    #print("\n" + mic_record)
    os.system(mic_record)
elif record_mode == "b":
    #print("\n" + mix_record)
    os.system(mix_record)
else:
    print("Unknown Command")


