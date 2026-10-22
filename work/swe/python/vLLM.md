
## Definitions

### General
- **GEMM (General Matrix Multiply)**
  Part of BLAS. Kernel for general matrix multiplication. Used in linear layers.

- **W8A16 (Weight 8 Activations 16)**
  In general, quantization schemes can be described succintly as WXAY, which is read as "X bit weights, Y bit activations", meaning the weights are stored in memory with X bit datatypes, and inputs/outputs and computation is done in Y bits.

- **Prefill**
  The phase of model inference when inputs go through the forward pass.

### Benchmarking Metrics

End-to-end benchmarking metrics that measure performance of a setup. Usually given as a mean.

- **TTFT (Time to first token)**
  Time to first token (thinking or content both count). Measures the latency from the prefill phase.

- **TPOT (Time per output token)**
  Measures the average (single-stream) time between tokens during the decode phase (not including the first token). 
  
- **tok/s (Token throughput in tokens per second)**
  Measures the average (concurrent) tokens generated per second during the decode phase. Calculated as the total number of tokens generated across every stream divided by the time taken for the entire request (including prefill, scheduling, and tail time).


## Benchmarking

Results from running `vllm bench serve`. Standardized metrics to report for performance related PRs.

To run a benchmark on a given model (Qwen 3.8 27B) quickly, run:

```bash
vllm bench serve --model Qwen/Qwen3.8-27B-FP8
```

By default, `vllm bench serve` assumes that the API is located at `localhost` with port `8000`. This can be modified as follows (defaults shown):

```bash
vllm bench serve \
	--model Qwen/Qwen3.8-27B-FP8 \
	--host 127.0.0.1 \
	--port 8000 \
	--endpoint /v1/completions
```

To automate table generation, benchmark outputs can be saved to a json file with:

```bash
vllm bench serve --save-result --result-filename foo.json
```

Benchmarks run test inputs into the model, and the dataset can be changed with the following:

```bash
vllm bench --dataset-name random
```

| Dataset  | What is it?                                                                                                                                                                                             | Purpose                                                                    |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| Random   | Generates random token ids from the model's vocabulary with a specified length, and inputs them, and runs decode for a specified length.<br><br>Options: `--random-input-len` and `--random-output-len` | Used for general end to end on kernel, quantization, and long-context work |
| ShareGPT | Samples from `ShareGPT_V3_unfiltered_cleaned_split.json`                                                                                                                                                | Used for testing spec decode setups                                        |


## Serving models

```bash
vllm serve --model HuggingFace/model
```

vLLM supports serving a model with a yaml config (to remove the need for command args) like the following:

```bash
vllm serve --config config.yaml
```


## vLLM Execution Flow


## Pull Requests

### Testing

A sample "Test Plan" from a real vLLM [PR](https://github.com/vllm-project/vllm/pull/59082):

```bash
.venv/bin/python -P -m pytest -q \
  tests/kernels/attention/test_cpu_attn.py \
  tests/v1/attention/test_group_head_counts.py
.venv/bin/python -P -m pytest -s -v \
  tests/evals/mrcr/test_mrcr_correctness.py \
  --config-list-file="$MRCR_CONFIG_LIST"
```

```bash
vllm serve Qwen/Qwen3.5-4B --dtype bfloat16 \
  --kv-cache-dtype fp8 --max-model-len 128K \
  --no-enable-prefix-caching \
  --speculative-config '{"method":"mtp","num_speculative_tokens":3}'
# In another terminal:
vllm bench serve --backend openai --endpoint /v1/completions \
  --model Qwen/Qwen3.5-4B --dataset-name random \
  --random-input-len 100000 --random-output-len 1024 \
  --random-range-ratio 0 --request-rate inf \
  --max-concurrency 1 --num-prompts 1 --num-warmups 1 \
  --ignore-eos --temperature 0 --seed 1000
```

The standard shape is a correctness test and a performance benchmark.