#include <stdio.h>
#include <string.h>

int main() {

	char input[10] = {0};
	char password[10] = "abcdefghi";

	printf("Enter input: \n");
	fflush(stdout);

	gets(input);

	printf("\nLength: %zu\n", strlen(input));

	printf("Password: %s\n", password);

	if (strcmp(password, "supersecret") == 0) {
		printf("Well done! you get a flag: %s\n", flag);
	}
	fflush(stdout);

	return 0;
}
