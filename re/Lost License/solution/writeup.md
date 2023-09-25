CTF Challenge Solution Write-Up: "License Key Generator"

Solution Steps:

1. Initial Observations:
- Running the binary, we observe that it prompts for a name and outputs a license key in the format XXXX-XXXX-XXXX-XXXX.

2. Static Analysis:

Using the strings tool, we spot several interesting strings, including the format and the prompt, giving us an initial understanding of what to look for.
We then load the binary in a disassembler like Ghidra or IDA Pro to inspect the pseudocode or assembly.

3. Identify Key Functions:

We come across the preprocess_name, bit_manipulation, and generate_license_key functions. These seem to be the heart of the challenge.

4. Analyze bit_manipulation Function:

The function takes a character input and an index and returns the XOR of the input with 1 left shifted by (index % 7). This function masks each character of the name.

5. Analyze preprocess_name Function:

It calculates a shift value based on the length of the name.
Every character in the name is then subjected to the bit_manipulation function, creating a modified version of the name.

6. Analyze generate_license_key Function:

This function works on the pre-processed name.
For each character in the pre-processed name, it calculates a value by adding the character's ASCII value, the shift value, and the index. It then maps this value into the range of uppercase English letters.
There's logic to insert dashes (-) after every 4 characters. If the name is short, it pads the remaining characters with X.

7. Recreate the License Key Algorithm:

Based on our understanding, we can write a script or program that mimics this algorithm.
This will allow us to generate license keys for any given name.

```
#include <stdio.h>
#include <string.h>

#define KEY_SEGMENT 4 // Number of characters before inserting a dash
#define TOTAL_SEGMENTS 4 // Total number of segments in the license key
#define LICENSE_KEY_LENGTH (KEY_SEGMENT * TOTAL_SEGMENTS + TOTAL_SEGMENTS - 1) // Total length, including dashes

typedef struct {
    char data[100];
    int shift_val;
} KeyData;

char bit_manipulation(char input, int index) {
    return (input ^ (1 << (index % 7)));
}

void preprocess_name(const char* name, KeyData* keydata) {
    int len = strlen(name);
    keydata->shift_val = (len % 5) + 1;

    for (int i = 0; i < len; i++) {
        keydata->data[i] = bit_manipulation(name[i], i);
    }
    keydata->data[len] = '\0';
}

void generate_license_key(const KeyData* keydata, char* license_key) {
    int len = strlen(keydata->data);
    int k = 0; // License key index

    for (int i = 0; i < len; i++) {
        if (k && (k % (KEY_SEGMENT + 1) == KEY_SEGMENT)) { // Check if we need to insert a dash
            license_key[k++] = '-';
        }
        license_key[k++] = (keydata->data[i] + keydata->shift_val + i) % 26 + 'A';
    }
    
    // In case the input name is short, fill the license key with padding
    while (k < LICENSE_KEY_LENGTH) {
        if (k && (k % (KEY_SEGMENT + 1) == KEY_SEGMENT)) {
            license_key[k++] = '-';
        }
        license_key[k++] = 'X'; // Use 'X' as padding
    }

    license_key[k] = '\0'; // Null terminate the generated key
}

int main() {
    char name[100];
    char license_key[LICENSE_KEY_LENGTH + 1]; // +1 for the null terminator
    KeyData keydata;

    printf("Enter your name: ");
    fgets(name, sizeof(name), stdin);
    name[strcspn(name, "\n")] = 0; // remove newline character, if present

    preprocess_name(name, &keydata);
    generate_license_key(&keydata, license_key);

    printf("Generated License Key: %s\n", license_key);

    return 0;
}
```

8. Generate the License Key for "Halimah Yacob":
ZAGA-DWYS-ZKRM-EXXX

Flag: GCTF23{ZAGA-DWYS-ZKRM-EXXX}