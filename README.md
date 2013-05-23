pypoo
=====

## Thoughts

We are interested in:

- memory dependencies *between* basic blocks
- conditional dependencies

Do we need a full taint tracking framework? What we really need is:

- memory operations by the basic blocks
- memory dependencies of conditionals

Basically, we need to add taint tracking and conditionals analysis to lackey.


Several types of data movements:

Registers:

- immediate to register
- register to register


Memory:

- immediate to memory
- memory to register
- register to memory


Pointers:

- What here?

### Output format:

[ TYPE, instruction, [ input locations ], [ output locations ] ]

```
mov eax, $10	# [ IM-REG, mov, [ ], [ eax ] ]
mov ebx, eax	# [ REG-REG, mov, [ eax ], [ ebx ] ]
mov (ecx), ebx  # [ REG-MEM, mov, [ ebx ], [ *ecx ] ]
or eax, ebx	# [ REG-REG, or, [ ebx ], [ eax ] ]

cmp eax, ecx	# [ REG, cmp, [ eax, ecx ], [ Z ] ]
je edx		# [ REG, je, [ edx ], [ eip ] ]
ret		# [ REG, ret, [ *esp ], [ eip ] ]
```

Alternative: only report memory taint immediately. Track register taint until it's actually used in a computation or output and report it then. THe above would be:

```
push   rbp				# [ REG-MEM, push, [ rbp ], [ *rsp ] ]
mov    rbp,rsp				# (tracked internally)
mov    DWORD PTR [rbp-0x4],edi		# [ REG-MEM, mov, [ edi ], [ *rbp-0x4 ] ]
cmp    DWORD PTR [rbp-0x4],0x9		# [ MEM-REG, cmp, [ *rbp-0x4 ], [ Z ] ]
jg     4004c8 <asdf+0x14>		# [ CB, jg ]
mov    eax,0x1				# ( tracked internally)
jmp    4004cb <asdf+0x17>		# [ CB, jg ]
mov    eax,DWORD PTR [rbp-0x4]		# (tracked internally)
pop    rbp				# [ MEM-REG, pop,  [ *rsp ], rbp ]
ret    					# [ B, ret ]
```

Issues:

- probably insane overhead (thousands of times slower?)
- syscall wrapping?
- library functions
-- tradeoff of speed versus missing stuff
-- maybe implement wrappers for commonly-used ones (wouldn't work for statically compiled code unless IDA identifies them)
