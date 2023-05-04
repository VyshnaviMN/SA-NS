<!-- ---
layout: post
title:  "Part 2 - System Requirements"
date:   2023-03-07 17:53:53 +0100
categories: system requirements
--- -->

As with any project it is important to know who you are designing for, what they want, and what they need. In this case we decided to start out with a thorough stakeholder analysis, in the next section we only consider the most interesting stakeholders. 

After we know who we are designing for and what they want we can identify what they need in our system. This is touched upon in the functional requirements section, and combined with the stakeholder analysis and our own preferences we can set up the non-functional requirements, which will be the last section of this part.

# 1. Stakeholder Analysis

Identifying stakeholders is an important and daunting task. We can identify three types of stakeholders: those working on the system, those using the system and those unrelated to the system but able to influence it. The complete stakeholder analysis can be found in this [link](/appendices/design/stakeholder_analysis). In the following paragraphs, we present a general description for each stakeholder category: 

#### 1.1 Project Teams
These are the main system implementers and designers, and are in the end the most important combined with the support teams to keep the system running. Thinking about how to design the system in such a way that a lot of different teams can work together is important to keep in mind in the future system design. 

#### 1.2 Schedulers
While an obvious choice of stakeholders are the customers, when it comes to trains the people creating the schedules are very important not to overlook. On top of being important for the core business of the NS they also need information and access to a lot of different systems within the NS. For example, they have to be able to interact with the expected schedule of arrivals for every station, be able to have a look at train maintenance, or employee schedules. Knowing this beforehand allows us to take this into account in the broader system design and when creating endpoints.

#### 1.3 The Shareholders (Rijksoverheid)
NS presents a unique situation as its only shareholder is the Dutch government. Thus, the main goal is to deliver a proper service in such a way that the constituents will see no reason to complain to the government. Nevertheless, it follows common corporate practices and deals with issues such tight budgets, compliance restrictions etc. Political decisions might also influence the company's way of operation (modus operandi), budget limitations and infrastructure.

# 2. Functional Requirements

The three important drivers of architectural design decisions include: (i) Features of the system (Functional Requirements), (ii) Quality Attributes (Non-Functional Requirements) and (iii) System Constraints such as Time, Finance and Staff (Limitations and boundaries). According to Cesare Pautasso’s "Software Architecture: visual lecture notes" {% cite refpautasso %}, functional requirements need to be correct, complete, and in compliance. This framework is used to identify the functional requirements of the NS system. This section also consists of user stories, various scenarios, related sequential diagrams. The complete analysis [can be found here.](/appendices/design/functional_requirements)

# 3. Non-Functional Requirements

Non-functional requirements are used to describe the intended properties or features of the software system and give direction to the software architects on how to develop the system to fulfil the specified quality attributes. They aid in managing trade-offs between competing quality criteria and arranging the design selections in a more effective order. Our approach follows Pautasso guidelines, taking into consideration Sommerville's approach. Therefore, we discuss five different categories: Design, Normal Operation, Dependability, Security and Long Term Qualities. Our system focuses on a wide range of quality attributes such as Usability, Performance, Availability, Scalability, Security etc. The complete analysis [take a look here.](/appendices/design/non_functional_requirements)

----

[Continue reading the next section.]({% post_url 2023-03-07-part-3-system-design %})

Or are you interested in more in depth view of part on the context consider reading one of these posts:

* Read more about the different stakeholders and what they want out of the NS system in [Stakeholder Analysis.](/appendices/design/stakeholder_analysis)
* Want to discover more of what the NS system needs to create happy stakeholders, have a look at [the Functional Requirements appendix.](/appendices/design/functional_requirements)
* Have a peek inside the kitchen with the [Non-Functional Requirements appendix.](/appendices/design/non_functional_requirements)

---
