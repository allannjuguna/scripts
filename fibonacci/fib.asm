global _start

section .data
    n: dq 25            ;the number of fibonacci numbers we want

section .text
_start:
    push rsp            ;save the address of the top of the stack
    mov rax, qword[n]   ;we are going to allocate N quadwords
    mov rcx, 0x8        ;intel x64 considers a word to be 16 bits (for historical reasons), so a quadword is 8 bytes
    xor rdx,rdx         ;clean rdx as its value might affect the multiplication
    mul rcx             ;multiply rax (n) by 8 to obtain the number of bytes we need to allocate 
    sub rsp, rax        ;allocates that many bytes on the stack
    mov rax, 0x0        ;first fibonacci number
    mov rbx, 0x1        ;second fibonacci number

    xor rcx, rcx        ;set rcx to 0 as it will be used to count how many numbers we got already
    xor rsi, rsi        ;set rsi to 0 as well as it will be used as an index to our array

    ;the following loop is going to store N fibonacci numbers at an array and also print each number as it does it

    .fibonacci:

        ;the sum of 2 numbers define the next one
        mov rdx, rbx    ;saves rbx at rdx
        add rbx, rax    ;sets rax = rbx + rax
        mov rax, rdx    ;rax = rdx
        ;rax is the next fibonacci number, copy it to rsp+rsi
        mov qword[rsp + rsi], rax

        push rax        ;saves rax
        push rcx        ;saves rcx
        push rsi        ;saves rsi
        call print_fib   ;prints the current value of rax
        pop rsi         ;restores rsi
        pop rcx         ;restores rcx
        pop rax         ;restores rax

        add rsi, 0x8    ;add 8 bytes to rsi, moving to the next position
        inc rcx         ;increments rcx
        cmp rcx, qword[n] ;compares rcx with the value of N
        jl .fibonacci   ;repeats if rcx < N

    
    pop rcx         ;recover the previous stack address to rcx
    mov rsp, rcx    ;restore it to rsp (and basically desallocates the array)
    jmp exit        ;gracefully exits the program

print_fib:
    ;this function will print whatever number is stored at rax to the screen
    push rbx        ;saves rbx
    mov rbx, rsp    ;copy the current stack address to rbx
    ;we will use rsp (the stack) as a buffer to store the representation of the number and then print it to the screen
    ;Note that the stack stores each character in reverse order
    
    mov rsi, 0xa       ;rsi will store the value 10 to use on division

    ;first, we will store "\r\n" to print a new line after each number
    ;;;;;;UNCOMMENT THE NEXT LINE IN CASE OF ERRORS
    dec rsp            ;move to the next position on our buffer
    mov byte[rsp], 0xd ;stores a '\r' char
    dec rsp            ;move to the next position on our buffer
    mov byte[rsp], 0xa ;stores a '\n' char

    mov rcx, 0x2       ;rcx stores the number of bytes on our buffer, we start with 2 (\r\n)

    .loop:
        xor rdx, rdx        ;clean rdx or it can mess with the division
        div rsi             ;divides rax by rsi (10) and the remainder is stored at rdx
        add rdx, 0x30       ;add 48 to rdx (char '0') to get the last digit of the number as a character
        dec rsp             ;move to the next position on our buffer
        mov byte[rsp], dl   ;set the current position of the buffer to the resulting char
        inc rcx             ;increments rcx
        test rax, rax       ;quick way to test if a number is 0
        jnz .loop           ;repeat if rax is not zero

    ;the above loop converts an integer number to its string representation by getting the remainder of division by 10
    ;(the last digit of the number at rax) at each iteration, untill rax is 0

    mov rax, 1      ;set rax to 1 (write system call)
    mov rdi, 1      ;set rdi to 1 (stdout)
    mov rsi, rsp    ;set rsi to the address of rsp (the start of our buffer)
    mov rdx, rcx    ;set rdx to rcx (the number of bytes of our buffer)
    syscall         ;executes the system call to print it to stdout

    mov rsp, rbx    ;restores the value of rsp from rbx
    pop rbx         ;restores the original value of rbx
    ret             ;returns to the caller

exit:
    mov rax, 60     ;set rax to 60 (exit system call)
    mov rdi, 0      ;set rdi to 0 (the return value)
    syscall         ;executes the system call
