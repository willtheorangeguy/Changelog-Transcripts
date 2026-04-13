[0.00 --> 19.34]  Welcome to The Change Log, episode 0.2.4.
[19.44 --> 20.44]  I'm Adam Stachowiak.
[20.68 --> 21.46]  And I'm Wynne Edelman.
[21.72 --> 23.12]  This is The Change Log.
[23.18 --> 24.82]  We cover what's fresh and new in open source.
[25.34 --> 28.14]  If you caught us on iTunes, we're also on the web at thechangelog.com.
[28.14 --> 29.42]  And hey, look, we're also on GitHub.
[30.00 --> 30.28]  Yep.
[30.40 --> 34.30]  Check out some feature repos there from our blog, as well as some trending repos from GitHub,
[34.98 --> 36.42]  as well as our audio podcast.
[36.80 --> 40.34]  And if you're on Twitter, you can follow changelogshow, not the changelog.
[40.44 --> 41.34]  And I'm Adam Stach.
[41.82 --> 44.16]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[44.86 --> 50.86]  Had fun talking to David or Corden and gang over at Facebook about the open source projects.
[51.06 --> 53.64]  Hey, you might as well call them open source with all the projects they've got going on.
[53.80 --> 54.30]  That's true.
[54.30 --> 61.18]  We talked about Tornado and HipHop and 320, some cool applications that cover a wide range of technologies.
[61.30 --> 65.40]  Also, some new API advancements, OAuth 2 and OpenGraph.
[65.82 --> 67.04]  Yeah, a lot of fun stuff going on there.
[67.12 --> 69.42]  They were really excited, too, about everything they were doing.
[69.92 --> 72.74]  Yeah, the passion kind of just oozes out of what they're doing.
[72.84 --> 73.46]  You can see it.
[73.88 --> 74.08]  Yeah.
[74.32 --> 74.46]  Yeah.
[74.46 --> 76.78]  Hey, Adam, where can people catch up with us in person?
[77.44 --> 81.96]  The Texas JavaScript Conference over at Austin, June 5th.
[81.98 --> 82.76]  June 5th?
[82.84 --> 82.98]  June 5th.
[82.98 --> 84.88]  And you're going to be at LesConf this weekend?
[85.22 --> 86.00]  Absolutely, yeah.
[86.04 --> 88.14]  Be over there all weekend.
[88.84 --> 89.60]  Enjoying Atlanta.
[90.02 --> 91.24]  Sunny Atlanta, Georgia.
[91.52 --> 92.34]  Great episode this week.
[92.38 --> 92.90]  Should we get to it?
[93.18 --> 93.78]  Let's do it.
[93.78 --> 107.18]  All right, we're joined today by several folks at Facebook to talk about open-sourcery at Facebook.
[107.80 --> 112.44]  David, kind of the ringleader there in the conference room, why don't you introduce the folks and each of the projects?
[113.40 --> 113.70]  Sure.
[113.70 --> 115.00]  So I'm David Recorden.
[115.56 --> 120.48]  I joined Facebook last fall and work on open-source and standards here at Facebook.
[120.48 --> 126.44]  As Wyn said, we have a group of five engineers here that work on a variety of open-source projects.
[127.40 --> 133.34]  We'll go ahead and introduce themselves, talk a little bit about the projects which they work on, and we can dig into them, answer some questions.
[134.20 --> 135.82]  Hi, this is Hai Ping.
[136.28 --> 138.32]  I joined Facebook about three years ago.
[138.32 --> 146.66]  I have been working on this project that's called HipHop Compiler, which is basically transforming PHP into CPaaS Pass, just to try to speed it up.
[147.30 --> 148.64]  Hi, this is Paul Buhay.
[148.64 --> 151.52]  I'm one of the former friend feeders.
[151.68 --> 164.30]  We've joined Facebook last August, and I'm going to talk about Tornado, which was the real-time web framework that was extracted from friend feed and open-source last fall.
[165.42 --> 166.70]  I'm Owen Yamauchi.
[166.98 --> 168.50]  I work on our iPhone application.
[168.96 --> 175.36]  I've been at Facebook for almost a year now, and I'll be talking about 320, which is our open-source framework for iPhone developers.
[175.36 --> 182.42]  And I'm Scott McVicker, and I work on hip-hop for PHP with Hai Ping as well.
[183.24 --> 185.96]  I always love those deep, long introductions there.
[186.04 --> 186.60]  They're always awesome.
[186.68 --> 188.06]  It's such one as, like, five people deep.
[188.58 --> 190.12]  I was trying to write all the names down.
[190.32 --> 191.34]  I had lost count.
[191.36 --> 192.36]  I was waiting one more.
[192.52 --> 195.14]  I wrote all the names down and kind of got the gist of this.
[195.18 --> 195.94]  We got David recording.
[196.04 --> 196.50]  We got Hai Ping.
[196.58 --> 197.32]  We got Paul Buhay.
[197.40 --> 200.32]  We got, is it Owen Yamaguchi and Scott McVicker?
[200.52 --> 200.96]  Is that right?
[201.42 --> 201.72]  Yeah.
[202.12 --> 202.34]  Okay.
[202.34 --> 204.04]  So, I don't know.
[204.10 --> 204.92]  Should we start with Tornado?
[205.62 --> 205.92]  Sure.
[206.46 --> 206.70]  Sure.
[207.38 --> 208.88]  Paul, do you want to start Tornado a little bit?
[209.42 --> 209.72]  Sure.
[209.86 --> 216.50]  So, Tornado is actually a collection of useful parts, basically, that we extracted from friend feed.
[216.84 --> 223.00]  We took what we thought was probably most reusable, most applicable to things other than friend feed,
[223.00 --> 229.80]  and also things that were somewhat unique and packaged them all up for the world to use.
[229.80 --> 231.84]  And so, it's written in Python.
[232.46 --> 234.86]  It's actually relatively small.
[235.60 --> 240.02]  I keep getting this number wrong, but I think it's about 5,000 lines of code.
[240.38 --> 247.78]  So, if nothing else, it's actually just an interesting and enjoyable code base to read through
[247.78 --> 254.14]  and get familiar with some of the real-time non-blocking concepts that are becoming more important
[254.14 --> 264.02]  as more web services are trying to do things like IM or real-time updates in the way that friend feed or Facebook does.
[264.60 --> 270.34]  And the reason that that can be difficult with a lot of traditional frameworks is that they are based on a blocking model
[270.34 --> 276.32]  where every request requires a thread or a process on the server.
[276.84 --> 283.30]  And so, if you have thousands or tens of thousands or millions of users connected to your website,
[283.72 --> 287.96]  that means you have a connection open from every one of those web browsers at all times.
[288.28 --> 292.46]  So, you need a web server that's capable of handling many thousands of connections simultaneously.
[292.46 --> 299.74]  And so, that's really the most core value provided by Tornado.
[300.00 --> 305.36]  But there's also a number of other features in there like easy authentication modules for Facebook
[305.36 --> 311.28]  and OpenID and OAuth and Twitter and Google and just a handful of other utilities
[311.28 --> 316.18]  that we thought were really nice to have, such as command line flags that are very easy to use.
[316.54 --> 319.32]  So, who's using Tornado besides Facebook, do you know?
[319.32 --> 322.44]  Quora is using it, I believe.
[322.88 --> 326.82]  That's Adam DeAngelo's startup that's doing the Q&A service.
[327.64 --> 335.48]  Brizzly, which is Jason Schellin's startup, they're doing kind of like a Twitter client and more.
[335.60 --> 341.48]  I don't really know the complete vision, honestly, but they've been in the process of switching over.
[342.40 --> 345.20]  And I've heard of a number of other people using it,
[345.20 --> 349.26]  I'm not sure which ones are publicly announced yet.
[349.34 --> 351.20]  But there's a fairly active community.
[351.70 --> 353.76]  What is the Quora one you mentioned, the first one?
[354.48 --> 359.44]  Quora, Adam DeAngelo is one of the other, I don't know if he's officially a Facebook co-founder
[359.44 --> 360.88]  or what the status is there.
[360.98 --> 365.66]  But he was one of Zuck's roommates early on and used to be the CTO of Facebook.
[365.86 --> 369.78]  And so, he has a new startup called Quora, which is a Q&A service.
[370.32 --> 372.16]  It may still be in private beta, I'm not sure.
[372.16 --> 373.06]  It's pretty cool, though.
[373.68 --> 380.26]  And what it does, part of the reason they use Tornado is it does some of the same real-time updates.
[380.48 --> 385.38]  So, someone might ask a question and then other people will add answers or edit the question.
[386.06 --> 390.16]  And because of the real-time functionality, when you're looking at the web page,
[390.20 --> 393.42]  you'll actually see those updates come in as they occur.
[393.54 --> 396.62]  So, you don't have to reload the page to see if someone has added a comment.
[397.00 --> 399.00]  You'll actually see it pop in in real-time.
[399.00 --> 405.06]  How would this correspond to, I guess, some other technologies, maybe in the Ruby space,
[405.14 --> 407.96]  like Event Machine or Node.js over in the JavaScript space?
[409.50 --> 413.82]  It's actually a comparable approach.
[414.40 --> 420.18]  I don't know everything about Event Machine, but I know Node.js is based on a similar model
[420.18 --> 427.88]  where you have, I think they're all based fundamentally on the ePoll system call in Unix,
[427.98 --> 432.60]  which allows you to basically monitor a large number of file descriptors in an efficient manner.
[433.36 --> 438.90]  And so, they're all just different wrappers around ePoll at its heart, but done in different languages.
[438.90 --> 442.96]  So, I think Event Machine, and I'm probably getting this wrong,
[443.04 --> 445.70]  but I think it's kind of a hybrid of C++ and Ruby.
[447.42 --> 451.56]  We actually tried to keep Tornado as pure of Python as possible.
[451.74 --> 459.56]  There is a small C++ module for Python 2.5, but 2.6, it actually is completely Python-based.
[459.56 --> 463.82]  So, it looks like with something this fast in the middle tier,
[463.94 --> 467.20]  your data layer could quite possibly be the bottleneck very quickly.
[467.40 --> 471.56]  What is normally, I guess, coupled with something like this to provide that sort of speed?
[473.02 --> 473.60]  Yeah, exactly.
[473.78 --> 477.50]  So, this has actually been a fairly controversial point, I think,
[477.54 --> 483.10]  in the asynchronous web server community, to the extent there is such a thing,
[483.52 --> 486.08]  which is, do you try to make everything asynchronous?
[486.30 --> 487.20]  How do you handle that?
[487.20 --> 491.30]  And the approach that we took was that we found that making everything asynchronous
[491.30 --> 499.12]  was actually just annoying because it makes your code fairly complex because it's full of callbacks.
[499.66 --> 505.12]  So, we thought that the most important thing was that the external events,
[505.32 --> 509.20]  you know, web browsers or fetching external URLs need to be asynchronous
[509.20 --> 511.04]  because those are things beyond your control.
[511.52 --> 514.94]  But local resources, such as a database, is actually okay to block
[514.94 --> 518.04]  because you need for your database to be fast anyway.
[519.32 --> 527.10]  And so, the approach we took at FriendFeed is essentially just to run a fairly large number of frontends.
[527.28 --> 531.60]  And that way, we also circumvent the problem with the Python global interpreter lock,
[532.04 --> 537.98]  which effectively limits Python to only be able to use a single core at a time anyway.
[537.98 --> 542.16]  And so, what we would do is, you know, on an eight-core machine, we might just run 10 frontends.
[542.48 --> 546.86]  And then we would put them all behind Nginx, which is a very fast reverse proxy.
[547.70 --> 551.80]  Are you guys using this just at FriendFeed, or has it been folded into Facebook properties at all?
[552.76 --> 554.76]  I don't believe there's any usage at Facebook.
[554.90 --> 558.66]  Facebook, as I guess the others we'll talk about, is largely written in PHP.
[558.66 --> 564.48]  So, it's not really something that can be easily adapted for use here.
[565.02 --> 569.10]  So, in the lunchroom, you guys kind of divide up into the tornado and hip-hop crowds
[569.10 --> 570.94]  and throw gang symbols and things?
[571.12 --> 573.84]  Yeah, it's an east side, west side kind of thing.
[575.06 --> 576.52]  That might be a nice segue.
[576.62 --> 577.82]  Let's talk about hip-hop for a second.
[578.38 --> 578.86]  Yeah, sure.
[579.22 --> 579.98]  This is Hai Ping.
[580.64 --> 586.40]  So, the major problem we're trying to solve is the CPU consumption problem on WebTier.
[586.40 --> 590.34]  The intention is very simple.
[590.46 --> 592.02]  We just want to speed up PHP.
[592.52 --> 597.98]  That way, it can take a lot less CPU, which means a lot less number of machines.
[599.48 --> 605.96]  The idea was just to transform the PHP into C++ because, you know, syntax-wise,
[606.08 --> 608.32]  these two languages are very similar to each other.
[608.84 --> 610.30]  And, you know, we were just asking the question,
[610.98 --> 614.86]  why C++ could run faster, but PHP runs a lot slower?
[614.86 --> 620.56]  After the transformation, you know, a lot of the dynamic C++ lookup can be eliminated.
[621.40 --> 626.02]  Things were dynamic in PHP can just become static in C++.
[626.80 --> 629.08]  And also, we do some type inference.
[629.38 --> 631.94]  You know, hopefully the code can be a lot more efficient.
[632.48 --> 633.86]  So, that was the basic idea.
[634.00 --> 639.04]  And it took us two and a half years, two years,
[639.14 --> 640.80]  about like one and a half year of development.
[640.80 --> 645.74]  Initially, we had three people, Ian Proctor, Minghui Yao, and I.
[646.42 --> 649.56]  We spent one and a half year of coding.
[649.94 --> 650.88]  We wrote a lot of code.
[651.50 --> 654.88]  And then it took us another one year of time, you know,
[654.96 --> 657.80]  six months of correctness testing and six months of rollout.
[658.14 --> 663.04]  So, adding together is like one year of rolling out to all the web servers we have.
[663.04 --> 670.86]  So, right now, nearly all the web traffic is served by the HipHop Compile program.
[672.32 --> 673.26]  It's been running well.
[673.40 --> 676.02]  It's been running, you know, with a lot of speed up.
[676.22 --> 679.36]  I think it's 2x, 2x, 3x speed up.
[679.66 --> 681.60]  So, it's been working for us.
[682.32 --> 684.86]  How long did you say that you were in development of the project part of it?
[684.98 --> 685.96]  Like a year, year and a half?
[686.36 --> 687.76]  A year and a half, yes.
[687.76 --> 690.10]  We've been writing a call for one year and a half.
[692.20 --> 698.04]  And then we spent like a lot of time just to make sure it really runs, you know, correctly.
[698.28 --> 700.88]  Meaning like it's the same as what PHP does.
[701.84 --> 704.16]  And so, what kind of resources did you have available like when you were in development?
[704.32 --> 707.40]  Was it just two people or was it a small team?
[708.10 --> 708.68]  Three people.
[708.88 --> 711.32]  So, Ian Proctor, Minghui Yao, and I, we have three people.
[711.62 --> 717.14]  And then after one year time, we have another three people join our team.
[717.14 --> 719.12]  So, right now we have more people.
[719.30 --> 721.56]  We have a total of eight people working on the compiler.
[722.24 --> 724.58]  You know, we're still working very hard on more optimizations.
[725.48 --> 728.56]  So, do you have to pre-compile your PHP code to take advantage of something like this?
[729.68 --> 730.76]  You mean other people?
[730.88 --> 732.82]  Have other people done similar work before?
[732.94 --> 739.08]  So, if you're going to use hip-hop, does your PHP code have to run through some sort of pre-compiler to get this performance boost?
[739.16 --> 740.92]  Or is it still a dynamic language?
[742.80 --> 745.88]  The compilation only happens during deployment.
[745.88 --> 753.06]  So, during regular development, people continue to use the interpreter, which doesn't require them to compile.
[753.48 --> 756.74]  So, they can still write the web pages really, really, really fast.
[757.60 --> 762.48]  Only when the code is ready to push, we'll just compile that into a binary and just push that binary.
[763.04 --> 769.66]  Are there any syntactical limitations, I guess, between the interpreted PHP code and what you guys can support from the compiled version?
[769.66 --> 771.28]  Very few.
[771.88 --> 775.26]  Evalve is one of them, which isn't recommended anyway.
[775.26 --> 783.28]  So, to support Evalve is pretty hard for us because it also takes away some of the organization we can do.
[784.34 --> 788.56]  Other than that, there's also two or three minor places we don't support.
[788.56 --> 792.32]  But otherwise, you know, almost all the features are supported.
[793.76 --> 800.12]  What would be the use case for someone to consider using this PHP framework?
[800.12 --> 811.24]  I think it's more useful if you have a large number of machines or you are running a large-scale PHP code base.
[812.84 --> 819.16]  You really want to save a number of machines in your company, then this might help.
[819.62 --> 824.38]  So, the biggest gain really is just a reduction of the amount of machines needed and faster code, obviously.
[824.38 --> 824.82]  Yes.
[825.58 --> 826.02]  Yes.
[827.02 --> 829.14]  A lot of people were confused.
[829.46 --> 833.54]  You know, maybe this compiler can help making web pages serving faster.
[833.74 --> 836.32]  But that turned out to be a bigger equation.
[836.80 --> 840.86]  When you talk about web page speed, you also have to count the network time.
[841.28 --> 848.94]  Not only from the browser to your web servers, but also from your web server to backend servers, you know, to database servers, to mempatch servers.
[849.28 --> 851.58]  You have to count all those network IEL time.
[851.58 --> 858.18]  What we are saving is only the CPU time taken by the web servers.
[858.86 --> 864.22]  So, depending on the nature of your web page, that portion can be big or small.
[865.08 --> 869.14]  What we are trying to save is really the computation power or the number of machines.
[870.04 --> 871.00]  How did this project come about?
[871.10 --> 875.12]  Who had the idea to take off and do this?
[875.92 --> 877.54]  I had the idea, for sure.
[877.54 --> 885.12]  But, you know, Ian and Minghui, they just loved my idea, you know.
[885.36 --> 894.28]  And then when we got into implementation, it's everyone's idea, you know, how exactly to convert different kinds of PHP code into static C++ code.
[894.76 --> 896.14]  Then it's really just teamwork.
[896.66 --> 899.22]  You know, we had to just work out all the details.
[899.36 --> 900.82]  We had to solve all the problems we had.
[900.82 --> 906.94]  How far did you get in the process before you started enlisting support from your team and from management?
[907.88 --> 916.88]  I think I spent about eight months just by myself just to work out a prototype good enough to show people.
[917.52 --> 919.02]  It's very promising, you know.
[919.12 --> 919.60]  It does.
[919.72 --> 920.76]  It runs faster.
[920.76 --> 924.86]  That's the time I had the other two people joining me.
[925.68 --> 930.64]  Having worked in that corporate type of environment before, I'm just always curious of, you know, sometimes you have to show rather than tell.
[930.86 --> 936.66]  And it's just curious of how far you had to get in the process before you could actually prove the idea.
[937.42 --> 944.84]  Well, so you have to realize Facebook is a very decentralized software engineering force.
[945.74 --> 948.52]  Everyone is very talented.
[948.52 --> 953.78]  You know, people normally can identify problems by themselves and proposing solutions by themselves.
[955.68 --> 964.06]  I don't think our management, you know, never will say words to say you're not allowed to work on something, especially after communication with other people.
[964.52 --> 969.34]  Your idea can be appreciated by other people or approved by other people.
[969.34 --> 973.08]  So, no, no one said no to me.
[973.30 --> 974.42]  So, I was able to continue.
[975.08 --> 980.18]  And we were able to even form three people of a group to continue to work on this.
[980.60 --> 983.34]  Even though we understood that's risky, right?
[983.38 --> 987.64]  At any time point, we could just say, you know, that doesn't work well and it could fail.
[987.64 --> 994.86]  So, if we zoom out and we look at Facebook as it is now compared to previous to this project, what's really happened and what's been the gain?
[995.50 --> 998.00]  Comparing to not having a compiler.
[998.32 --> 998.62]  Right.
[998.62 --> 1002.98]  Then we would require more machines to run the same website.
[1003.70 --> 1014.52]  And there are some other benefits, you know, after converting the PHP code into CPaaS, we were able to build CPaaS libraries that the backend people can also take advantage of.
[1014.92 --> 1021.58]  You know, before the compiler, they were not able to call into PHP code base because PHP is not quite reusable by other languages.
[1021.58 --> 1028.10]  But after the conversion, you know, we were able to build a small library, you know, that people can just take and just call into PHP functions.
[1028.34 --> 1029.42]  That's also very beneficial.
[1030.00 --> 1035.06]  So, basically, we were just building a bridge between our PHP programmers and CPaaS path programmers.
[1035.46 --> 1036.24]  That's kind of cool.
[1037.04 --> 1037.68]  That's pretty cool.
[1038.70 --> 1041.52]  It's great that you have an environment that fosters innovation like that as well.
[1042.64 --> 1043.24]  Thank you.
[1043.70 --> 1051.34]  Speaking of innovation, I think one of the coolest apps on the iPhone, you know,
[1051.34 --> 1052.44]  is the Facebook application.
[1052.98 --> 1056.48]  And, correct me if I'm wrong, but I believe the 320 open source application is,
[1057.04 --> 1059.54]  the project is kind of the underpinnings of that.
[1059.76 --> 1061.32]  Who do we have to speak to 320?
[1062.06 --> 1062.86]  This is Owen.
[1063.46 --> 1067.08]  So, yeah, I'm currently the developer of Facebook's iPhone app.
[1067.74 --> 1074.74]  And, yeah, 320 is originally, it was extracted from Facebook for iPhone by the original developer, Joe Hewitt,
[1075.46 --> 1077.44]  whose name you probably know.
[1077.44 --> 1083.06]  So, it wasn't really developed with a sort of overarching theme.
[1083.18 --> 1089.74]  It was just a set of things that he considered useful or potentially useful to other developers.
[1091.60 --> 1097.92]  And, yeah, 320 powers a lot of what the iPhone app does, including its infrastructure for doing network requests.
[1097.92 --> 1104.56]  It does caching on the file system and in memory and network request queuing,
[1105.20 --> 1109.08]  as well as URL routing internal to the app.
[1109.62 --> 1116.42]  So, the app opens different views within itself through this internal URL mapping and routing mechanism that 320 provides.
[1116.42 --> 1122.70]  Other stuff that 320 provides is, like, large-scale pre-made native controls,
[1123.16 --> 1128.98]  like an interface that mimics the message-composing UI of the iPhone system's mail.app,
[1129.68 --> 1133.24]  which we use in the Facebook app for composing an inbox message.
[1134.24 --> 1144.14]  Other stuff includes what essentially comes down to a reimplementation of a CSS-like layout engine,
[1144.14 --> 1151.32]  which allows you to describe the way a set of views should be laid out or the way an individual view should be drawn.
[1152.56 --> 1157.20]  Those are sort of the main benefits that 320 gives us.
[1157.20 --> 1165.46]  How does a project keep up with the ever-involving Apple platform?
[1166.16 --> 1167.84]  iPad, iPhone, stuff like that.
[1169.18 --> 1172.66]  So, 320, one of our main focuses...
[1172.66 --> 1174.76]  So, I'm not the only person who works on 320, by the way.
[1174.92 --> 1178.64]  A former intern of ours named Jeff Riquoin has also done a lot of great work on it.
[1178.64 --> 1187.08]  Adapting 320 to be usable by iPad developers is a pretty high priority for us
[1187.08 --> 1190.66]  because, you know, it contains a lot of useful stuff, but in its current state,
[1191.24 --> 1196.88]  it's not really suitable for the iPad because it makes a lot of assumptions about screen size
[1196.88 --> 1198.88]  and a couple of other things.
[1198.88 --> 1205.58]  It would take some effort to make it compatible with, for example, the split view metaphor
[1205.58 --> 1209.16]  that is standard on the iPad.
[1209.50 --> 1211.84]  By split, you mean portrait or landscape?
[1213.30 --> 1214.68]  No, that part is fine.
[1214.82 --> 1218.96]  It's just by split, I mean having one scrollable list on the left
[1218.96 --> 1221.04]  and another scrollable list on the right, for example.
[1222.90 --> 1225.48]  Sorry, I've kind of forgotten what your original question was.
[1225.48 --> 1225.76]  Sorry.
[1227.86 --> 1228.42]  That's okay.
[1228.68 --> 1232.76]  What I wanted to know was, you know, as you guys evolve 320 in this code base,
[1232.82 --> 1237.02]  how do you continue to just keep up with this ever-evolving Apple platform
[1237.02 --> 1240.10]  that we're dealing with between, you know, we had the iPhone for a while,
[1240.16 --> 1243.00]  we have many applications, lots of different opportunities out there,
[1243.02 --> 1245.78]  and now you have this bigger platform called the iPad.
[1245.78 --> 1248.96]  How are you evolving 320 to manage both platforms?
[1252.80 --> 1254.52]  It's not really clear at this point.
[1254.52 --> 1258.94]  Like, our work on adapting 320 to the iPad is in its very early stages
[1258.94 --> 1264.64]  because there's a lot of, like, code architecture decisions that we need to make,
[1264.64 --> 1267.40]  and some of them it's not really clear what the best choice is.
[1269.80 --> 1273.04]  So, yeah, I don't really have much to say on that front.
[1273.12 --> 1277.02]  As far as the evolving Apple platform in the sense of new features
[1277.02 --> 1283.24]  that they introduce in the SDK, you know, generally we sort of look at those
[1283.24 --> 1287.50]  as they come out and, you know, keep up with when they deprecate certain things,
[1287.66 --> 1289.34]  which is pretty minor.
[1290.70 --> 1296.06]  For something like OS 4.0, which, where the SDK is going to have a bunch of new features,
[1296.12 --> 1299.86]  it remains to be seen, like, which ones of those will hook into 320.
[1299.86 --> 1304.48]  Some of it depends on if we decide to use those new features in the Facebook for iPhone app.
[1304.64 --> 1309.14]  Like, that's a major driver of putting new stuff into 320.
[1309.58 --> 1314.46]  Like, if our iPhone app requires it and 320 is a good place for it, then we do that.
[1314.46 --> 1314.50]  Yeah.
[1315.62 --> 1321.36]  We certainly applaud you for one of the better Objective-C iPhone open source projects out there.
[1322.10 --> 1326.38]  Are you up to date on kind of the state of open source and Objective-C,
[1326.48 --> 1330.10]  especially in the iPhone, and what other good projects are out there that folks should check out?
[1331.96 --> 1337.06]  Well, just to start with, a lot of people have actually made forks of 320
[1337.06 --> 1339.74]  where they put their own modifications on top of it.
[1339.74 --> 1342.58]  And some of those are actually pretty good.
[1342.70 --> 1344.78]  Like, they implement a lot of new features.
[1345.52 --> 1348.20]  And those forks are divergent from our implementation,
[1348.52 --> 1351.44]  and we're probably not going to reintegrate those into mainline,
[1351.52 --> 1353.60]  but it's still well worth checking out.
[1354.52 --> 1359.30]  As far as other frameworks for the iPhone,
[1359.78 --> 1364.16]  I don't know of any that are as sort of broad-ranging and comprehensive as 320.
[1364.16 --> 1370.38]  I actually don't know very many at all.
[1370.52 --> 1373.24]  Like, the ones that I do know have very specific purposes,
[1374.18 --> 1376.76]  like serializing and deserializing JSON,
[1378.20 --> 1380.86]  translating between JSON and Objective-C objects, that is,
[1381.48 --> 1385.92]  or providing sort of object-oriented interface to SQLite.
[1386.76 --> 1389.04]  Those are the kinds of things we can make use of.
[1389.04 --> 1396.62]  But, no, really, as far as the state of open-source iPhone libraries in general,
[1396.74 --> 1400.40]  I think, you know, there's a lot less there than there could be.
[1400.94 --> 1403.88]  320 is pretty big and in fairly wide use,
[1404.74 --> 1410.30]  but I really don't know of that many others,
[1410.30 --> 1413.64]  which sort of suggests to me that there isn't really a thriving
[1413.64 --> 1416.54]  open-source community in iPhone development.
[1416.54 --> 1419.60]  So, was that all the projects?
[1419.84 --> 1420.78]  I'm looking at my notes here.
[1421.68 --> 1422.98]  We got Scott McVicker left over.
[1423.06 --> 1423.40]  I'm not sure.
[1423.44 --> 1426.74]  Yeah, so, Scott, you've just got to at least say Facebook for the folks at home.
[1429.66 --> 1434.16]  I met the guys at a recent, during, what conference was it during?
[1434.94 --> 1435.36]  At Twitter?
[1435.60 --> 1436.32]  Chirp, I guess?
[1436.58 --> 1437.48]  Yeah, it was Chirp Conference.
[1437.74 --> 1438.86]  Well, let's redact that.
[1439.24 --> 1441.38]  I should mention Twitter on the Facebook podcast.
[1441.38 --> 1445.44]  So, it was at a certain unknown social media conference, right?
[1445.44 --> 1448.90]  Yeah, and they noticed that my accent's a little on the strange side,
[1449.16 --> 1451.64]  and I can't actually say the name of the company I work for properly.
[1452.24 --> 1454.04]  So, it's pronounced Facebook.
[1457.84 --> 1460.48]  So, Scott was telling me at the meetup that,
[1460.54 --> 1464.58]  maybe this is a nice segue into just general Facebook,
[1464.82 --> 1466.74]  working in slinging code at Facebook questions.
[1467.14 --> 1470.10]  Scott was telling me that you guys are all friends with Mark on Facebook.
[1470.18 --> 1470.56]  Is that right?
[1472.76 --> 1473.54]  With Zach?
[1473.54 --> 1473.62]  Yeah.
[1474.04 --> 1477.40]  I think it was like, you see him walking around,
[1477.58 --> 1479.14]  and he's very involved with the company.
[1479.26 --> 1481.62]  He doesn't like, he's there.
[1481.96 --> 1486.02]  Yeah, I mean, I think Zuck even wrote a patch for one of the features
[1486.02 --> 1489.84]  or fixing something that we were going to roll out at F8 a few weeks ago as well.
[1491.82 --> 1493.06]  So, he's still in the code, huh?
[1493.38 --> 1494.08]  Yeah, I was going to ask.
[1494.12 --> 1494.68]  Yeah, now and then.
[1496.68 --> 1499.70]  Well, it's good to have the guy at the top of the company still stinging code.
[1499.70 --> 1504.52]  Yeah, I mean, I think it really speaks to the engineering culture that we have here
[1504.52 --> 1507.04]  in terms of both what Haiping was talking about earlier
[1507.04 --> 1510.96]  in terms of being able to go try out an idea, see if it works,
[1511.14 --> 1513.84]  work with other engineers or small teams,
[1514.36 --> 1518.68]  and really the entire company and products moving forward
[1518.68 --> 1519.92]  from an engineering perspective.
[1520.92 --> 1523.86]  Our entire design team writes code as well.
[1523.86 --> 1526.54]  So, generally when we get a mock-up, it's something that you can click on.
[1526.68 --> 1529.64]  It's not just a Photoshop file that's delivered.
[1530.12 --> 1533.50]  So, I think that really has a huge impact on how we build products
[1533.50 --> 1534.68]  and how we build infrastructure.
[1535.28 --> 1536.86]  A lot of people really care about what they're doing.
[1537.06 --> 1537.78]  It shows through.
[1538.94 --> 1539.72]  Yeah, thank you.
[1540.72 --> 1541.64]  So, David, your…
[1541.64 --> 1543.72]  That was kind of a question, but a statement too.
[1544.22 --> 1547.50]  So, David, your title, I guess, is Senior Open Manager?
[1547.98 --> 1549.28]  I don't know. We made something like that.
[1549.80 --> 1551.22]  That's what your Facebook page says,
[1551.22 --> 1553.54]  and I guess at the PGA that means something totally different.
[1553.86 --> 1559.34]  Talk a minute about your role and kind of how you heard Gats
[1559.34 --> 1562.34]  or slang open source at Facebook.
[1563.16 --> 1566.76]  Yeah, I mean, I'm really focused and my team's focused
[1566.76 --> 1571.72]  on making it really easy for anyone at Facebook to use open source,
[1571.92 --> 1575.38]  to use standards, to create open source technologies, to release them,
[1575.84 --> 1579.42]  and just helping the company make sure that we do a really good job of that.
[1579.64 --> 1581.54]  And not just from an engineering perspective,
[1581.54 --> 1586.94]  but making sure that's pulled in from a marketing perspective or recruiting
[1586.94 --> 1589.66]  or even legal stuff now and then.
[1589.92 --> 1592.36]  Open source licenses are a lot of fun to go and understand.
[1593.00 --> 1597.62]  But really that fundamental goal, making open source and standards really easy to use at a company,
[1597.78 --> 1599.36]  easy to create, easy to release,
[1600.00 --> 1602.58]  going and building developer communities around them.
[1603.12 --> 1605.12]  Lots of innovation happening on the platform too.
[1605.12 --> 1607.66]  So you mentioned F8 earlier.
[1608.18 --> 1612.54]  You guys have the Open Graph and OAuth 2 that came out of the conference
[1612.54 --> 1616.56]  and have seen a number of wrappers for both emerge practically overnight
[1616.56 --> 1618.34]  for just about every language out there.
[1618.98 --> 1622.52]  Why don't you tell the folks at home what each of those aims to solve?
[1622.52 --> 1623.42]  Well, sure.
[1623.56 --> 1632.08]  I mean, so the Graph API is a really simple API that allows developers to go and interact with user data
[1632.08 --> 1634.98]  that users have given them access to.
[1635.62 --> 1638.52]  Being able to go and sort of, it's extremely restful.
[1638.76 --> 1641.24]  A lot of ideas were inspired by the FriendFeed API.
[1642.50 --> 1647.38]  And then we use OAuth 2.0 for all of our user authorization to that.
[1647.38 --> 1652.68]  So really got involved in helping drive the OAuth 2.0 standard inside of the IETF.
[1653.30 --> 1654.58]  It's really simple.
[1655.26 --> 1657.92]  If you've played with OAuth 1.0, you had to work with signatures.
[1658.12 --> 1660.56]  You had to figure out multiple types of secrets and tokens.
[1661.10 --> 1666.36]  With OAuth 2.0, it has specific flows, whether you're in a web browser, a desktop app, a phone, an Xbox.
[1667.00 --> 1668.08]  You get an access token.
[1668.50 --> 1671.84]  Then you just make API requests over SSL using that access token.
[1672.34 --> 1674.00]  So that's been going extremely well.
[1674.00 --> 1680.00]  Developers are really loving both the Graph API as well as just how much easier OAuth 2.0 is to work with.
[1680.72 --> 1687.72]  And then we also released the Open Graph Protocol, which allows you to add some basic metadata to any web page
[1687.72 --> 1695.14]  so that users can go and connect to it inside of a social graph and so that they can like that page.
[1695.34 --> 1701.70]  And that page is really represented well with a graph so that we understand what type of page is it.
[1701.70 --> 1705.06]  Is it a movie that the user is interacting with or is it a website?
[1705.28 --> 1705.98]  Is it an article?
[1706.62 --> 1710.70]  As well as some other information such as title and stuff like that that you want to know.
[1711.74 --> 1717.32]  I noticed on the Open Graph Protocol page that kind of gives the overview that one of the examples is IMDB.
[1717.66 --> 1723.14]  Have they implemented anything with Open Graph or was that just kind of a use case?
[1723.14 --> 1731.66]  Well, IMDB still has some of the meta tags that we were playing with and prototyping before F8.
[1732.30 --> 1736.02]  They're working on going and using the Open Graph Protocol tags themselves.
[1736.78 --> 1738.78]  If you check out Rotten Tomatoes, you'll see them there.
[1738.86 --> 1740.94]  If you look at CNN, you'll see them there.
[1741.38 --> 1743.04]  They're definitely starting to spread around the web.
[1743.04 --> 1752.22]  How does Open Graph compare to other technologies that are kind of similar like OEMBED or perhaps microformats?
[1753.20 --> 1756.24]  So I think microformats are probably easiest to start with.
[1757.00 --> 1763.62]  Microformats really came about by looking at how are people marking up semantic information in the bodies of web pages
[1763.62 --> 1766.06]  and trying to create some patterns around that.
[1766.06 --> 1774.78]  We're using the RDFA syntax, which is basically a way of saying like you put the quotes a little bit different than if you were using microformats.
[1775.28 --> 1780.46]  We tried to reuse the microformats H-card schema when we're talking about contact information,
[1781.04 --> 1788.36]  but really just wanted something that was dead simple for developers so that they can literally copy and paste four meta tags,
[1788.88 --> 1791.40]  place them into the head of their page and have it work,
[1791.40 --> 1798.24]  not have to go and dig into the body of the HTML, not have to worry about namespaces and different schemas to combine things together.
[1799.72 --> 1801.88]  And the other thing you asked about was OEMBED.
[1801.98 --> 1804.04]  I guess OEMBED is more, it's an API.
[1804.46 --> 1810.00]  So you go and you take something like a YouTube video page, you discover the OEMBED endpoint,
[1810.34 --> 1815.78]  and I think you actually make an API request about it, and that returns a JSON object describing some metadata.
[1815.78 --> 1821.54]  So I think the Open Graph protocol really aims to be simpler than that from a developer perspective,
[1821.98 --> 1826.86]  not having to stand up another API, not having to go and make an additional HTTP request.
[1827.54 --> 1831.80]  You know, Adam and I both make our livings and our day jobs on the front end.
[1832.42 --> 1837.00]  And just my initial take was, you know, with microformats, you know, I got excited when they first came out.
[1837.00 --> 1841.74]  But to tell you the truth, just even as someone that makes his living doing front end code,
[1841.82 --> 1844.46]  every time that I wanted to construct one, I'd have to go out and look at an example.
[1844.76 --> 1846.90]  Just, you know, it's just complex.
[1847.22 --> 1848.44]  I have the book right there next to you.
[1849.40 --> 1854.36]  I got excited when I saw Open Graph because my initial reaction when I saw the meta tags was,
[1855.34 --> 1857.72]  wow, how could we think of this sooner?
[1859.60 --> 1860.14]  Thank you.
[1860.48 --> 1862.38]  I mean, there's really a whole team of people.
[1862.38 --> 1867.62]  And I think some of this, a lot of this comes from the fact that we were working with a lot of different partners
[1867.62 --> 1872.84]  and getting feedback from large publishers on what they were willing and what they weren't willing to go and do.
[1873.30 --> 1878.80]  So, like, one of the things that we discovered is there's a link tag where it's link rel canonical.
[1879.36 --> 1883.18]  And the goal of that is that you say this is the canonical URL for a page.
[1883.34 --> 1885.70]  So the example is if you have a bunch of, like, query parameters,
[1886.32 --> 1891.78]  then a search engine can know, ignore the query parameters, this is the actual canonicalized URL.
[1891.78 --> 1893.58]  And search engines understand it.
[1893.94 --> 1897.72]  And so we were thinking of using this tag instead of the OG URL property.
[1898.20 --> 1900.36]  But when we went and started talking to some large publishers,
[1900.72 --> 1905.96]  they were afraid that adding this tag would have potentially negative effects on their search engine optimization.
[1906.48 --> 1913.20]  And so we really wanted something separate rather than having something that was tied into what they were already doing from an SEO perspective.
[1913.20 --> 1921.08]  It's about that time where we ask everybody, you know, what's on their open source radar more or less.
[1921.14 --> 1925.16]  What's out there in the open source world that's just got you excited about what you're doing.
[1926.04 --> 1927.42]  And we just kind of wanted to go around the room.
[1927.52 --> 1932.14]  I guess we can, David, if you want to lead this, you can and just kind of go in turn with whom wants to go next.
[1932.20 --> 1935.62]  But pretty much the question is, you know, what's on your radar in terms of open source?
[1935.62 --> 1936.98]  What are you just trying to play with?
[1937.84 --> 1938.96]  So what's on my radar?
[1941.18 --> 1945.62]  I guess for me, it's this...
[1945.62 --> 1954.70]  We're seeing more and more examples of how you can really use open source to go and scale large websites.
[1955.10 --> 1962.56]  And it's no longer that open source is just the text editor that you use on your computer or your mail client or only your database.
[1962.92 --> 1967.14]  But I think open source is really moving beyond that traditional LAMP stack.
[1967.14 --> 1977.96]  And you're going and seeing other technologies which are becoming really relevant in building scalable dynamic websites today that are open source that are working really well.
[1978.08 --> 1982.68]  So I guess sort of that evolution is pretty interesting to me.
[1984.46 --> 1989.40]  And I guess one question you probably gleaned over earlier, which was probably something you kind of hinted on there.
[1989.46 --> 1995.50]  But how has GitHub as part of open source impacted how you feel about open source now and where it's going?
[1995.50 --> 1997.60]  I mean, we love GitHub.
[1999.04 --> 2005.98]  It's an incredible web interface to go and manage a project, to go and browse through source code.
[2006.76 --> 2012.40]  And I think one of the most interesting things is how GitHub really went and embraced that idea of forks.
[2012.84 --> 2024.50]  So instead of saying that forks are a bad thing and trying to ignore forks, GitHub really gives you the ability to easily see who else is going and working with your code.
[2024.50 --> 2027.04]  Even if they haven't directly submitted a patch.
[2027.14 --> 2034.72]  And so that really allows us to go and see what are other people doing on a project like Tornado or on a project like 320 from a much more proactive fashion.
[2036.92 --> 2037.50]  Very cool.
[2037.64 --> 2040.34]  And I guess who would be next to answer the radar question?
[2040.42 --> 2042.80]  And if you want to answer the GitHub part of it too, you're welcome to.
[2044.64 --> 2046.18]  So I'll answer it, but I'm going to cheat.
[2046.18 --> 2055.46]  So I'm going to say I think maybe what I'm most excited about in the open source world is a couple of the projects that are still in the pipeline here at Facebook.
[2055.72 --> 2061.96]  I think there's a couple of cool things that will be out in the coming year.
[2062.32 --> 2063.28]  We love scoops.
[2063.74 --> 2063.98]  Yeah.
[2063.98 --> 2069.28]  And I mean, I agree with everything about GitHub.
[2069.50 --> 2071.76]  I think it's a great example.
[2072.20 --> 2079.00]  I mean, not only is it a really great product, but it's a great example of how you can have a space that's been around for a long time.
[2079.12 --> 2085.84]  You know, things like SourceForge and everyone kind of, or Google Code, and everyone kind of assumes that, you know, that's as good as it gets.
[2085.84 --> 2089.34]  And then all of a sudden someone comes along and does something that's just fundamentally different.
[2090.04 --> 2091.98]  And once it's there, everyone sees it.
[2092.04 --> 2094.52]  And you're like, wow, why didn't we do that sooner?
[2095.40 --> 2098.20]  So it's just a cool company.
[2101.28 --> 2105.24]  I really like the network overview on GitHub where you can see all the forks.
[2105.32 --> 2109.36]  And it's got a visualization of the branches and what commits went into the various branches.
[2109.56 --> 2111.20]  So you can, like, pull things back in.
[2111.92 --> 2112.88]  I think that's pretty awesome.
[2112.88 --> 2116.48]  Yeah, this is Owen again.
[2116.68 --> 2126.88]  And sort of related to that, the thing that's impressed me most about the open source community that's grown up around our stuff is, like, the quality of the contributions that we get back.
[2127.98 --> 2132.76]  We've gotten plenty of pull requests from people who have forked 320 in GitHub.
[2133.80 --> 2136.04]  And a lot of those we've actually integrated back in.
[2136.10 --> 2139.22]  We have at least 16 separate contributors to mainline right now.
[2139.22 --> 2144.72]  Most of them are in the form of just little bug fixes and patches.
[2146.16 --> 2148.28]  But, you know, that makes our life so much easier.
[2148.38 --> 2151.08]  Like, if someone reports a bug to 320, that's one thing.
[2151.54 --> 2155.44]  But if someone reports a bug and includes a patch that fixes it, that's even better.
[2155.92 --> 2158.44]  And that happens actually fairly often.
[2158.44 --> 2162.56]  And that's been one of the best things about open sourcing 320.
[2164.24 --> 2170.70]  Has GitHub and just having open source project profiles available impacted the hiring process over there at all?
[2172.68 --> 2173.82]  I don't know specifically.
[2173.98 --> 2174.68]  That's a good question.
[2178.00 --> 2179.04]  And that's all we get.
[2179.04 --> 2184.62]  I mean, I can make up an answer if you want me to.
[2185.62 --> 2202.12]  No, I was actually, I mean, I was interested in seeing a blog post by Matt Bidolph, who created Doppler and then sold it to Nokia a few months ago, where he was actually going and analyzing GitHub network statistics for each city, looking at who were some of the most interesting contributors.
[2202.12 --> 2205.32]  And he was using that, I believe, from a hiring perspective.
[2205.90 --> 2209.70]  So there's definitely something there if you want to play with it.
[2210.32 --> 2211.80]  Well, we certainly appreciate your time today.
[2212.30 --> 2213.78]  Anything to add before we wrap?
[2214.22 --> 2216.52]  I mean, I guess the only other thing is Google Summer of Code.
[2217.24 --> 2219.62]  We're actively participating in that this year.
[2220.38 --> 2226.80]  All three of Hip Hop, Tornado and 320, have students working on it as part of Summer of Code.
[2227.38 --> 2230.18]  So that's definitely another thing that's really exciting for us.
[2230.18 --> 2231.26]  When does that take place?
[2232.12 --> 2237.58]  So Google Summer of Code is, I think it's actually starting within the next few weeks, if it hasn't started already.
[2238.08 --> 2239.52]  It's entirely distributed.
[2239.92 --> 2251.24]  So Google goes and helps projects find college students and gives them an internship over the summer remotely to work on open source.
[2251.80 --> 2253.56]  I just pulled the page down here now.
[2253.72 --> 2254.68]  That's pretty cool.
[2255.18 --> 2255.44]  Wow.
[2256.04 --> 2256.34]  All right.
[2256.38 --> 2256.82]  Thanks, guys.
[2256.86 --> 2257.44]  We appreciate it.
[2257.44 --> 2257.92]  Yeah.
[2258.14 --> 2261.66]  And facebook.com slash open source if you want to learn more about our projects.
[2261.66 --> 2264.10]  And other stuff that's going on there.
[2264.76 --> 2265.88]  And also github.com.
[2266.12 --> 2266.48]  Yeah.
[2266.56 --> 2268.82]  Also github.com forward slash facebook as well.
[2268.90 --> 2270.38]  It's basically the same thing.
[2271.16 --> 2272.38]  But hey, thanks, guys, for coming on the show.
[2272.42 --> 2275.04]  We really appreciate all you had to share with open source.
[2275.12 --> 2279.58]  We appreciate your wisdom and standing on the shoulder of giants and out there doing what you're doing.
[2279.74 --> 2280.58]  It's super awesome.
[2280.58 --> 2281.86]  We certainly appreciate it.
[2282.64 --> 2282.86]  Yeah.
[2282.90 --> 2283.72]  Thank you for having us.
[2289.82 --> 2292.74]  Thank you for listening to this edition of the changelog.
[2292.74 --> 2300.52]  Point your browser to tale.thechangelog.com to find out what's going on right now in open source.
[2301.76 --> 2310.28]  Also be sure to head to github.com forward slash explore to catch up on trending and feature repos as well as the latest episodes of the changelog.
[2310.28 --> 2340.26]  We'll see you next time.
[2340.28 --> 2370.26]  We'll see you next time.
