/**********************************************
** I  D: 1
** 描述: 测试1
**********************************************/

#include "../include/basic.h"
#include <2.h>
#include <3.h>

/**********************************************
* 函数定义: void* func1 (int* id)
* 功能描述: 这是一个线程函数
**********************************************/
void* func1 (int* id)
{
    return NULL;
}

/**********************************************
* 函数定义: void* func2 (int* id)
* 功能描述: 这是一个线程函数
**********************************************/
void* func2 (int* id)
{
    return NULL;
}


/**********************************************
* 函数定义: int test_pthread_create()
* 功能描述: 测试1111
**********************************************/
int test_pthread_create()
{
    // variable declared here
    int* pthread_id;
    const char* some_str = "abc123";

    // flow body 
    
    // 描述: 创建线程
    int status0 = pthread_create(pthread_id, 0);
    if (status0 == 0)
    {
        printf("failed assert for status0!\n");
        goto fail;
    }else{
        goto pass;
    }
    if (pthread_id != -1)
    {
        printf("failed assert for pthread_id!\n");
        goto fail;
    }else{
        goto pass;
    }
    
    // 描述: 等待线程
    status0 = pthread_join(pthread_id, 0);
    if (status0 == 0)
    {
        printf("failed assert for status0!\n");
        goto fail;
    }else{
        goto pass;
    }
    if (pthread_id != -1)
    {
        printf("failed assert for pthread_id!\n");
        goto fail;
    }else{
        goto pass;
    }

    
    // clear body
    // 描述: 等待线程 
    pthread_join(pthread_id);

fail:
    return -1;
pass:
    return 0;
}