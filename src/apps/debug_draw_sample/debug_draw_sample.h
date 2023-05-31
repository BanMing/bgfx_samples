#ifndef _DEBUG_DRAW_SAMPLE_H_
#define _DEBUG_DRAW_SAMPLE_H_

#include "apps/application.h"

class DebugDrawSample : public Application
{
public:
    DebugDrawSample(const char *_name, const char *_description)
        : Application(_name, _description)
    {
    }

protected:
    void onInit() {}
    void onShutdown() {}
    void onUpdate(float _deltaTime) {}
    void onRender(float _inAspectRatio) {}
    void onGui() {}
};

#endif //_DEBUG_DRAW_SAMPLE_H_
