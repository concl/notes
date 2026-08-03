
## Matching

A regex is a pattern that can match parts of a string. In the simplest form, it consists of ascii characters (most of which match themselves) and quantifiers.

For instance the regex `test` matches exactly substrings that are `test`.

The rest of the notes cover the `re` library in python.

---

Quantifiers are special characters that specify things like repeated matching, sets, and complements.

The full list of quantifier characters are:
```
. ^ $ * + ? { } [ ] \ | ( )
```

---

The most important quantifier is `\`, which can allow every other quantifier including itself to be expressed literally (i.e. the pattern `\\` or `\[` matches `\` or `[` respectively), and also has some other special meanings.

---

The second most important qualifiers are `[ ]`, which specify a set of characters that can be matched. For instance the regex: `[abc]` matches either a, b, or c. Using `^` can complement the set i.e. `[^abc]` matches anything but a, b, or c.

---
## Repetitions

`*` matches any number of the preceding object (which can be a character or set). `+` matches one or more of the preceding object. `?` matches 0 or 1 of the preceding object (can be thought of as the thing being optional). `{m, n}` matches at least `m` times and at most `n` times.

Examples:
`[abc]*` matches `abcababacab` but not `aaaas`.
`5+` matches `5555` but not the empty string.

Behavior:
For expressions like this, the engine matches greedily, meaning that it tries to match as many of the previous object as possible or permitted, and backtracking if a match isnt found after.

In order to make this lazy (not greedy), add a ? at the end of the quantifier
Example:
`a+?` matches 1 or more `a` characters but tries to match as little as possible.

---
## Groups

`()` groups up subexpressions to be used with the other quantifiers. It can be used with matches to get the substrings and such that are matched (to access individual groups in a regex).

Example:
`(ab)+` matches repetitions of "ab", so `abababab` but not `abababa`
`([a-c]d)+` matches repetitions of characters from a-c and then a d following, i.e. `adbdcd`


The `(?...)` syntax denotes special properties for the group.

For example:
- `(?P=<name>...)` denotes a group with the name `name`, which can be used to extract parts of matches.

- `(?=...)`  is a lookahead assertion (useful for splitting strings without consuming), and it causes a match if and only if there is a match for `...` after the current match.
	- Example: `Isaac (?=Asimov)` matches `Isaac ` iff it is followed by `Asimov` 
- `(?:...)` is a non capturing group.
---

`.` matches any character except newlines. However, if `re.DOTALL` is passed, then it also matches newline characters.

---
## Using Patterns

We can compile regexes in python like the following (note that we use the r"foo" notation for raw strings so we dont have to escape backslashes):
```
import re

pattern = re.compile(r"test[1-4]+")
```

Once a pattern is compiled it can be used in the following ways:

| Method                | Purpose                                                                   |
| --------------------- | ------------------------------------------------------------------------- |
| `pattern.match(s)`    | Determine if the RE matches at the beginning of the string.               |
| `pattern.search(s)`   | Scan through a string, looking for any location where this RE matches.    |
| `pattern.findall(s)`  | Find all substrings where the RE matches, and returns them as a list.     |
| `pattern.finditer(s)` | Find all substrings where the RE matches, and returns them as an iterator |
match and search return `None` if nothing can be found, otherwise they return `Match` objects (which can be used as boolean objects as `True`)

One thing that `Match` objects can do is return the indices of where they matched in the string:
`match.start()`, `match.end()` return the indices `[l, r)` where the pattern matched. For instance if you have the pattern `patt = r"remove_this"`, you can do:
```
s = "john@exremove_thisample.com"
patt = r"remove_this"
match = re.search(patt, s)
cleaned = s[:match.start()] + s[match.end():]
print(cleaned)
```

In this case `cleaned` is equal to `john@example.com`.

Another thing they can do is the `group()` method where `match.group()` returns the entire string matched and `matched.group(i)` returns the `i`th subgroup in the pattern, (with the `()` quantifiers). 


## Modifying Strings

| Method                        | Purpose                                                                                                                            |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| `pattern.split(s)`            | Splits the string wherever the pattern matches (greedily) and returns a list of the non matching parts. (The matches are consumed) |
| `pattern.sub(replacement, s)` | Replaces matches in `s` with `replacement`                                                                                         |


