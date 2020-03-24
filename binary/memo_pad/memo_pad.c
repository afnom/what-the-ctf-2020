#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


typedef uint64_t u64;

void exit_pad();
void new_pad();
void read_pad();
void clear_pad();
void write_memo();

size_t size = 0;
void* heap_buffer = NULL;
void (*func_ptr[5])() = {exit_pad, new_pad, clear_pad, read_pad, write_memo};

void print_menu(){
    printf("1. New Note\n2. Delete Note\n3. Write text in note\n4. Print note from memory\n0. Exit\n");
    fflush(stdout);
}

int _()
{
  return system("cat flag");
}

u64 read_long()
{
  char s[40];
  memset(s, 0, 0x20uLL);
  s[(signed int)((u64)read(0, s, 0x20uLL) - 1)] = 0;
  return strtoul(s, 0LL, 0);
}

void exit_pad(){
    printf("Thanks. Bye!\n");
    exit(1);
}

void new_pad(){
    printf("What size should the note be? \n");
    fflush(stdout);

    size_t memo_size = (uint64_t)read_long();
    printf("Creating a %lu chars memo \n", memo_size);
    fflush(stdout);
    size = memo_size;
    int *addr = (int *)malloc(memo_size);

    if(addr == NULL)
        heap_buffer = NULL;
    else
        heap_buffer = addr;
}

void read_pad(){
    printf("Input your text: \n");
    fflush(stdout);
    if ( heap_buffer == NULL) {
        printf("Not allocated.\n");
        fflush(stdout);
    }
    else
        read(0, heap_buffer, size);
}

void clear_pad(){
  printf("Your Memo Pad is now empty. You may create a new note.\n");
    fflush(stdout);
    if(heap_buffer == NULL ) {
      printf("Not allocated.\n");
      fflush(stdout);
    }
    else{
        free(heap_buffer);
        heap_buffer = NULL;
    }
}

void write_memo(){
    if(heap_buffer == NULL ) {
        printf("Not allocated.\n");
      fflush(stdout);
    }
    else {
      printf("Latest memo from memory: \n");
      fflush(stdout);
      write(1, heap_buffer, size);
      fflush(stdout);
    }
}

int main(int argc, const char **argv, const char **envp)
{
  puts("Welcome to neko3's super duper memo pad! \nIt can only hold ONE memo currently!\nWork in progress...\n");
    fflush(stdout);
  signed int opt;

  while ( 1 )
  {
    print_menu();
    printf("> ");
    fflush(stdout);
    opt = read_long();
    if ( opt <= 4 )
      (*func_ptr[opt])();
    else
      puts("Not and option. Try again.\n");
    fflush(stdout);
  }
}
