import * as React from 'react';

import Layout from '@/components/layout/Layout';
import config from '../lib/config';

export default function HomePage() {
  const [u_id, set_Uid] = React.useState("")

  return (
    <Layout>
      <main>
        <section className='bg-white'>
          <div className="ml-16 mt-8 w-full">
            CaseTestC
          </div>
          <div className="ml-16 mt-8 border-2 w-1/2">
            <input placeholder='请输入工程u_id' className="borader-4" onChange={(e) => {
              set_Uid(e.target.value)
            }} />
          </div>
          <div className="ml-16 mt-4">
            <button className="bg-blue-200 rounded" onClick={() => {
              //const formData = new FormData();
              //formData.append("key1", "val1")
              const jsonStr = `{case1: {clearFlowList: [{pthread_join: {paramList: [{param1: {cfg: null, name: pthread_id,    
                type: int}}]}}], declareList: [{pthread_id: {type: int*, val: null}},
      {structA: {type: WeightMsg, val: [{name: {type: char*, val: '"jenny"'}}, {time: {        
                type: DateC, val: [{year: {type: unsigned long, val: 2022}}, {month: {
                      type: int, val: 10}}, {day: {type: int, val: 22}}]}}, {count: {
                type: float, val: 22.33}}]}}], defFuncList: [{func_def1: {description: nothing,
          params: [{id: int*}], return: 'NULL', template: null, type: void*}}, {func_def2: {   
          description: nothing, params: null, return: 0, template: for-loop, type: int}}],     
    description: "\u6B64\u6D4B\u4F8B\u7528\u4E8E\u6D4B\u8BD5\u7EBF\u7A0B\u521B\u5EFA\
      \u6B63\u786E\u6027", flowInfo: "\u6D4B\u8BD5\u521B\u5EFA\u7EBF\u7A0B\u4E3B\u5165\        
      \u53E31", flows: [{pthread_create: {checks: [{status0: 0}, {pthread_id: {op: '!=',
                val: 0}}], description: "\u9996\u5148\u521B\u5EFA\u7EBF\u7A0B", paramList: [
            {param1: {cfg: overflow, name: pthread_id, type: pthread_t*}}, {param2: {
                cfg: null, name: 'NULL', type: null}}, {param3: {cfg: null, name: func_def1,
                type: null}}, {param4: {cfg: null, name: 'NULL', type: null}}], result: {
            isNew: y, name: status0, type: int}}}], headerFiles: [pthread.h], id: 1,
    name: test_pthread_create, people: 'KK, PP, LL'}, case2: {declareList: [{pthread_id: {
          len: null, type: pthread_t*, val: null}}, {some_str: {len: null, type: char*,
          val: '"show_string"'}}], defFuncList: [{func_def3: {description: "\u7EBF\u7A0B\
            \u51FD\u6570\u4E3B\u4F53", params: [{id: int*}], return: 'NULL', template: null,
          type: void*}}], description: "\u6B64\u6D4B\u4F8B\u7528\u4E8E\u6D4B\u8BD5\
      \u7EBF\u7A0B\u5220\u9664\u6B63\u786E\u6027", flowInfo: "\u6D4B\u8BD5\u5220\u9664\
      \u7EBF\u7A0B\u4E3B\u5165\u53E32", flows: [{pthread_create: {checks: [{status0: 0},
            {pthread_id: {op: '!=', val: 0}}], description: null, paramList: [{param1: {
                cfg: null, name: pthread_id, type: pthread_t*}}, {param2: {cfg: null,
                name: 'NULL', type: null}}, {param3: {cfg: null, name: func_def3,
                type: null}}, {param4: {cfg: null, name: 'NULL', type: null}}], result: {
            isNew: y, name: status0, type: int}}}, {pthread_join: {checks: [{status0: {
                op: ==, val: 0}}], paramList: [{param1: {cfg: null, name: 0, type: int}},
            {param2: {cfg: null, name: pthread_id, type: int*}}, {param3: {cfg: null,
                name: status0, type: null}}], result: {isNew: null, name: status0,
            type: int}}}], headerFiles: [pthread.h], id: 2, name: test_pthread_delete,
    people: KK}}`
              fetch(config.devUrl + `/api/uploadcfg/${u_id}`, {
                mode: "no-cors",
                method: "POST",
                body: jsonStr//JSON.stringify({ k1: "v1", k2: "v2" }),//formData,
              })
                .then((response) => response.json())
                .then((responseData) => {
                  console.log("got responseData:", responseData)
                })
                .catch((error) => {
                  console.log("err:", error)
                })
            }}>上传配置文件</button>
            <input className="ml-4" type="file" />
          </div>
          <div className="ml-16 mt-4">
            <button className="bg-blue-200 rounded" onClick={() => {
              const link = document.createElement('a');
              if (u_id.length > 0) {
                link.href = config.devUrl + `/downld/cfiles/${u_id}`
                link.click();
              } else {
                console.warn("Empty u_id!!!")
              }
            }}> 下载工程</button>
          </div>
        </section>
      </main>
    </Layout >
  );
}
