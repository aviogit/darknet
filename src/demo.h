#ifndef DEMO_H
#define DEMO_H

#include "image.h"
#ifdef __cplusplus
extern "C" {
#endif

struct save_info_;

void demo(char *cfgfile, char *weightfile, float thresh, float hier_thresh, int cam_index, const char *filename, char **names, int classes,
    int frame_skip, char *prefix, char *out_filename, int mjpeg_port, int json_port, int dont_show, int ext_output, int letter_box_in, struct save_info_ *save_info);
#ifdef __cplusplus
}
#endif

#endif
