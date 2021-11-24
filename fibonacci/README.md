# How to Run the code Online

[Source Code](fibonacci.asm)

There are two methods of running the code online

- https://onecompiler.com/assembly (Fastest Way)
- https://replit.com/ (Required Way)


Make sure the file is saved as fibonacci.asm

## Method One
```
Just paste the code in https://onecompiler.com/assembly and click run
```


## Method Two
```
1.Create and account and login in to https://replit.com/.
2.Create a new Repl
3.Select C Template (Create a C programming template Repl)
4.It will generate a main.c file.Delete this file
5.Create a new file and name it fibonacci.asm
6.Paste the assembly code in the file
7.Do not press run
8.Navigate to the right hand side and select Shell
9. Type the command below

nasm -f elf64 -o outfile.o fibonacci.asm && ld outfile.o -o outfile && ./outfile

```
