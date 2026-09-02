https://github.com/cordiverse/cordis

## A Programming Paradigm for Spatiotemporal Composability

### Introduction
- In software engineering, a ubiquitous concern is composition: creating complex systems from smaller building blocks.
	- For instance, classes are often built from smaller objects.
- Compile time composition is well-studied, but dynamic composition (composition during runtime) is not.
- In general, there is no unified framework for software to be built from components during runtime (plugin systems are implemented on a case-by-case basis, often with many drawbacks)
	- For instance, VSCode manages extensions during runtime with the Extension Host. When an extension is disabled (unless the extension doesn't have any effect on runtime state), the Extension Host must be reloaded.
- Proposition: Define 2 properties which would make runtime components easier to manage and solve problems: Temporal and Spatial Composability.
	- Temporal Composability: Components with side effects should have an inverse function which can revert its side effects when the component is disabled.
	- Spatial Composability: Components and dependencies between them should be reactively managed. Components should be able to expose themselves, declare their dependencies, and resolve them robustly.

## Agent Harnesses

Agent harnesses are often self-evolving. Since they accumulate changes rapidly and often without any human oversight, systems that don't implement dynamic composability well can experience problems, including expenses from the need to restart extension systems when components are added and removed.

## Cordis Library

- A plugin is defined as an object that implements the `Service` trait (can be a function with "inject" and "apply(ctx)" or subclass of `Service`).
- 