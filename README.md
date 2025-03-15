⏰ Floating World Clock  

A simple, lightweight, and customizable floating world clock built with **Tkinter**.  
Displays multiple time zones, stays on top of other windows, and allows transparency adjustments.

![Demo Screenshot](assets\demo.jpg)

---

## 🚀 Features  
✅ Displays multiple time zones with customizable labels  
✅ Transparent, borderless window for a sleek look  
✅ Always stays on top of other windows  
✅ Drag to move anywhere on the screen  
✅ Right-click menu for adding time zones & adjusting transparency  
✅ Double-click on a time zone to remove it  
✅ Built-in **help menu** for quick reference  

---

## 💻 Installation  

### 🔹 Option 1: Run the Python Script  
Make sure you have **Python 3.x** installed.  

1️⃣ Install dependencies:  
```bash
pip install pytz
```
2️⃣ Run the script:  
```bash
python floating_clock.py
```

### 🔹 Option 2: Create a Windows Executable (.exe)  
To generate a standalone `.exe` file:  
```bash
pip install pyinstaller
pyinstaller --onefile --windowed floating_clock.py
```
Your `.exe` file will be in the `dist/` folder.

---

## 🛠️ Usage  
- **Move:** Click & drag the clock anywhere  
- **Right-click:** Open the menu  
- **Add Timezone** → Add a new world clock  
- **Transparency** → Adjust window transparency  
- **Help** → Open the help guide  
- **Exit** → Close the application  
- **Double-click:** Remove a time zone  

---

## 📂 Project Structure  
```
📁 FloatingClock/
│── 📄 floating_clock.py   # Main script
│── 📄 README.md           # Project documentation
│── 📁 assets/             # Optional (store icons, images)
│── 📄 .gitignore          # Ignore unnecessary files
```

---

## 🎯 To-Do / Future Features  
- [ ] Save & restore user preferences (position, time zones, transparency)  
- [ ] Add custom fonts & themes  
- [ ] Package as an installer for easier distribution  

---

## 🤝 Contributing  
Feel free to fork this repository and submit a pull request with enhancements!  

---
