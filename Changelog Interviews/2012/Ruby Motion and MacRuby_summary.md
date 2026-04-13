• Introduction to the podcast, ChangeLog, and its hosts Adam Stachowiak and Wynne Netherland
• Discussion of the hosts' move to GitHub and Sam Sophus's new app, Cheddar
• Interview with Laurent Sancinetti, developer of MacRuby and RubyMotion
• Explanation of MacRuby and RubyMotion, including their features and applications
• Discussion of Laurent's background and experience at Apple and his current startup
• The speaker discusses RubyCoco, a bridge between Objective C and C Ruby runtimes, which had performance and stability issues.
• The idea of re-hosting Ruby on top of the Objective C runtime was proposed by Bertrand Serlet, leading to the creation of MacRuby.
• MacRuby was developed and maintained at Apple for four years, used in several products, including Lion, and was eventually abandoned by Apple.
• The speaker left Apple and started a startup to continue working on MacRuby, eventually creating RubyMotion.
• RubyMotion uses the same runtime as MacRuby but has a rewritten compiler, memory model, and other optimizations for iOS.
• The speaker compares RubyMotion to other tools like Titanium and MonoTouch, but notes that it is architecturally different.
• RubyMotion allows direct access to iOS SDK APIs
• RubyMotion generates a native binary similar to Objective-C apps
• Comparison to MonoTouch, which does the same for C#
• RubyMotion is a native solution, not bridging languages
• Language additions in RubyMotion (selector syntax) inherited from MacRuby
• RubyMotion not open source, but some toolchain components have been open sourced
• RubyMotion allows development without Xcode
• Command line interface used to develop and debug
• Repo provides interactive console for real-time coding and debugging
• Can type expressions and see changes in the simulator
• Allows for debugging and fixing of bugs in real-time
• Objective-C developers find the Repo to be "mind-blowingly fantastic"
• Compared to Xcode, Repo provides a more interactive and dynamic way of developing and debugging applications
• Designing programming languages and runtimes
• Build system for Ruby Motion
• Community growth and open sourcing the tool chain
• Tools developer vs end-user developer distinction
• Laurent's background and interests in programming language design
• Ruby Motion
• Cocoa Pods
• Ruby Motion ecosystem
• Cocoa Framework
• Open source projects related to Ruby Motion
• Libraries for UIKit, CoreData, OpenGL, and third-party libraries
• Use of Cocoa Pods to include pure Ruby extensions for Ruby Motion
• Comparison of Ruby Motion to other tools like Titanium
• Ruby Motion as a gateway to iOS development for non-C programmers
• Objective-C as a C-based language that is difficult for modern programmers to learn
• Ruby Motion's simplicity and ease of use compared to Objective-C
• Ruby Motion as an intermediate step to iOS development
• Ruby Motion as a way to get new programmers into the iOS community
• Teaching iOS development using Ruby Motion
• Potential for mature DSLs (domain-specific languages) in the future
• Ruby Motion's current limitations and need for mature libraries
• Ability to write full-fledged applications using libraries and DSLs
• Potential for Ruby Motion to become a primary choice for iOS development
• Ruby Motion's maintainability, ease of use, and growing community
• Importance of command line tool chain and REPL
• Future features for Ruby Motion and REPL, including a debugger
• Debugger will be similar to GDB, allowing for breakpoints and other features
• Debugger will be integrated into the simulator first, then the device
• Breakpoint method on kernel
• Debugger capabilities on device
• Improvements to Ruby Motion and backporting to Mac Ruby
• MacRuby and its differences from Ruby Motion
• REPL (Read-Eval-Print Loop) interfaces for MacRuby
• Connecting the REPL to a MacRuby app and typing expressions
• Memory management in RubyMotion and how it differs from ARC and manual memory management
• How RubyMotion's memory management works, including the use of auto-release calls
• Future plans for improving RubyMotion's memory management, including introducing a system to handle cycles and automatically clear objects with cycle references
• The decision not to introduce weak references in RubyMotion, citing concerns about breaking the automatic memory management system
• The user asks about the possibility of using blocks in Ruby to save typing, similar to Objective-C.
• The speaker, Laurent, talks about his development tools, specifically GDB and VI.
• Laurent explains that he uses VI for code edition and GDB as his terminal and for starting programs.
• The user asks about plans for supporting instruments or building own profiling tools for RubyMotion.
• Laurent says they will be coming out with something soon, but don't know the details yet.
• He mentions that there is no current way to see Ruby traces when holding a reference to an object.
• He thinks it's possible to do that, and they will try to support instruments.
• The speaker expresses a desire for a memory and CPU profiler to be included in the command line of RubyMotion.
• The speaker suggests that a terminal version of the profiler would also be useful.
• The speaker praises the business model of RubyMotion and the decision to open source certain aspects of the project.
• The speaker discusses the challenges of being a free software activist and creating a proprietary development project.
• The speaker reports that the RubyMotion community has been accepting of the business model and that they are considering charging customers for using RubyMotion.
• The speaker notes that open sourcing the project without a sponsor would be difficult and that finding consistent sponsorship is a problem.
• Corporate sponsorship model for William Motion is being considered
• Potential for parts of William Motion to be proprietary/closed source
• Difficulty in maintaining the platform with current revenue
• Plan to open source as many things as possible
• Current struggle with doing everything in-house (design, marketing, support, engineering)
• Revenue generation is currently sufficient to hire people
• Interest in bringing some of the build system and other pieces of Ruby Motion to MacRuby and non-iOS specific parts
• Replacing the memory model of MacRuby or finding an alternative solution
• Backporting the Ruby Motion memory model to MacRuby
• Creating static libraries or frameworks in Ruby Motion
• Adding support for Ruby Motion code in existing Xcode Objective-C projects
• Improving testing support in Ruby Motion
• Ruby Motion's spec system is based on Bacon, a clone of RSpec
• Default spec checks for a UI window in the app, which fails by default
• Writing specs is test-driven development, and passing the default spec requires creating a UI window
• There's a gem that colorizes the output of rake spec
• Support for UI automation tools (instruments) is being worked on
• Ruby Motion's ecosystem is similar to Cucumber for Ruby, simulating interactions with the app's UI.
• No conversation or dialogue appears to be taking place 
• The speaker is repeatedly saying "bye" 
• The conversation appears to be ending