[0.00 --> 17.98]  Welcome to The Change Log episode 0.2.0.
[18.28 --> 19.30]  I'm Adam Stachowiak.
[19.46 --> 20.38]  And I'm Wyn Netherland.
[20.60 --> 22.72]  We cover what's fresh and new in the world of open source.
[23.12 --> 26.80]  If you found us on iTunes, we're also on the web at thechangelog.com.
[26.80 --> 30.12]  Or for a real-time view, check out tail.thechangelog.com.
[30.24 --> 38.82]  You can also head over to github.com forward slash explore where you'll find some trending repos, some featured repos, as well as all the audio podcasts from this year podcast.
[39.22 --> 43.46]  If you're on the Twitter, you can follow Change Log Show, not The Change Log.
[43.58 --> 44.52]  And I am Adam Stach.
[44.98 --> 47.62]  And I am Penguin, P-E-N-G-W-Y-N-N.
[48.14 --> 49.30]  Awesome episode today.
[49.44 --> 56.02]  Talk to Felix Geisendorfer from Transloaded about Node.js, our favorite server-side JavaScript framework.
[56.02 --> 58.56]  Nice to see the streak has been kept alive.
[58.70 --> 59.96]  Kept alive at 20.
[60.96 --> 62.92]  Some awesome mind-bending JavaScript.
[63.10 --> 68.04]  Speaking of mind-bending JavaScript, we'll be at Texas JavaScript June 5th in sunny Austin, Texas.
[68.36 --> 73.42]  And let's not forget, we're heading to Red Dirt RubyConf, back up to the OKC Coco.
[73.74 --> 75.14]  Up to the OKC Coco.
[75.22 --> 80.82]  Actually, I think it's at the convention center, the actual conference, but I'm sure we'll stop into the Coco and see all of our compadres there.
[81.54 --> 84.32]  That's May 6th and 7th, open Oklahoma City.
[84.32 --> 85.70]  Great episode this week.
[85.74 --> 86.30]  Should we get to it?
[86.52 --> 87.20]  Let's do it.
[95.64 --> 101.00]  Hi, we're joined today by Felix Geisendorfer from Berlin to talk about Node.js.
[101.22 --> 105.52]  Felix, why don't you introduce yourself to the audience, let them know who you are and why they should care.
[106.56 --> 107.10]  All right.
[107.10 --> 112.74]  My name is Felix Geisendorfer, and I currently work a lot on Node.js, which is why I'm on the show.
[113.12 --> 115.58]  I previously did a lot of work on CakePHP.
[116.38 --> 122.96]  And, yeah, I started using Node for a project of mine where, like other technologies, were a really bad fit.
[123.24 --> 125.02]  And maybe we can talk about that a little bit.
[125.02 --> 134.06]  Well, it's kind of hard to think that anybody that's caught a single episode of the changelog would not know what Node.js is at this point.
[134.18 --> 143.08]  But for those uninitiated folks, and maybe this is their first episode, why don't you give a little background about Node.js and what problems it aims to solve.
[143.08 --> 145.20]  Oh, okay, sure.
[146.24 --> 158.12]  Well, Node, pretty much one description I read was it's the first server-side JavaScript implementation that you actually would want to use, which I think is a nice and simple explanation.
[158.86 --> 169.04]  A slightly longer version goes somewhere along the lines that you can do things in parallel with Node really easily because it sits in an event loop.
[169.04 --> 177.10]  So instead of just writing your code line by line and seeing it executed in this order, you get callbacks for everything.
[177.32 --> 184.68]  So if you want to start 1,000 HTTP requests or answer 1,000 of them at the same time, it's not a big deal because it's all event-based.
[184.98 --> 192.80]  And that makes Node kind of special from most platforms where this stuff is definitely possible but really cumbersome and not really efficient.
[194.28 --> 196.88]  So Node was created by Ryan Dahl.
[197.42 --> 197.76]  Right.
[197.76 --> 200.10]  How did you get involved with the project?
[201.20 --> 205.36]  I got involved with Node around June last year.
[205.98 --> 209.24]  I saw it a little bit earlier since that and thought it looked kind of neat.
[209.82 --> 219.62]  And then I was doing a lot of work that involved worker queues, and I was writing those worker queues in PHP and PHP daemons to process a queue, and it was really messy.
[219.62 --> 228.52]  And I was like remembering Node and how it was really easy to run comment line scripts in parallel with it, which is what I was doing a lot at that time.
[229.00 --> 235.00]  And so I tried to use it, and it worked pretty well initially, but I hit issues, and so I just started contributing.
[235.00 --> 241.74]  Because what actually made it really easy is that most of Node's API itself is in JavaScript instead of C++.
[242.30 --> 244.02]  So people can contribute easily.
[244.02 --> 249.96]  I think it's kind of funny that we've actually, I mean, I'm not sure if you actually noticed this, but this is going to be the next point release.
[250.08 --> 255.90]  The last point release was Chris Wanstrow from GitHub, and Felix gets to be episode 0.2.0.
[257.16 --> 258.46]  And that's, you know, Node.
[258.52 --> 260.28]  We've been talking about Node for such a long time.
[260.32 --> 261.02]  It's been like a streak.
[261.02 --> 265.96]  So we finally get to episode 20 of the changelog and finally have someone on to talk about Node.
[266.32 --> 266.88]  How fitting.
[267.38 --> 268.82]  It's actually even more fitting.
[269.62 --> 273.58]  The next big release of Node is also 0.2.0.
[273.84 --> 274.24]  Wow.
[275.82 --> 276.26]  Yeah.
[277.64 --> 282.40]  Yeah, and it's an important release because it's going to bring some API stability.
[283.30 --> 287.86]  So Felix, let's talk about how you got started in, I guess, in open source and in Node.js.
[287.86 --> 290.72]  What got you on this kick, and what got you excited about it to get started with it?
[291.86 --> 296.08]  Well, my story programming goes that I started fairly early.
[296.62 --> 301.04]  My dad gave me a C64 where all I wanted to do was play games.
[301.20 --> 305.90]  But if you guys know the machines, you had to type in like three comments to load the disk and start it all up.
[306.48 --> 312.08]  And I got interested in that, did like visual basic on that afterwards on the PC, got internet.
[312.22 --> 315.96]  But even after that, for a long, long time, I was really isolated from the programming world.
[316.96 --> 320.44]  And then a friend of mine introduced me to CakePHP.
[320.78 --> 322.68]  I was doing web development stuff at the time.
[322.88 --> 325.82]  And I realized that I just had been reinventing the wheel.
[326.20 --> 328.48]  I mean, I did my own kind of framework.
[328.66 --> 329.54]  I didn't call it that.
[329.54 --> 332.62]  But it was really messy in comparison.
[332.76 --> 333.96]  I was like, let's use that.
[334.58 --> 337.26]  At the same time, Rails obviously was big, and I looked at that.
[337.38 --> 339.70]  But I couldn't get it to run on my Windows machine back then.
[339.92 --> 341.86]  So that's where that decision was made for me.
[341.86 --> 346.08]  And it wasn't really like a wise technology kind of choice.
[346.08 --> 350.34]  So then I started blogging about what I was doing.
[350.58 --> 353.24]  And I was blogging a lot about CakePHP and how it sucked.
[353.78 --> 361.78]  And I guess a year into that, the people on the CakePHP team finally had enough of that and gave me a chance to contribute.
[361.96 --> 366.64]  And they were like, listen, if you're just saying what's bad, why don't you come on and help fixing it?
[366.66 --> 368.12]  And I was really interested in that.
[368.12 --> 374.96]  And I started working on CakePHP and blogging about that a lot.
[374.96 --> 378.94]  And our little blog, I'm now doing it together with my partner, Tim.
[379.34 --> 381.06]  We've written like 400 entries.
[381.44 --> 386.38]  And so that actually, I think that is an important part why open source is fun for me.
[386.42 --> 391.12]  Because if you start writing about it, you also get a lot more feedback instead of just like doing commits.
[391.94 --> 395.68]  So they're not really visible to anybody who's not deep into the project.
[395.74 --> 398.88]  So what source control system are you guys using for CakePHP?
[400.72 --> 402.52]  The longest time it was subversion.
[403.34 --> 404.58]  They now switch to Git.
[404.96 --> 407.52]  I'm not actively involved with the project anymore.
[408.22 --> 410.06]  I still do a lot of work with it.
[410.42 --> 414.30]  But I'm at the point where it really does everything I need.
[414.72 --> 416.68]  I don't hit any bugs with it.
[417.32 --> 424.28]  And going forward, the next technology I'm going to heavily invest in is going to be Node and JavaScript.
[424.28 --> 429.58]  You know, that's interesting though with more and more projects going over to Git.
[429.74 --> 434.46]  Git just makes it so easy to fork a project and apply patches to a project.
[434.68 --> 440.88]  It's almost like a put up or shut up if you've got criticism of a particular project, right?
[441.74 --> 442.06]  Yeah.
[442.22 --> 447.02]  And I guess because people can do it without asking for permission first.
[447.02 --> 451.52]  They can like go ahead, fork and do stuff and point it out to the world.
[452.02 --> 457.24]  Whereas with subversion, you could write a patch and email to some mailing list, but it wouldn't really get a lot of ice on it.
[457.24 --> 466.04]  And, well, it's also a bigger barrier because you'd have to be like – when I was using subversion, I would never email patches around.
[466.42 --> 469.04]  I knew how to use subversion, but I didn't care much beyond that.
[469.04 --> 473.90]  That's quite the leap from PHP to server-side JavaScript.
[475.70 --> 480.08]  PHP is on every Unix machine and half the Windows machines on the planet.
[481.10 --> 484.34]  Google, the V8 engine that powers Node, not so much.
[484.52 --> 492.76]  Talk a bit about how does someone get it set up with Node and the installation process and how do you get up and running?
[494.44 --> 494.88]  Sure.
[494.88 --> 494.92]  Sure.
[496.14 --> 499.82]  Installing Node is pretty easy if you're on a Linux and Mac machine.
[500.46 --> 510.34]  If not, and you're not really like a Unix hacker who can pull off like a CYG install and fix all the issues you might hit, don't try it.
[510.42 --> 511.82]  I wouldn't try it with Windows yet.
[512.48 --> 516.56]  If you're on a Linux machine or Mac, you can just download the source.
[517.54 --> 519.90]  The description on how to do that is on the website.
[520.08 --> 524.66]  Then you type in configure and make install, and it's a pretty painless process.
[524.88 --> 531.50]  There's no external dependencies, and I haven't heard of a build error on the mailing list for the last two months or something.
[532.14 --> 537.56]  So now that you've got Node set up, it's pretty easy from that point on.
[537.64 --> 544.32]  You just create your first JavaScript file, call it my.js, and then you call up the Node binary,
[544.32 --> 551.98]  which is now installed in the comment line, and you're saying node my.js, and our JavaScript code gets executed.
[551.98 --> 561.34]  If you're doing a server, which is going to be a long-running process and you want to deploy it, you're going to need some way to demonize it.
[562.12 --> 570.06]  Node might do that in the future, but for now you're going to have to use like a Ubuntu upstart script or whatever your platform has for that.
[571.02 --> 572.94]  But really running locally is very easy.
[573.24 --> 578.10]  Deploying is easy as well, but you need a little bit of sysadmin skills for that.
[578.10 --> 585.60]  For those developers out there who are, I guess, primarily client-side JavaScript hackers, maybe even some really deep ones,
[585.76 --> 591.22]  what is the biggest difference between client-side JavaScript coding and server-side with Node?
[593.44 --> 594.48]  A few things.
[594.70 --> 595.20]  Speed.
[595.56 --> 596.90]  Everything is placing fast.
[597.38 --> 604.64]  With the browsers, unless you look in Google Chrome, which is the engine that Node uses, V8, things can be sluggish.
[604.64 --> 615.58]  Another big difference is that you can use a lot of new JavaScript features that people are avoiding right now because they are not going to run in everybody's favorite browser like Internet Explorer.
[617.18 --> 628.80]  So V8 is headed for a full ECMA 5 compatibility, which is the new proposal or standard for JavaScript that got accepted a little bit ago.
[628.80 --> 632.64]  And so you can use all of those functions that V8 currently implements.
[632.86 --> 635.98]  That means like array has a native for each method filter.
[637.50 --> 643.90]  What's really cool is you have a standard JSON parser and stringifier and a few other goodies.
[644.06 --> 645.32]  I think getters and setters.
[645.96 --> 652.48]  And there's actually a page in the Node wiki which describes all the cool features that are available.
[652.66 --> 654.56]  Google, Node, and V8, I think.
[654.56 --> 658.70]  Those are definitely the biggest differences.
[659.46 --> 662.98]  And other than that, I think there's also a lot of similarities.
[663.20 --> 670.24]  Like if you're used to handling click events like on click, those same ideas apply a lot in Node because you have events.
[670.42 --> 676.22]  Like your connection coming in or some data finishing, writing, or sending, and you get a callback.
[676.40 --> 677.80]  And you just deal with the callback.
[677.80 --> 685.46]  So everything in Node is asynchronous, and a lot of things in Node glide sites are asynchronous as well.
[686.26 --> 690.94]  When you look at, I guess, kind of where Node is going now, it's still sort of fresh and young, right?
[691.38 --> 700.16]  What are some of the new things that are happening with Node, like any web frameworks or any specific templates that are coming out that makes jumping into the scene a lot easier?
[700.16 --> 717.08]  I think right now is a little difficult moment to join the scene because since Node 0.1.28, there's been a lot of backwards compatibility breaking changes.
[717.08 --> 721.64]  Those are a little painful because everybody has to update their applications.
[722.52 --> 728.10]  But they're really nice because some of the things that are enabled by them.
[728.68 --> 734.66]  I guess the biggest deal is that one concept that's really important in Node is streams, streams of data.
[734.66 --> 742.54]  Like you're having a read stream of files that you're reading in or TCP connection or standard out.
[742.80 --> 749.46]  Or you have a write stream like standard in or like an HTTP connection you're writing to or TCP your file.
[750.38 --> 755.88]  And with a standardized interface, Node will be able to build abstractions to that or users will be.
[755.88 --> 765.58]  So you can say, take the stream that's coming in here and pump it into this other stream and automatically handle buffering and all kinds of other issues you might encounter.
[766.32 --> 769.50]  So that's a place where the API is changing a lot.
[770.90 --> 773.88]  Another thing is features being added.
[775.02 --> 778.28]  There's support for Unix sockets was added.
[779.28 --> 782.94]  Interprocess communication is a big thing on the agenda as well.
[782.94 --> 785.86]  Because with Node, you only have like one thread.
[786.20 --> 792.78]  So if you're running out of CPU power, you need more processes to split it amongst multiple cores.
[793.26 --> 795.76]  And so you would start multiple Node processes that communicate.
[797.76 --> 800.04]  And I guess buffers are a big deal as well.
[800.90 --> 810.64]  You notice working on a native buffer object, which allows you to directly address memory chunks.
[810.64 --> 813.34]  Similar like you would do in a low-level language like C.
[813.88 --> 816.36]  And so you would get a buffer of a fixed size.
[816.80 --> 818.64]  And you would operate on that.
[818.80 --> 823.16]  So then on strings, which Node has previously used, but which are not really efficient.
[823.42 --> 829.26]  You know, one of the things that I hear quite a lot in the same context as Node is just how fast it is.
[829.36 --> 835.62]  Can you give the listeners any idea just how fast Node.js is and what types of tasks it does well?
[835.62 --> 835.92]  Yeah.
[836.46 --> 837.10]  Yeah.
[838.30 --> 846.44]  Node is very fast in like Hello World benchmarks, which are often used for comparing technologies.
[847.18 --> 856.66]  Simply because you have a really like low or fast path between like a connection coming in and Node being able to handle it.
[856.78 --> 859.60]  That's by design and that's an advantage over a lot of things.
[859.60 --> 866.16]  In terms of numbers, Node on them, like those are really rough numbers.
[866.30 --> 875.52]  But I guess on a machine where you would install Engine X to serve a static file and Engine X would get like 20,000 requests a second.
[875.92 --> 879.78]  I guess Node is somewhere in the 10K to 15K area.
[879.78 --> 886.36]  But you have to see that the responses sent by Node are dynamic.
[886.90 --> 898.30]  So in terms of like having a dynamic web server, there's not a lot of stuff that's fastest than Node that is not written completely in C or C++.
[899.48 --> 904.38]  Most dynamic scripting languages will be, yeah, a lot slower.
[904.38 --> 909.20]  So do you see Node shining, I guess, coupled with something like WebSockets?
[909.34 --> 911.14]  Is that really where the sweet spot is?
[913.54 --> 915.44]  Depending on what you're doing, it is.
[916.24 --> 922.42]  Everybody who is excited about real-time web technologies should definitely have an eye on Node.
[922.50 --> 924.50]  I think it's a very excellent use case.
[924.50 --> 937.72]  I've done a lot of long polling kind of stuff with Node, which is also nice because with like a PHP script, you really wouldn't want to send an Ajax request, which hangs for multiple seconds until the answer becomes available.
[938.12 --> 944.12]  With Node, that kind of thing is really efficient and you don't have to worry about thousands of those requests just hanging in there.
[947.24 --> 952.26]  Yeah, so WebSockets are definitely a big area where Node will shine.
[952.26 --> 956.70]  Talk for a minute about promises and do.
[957.06 --> 958.80]  Opinions on those.
[959.90 --> 965.52]  Yeah, that's a big thing I actually left out in the API changes.
[965.94 --> 967.24]  Node removed promises.
[967.62 --> 977.20]  For those of you who don't know what promises are, essentially whenever you call the function that was asynchronous, you would get an object returned, which we would call the promise.
[977.20 --> 982.80]  And you could send call methods on this object, which would notify you when things happen.
[982.92 --> 988.60]  So you could say promise at callback and you'd be notified when this promise has been completed.
[989.08 --> 991.82]  Or there would also be an error handler, so you could handle errors.
[993.28 --> 1000.18]  This is completely gone from Node now because everybody had an opinion on how to do it better or not.
[1000.18 --> 1006.94]  And there was at least three threads on the mailing list with close to 100 messages.
[1007.82 --> 1009.12]  And so Node removed those.
[1009.62 --> 1018.30]  We are now using simple callbacks where the first parameter is either null or the error object if an error occurred.
[1019.16 --> 1021.18]  And this makes a bunch of things easier.
[1022.46 --> 1023.86]  You mentioned the do library.
[1023.86 --> 1033.72]  So do library deals with scenarios where you have multiple asynchronous things happening at the same time.
[1034.02 --> 1036.92]  You have the callbacks for those, but you want to group them.
[1037.12 --> 1038.80]  Like you want to wait for all of them to finish.
[1039.48 --> 1044.82]  Or you want to do all of them in sequence and handle the event where something goes wrong in between.
[1046.18 --> 1048.66]  Node doesn't really come with any abstractions for that.
[1049.16 --> 1053.22]  And do looks like a really nice way to deal with those.
[1053.22 --> 1065.64]  For my code that I'm writing with Node, I usually haven't used do yet because whenever I had the need that I needed to abstract multiple things going on and group them,
[1065.98 --> 1070.48]  I was using an integer counter as a private variable to keep track of it.
[1070.76 --> 1074.90]  And that worked really well and gave me more flexibility than any abstraction would.
[1075.48 --> 1081.28]  So I guess if I would have this problem more often, then I would definitely go with do because it looks really nice.
[1083.22 --> 1087.64]  And do is from our buddy Tim Caswell.
[1087.80 --> 1089.18]  It was in episode 017.
[1090.66 --> 1090.78]  Yep.
[1091.52 --> 1095.58]  And they built the blog howtonode.org.
[1095.90 --> 1100.16]  I'm not sure if he's running do in that framework, but the open blog still fascinates me.
[1101.84 --> 1104.52]  Along those same lines with libraries like do,
[1104.52 --> 1109.52]  what's the state of package management or library sharing in the Node ecosystem?
[1112.40 --> 1115.10]  Basically, nobody's really using package management yet.
[1115.60 --> 1121.06]  And by nobody, I mean most people who are not some creators of package management software for Node.
[1122.20 --> 1124.88]  There's Isaac, who's working on NPM.
[1125.74 --> 1128.82]  And there's TJ Huichak.
[1129.04 --> 1130.84]  Or do you guys know how he's pronounced?
[1130.84 --> 1134.08]  Anyway, he's working on something called Kiwi.
[1134.68 --> 1137.08]  He's also the creator of Express.
[1137.72 --> 1143.94]  And I really haven't invested heavily in those yet because with Node's API is still moving.
[1144.30 --> 1145.26]  So things will break.
[1145.44 --> 1149.28]  And when I need to deploy and make package management part of my deployment process,
[1149.66 --> 1152.48]  that's really just another hassle to worry about at this point.
[1153.12 --> 1159.56]  So I'd say once the API settles down, both NPM and Kiwi will be really interesting to follow.
[1159.56 --> 1162.60]  So TJ's got another project called Express.
[1162.90 --> 1163.58]  Express.js.
[1163.88 --> 1169.58]  It aims to be a Sinatra-like DSL for creating apps on top of Node.
[1169.78 --> 1170.74]  Have you played with this at all?
[1173.52 --> 1173.96]  Sorry.
[1176.60 --> 1177.00]  Express.
[1177.42 --> 1179.08]  No, I have not played with it.
[1179.34 --> 1179.74]  Oh, sorry.
[1180.12 --> 1180.52]  My throat.
[1184.52 --> 1187.10]  I might have to get a glass of water in a second.
[1187.16 --> 1187.42]  Sure.
[1187.68 --> 1188.22]  No problem.
[1188.22 --> 1190.44]  Anyway, let's try Express.
[1191.64 --> 1193.70]  Express looks really nice.
[1194.52 --> 1197.04]  It seems like TJ is putting a lot of work in it.
[1198.26 --> 1200.36]  I have one big problem with it.
[1200.58 --> 1205.58]  That is, it's just taking this idea of one language, namely Ruby and Sinatra,
[1205.94 --> 1208.76]  and tries to emulate it kind of one-to-one in Node.
[1208.76 --> 1214.56]  I think most projects taking this route are not really going to feel natural in Node because
[1214.56 --> 1220.80]  all these Ruby or Python or whatever projects were written with a different programming style in mind.
[1220.80 --> 1226.60]  Another big problem is creating DSLs in JavaScript.
[1226.60 --> 1243.56]  JavaScript does not really lend itself nicely to create domain-specific languages just because you cannot easily define symbols and function names and mix them into the local scope without polluting the global scope.
[1243.56 --> 1252.20]  And so Express, as far as I know, pollutes the global scope with global methods like GET and other methods.
[1252.64 --> 1256.06]  And I think that is really something that people should avoid in JavaScript.
[1256.06 --> 1261.52]  If it wasn't for that, I would really recommend Express because it looks, TJ puts a lot of work in that.
[1261.96 --> 1270.70]  But I have a problem with anything that pollutes the global namespace in JavaScript just because it's a bad practice that we should all try to get away from.
[1270.92 --> 1276.04]  Pretty much every time Wynn jumps on my project and I don't have jQuery defined properly, he yells at me, so I'm used to that.
[1276.04 --> 1282.34]  So you haven't played with Express, but what about FAB?
[1282.42 --> 1284.08]  It's another pure JavaScript DSL.
[1284.88 --> 1287.32]  I guess everybody's got a Sinatra fetish these days.
[1287.66 --> 1288.28]  What about this one?
[1289.74 --> 1292.40]  FAB is one that I actually have played with.
[1293.02 --> 1296.64]  And I think it's really going an interesting path.
[1297.34 --> 1300.56]  Rather than trying to ban JavaScript to look like a DSL,
[1301.66 --> 1305.04]  it's pretty much on every function call, it returns a function call.
[1305.04 --> 1316.32]  And so you get a really long list of function calls, but you can indent them and the parameters are then taken into account.
[1316.52 --> 1320.84]  And it kind of looks like a definition of the sitemap of your website.
[1321.36 --> 1326.48]  You really have to see it to get a picture of it, but it looks like lists.
[1328.64 --> 1332.72]  What is really interesting about it is that it really focuses on streaming.
[1332.72 --> 1344.36]  So every node that you kind of have in your tree that defines your site is like a little application that can stream data up to the next node or down from the previous node.
[1344.50 --> 1346.74]  And you can alter the data stream.
[1347.36 --> 1350.66]  And you can also change the type of the data stream.
[1350.66 --> 1358.74]  Like you could take JavaScript objects like chasen downstream and then convert them into actual chasen strings.
[1359.30 --> 1362.04]  And then the next application gzip them.
[1362.64 --> 1371.28]  And it's really nice to see how you can create really reusable stuff with that and just chain it together in interesting ways.
[1371.94 --> 1372.64]  Yeah, that's interesting.
[1372.64 --> 1382.32]  The two, I guess, initial reactions that I've got to looking at this is it looks a lot like jQuery, which it says right there on the homepage in the chaining events.
[1382.56 --> 1389.32]  But in the other approach that you just mentioned, having these horizontal aspects, it sounds a lot like in the Ruby world what we call rack middleware,
[1389.42 --> 1395.94]  where you can just have different levels of your application kind of latch onto the responses and requests.
[1395.94 --> 1398.00]  Right, right, exactly.
[1398.24 --> 1404.90]  And there was a lot of discussion in the node and also the common chairs community on like a standard for this.
[1405.02 --> 1406.84]  I think, what's the rack standard called?
[1406.96 --> 1407.48]  Help me out, guys.
[1410.60 --> 1417.88]  I mean, either way, there's like some sort of standards that governs how rack works and how the objects looks that it passes around.
[1418.52 --> 1425.14]  And what's really not been part of the discussion until node came along was how to do this with streaming data.
[1425.14 --> 1430.60]  But I think with rack, you always have like a finished message and you pass it on to the next middleware.
[1431.06 --> 1431.50]  Right, right.
[1431.66 --> 1433.18]  And then it deals with that.
[1433.58 --> 1437.04]  But with node, you actually have the ability to take like half a message and pass it on.
[1437.52 --> 1441.40]  And the application needs to be able to deal with it every step of the way.
[1442.00 --> 1451.08]  And that is, I think, something that Fab solves really elegantly and where it's going a little bit beyond of what rack might do in the Ruby world.
[1451.84 --> 1452.24]  Interesting.
[1452.24 --> 1458.14]  So it mentions here on the Fab homepage about using it as a common JS library.
[1458.58 --> 1462.50]  What's your experience with common JS and how does it play into dealing with node?
[1465.00 --> 1468.78]  I'm not very involved with common JS itself.
[1468.94 --> 1476.84]  But since we're in the JavaScript server side world, we're talking a lot to the people that are pushing common JS.
[1476.84 --> 1477.02]  Yes.
[1477.80 --> 1484.34]  I think the node standpoint is we look at everything that common JS puts out there.
[1485.42 --> 1488.28]  And if it looks nice, we consider adopting it.
[1488.76 --> 1491.92]  But mostly node is like driven by implementations.
[1492.08 --> 1495.72]  Ryan always says implementations should drive standards.
[1495.72 --> 1510.70]  So if there's something that's like really hotly debated and the scope is limited, I guess node is the kind of libraries that goes ahead and starts an implementation, tries to look how that feels and then takes it from there.
[1511.06 --> 1513.14]  Rather than like defining a big standard up front.
[1513.14 --> 1519.68]  And so the common JS people are probably a little frustrated with node from time to time.
[1519.98 --> 1528.38]  But at the same time, it's like it's an interesting discussion between like defining standards or like implementing something and like deriving a standard out of it.
[1528.38 --> 1532.90]  We've got a couple questions coming at us from the IRC channel, actually.
[1533.16 --> 1534.56]  And one is a pretty good one.
[1534.58 --> 1536.20]  I actually think I've had this one in the past, too.
[1536.26 --> 1537.78]  It comes from a fellow.
[1537.82 --> 1538.92]  I'm not sure how you're going to pronounce this.
[1539.10 --> 1541.66]  His Twitter handle is E-T-H-N-T.
[1542.52 --> 1545.68]  I'll let you try to butcher that one since you're good at butchering names.
[1545.68 --> 1553.74]  His question is in regards to production environments, he doesn't really want to take the time to learn Node.js.
[1553.98 --> 1561.04]  But his question is if there's any hosts out there that have Node.js already on them that he could deploy to and if there's anything you could recommend.
[1563.72 --> 1564.20]  No.
[1564.60 --> 1568.24]  I am not aware of any node-specific hosting at this point.
[1568.24 --> 1580.16]  I think most people have a dedicated server or virtual machine that's a SSH into configure Node, compile it, and then push their applications to.
[1580.68 --> 1583.86]  And it's pretty much a manual process at this time.
[1584.96 --> 1590.32]  It would definitely be nice to see something like Heroku for Node in the future, but I think it's a little too early for that.
[1590.82 --> 1597.20]  Before we go too far away from the discussion we had earlier, too, we were talking about TJ and Express and all that.
[1597.20 --> 1602.74]  But he's also got a library called JSSpec and it deals with testing your code.
[1602.90 --> 1607.62]  How does that play into Node and how does Node deal with TDD and BDD kind of setups?
[1608.56 --> 1609.68]  That's a good one.
[1610.24 --> 1622.72]  With testing stuff, I find DSLs to be more compelling because I can see how they make the tests easier to structure and easier to read.
[1622.72 --> 1629.94]  I still disagree with what JSSpec does in terms of exporting global objects.
[1630.42 --> 1631.10]  I think it's messy.
[1631.26 --> 1636.62]  I think it exports a describe method and an it method and all kinds of things.
[1638.02 --> 1646.56]  Node itself, what Node does is initially it was using the test suite from V8, which is called MJSUnit.
[1646.56 --> 1657.96]  And now we're using the CommonJS testing module or their specification, which is pretty much a module called assert.
[1658.22 --> 1665.84]  And it just has assert equal or assert deep equal and a bunch of assertation message, which throw an error.
[1666.14 --> 1669.02]  So you write your test as like a plain JavaScript file.
[1669.02 --> 1673.90]  And if one of your assertations throws an error, Node exits with an error code of one.
[1674.44 --> 1679.36]  And so if you automate like your test suite, you just check if one of your tests has an exit code of one.
[1680.60 --> 1683.86]  For a project of mine, I'm also using just the assert module.
[1685.02 --> 1688.58]  I kind of like the purity of it, just like doing the minimum I need.
[1688.58 --> 1699.36]  And like a library and top of Node, which might again break with the compatibility if Node like changes API, is really just another headache for me to worry about.
[1700.54 --> 1710.16]  My personal guideline for any like third party libraries with Node is unless they have full unit test coverage and look really well written, I try to avoid them.
[1710.16 --> 1715.44]  Just because it's another part of the software I don't control and Node itself is moving fast.
[1715.44 --> 1724.84]  So in general, I might like to have something like JS spec if done a little differently in the future.
[1725.12 --> 1727.28]  But I'm also not sure if we really need it.
[1727.84 --> 1732.54]  That's because JavaScript itself lends itself nicely to unit testing.
[1733.92 --> 1739.14]  If you need like a mock object or something, you just define a JavaScript object and you attach methods to it.
[1739.14 --> 1742.96]  Or you take the original object and you just replace a method.
[1743.62 --> 1746.96]  And that all feels very natural and very easy in JavaScript.
[1747.90 --> 1750.62]  So, but the jury's still out.
[1750.88 --> 1756.10]  I don't think a lot of people in the past had to deal with testing stuff that's asynchronous.
[1756.82 --> 1764.12]  It really changes how tests look because the indentional level goes a lot deeper than it would go for test suits usually.
[1764.12 --> 1768.68]  Usually you just have one like indentional level with assets, maybe an if statement.
[1769.70 --> 1772.94]  But asynchronous testing is still pretty new land.
[1773.32 --> 1778.24]  And I stick with the purest form which is using the asset module and Node right now.
[1778.62 --> 1780.64]  But going forward, who knows what comes up.
[1781.76 --> 1785.32]  You know, in the changelog, Adam and I are big Hamil and SAS fans.
[1785.32 --> 1790.68]  And so I think we've covered multiple ports of Hamil to JavaScript.
[1791.72 --> 1793.52]  Both Hamil.js and JSHAMIL.
[1793.66 --> 1794.72]  I've seen SAS.js.
[1795.66 --> 1797.98]  What are you using for your markup?
[1798.80 --> 1802.24]  I would imagine Mustache would be suited for this sort of thing.
[1802.32 --> 1803.42]  What do you use in your projects?
[1805.38 --> 1808.10]  Well, my main project does not output any HTML.
[1808.66 --> 1810.76]  So it's a problem I don't have.
[1810.76 --> 1815.22]  For some client consulting I did, I actually set up Mustache.
[1815.58 --> 1817.38]  Because I think it's a nice approach.
[1817.70 --> 1821.94]  And I think I was using Jan Leonard's implementation of it.
[1823.34 --> 1825.70]  Hamil, I like.
[1825.88 --> 1827.98]  I used Hamil a little bit in Ruby before.
[1829.02 --> 1834.38]  I'm just not convinced of the quality of Hamil.js implementations out there yet.
[1834.52 --> 1837.68]  Because most people think like, hey, it's easy to parse the syntax.
[1837.92 --> 1839.64]  But then it turns out it isn't.
[1839.64 --> 1844.64]  And you have to debug a parser or compiler, which is not fun.
[1845.74 --> 1849.70]  So Mustache is what I use right now, which I find good.
[1850.28 --> 1853.26]  So if you're not returning a front-end markup, are you returning JSON objects?
[1854.00 --> 1854.56]  Yeah.
[1855.06 --> 1859.82]  The project just has a web service API, and it's all REST and JSON.
[1860.36 --> 1863.74]  So what sort of projects are you working on with Node.js?
[1863.74 --> 1871.48]  The main project that got me into Node and that I'm still heavily working on is called Transloaded.
[1872.34 --> 1879.00]  It's basically a service for people who want to outsource their file uploading and video encoding
[1879.00 --> 1881.98]  and don't want to deal with that on their own boxes at all.
[1881.98 --> 1890.26]  We give them a jQuery plugin, and their form submit events are hijacked, and we take their files to our machines.
[1890.44 --> 1895.20]  We show an upload progress bar, and then we encode the videos and upload them to S3.
[1895.20 --> 1904.92]  Where Node really shines here is that a lot of the stuff we do is call up command line scripts once we've received the upload.
[1905.58 --> 1910.90]  So we have, at any given moment, like 20 or 30 command line tools running side by side,
[1910.98 --> 1914.76]  and it's all just one Node process managing them and handling their events.
[1914.76 --> 1925.56]  With any other kind of technologies, we would have to write workers where we'd have one worker working on one command line tool execution
[1925.56 --> 1927.42]  because that's usually a blocking process.
[1928.76 --> 1931.28]  The other thing where Node is really nice is file uploading.
[1932.46 --> 1937.38]  One of my earliest contributions to Node was actually a multi-part parser,
[1937.84 --> 1940.88]  which has now been replaced by a better one that Isaac wrote.
[1940.88 --> 1948.14]  And so in Node, you can actually receive a file upload and handle every byte as it comes in.
[1948.22 --> 1953.74]  It's a stream of data, and you can choose to write it to disk or first inspect it before you write it to disk.
[1954.38 --> 1958.92]  And that is nice to us because we can kind of look at authentication information.
[1959.56 --> 1962.50]  That's one of the form fields that's being submitted to us.
[1962.80 --> 1967.02]  And if this doesn't match, we can abort an upload which might take an hour for a big video
[1967.02 --> 1970.28]  and notify the user of a problem right away.
[1970.88 --> 1978.68]  And that kind of flexibility is what I really enjoy in Node and I guess why I started using Node initially.
[1979.18 --> 1981.92]  So you're going to be speaking at JSConf coming up, right, Felix?
[1982.82 --> 1983.06]  Yep.
[1983.52 --> 1984.86]  Got your topic picked yet?
[1985.82 --> 1986.24]  Yeah.
[1986.46 --> 1988.46]  The topic is called Node Dirty.
[1989.60 --> 1994.26]  Node Dirty is like a fun project that just came to me one day.
[1994.40 --> 1997.62]  I was thinking about what kind of stuff you could do with Node.
[1997.62 --> 2004.68]  And one thing I came up with, you could write like a key value store because it seems fashionable these days.
[2005.36 --> 2008.78]  And I started playing around with a few ideas.
[2009.06 --> 2011.42]  And what came out of it is called Node Dirty.
[2012.22 --> 2021.28]  And what it basically does is it tries to not do the things that all the other databases being relational or NoSQL suck at.
[2021.28 --> 2023.78]  And that usually is abstraction.
[2024.68 --> 2026.20]  Abstraction itself is not bad.
[2026.50 --> 2033.34]  It just means that you have to learn some sort of interface and some sort of like thinking model to access your data.
[2033.78 --> 2039.48]  And I think that's really a barrier to your data rather than like helpful unless you know it really well.
[2039.48 --> 2042.52]  And this other thing is networking.
[2044.38 --> 2048.48]  I guess the more decent data stores out there have decent networking code.
[2048.48 --> 2059.24]  But where they still fail is that a typical application has to send multiple requests over the network to generate its page or whatever it's doing with the data.
[2059.92 --> 2065.12]  And then aggregates its results and compiles them to some HTML on the client side.
[2065.12 --> 2071.10]  And I think the networking is a really big bottleneck, especially if you go for high write performance.
[2072.10 --> 2076.58]  And so what Node Dirty does, it does no abstraction and it does no networking.
[2077.04 --> 2081.80]  So all you get is a little database object with a get and set method.
[2082.48 --> 2090.12]  Whenever you set a key and a value, it's directly written to an append-only JSON file.
[2090.94 --> 2092.56]  It's just newline-separated JSON.
[2092.72 --> 2095.00]  So that's really simple about it.
[2095.80 --> 2096.86]  And you get a callback.
[2097.24 --> 2099.24]  So callback fires when the data has been written.
[2099.74 --> 2102.90]  But even before the data has been written, it's already in memory.
[2103.24 --> 2110.24]  So if all you care about is having the data in memory, you could return to the client that it's done right away.
[2110.24 --> 2112.00]  Or you could wait for the disk persistence.
[2112.58 --> 2117.86]  So that enables something that most data stores don't allow you.
[2117.86 --> 2125.22]  They either go for full consistency or they give it up for eventual consistency or all kind of ways you can spin the cap theorem.
[2125.22 --> 2132.76]  And with Dirty, my hope is kind of that you can choose what model applies the best depending on your situation and current data set.
[2133.48 --> 2138.70]  And people would use it to build their own databases that are actually applications.
[2138.70 --> 2148.06]  It would be applications that directly contain the business logic and use something either Node dirty or something like that as an underlying mechanism.
[2148.06 --> 2153.12]  I think that's a really interesting use case for Node.
[2153.12 --> 2163.36]  Because now you can write all your business logic in JavaScript and just provide a nice JSON interface, REST interface, that answers business questions.
[2163.80 --> 2165.58]  Rather than abstraction questions.
[2165.68 --> 2169.44]  Rather than doing a query or some sort of mapper to use.
[2169.44 --> 2174.90]  You just directly ask your database a business question, which I think is what databases should answer.
[2175.32 --> 2177.76]  And all the abstractions happen internally.
[2178.48 --> 2188.34]  So your current query API is basically a get by ID or a filter where you essentially pass it a function much like you would if you were filtering an array in JavaScript or jQuery, right?
[2188.92 --> 2189.26]  Right.
[2189.78 --> 2193.00]  The filter thing is just to get people started.
[2193.00 --> 2199.26]  Once you get into millions of records that won't perform anymore for a few reasons.
[2199.26 --> 2201.52]  One of them is Node just has a single thread.
[2202.12 --> 2206.98]  So if you filter over a million records, nothing will happen until you looped over all of them.
[2209.06 --> 2216.02]  So once you go for bigger data sets, you probably want to update some fuse or caches every time the set method is called.
[2217.36 --> 2227.14]  I'm currently thinking about either providing an explicit plugin system to make those things happening or just overwriting the set method and monkey patching it.
[2227.14 --> 2228.92]  But I dislike that a little bit.
[2229.10 --> 2231.02]  So I'm still working on that.
[2231.82 --> 2232.80]  So no dirty.
[2232.96 --> 2233.54]  Get set and filter.
[2234.40 --> 2234.88]  No dirty.
[2234.98 --> 2236.02]  No sequel for the little man.
[2236.08 --> 2238.40]  Is that the title of the talk at JSConf?
[2239.60 --> 2242.34]  I'm changing the sub-slogan from time to time.
[2242.46 --> 2243.76]  But no dirty is the title.
[2245.16 --> 2245.36]  Gotcha.
[2245.36 --> 2253.00]  At this point, really, just to clarify that it's mostly a fun project and I'm seeing how far it can be pushed.
[2253.12 --> 2260.52]  I think it's going to be a nice way to store data, especially for prototyping, especially to keep your moving parts in the stack low.
[2260.78 --> 2264.80]  If it's really going to make an impact for high-performance stuff, I don't know.
[2264.80 --> 2270.54]  I'm doing some benchmarks that look very, very promising, but I don't work on high-performance site.
[2270.62 --> 2271.50]  It's part of my day job.
[2271.62 --> 2276.50]  So I can only go by what all the cool kits publish and what their problems supposedly are.
[2277.54 --> 2279.68]  I'll hopefully get some feedback at the conference.
[2280.50 --> 2284.24]  And that question was from, I believe, Chris Williams' Voodoo Tiki God on Twitter.
[2284.24 --> 2290.56]  Let's talk a bit, before we hit the radar, Felix, about the development scene in Berlin.
[2290.74 --> 2294.86]  What's it like to be a code slinger in Germany?
[2297.68 --> 2299.34]  It's pretty nice.
[2299.44 --> 2302.88]  I think Berlin has the biggest startup scene in Germany.
[2303.58 --> 2307.38]  I don't think it's anywhere near Silicon Valley, Bay-ish area.
[2307.84 --> 2310.24]  But there's a lot of interesting stuff going on.
[2310.24 --> 2316.94]  Jan from KarchDB are there, and I started hanging out with those guys a little bit.
[2317.18 --> 2328.40]  They started actually a Travis Group user group in their co-op, and I did one talk on Node there,
[2328.44 --> 2330.36]  and there's been a lot of excellent other talks there.
[2331.64 --> 2338.68]  And, yeah, I mean, whatever your technology is, you will find lots of people in Berlin to talk with them.
[2338.68 --> 2344.02]  There's a lot of events, and as far as the tech scene in Germany goes, I think Berlin is where it's happening.
[2346.18 --> 2351.58]  So I guess the common question we ask to close off the podcast is, you know,
[2351.62 --> 2353.50]  what's on your radar in terms of open source software?
[2353.66 --> 2360.82]  What's out there, I guess, besides Node that you're just dying to play with that's just got you really excited about open source and what you're doing?
[2360.82 --> 2368.94]  My April Fool's was I'm quitting open source, but that's not going to happen.
[2369.32 --> 2371.26]  So what else is on the radar?
[2372.82 --> 2378.52]  I really am liking Ruby, and I would like to do more with it.
[2378.52 --> 2385.98]  I don't have, like, client work or any other time that I could spend on it.
[2387.04 --> 2391.62]  I really hope that Node will be able to do everything Ruby is being used for right now,
[2391.72 --> 2393.74]  but that's still, like, multiple years off.
[2394.00 --> 2398.28]  So if I happen to have some time, I'll definitely play more with Ruby.
[2398.28 --> 2404.48]  And I guess any Node projects that come up.
[2404.76 --> 2408.76]  But other than that, I'm mostly looking at the JavaScript stack at this point.
[2409.88 --> 2410.32]  Cool.
[2410.42 --> 2413.94]  And before we close off, you mentioned earlier a startup you're working on.
[2414.00 --> 2418.52]  Can you plug that URL so that the listeners who didn't hear it clearly can go there and check it out?
[2419.12 --> 2419.52]  Right.
[2419.88 --> 2423.04]  It's called transloaded.com.
[2423.04 --> 2429.00]  That's T-R-A-N-S-L-O-A-D-I-T.com.
[2429.90 --> 2433.54]  And I assume you're on Twitter, too, so what's your Twitter handle is?
[2433.74 --> 2434.70]  Felix E, is that right?
[2435.68 --> 2436.96]  Felix G-E.
[2437.70 --> 2442.88]  Well, thanks, Felix, for taking the time on a late Friday evening over in Berlin to chat with us.
[2443.00 --> 2443.98]  Really appreciate it.
[2443.98 --> 2450.44]  Now we can maybe put the Node.js streak to bed on purpose maybe next episode.
[2450.84 --> 2452.98]  I don't know about you, man, but I'm going to sleep well tonight.
[2453.04 --> 2455.72]  Knowing that we've talked about Node.js so much.
[2455.82 --> 2461.48]  And finally, our second point release, episode 20, is going to have a full-featured episode of Node.js.
[2461.62 --> 2462.00]  It's awesome.
[2462.50 --> 2462.84]  Well, cool.
[2463.26 --> 2464.18]  Let's wrap there.
[2464.32 --> 2466.64]  Felix, anything else you want to mention before we head out?
[2467.48 --> 2468.24]  Sure, yeah.
[2468.52 --> 2471.78]  I want to thank you guys for the opportunity to speak here.
[2471.78 --> 2480.40]  I want to just say that Node is, like, I'm spending a lot of time on it, but the really big man behind Node is Ryan.
[2480.54 --> 2483.14]  He's, like, working day and night to make it awesome.
[2483.34 --> 2493.22]  And I guess if somebody who hasn't contributed to open source before wants to contribute to something, Node gives you the opportunity to use your JavaScript skills.
[2493.22 --> 2495.46]  There's a lot of stuff to help out with.
[2495.60 --> 2497.76]  Just hop on the IRC channel.
[2498.38 --> 2499.60]  Check the GitHub issues.
[2499.60 --> 2508.36]  If you need any help with stuff, people are around to help you, and we love everybody's contributions.
[2508.92 --> 2509.16]  Cool.
[2509.52 --> 2509.98]  Thanks, Felix.
[2510.22 --> 2511.02]  We'll chat at you soon.
[2511.24 --> 2512.18]  Yeah, thanks for having me.
[2512.18 --> 2521.34]  Thank you for listening to this edition of The Changelog.
[2522.38 --> 2529.10]  Point your browser to tale.thechangelog.com to find out what's going on right now in open source.
[2530.30 --> 2538.88]  Also, be sure to head to github.com forward slash explore to catch up on trending and feature repos as well as the latest episodes of The Changelog.
[2542.18 --> 2572.16]  The Changelog.
[2572.18 --> 2574.18]  The Changelog.
[2574.18 --> 2576.18]  The Changelog.
