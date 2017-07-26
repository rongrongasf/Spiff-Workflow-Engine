from __future__ import print_function, absolute_import, division
import logging
import os
from SpiffWorkflow.task import Task
from SpiffWorkflow.bpmn.serializer.BpmnSerializer import BpmnSerializer
from SpiffWorkflow.bpmn.serializer.CompactWorkflowSerializer import CompactWorkflowSerializer
from PackagerForTests import PackagerForTests
from SpiffWorkflow.bpmn.workflow import BpmnWorkflow

def startt(workflow,msg):
    print(workflow.get_tasks())

def end(workflow,msg):
    print('end')

def usertask1(workflow,msg):
    task=workflow.get_tasks_from_spec_name('sid-6A83C24E-9609-47CD-B595-BCFC30BBF790')[0]
    set_attribs = {}
    choice=raw_input('input choice:')
    set_attribs['choice'] = choice
    task.set_data(**set_attribs)

def catchevent(workflow,msg):
    while True:
        choise=raw_input('catch event:')
        if choise=='yes':
            workflow.accept_message('Test Message')
            break

def callpython(workflow,msg):
    taskspec=workflow.get_tasks_from_spec_name('sid-516421BF-6D56-4D23-87A5-6E8FC1E2636F')[0].task_spec
    taskspec.completed_event.connect(catchevent)
    

def load_workflow_spec(filename,process_name):
    f=os.path.join(os.path.dirname(__file__),'data',filename)
    return BpmnSerializer().deserialize_workflow_spec(
        PackagerForTests.package_in_memory(process_name,f))

if __name__ == '__main__':
    spec=load_workflow_spec('Test-Workflows/*.bpmn20.xml', 'Test Workflows')
    workflow=BpmnWorkflow(spec)

    task_spec0=workflow.get_task_spec_from_name('sid-6A83C24E-9609-47CD-B595-BCFC30BBF790')
    task_spec0.ready_event.connect(usertask1)

    task_spec1=workflow.get_task_spec_from_name('sid-7C7227E8-087F-4CB6-9B60-200B5D495886')
    task_spec1.completed_event.connect(callpython)


    task_spec2=workflow.get_task_spec_from_name('sid-464B8E64-10B4-4158-BDEE-11144CE20306')
    task_spec2.ready_event.connect(end)
    

    workflow.complete_all(halt_on_manual=False)



