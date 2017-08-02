# -*- coding: utf-8 -*-
from __future__ import print_function, absolute_import, division
import logging
import os
from SpiffWorkflow.task import Task
from SpiffWorkflow.bpmn.serializer.BpmnSerializer import BpmnSerializer
from SpiffWorkflow.bpmn.serializer.CompactWorkflowSerializer import CompactWorkflowSerializer
from PackagerForTests import PackagerForTests
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow
import datetime
from SpiffWorkflow.bpmn.BpmnScriptEngine import BpmnScriptEngine
import time


def script_connect(workflow,msg):
    a=raw_input('please input script route:')
    if a=='/Users/macbookpro/Desktop/Test/data/Test-Workflows/exe.py':
        b={}
        url=raw_input('please input url:')
        b['url']=url
    task=workflow.get_tasks_from_spec_name('sid-2D13DB20-B41B-44C7-BC3B-ECE223C8B793')[0]
    task_spec=workflow.get_task_spec_from_name('sid-2D13DB20-B41B-44C7-BC3B-ECE223C8B793')
    task_spec.script=('execfile("%s",%s,task.data)'%(a,b))


def load_workflow_spec(filename,process_name):
    f=os.path.join(os.path.dirname(__file__),'data',filename)
    return BpmnSerializer().deserialize_workflow_spec(
        PackagerForTests.package_in_memory(process_name,f))

if __name__ == '__main__':
    spec=load_workflow_spec('Test-Workflows/*.bpmn20.xml', 'Action Management')
    workflow=BpmnWorkflow(spec)
    

    start_time = datetime.datetime.now() + datetime.timedelta(seconds=0.5)
    finish_time = datetime.datetime.now() + datetime.timedelta(seconds=1.5)
    workflow.get_tasks(Task.READY)[0].set_data(
            start_time=start_time, finish_time=finish_time)
    workflow.do_engine_steps()
    set_attribs = {}
    set_attribs['choice'] = 'Approve'
    task=workflow.get_tasks(Task.READY)[0]
  

    task.set_data(**set_attribs)
    task.complete()

    task_spec=workflow.get_task_spec_from_name('sid-2D13DB20-B41B-44C7-BC3B-ECE223C8B793')
    task_spec.ready_event.connect(script_connect)
    
    workflow.do_engine_steps()  

    task=workflow.get_tasks_from_spec_name('sid-2D13DB20-B41B-44C7-BC3B-ECE223C8B793')[0]
    print(task.data['result'])
    

