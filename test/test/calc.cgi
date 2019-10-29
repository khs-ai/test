
#include "soapcalcProxy.h" 
#include "calc.nsmap" 
int main() 
{ 
   calcProxy service; 
   double result; 
   if (service.add(1.0, 2.0, result) == SOAP_OK) 
      std::cout << "The sum of 1.0 and 2.0 is " << result << std::endl; 
   else
      service.soap_stream_fault(std::cerr); 
   service.destroy(); // delete data and release memory 


    printf("Content-type: text/html\r\n\r\n<html><h1>Magic Square of Rank %d</h1><pre>\n", 1);
 // if (soap_call_ns1__magic(&soap, magicserver, NULL, r, A))
  //{ soap_print_fault(&soap, stderr);
   // soap_print_fault_location(&soap, stderr);
 // }
  //else
  /*{ for (int i = 0; i < (*A).__size; i++)
    { for (int j = 0; j < (*A)[i].__size; j++)
        printf("%4d", (*A)[i][j]);
      printf("\n");
    }
  }*/
  printf("</pre></html>\n");

   getchar();
}
