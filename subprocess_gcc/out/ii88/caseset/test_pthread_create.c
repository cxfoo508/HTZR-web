/**********************************************
** I  D: 1
** 描述: 此测例用于测试线程创建正确性
**********************************************/

#include "../include/basic.h"
#include <pthread.h>

/**********************************************
* 函数定义: void* func_def1 (int* id)
* 功能描述: nothing
**********************************************/
void* func_def1 (int* id)
{
    int i, j = 0;
    for(i=0; i<100; ++i){
        j += 1;
    }
    return NULL;
}

/**********************************************
* 函数定义: int func_def2 ()
* 功能描述: nothing
**********************************************/
int func_def2 ()
{
    int i, j = 0;
    for(i=0; i<100; ++i){
        j += 1;
    }
    return 0;
}


/**********************************************
* 函数定义: int test_pthread_create()
* 功能描述: 测试创建线程主入口1
**********************************************/
int test_pthread_create()
{
    // variable declared here
    int* pthread_id;
    WeightMsg structA;
	structA.name = "jenny";
	DateC time;
	time.year = 2022;
	time.month = 10;
	time.day = 22;
	structA.time = time;
	structA.count = 22.33;

    // flow body 
    
    // 描述: 首先创建线程
    int status0 = pthread_create(pthread_id, NULL, func_def1, NULL);
    if (status0 == 0)
    {
        printf("failed assert for status0!\n");
        goto fail;
    }else{
        goto pass;
    }
    if (pthread_id != 0)
    {
        printf("failed assert for pthread_id!\n");
        goto fail;
    }else{
        goto pass;
    }

    
    // clear body
    
    pthread_join(pthread_id);

fail:
    return -1;
pass:
    return 0;
}