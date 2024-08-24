#include
#include
#include

char buf[1024];

int fail()
{
	printf("Usage: gcj <problem> (small [<attempt>] | large [<type>])\n");
	printf("Examples:\n");
	printf("    gcj A small\n");
	printf("    gcj A small 1\n");
	printf("    gcj B large\n");
	printf("    gcj C large 1\n");
	return 0;
}

int main(int argc, char* argv[])
{
	if (argc >= 3 && !strcmp(argv[2], "small"))
	{
		int attempt = 0;
		if (argc == 4)
			sscanf(argv[3], "%d", &attempt);
		else if (argc > 4)
			return fail();
		sprintf(buf, "./%s < %s-small-attempt%d.in | tee %s-small-attempt%d.out",
                     argv[1], argv[1], attempt, argv[1], attempt);
		system(buf);
	}
	else if (argc >= 3 && !strcmp(argv[2], "large"))
	{
		if (argc == 3)
			sprintf(buf, "./%s < %s-large.in | tee %s-large.out",
                         argv[1], argv[1], argv[1]);
		else if (argc == 4)
			sprintf(buf, "./%s < %s-large-%s.in | tee %s-large-%s.out",
                         argv[1], argv[1], argv[3], argv[1], argv[3]);
		else
			return fail();
		system(buf);
	}
	else
		return fail();
}
