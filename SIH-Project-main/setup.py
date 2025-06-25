import ollama

def setup_models():
    print("Pulling LLaVA model...")
    ollama.pull('llava')

    print("Pulling LLaMA 3.1 model...")
    ollama.pull('llama3.1')

if __name__ == "__main__":
    setup_models()
