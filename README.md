# Mad Libs Story Generator

This is a **Mad Libs Story Generator** built using **Streamlit** and **Google Gemini AI**. The app allows users to generate short AI-based stories or predefined logic-based stories by entering a **noun, adjective, and verb**.

---

## Features
- 🎨 **Interactive UI** with a modern and clean design
- 🤖 **AI-generated stories** using Google Gemini API
- 🔄 **Logic-based story generator** (without AI)
- 📝 **Simple word input fields** with validation
- 🚀 **Fast and responsive design** built with Streamlit

---

## Installation & Setup
This project uses `uv` for dependency management.

### 1️⃣ Install `uv` (if not installed)
```bash
pip install uv
```

### 2️⃣ Clone the repository
```bash
git clone https://github.com/muzaffar401/AI_Mad_Libs_Story_Generator.git
cd mad-libs-story-generator
```

### 3️⃣ Install dependencies using `uv`
```bash
uv venv   # Create a virtual environment
uv pip install -r requirements.txt  # Install dependencies
```

### 4️⃣ Get Your Google Gemini API Key
To use AI-generated stories, you need a **Google Gemini API Key**:
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Navigate to the **API Keys** section
4. Generate a new API key and copy it

Then, create a `.env` file in your project folder and add:
```
GEMINI_API_KEY=your-api-key-here
```

---

## How to Run the Project
Once everything is set up, run the app with:
```bash
uv run streamlit run app.py
```

This will start the Streamlit web app. Open the **localhost link** in your browser to start generating stories!

---

## Usage Guide
1. Enter a **noun, adjective, and verb** in the respective fields.
2. Choose the **story type** (AI-generated or Logic-based).
3. Click the **"✨ Generate Story"** button.
4. The generated story will be displayed in a styled box.
5. If AI is selected, it will use the Google Gemini API to generate a creative response.

---

## Example Output
**Input:**
- Noun: *dog*
- Adjective: *happy*
- Verb: *runs*

**Output (AI-generated):**
> "The happy dog runs through the golden fields, chasing the sunset with joy."

**Output (Logic-based):**
> "One fine morning, a happy dog decided to run through the bustling city, marveling at the sights and sounds of the world coming to life."

---

## Contributing
If you'd like to contribute or improve the project, feel free to fork the repo and submit a pull request! 🚀

---

## License
This project is open-source and available under the **MIT License**.

