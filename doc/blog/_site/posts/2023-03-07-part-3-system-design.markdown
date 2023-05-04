<!-- ---
layout: post
title:  "Part 3 - System Design"
date:   2023-03-06 17:53:53 +0100
categories: system design
--- -->

In this section, we provide an extensive analysis of the NS system design. Following the classical model of the requirements gathering process, we discuss the design of the complete system and lastly the four alternative designs and the architectural decisions of the system compoment we will be focusing on (vertical design). We discuss thoroughly the vertical design at the following blog parts and including our approach for a proof-of-concept.

# 1. Complete System Design

We model a wide high level overview of the NS system. The model presents the system in two levels of abstraction. The first highest representation level has been divided into three parts. The Customer interaction entails the system part a customer interacts with (i.e. the website, the app, display signs at stations and ticket machines). Services component entail all sub-services, products and operations that NS provides. Employees component incldes all the employee tasks and procedures of NS. The second level representations inside these 3 topics represent the aspects of the whole NS system.

![Complete system architecture design image.](/appendices/design/NSbroadsystem.png)

<!-- TODO fix this to discuss the four propsed designs and then why we chose for space based -->
#### 1.1 Train Management Vertical Design

The main goal of train management is to provide live data of the position and status of trains as well as assist in scheduling trains for maintenance. Under here, an initial design drawing is posted, the red parts are considered external systems seen from the perspective of train management, which rely on info or impose limits on the subsystem.


#### 1.2 Alternative System Designs

Having considered many approaches and designs, we decided to propose the following four alternatives for our system design. These include microservices, space-based, event-based and N-tier architecture. We elaborate our approach for each design in a separate page, below:

1. [Microservices Architecture](/appendices/design/microservices/train_management_design_summary_microservices)

2. [Space-Based Architecture](/appendices/design/space-based/space-based)

3. [Event Bus Architecture](/appendices/design/event-bus/train_management_event_bus_design_summary)

4. [N-Tier Architecture](/appendices/design/n-tier/n-tier-architecture)


#### 1.3 Architectural Design Decisions
[In this section](/appendices/design/design-decision), we summarize the characteristics of the four architectural alternatives and draw conclusions on the selected architecture. This decision is based on our KPIs, stakeholder concerns, functional and non-functional requirements with respect to balancing the trade-offs.

#### 1.4 C4 model - Context, Conatiners, Components, Code

The C4 model is a hierarchical approach to software architecture that provides a consistent way to create and communicate software architecture diagrams. It is a simple, yet powerful way to describe and communicate software architecture, especially when working with large and complex systems. [In this section](/appendices/design/c4model), we will apply the C4 model to visualize the architecture of the Train Management aspect of NS system.

#### 1.5 Proof of concept
4. [Proof of concept outline](/appendices/poc/poc_outline)

{% bibliography --cited_in_order %}
