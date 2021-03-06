#include "stdint.h"
#include "init.h"
#include "tm4c123gh6pm.h"


void PortA_Init() {  //command port (PA5 for RS ,PA6 for R/W, PA7 for E)
	
	SYSCTL_RCGCGPIO_R |= 0x01;     // 1) A clock
	while ((SYSCTL_PRGPIO_R & 0x01) == 0) {};         
	GPIO_PORTA_CR_R = 0xE0;           // allow changes to PA7-5       
	GPIO_PORTA_AMSEL_R = 0x00;        // 3) disable analog function
	GPIO_PORTA_PCTL_R = 0x00000000;   // 4) GPIO clear bit PCTL  
	GPIO_PORTA_DIR_R = 0xE0;          // 5) PB7-PA5 output   
	GPIO_PORTA_AFSEL_R = 0x00;        // 6) no alternate function
	GPIO_PORTA_PUR_R = 0x00;          // disable pullup resistors         
	GPIO_PORTA_DEN_R = 0xE0;          // 7) enable digital pins PA7-PA0        
}

void PortB_Init(){    // Data port 
  
  SYSCTL_RCGCGPIO_R |= 0x02;     // 1) B clock
  while ((SYSCTL_PRGPIO_R & 0x02) == 0) {};     
  GPIO_PORTB_LOCK_R = 0x4C4F434B;
  GPIO_PORTB_CR_R = 0xFF;           // allow changes to PB7-0       
  GPIO_PORTB_AMSEL_R = 0x00;        // 3) disable analog function
  GPIO_PORTB_PCTL_R = 0x00000000;   // 4) GPIO clear bit PCTL  
  GPIO_PORTB_DIR_R = 0xFF;          // 5) PB7-PB0 output   
  GPIO_PORTB_AFSEL_R = 0x00;        // 6) no alternate function
  GPIO_PORTB_PUR_R = 0x00;          // disable pullup resistors       
  GPIO_PORTB_DEN_R = 0xFF;          // 7) enable digital pins PA7-PA0       
}

void PortF_Init(void)  // led & switches port
{
	
	SYSCTL_RCGCGPIO_R |= 0x20;
	while ((SYSCTL_PRGPIO_R & 0x20) == 0) {};
	GPIO_PORTF_AFSEL_R = 0;
	GPIO_PORTF_PCTL_R = 0;
	GPIO_PORTF_AMSEL_R = 0;
	GPIO_PORTF_PUR_R = 0x11;
	GPIO_PORTF_DIR_R = 0x0E;
	GPIO_PORTF_DEN_R = 0x1F;
	GPIO_PORTF_LOCK_R = 0x4C4F434B;
	GPIO_PORTF_CR_R = 0x1F;
}

void PortD_Init(void)  // GPS port
{

	SYSCTL_RCGCGPIO_R |= 0x08;
	while ((SYSCTL_PRGPIO_R & 0x08) == 0) {};
	GPIO_PORTD_AFSEL_R = 0;
	GPIO_PORTD_PCTL_R = 0;
	GPIO_PORTD_AMSEL_R = 0;	
	GPIO_PORTD_PUR_R = 0x00;	// need to add
	GPIO_PORTD_DIR_R = 0x00;  // need to add
	GPIO_PORTD_DEN_R = 0xFF;
	GPIO_PORTD_LOCK_R = 0x4C4F434B;
	GPIO_PORTD_CR_R = 0xFF;
}


void distance(uint_t32 dis)
{
	if (dis >= 100) {

		GPIO_PORTF_DATA_R |= (1 << 1);

	}
}




