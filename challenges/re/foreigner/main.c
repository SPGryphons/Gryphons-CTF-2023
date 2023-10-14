#include <stdio.h>
#include <stdlib.h>

static inline void catcherror(char x) {
	fprintf(stderr, "Error parsing: %02x\n", x);
	exit(1);
}
#define REGSIZEOF (sizeof(registers)/sizeof(char))

int main() {
	FILE *fp;
	size_t len = 0, IP = 0;
	unsigned char *buf = NULL;
	unsigned char registers[4];
	registers[0] = 0;
	registers[1] = 0;
	registers[2] = 0;
	registers[3] = 0;
	fp = fopen("ALIENWARE", "r");
	if(fp == NULL) {
		fprintf(stderr, "Error opening file: ALIENWARE");
		exit(-1);
	}
	fseek(fp, 0, SEEK_END);
	len = ftell(fp);
	fseek(fp, 0, SEEK_SET);
	buf = malloc(sizeof(char)*len +1);
	if(buf == NULL) {
		fprintf(stderr, "Error allocating memory");
	}
	fread(buf, 1, len, fp);
	while(IP < len) {
		switch(buf[IP]) {
			case 0x2:
				if(buf[IP+1] >= (REGSIZEOF) || (IP+2) > len) {
					catcherror(buf[IP]);
				}
				registers[buf[IP+1]] = buf[IP+2];
				IP += 3;
				break;
			case 0x3:
				if(buf[IP+1] >= (REGSIZEOF) || buf[IP+2] >= REGSIZEOF || (IP+2) > len) {
					catcherror(buf[IP]);
				}
				registers[buf[IP+1]] += registers[buf[IP+2]];
				IP += 3;
				break;
			case 0x5:
				if(buf[IP+1] >= (REGSIZEOF) || buf[IP+2] >= REGSIZEOF || (IP+2) > len) {
					catcherror(buf[IP]);
				}
				registers[buf[IP+1]] -= registers[buf[IP+2]];
				IP += 3;
				break;
			case 0x7:
				if(buf[IP+1] >= REGSIZEOF || buf[IP+2] >= REGSIZEOF || (IP+2) > len) {
					catcherror(buf[IP]);
				}
				registers[buf[IP+1]] ^= registers[buf[IP+2]];
				IP += 3;
				break;
			case 0x11:
				if(buf[IP+1] >= REGSIZEOF || (IP+1) > len) {
					catcherror(buf[IP]);
				}
				registers[buf[IP+1]] = ~registers[buf[IP+1]];
				IP += 2;
				break;
			case 0x13:
				if(buf[IP+1] >= REGSIZEOF || buf[IP+2] >= REGSIZEOF || (IP+2) > len) {
					catcherror(buf[IP]);
				}
				registers[buf[IP+1]] |= registers[buf[IP+2]];
				IP += 3;
				break;
			case 0x17:
				if(buf[IP+1] >= REGSIZEOF || buf[IP+2] >= REGSIZEOF || (IP+2) > len) {
					catcherror(buf[IP]);
				}
				registers[buf[IP+1]] &= registers[buf[IP+2]];
				IP += 3;
				break;
			case 0x19:
				if(buf[IP+1] >= REGSIZEOF || buf[IP+2] >= REGSIZEOF || (IP+4) > len) {
					catcherror(buf[IP]);
				}
				if(registers[buf[IP+1]] > registers[buf[IP+2]]) {
					IP = (buf[IP+3]<<8) | (buf[IP+4]);
					continue;
				}
				IP += 5;
				break;
			case 0x23:
				if(buf[IP+1] >= REGSIZEOF || (IP+1) > len) {
					catcherror(buf[IP]);
				}
				registers[buf[IP+1]] = getchar();
				IP += 2;
				break;
			case 0x29:
				if(buf[IP+1] >= REGSIZEOF || (IP+1) > len) {
					catcherror(buf[IP]);
				}
				putchar(registers[buf[IP+1]]);
				IP += 2;
				break;
			default:
				printf("Unimplemented: 0x%02x\n", buf[IP]);
				IP++;
				break;
		}
	}
	fclose(fp);
	free(buf);
	return 0;
}
