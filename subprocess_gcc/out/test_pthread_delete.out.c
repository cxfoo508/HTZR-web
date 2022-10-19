/**********************************************
** I  D: 2
** 描述: 此测例用于测试线程删除正确性
**********************************************/

#include "../include/basic.h"

/**********************************************
* 函数定义: void* func_def1 (int* id)
* 功能描述: 线程函数主体
**********************************************/
void* func_def1 (int* id)
{
    int i, j = 0;
    for(i=0; i<100; ++i){
        j += 1;
    }
    return;
}


/**********************************************
* 函数定义: int test_pthread_delete()
* 功能描述: 测试删除线程主入口2
**********************************************/
int test_pthread_delete()
{
    // variable declared here
    int* pthread_id;
    char* some_str;

    // flow body 
    
    // 描述: None
    status0 = func1(0, pthread_id);
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
    status0 = func2(0, pthread_id);
    if (status0 == 0)
    {
        printf("failed assert for status0!\n");
        goto fail;
    }else{
        goto pass;
    }

    

fail:
    return -1;
pass:
    return 0;
}