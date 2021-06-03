#!/usr/bin/env python
# coding: utf-8

# # Operating Systems
# 
# We call the collection of software that we use to make a "computer"  "useful" an operating system.  But what exactly does this mean?
# 
# 
# ## Computer
# 
# Today a computer can take many forms from desktop Personal Computers (PCs), laptops, mobile phones, tablets, building scale super-comptures, etc.  In some sense the defining property we care about is that the device supports a classic model for programming it -- we call this model the VonNeumman architecture.   We will discuss this model in much more detail when we start considering exactly how software and hardware work.  For the moment it suffices to say that programming it means being able to apply your knowledge of a programming language and existing software to have the computer do something you want it to.  For example, edit photos, play music, maintain a list of grocery items, calculate PI, send email, browse the web, test if a molecule might have promise as a new vacine, automatically adjust the temperature of your home, control a car, etc.  
# 
# ### Programmer vs User
# 
# To be honest many people simply care that the computer can run existing programs we will call these folks "Users"  However, "Programmers" are a special type of user.  Programmers use Operating system, and other software tools to create new programs themselves.  As a matter of fact some programmers simply focus on developing programs that make writing programs easier -- like the folks that develop the operating system software, programming languages, editors, etc.  
# 
# ## Useful
# 
# So from our perspective, the main aspects of the operating system, that we care about, is that it makes it ease for programmers to create new programs and does not hide things from us so that we can explore how programs (and  computers) work.  
# 
# Operating Systems are designed and created with specific uses and hardware in mind.  Some are designed for special purpose computers and the programs that are expected to run on them like computers built into an airplane to control is various parts or a super-computer which is expected to run complex and large scientific simulation programs.  While other operating systems are designed primarily to enable users to install and run commercial grade programs on their personal devices.  These operating systems while they do enable programmers to write new programs they are designed to hide most of these aspects from their target user who mainly just wants to use programs written by others.  The interface of these operating systems tend to focus on graphics and visually oriented ways of interacting with programs.
# 
# ## Why UNIX
# 
# UNIX on the other hand assumes that its users are primarily programmers.  Its design and collection of tools are not meant to be particularly user friendly rather it is designed to allow programmers to be very productive and also to support a broad range of programming tools.  Many of the concepts and mechanisms of UNIX underly other operating systems but have been hidden or obscured to make things easier for non-programmer users.  
# 
# ## UNIX organization / philosiphy
# 
# Given its programming focus UNIX is organized around two categories of software -- kernel and user.  The kernel is a componet of the UNIX that most users of UNIX do not directly interact with.  It is the core software that is used to manage the various devices of the computer and construct an environment that allows programmers to create new users programs.  The idea is that very little is really built into UNIX rather its users are enouraged to write lots of small programs that extended the functionality of the kernel to do useful things.  The kernel main job is to provide the ability to run new program, provide those programs with access to the hardware, and common ways for programs to interconnect.  
# 
# I know this all sounds a bit recursive -- welcome to computer science.  As we start interacting with UNIX it will make more sense. 
# 
# ## Bottomline
# 
# To this end, out of the box, UNIX comes with the kernel and a large collection of existing programs that permit a programmer to write more programs that they and others can use.   In this class we will focus on what a program really is, how they are constructed and along the way the core tools, skills and ideas that underly all of computing.  Given UNIX's programmer focus and transprancy it is an good choice for us and learning how to be productive in the UNIX environment will teach us a lot about how to be productive programmers period.
# 
# ```{note}
# An example of an admonition with a title.
# ```
