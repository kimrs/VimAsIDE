#include <stdio.h>
#include <iostream>
#include <string>

extern "C" { 
	#include "hello.h"
}

int main()
{
	std::cout << "Testing open slp" << std::endl;
	hello();
//        SLPError err;
//        SLPError callbackerr;
//       SLPHandle hslp;
//        
//      err = SLPOpen("en",SLP_FALSE,&hslp);
// 
//        if(err != SLP_OK)
//        {
//            printf("Error opening slp handle %i\n",err);
//            return err;
//        }
	
	return 0;
}
