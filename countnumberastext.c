#include <stdio.h>
#include <stdlib.h>

char* ones[] = {"zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"};
char* teens[] = {"ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};
char* tens[] = {"zero", "ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};

int bignumbers[] = {33, 30, 27, 24, 21, 18, 15, 12, 9, 6, 3, 0};
char* bignames[] = {"decillion", "nonillion", "octillion", "septillion", "sextillion", "quintillion", "quadrillion", "trillion", "billion", "million", "thousand", "hundred"};

char* numbertotext(int i) {
  char* returnstring = malloc(1000);
  returnstring[0] = '\0';
  
  if(i < 0) {
    strcat(returnstring, "negative ");
    i = -i;
  }
  
  if(i == 0) {
    strcat(returnstring, "zero\0");
    return returnstring;  
  }
  
  for(int c = 0; c < 12; c++) {
    int multiplier = pow(10, bignumbers[c]);
    int ht = (i / multiplier) % 1000;

    int tensdata = ht % 100;
    int hundredsdata = ht / 100;

    if(hundredsdata > 0) {
      strcat(returnstring, ones[hundredsdata]); 
      strcat(returnstring, " hundred ");
    }
    
    if(tensdata > 0 && tensdata < 10) {
      strcat(returnstring, ones[tensdata]);
      strcat(returnstring, " ");
    }
    
    if(tensdata >= 10 && tensdata < 20) {
      int temp = tensdata % 10;
      strcat(returnstring, teens[temp]);
      strcat(returnstring, " ");
    }
    
    if(tensdata >= 20 && tensdata < 100) {
      int temp = (tensdata / 10) % 10;
      int temp2 = tensdata % 10;
      if(temp2 > 0) {
        strcat(returnstring, tens[temp]);
        strcat(returnstring, " ");
        strcat(returnstring, ones[temp2]);
        strcat(returnstring, " ");  
      } else {
        strcat(returnstring, tens[temp]);
        strcat(returnstring, " ");
      }
    }

    if(ht > 0 && c != 11) {
      strcat(returnstring, bignames[c]);
      strcat(returnstring, " ");
    }
  }
  strcat(returnstring, "\0");
  //printf("%i\n", strlen(returnstring));
  return returnstring;
}

int main() {
  char *data;
  for(int i=-50; i<200000001; i++) {
    data=numbertotext(i);
    printf("%s\n", numbertotext(i));
    free(data);
  }
  return 0;
}
