#include <sys/socket.h>
#include <sys/ioctl.h>
#include <linux/if.h>
#include <netdb.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

static const char *my_mac = "DEADBEEFDEAD";

char *get_mac() {
	struct ifreq s;
	int fd = socket(PF_INET, SOCK_DGRAM, IPPROTO_IP);
	strcpy(s.ifr_name, "eth0");
	if (0 == ioctl(fd, SIOCGIFHWADDR, &s)) {
		char *mac = malloc(23);
		sprintf(mac, "%2X%2X%2X%2X%2X%2X", 
				(unsigned char)s.ifr_addr.sa_data[0],
				(unsigned char)s.ifr_addr.sa_data[1],
				(unsigned char)s.ifr_addr.sa_data[2],
				(unsigned char)s.ifr_addr.sa_data[3],
				(unsigned char)s.ifr_addr.sa_data[4],
				(unsigned char)s.ifr_addr.sa_data[5]);
		return mac;
	}
	return NULL;
}

int main(void) {
	if (strcmp(my_mac, get_mac()) == 0) {
		printf("Your programm installed successfully.\n");
		printf("Hello, world!\n");
	} else {
		printf("Your mac is %s\n", get_mac());
		printf("Needed mac is %s\n", my_mac);
		printf("May be you should run installer first\n");
	}
	return 0;
}