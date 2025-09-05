# Ubuntu-Inspired Image Fetcher 🖼️

**"I am because we are." – Ubuntu Philosophy**

This project is part of my **Python Libraries Assignment**.  
The goal of this program is to fetch images from the web and organize them locally, inspired by the Ubuntu philosophy of community, sharing, and respect.

---

## 📖 Description
This Python program allows a user to:
1. Input a URL of an image.
2. Download the image from the internet using the **`requests`** library.
3. Save the image in a dedicated folder called **`Fetched_Images`**.
4. Handle errors gracefully (e.g., network issues, invalid URLs).
5. Ensure the process respects and connects to the global web community.

The project reflects Ubuntu principles:
- **Community:** Connecting to the web to fetch shared resources.  
- **Respect:** Gracefully handling errors without crashing.  
- **Sharing:** Organizing downloaded images for future use.  
- **Practicality:** Creating a simple, functional, and helpful tool.  

---

## 🗂️ Project Structure
```

Ubuntu\_Requests/
│
├── Fetched\_Images/        # Folder where downloaded images are stored
│
├── fetch\_image.py          # Main Python script
│
└── README.md               # Project documentation

````

---

## 🚀 Features
- Downloads an image using its URL.
- Automatically creates the **`Fetched_Images`** folder if it doesn’t exist.
- Extracts the filename from the URL or generates a default filename.
- Graceful error handling for:
  - Bad URLs
  - Timeout issues
  - HTTP errors (e.g., 404, 500)
- Clear terminal feedback for every step.

---

## 💻 Technologies Used
- **Python 3**
- **Requests Library** – For fetching images from the internet.
- **os module** – For directory and file management.
- **urllib.parse** – To extract filenames from URLs.

---

## 🛠️ Installation & Setup
Follow these steps to run the program:

### **1. Clone the repository**
```bash
git clone https://github.com/<your-username>/Ubuntu_Requests.git
````

### **2. Navigate to the project folder**

```bash
cd Ubuntu_Requests
```

### **3. Install dependencies**

Make sure you have `requests` installed. If not, run:

```bash
pip install requests
```

### **4. Run the program**

```bash
python fetch_image.py
```

---

## 📝 Example Usage

**Terminal Output Example:**

```
Welcome to the Ubuntu Image Fetcher
A tool for mindfully collecting images from the web

Please enter the image URL: https://example.com/ubuntu-wallpaper.jpg
✓ Successfully fetched: ubuntu-wallpaper.jpg
✓ Image saved to Fetched_Images/ubuntu-wallpaper.jpg

Connection strengthened. Community enriched.
```

---

## 🧪 Challenge Extensions

These are optional features I plan to add:

1. **Multiple URL Support:** Allow downloading several images at once.
2. **Safety Measures:** Warn users before downloading from suspicious sources.
3. **Duplicate Prevention:** Avoid saving the same image twice.
4. **HTTP Header Checks:** Validate response headers before downloading files.

---

## 📌 Requirements

* Python 3.7+
* Internet connection
* The following Python library:

  * `requests`

Install dependencies with:

```bash
pip install requests
```

---

## 🗃️ GitHub Repository

You can find this project hosted on GitHub:
[**Ubuntu\_Requests Repository**](https://github.com/<your-username>/Ubuntu_Requests)

---

## 🧭 Evaluation Criteria

This project is graded based on:

* Correct and efficient use of the `requests` library.
* Error handling for network and file issues.
* Organized and well-documented code.
* Alignment with Ubuntu principles.

---

## ✨ Ubuntu Philosophy

> "A person is a person through other persons."
> This project represents that spirit by connecting with others' creations and organizing them for mindful appreciation.

---

## 🧑‍💻 Author

**Ian Kuria Kariuki**
GitHub: [@<iainkuria>](https://github.com/<iainkuria>)
