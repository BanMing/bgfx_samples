#include "apps/helloworld/helloworld.h"
#include <entry/entry.h>

int _main_(int _argc, char** _argv)
{
	HelloWorld* app = new HelloWorld("Hello World", "Hello World Demo.");
	return entry::runApp(app, _argc, _argv);
}
