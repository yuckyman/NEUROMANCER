here’s a clean markdown guide you can keep in your vault and reference when you’re spinning up **gpt-oss-120B** on vast.ai:

---

# 🚀 running gpt-oss-120B on vast.ai

a step-by-step setup guide to get the 120B param model up and serving.

---

## 1. pick your vast.ai instance

requirements:

- **gpu**: h100-80gb or a100-80gb (1x or multi-gpu setup)
    
- **ram**: ≥ 128gb system memory
    
- **disk**: ≥ 250gb fast nvme ssd
    
- **network**: ssh access + optional public ip for api/webui
    

search filters on vast.ai:

```bash
gpu_name: H100_SXM or A100_80GB
disk_space: >= 250GB
cpu_ram: >= 128GB
```

---

## 2. launch & connect

1. deploy instance with ubuntu 22.04/24.04 base.
    
2. ssh in:
    

```bash
ssh -i ~/.ssh/your_key root@<instance_ip>
```

---

## 3. install dependencies

update + basics:

```bash
sudo apt update && sudo apt install -y \
  python3 python3-pip git build-essential
```

install nvidia drivers / cuda (if not preinstalled by template).  
optional: docker for containerized serving.

---

## 4. install gpt-oss + vllm

```bash
pip install torch transformers

# install vLLM build with gpt-oss support
pip install --pre vllm==0.10.1+gptoss \
  --extra-index-url https://wheels.vllm.ai/gpt-oss/ \
  --extra-index-url https://download.pytorch.org/whl/nightly/cu118
```

(adjust `cu118` to your cuda version.)

---

## 5. run the model

```bash
vllm serve openai/gpt-oss-120b \
  --host 0.0.0.0 \
  --port 8000 \
  --tensor-parallel-size <num_gpus>
```

- `--tensor-parallel-size`: set to number of gpus you reserved.
    
- model will expose an **openai-compatible api** at port 8000.
    

---

## 6. optional: add a webui

use [openwebui](https://github.com/open-webui/open-webui) or similar:

```bash
docker run -d -p 3000:3000 \
  -e OPENAI_API_BASE=http://localhost:8000/v1 \
  -e OPENAI_API_KEY=none \
  openwebui/openwebui:latest
```

now you have a browser ui at `http://<instance_ip>:3000`.

---

## 7. security & monitoring

- firewall / ufw: restrict ports 22, 8000, 3000 to your ip.
    
- log output: redirect `vllm serve` logs to a file.
    
- monitor gpu/ram usage:
    

```bash
watch -n 2 nvidia-smi
```

- set alerts or remember to **shut down instance when idle**.
    

---

## 8. snapshot for reuse

once stable:

```bash
# in vast.ai dashboard
create image snapshot
```

this saves time (no reinstall next spin-up).

---

## 9. notes & gotchas

- **cost**: h100/a100 80gb are pricey, watch idle time.
    
- **disk**: model weights are huge, don’t undersize disk.
    
- **latency**: throughput is slower than small models; use quantization if supported.
    
- **multi-gpu**: requires tensor parallel; bandwidth between gpus matters.
    

---

### quick test with curl

```bash
curl http://<instance_ip>:8000/v1/chat/completions \
  -H "Content-Type: application/json" \
  -d '{
    "model": "openai/gpt-oss-120b",
    "messages": [{"role":"user","content":"hello gpt-oss!"}]
  }'
```

---

would you like me to add a **budgeting table** (est. $/hr for h100 vs a100 setups on vast.ai) into this guide too?