// Entry: "The Day in One Picture" — front-page collage of the five
// 13 November 2026 stories (Nvidia, Hormuz, Dublin talks, tariffs,
// Outlook outage) drawn in code with Pillow; see draw.py for the source.
// The image is entry.png beside this file; the program copies it to the
// output directory so the grader sees exactly those bytes.
// The gate takes a whole PNG or JPEG of at most 1 MiB and 1024 by 1024 pixels.
//
// Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts

import { copyFileSync } from 'node:fs';
import { join } from 'node:path';

copyFileSync(new URL('./entry.png', import.meta.url), join(process.env.MAKEFUN_OUTPUT_DIR ?? '/output', 'entry.png'));
