from transformers import AutoTokenizer, AutoModelForCausalLM
from functools import lru_cache


@lru_cache(maxsize=10)
def load_model():
    tokenizer = AutoTokenizer.from_pretrained(
        "../Book_Companion/hugging_face_models/cache/models--google--gemma-2b-it/snapshots/de144fb2268dee1066f515465df532c05e699d48/",
        low_cpu_mem_usage=True,
        local_files_only=True,
    )
    model = AutoModelForCausalLM.from_pretrained(
        "../Book_Companion/hugging_face_models/cache/models--google--gemma-2b-it/snapshots/de144fb2268dee1066f515465df532c05e699d48/",
        low_cpu_mem_usage=True,
        local_files_only=True,
    )
    return model, tokenizer


def generate_response(prompt, tokens=100):
    model, tokenizer = load_model()
    input_ids = tokenizer(prompt, return_tensors="pt")
    outputs = model.generate(**input_ids, max_new_tokens=tokens)
    return tokenizer.decode(outputs[0])