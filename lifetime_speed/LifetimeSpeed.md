## Speed Racer

```C
uint64_t local() {
  uint64_t a;
  uint64_t b;
  empty();
  return a + b;
}
```

```asm
push   %rbp
mov    %rsp,%rbp
sub    $0x10,%rsp
call   404540 <_Z5emptyv>
mov    -0x8(%rbp),%rax
add    -0x10(%rbp),%rax
add    $0x10,%rsp
pop    %rbp
ret    
```

```C
uint64_t static_() {
  static uint64_t a;
  static uint64_t b;
  empty();
  return a + b;
}
```

```asm
push   %rbp
mov    %rsp,%rbp
call   404540 <_Z5emptyv>
mov    0x5e2558,%rax
add    0x5e2560,%rax
pop    %rbp
ret    
```
