# Spiff-Workflow-Engine
深入调研使用与BPMN兼容的Python工作流引擎Spiff，Ref. https://github.com/knipknap/SpiffWorkflow

## 概述

### 工作流引擎

在互联网应用开发过程中，事务性流程性的需求非常常见，如果针对每一种流程需求都逐一开发，势必会大大增加开发工作量，也降低了系统的维护性，因而针对事务性和流程性的需求，应该使用工作流引擎极其配置方法，实现功能定制，遵循一定的流程定义标准（例如BPMN标准），实现流程的高效开发。

### 工作流模式

根据BPMN2.0描述的工作流标准，工作流由角色、行为、分支和泳道等角色组成，又称为泳道图。角色在泳道图中某个起点开始，不断地实施行为，最终结束于某个终点，完成完整的工作流推演。而根据Spiff的github[网页介绍](https://github.com/knipknap/SpiffWorkflow)中说，工作流引擎本身是存在诸多工作流模式的，参见[链接](http://www.workflowpatterns.com/)。具体而言，工作流模式都有哪些？在使用过程中需要注意什么呢？

#### 工作流模式详解



#### 工作流模式的应用举例





## 工作流引擎框架Spiff

Python社区中涌现的Spiff框架，可以支持三种不同的方式描述定制的工作流，XML方式、JSON方式、Python方式，这三种方式描述的工作流引擎如何与外部交互？工作流引擎如何实现嵌套与泳道角色跳转？都有待于进一步研究。