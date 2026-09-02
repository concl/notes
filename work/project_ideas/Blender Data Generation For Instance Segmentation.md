
| Arbitrary approach                                | Fundamental approach                                                                                       |
| ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| "I downloaded random 3D models and rendered them" | "I used the geometric primitive basis set and procedural variation to isolate shape as a variable"         |
| "I used random textures I found online"           | "I used mathematically generated noise to ensure texture statistics are orthogonal to real-world data"     |
| "I placed objects by hand"                        | "I used physics simulation to generate occlusion and contact, which are the hard cases in segmentation"    |
| "I hope it works"                                 | "I am testing a specific hypothesis about shape bias vs. texture bias in pretraining for dense prediction" |

## Theoretical Basis

### Background

- DINO shows that self supervision with real data can learn interesting information. Can we augment models with synthetic data?
- CV models are biased to texture when trained on ImageNet, can we design an experiment to isolate shape as a pretraining objective with reasonable performance?

### Ideas

- Hypothesis based on fundamental observations on objects (Can we induce an inductive bias to better train models on computer vision tasks?):
	- Composition
	- Symmetry
	- Scale Coherence
	- Manifold Continuity
	- Background Subject Distinction
- We can test this by designing 2 data pipelines:
	- Primitives only, chaotic scenes (Spheres, Cubes, Cylinders, etc)
	- Scene construction with our inductive biases as a baseline.
	- Variables to control: texture will be mathematically generated