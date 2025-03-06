# Numenigma: Crafting Math Riddles with TinyLlama

Welcome to **Numenigma** – a fun, creative project that harnesses the power of a fine-tuned TinyLlama model to generate intriguing math riddles! This project combines natural language processing (NLP) with mathematical puzzles to deliver engaging and clever riddle-generation capabilities.

---

## Table of Contents

- [Overview](#overview)
- [Why TinyLlama?](#why-tinyllama)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Dataset](#dataset)
- [Fine-Tuning](#fine-tuning)
- [Streamlit Interface](#streamlit-interface)
- [Links & Resources](#links--resources)
- [Contributing](#contributing)
- [License](#license)
- [Hashtags](#hashtags)

---

## Overview

**Numenigma** is a project designed to automatically generate complete math riddles – each featuring both a challenging question and its corresponding answer. The project is divided into three main phases:

1. **Dataset Creation:** We prepared a CSV dataset containing 50 unique math riddles.
2. **Model Fine-Tuning:** We fine-tuned the lightweight TinyLlama model using PyTorch and the Hugging Face Transformers library.
3. **Interactive Testing:** A user-friendly Streamlit interface allows you to generate and test new math riddles on the fly.

---

## Why TinyLlama?

TinyLlama is chosen for its balance of efficiency and performance:
- **Lightweight & Fast:** Suitable for low-resource environments and rapid experimentation.
- **Efficient Fine-Tuning:** Its smaller architecture allows for quick fine-tuning on custom datasets.
- **Transformer-based:** Uses self-attention mechanisms to generate coherent and creative text.

### How It Works

TinyLlama processes text by converting words into embeddings, applying self-attention across multiple layers, and then generating output tokens based on learned patterns. When fine-tuned on our math riddle dataset, it learns the structure and style needed to craft both the riddle and its answer.

---

## Project Structure

```
Numenigma/
├── Numenigma.ipynb       # Notebook File
├── riddlesfactory.csv    # CSV file with 50 math riddles (Riddle column and Answer column)     
├── app.py                # Streamlit interface for interactive riddle generation
├── README.md             # This file
└── requirements.txt      # Python dependencies
```

---

## Installation

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/buzzgrewal/numenigma.git
   cd numenigma
   ```

2. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   *Example content for `requirements.txt`:*
   ```txt
   torch
   transformers
   pandas
   streamlit
   ```

---

## Dataset

The dataset is stored in `riddlefactory.csv` and should have the following format:

```csv
Riddle,Answer
"What number becomes zero when you subtract 15 from half of it?",30
...
```

Each entry contains a math riddle along with its answer. During fine-tuning, the riddle is formatted into a prompt (e.g., `"Riddle: <riddle_text>"`) that the model uses to learn the complete structure.

---

## Fine-Tuning

To fine-tune TinyLlama on our custom dataset, use the  `Numenigma.ipynb` file:



### Key Points:
- **Dataset Splitting:** The script splits the data into training (80%) and validation (20%) sets.
- **Hyperparameter Tuning:** Adjust learning rate, weight decay, warmup steps, and other parameters for optimal performance.
- **Randomization:** Training data is shuffled each epoch to maximize learning on our small dataset.


---

## Streamlit Interface

For an interactive experience, run the Streamlit interface:

```bash
streamlit run app.py
```

### Features:
- **Custom Prompt:** Enter your own prompt (e.g., "Generate a math riddle:") to guide the model.
- **Adjustable Parameters:** Modify `max_new_tokens`, `top_k`, and `top_p` to influence generation length and diversity.
- **Real-Time Generation:** View the generated math riddle instantly on the web interface.

---

## Links & Resources

- **GitHub Repository:** [https://github.com/buzzgrewal/numenigma](https://github.com/buzzgrewal/numenigma)
- **Kaggle Notebook:** [https://www.kaggle.com/yourusername/numenigma](https://www.kaggle.com/yourusername/numenigma)
- **Hugging Face Transformers Docs:** [https://huggingface.co/transformers/](https://huggingface.co/transformers/)

---

## Contributing

Contributions are welcome! If you have suggestions, improvements, or bug fixes, please open an issue or submit a pull request. Follow the repository's contribution guidelines to get started.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Hashtags

#Numenigma #MathRiddles #TinyLlama #NLP #MachineLearning #DeepLearning #AI #Streamlit #MathPuzzles #TechArt


---

## Conclusion

**Numenigma** showcases how a lightweight model like TinyLlama can be fine-tuned to generate creative, engaging math riddles. Whether you’re a math enthusiast or an AI hobbyist, this project is a fun demonstration of blending technology with creativity. Enjoy exploring, and feel free to contribute or fork the project for your own experiments!

Happy riddle crafting! 🔢✨

---
