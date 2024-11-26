#include<stdio.h>

int main(){
	int t,r,e,c;
	scanf("%d",&t);
	for(int i = 0 ; i < t ; i++){
		scanf("%d %d %d",&r,&e,&c);
		if(r==(e-c))
			printf("does not matter\n");
		else if(r > (e-c))
			printf("do not advertise\n");
		else 
			printf("advertise\n");
	}
}