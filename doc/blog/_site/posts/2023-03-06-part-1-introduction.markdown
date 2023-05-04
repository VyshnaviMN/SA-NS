<!-- ---
layout: post
title:  "Part 1 - Introduction"
date:   2023-03-08 17:53:53 +0100
categories: Introduction
--- -->

# The NS system

This Software Architecture project studies the NS (Nederlandse Spoorwegen) system. 

As a complex construction with multiple sub-systems, NS presents an intriguing and challenging subject for software architecture research. The system offers various functionalities, including ticket buying, train schedules, real-time train information, and customer service, all of which rely on a sophisticated software architecture. Furthermore, NS has a widely used website in the Netherlands and its quality attributes such as performance, scalability, and reliability are essential to people who commute every day. Analyzing the software architecture of NS can provide valuable insights into how large-scale, real-world systems are designed, developed, and maintained.

# Pyramid Structure

Having identified availability, reliability, security and scalability as our key performance indicators (KPIs) we present and elaborate our proposed solution for NS, Space-based architecture (SBA). This design method organizes the system around isolated and independent functional nodes - "spaces" - which have their own logic, data, and interface {% cite sba_general %}. We argue that SBA satisfies the domain analysis, solves the design problem, implements our architectural description, outweighs alternative architectures and it is doable. Lastly, we present a proof of concept that confirms our argumentation. 



 <!-- we now perform an analysis of the stakeholder concerns and functional and non-functional requirements. Next, we explore the four alternative designs and consider the advantages and disadvantages for each architecture. Lastly, we reach to our proposed approach for the system, space-based architecture, and we provide argumentation about our choice. -->

