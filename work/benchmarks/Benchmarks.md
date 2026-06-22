- SWE bench is the main benchmark for agents
	- Other benchmarks: deepswe, 



## Benchmarking Runs

Benchmarking runs start with selecting:
- A type of task (agents, chat, etc.)
- For agents (explained in [[Agents]]) :
	- One or more benchmarks for the field
		- swe bench, code arena?, deepswe?
	- One or more agent harnesses
		- claude code
		- openclaw
	- One or more llms
		- deepseek
		- gpt
		- claude

Benchmarking runs should have the following:
- Results
- Logs
	- i.e. model output, stderr
	- good for debugging issues
- Metadata
	- i.e. OS, hardware