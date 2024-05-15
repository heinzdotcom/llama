from example_chat_completion import max_batch_size, max_seq_len, tokenizer_path
from llama import Llama


generator = Llama.build(
        ckpt_dir=ckpt_dir,
        tokenizer_path=tokenizer_path,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
    )