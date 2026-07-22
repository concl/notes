https://developer.mozilla.org/en-US/docs/Web/CSS

CSS is the main way to style website 

## Basic Box Model

Boxes have an outer display type and inner display type.
- Outer display type: controls how the element is laid out with respect to other elements next to it
	- `display: block`, `display: inline`
- 

## Properties

`display: <outer> <inner>` Used to control the outer display type and inner display type
Example: `display: block flex` creates a flexbox (inner display type) that is displayed relative to other elements of its level as a block.

### Variables

Variables can be used as inputs to properties to make things like standard colors easier.

We can define a variable like so:
```
:root {
	--foo: #000000;
	--radius: 8px;
}
```
and access it later like:
```
.card-thing {
	background: var(--foo);
}
```
## Animations




## Flex Boxes

