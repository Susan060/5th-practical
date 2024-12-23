#include<stdio.h> 
int main()
{
char message[100], ch;
int i, key;
printf("Enter a message to encrypt: ");
gets(message);
printf("Enter key: ");
scanf("%d", &key); //kanya
for(i = 0; message[i] != '\0'; ++i){
ch = message[i];

if(ch >=  'a' && ch <= 'z'){
printf("Numeric ascii Accept");
ch = ch + key;
printf("Character Value: %C", ch);
if(ch > 'z'){
ch = ch - 'z' + 'a' - 1;
}
message[i] = ch;
}
else if(ch >= 100 && ch <= 126){
printf("Numeric ascii Accept");
ch = ch + key;
printf("Character Value: %C", ch);
if(ch > 'Z'){
ch = ch - 'Z' + 'A' - 1;
}
message[i] = ch;
}
}
printf("Encrypted message: %s", message);
return 0;
}
