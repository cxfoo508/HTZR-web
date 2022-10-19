/**********************************************
** I D: {{ id }}
** 描 述: 所有测试函数主入口
**********************************************/

#include "include/basic.h"

{%- if caseLen > 0 -%}
{% for tcase in tCases %}
#include "caseset/{{ tcase }}.c"
{%- endfor -%}
{%- else -%}
{% endif %}

static int case_cnt = 0;
static int case_pass = 0;
static int case_fail = 0;

/**********************************************
* 函数定义: int main(int argc, char **argv)
* 功能描述: 所有测试主入口， 收集并打印测试统计结果
**********************************************/
int main(int argc, char **argv)
{
    {%- if caseLen > 0 -%}
    {% for tcase in tCases %}
    {{ tcase }}();
    {%- endfor -%}
    {%- else -%}
    {% endif %}

    printf("测试结果为: \n\t总测例数量: %4d\n\t通过测例数: %4d\n\t失败测例数: %4d\n", case_cnt, case_pass, case_fail);
    return 0;
}
