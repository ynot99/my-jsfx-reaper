# Ynot99's REAPER JSFX Collection

This repository will store various MIDI and audio effects designed to extend REAPER's capabilities.

## 🎹 Available Plugins

* **[Circle of Fifths Analyzer](./CircleOfFifthAnalyzer/)**
  An interactive Circle of Fifths visualizer and MIDI chord generator. It allows you to visually analyze keys and click on the circle to play chords, select chord types, add extensions (7ths, 9ths), and automate parameters.

* **[MIDI Channel Filter](./MIDIChannelFilter/)**
  A lightweight MIDI filter that isolates and passes through notes from a specific user-selected MIDI channel. Perfect for selective arpeggiation or routing specific chord notes to independent VST instruments on the same track.

## 📥 How to Install

To add these plugins to your REAPER:

1. Open REAPER.
2. In the top menu, go to **`Options`** > **`Show REAPER resource path in explorer/finder...`**
3. In the opened folder, find and open the **`Effects`** directory.
4. Copy the desired plugin folder (e.g., `CircleOfFifthAnalyzer`) into the `Effects` folder.
5. Go back to REAPER and open the **`FX Browser`** (or press `Shift + F`).
6. Right-click in the left panel of the FX Browser and select **`Scan for new plugins`** (or press `F5`).
7. Find the plugin by name (usually located in the `JS` category) and add it to your desired track!

*Note: for MIDI effects (like the Circle of Fifths Analyzer), make sure to put them BEFORE a virtual instrument (VSTi/AUi/CLAP synth) in the FX chain, otherwise there will be no sound.*
