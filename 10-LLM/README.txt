SERVER SIDE SETUP

https://github.com/ggerganov/llama.cpp/ - The aim of this repository, is to enable LLM inference locally.

cd llama.cpp && mkdir build && cd build
cmake ..
make -j4
cd bin

Model - mistral-7b-instruct-v0.2.Q4_K_M.gguf {https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.2-GGUF}

:~ export MODEL_PATH=/home/vishal/missing_semester/Exercise_10/llama.cpp/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf

:~ ./server -m ~/models/mistral-7b-instruct-v0.2.Q4_K_M.gguf --port 8080 -v -ngl 100 --api-key 1a2b3c4d5e6f7g8h9i0j


CLIENT SIDE SETUP

:~ python client_side.py http://127.0.0.1 --api_key 1a2b3c4d5e6f7g8h9i0j --mode helpful

