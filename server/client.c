#ifdef _WIN32
#include <Winsock2.h>
#endif
#include <sys/socket.h>
#include <unistd.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <string.h>
#include <stdbool.h>

#define PORT 50000


void send_info(int sock, void* msg, uint32_t msgsize)
{
	if(write(sock, msg, msgsize) < 0){
		printf("Probleme lors de l'envoi");
		close(sock);
		exit(1);
	}
	printf("Message envoyé, (%d bits envoyés).\n", msgsize);
	
}



int main(void){

    
	char id, server_reply[2000];

    int socketClient = socket(AF_INET, SOCK_STREAM, 0);
    struct sockaddr_in addrClient;
    addrClient.sin_addr.s_addr = inet_addr("192.168.1.30");
    addrClient.sin_family = AF_INET;
    addrClient.sin_port = htons(PORT);
    connect(socketClient, (const struct sockaddr *)&addrClient, sizeof(addrClient));
    printf("connection réussi\n");

	char reserv[] = "Y,01";
    send_info(socketClient, reserv, sizeof(reserv));


    close(socketClient);

    return 0;
}