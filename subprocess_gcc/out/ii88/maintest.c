/**********************************************
** I D: 
** 描 述: 所有测试函数主入口
**********************************************/

#include "include/basic.h"
#include "caseset/test_pthread_create.c"
#include "caseset/test_pthread_delete.c"

static int case_cnt = 0;
static int case_pass = 0;
static int case_fail = 0;

/**********************************************
* 函数定义: int main(int argc, char **argv)
* 功能描述: 所有测试主入口， 收集并打印测试统计结果
**********************************************/
int main(int argc, char **argv)
{
    test_pthread_create();
    test_pthread_delete();

    printf("测试结果为: \n\t总测例数量: %4d\n\t通过测例数: %4d\n\t失败测例数: %4d\n", case_cnt, case_pass, case_fail);
    return 0;
}