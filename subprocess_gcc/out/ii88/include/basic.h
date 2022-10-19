#pragma once

#include <stdio.h>
#include <string.h>
#include <assert.h> 

typedef struct{
    unsigned long year;
    int month;
    int day;
} DateC;

typedef struct{
    char* name;
    struct DateC time;
    float count;
} WeightMsg;
