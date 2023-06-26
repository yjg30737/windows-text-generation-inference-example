import time
from text_generation import Client

client = Client("http://127.0.0.1:8080", timeout=30)
print(client.timeout)

text = ""
bef = time.time()
for response in client.generate_stream("What is Deep Learning?", max_new_tokens=17):
    if not response.token.special:
        text += response.token.text
        print(text)

aft = time.time()
print(aft-bef)