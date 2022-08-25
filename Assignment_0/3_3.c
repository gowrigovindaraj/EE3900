#include <stdio.h>
#include <string.h>

int main(void) {
  float x[] = {1.0,2.0,3.0,4.0,2.0,1.0};
  int k = 20;
  float y[20] = {0};
  y[0] = x[0];
  y[1] = -0.5*y[0]+x[1];

  for (int n = 2;n<k-1;n++){
    if(n<6){
      y[n] = -0.5*y[n-1]+x[n]+x[n-2];
    }
    else if (n > 5 && n < 8){
      y[n] = -0.5*y[n-1]+x[n-2];
    }
    else{
      y[n] = -0.5*y[n-1];
    }
  }
//   for (int i = 0;i<6;i++){
//     printf("%f\n",x[i]);
//   }
  
  FILE *f = fopen("x.txt", "w");
  for (int i = 0; i < 6; i++)
        fprintf(f, "%f\n",x[i]);
  fclose(f);

  FILE *f1 = fopen("y.txt", "w");
  for (int i = 0; i < k; i++)
        fprintf(f1, "%f\n",y[i]);
  fclose(f1);

  return 0;
}
