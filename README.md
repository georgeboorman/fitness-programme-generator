# Fitness programme generator
Streamlit app powered by an open-source LLM (Llama 3.2:1b) to generate fitness programmes.

Check out the app [here](https://georgeboorman-fitness-programme-generator-main-j899qo.streamlit.app/).

# Steps to recreate
1. Clone the repo
```
git clone https://github.com/georgeboorman/fitness-programme-generator.git
```

2. Install Ollama
Mac:
```
brew install ollama
```
Windows: Visit [here](https://ollama.com/download)

3. Pull the model (e.g., Llama 3.2:1b)
See [here]() for all available models
```
ollama pull llama3.2:1b
```

4. Set up a virtual environment
```
python3 -m venv .venv
```

5. Activate virtual environment
```
source .venv/bin/activate
```

6. Install packages
```
pip3 install -r requirements.txt
```

7. Test Streamlit app
```
streamlit run main.py
```

8. Close the app
```
Ctrl + C
```

9. Deactivate virtual environment
```
deactivate
```