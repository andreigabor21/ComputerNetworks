#include "winsock2.h"
#include <WinSock2.h>
#include <iostream>
#include <conio.h>

using namespace std;
#pragma comment(lib,"Ws2_32.lib")
#define MYPORT 9009 //the port users will be connecting to

int main() {
    // initialize the Windows Sockets LIbrary only when compiled on Windows
#ifdef WIN32
    WSADATA wsaData;
    if (WSAStartup(MAKEWORD(2, 2), &wsaData) < 0) {
        printf("Error initializing the Windows Sockets LIbrary");
        return -1;
    }
#endif

    SOCKET sock;
    sock = socket(AF_INET, SOCK_DGRAM, 0);

    char broadcast = '1';
    /* This option is needed on the socket in order to be able to receive broadcast messages
     If not set, the receiver will not receive broadcast messaged in the LAN */
    if(setsockopt(sock, SOL_SOCKET, SO_BROADCAST, &broadcast, sizeof(broadcast)) < 0) {
        cout<<"Error in setting Broadcast option";
        closesocket(sock);
        return 0;
    }

    struct sockaddr_in recv_addr{}, sender_addr{};
    int len = sizeof(struct sockaddr_in);

    char recvbuff[50];
    int recvbufflen = 50;
    char sendMSG[] = "SALUUT DIN RECEIVER";

    recv_addr.sin_family = AF_INET;
    recv_addr.sin_port = htons(MYPORT);
    recv_addr.sin_addr.s_addr = INADDR_ANY;

    if(bind(sock, (struct sockaddr*) &recv_addr, sizeof(recv_addr)) < 0) {
        cout<<"Error in BINDING";
        closesocket(sock);
        return 0;
    }

    recvfrom(sock, recvbuff, recvbufflen, 0, (struct sockaddr*) &sender_addr, &len);
    cout<<"\n\n\tReceived Message is: "<<recvbuff;
    cout<<"\n\n\tPress Any to send message";
    _getch();

    if(sendto(sock, sendMSG, strlen(sendMSG) + 1, 0, (struct sockaddr*) &sender_addr, sizeof(sender_addr)) < 0) {
        cout<<"Error in Sending.";
        cout<<"\n\n\t\t Press any key to continue...";
        closesocket(sock);
        return 0;
    }
    else
        cout<<"\n\n\n\tReader sends the broadcast message successfully";

    cout<<"\n\n\t Press any key to CONT...";
    _getch();

    closesocket(sock);
    WSACleanup();
}
