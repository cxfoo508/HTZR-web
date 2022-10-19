/**********************************************
** I  D: {{ id }}
** 描述: {{ description }}
**********************************************/

#include "../include/basic.h"
{%- if headersLen > 0 -%}
{% for header in headers %}
#include <{{ header }}>
{%- endfor -%}
{%- else -%}
{%- endif -%}

{% if defFuncLen > 0 %}
{% for func in defFuncs %}
/**********************************************
* 函数定义: {{ func.getDeclare() }}
* 功能描述: {{ func.description }}
**********************************************/
{{ func.getDeclare() }}
{
    int i, j = 0;
    for(i=0; i<100; ++i){
        j += 1;
    }
    return{{ func.getRtn() }};
}
{% endfor %}
{%- else -%}
{% endif %}

/**********************************************
* 函数定义: int {{ name }}()
* 功能描述: {{ flowInfo }}
**********************************************/
int {{ name }}()
{
    // variable declared here
    {%- if defVarLen > 0 -%}
    {% for var in defVars%}
    {{ var.getDeclare() }}
    {%- endfor -%}
    {%- else -%}
    {% endif %}

    {% if defFlowLen > 0 %}// flow body {% for flow in defFlows %}
    {% if flow.description != "" %}
    // 描述: {{ flow.description }}
    {% endif %}
    {%- if flow.result != None -%}
    {{ flow.result.getDeclare() }}
    {%- endif -%}
    {{ flow.getCall() }};
    {%- if flow.getCheckLen() > 0 -%}
    {% for check in flow.checks %}
    {{ check.getDeclare() }}
    {
        printf("failed assert for {{ check.name }}!\n");
        goto fail;
    }else{
        goto pass;
    }
    {%- endfor -%}
    {%- endif -%}
    {%- endfor -%}
    {%- else -%}
    {% endif %}

    {% if clearFlowLen > 0 %}
    // clear body
    {% for flow in clearFlows %}
    {%- if flow.description != "" -%}// 描述: {{ flow.description }} {% endif %}
    {{ flow.getCall() }};
    {%- endfor -%}
    {%- else -%}
    {% endif %}

fail:
    return -1;
pass:
    return 0;
}
