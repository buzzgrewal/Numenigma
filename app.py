import streamlit as st
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


@st.cache_resource
def load_model(model_path):
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(model_path)
    model.eval()
    return tokenizer, model

def generate_riddle(prompt, tokenizer, model, max_new_tokens=50, top_k=50, top_p=0.95):
    encoding = tokenizer(prompt, return_tensors="pt", padding="max_length", truncation=True, max_length=50)
    input_ids = encoding.input_ids
    attention_mask = encoding.attention_mask

    output_ids = model.generate(
        input_ids=input_ids,
        attention_mask=attention_mask,
        max_new_tokens=max_new_tokens,
        do_sample=True,         
        top_k=top_k,          
        top_p=top_p,            
        num_return_sequences=1, 
        pad_token_id=tokenizer.eos_token_id
    )
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

def main():
    st.title("🔢 Numenigma: Unlocking the Mysteries of Numbers")
    st.write("Spinning Mathematical Mysteries!")
    
    st.sidebar.header("Generation Settings")
    prompt = st.sidebar.text_area("Enter a prompt", "Riddle:")
    max_new_tokens = st.sidebar.slider("Max New Tokens", min_value=20, max_value=100, value=50)
    top_k = st.sidebar.slider("Top K", min_value=10, max_value=100, value=50)
    top_p = st.sidebar.slider("Top P", min_value=0.5, max_value=1.0, value=0.95)


    tokenizer, model = load_model("./fine_tuned_tinyllama")

    if st.sidebar.button("Generate Riddle"):
        with st.spinner("Generating riddle..."):
            result = generate_riddle(prompt, tokenizer, model, max_new_tokens, top_k, top_p)
            st.write("### Generated Riddle:")
            st.write(result)

if __name__ == '__main__':
    main()
