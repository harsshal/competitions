#include<stdio.h>
#include<string.h>
#include<stdlib.h>

char buf[1024];

int fail()
{
	printf("Usage: codejam <problem> (small [<attempt>] | large [<type>])\n");
	printf("Examples:\n");
	printf("    codejam A small 1\n");
	printf("    codejam A small 2\n");
	printf("    codejam B large 1\n");
	printf("    codejam C large 2\n");
	return 0;
}

int main(int argc, char* argv[])
{
	if (argc == 4 && (!strcmp(argv[2], "small") or !strcmp(argv[2], "large")) )
	{
		int attempt;
		sscanf(argv[3], "%d", &attempt);
		sprintf(buf, "../%s/bin/Debug/%s < ../%s/%s-%s-attempt%d.in | tee ../%s/%s-%s-attempt%d.out",
                      argv[1], argv[1], argv[1], argv[1], argv[2], attempt, argv[1], argv[1], argv[2], attempt);
		system(buf);
	}
	else
		return fail();
}
