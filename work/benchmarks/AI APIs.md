## OpenAI

Steps for running models in Python:
1. Import openai, create .env file and read from them to use api keys
2. Create a client (example with deepseek as the model provider):
```
client = OpenAI(
	api_key=os.getenv("DEEPSEEK_API_KEY"),
	base_url="https://api.deepseek.com",
)
```
3. Generate response:
```
response = client.chat.completions.create(
	model=model_name,
	messages=[
		{"role": "system", "content": "You are a helpful assistant"},
		{"role": "user", "content": "Hello"}, 
	],
	max_tokens=1024,
	temperature=0.7,
	stream=False,
	reasoning_effort="high", # high/max
	extra_body={"thinking": {"type": "enabled"}} # enabled/disabled/adaptive
	logprobs=True
)
```

### Nonstreaming Response:

Example (... means the field is not that useful to know, or an omission of fields):
```
    ChatCompletion(
        id="10085e44-56e3-4b89-b1fa-2ccaf3b0895a",
        choices=[
            Choice(
                finish_reason="stop",
                index=0,
                logprobs=ChoiceLogprobs(
                    content=[
                        ChatCompletionTokenLogprob(
                            token="Hello",
                            bytes=[72, 101, 108, 108, 111],
                            logprob=-0.043201447,
                            top_logprobs=[],
                        ),
                        ...
                    ],
                    refusal=None,
                    reasoning_content=[
                        {
                            "token": "We",
                            "logprob": -0.0031337738,
                            "bytes": [87, 101],
                            "top_logprobs": [],
                        },
						...
                ),
                message=ChatCompletionMessage(
                    content="Hi there! How can I help you today? 😊",
                    refusal=None,
                    role="assistant",
                    annotations=None,
                    audio=None,
                    function_call=None,
                    tool_calls=None,
                    reasoning_content='We are asked: "Hello" We need to respond as the helpful assistant. So we should greet back and offer help. Just a simple friendly response.',
                ),
            )
        ],
        created=1782122979 (unix timestamp in seconds),
        model="deepseek-v4-pro",
		...
        system_fingerprint="fp_9954b31ca7_prod0820_fp8_kvcache_20260402", (This fingerprint represents the backend configuration that the model runs with.)
        ...
    )
```

To get the content of the message:
```
message_response = response.choices[0].message.content
reasoning = response.choices[0].message.reasoning_content
```

### Streaming Response

Creates an iterable of `ChatCompletionChunks`:
Example:

Reasoning Token:

```
ChatCompletionChunk(
	id="69b5df96-481a-402a-93ff-d4ef9d842e5c",
	choices=[
		Choice(
			delta=ChoiceDelta(
				content=None,
				function_call=None,
				refusal=None,
				role=None,
				tool_calls=None,
				reasoning_content="We",
			),
			finish_reason=None,
			index=0,
			logprobs=ChoiceLogprobs(
				content=None,
				refusal=None,
				reasoning_content=[
					{
						"token": "We",
						"logprob": -0.00048065186,
						"bytes": [87, 101],
						"top_logprobs": [],
					}
				],
			),
		)
	],
	...
)
```

To get the content of the message:
```
message_response = chunk.choices[0].delta.content
reasoning = chunk.choices[0].delta.reasoning_content
```

### Tool Calls

Source: https://developers.openai.com/api/docs/guides/tools


## Anthropic
