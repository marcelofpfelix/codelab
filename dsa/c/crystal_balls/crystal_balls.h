// This is called an include guard, which ensures that the header is only
// included once. You could alternatively use '#pragma once'. See
// https://en.wikipedia.org/wiki/Include_guard.
#ifndef CRYSTAL_BALLS_H
#define CRYSTAL_BALLS_H

// Declare the 'hello()' function, which takes no arguments and returns a
// 'const char *', i.e. a pointer to a character (in this case the first
// character in a string). The function itself is defined in the hello_world.c
// source file. Ths function is called by the test case(s) in the test source
// file test/test_hello_world.c.
int crystalBalls(int*, int);

#endif
