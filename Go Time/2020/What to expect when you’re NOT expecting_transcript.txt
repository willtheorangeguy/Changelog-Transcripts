[0.00 --> 3.30]  I've done a few things with eBPF a little bit here and there.
[3.60 --> 7.58]  Actually, Delve has a trace functionality, which works somewhat similar,
[7.68 --> 12.14]  but it works at a higher level using ptrace and some of those other kind of syscalls.
[12.46 --> 16.34]  And I've thought about experimenting a little bit on Linux systems that support it,
[16.54 --> 19.54]  replacing that with like an eBPF-backed tracing system.
[19.54 --> 24.40]  So Grant, if you ever want to send a pull request, we'd love to have it.
[24.40 --> 34.52]  Yeah, I am happy to integrate it from the VS Code side with the visualization.
[36.24 --> 37.44]  I would love that.
[37.66 --> 39.88]  This is the most productive meeting I've ever been in.
[40.50 --> 42.04]  It wasn't even meant to be a meeting.
[44.24 --> 46.92]  BAM with 4Change Log is provided by Fastly.
[47.22 --> 49.10]  Learn more at Fastly.com.
[49.34 --> 51.64]  Our feature flags are powered by LaunchDarkly.
[51.90 --> 53.70]  Check them out at LaunchDarkly.com.
[53.70 --> 55.80]  And we're hosted on Linode cloud servers.
[56.14 --> 59.72]  Get $100 in hosting credit at Linode.com slash changelog.
[62.36 --> 66.22]  Whether you're working on a personal project or managing enterprise infrastructure,
[66.22 --> 70.56]  you deserve simple, affordable, and accessible cloud computing solutions
[70.56 --> 73.08]  so you can take your project to the next level.
[73.54 --> 79.96]  Simplify your life with Linode's Linux VMs to develop, deploy, and scale your applications faster and easier.
[79.96 --> 84.48]  Get started on Linode today with $100 in free credit for our listeners.
[84.48 --> 88.28]  You can find all the details at Linode.com slash changelog.
[88.40 --> 94.60]  Or if you're not at your desk, just text changelog to 474747 and get instant access to that $100.
[95.14 --> 102.72]  Linode has 11 global data centers and provides 24-7, 365 human support with no tiers or handoffs,
[102.92 --> 104.24]  regardless of your plan size.
[104.24 --> 106.94]  In addition to shared and dedicated compute instances,
[107.24 --> 112.42]  you can use that $100 credit on S3-compatible object storage, manage Kubernetes, and more.
[113.20 --> 118.18]  Visit linode.com slash changelog and click on the Create Free Account button to get started.
[118.36 --> 120.92]  Or just text changelog to 474747.
[121.44 --> 123.08]  Get started today on Linode.
[123.08 --> 134.66]  Let's do it.
[135.28 --> 136.30]  It's go time.
[137.06 --> 141.72]  Welcome to Go Time, your source for diverse discussions from around the Go community.
[142.48 --> 147.04]  We're taking you back to GopherCon this week for our second live episode from the conference.
[147.46 --> 150.56]  We hope you enjoy it, and if you do, please tell a friend about Go Time.
[151.20 --> 152.86]  Okay, let's get straight into it, shall we?
[153.08 --> 154.62]  Here we go.
[168.32 --> 175.76]  Hello there, and welcome to a very special episode of Go Time, and it's a GopherCon mashup.
[176.48 --> 181.20]  This is the lunchtime sessions for GopherCon, and also a Go Time episode.
[182.10 --> 182.74]  So welcome.
[182.74 --> 187.60]  Today, we're talking about what we do when things go wrong.
[188.14 --> 193.56]  A manager once asked me to only write code that didn't have any bugs in it.
[193.72 --> 195.88]  So that was an interesting thing.
[196.08 --> 201.28]  We're going to find out today what are bugs, and what can we do to get rid of them,
[201.38 --> 203.46]  or make sure they're never there in the first place.
[203.46 --> 211.62]  And we'll look at tools and techniques around this, too, with our expert panel, who I'm going to introduce now.
[212.08 --> 214.56]  We're joined by Hannah Kim from the Go team.
[214.70 --> 215.06]  Hello, Hannah.
[215.58 --> 215.96]  Hi.
[216.34 --> 217.34]  Welcome to Go Time.
[217.34 --> 222.40]  Yeah, I don't know if I'm an expert, but thank you very much for inviting me to Go Time.
[222.48 --> 223.62]  It's so exciting.
[223.96 --> 224.76]  Yeah, I'm so honored.
[224.88 --> 226.48]  Yes, you're more than welcome to be here.
[226.54 --> 229.98]  Sorry, I do sometimes accidentally say expert, and people don't like that.
[230.08 --> 230.92]  It sets things up.
[231.18 --> 233.14]  So don't worry.
[233.22 --> 233.62]  No pressure.
[234.42 --> 236.94]  We're also joined by Grant Seltzer-Richman.
[237.06 --> 237.60]  Hello, Grant.
[238.18 --> 238.48]  Hi.
[238.66 --> 239.38]  Thanks for having me.
[239.82 --> 240.68]  Oh, welcome, mate.
[240.72 --> 241.40]  You're very welcome.
[241.72 --> 242.80]  Are you having a good day so far?
[242.80 --> 244.10]  So far, so good.
[244.38 --> 246.64]  Go4Con is, so far, the talks have been great.
[247.24 --> 247.76]  Great.
[247.90 --> 249.34]  Well, hopefully we won't ruin it.
[250.34 --> 253.02]  And we're also joined by Derek Parker.
[253.40 --> 253.84]  Hello, Derek.
[254.58 --> 255.38]  Hello, everybody.
[256.10 --> 256.36]  Hello.
[256.74 --> 260.18]  Welcome to Go Time slash Go4Con lunchtime session.
[260.58 --> 261.06]  Thank you.
[261.30 --> 266.28]  And good evening, good morning for me on the West Coast, having my second cup of coffee.
[266.76 --> 267.12]  Great.
[267.32 --> 267.88]  Enjoy it.
[268.44 --> 272.62]  So, yes, I should say, Derek, you work at Red Hat.
[272.62 --> 275.04]  And you actually created Delve, didn't you?
[275.08 --> 275.94]  Which is a debugger.
[276.68 --> 277.48]  Yeah, that's correct.
[277.92 --> 278.12]  Okay.
[278.28 --> 282.06]  So this will be good because we'll definitely dig into that a little bit more.
[282.28 --> 283.38]  It's such a great tool.
[283.88 --> 286.02]  And, you know, it's a great way to get rid of bugs.
[286.26 --> 287.32]  But maybe we could start.
[287.76 --> 288.80]  What is a bug?
[289.10 --> 294.68]  Why was it a little bit absurd that my manager asked me to only write code that didn't have bugs in?
[295.02 --> 296.90]  I would say what is a bug?
[296.90 --> 307.60]  Like a bug is, I guess, something unexpected in your code or something incorrect, right, is what it's typically is as how I think most people typically think of it.
[307.72 --> 312.88]  It's something not only unexpected, but just incorrect, the wrong result or wrong something.
[312.88 --> 325.96]  And the absurdity, I think, of that statement comes from, you know, how could you have the premonition not to, you know, sometimes it's maybe a little bit out of your control when a bug happens.
[326.20 --> 329.44]  You know, like I would say like weird things can happen.
[329.58 --> 338.88]  Like running on a different architecture could expose a bug that you wouldn't have seen on the CPU architecture that you're using or in a different environment or with different environment variables or whatever.
[338.88 --> 350.62]  Whatever, you know, there could be so many things outside of your direct control that could expose a bug, which I think is part of the absurdity of that statement that please write code that does not have bugs.
[351.58 --> 351.92]  Yes.
[352.84 --> 353.32]  Yeah.
[353.48 --> 354.90]  So, right.
[355.00 --> 358.60]  It's just behavior that happens that we don't want to happen.
[358.72 --> 363.20]  But of course, there's no way for the compiler to know that that shouldn't happen.
[363.20 --> 372.04]  It's not like a type error where you can have a compiler look at the code and, you know, tell you or fail the compilation if things aren't right.
[372.58 --> 381.96]  It's kind of they emerge sometimes from either different ways things are interacting or just sometimes it's, you know, made a mistake.
[382.12 --> 382.82]  It happens too.
[383.44 --> 383.56]  Yeah.
[383.68 --> 385.16]  Sometimes bugs turn into features.
[385.64 --> 387.76]  So, yeah, that's yeah, absolutely.
[387.94 --> 392.28]  Especially when when I've done it, I will always pretend it was meant to be like that.
[393.20 --> 394.06]  That's a great one.
[394.70 --> 396.54]  So what do we mean by debugging then?
[396.66 --> 401.52]  Is this just any method that anything you do to get rid of bugs?
[401.52 --> 405.58]  Is that debugging or is debugging a more specific technical term?
[406.20 --> 422.24]  So I suppose when you're, you know, using a debugger doing some type of debugging, you're trying to figure out what it is that's causing this unexpected behavior that, you know, everybody has an intention when they're writing their code.
[422.24 --> 428.66]  So just like how you said that there's no way for the compiler to tell, you know, what you meant for your code to do.
[428.74 --> 430.90]  It's doing exactly what you told it to do.
[430.90 --> 443.24]  So, you know, let's say you're seeing some bugs, you know, output that's coming out of your program is not as expected or you're just seeing some errors that you didn't expect to happen.
[443.76 --> 448.38]  The act of debugging is trying to figure out what's causing that bug.
[448.56 --> 456.84]  You know, where in your code did you have some logic that isn't what you intended it to be and trying to figure that out so that you could then fix it.
[456.84 --> 470.28]  Yeah. And when you come to debugging then with techniques and tools, do you have a particular favorite of what's your sort of go-to, what's the first thing you do when you've noticed something's wrong?
[470.68 --> 471.80]  Does it depend or?
[471.80 --> 489.88]  So I will say that I think there's a sort of a half joke within all of the tech industry that, you know, adding print statements to your code is wrong or like an amateur approach.
[489.88 --> 501.62]  But to be honest, if your program compiles particularly quickly, there's no reason that adding a print statement should be looked at as, you know, like a dirty way of doing it.
[501.86 --> 506.42]  So, you know, the feedback loop, you know, when you're debugging, you want to have a quick feedback loop.
[506.56 --> 515.42]  So if it's a simple enough program where you could just add a print statement at, you know, a certain point that's printing out the contents of variables, I don't think there's anything wrong with that.
[515.42 --> 521.34]  Because it's an intuitive interface, you know, that like, I want to know what happens at this point in the program.
[521.74 --> 532.56]  If it's a particularly complex program or, you know, the compile time is long and you need a faster feedback loop or something like that, that's when I would typically use a debugger or some type of tracing tool.
[533.42 --> 535.44]  But nothing wrong with print statements.
[535.44 --> 547.84]  Yeah, I think that's a great, I'm really pleased you said that because I've met junior developers who feel like that's, they're just, they don't know how to use a debugger or they don't know what they're doing and they just put prints out.
[548.00 --> 550.34]  But it is completely legitimate.
[550.78 --> 553.86]  In fact, it tends to be my go-to thing is doing that.
[554.20 --> 557.18]  And there's a particular verb that's very useful in Go.
[557.18 --> 563.44]  If you use the FMPT package, you can do like percent plus V and then give it any type.
[563.60 --> 570.72]  And it does a really good job of describing that type, even if it's a complicated kind of struct with nested data and all sorts.
[571.22 --> 573.86]  And you see the field names too, which is quite useful.
[574.34 --> 580.96]  Are there any other favorite techniques like that, the sort of simple, debuggable things?
[581.66 --> 582.78]  Printing's a great one.
[582.78 --> 592.62]  Certainly, you know, I'm sure both Derek and Hannah can talk about using Delve, but I certainly use Delve, you know, a full-fledged debugger.
[592.94 --> 593.14]  Right.
[593.28 --> 596.02]  So Delve's a kind of a different beast, really.
[596.20 --> 600.08]  And the other one that we should talk about before we get on to Delve is test code.
[600.16 --> 603.42]  Because actually test code is a great way to debug your code.
[603.42 --> 615.58]  One trick that I find works really well is if somebody identifies there's a bug, if you ask them to write a failing test, if they can do that, you know, that is a great way.
[615.68 --> 616.80]  You remove all ambiguity.
[617.32 --> 619.64]  You're looking, you know, you speak in the same language.
[619.78 --> 620.64]  You look at the code.
[621.10 --> 625.46]  And if it's a failed test, you know, you've proven that there's a bug there.
[625.46 --> 629.24]  And sometimes the test is wrong and some of the assumptions are wrong.
[629.34 --> 630.56]  And that's one thing.
[631.04 --> 633.64]  But usually it does kind of highlight the bug.
[633.70 --> 640.46]  And then, of course, once it's fixed, you can put that test into your test suite and you kind of never get that same bug again.
[641.22 --> 647.36]  Hannah, you work on the Go team and you're working on the VS Code plugin for Go, right?
[647.36 --> 649.92]  So tell us about that then.
[650.14 --> 662.22]  That plugs into the IDE, integrates, so turns visual code from being what might be just a sort of basic text editor and adds some kind of Go intelligence to it.
[662.56 --> 663.16]  Is that fair?
[663.72 --> 664.54]  Oh, yeah.
[664.70 --> 667.04]  And also it has a debug integration too.
[667.04 --> 678.78]  And also all kind of facilities that actually helps users to write a good test, like all kind of templating and autocomplete and that kind of features.
[679.46 --> 681.08]  And also like a test command.
[681.32 --> 685.36]  So with just one click, you can write a test on your package.
[685.60 --> 685.72]  Yeah.
[686.26 --> 687.74]  So, yeah.
[687.74 --> 697.14]  But for debugging purpose, I think my go-to is still like a print app and log or that kind of thing.
[697.64 --> 698.30]  So, yeah.
[698.90 --> 699.12]  Yeah.
[699.30 --> 701.64]  So maybe it's time then just to talk about Delve.
[702.26 --> 707.18]  Maybe we could start by just for anybody that hasn't used a debugger before.
[707.76 --> 709.38]  Maybe, Derek, this is one for you.
[709.68 --> 711.84]  What is a debugger and what's it doing?
[711.92 --> 712.56]  How does it work?
[712.66 --> 713.34]  How do you use it?
[713.34 --> 713.86]  Yeah.
[713.86 --> 723.08]  So I actually heard like a really good explanation yesterday from Jason, who I was co-instructing our workshop with.
[723.14 --> 724.50]  The format or is it a human?
[725.38 --> 727.00]  You're not talking about the data format.
[727.38 --> 727.52]  No.
[728.96 --> 729.58]  It's a human.
[730.14 --> 730.56]  Got it.
[732.12 --> 732.34]  Okay.
[732.80 --> 736.32]  That's a half joke, like what Grant did earlier.
[736.92 --> 737.74]  It's just not funny.
[738.70 --> 739.08]  Go on.
[739.16 --> 739.32]  Sorry.
[739.32 --> 745.44]  I like the way that Jason kind of explained like what a tool like a debugger is.
[745.58 --> 751.72]  So it's actually kind of like, like I think that the name debugger is a little bit of a misnomer.
[751.98 --> 755.38]  Like the tool itself doesn't actually fix the bug for you.
[755.64 --> 760.30]  It's just a tool that you can use to understand your program, right?
[760.30 --> 764.60]  It's just like a, it's a way to just understand what your program is doing.
[764.74 --> 768.14]  And then once you figure out what's going wrong, you can fix the bug.
[768.54 --> 770.80]  It doesn't fix the bug for you, but who's fault's that?
[770.92 --> 773.94]  You're the creator and co-maintainer of Delve.
[774.06 --> 776.08]  So really you've only got yourself to blame there.
[776.32 --> 777.56]  In the next release, you know.
[779.40 --> 780.94]  But it's actually an interesting point.
[781.08 --> 782.42]  It can't be done automatically.
[782.54 --> 785.52]  Otherwise, of course, the tooling would be doing it for you.
[785.52 --> 791.74]  You know, you have to sort of tell it what correct is and you've already told it what incorrect is, right?
[791.94 --> 797.38]  Yeah, I think it's approaching like any kind of debugging situation with the mindset of like,
[797.88 --> 801.02]  how can I gain insight into what's actually happening?
[801.02 --> 807.78]  And how can I do that in a way that will quickly allow me to figure out what's going wrong so that I can fix it?
[807.78 --> 814.90]  And I think kind of like what Grant said earlier, whatever gives you the fastest feedback loop, that's kind of what you should pursue.
[815.08 --> 821.68]  So whether that's, you know, I do print line debugging all the time as well, especially when like working on Delve,
[821.70 --> 824.42]  it's hard to debug a debugger with a debugger sometimes.
[824.42 --> 830.60]  So doing like print line debugging in those kind of situations and kind of whatever gives you the quickest feedback loop,
[830.66 --> 834.34]  I think is the best tool to reach for in that situation.
[834.34 --> 843.18]  Hmm. Okay. So if printing the results isn't working for you, then Delve allows you to kind of set a break point, doesn't it?
[843.34 --> 847.50]  And what happens then in the program, the program stops at that point?
[848.14 --> 853.00]  Yeah, exactly. So with a tool like Delve, like a traditional like source level debugger,
[853.14 --> 856.60]  you're interacting with your program like in real time.
[856.60 --> 863.62]  And that's kind of what's fun and interesting about using a debugger is you have the ability to stop what's happening,
[863.62 --> 866.96]  inspect state, even change state if you want, continue.
[867.64 --> 873.16]  So yeah, like for example, when you start up a new debug session and you set a break point, you continue to it.
[873.20 --> 878.40]  You're telling the program, I want to stop at this specific location and just check out what's going on.
[878.72 --> 880.60]  You know, see how I got here.
[880.70 --> 882.16]  You can look at the stack trace.
[882.26 --> 883.62]  You can see the value of variables.
[883.62 --> 888.54]  And if you want to experiment a little bit, debuggers also can let you experiment.
[888.80 --> 894.68]  So you can say, for example, like change the value of a variable and see if that gives you the result that you wanted.
[894.84 --> 901.64]  So it gives you a little bit more of like real time interaction, like getting back to that quicker feedback loop,
[901.70 --> 907.00]  you know, without like changing a variable in the code, recompiling it, rerunning it, trying to hit that bug again,
[907.00 --> 912.06]  or seeing if you don't, you can kind of do some interactive stuff within like a debug session.
[912.60 --> 915.26]  And you can step then, can't you, through the instructions.
[915.26 --> 921.54]  So you can advance the program step by step slowly and keep an eye on things just so you understand what's happening.
[921.64 --> 926.74]  It sort of like puts it into slow motion and lets you do that carefully, right?
[927.36 --> 927.60]  Yeah.
[927.78 --> 928.44]  Yeah, absolutely.
[928.60 --> 928.86]  Exactly.
[928.86 --> 930.70]  And how does that actually work?
[930.78 --> 931.36]  What's going on?
[931.44 --> 936.68]  Do you have to build the binary specifically with that debug information added to it?
[936.76 --> 938.08]  Or can you just debug anything?
[938.98 --> 939.16]  Yeah.
[939.30 --> 943.32]  So all binaries include information called, it's called dwarf information.
[943.76 --> 950.00]  And that's like a standard format of debug information.
[950.10 --> 957.78]  Basically, it tells tools like Delve how to find variables, how to unwind the stack, how to do all kinds of things.
[957.78 --> 961.28]  So Go, by default, will build that into all binaries.
[961.58 --> 963.74]  You have to opt out of it specifically.
[964.38 --> 969.20]  And the only reason why you would opt out of it would be maybe you really, really care about binary size.
[969.30 --> 975.24]  And you want to get out every last bit that you can to shrink your binary as much as possible.
[975.44 --> 978.00]  But by default, that information is going to be in there.
[978.00 --> 992.82]  The only other thing that like Delve does by default, and I would recommend folks do if they're going to try to debug their Go applications, processes, whatever, is Go also by default will put in optimizations.
[992.82 --> 999.42]  So like if you're familiar with like GCC or some other compiler, you have to explicitly tell it what level of optimization you want.
[999.54 --> 1003.32]  And you kind of have to opt into some of the more extreme optimizations.
[1003.90 --> 1005.10]  But Go does that by default.
[1005.58 --> 1008.86]  And that's great for when you're building a production binary, you want to ship it off.
[1008.92 --> 1010.72]  It's going to be fast and performant and all that.
[1010.72 --> 1017.58]  But it could hamper debugging a little bit because of like inlining functions can get weird sometimes.
[1017.74 --> 1018.94]  Delve handles it really well now.
[1019.08 --> 1026.02]  And the Go compiler has gotten a lot better at providing information for telling debuggers how to handle that.
[1026.14 --> 1032.22]  But there's still certain weirdness there that you can run into when trying to debug and optimize binary.
[1032.50 --> 1035.66]  So that's the only caveat that I would like explicitly mention.
[1036.94 --> 1037.74]  That's interesting.
[1037.74 --> 1045.76]  And so, Hannah, when you talk about the VS Code plugin and it has debugger support, does it support Delve?
[1046.90 --> 1049.44]  Well, actually, Delve is behind the scene.
[1049.94 --> 1054.68]  Actually, like other editors like Golan, they also use Delve.
[1055.10 --> 1062.20]  So basically this idea, like when user requests to debug their code, it actually formulates all this Delve command
[1062.20 --> 1066.38]  and then invoke Delve and ask Delve to answer the question.
[1066.38 --> 1074.12]  And then most of modern IDs, they have a kind of like all this local variable, global variable or step trace.
[1074.44 --> 1076.24]  So it just asks Delve.
[1076.48 --> 1081.84]  And then all the information are visible through all this UI.
[1082.14 --> 1089.04]  And then users can actually step through all this, yeah, step through the program using the UI.
[1089.04 --> 1092.84]  And again, we ask Delve to do all this job.
[1093.26 --> 1100.92]  So IDEA's work is kind of like provide the best experience, user experience, and visualize the data coming in and coming out.
[1101.32 --> 1107.22]  Like, I mean, all the information between this Delve and the front end.
[1107.22 --> 1110.04]  So that's really nice then.
[1110.22 --> 1119.58]  So you don't have to learn these complicated commands and you don't have to know about the Dwarf data or anything like that because it's integrated.
[1119.78 --> 1120.80]  Yeah, ideally.
[1121.54 --> 1121.68]  Yeah.
[1122.06 --> 1127.82]  Because it's integrated, you get to just do it right in your code, the same place where you're writing the code.
[1127.88 --> 1128.72]  So that's really cool.
[1128.82 --> 1132.02]  How do you actually do that then in VS Code?
[1132.46 --> 1133.54]  How do you set a breakpoint?
[1133.54 --> 1138.16]  So actually what the nice thing about Delve is Delve has the API.
[1138.66 --> 1145.16]  So like all this method and instruction, they are actually, they can be invoked through the RPC.
[1145.94 --> 1150.32]  And so we just launched the headless Delve server.
[1150.86 --> 1158.22]  And then from the VS Code, we also use, so from the VS Code, we just invoke this RPC.
[1158.22 --> 1166.82]  And there is some recent movement about the debug adapter protocol that is a kind of like a standardized all this.
[1167.14 --> 1173.28]  So not Delve is Go debugger, but there is GDB, there is LLDB, and there is a JavaScript debugger.
[1173.44 --> 1175.70]  And like there are all kinds of debuggers, right?
[1175.76 --> 1177.32]  And then we have VS Code.
[1177.32 --> 1185.90]  So VS Code team, yeah, they try to standardize the interaction between debugger, just general debugger and editor.
[1186.40 --> 1188.48]  So it's called the debug adapter protocol.
[1189.52 --> 1194.94]  And like VS Code Go extension speaks Delve adapter protocol.
[1195.22 --> 1201.70]  And there is a small tiny Delve adapter, a debug adapter that actually talks Delve RPC.
[1201.70 --> 1208.52]  So it's a little bit complicated, but we try to minimize, like simplify this, like communication path.
[1208.68 --> 1215.54]  So that next version, I hope like the communication is more efficient and like, yeah.
[1216.06 --> 1219.20]  So yeah, that is the general direction we are heading at.
[1219.58 --> 1220.68]  That's really cool then.
[1220.76 --> 1221.20]  That's nice.
[1221.30 --> 1225.84]  It's nice because we don't, as users of this, we don't sort of have to worry about that, right?
[1225.84 --> 1229.46]  That's like something that happens behind the scenes.
[1229.66 --> 1232.54]  We get to just use the VS Code interface.
[1233.42 --> 1234.76]  So that, yeah, that's really great.
[1245.12 --> 1248.84]  How much time does your team spend building and maintaining internal tooling?
[1249.12 --> 1253.14]  I'm talking about those behind the scenes apps, the ones no one else sees.
[1253.14 --> 1259.62]  The S3 uploader you built last year for the marketing team, that quick Firebase admin panel that lets you monitor key KPIs.
[1259.92 --> 1264.90]  Maybe even the tool your data science team hacked together so they can provide custom ad spend analytics.
[1265.48 --> 1267.42]  Now, these are tools you need so you build them.
[1267.62 --> 1268.56]  And that makes sense.
[1269.10 --> 1275.62]  But the question is, could you have built them in less time, with less effort, and less overhead and maintenance required?
[1275.94 --> 1278.12]  And the answer to that question is, yes.
[1278.56 --> 1279.86]  That's where Retool comes in.
[1279.86 --> 1283.72]  Rohan Chopra, engineering director at DoorDash, has this to say about Retool.
[1284.10 --> 1284.34]  Quote,
[1284.34 --> 1292.58]  The tools we've been able to quickly build with Retool have allowed us to empower and scale our local operators, all while reducing the dependency on engineering.
[1293.02 --> 1293.36]  End quote.
[1293.84 --> 1300.10]  Now, the internal tooling process at DoorDash was bogged down with manual data entry, missed handoffs, and long turnaround times.
[1300.10 --> 1309.64]  And after integrating Retool, DoorDash was able to cut the engineering time required to build tools by a factor of 10x and eliminate the error-prone manual processes that plague their workflows.
[1310.04 --> 1314.14]  They were able to empower backend engineers who wouldn't otherwise be able to build frontends from scratch.
[1314.54 --> 1319.52]  And these engineers were able to build fully functional apps in Retool in hours, not days or weeks.
[1319.52 --> 1323.68]  Your next step is to try it free at retool.com slash changelog.
[1323.84 --> 1326.28]  Again, retool.com slash changelog.
[1326.28 --> 1350.96]  I'm interested.
[1351.60 --> 1354.72]  Grant, your talk is, is your talk on Friday?
[1354.72 --> 1356.28]  Uh, yes.
[1356.48 --> 1358.60]  Friday, I think something around four o'clock.
[1359.06 --> 1359.30]  Mm-hmm.
[1359.72 --> 1362.00]  That's meaningless to me because I'm in the different time zone.
[1362.30 --> 1363.26]  Oh, Eastern time.
[1363.56 --> 1364.06]  Yeah, okay.
[1364.46 --> 1366.24]  I think we should get rid of time zones, by the way.
[1366.28 --> 1367.00]  I think that was a bug.
[1367.34 --> 1369.34]  I think there's a bug in that, to be honest.
[1369.76 --> 1371.80]  We should all just follow New York time.
[1372.22 --> 1372.76]  If you like.
[1372.98 --> 1376.16]  I mean, don't, you know, jump to an assumption there.
[1376.48 --> 1380.82]  I mean, Greenwich, I live near Greenwich, which is actually where they invented time, I think.
[1381.20 --> 1382.28]  So, do you know what I mean?
[1382.84 --> 1384.24]  I live near Greenwich Village.
[1384.72 --> 1384.92]  Yeah.
[1385.88 --> 1386.24]  Okay.
[1388.48 --> 1390.44]  I wasn't going to say there's a line and you've crossed it.
[1390.64 --> 1394.72]  I was going to say in Greenwich, there's a line that's like the Meridian zero line.
[1394.72 --> 1394.92]  Yeah.
[1394.98 --> 1396.48]  You can sort of go and cross it.
[1396.48 --> 1396.90]  I gotcha.
[1397.40 --> 1398.14]  Yeah, it's all right.
[1398.14 --> 1400.86]  So, yeah.
[1400.90 --> 1403.56]  I was going to ask, what is your talk about on Friday?
[1403.56 --> 1407.50]  So, my talk is about tracing Go programs with eBPF.
[1408.30 --> 1416.72]  So, eBPF has been talked about a lot at various different conferences for the past two or three years.
[1416.84 --> 1417.96]  It's been gaining a lot of momentum.
[1417.96 --> 1422.68]  And it's a feature of the Linux kernel.
[1422.68 --> 1424.24]  So, it's certainly Linux specific.
[1424.24 --> 1432.02]  But what it allows you to do is add ad hoc, add logic to the Linux kernel.
[1432.36 --> 1433.56]  And I know that's very abstract.
[1433.56 --> 1447.44]  But the way that it's often put, Brendan Gregg, a leader in the eBPF space, likes to put it as eBPF does to the Linux kernel what JavaScript does to HTML.
[1447.44 --> 1451.40]  So, you can attach eBPF programs.
[1451.54 --> 1460.32]  You could think of them as scripts and attach them to various hooks, such as to network sockets every time a packet comes in and have some logic.
[1460.64 --> 1466.72]  Or to kernel probes, which, you know, every time source code is executed within the Linux kernel itself.
[1467.40 --> 1473.60]  And in particular, what my talk is about is attaching eBPF programs to something called uProbes.
[1473.60 --> 1480.88]  And uProbes attach to what essentially is like source code symbols.
[1481.22 --> 1492.32]  So, if you have a Go program that has a function called test function, you can attach a uProbe to that and attach an eBPF program to that uProbe.
[1492.32 --> 1508.76]  So, that every time a process executes that function, so if you run that program and it's, you know, a running service or whatever else, you could have essentially a script respond to that function every time it's called.
[1509.04 --> 1510.98]  So, you could print out what the arguments are.
[1511.12 --> 1513.92]  You could have some logic for inspecting another area of memory.
[1513.92 --> 1522.40]  You know, and it's useful for debugging, for monitoring, potentially for fuzzing or fault injection as well.
[1523.20 --> 1528.92]  So, does the original function still run and you're just sort of intercepting it or do you replace it?
[1529.62 --> 1530.74]  That's a really good question.
[1530.86 --> 1532.24]  So, it does still run.
[1532.48 --> 1535.82]  It doesn't stop the program from running at all.
[1535.96 --> 1536.98]  It doesn't affect the process.
[1537.16 --> 1542.70]  It runs in its own virtual machine inside the Linux kernel, actually.
[1542.70 --> 1559.04]  So, the difference between, or, you know, I guess there's a lot of difference in terms of the underlying technology, but the advantage to eBPF, which I guess could also be seen as a disadvantage compared to buggers, is that it's not stopping the program.
[1559.36 --> 1562.10]  It's not attaching to the process.
[1562.64 --> 1570.84]  You can have a running program that is completely unaware of the fact that it's, you know, being inspected via eBPF.
[1570.84 --> 1575.10]  Because you're doing it down at the low levels of the operating system, I guess.
[1575.64 --> 1576.02]  Exactly.
[1576.80 --> 1581.84]  So, what use cases are there for that then, from a kind of debugging practical standpoint?
[1582.12 --> 1583.28]  What sorts of things can you do?
[1583.76 --> 1586.10]  So, I have a project I'll shamelessly plug in.
[1586.16 --> 1587.24]  I'm almost at 100 stars.
[1587.44 --> 1588.42]  Go star it.
[1588.60 --> 1589.54]  It's called Weaver.
[1589.92 --> 1592.98]  It's on my GitHub, GrantSeltzer slash Weaver.
[1592.98 --> 1598.48]  And what I'm trying to do is have strace-like functionality.
[1599.06 --> 1604.38]  Strace is another tracing tool that you run a program, it'll print out every time a system call is executed.
[1604.80 --> 1608.68]  Where I'm trying to have a functionality like that for Go programs.
[1608.68 --> 1614.56]  Well, where you run a Go program, and every time any function inside of that is called.
[1614.88 --> 1622.52]  So, you know, all of your functions in all of your packages, every time they're called, it will print out a line with,
[1622.64 --> 1627.12]  it was called at this timestamp, and the arguments passed had these values.
[1627.52 --> 1629.98]  And its return was X, Y, or Z.
[1629.98 --> 1638.88]  So, the application there is, you know, for debugging purposes, let's say you want to know why you're getting some garbled output.
[1639.30 --> 1647.42]  And you want to know at what point down the function call stack, a function was getting some weird output.
[1647.64 --> 1655.68]  And you see somewhere along the line, like, this function for, like, printf, or, like, you know, a wrapper around printf is getting really weird output.
[1655.68 --> 1659.28]  So, then you might want to start inspecting at the function that called that one.
[1659.98 --> 1666.98]  It's also useful for, you know, not that I'm saying that this is the greatest idea.
[1667.48 --> 1670.34]  It's still a developing ecosystem.
[1670.34 --> 1680.92]  But you could attach these to services running in production because it has such a minimal effect on the performance of the service.
[1680.96 --> 1683.18]  And you could attach it to running programs as well.
[1683.98 --> 1684.50]  Hmm.
[1684.94 --> 1686.34]  That is really interesting.
[1686.34 --> 1689.04]  I mean, can you interact?
[1689.04 --> 1695.22]  Can you, like, I guess you can't change things in these little eBPF programs, can you?
[1695.78 --> 1700.02]  So, I have a little example of how you can, actually, in my talk.
[1700.40 --> 1704.52]  There is a really good talk that was given at some security conference.
[1704.80 --> 1705.94]  I can link it later.
[1706.04 --> 1709.90]  But of how you can write essentially malicious code with eBPF.
[1709.90 --> 1715.78]  But even for non-malicious purposes, you could actually write to memory from eBPF.
[1715.84 --> 1719.72]  So, you can change the value of parameters, which I do in my talk.
[1720.26 --> 1720.48]  Wow.
[1720.88 --> 1723.56]  And would you recommend that or not sure yet?
[1723.96 --> 1734.90]  I think it has its use cases if you are trying to do, let's say, something like fault injection, where, you know, you have processes that are communicating with one another.
[1734.90 --> 1738.12]  And you have a function that is pulling in from another endpoint.
[1738.76 --> 1750.72]  And if you don't want to have that external dependency, you could have an eBPF program that writes some garbled data to, you know, to a particular function and, you know, see how your program reacts to it.
[1750.72 --> 1768.88]  And you could also, if you have a compiled and running service and you want to see if, you know, a particular fix to your source code will fix the issue, you can write, you know, insert a small eBPF program that writes correct data, you know, if it was getting incorrect data.
[1769.02 --> 1774.08]  And if that fixes your whole issue, you know, that's, you know, the symptom of it.
[1774.14 --> 1776.28]  But I guess it depends on a case-by-case basis.
[1776.46 --> 1778.04]  Certainly not in production, I'll say that.
[1778.16 --> 1780.60]  And so these scripts, what language are they?
[1780.72 --> 1782.26]  Does it have its own little language?
[1782.40 --> 1784.58]  Is it something that would be familiar to us?
[1784.90 --> 1786.28]  So it would be familiar to you.
[1786.38 --> 1787.38]  It's essentially C.
[1787.60 --> 1789.16]  It's a subset of C.
[1789.32 --> 1792.42]  There are some restrictions to it, but it essentially looks like C.
[1792.48 --> 1794.86]  I guess the language could be called BPF.
[1794.86 --> 1800.14]  And it's, you know, there's a verifier within the Linux kernel when you try and load the bytecode.
[1800.30 --> 1802.76]  It's an LLVM-backed compiler.
[1804.10 --> 1805.60]  It's a really interesting thing.
[1805.60 --> 1807.42]  Do you think there's work?
[1807.54 --> 1811.88]  What's sort of next before we can start using that kind of technique?
[1812.06 --> 1815.22]  Is it because it feels like it's quite a new thing on the scene?
[1815.30 --> 1815.92]  Has it been around?
[1816.26 --> 1817.00]  Where did it come from?
[1817.00 --> 1824.62]  So the original technology of it, I think, was, I don't even want to guess, like early 2000s.
[1824.68 --> 1828.18]  It used to be strictly for network packet processing.
[1828.86 --> 1833.82]  But I would say it's been within the past two years or so that the ecosystem has really developed.
[1833.98 --> 1835.66]  There's a group of startups.
[1835.82 --> 1840.98]  I know Facebook does a lot of EBPF stuff, and they've contributed to the community quite a bit.
[1840.98 --> 1847.64]  I would say there's no better time to start doing it than right now because the ecosystem definitely is developing.
[1847.82 --> 1862.42]  But there's a really strong community of people who, you know, really help one another, you know, try and figure this all out and define what good EBPF code looks like and what the ecosystem related to how it's related to Go looks like.
[1863.30 --> 1867.66]  So I think it's best to get in at the ground floor, so to speak.
[1868.66 --> 1869.66]  Very interesting.
[1869.66 --> 1871.26]  Yeah, it's definitely something to play with.
[1871.34 --> 1884.56]  It sounds like one of those things that can be extremely powerful, but also a bit like in C and C++, you can do like operator overloading and things, which is, if used correctly, it can be great.
[1885.08 --> 1893.76]  But as soon as it's abused, you end up not knowing what an add means in the code, you know, what a plus symbol is doing to things.
[1894.44 --> 1894.78]  Fair enough.
[1894.92 --> 1898.38]  There's probably one of those things you would end up using it very cautiously, I suppose.
[1898.38 --> 1899.90]  Yeah, that's fair.
[1900.04 --> 1910.86]  I will say that the goal of my talk is to show how accessible the technology is and you don't have to have any expertise in the low levels of Linux or even of Go for that matter.
[1910.98 --> 1919.46]  Like you could really start playing around with it and it can make a whole new class of problems much more accessible to so many more people.
[1919.46 --> 1921.84]  Have you ever used it, Derek?
[1922.12 --> 1922.86]  Are you aware of it?
[1924.12 --> 1929.34]  Yeah, I've done a few things with EBPF a little bit here and there.
[1929.34 --> 1938.74]  Actually, Delve has a trace functionality, which works somewhat similar, but it works at a higher level using ptrace and some of those other kind of syscalls.
[1939.56 --> 1947.92]  And I've thought about experimenting a little bit, replacing on Linux systems that support it, replacing that with like an EBPF backed tracing system.
[1947.92 --> 1953.00]  So Grant, if you ever want to send a pull request, we'd love to have it.
[1954.26 --> 1955.28]  Yeah, I would.
[1955.52 --> 1963.10]  Yeah, I am happy to integrate it from the VS Code side with the visualization.
[1964.74 --> 1966.16]  I would love that.
[1966.40 --> 1968.62]  This is the most productive meeting I've ever been in.
[1969.10 --> 1970.76]  It wasn't even meant to be a meeting.
[1970.76 --> 1985.20]  Yeah, and the benefit like of what Grant was talking about doing it, like the EBPF route versus, so Go does it kind of at a higher level using like ptrace syscalls and various other like syscalls on different platforms like Windows and stuff like that.
[1985.58 --> 1993.78]  But the fundamental problem of why it's like slower than the approach that Grant described with EBPF is like EBPF stays all within the kernel.
[1993.78 --> 1998.90]  So there's no context switching from kernel space to user space back to kernel space back to user space.
[1998.90 --> 2001.44]  That context switch can get expensive.
[2002.08 --> 2012.38]  So when Delve traces in kind of a more portable way, it traces in such a way where there's, you know, you do switch from the kernel to user space back to the kernel back to the user space.
[2012.68 --> 2019.22]  And typically, you don't really see like that much of a slowdown if you're just tracing a program locally or something like that.
[2019.22 --> 2026.92]  But certainly there is a performance hit there that could be like alleviated by switching to EBPF where appropriate, where possible.
[2026.92 --> 2031.18]  But usually people are debugging not in production.
[2031.64 --> 2032.80]  But I mean, does it change?
[2032.88 --> 2033.68]  Does that change at all?
[2033.76 --> 2037.46]  Or is this, we're not going to, we're still going to keep doing how we're doing it?
[2037.82 --> 2038.06]  Do you know what I mean?
[2038.66 --> 2045.98]  I think with EBPF, you could make the case that it's easier and a little bit safer and more rational to do in a production environment.
[2045.98 --> 2052.86]  I would say I wouldn't recommend doing like a, like a delve trace on a production system unless you really, really had to.
[2053.28 --> 2058.88]  For example, yeah, there's, you're just going to run into some performance penalties there is really kind of the biggest issue.
[2058.88 --> 2072.20]  What up, Gophers?
[2072.48 --> 2074.48]  Jared Santo here, your humble producer.
[2075.16 --> 2078.28]  I want to take a quick moment to tell you about Changelog++.
[2078.68 --> 2084.88]  It's our membership program where you can directly support GoTime and all the podcasts we create here at Changelog.
[2084.88 --> 2090.02]  Ditch the ads, get closer to the metal and enjoy supporting GoTime into the future.
[2090.60 --> 2093.46]  Learn more at changelog.com slash plus plus.
[2093.78 --> 2096.56]  Once again, that's changelog.com slash plus plus.
[2096.74 --> 2097.40]  Check it out.
[2097.80 --> 2098.90]  We'd love to have you with us.
[2098.90 --> 2119.56]  Hannah, you mentioned earlier that Delve has an API, an RPC API.
[2119.96 --> 2120.60]  What is that?
[2120.66 --> 2121.54]  What does that look like?
[2121.70 --> 2122.90]  How do you consume that?
[2122.96 --> 2125.88]  How does VS Code, is it an HTTP API?
[2126.16 --> 2127.58]  Are there, is it protobuf?
[2127.58 --> 2128.86]  How does it actually work?
[2129.78 --> 2131.46]  Yeah, so Derek is here.
[2131.96 --> 2135.02]  So it's a little bit weird to answer the question.
[2135.28 --> 2139.76]  So I think, yeah, that is a JSON RPC, like one, right?
[2139.88 --> 2144.48]  So it's just like the JSON streaming between client and server.
[2144.74 --> 2145.72]  Like it's a simple one.
[2146.24 --> 2151.18]  And yeah, that is a kind of like another JSON RPC 2 based protocol.
[2151.18 --> 2154.12]  So just do JSON message exchange.
[2154.56 --> 2158.36]  So you start the program, start the debugger, Delve.
[2158.82 --> 2162.04]  And does it then return back some endpoint for you to hit?
[2162.38 --> 2163.70]  Or how does it work?
[2163.70 --> 2163.84]  Yeah.
[2163.96 --> 2170.28]  So like, yeah, just to connect it to the socket, the network socket, like the port and then create a socket.
[2170.68 --> 2173.62]  And yeah, communication over the socket.
[2173.62 --> 2174.02]  Yeah.
[2174.82 --> 2175.50]  Very cool.
[2176.26 --> 2186.50]  Well, you see, I asked that because that's quite interesting because I think there's a whole space of tooling, particularly like static analysis or even other sort of runtime tools like debuggers.
[2186.50 --> 2194.16]  And there's sort of a lot of choice for how to build those things so that they can be easily consumed by plugins and things.
[2194.32 --> 2198.26]  So that's quite interesting to always is quite interesting to hear about that.
[2198.90 --> 2203.74]  When did the VS Code plugin officially get taken up by the Go team?
[2203.84 --> 2206.06]  Because it used to just be something else before, didn't it?
[2206.86 --> 2207.08]  Yeah.
[2207.20 --> 2211.00]  So it was originally owned by Microsoft, Microsoft team.
[2211.00 --> 2218.72]  And I think VS Code Go was one of the earliest language supporting plugins VS Code team offered.
[2219.26 --> 2223.34]  And then for a while, like it was in the maintenance mode.
[2223.56 --> 2229.24]  And this year, actually, we got the responsibility to maintain.
[2229.56 --> 2235.64]  So I think there was a blog post from blog.golang.org about this transition.
[2235.64 --> 2242.18]  So now like the tool team inside of like Go team in Google.
[2242.44 --> 2242.60]  Yeah.
[2242.70 --> 2244.34]  We are maintaining this plugin.
[2245.00 --> 2247.24]  How many is on the Go tool team?
[2247.66 --> 2248.26]  Tool team.
[2248.68 --> 2248.92]  Hmm.
[2249.36 --> 2251.30]  I remember when there was just the Go team.
[2251.74 --> 2253.90]  And now there's like there's a security team.
[2254.00 --> 2255.30]  There's a team for tools.
[2256.06 --> 2256.28]  Right.
[2256.36 --> 2257.14]  It's really growing.
[2257.68 --> 2258.02]  Yeah.
[2258.24 --> 2258.94]  So, yeah.
[2259.28 --> 2261.60]  So, yeah, there is a high demand.
[2261.60 --> 2264.88]  So, yeah, we need a lot of work to do.
[2265.60 --> 2269.86]  And so there is like currently the Go Place team.
[2270.10 --> 2273.44]  That is like Go Place is one of the biggest project.
[2273.82 --> 2275.24]  I don't know if you heard about it.
[2275.48 --> 2275.82]  Yes.
[2275.84 --> 2281.42]  That is the language like service implementation for the Go language.
[2282.02 --> 2287.00]  And, yeah, the Go tool team is basically provide the best developer experience,
[2287.00 --> 2290.92]  including the debug support or language intelligence support.
[2291.38 --> 2296.20]  And, yeah, so VS Code Go is kind of like one of the projects.
[2296.60 --> 2301.34]  And currently, like we are based on the New York and like a handful number of like a few
[2301.34 --> 2307.10]  of us are working on various aspects of this developer experience improvement.
[2307.10 --> 2307.50]  Yeah.
[2308.60 --> 2313.08]  Well, we all appreciate all the work, of course, because it's very nice for us to just we just
[2313.08 --> 2315.80]  get to use it and it hopefully makes our lives easier.
[2316.00 --> 2318.60]  So I do like to thank people that have contributed.
[2318.72 --> 2319.86]  This goes for everyone on this call.
[2320.38 --> 2325.38]  Can you give us any spoilers about things that you're working on now that we might see soon?
[2326.06 --> 2326.90]  Won't tell anyone.
[2328.66 --> 2329.06]  I will.
[2330.34 --> 2332.48]  That is technically, that is legally watertight.
[2334.70 --> 2336.24]  So what's coming next?
[2337.10 --> 2337.52]  Yeah.
[2337.78 --> 2349.56]  So, yeah, we are currently like working really hard to use GoPlace as a default Go intelligent,
[2349.92 --> 2352.54]  yeah, Go language service.
[2353.06 --> 2358.98]  And also we are now currently working on, like, I think I talked about it, right?
[2358.98 --> 2364.64]  The debug adapter plugin, adapter protocol, so that we can simplify and then provide like
[2364.64 --> 2370.42]  a more performant, like a debugging experience from the VS Code users.
[2371.12 --> 2371.80]  So, yeah.
[2372.06 --> 2376.58]  So that is, yeah, they are the two big main projects I'm currently working on.
[2377.26 --> 2378.04]  Oh, great.
[2378.14 --> 2378.82]  Yeah, sounds good.
[2379.02 --> 2380.74]  And what about for Delve?
[2380.74 --> 2386.18]  I mean, is that pretty much kind of done or is there a roadmap there?
[2386.82 --> 2388.94]  I'm interested in what's coming next for that too.
[2390.50 --> 2394.14]  Yeah, it's one of those things where it's still constantly evolving.
[2394.14 --> 2396.72]  We have a few kind of big things planned.
[2396.96 --> 2399.96]  We always work to keep up to date with the latest Go release.
[2400.16 --> 2401.94]  So Go 1.16 is coming out soon.
[2402.06 --> 2407.20]  With each release like that, there's subtle things that may change in the runtime or how
[2407.20 --> 2409.96]  the binaries are put together that Delve kind of has to adapt to.
[2409.96 --> 2415.68]  So we continuously work on supporting the latest release, making sure that, you know, by the
[2415.68 --> 2418.94]  time that release comes out, there's a Delve version that can support and debug it.
[2419.30 --> 2421.04]  So that's always kind of a big thing for us.
[2421.16 --> 2425.16]  We also have a few kind of interesting like features coming up down the line.
[2425.42 --> 2430.78]  So my co-maintainer is working on a feature where you can, during an interactive debug session,
[2430.78 --> 2435.78]  you can create and produce a core dump from the process that you're debugging.
[2435.92 --> 2439.38]  So it's similar to like G-Core, if folks have ever used something like that.
[2439.38 --> 2441.00]  But works a little bit differently.
[2441.26 --> 2443.50]  So that's kind of a cool feature that's coming up.
[2443.94 --> 2449.28]  Another big push that we're kind of trying to do is improve the overall architecture support.
[2449.56 --> 2455.26]  So right now, Delve actually only supports a subset of all of the architectures that Go
[2455.26 --> 2456.18]  can actually run on.
[2456.50 --> 2462.46]  And it supports the main ones that folks actually use, you know, AMD 64, ARM 64, things like that.
[2462.58 --> 2467.88]  But there are some kind of outlier architectures that Go supports that Delve doesn't yet that
[2467.88 --> 2469.56]  we're also working on as well.
[2469.74 --> 2472.84]  So there's a pull request up right now for supporting 32-bit ARM.
[2473.06 --> 2478.62]  We're looking at supporting like PowerPC 64 and S390X, which are kind of weird architectures.
[2479.12 --> 2482.58]  But those are kind of some of the bigger things that we have on the roadmap so far.
[2483.04 --> 2484.18]  What about Apple Silicon?
[2484.18 --> 2486.26]  Yeah, so that's an interesting one.
[2486.36 --> 2490.92]  Because with Delve, we actually have like a so we have a few different backends that Delve
[2490.92 --> 2491.48]  can actually use.
[2491.56 --> 2496.90]  So there's a native backend, which we actually we wrote and maintain and we can actually interact
[2496.90 --> 2497.70]  with other backends.
[2497.82 --> 2502.84]  So like the talk that I'm giving tomorrow is on using Mozilla RR as a backend to do like
[2502.84 --> 2503.84]  record replay debugging.
[2503.84 --> 2511.26]  So with that, Delve on macOS actually uses LODB server as the backend.
[2511.44 --> 2518.26]  We have a native Mac backend, but it turns out that the documentation for the mock kernel
[2518.26 --> 2519.70]  is horrendous.
[2519.84 --> 2524.52]  And trying to figure out like how to actually work and interact with that kernel means like
[2524.52 --> 2529.98]  when I wrote the original backend for Mac, it was digging through like the open source
[2529.98 --> 2534.90]  kernel to figure out some of these like ptrace commands and some of these weird stuff that
[2534.90 --> 2538.74]  I that I had to do because the documentation is subpar for that kind of thing.
[2538.86 --> 2541.84]  So all that to say, we use LODB server on the backend.
[2542.00 --> 2545.54]  So there's some kind of changes that we have to do internally with Delve.
[2545.68 --> 2550.96]  But some of the heavy lifting we kind of get for free by using LODB server, which, you
[2550.96 --> 2555.16]  know, Apple is certainly going to make work on their silicon.
[2555.58 --> 2557.46]  So, okay, great.
[2557.46 --> 2557.78]  Wow.
[2557.94 --> 2562.66]  So Delve really is kind of a big thing because I always think of it as this little tool.
[2563.52 --> 2564.64]  I mean, how big is it?
[2565.08 --> 2566.80]  Big in terms of what metric?
[2567.26 --> 2567.70]  Size.
[2568.08 --> 2569.94]  It's a fairly, I mean, no, I don't know.
[2570.14 --> 2575.58]  The scope of the actual source code and all that stuff, it's definitely grown and it's
[2575.58 --> 2580.54]  grown a little bit in complexity over the years as we've introduced like different backends
[2580.54 --> 2581.56]  and things like that.
[2581.62 --> 2586.90]  The goal has kind of always been to keep it as simple and straightforward from a code perspective
[2586.90 --> 2587.88]  on this possible.
[2588.06 --> 2592.48]  But, you know, over time, obviously things get more complicated and you have to deal
[2592.48 --> 2593.62]  with weird situations.
[2594.32 --> 2598.86]  But yeah, I mean, from just, you know, like the perspective of the code and stuff like
[2598.86 --> 2601.68]  that, the project itself, it's a fairly big project at this point.
[2602.32 --> 2603.24]  Yeah, it sounds like it.
[2603.24 --> 2610.20]  When new features come to Go, like say, generics lands in Go, what will that mean for Delve?
[2610.54 --> 2614.16]  You know, is there things you're just going to get for free or will there be times when
[2614.16 --> 2618.30]  certain language features are added that that creates a lot of work for you?
[2618.64 --> 2619.20]  It depends.
[2619.36 --> 2625.08]  So a lot of that we would get for free a little bit by the kind of debug information that's
[2625.08 --> 2627.92]  provided from like Go binaries and things like that.
[2627.92 --> 2633.64]  So it would kind of be up to the Go compiler and linker to produce the correct information
[2633.64 --> 2636.64]  that Delve needs to be able to debug that stuff properly.
[2637.22 --> 2641.24]  And with big new features like that, sometimes the support is there, sometimes it's not.
[2641.40 --> 2646.72]  You know, sometimes we have to work with folks upstream to get that in or submit some patches
[2646.72 --> 2648.22]  ourselves and things like that.
[2648.52 --> 2652.10]  But a lot of it comes with like just coordination with the Go team.
[2652.10 --> 2657.70]  There's certain things that are Go specific that, you know, we've had to work really closely
[2657.70 --> 2659.76]  with the Go team to be able to achieve.
[2660.06 --> 2661.66]  Like, for example, function calls.
[2661.76 --> 2665.30]  This is something that actually requires support from the Go runtime.
[2665.76 --> 2668.50]  And we had to work with the Go team to kind of make that happen.
[2668.60 --> 2669.54]  It was a coordinated effort.
[2669.74 --> 2671.34]  So sometimes there's more coordination.
[2671.56 --> 2672.70]  Sometimes we get stuff for free.
[2673.76 --> 2675.04]  Oh, cool.
[2675.82 --> 2679.54]  Okay, well, it's time for our regular slot.
[2679.54 --> 2682.48]  It's time for Unpopular Opinions.
[2699.00 --> 2702.08]  So who wants to kick us off with an unpopular opinion?
[2702.92 --> 2707.68]  I will say that when you mentioned this, I was going to say that print statements are okay
[2707.68 --> 2710.94]  for debugging, but I don't think that will be that unpopular.
[2710.94 --> 2719.64]  So I will say that baseball is the by far most exciting sport in the world.
[2720.00 --> 2720.44]  Baseball?
[2720.54 --> 2721.20]  Which one's that?
[2721.40 --> 2724.58]  It's the one with all the bases and the ball.
[2724.98 --> 2725.56]  Clues in the name.
[2726.48 --> 2726.88]  Absolutely.
[2727.30 --> 2728.42]  Clever name now, actually.
[2728.52 --> 2731.00]  I genuinely didn't actually make that link.
[2731.00 --> 2736.92]  Well, baseball, it gives us lots of metaphors, doesn't it?
[2737.14 --> 2739.62]  It contributes the most metaphors, but I don't know.
[2740.12 --> 2742.64]  Hannah, is baseball a good sport?
[2742.64 --> 2743.56]  Hannah, do you agree?
[2743.68 --> 2744.78]  Is baseball a good sport?
[2745.42 --> 2750.32]  So other than US and some Asian countries, who play baseball?
[2750.90 --> 2751.70]  Yeah, I don't know.
[2752.26 --> 2752.86]  Latin America?
[2753.56 --> 2753.72]  Yeah.
[2753.84 --> 2754.68]  Oh, yeah.
[2755.22 --> 2756.12]  And in Europe?
[2756.38 --> 2757.12]  No, not really.
[2757.12 --> 2760.94]  No, we have kind of versions, different versions of it.
[2761.18 --> 2761.60]  I don't know.
[2761.74 --> 2764.54]  But yeah, that is potentially unpopular.
[2764.78 --> 2765.40]  We'll just...
[2765.40 --> 2767.44]  But they are missing the best sport, right?
[2767.84 --> 2768.52]  Apparently so.
[2768.80 --> 2769.04]  Yeah.
[2769.28 --> 2770.66]  That's what we've heard.
[2770.92 --> 2771.78]  According to Grant.
[2772.02 --> 2772.18]  Yeah.
[2772.80 --> 2774.86]  Derek, is baseball the best sport?
[2775.38 --> 2777.24]  Best or most exciting?
[2777.40 --> 2780.16]  I would refute most exciting.
[2780.34 --> 2782.78]  I think football is pretty exciting.
[2783.10 --> 2784.52]  I get excited watching...
[2784.52 --> 2786.04]  I don't know if you consider this a sport,
[2786.04 --> 2789.44]  but I like watching poker championships and stuff,
[2789.54 --> 2790.40]  and that's pretty exciting.
[2790.66 --> 2792.70]  So it depends on your metric.
[2793.22 --> 2795.80]  I watch the StarCraft online, the StarCraft championships.
[2796.50 --> 2796.70]  Yeah.
[2796.84 --> 2797.20]  There you go.
[2797.26 --> 2797.60]  That's exciting.
[2798.34 --> 2798.54]  Yeah.
[2798.98 --> 2799.16]  Yeah.
[2799.26 --> 2802.48]  But I just don't go outside, so I've certainly never played baseball.
[2803.44 --> 2805.16]  I think baseball is exciting.
[2805.66 --> 2805.84]  Yeah.
[2805.92 --> 2809.14]  Especially because when you watch baseball,
[2809.38 --> 2811.96]  you eat hot dog, you drink beer.
[2812.28 --> 2813.62]  How cool is it, right?
[2813.70 --> 2815.06]  That's the most exciting one.
[2815.06 --> 2817.16]  Like soccer, you have to watch.
[2818.28 --> 2819.52]  Basketball, you have to watch.
[2819.98 --> 2821.92]  Baseball, it's so slow and relaxing.
[2822.10 --> 2822.80]  Best sport.
[2823.02 --> 2823.12]  I agree.
[2823.12 --> 2824.70]  You don't have to pay attention to it.
[2824.76 --> 2825.60]  That's how good it is.
[2825.78 --> 2826.52]  That's how exciting.
[2827.04 --> 2827.14]  Yeah.
[2827.64 --> 2829.24]  You can just focus on your hot dog.
[2830.40 --> 2832.38]  Do we have any other unpopular opinions?
[2832.58 --> 2834.40]  And by the way, we test these on our Twitter,
[2834.82 --> 2836.06]  at GoTimeFM.
[2836.06 --> 2840.06]  So we'll find out if that is indeed popular or not.
[2840.32 --> 2840.74]  Any others?
[2840.94 --> 2841.82]  We've got a couple of minutes.
[2842.92 --> 2845.06]  I have an opinion.
[2845.48 --> 2848.56]  The world will be better if everybody uses Linux.
[2849.44 --> 2849.70]  Oh.
[2850.84 --> 2851.52]  Now that's okay.
[2851.78 --> 2851.94]  Oh, yeah.
[2852.28 --> 2853.16]  It's controversial.
[2853.54 --> 2853.88]  Oh, yeah.
[2853.88 --> 2857.54]  All the EVPF, like all this Ptrace,
[2857.70 --> 2860.52]  they are not available in other platforms.
[2860.52 --> 2864.60]  But what about every other app in the world?
[2865.94 --> 2867.76]  But I suppose if everyone was using it,
[2868.30 --> 2869.40]  if everyone's using it,
[2869.50 --> 2871.42]  they would work too, wouldn't they?
[2872.26 --> 2872.90]  That's a fair one.
[2872.98 --> 2873.06]  Yeah.
[2873.68 --> 2875.22]  Derek, do you have an unpopular opinion?
[2875.62 --> 2876.38]  I don't think so.
[2876.62 --> 2877.98]  Do you agree with the Linux one?
[2878.32 --> 2879.78]  I think the world could be a better place
[2879.78 --> 2880.74]  if everybody used Linux.
[2882.56 --> 2884.30]  I'm not as creative as everybody else.
[2884.36 --> 2885.82]  I don't have anything off the top of my head.
[2886.58 --> 2887.36]  That's unpopular.
[2887.58 --> 2888.64]  You created Delve.
[2889.44 --> 2890.02]  You've done it.
[2890.42 --> 2892.40]  You've accidentally fulfilled
[2892.40 --> 2893.64]  your contractual obligations
[2893.64 --> 2896.86]  to provide an unpopular opinion for us.
[2897.06 --> 2899.96]  We are running out of time.
[2900.30 --> 2902.06]  So I really only have time to say
[2902.06 --> 2904.14]  thank you so much for doing this.
[2904.22 --> 2905.12]  It was a great conversation.
[2905.54 --> 2906.98]  I wish we could spend more time.
[2907.06 --> 2908.74]  And in fact, we'll invite you back
[2908.74 --> 2909.92]  at some point to come and do
[2909.92 --> 2911.12]  another GoTime episode.
[2911.64 --> 2914.04]  Thank you very much to my guests,
[2914.18 --> 2915.22]  Hannah, Grant and Derek.
[2915.78 --> 2916.72]  It's been a pleasure.
[2917.66 --> 2918.02]  Goodbye.
[2918.94 --> 2919.64]  Thank you so much.
[2919.64 --> 2920.36]  Thank you.
[2920.62 --> 2920.98]  Thank you.
[2920.98 --> 2922.22]  Yeah, thank you for inviting me on.
[2922.22 --> 2927.88]  If you enjoyed this episode,
[2928.20 --> 2930.28]  subscribe now at GoTime.fm.
[2930.68 --> 2932.42]  Hey, we are getting close to the end of the year
[2932.42 --> 2934.10]  and you may be dusting off the old blog
[2934.10 --> 2936.88]  to write that epic best of or worst of post.
[2937.38 --> 2939.76]  If so, we'd love if you'd include GoTime
[2939.76 --> 2940.54]  in your list of favorites.
[2941.06 --> 2942.72]  Let us know on Twitter when you publish.
[2942.72 --> 2944.74]  I can pretty much guarantee you a retweet
[2944.74 --> 2945.96]  from at GoTime.fm.
[2946.42 --> 2948.74]  Music for GoTime is produced by the Mysterious One,
[2948.96 --> 2949.78]  Breakmaster Cylinder,
[2949.96 --> 2951.62]  and we're brought to you by awesome sponsors.
[2952.12 --> 2954.78]  Thanks again to Fastly, Linode, and LaunchDarkly.
[2955.22 --> 2956.26]  That's our show.
[2956.52 --> 2957.40]  On the next episode,
[2957.52 --> 2960.06]  Ellen Corbis joins Matt, Chris, and Natalie
[2960.06 --> 2962.46]  to discuss Go in other spoken languages.
[2962.56 --> 2963.46]  It's a good one,
[2963.62 --> 2964.62]  so stay tuned for that
[2964.62 --> 2965.96]  next week.
[2992.46 --> 3022.44]  Thank you.
[3022.46 --> 3052.44]  Thank you.
[3052.46 --> 3055.00]  You'd have told me you were going to do that and then I'd have done an index earlier.
[3056.16 --> 3056.94]  As it is.
[3057.10 --> 3057.24]  Yeah.
[3057.52 --> 3057.82]  Nothing.
[3058.52 --> 3064.52]  All my jokes are from my kids because they ask Alexa for jokes all the time and they're
[3064.52 --> 3066.96]  just the dumbest jokes ever.
[3067.48 --> 3070.20]  And those are literally the only ones I know because they'll ask me like six times.
[3070.26 --> 3073.22]  I have a bunch of kids so each kid will ask me the same joke because they just learned
[3073.22 --> 3074.16]  it from their brother or sister.
[3074.72 --> 3076.02]  They think I've never heard it.
[3076.02 --> 3076.90]  I've heard them all six times.
[3078.76 --> 3080.54]  What has four wheels and flies?
[3081.50 --> 3082.18]  A garbage truck.
[3082.58 --> 3082.76]  See?
[3083.12 --> 3083.62]  They're not funny.
[3084.24 --> 3085.38]  But I knew it immediately.
[3086.06 --> 3086.76]  It's not funny.
[3086.88 --> 3087.22]  What does it fly?
[3087.80 --> 3088.46]  It has flies.
[3088.76 --> 3089.60]  Oh, it has flies.
[3089.96 --> 3090.18]  Yeah.
[3090.36 --> 3092.14]  What has four wheels and flies?
[3092.56 --> 3093.10]  Oh, right.
[3093.66 --> 3094.10]  There you go.
[3094.16 --> 3094.48]  Ah, see?
[3094.52 --> 3095.10]  It is funny.
[3096.04 --> 3097.50]  It's better than you thought it was.
[3098.00 --> 3098.16]  Yeah.
[3098.66 --> 3099.76]  I need to explain it.
[3099.82 --> 3102.62]  But yeah, once it's explained, I'm all over it.
[3102.94 --> 3105.28]  Did you know that ducks can float?
[3105.62 --> 3105.96]  Can they?
[3106.44 --> 3106.72]  Yeah.
[3106.86 --> 3107.50]  I didn't know that.
[3107.64 --> 3108.00]  What do you mean?
[3108.28 --> 3108.84]  Of course they do.
[3108.90 --> 3110.16]  They're always on the water, aren't they?
[3110.66 --> 3111.52]  Is this another joke?
[3112.08 --> 3113.00]  No, it's not a joke.
[3113.18 --> 3113.52]  Flunt back?
[3113.52 --> 3114.02]  Ducks can float.
[3114.52 --> 3114.70]  Yeah.
[3114.70 --> 3116.46]  I think it's pretty cool.
[3117.08 --> 3118.16]  Are they floating or swimming?
[3118.60 --> 3119.86]  I guess a little bit of both.
[3120.38 --> 3120.60]  Hmm.
