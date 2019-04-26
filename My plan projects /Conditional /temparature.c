# include<stdio.h>
int main()
{
    int choice;
    float  temp, convertedTemp;
    printf("Temperature manu \n");
    printf("1. To Fahrenheit to Celsius \n");
    printf("2. Celsius to Fahrenheit \n");
    printf ("Enter your choice :");
    scanf("%d",&choice);
    switch(choice)
    {
        case 1:
             {
                printf("Enter Fahrenheit Temperature");
                scanf("%f",&temp);
                convertedTemp =(temp-32)/1.8;
                printf("The Temperature of Celsius is %f",convertedTemp);
                break;
            }
         case 2:
            {
                printf("Enter Celsius Temperature:");
                scanf("%f",&temp);
                convertedTemp =(temp*1.8)+32;
                printf("The Temperature of Fahrenheit  is %f",convertedTemp);

            }

         default:
            printf("Not a correct Option");
    }


}
