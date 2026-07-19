Before submitting code to programming contests check the following:

Most Important  (step by step):
1. Make sure sample test cases are completely correct (pay extra attention to formatting)
2. 64 bit integer overflow (any usage of 32 bit integers can be problematic)
	- The pattern `1 << bits` can easily overflow as the literal `1` is 32 bit. Use: `1LL << bits` for 64 bits.
3. **Bitwise order of ops**: Very important. `x & 1 == 0` always evaluates to 0 since `1 == 0` comes first. Use `(x & 1) == 0`. In general use many brackets when working with bitwise ops.
4. Make sure you used modulo operations everywhere if necessary



Others: