**Mat Ryder:** Hello there, and welcome to a very special episode on Go Time. It's a Gopher Con mashup. This is the lunchtime sessions for Gopher Con, and also a Go Time episode, so welcome.

Today we're talking about what we do when things go wrong. A manager once asked me to only write code that didn't have any bugs in it; that was an interesting thing... We're going to find out today what are bugs, and what can we do to get rid of them, or make sure they're never there in the first place. We'll look at tools and techniques around this too with our expert panel, who I'm going to introduce now.

Furthermore, we're joined by Hana Kim, from the Go team. Hello, Hana!

**Hana Kim:** Hi!

**Mat Ryder:** Welcome to Go Time.

**Hana Kim:** Yeah, I don't know if I'm an expert, but thank you very much for inviting me to Go Time. It's so exciting, I'm so honoured.

**Mat Ryder:** Yes, you are more than welcome to be here. Sorry, I sometimes do accidentally say "expert" and people don't like that. It sets things up, so... \[laughter\] Don't worry, no pressure. We're also joined by Grant Seltzer Rich man. Hello, Grant.

**Grant Seltzer Rich man:** Hi. Thanks for having me.

**Mat Ryder:** Well, welcome, mate. You're very welcome. Are you having a good day so far?

**Grant Seltzer Rich man:** So far, so good. Gopher Con is -- so far the talks have been great.

**Mat Ryder:** Great. Well, hopefully we won't ruin it. \[laughter\] And we're also joined by Derek Parker. Hello, Derek!

**Derek Parker:** Hello, everybody.

**Mat Ryder:** \[04:15\] Hello. Welcome to Go Time/Gopher Con lunchtime session.

**Derek Parker:** Thank you. And good evening, good morning for me on the West Coast... I'm having my second cup of coffee.

**Mat Ryder:** Great. Enjoy it! So yes, I should say - Derek, you work at Red Hat, and you've actually created Delve, which is a debugger.

**Derek Parker:** Yes, that's correct.

**Mat Ryder:** Okay. So this will be good, because we'll definitely dig into that a little bit more. It's such a great tool, and it's a great way to get rid of bugs. But maybe we could start - what is a bug? Why was it a little bit absurd that my manager asked me to only write code that didn't have bugs in it?

**Derek Parker:** What is a bug - a bug is something unexpected in your code, or something incorrect; that's how I think most people typically think of it. It's something not only unexpected, but just incorrect; a wrong result, or a wrong something. And the absurdity of that statement comes from "How can you have the premonition not to--" You know, sometimes it's maybe a little bit out of your control when a bug happens.

I would say weird things can happen, like running on a different architecture could expose a bug that you wouldn't have seen on the CP architecture that you're using, or in a different environment, or with different environment variables, or whatever. There could be so many things outside your direct control that could expose a bug, which I think is part of the absurdity of that statement, that "Please write code that does not have bugs." \[laughs\]

**Mat Ryder:** Yes. Right, it's just behaviour that happens that we don't want to happen. But of course, there's no way for the compiler to know that that shouldn't happen. It's not like a type error, where you can have a compiler look at the code and tell you, or fail the compilation if things aren't right. It's kind of they sometimes emerge from either different ways things are interacting, or just sometimes it's -- you know, you've made a mistake; that happens, too.

**Derek Parker:** Sometimes bugs turn into features, so... \[laughs\]

**Mat Ryder:** Yeah, absolutely. Especially when I've done it; I will always pretend it was meant to be like that. That's a great one.

**Derek Parker:** \[laughs\]

**Mat Ryder:** So what do we mean by debugging then? Is this just any method, anything you do to get rid of bugs? Is that debugging? Or is debugging a more specific technical term?

**Grant Seltzer Rich man:** I suppose when you're using a debugger, doing some type of debugging, you're trying to figure out what it is that's causing this unexpected behaviour; everybody has an intention when they're writing their code, so just like how you said that there's no way for the compiler to tell what you meant for your code to do, it's doing exactly what you told it to do. So let's say you're seeing some bugs - output that's coming out of your program is not as expected, or you're just seeing some errors that you didn't expect to happen. The active debugging is trying to figure out what's causing that bug, where in your code did you have some logic that isn't what you intended it to be, and trying to figure that out so that you can then fix it.

**Mat Ryder:** Yeah. And when you come to debugging then, with techniques and tools, do you have a particular favourite? What's the first thing you do when you've noticed something's wrong? Does it depend, or...?

**Grant Seltzer Rich man:** \[07:51\] So I will say that I think there's a sort of half-joke within all the tech industry, that adding print statements to your code is wrong, or like an amateur approach... But to be honest, if your program compiles particularly quickly, there's no reason that adding a print statement should be looked at as like a dirty way of doing it. So the feedback loop - when you're debugging, you want to have a quick feedback loop.

So if it's a simple enough program where you could just add a print statement at a certain point, that's printing out the contents of variables, I don't think there's anything wrong with that, because it's an intuitive interface. You know that like "I want to know what happens at this point in the program..." If it's a particularly complex program, or the compile time is long, and you need a faster feedback loop or something like that, that's when I would typically use a debugger or some type of tracing tool. But... Nothing wrong with print statements.

**Mat Ryder:** Yeah, I'm really pleased you said that, because I've met junior developers who feel like they don't know how to use a debugger, or they don't know what they're doing, and they just put prints out. But it is completely legitimate. In fact, it tends to be my go-to thing, doing that.

There's a particular verb that's very useful in Go. If you use the FMT package, you can do %+v, and then give it any type, and it does a perfect job of describing that type, even if it's a complicated struct, with nest data, and all sorts. And you see the field names too, which is quite useful.

Are there any other favourite techniques like that, that are sort of simple, debuggable things? Printings were a great one.

**Grant Seltzer Rich man:** I'm sure both Derek and Hana can talk about using Delve, but I certainly use Delve, a full-fledged debugger.

**Mat Ryder:** Right. Delve is a different beast, really. And the other one that we should talk about before we get onto Delve is test code. Because actually test code is a great way to debug your code. One trick that I find works really well is if somebody identifies there's a bug, if you ask them to write a failing test, if they can do that, that is a great way. You remove all ambiguity, you're speaking the same language, you look at the code, and if it's a failed test, you know, you've proven that there's a bug there. And sometimes the test is wrong, and some of the assumptions are wrong; that's one thing. But usually, it does kind of highlight the bug. And then, of course, once it's fixed, you can put that test into your test suite, and you can never get that same bug again.

Hana, you work on the Go team, and you're working on the VS Code plugin for Go, right? So tell us about that then. That plugs into the IDE, it integrates... So it turns visual code from being what may be just a sort of basic text editor, and adds some kind of Go intelligence to it. Is that fair?

**Hana Kim:** Yeah. And also, it has a debugger integration, too. And also facilities that actually help users to write a good test; or emulating, and auto-complete, and those kinds of features... And also like a test comment. So with just one click, you can write a test in your package. So for a debugging purpose, I think my go-to is still a print and look over it, that kind of thing...

**Mat Ryder:** Yeah. So maybe it's time then just to talk about Delve. Maybe we could start by -- just for anybody that hasn't used a debugger before, and maybe Derek, this is one for you - what is a debugger, and what's it doing? How does it work, how do you use it?

**Derek Parker:** Yeah, so I actually heard a perfect explanation yesterday from Jason, who I was co-instructing a workshop with...

**Mat Ryder:** The format? Or is it a human? You're not talking about the data format...

**Derek Parker:** No. \[laughter\] As a human.

**Mat Ryder:** \[12:08\] Got it. That was a half-joke, like what Grant did earlier. \[laughter\] Go on, sorry.

**Derek Parker:** I liked the way that Jason explained what a tool like a debugger is. I think the name debugger is a bit of a misnomer. The tool itself doesn't actually fix the bug for you; it's just a tool that you can use to understand your program. It's a way to just understand what your program is doing, and then once you figure out what's going wrong, you can fix the bug.

**Mat Ryder:** It doesn't fix the bug for you, but whose fault is that? You're the creator and co-maintainer of Delve, so really, you've only got yourself to blame there.

**Derek Parker:** In the next release. We're working on it. \[laughter\]

**Mat Ryder:** But it's actually an interesting point - it can't be done automatically; otherwise, of course, the tooling would be doing it for you. You have to tell it what correct is, and you've already told it what incorrect is, right?

**Derek Parker:** Yeah, I think it's approaching any kind of debugging situation with the mindset of "How can I gain insight into what's actually happening, and how can I do that in a way that will quickly allow me to figure out what's going wrong, so that I can fix it. And like Grant said earlier, whatever gives you the fastest feedback loop, that's what you should pursue.

I do print debugging all the time as well, especially when -- like, working on Delve, it's hard to debug a debugger with a debugger sometimes... So doing print debugging in those situations, and whatever gives you the quickest feedback loop I think is the best tool to reach for in that situation.

**Mat Ryder:** Okay, so if printing the results isn't working for you, then Delve allows you to set a breakpoint. What happens then in the program? The program stops at that point.

**Derek Parker:** Yeah, exactly. So with a tool like Delve, a traditional source level debugger, you're interacting with your program in real time, and that's what's fun and interesting about using a debugger - you have the ability to stop what's happening, inspect state, even change state if you want to continue...

For example, when you start up a new debug session, and you set a break point, and you continue to it, you're telling the program "I want to stop at this specific location and just check out what's going on. See how I got here." You can look at the stack trace, you can see the value of variables. And if you wanna experiment a little bit, debuggers also can let you experiment. You can, for example, change the value of a variable and see if that gives you the result that you wanted.

So it gives you a little bit more of like real-time interaction... Getting back to that quicker feedback loop, without changing a variable in the code, recompiling it, rerunning it, trying to hit that bug again, or seeing if you don't... You can do some interactive stuff within a debug session.

**Mat Ryder:** And you can step then through the instructions; so you can advance the program step by step, slowly, and keep an eye on things, just so you understand what's happening. It sort of puts it into slow motion and lets you do that carefully, right?

**Derek Parker:** Yeah, absolutely. Exactly.

**Mat Ryder:** And how does that actually work? What's going on? Do you have to build the binary specifically with that debug information added to it, or can you just debug anything?

**Derek Parker:** All binaries include information -- it's called DWARF information. And that's like a standard format of debug information, basically. It tells tools like Delve how to find variables, how to unwind the stack, how to do all kinds of things.

Go by default will build that into all binaries. You have to opt out of it specifically. And the only reason why you would opt out of it would be maybe you really care about binary size, and you want to get out every last bit that you can to shrink your binary as much as possible. But by default, that information is going to be in there.

\[16:16\] The only other thing that Delve does by default, and I would recommend folks do if they're going to try to debug their Go applications/processes etc. is Go also by default will put in optimizations. If you're familiar with GCC or some other compiler, you have to explicitly tell it what level of optimization you want, and you kind of have to opt into some of the more extreme optimizations. But Go does that by default, and that's great for when you're building a production binary - if you want to ship it off, it's going to be fast and performant, and all that. But it could hamper debugging a little bit, because in-lining functions can get weird sometimes... Delve handles it really well now, and the Go compiler has gotten a lot better at providing information for telling debuggers how to handle that. But there's still certain weirdness there that you can run into when trying to debug and optimize a binary. So that's the only caveat that I would explicitly mention.

**Mat Ryder:** That's interesting. Hana, when you talk about the VS Code plugin, and it has debugger support, does it support Delve?

**Hana Kim:** Well, actually, Delve is behind the scenes. Other editors, like Poland, they also use Delve. Basically, this idea that when a user requests to debug their code, it actually formulates, "Oh, this is a Delve comment", and then invokes Delve, and asks Delve to answer the question. And most of the modern IDEs - they have either this local variable, global variable, or stack trace... So it just asks Delve, and all the information is visible through all this UI, and then users can actually step through the program using the UI... And again, we ask Delve to do all this job.

So the idea is to provide the best user experience and visualize the data coming in and coming out, all the information between Delve and the frontend.

**Mat Ryder:** That's really nice then. So you don't have to learn these complicated commands, and you don't have to know about the DWARF data or anything like that, because it's integrated.

**Hana Kim:** Yeah, ideally...

**Mat Ryder:** Yeah. Because it's integrated, you get to just do it right in your code, the same place where you're writing the code. So that's really cool. How do you actually do that then in VS Code? How do you set a breakpoint?

**Hana Kim:** Actually, the nice thing about Delve is Delve has the API. Like the oldest method and the instruction, they can be invoked through the RPC. So we just launch the headless Delve server, and then from VS Code we just invoke this RPC. There's some recent movement about a Debug Adapter Protocol; that is kind of like a standardized -- so Delve is a Go debugger, but there is GDB, there's LLDB, and there is a JavaScript debugger... There are all kinds of debuggers, and we have VS Code.

So the VS Code team - they tried to standardize the interaction between debugger, just generally a debugger, and the editor. It's called the Debug Adapter Protocol, and the VS Code Go extension speaks the Delve adapter protocol and there is a small, tiny Delve debug adapter that actually talks Delve RPC. So it's a little bit complicated, but we try to simplify this communication path, so that the next version, I hope, the communication is more efficient. So that is the general direction we're heading in.

**Mat Ryder:** \[20:16\] That's really cool. It's nice, because as users of this, we don't have to worry about that. That's something that happens behind the scenes. We get to just use the VS Code interface. That's really great.

**Break:** \[20:35\]

**Mat Ryder:** I'm interested - Grant, is your talk on Friday?

**Grant Seltzer Rich man:** Yes, Friday. I think something around 4 o'clock.

**Mat Ryder:** Mm-hm. It's meaningless to me, because I'm in a different timezone...

**Grant Seltzer Rich man:** Oh. Eastern Time.

**Mat Ryder:** Yeah, okay. I think we should get rid of timezones, by the way. I think that was a bug. There's a bug in that, to be honest.

**Grant Seltzer Rich man:** We should all just follow New York Time.

**Mat Ryder:** If you like... I mean, you jump to an assumption there. \[laughter\] I live near Greenwich, which is actually where they invented time, I think... Do you know what I mean?

**Grant Seltzer Rich man:** I live near Greenwich Village.

**Mat Ryder:** Yeah, okay. \[laughter\] I wasn't going to say there's a line, and you crossed it; I was going to say in Greenwich there's a line that's like the meridian zero line. You can go and stand across it.

**Grant Seltzer Rich man:** I got you.

**Mat Ryder:** Yeah, it's alright. \[laughter\] I was going to ask, what is your talk about, on Friday?

**Grant Seltzer Rich man:** My talk is about tracing Go programs with EPF. EPF has been talked about a lot at various different conferences for the past 2–3 years, it's been getting a lot of momentum... And it's a feature of the Linux kernel, so it's certainly Linux-specific... But what it allows you to do is add ad-hoc app logic to the Linux kernel. And I know that's very abstract, but the way that it's often put - Brendan Gregg, a leader in the EPF space likes to put it as "EPF does to the Linux kernel what JavaScript does to HTML."

\[24:05\] So you can attach EPF programs, you can think of them as scripts, and attach them to various hooks, such as to network sockets every time a packet comes in, and have some logic. Or to kernel probes, every time source code is executed within the Linux kernel itself.

In particular, what my talk is about is attaching EPF programs to something called probes. Probes attach to what essentially is source code symbols. So if you have a Go program that has a function called test function, you can attach an probe to that, and attach an EPF program to that probe, so that every time a process executes that function - so if you run that program, and it's a running service, or whatever else, you could have essentially a script respond to that function every time it's called; so you could print out what the arguments are, you could have some logic for inspecting another area of memory, and it's useful for debugging, for monitoring, potentially for fuzzing or fault injection as well.

**Mat Ryder:** So does the original function still run, and you're just sort of intercepting it? Or do you replace it?

**Grant Seltzer Rich man:** That's a perfect question. So it does still run... It doesn't stop the program from running at all; it doesn't affect the process. It runs in its own virtual machine inside the Linux kernel, actually. So the difference between where -- I guess there's a lot of difference in terms of the underlying technology, but the advantage to EPF, which I guess could also be seen as a disadvantage compared to debuggers, is that it's not stopping the program. It's not attaching to the process. You can have a running program that is completely unaware of the fact that it's being inspected via EPF.

**Mat Ryder:** Because you're doing it down at the low-levels of the operating system, I guess.

**Grant Seltzer Rich man:** Exactly.

**Mat Ryder:** So what use cases are there for that then? From kind of debugging, practical standpoint. What sorts of things can you do?

**Grant Seltzer Rich man:** I have a project - I'll shamelessly plug it; I'm almost at a hundred stars... Go star it. It's called Weaver. It's on my GitHub, /grant seltzer/weaver, and what I'm trying to do is have Saracenlike functionality. Trace is another tracing tool that you run a program, and it'll print out every time a system call is executed. I'm trying to have a functionality like that for Go programs, where you run a Go program and every time any function inside of that is called - so all of your functions in all of your packages, every time they're called, they'll print out a line with "It was called at this timestamp, and the arguments passed had these values, and its return was X, Y or Z."

So the application there is, you know, for debugging purposes, let's say you want to know why you're getting some garbled output, and you want to know at what point down the function call stack a function was getting some weird output. And you see somewhere along the line a wrapper around print is getting really weird outputs; so then you might want to start inspecting at the function that called that one.

It's also useful for -- not that I'm saying that this is the greatest idea; it's still a developing ecosystem, but you could attach these two services running in production, because it has such a minimal effect on the performance of the service. And you could attach it to running programs, as well.

**Mat Ryder:** \[28:01\] That is fascinating. Can you interact -- I guess you can't change things in these little EPF programs, can you?

**Grant Seltzer Rich man:** I have a little example of how you can, actually, in my talk. There's a perfect talk that was given at some security conference (I can link it later) of how you can write essentially malicious code with EPF... But even for non-malicious purposes, you could actually write to memory from EPF. So you can change the value of parameters, which I do in my talk.

**Mat Ryder:** Wow. And would you recommend that, or not sure yet?

**Grant Seltzer Rich man:** I think it has its use cases if you are trying to do let's say something like fault injection, where you have processes that are communicating with one another, and you have a function that is pulling in from another endpoint... And if you don't want to have that external dependency, you could have an EPF program that writes some garbled data to a particular function and see how your program reacts to it.

You could also, if you have a compiled and running service, and you want to see if a particular fix to your source code will fix the issue - you can insert a small EPF program that writes correct data... You know, if it was getting incorrect data and if that fixes your whole issue, you know that's the symptom of it. But I guess it depends on a case-by-case basis. Certainly not in production, I'll say that.

**Mat Ryder:** So these scripts - what language are they? Does it have its own little language? Is it something that would be familiar to us?

**Grant Seltzer Rich man:** So it would be familiar to you -- it's essentially C. It's a subset of C. There are some restrictions to it, but it essentially looks like C. I guess the language could be called BPF. There's a verifier within the Linux kernel when you try and load the byte code. It's an LLVM-backed compiler.

**Mat Ryder:** Nice. It's a fascinating thing. What's next before we can start using that kind of technique? Because it feels like it's quite a new thing on the scene. Has it been around? Where does it come from?

**Grant Seltzer Rich man:** The original technology of it I think was -- I don't even want to guess... Early 2000s. It used to be strictly for network packet processing. But I would say it's been within the past two years or so that the ecosystem has really developed. There's a group of startups -- I know Facebook does a lot of EPF stuff, and they've contributed to the community quite a bit. I would say there's no better time to start doing it than right now, because the ecosystem definitely is developing, but there's a really strong community of people who really help one another, try and figure this all out and define what good EPF code looks like and what the ecosystem -- how it's related to Go looks like. So I think it's best to get in at the ground floor, so to speak.

**Mat Ryder:** Very interesting, yeah. It's definitely something to play with. It sounds like one of those things that can be extremely powerful, but also a bit like in C and C++ - you could do operator overloading, and things, which is used correctly, can be great. But as soon as it's abused, you end up not knowing what an @ means in the code, or what a plus symbol is doing to things.

**Grant Seltzer Rich man:** Yeah, fair enough.

**Mat Ryder:** It's probably one of those things you would end up using very cautiously, I suppose.

**Grant Seltzer Rich man:** Yeah, that's fair. I will say that the goal of my talk is to show how accessible the technology is. You don't have to have any expertise in the low levels of Linux, or even of Go, for that matter. You could really start playing around with it, and it can make a whole new class of problems much more accessible to so many more people.

**Mat Ryder:** \[31:56\] Have you ever used it, Derek? Are you aware of it?

**Derek Parker:** Yeah, I've done a few things with EPF a little bit here and there. Actually, Delve has a trace functionality which works somewhat similar, but it works at a higher level, using trace and some of those other kinds of miscalls. I've thought about experimenting a little bit, replacing -- on Linux systems I supported replacing that with an EPF-backed tracing system... So Grant, if you ever want to send a pull request, we'd love to have it. \[laughter\]

**Hana Kim:** Yeah, I am happy to integrate it from the VS Code side, with visualization... \[laughs\]

**Grant Seltzer Rich man:** I would love that.

**Mat Ryder:** This is the most productive meeting I've ever been in. \[laughter\] And it wasn't even meant to be a meeting.

**Derek Parker:** Yeah. And the benefit, like Grant was talking about it the EPF route, versus -- so Go does it at a higher level, using trace miscalls and various other miscalls on different platforms, like Windows, and stuff like that... But the fundamental problem of why it's slower than the approach that Grant described is EPF stays all within the kernel. So there's no context switching from kernel space, to user space, back to kernel space, back to user space... That context switch can get expensive. So when Delve traces, in kind of more portable way, it traces in such a way where there's -- you know, you do switch from the kernel to user space, back to the kernel, back to the user space, and typically, you don't really see that much of a slowdown if you're just tracing a program locally, or something like that... But certainly, there's a performance hit there that could be alleviated by switching to EPF where appropriate, where possible.

**Mat Ryder:** But usually, people are debugging not in production... Does that change at all, or we're still going to keep doing it how we're doing it, if you know what I mean.

**Derek Parker:** I think with EPF you can make the case that it's easier and a little bit safer, and more rational to do in a production environment. I wouldn't recommend doing a Delve trace on a production system unless you really had to. You're just going to run into some performance penalties there; that's really the biggest issue.

**Break:** \[34:19\]

**Mat Ryder:** Hana, you mentioned earlier that Delve has an RPC API... What is that? What does that look like? How do you consume that? How does VS Code -- is it an HTTP API? Is it a proof? How does that actually work?

**Hana Kim:** Yeah, so Derek is here to answer the question... I think that there's a JSON RPC one; it's just like the JSON stringing between client and server; it's a simple one. A kind of JSON-RPC 2.0-based protocol... So just a JSON message exchange.

**Mat Ryder:** Hm. So you start the program, start the debugger, Delve, and does it then return some endpoint for you to hit, or how does it work?

**Hana Kim:** \[35:59\] Yeah, so just a connected to the socket... At the port, and then create a socket, and communication over the socket.

**Mat Ryder:** Very cool. Well, I ask that, because that's quite interesting - I think there's a whole space of tooling, particularly static analysis, or even other runtime tools, like debuggers... And there's a lot of choice for how to build those things so that they can be easily consumed by plugins, and things... So it is always quite interesting to know about that.

**Hana Kim:** Yeah.

**Mat Ryder:** When did the VS Code plugin officially get taken up by the Go team? Because it used to just be something else before, didn't it?

**Hana Kim:** Yeah, so it was originally owned by the Microsoft team, and I think VS Code Go was one of the oldest languages supporting a plugin VS Code team effort. And then for a while it was in the maintenance mode, and this year actually we got the responsibility to maintain... So I think there was a blog post from [blog.golang.org](https://blog.golang.org/vscode-go) about this transition. Now the tool team inside the Go team in Google - we are maintaining this plugin.

**Mat Ryder:** Hm. How many is on the Go tool team?

**Hana Kim:** Tool team... Hm...

**Mat Ryder:** I remember when there was just the Go team, and now it's like there's a security team, there's a team for tools... Right? It's really growing.

**Hana Kim:** Yeah, there is a high demand. We need a lot of work to do... So there's currently the goals team. Goals is one of the biggest projects. I don't know if you heard about it...

**Mat Ryder:** Yes...

**Hana Kim:** That is the language service implementation for the Go language... And the Go tool team is to basically provide the best developer experience, including the debug support or language intelligence support. So VS Code Go is one of the projects. Currently, we are based in New York, and a few of us are working on various aspects of the developer experience improvement.

**Mat Ryder:** Well, we all appreciate all the work, of course...

**Hana Kim:** Thank you.

**Mat Ryder:** ...because it's very nice for us; we just get to use it, and it hopefully makes our lives easier... So I do like to thank people that have contributed. This goes for everyone on this call. Can you give us any spoilers about things that you're working on now, or that we might see soon? I won't tell anyone...

**Hana Kim:** \[laughs\]

**Mat Ryder:** That's legally watertight...

**Hana Kim:** So what's coming next? Yeah, we are currently working really hard to use goals as the default Go language service... And also, we are now currently working on -- I think I talked about it, the debug adapter protocol, so that we can simplify and then provide a more performant debugging experience for VS Code users. So they are the two big, main projects I am currently working on.

**Mat Ryder:** Great. That sounds good. And what about for Delve? Is that pretty much done, or is there a roadmap there? I'm interested in what's coming next for that, too.

**Derek Parker:** Yeah, it's one of those things where it's still constantly evolving. We have a few big things planned. We always work to keep up to date with the latest Go release. Go 1.16 is coming out soon. With each release like that there are subtle things that may change in the runtime, or how the binaries are put together that Delve has to adapt to... So we continuously work on supporting the latest release, making sure that by the time that release comes out, there's a Delve version that can support and debug it. So that's always kind of a big thing for us.

\[40:15\] We also have a few interesting features coming up down the line... My co-maintainer is working on a feature where during an interactive debug session you can create and produce a core dump from the process that you're debugging. It's similar to score, if folks have ever used something like that, but it works a little bit differently. So that's a cool feature that's coming up.

Another big push that we're trying to do is improve the overall architecture support. Right now, Delve actually only supports a subset of all the architectures that Go can actually run on... And it supports the main ones that folks actually use. You know, AMD64, ARM64, things like that. But there are some outlier architectures that Go supports that Delve doesn't yet, that we're also working on as well.

There's a pull request up right now for supporting 32-bit ARM, we're looking at supporting PowerPC 64 and S390x, which are kind of weird architectures... But those are kind of some of the bigger things that we have on the roadmap so far.

**Mat Ryder:** What about Apple Silicon?

**Derek Parker:** Yeah, that's an interesting one, because -- we have a few different backends that Delve can actually use. So there's a native backend, which we actually wrote and maintained, and we can actually interact with other backends. The talk that I'm giving tomorrow is on using Mozilla RR as a backend to do record/replay debugging. So with that, Delve on macOS actually uses LLB-server as the backend. We have a native Mac backend, but it turns out that the documentation for the mock kernel is horrendous, and trying to figure out how to actually work and interact with that kernel means -- like, when I wrote the original backend for Mac, it was digging through the open source kernel to figure out some of these trace commands, and some of these weird stuff that I had to do, because the documentation is subpar for that kind of thing.

So all that to say we use LLB-server on the backend, so there are some changes that we have to do internally with Delve... But some of the heavy lifting we kind of get for free by using LLB-server, which Apple is certainly going to make work on their silicon...

**Mat Ryder:** Okay, great. Wow, Delve really is kind of a big thing... I always think of it as this little tool. I mean, how big is it?

**Derek Parker:** Big in terms of what metric?

**Mat Ryder:** Size.

**Derek Parker:** It's a fairly --

**Mat Ryder:** No, I don't know.

**Derek Parker:** The scope of the actual source code and all that stuff - it's definitely grown, and it's grown a little bit in complexity over the years as we've introduced different backends, and things like that. The goal has always been to keep it as simple and straightforward from a code perspective as possible, but over time, obviously, things get more complicated, and you have to deal with weird situations. But yeah, from the perspective of the code and stuff like that, the project itself is a fairly big project, at this point.

**Mat Ryder:** Yeah, it sounds like it. When new features come to Go, like to say generics lands in Go, what will that mean for Delve? Is there things you're just going to get for free, or will there be times when certain language features are added, that that creates a lot of work for you?

**Derek Parker:** It depends. So a lot of that we would get for free a little bit, by the kind of debug information that's provided from Go binaries, and things like that. So it would kind of be up to the Go compiler and linker to produce the correct information that Delve needs to be able to debug that stuff properly. And with big, new features like that, sometimes the support is there, sometimes it's not. Sometimes we have to work with folks upstream to get that in, or submit some patches ourselves, and things like that. But a lot of it comes with just coordination with the Go team.

\[44:06\] There are certain things that are Go-specific that we've had to work really closely with the Go team to be able to achieve... For example function calls; this is something that actually requires support from the Go runtime, and we had to work with the Go team to make that happen. It was a coordinated effort. So sometimes there's more coordination, sometimes we get stuff for free.

**Mat Ryder:** Cool. Okay, well, it's time for our regular slot, it's time for Unpopular Opinions.

**Jingle:** \[44:33\] to \[44:49\]

**Mat Ryder:** So who wants to kick us off with an unpopular opinion?

**Grant Seltzer Rich man:** When you mentioned this, I was going to say that print statements are okay for debugging, but I don't think that will be that unpopular... So I will say that baseball is by far the most exciting sport in the world.

**Mat Ryder:** Baseball. Which one's that?

**Grant Seltzer Rich man:** It's the one with all the bases, and the ball.

**Mat Ryder:** The ball. The clue's in the name.

**Grant Seltzer Rich man:** Absolutely.

**Mat Ryder:** Clever name, actually. I genuinely didn't actually make that link. Well, baseball gives us lots of metaphors, doesn't it? It contributes the most metaphors. But I don't know...

**Grant Seltzer Rich man:** Sure. \[laughs\]

**Mat Ryder:** Hana, do you agree? Is baseball a good sport?

**Hana Kim:** Other than U.S. and some Asian countries, who plays baseball?

**Mat Ryder:** Yeah, I don't know.

**Grant Seltzer Rich man:** Latin America.

**Hana Kim:** Oh... Yeah. \[laughs\] And in Europe?

**Grant Seltzer Rich man:** Nah, not really.

**Mat Ryder:** No, we have different versions of it, I don't know. But yeah, that is potentially unpopular.

**Hana Kim:** But they are missing the best sport, right?! \[laughter\]

**Mat Ryder:** Apparently so, yeah. That's what we've heard... According to Grant, yeah. Derek? Is baseball the best sport?

**Derek Parker:** Best, or most exciting...? I would refute most exciting. I think football is pretty exciting. Furthermore, I get excited watching -- I don't know if you consider this a sport, but I like watching poker championships, and stuff... And that sounds pretty exciting. So it depends on your metric.

**Mat Ryder:** I watch the Star craft championships online.

**Derek Parker:** Yeah, there you go.

**Mat Ryder:** It's exciting.

**Grant Seltzer Rich man:** It's awesome

**Derek Parker:** Yeah, yeah.

**Mat Ryder:** But I just don't go outside, so... certainly not to play baseball.

**Derek Parker:** \[laughs\]

**Hana Kim:** I think baseball is exciting, especially because when you watch baseball, you eat hot dog, you drink a beer... How cool is it? That's the most exciting one. Soccer - you have to watch. Basketball - you have to watch. Baseball is so slow and relaxing. Best sport, I agree.

**Mat Ryder:** You don't have to pay attention to it, that's how good it is. \[laughter\] You can just focus on your hot dog. Do we have other unpopular opinions? And by the way, we test these on our Twitter at @gotimefm. So we'll find out if that is in deep popular or not. Any others? We've got a couple of minutes...

**Hana Kim:** I have an opinion... The world will be better if everybody uses Linux.

**Mat Ryder:** Ooohhhh...!

**Hana Kim:** It's controversial!

**Grant Seltzer Rich man:** Oh, yeah.

**Hana Kim:** All the EPF, and all this trace - they are not available on other platforms.

**Mat Ryder:** But what about every other app in the world? But I suppose if everyone was using it... If everyone's using it, it would work too, wouldn't it? That's a fair one... Derek, do you have an unpopular opinion?

**Derek Parker:** I don't think so.

**Mat Ryder:** Do you agree with the Linux one?

**Derek Parker:** I think the world could be a better place if everybody used Linux... \[laughs\] I'm not as creative as everybody else. I don't have anything off the top of my head.

**Mat Ryder:** That's unpopular... You created Delve. You've done it. Furthermore, you've accidentally fulfilled your contractual obligations to provide an unpopular opinion for us.

**Derek Parker:** \[laughs\]

**Mat Ryder:** We are running out of time, so I really only have time to say thank you so much for doing this. It was a great conversation. I wish we could spend more time... And in fact, we'll invite you back at some point to come and do it, in another Go Time episode. Thank you very much to my guests, Hana, Grant and Derek. It's been a pleasure. Goodbye.

**Grant Seltzer Rich man:** Thank you so much.

**Hana Kim:** Thank you!

**Derek Parker:** Yeah, thank you for inviting me on.

**Break:** \[48:35\]

**Derek Parker:** I never know a joke when somebody asks me for a joke. It's one of those things, like "Tell me the dumbest joke you know." At that moment, it's like, I've never heard a joke in my entire life.

**Mat Ryder:** We just don't index the information in that way, do we?

**Derek Parker:** Right.

**Mat Ryder:** It's like, "I can't. You should have told me you were going to do that, and then \[50:46\]"

**Derek Parker:** Right. \[laughs\]

**Jerold Santo:** All my jokes are from my kids, because they ask Alexa for jokes all the time, and they're just the dumbest jokes ever. \[laughter\] Those are literally the only ones I know, because they'll ask me like six times... I have a bunch of kids, so each kid will ask me the same joke, because they'd just learned it from their brother or sister... They think I've never heard it; I've heard them all six times. \[laughter\]

What has four wheels and flies? A garbage truck. See? They're not funny, but... I knew it immediately. It's not funny.

**Mat Ryder:** What? Is it flying?

**Jerold Santo:** It has flies.

**Mat Ryder:** Oh, has flies.

**Jerold Santo:** Yeah. What has four wheels AND flies?

**Mat Ryder:** Oh, right... \[laughs\]

**Jerold Santo:** See, it is funny! It's better than you thought it was.

**Mat Ryder:** Yeah. I needed explaining, but yeah. Once it's explained, I'm all over it.

**Grant Seltzer Rich man:** Did you know that ducks can float?

**Mat Ryder:** Can they?

**Grant Seltzer Rich man:** Yeah.

**Jerold Santo:** I didn't know that.

**Mat Ryder:** What do you mean? Of course, they do. They're always on the water, aren't they?

**Grant Seltzer Rich man:** No, it's not a joke. Ducks can float.

**Jerold Santo:** Fun fact?

**Grant Seltzer Rich man:** Yeah. I think it's pretty cool.

**Jerold Santo:** Are they floating or swimming?

**Grant Seltzer Rich man:** I guess a little bit of both.
