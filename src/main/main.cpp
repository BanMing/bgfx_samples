// #include "apps/helloworld/helloworld.h"
#include "apps/debug_draw_sample/debug_draw_sample.h"
#include <entry/entry.h>

int _main_(int _argc, char **_argv)
{
  // HelloWorld *app = new HelloWorld("Hello World", "Hello World Demo.");
  DebugDrawSample *app = new DebugDrawSample("Debug Draw", "Debug Draw Demo.");
  return entry::runApp(app, _argc, _argv);
}
