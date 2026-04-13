[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com and we're hosted
[11.42 --> 17.34]  on Linode servers. Head to linode.com slash Changelog. This episode is sponsored by our
[17.34 --> 22.18]  friends at Rollbar. How important is it for you to catch errors before your users do? What if you
[22.18 --> 26.80]  could resolve those errors in minutes and then deploy with confidence? That's exactly what Rollbar
[26.80 --> 31.60]  enables for software teams. One of the most frustrating things we all deal with is errors.
[32.08 --> 37.70]  Most teams either A, rely on their users to report errors or B, use log files and lists of errors to
[37.70 --> 43.28]  debug problems. That's such a waste of time. Instantly know what's broken and why with Rollbar.
[43.64 --> 49.04]  Reduce time wasted debugging and automatically capture errors alongside rich diagnostic data
[49.04 --> 53.78]  to help you defeat impactful errors. You can integrate Rollbar into your existing workflow.
[53.78 --> 58.26]  It integrates with your source code repository and deployment system to give you deep insights
[58.26 --> 63.66]  into exactly what changes caused each error. Give Rollbar a try today at no cost to you.
[63.94 --> 69.72]  No credit card is required. Our listeners get access to the Bootstrap plan with 100,000 events for free
[69.72 --> 74.46]  for 90 days. To get started, head to rollbar.com slash Changelog.
[74.46 --> 95.28]  Welcome to JS Party, a weekly celebration of JavaScript and the web. Tune in live on Thursdays at 1pm US
[95.28 --> 101.26]  Eastern at changelog.com slash live. Join the community and Slack with us in real time during the shows at
[101.26 --> 106.72]  the changelog.com slash community. Follow us on Twitter. We're at jspartyfm. And now onto the show.
[109.72 --> 114.72]  Hello and welcome to another episode of JS Party where it's a party every week with JavaScript.
[115.38 --> 120.32]  I'll be your host today, Nick Neesey, and I'm joined with my fellow panelists, Suze Hinton. Hey, Suze.
[120.62 --> 122.16]  Hey, how's it going? It's good to be back.
[122.60 --> 126.24]  Good to be back with you as well. And our other panelist is Jared Santo.
[126.24 --> 133.24]  Hello. Excited to chat with y'all. Dev tools, debugging, fun stuff.
[133.78 --> 138.56]  Yeah, lots of fun and very practical for everyone. So let's dig right into it today.
[139.12 --> 144.50]  We thought we'd talk about debugging and some dev tools magic and kind of how we approach
[144.50 --> 152.08]  that part of the job of developing with JavaScript and how we manage bugs or deal with bugs and
[152.08 --> 160.34]  some cool features that the platforms provide us. So I guess I'll start off with a basic question.
[160.90 --> 168.44]  How do you use, how do you get into debugging? Like you have a bug that you don't really know
[168.44 --> 172.38]  much information about. What are kind of the first steps that you take? Why don't we start with you,
[172.76 --> 172.96]  Suze?
[173.50 --> 180.02]  Yeah, I start super, super basic. So usually when I'm developing something that's more on the front
[180.02 --> 185.02]  end side in the browser, I'll usually just have dev tools popped up at the bottom, like always on
[185.02 --> 190.10]  showing the console tab. And then whenever I'm sort of developing a feature and sort of manually
[190.10 --> 195.16]  testing it, I'll usually just look for an error. And then if the error shows up, which it usually
[195.16 --> 200.80]  does, right, because we're not all perfect the first time when we code something, if the error is
[200.80 --> 205.76]  super, super obvious and there's like a line of code, then I'll just go straight back to my code
[205.76 --> 210.24]  and fix it. But if it's something that I don't know what it is, generally I'll Google it really
[210.24 --> 214.82]  quickly first. And if I don't really find anything that's specific to my case, that's when I sort of
[214.82 --> 221.00]  start digging deeper and deeper. And so what I love about the dev tools in every single browser that I've
[221.00 --> 225.56]  worked with is that it gives you the line number, you can generally click on the error and it will take
[225.56 --> 231.04]  you to that source code. And then that's where I'll set a break point and start stepping through,
[231.48 --> 235.60]  you know, refresh the page and start stepping through. So mine definitely starts super high level.
[235.76 --> 242.54]  Because I find that even though being able to kind of pause your page execution and step through
[242.54 --> 249.22]  those, those parts of your code, that's very time consuming. And sometimes it's super not necessary
[249.22 --> 254.40]  if it's a really, really simple problem. So that's kind of how I start like super high level and sort
[254.40 --> 260.76]  of go deeper from there. Yeah, that's really good. That's kind of how I start to I'll start really high
[260.76 --> 268.40]  level. Usually with if it's not an obvious thing, I might put console log statements in there and
[268.40 --> 273.96]  start going that way. And then eventually dig into actually the full blown debugger and stepping
[273.96 --> 277.70]  through code. How about you, Jared? Do you have any particular approach that you take?
[278.98 --> 285.18]  Well, I think all the technical, like the technical aspects of what I do change based in kind of the bug
[285.18 --> 289.54]  itself and you know, the environment in which I find it. But I mean, I do the first thing that
[289.54 --> 293.94]  every developer does is I start pointing fingers at other people, right? So like, could it be the
[293.94 --> 298.82]  browser vendors that did this? Could it be my dependencies that are causing me issues? I mean,
[298.82 --> 303.28]  maybe Apple made this laptop really poorly. And that's why it was not working right.
[303.28 --> 310.92]  So after I've exhausted all of my potential, you know, get blames at other people, then I turn to
[310.92 --> 318.82]  myself and I look inward and I find where the bugs truly come from. So in terms of the actual thing
[318.82 --> 325.70]  that I do, I mean, I'm pretty lame. And I've always been very much an alert debugger in terms of like,
[325.74 --> 331.60]  you know, usually like in the old days, we'd use the actual alert function and like we'd see object
[331.60 --> 336.26]  object and think, Oh, that wasn't very useful. But I've very much been a trace debugger my whole
[336.26 --> 344.04]  career in terms of like just out, you know, console logging. And I, I never set a breakpoint,
[344.14 --> 350.40]  almost never, unless I'm like super stuck. But I just put trace statements in until I can kind of
[350.40 --> 357.64]  chase down the source of what's going on. And that usually does it. Now, like Suze, I will start
[357.64 --> 363.62]  very high level. And I'll try to first determine, you know, what is the actual bug? Because lots of
[363.62 --> 368.24]  times we see symptoms. And those aren't like, it's kind of like a root cause analysis, right?
[368.70 --> 373.16]  And sometimes you get to that really quickly. Especially if it's a bug that you can kind of
[373.16 --> 377.30]  intuit what's happening right when you see the symptom. But lots of times there's red herrings
[377.30 --> 380.50]  and things that you think are happening, but it's actually something else.
[380.50 --> 388.00]  And so you can't really fix a bug until you identify it, isolate it, and make sure that
[388.00 --> 393.64]  it's actually causal and not just symptomatic. I don't know the word is for being a symptom,
[394.30 --> 398.74]  but it would have made me really smart if I would have drilled that. Is it causal or symptomatic?
[399.94 --> 400.72]  Symptomatic maybe?
[400.98 --> 403.52]  Yeah, I don't know. Just making up words over here.
[403.52 --> 409.98]  Yeah, isolation, identification, right? Once you have an actual diagnosis, and that's where
[409.98 --> 417.40]  I usually will use tracing tools to come to that, then, you know, fixing it is a whole
[417.40 --> 419.78]  other aspect of the job.
[420.16 --> 427.58]  Sure, yeah. So I do run into a lot of issues with that. Like, I will start with the kind
[427.58 --> 433.36]  of trace debugging, as you mentioned, and start going down that route. But sometimes I get
[433.36 --> 437.82]  thrown into projects that I really have no idea of what's actually going on. Maybe I'm just
[437.82 --> 444.14]  like hired as support to come in and try and diagnose one specific bug in a codebase I don't
[444.14 --> 451.02]  know or do other things. And so I've been trying to get really efficient at isolating the bugs and
[451.02 --> 458.28]  isolating where things could be occurring, and then trying to set up the traces, you know,
[458.28 --> 463.08]  just in that piece of code instead of the whole entire codebase and getting smarter about that.
[463.08 --> 467.92]  And that can be the big challenge. And especially with how complex JavaScript has
[467.92 --> 473.74]  gotten in recent years with all of the build tools and webpack and source maps and all of that can be
[473.74 --> 480.46]  really hard to find, you know, the bug is actually online 8,000 of this single JavaScript file and
[480.46 --> 487.14]  stepping in through there. But it can be a lot of fun, too. I a lot of times like to think of myself as
[487.14 --> 492.78]  like Dr. House standing in front of the whiteboard trying to figure out what the diagnosis is,
[492.84 --> 497.16]  crossing off a bunch of them. It's never lupus. And just continuing on from there.
[498.48 --> 499.82]  It's never lupus.
[501.26 --> 506.24]  I feel like there's a pun coming on there with lupus and like something about JavaScript loops
[506.24 --> 507.26]  or something like that.
[507.26 --> 510.62]  Oh, man, that would be so clever if I had thought of that.
[512.70 --> 519.58]  So some things that I'll do to try and get in there is I will use the console statements,
[519.72 --> 526.20]  but I will also use the debugger and try and pause the debugger when the error comes. And if
[526.20 --> 532.28]  you're really lucky, you'll be able to just set that pause on errors setting in Chrome or Firefox,
[532.28 --> 537.46]  and it will just pause on the line that is going to throw an error. But oftentimes, it seems like
[537.46 --> 543.90]  the errors are being caught. And so you have to enable that checkbox to tell it to break on
[543.90 --> 549.44]  caught errors as well. But the problem is, as you learn a lot of library code throws errors that are
[549.44 --> 556.28]  caught. And so you like if your bug is several thousand lines down, and there's a lot of library
[556.28 --> 561.20]  code that's running in the meantime, there might be a lot of caught bugs. And you might have to step
[561.20 --> 569.74]  through that 100 times before you get there. So do you have any tips or tricks that you use to
[569.74 --> 571.98]  kind of help speed that process up?
[572.52 --> 578.82]  It's going to have to be used to. Like I said, I use rudimentary tools and methods in my brain.
[580.90 --> 584.48]  So I don't really have tips and tricks. I do have, I mean, when I say I do the tracing,
[584.48 --> 590.76]  this kind of gets further down our timeline or our outline when we talk about
[590.76 --> 597.32]  dev tools tricks that we like. And one that I use all the time, in combination with console.log,
[597.90 --> 603.30]  instead of stopping the world is printing the state of the world at a specific point in the code.
[603.50 --> 609.14]  And then in the console, you can right click on that output and say store as temporary variable
[609.14 --> 612.96]  or something along these lines. Yep. And it will just like assign it to a temp one.
[612.96 --> 617.46]  And now you're, you know, you have an object or you have a function reference and you can
[617.46 --> 622.98]  manipulate it there and kind of dive down and, you know, run a function on it again or do what
[622.98 --> 627.96]  you have to do. And so it's kind of a combination of, I'm not stopping the world, but I'm like
[627.96 --> 633.22]  peeking into it at a specific point and able to manipulate it. And so it's like logging plus
[633.22 --> 637.40]  store as temporary variable or basically like my left hand and my right hand. But that's,
[637.48 --> 639.56]  I don't think that's necessarily good advice. It's just what I do.
[639.56 --> 646.18]  I was just gonna say, that's great advice. Being able to, to do that. And that is most of the time
[646.18 --> 650.92]  when I step into a debugging session, it's just because I want to figure out what the state of
[650.92 --> 656.88]  something is and to go from there. I'm not usually updating the state as I'm debugging or, or anything
[656.88 --> 661.90]  like that. So that's, that's a really cool thing. And kind of following along those lines of
[661.90 --> 669.54]  a cool tip, I guess, is using console logs to actually output the values of a variable.
[669.56 --> 673.06]  Obviously you can do that, just say console log and put the variable name in there.
[673.58 --> 678.76]  But one cool thing with ES6 is if you wrap it in curly braces and just put that out there,
[678.84 --> 682.92]  it will output an object where the name of the variable is the key and then the value is the
[682.92 --> 689.22]  value. So instead of having to like put the value name, comma, the, the value itself, you can just
[689.22 --> 692.34]  kind of do that all in one statement just by, by using that shortcut.
[692.34 --> 696.90]  That is a cool idea. I've never done that. Is that like using, what's that, that term,
[697.18 --> 701.26]  the new feature, like decompression or D what's the word? Destructuring?
[702.58 --> 707.52]  Kind of the opposite of that, where if you have a, you want to create an object where the key is
[707.52 --> 712.62]  the value, the name of the value that you're putting in there, you can just wrap it. You don't
[712.62 --> 715.94]  have to say like foo colon foo. You can just put foo in there.
[715.94 --> 721.20]  And it will take the variable name and assign that as the key value in an object. And the,
[721.20 --> 725.82]  the, the, the value in the variable will be the value. Is that what you're saying?
[725.98 --> 727.80]  Right. Yeah. Okay. That's cool.
[728.12 --> 731.76]  Hey, Nick, do you know if you can pass that directly to console.table?
[732.24 --> 737.38]  Ooh, uh, that's a good question. Honestly, console.table is something that I always think
[737.38 --> 742.32]  I should use and I never really think about it in the moment. Uh, but every time I see an
[742.32 --> 744.00]  example of it, I'm like, wow, that's so cool.
[744.00 --> 749.80]  Yeah. It makes good for animated GIFs and images on Twitter, but I've, every time I try to use it,
[749.84 --> 754.66]  like the, the data is not in the format that table would make it make sense. And it ends up being
[754.66 --> 758.04]  like munged. And then I was like, why am I doing this when I could just console log it?
[758.48 --> 765.98]  Yeah, that's, that's a, a cool thing. There's also a, uh, a really cool, um, feature of,
[765.98 --> 772.76]  I think just Chrome dev tools specifically, but in the same way that Chrome, uh, like console.table
[772.76 --> 781.10]  allows you to, um, see like a, a tabular, uh, display of the data. So you see columns and rows
[781.10 --> 786.74]  showing all of that. So it's easier to consume. You can actually create those, uh, those types of
[786.74 --> 794.14]  logging for the, the, um, console in Chrome yourself. And so, uh, I'll, I'll add a link to
[794.14 --> 800.84]  the show notes, but one example I've seen is, um, being able to plot out, uh, coordinates and then,
[800.84 --> 806.60]  uh, or so you can say console dot plot or something and name it yourself. And when you
[806.60 --> 810.68]  output that to the console, instead of just seeing like X, Y coordinates, you can actually like
[810.68 --> 815.40]  output a graph that plots those on there. Like that's just a really simple example, but you could
[815.40 --> 820.44]  do other things where you maybe take a geographic coordinates and then show a map of where that is
[820.44 --> 824.84]  in the console. That's really advanced. Uh, I haven't done anything like that, but I've seen
[824.84 --> 829.98]  articles. Yeah, exactly. A lot of these things are like, like awesome features, but then in
[829.98 --> 834.66]  practical day to day, I just never even like, it doesn't cross my mind to even try. Yeah. So
[834.66 --> 841.52]  kind of moving into, uh, that section, um, what are some of your favorite dev tools, tips and tricks?
[841.52 --> 846.38]  I always get so much out of, uh, talks and presentations like this because there's just so much that,
[846.38 --> 851.42]  uh, is there that I know I don't use that I probably should be using. So do you have any
[851.42 --> 856.52]  cool tips and tricks? Uh, Suze, do you want to start? Yeah, I, I really like styling console
[856.52 --> 861.40]  output. Like if you're not in the kind of breakpoint setting mood and we sort of talked about how
[861.40 --> 866.92]  sometimes that's not always the optimal solution and just outputting a ton of traces is, is really
[866.92 --> 871.16]  going to answer all your questions, being able to style the console output. So you're not just
[871.16 --> 878.00]  fishing through lines and lines of logs that all look the same, um, is really, really cool. And so
[878.00 --> 884.86]  you can use this kind of string interpolation to like CSS style, um, the actual, um, text that comes
[884.86 --> 889.54]  out in the console log. So you can change the color of it, the size of it, um, and do all sorts of other
[889.54 --> 894.68]  really, really cool stuff. And I think that that's not necessarily always known about, but if you are,
[894.76 --> 899.28]  you know, fishing through traces, it can really help you pull out the things that, that matter the most.
[899.28 --> 903.06]  That is really cool. I didn't realize that you could do that, but you can do things like
[903.06 --> 909.22]  pretty much anything in CSS with that, right? Yeah, pretty much, which is kind of fun. And I've
[909.22 --> 914.88]  definitely popped open the dev tools like on, um, just general websites I've been surfing and
[914.88 --> 921.64]  sometimes it will dump out, you know, like a, a very, very styled, um, bunch of logs that
[921.64 --> 926.14]  are saying something like we're hiring devs or something like that. So I've seen people do some
[926.14 --> 931.92]  pretty fun stuff with it. That is cool. Yeah. Wow. Very cool. That was exactly the use case I was
[931.92 --> 936.56]  considering was, was, you know, Easter eggs and stuff like that, where you, where it actually
[936.56 --> 941.38]  makes sense to take the time and style it to look really cool was when you're trying to, you know,
[941.42 --> 945.64]  find, have somebody find it, um, where it could be useful if you have lots of traces, like you said,
[945.68 --> 950.12]  but other than that, um, there could be a lot of yak shaving going on if you're spending lots of
[950.12 --> 954.68]  times just styling the output of your console logs. It could also be really interesting for like,
[955.30 --> 960.68]  uh, maybe long running log messages that could be in development and stripped out in production.
[961.08 --> 966.70]  Uh, that's not something that I normally do either, but, um, you know, maybe having specific events
[966.70 --> 973.32]  that are fired in like a bold font or, or a certain color that are always there during development to
[973.32 --> 978.46]  help you out. That could be really cool. And it kind of an easy, um, dev tools extension that you add
[978.46 --> 983.96]  to the code yourself. Yeah, totally. I know that debug, um, the module that's usually used with
[983.96 --> 988.62]  node JS, um, you know, console applications is super, super popular. And that's because it just
[988.62 --> 993.82]  does add a little bit of style and it sort of color codes the timestamps and things like that. So
[993.82 --> 999.44]  I'm imagining that you could do something very similar, but have it pretty lightweight. And so
[999.44 --> 1004.44]  when you are working with teams, you can actually switch that on during your development phase.
[1004.44 --> 1011.12]  Mm-hmm. So is that like a node module that you, you install and it gives you special, um,
[1011.56 --> 1014.08]  log statements for node or, uh, what is that?
[1014.72 --> 1019.54]  Yeah, it's, it's really cool. Actually, it does work in the browser. So if you look it up, um, on NPM,
[1019.54 --> 1025.18]  uh, in the registry, it does actually, it is able to be used in the browser as well. And so
[1025.18 --> 1029.60]  there's screenshots of it there, but what it essentially allows you to do is instead of using
[1029.60 --> 1036.60]  console log, um, you import it and you can create these different, um, I guess, scoped or
[1036.60 --> 1042.50]  get different context debug, um, logs. And so you don't just have like a generic console.log,
[1042.50 --> 1048.64]  you can have different contexts. So maybe you have some events that file with a certain style
[1048.64 --> 1053.70]  and keyword attached to it. And then maybe, um, you have a different debug context with,
[1053.70 --> 1059.40]  you know, using a different variable name to log it out where it, it, you can style it differently.
[1059.40 --> 1063.84]  And it's like non event based logs, for example, and I'm doing a terrible job of explaining it,
[1063.84 --> 1069.62]  but what I love about the debug module is you can actually, um, you know, create different instances
[1069.62 --> 1073.92]  of it and then style it differently depending on what you're actually logging out.
[1074.32 --> 1079.18]  Oh, wow. Very cool. I looking at the screenshot for it. I think I've definitely seen this in action,
[1079.18 --> 1085.46]  uh, but never actually used it. Yeah. And a lot of the time it is actually already being used in a
[1085.46 --> 1089.38]  lot of popular node modules you might be using. It's just that you have to turn it on with like
[1089.38 --> 1093.04]  an environment variable. And then you'll start seeing like the inner workings of that node module
[1093.04 --> 1098.20]  start dumping things out. So it's very useful when you, you are actually maintaining a module and you,
[1098.42 --> 1102.56]  and you can tell people to turn that on if they raise an issue on your GitHub repo or something like
[1102.56 --> 1106.74]  that, just so you can get some extra diagnostics from them. That's a great idea. It looks,
[1106.74 --> 1111.94]  looks really helpful. Yeah. I use it a lot because I, I maintain some super finicky
[1111.94 --> 1117.52]  libraries. Um, and I need to know the exact order that certain things are happening in.
[1117.52 --> 1122.08]  And instead of having a copy paste steps of code for people to run, it's way easier to tell them,
[1122.16 --> 1126.52]  Hey, can you just turn this on and dump the actual output into, you know, a comment on,
[1126.62 --> 1132.56]  on this issue. That's a great idea. And probably an example of where trace tracing specifically is,
[1132.60 --> 1136.68]  is quite a bit different for library authors than it is for application developer
[1136.68 --> 1141.36]  and probably even a different, uh, Nick, maybe you can speak to this with larger teams versus
[1141.36 --> 1148.10]  smaller teams. Um, where in every small team that I've worked on, like we use log statements to
[1148.10 --> 1152.62]  figure out a problem and then we purge them because they're, cause they're noise and unnecessary
[1152.62 --> 1158.14]  in, in like in code, uh, a library author, like you said, you want all those trace statements to
[1158.14 --> 1163.36]  exist as part of the software and maybe use all the log levels or whatever flags you need
[1163.36 --> 1168.34]  in order to, you know, use that for other people using your library debugging. So that's such a
[1168.34 --> 1172.40]  great implementation of saying, just run this again with this particular variable. And then,
[1172.40 --> 1176.88]  you know, you're, you're basically doing recon without them having any effort. That's spectacular.
[1177.32 --> 1181.02]  I've also seen in large teams where there's like trace statements similarly to what I would think
[1181.02 --> 1184.88]  in a library, but they just kind of live in the code at all times. And they're either commented
[1184.88 --> 1191.38]  out or they have log levels. And, um, that offends my personal sensibilities. It's like,
[1191.38 --> 1195.10]  get that out of there, but I see if it's a huge app and you have these recurring problems,
[1195.18 --> 1199.46]  you want to just leave, leave them there. Is that something you're, you see a lot, Nick is
[1199.46 --> 1205.58]  projects where there's like logging specifically applications where there's logging that's like
[1205.58 --> 1211.52]  integrated into the app and is always there. Yeah, definitely. Um, in some of the apps that I
[1211.52 --> 1218.42]  read, I don't typically add that. Um, and it's stripped out at like at build time, uh, as,
[1218.42 --> 1224.44]  as part of the build process, but, um, yeah, I've definitely seen that, uh, like additional
[1224.44 --> 1230.18]  information about like network requests is, is a big one. I think that I, I can recall. So, um,
[1230.52 --> 1236.24]  some, some cool dev tools, things that I've seen, um, that, that are really helpful. And I'll be honest,
[1236.28 --> 1243.20]  a lot of these dev tools, uh, tips really seem like they would have been really amazing before we
[1243.20 --> 1248.62]  started building all of our code and, um, and having complex build processes. Uh, but there are
[1248.62 --> 1255.34]  still some really good, uh, tricks to do, uh, with that. And one of them is black boxing, uh, and
[1255.34 --> 1261.06]  Firefox and Chrome both support this where you can, while you're stepping through code, uh, or you can
[1261.06 --> 1267.30]  set up a regular expression, uh, in the dev tools itself. And you can say that any script that has like
[1267.30 --> 1276.92]  jQuery in its name or, uh, this specific script, uh, this specific version of react, um, just black
[1276.92 --> 1280.68]  box that. And what that means is that when you're setting, when you're like stepping through code,
[1280.68 --> 1286.88]  uh, and you're looking at the stack trace, uh, in the right side, right-hand side, uh, don't ever show
[1286.88 --> 1292.14]  react in that stack trace. Just assume that that code is perfect and working, even though that might
[1292.14 --> 1297.56]  not be the case. Um, just assume that that is working and that I think the bug is actually in
[1297.56 --> 1302.46]  my code. And so it will save you a lot of time, not having to step through or, or look up the,
[1302.46 --> 1306.74]  the stack trace through all of your library code. And you can just focus on the code that you've
[1306.74 --> 1312.28]  written, uh, or a specific library that you're bringing in and using. It also will prevent it from,
[1312.28 --> 1317.70]  uh, stopping on errors inside of those files that are black boxed. So it'll just kind of stick to
[1317.70 --> 1322.02]  errors that are in your code and not anywhere else. So that can really help you to
[1322.02 --> 1326.80]  cut down on the amount of information that can be thrown at you when you're in a debugging session.
[1327.24 --> 1328.14]  That's so nice.
[1328.62 --> 1331.86]  Love it. And I had never even heard of that. So thank you very much.
[1332.14 --> 1338.16]  Yeah. Yeah. There's a lot of really cool little tricks like that. Um, it can be hard to,
[1338.44 --> 1343.48]  well, the nice thing about Chrome right now, uh, at least as if you do set up black boxing like that,
[1343.54 --> 1347.10]  uh, it'll actually put a little message at the top of the stack trace that says there are some
[1347.10 --> 1350.94]  scripts that are black box. So click here if you want to actually see those, and then you can
[1350.94 --> 1356.16]  right click on those and unblock box them if you like. And, uh, then they'll just be part of the
[1356.16 --> 1361.10]  flow again. So, uh, pretty easy to manage now. I think it was a little bit more difficult, uh,
[1361.10 --> 1365.00]  in the earlier iterations of that, but pretty easy right now.
[1365.16 --> 1371.50]  That's really cool. Cause I have the memory of a goldfish. And so whenever I'm, whenever I'm using
[1371.50 --> 1377.00]  the debugging tools, I try so hard not to check too many boxes where I'm just going to completely
[1377.00 --> 1383.40]  forget the really kind of like artisanal bespoke state I've put my teftels into. So it's good to
[1383.40 --> 1387.90]  know that I, it sounds like I'm not the only one with that problem and Chrome have done a good job
[1387.90 --> 1391.18]  at kind of making those little call outs to reset it back.
[1391.58 --> 1395.78]  Side note, when you said you had the memory of a goldfish, I thought you were going to then tell
[1395.78 --> 1400.22]  us about this memory that you have of a goldfish that you maybe you owned when you were a child.
[1400.22 --> 1403.80]  I was like, where is she going with this?
[1407.30 --> 1409.12]  Never heard that phrase before, but I like it.
[1409.12 --> 1411.86]  So what do you have Jared? Uh, tell us a cool trick.
[1411.86 --> 1418.84]  In terms of tips and tricks. So as I confessed to earlier, I'm very much a console.log plus
[1418.84 --> 1423.42]  right click and store as temporary variable person. That being said, there are a few other
[1423.42 --> 1428.34]  things I use all the time. And these are the kind of tips that you either know and you're rolling
[1428.34 --> 1432.64]  your eyes out right now, or you haven't heard and you're like, mind is exploding, but, um,
[1432.64 --> 1437.52]  they're very basic. Um, specifically there's shorthand references to specific things inside
[1437.52 --> 1443.72]  the dev tools, uh, dollar sign zero will, will refer to the element that is currently focused
[1443.72 --> 1448.10]  in the elements panel, which is super useful for grabbing a handler to something and then,
[1448.10 --> 1454.10]  um, running some code against it. And then dollar sign underscore in the console will, um,
[1454.10 --> 1458.12]  pull up the last return statement. And it's basically a reference to the previous return
[1458.12 --> 1462.44]  statement. So those are small little things, but once you know them, you'll use them all
[1462.44 --> 1467.22]  day, every day. And then the other thing I do a lot is in the elements panel specifically
[1467.22 --> 1473.84]  is, uh, you can drag and drop the elements to reorder the DOM. And again, either, either
[1473.84 --> 1477.24]  you just haven't tried yet and you're like, Whoa, you can do that. Or you roll in your eyes.
[1477.24 --> 1480.64]  Yeah. I've been doing that for years. It's not a new thing, but it's super useful, especially
[1480.64 --> 1486.86]  when you have maybe like a CSS specificity problem, or you didn't necessarily do the design,
[1486.86 --> 1492.44]  but you're wanting to change the HTML and wonder, can I put this div, uh, inside this other thing
[1492.44 --> 1496.96]  without screwing up any of the styles? Well, you can actually just drag and drop the elements
[1496.96 --> 1501.62]  right there in the page into the, you know, in and out of the tree in order to determine
[1501.62 --> 1506.04]  if it's going to look different or something like that. So I use that daily, daily. And then
[1506.04 --> 1510.84]  one kind of aspirational feature, which I haven't used yet, but it's super cool. And I just learned
[1510.84 --> 1517.12]  about recently and I want to use is that you can actually generate a screenshot of a single
[1517.12 --> 1522.76]  element. So instead of the full page or even a section of the page or dragging the thing around
[1522.76 --> 1528.16]  it, um, you can select an element in the elements panel and then use command shift P or I think it's
[1528.16 --> 1535.30]  control shift P on windows to bring up that little menu executor thing. And inside there,
[1535.30 --> 1540.44]  there's a menu item called capture node screenshot, and this might be Chrome only, but I'm not sure
[1540.44 --> 1546.42]  because I haven't tried it in the other, um, browsers. Hopefully not. And that will take a
[1546.42 --> 1551.78]  screenshot of that specific element as it exists right now in the page and then store it to your
[1551.78 --> 1558.02]  downloads folder or what have you. And that sounds very useful. I just haven't actually done it
[1558.02 --> 1561.18]  besides trying it, but it could be useful.
[1561.18 --> 1566.34]  I wonder if you could use that with puppeteer. Oh yeah. To automate like some snatching of
[1566.34 --> 1571.12]  specific elements. Yeah. To keep like a patent library refreshed or something like that.
[1571.44 --> 1576.22]  Hmm. That's a great idea. Yeah. That's a really good idea. Did you two know about that one or have
[1576.22 --> 1581.40]  you used it before? It was news to me until just like a week or so back. As you were talking,
[1581.48 --> 1589.78]  I just tried it and it's really cool. There you go. I did not know about it. Cool. Another one that I
[1589.78 --> 1597.52]  really like is, um, conditional, well, sorry, conditional and DOM break points. Uh, so conditional
[1597.52 --> 1605.14]  being the ability to, uh, only stop on this code. If you, if some condition is met and I actually don't
[1605.14 --> 1611.28]  use it for that. I use it for, uh, logging. If like, if I just want to add logging to a page that
[1611.28 --> 1617.26]  maybe I don't have actually downloaded, uh, I will add a conditional break point and then just put a
[1617.26 --> 1621.40]  console.log statement in that conditional break point. And what it'll do is it'll hit that
[1621.40 --> 1627.84]  console.log out and that returns falsie. And so it won't actually break there, but you can continue
[1627.84 --> 1632.62]  on and just add incremental logging as you need it, uh, to see things without actually changing the
[1632.62 --> 1637.82]  underlying source. That is a total lifesaver. You know, you know, when you're just constantly
[1637.82 --> 1645.34]  refreshing and it's maybe a situation where you can't always, uh, faithfully reproduce it.
[1645.34 --> 1651.64]  That is huge. I actually didn't know you could do that. And you know, when it always pauses on the
[1651.64 --> 1655.64]  break point and you get really annoyed and you have to like click forward and it feels so
[1655.64 --> 1663.04]  unproductive, I'm totally going to use this. Yeah, definitely. Uh, it's a big help if you are running
[1663.04 --> 1667.96]  into, uh, some kind of race condition, uh, because like you said, if you actually hit the break point,
[1667.96 --> 1673.50]  it pauses JavaScript execution right there. And then maybe things have settled by the time you
[1673.50 --> 1679.66]  start executing again and, uh, you won't be able to reproduce the bug in, in that, in that sense. But,
[1680.12 --> 1686.38]  um, if you're able to add logging in, uh, you know, sometimes you can, can glean more information
[1686.38 --> 1690.20]  about that without actually having to stop the, the execution of the JavaScript.
[1690.56 --> 1691.52]  I love that.
[1691.86 --> 1696.42]  Yeah. Then the other one I mentioned is a DOM break points. And this is really cool. If you have
[1696.42 --> 1701.22]  something on the page that, um, is being updated, but you don't really know what part of the code
[1701.22 --> 1707.18]  is updating that. So maybe, uh, it's the color of a button or it's the text inside of this div or
[1707.18 --> 1714.14]  something like that. You can, uh, right click on the element in the dev tools and then say break on.
[1714.50 --> 1719.16]  And there's a couple of options. There's subtree modifications. So if, uh, any of its children are
[1719.16 --> 1724.76]  updated, attribute modifications, if any of its attributes are modified, or if the node is removed,
[1724.76 --> 1731.28]  uh, and it will stop on the line of JavaScript that, uh, caused the modification to happen to that
[1731.28 --> 1736.04]  element or to its children. And then you can look up the, look at the stack trace and see, uh, maybe
[1736.04 --> 1741.54]  what part of your code triggered that node removal or, or modification, which can be really helpful.
[1741.54 --> 1746.24]  If you have no idea about the code base and you're just trying to, to get in there and quickly find,
[1746.24 --> 1748.90]  uh, where, where things are going wrong.
[1748.90 --> 1754.94]  That is super cool. Cause like, what would you have to do normally to like emulate that at your
[1754.94 --> 1758.82]  debugging? Would you have to do like a mutation observer or something like that would be super
[1758.82 --> 1763.54]  annoying to set up? I'm, I, I really want to try this out as well. I didn't know it existed,
[1763.54 --> 1765.26]  but I haven't had a good use case yet.
[1765.64 --> 1770.50]  Yeah. I think you could do it with a, um, with a mutation observer. Uh, but this,
[1770.50 --> 1774.24]  this is definitely much simpler to, to help figure that out.
[1774.24 --> 1780.06]  Another, uh, thing that's kind of related to that, although not really is you can, uh,
[1780.82 --> 1786.48]  by you, you can pass a, an element to a method on the console called get event listeners,
[1786.48 --> 1790.12]  and it will print out all of the event listeners that are set up on that element. So if it has a
[1790.12 --> 1797.24]  bunch of click events or, um, other types of events, you can, uh, get a list of those,
[1797.24 --> 1802.46]  and then you can right click on those and say, show in source. And it will go to that function that,
[1802.46 --> 1806.86]  that is the event listener callback. And then you can see what's actually being called.
[1807.12 --> 1810.68]  Can you just pass in window or something? Like, can you get all of them?
[1811.06 --> 1812.02]  That's a good question.
[1812.32 --> 1815.62]  Cause that would blow my mind. Cause I've had that question plenty of times. Like I want to know
[1815.62 --> 1821.46]  all of the things that are listening and what functions are going to, Oh dude, you just made my
[1821.46 --> 1826.18]  day. I did not know this. I need this in my life.
[1826.62 --> 1831.64]  Yeah. So it returns an object back and the keys are the events that are being listened for. So like,
[1831.64 --> 1835.66]  I'm just doing it on stack overflow right now. And there's a hash change event, key download,
[1836.06 --> 1840.98]  message, resize, all bunch. Well, we can go home now. I'm happy.
[1840.98 --> 1844.70]  We've accomplished what we came here to accomplish.
[1845.42 --> 1848.06]  I feel like we all learned something from each other.
[1848.06 --> 1859.56]  This episode of JS party is brought to you by hired. One thing people hate doing is searching
[1859.56 --> 1865.50]  for a new job. It's so painful to search through open positions on every job board under the sun.
[1865.50 --> 1871.50]  The process to find a new job is such a mess. If only there was an easier way. Well, I'm here to
[1871.50 --> 1878.20]  tell you there is our friends at hired have made it. So companies send you offers with salary benefits
[1878.20 --> 1882.92]  and even equity upfront. All you have to do is answer a few questions to showcase who you are
[1882.92 --> 1888.30]  and what type of job you're looking for. They work with more than 6,000 companies from startups to large
[1888.30 --> 1893.80]  publicly traded companies and 14 major tech hubs in North America and Europe. You get to see all of
[1893.80 --> 1899.40]  your interview requests. You can accept, reject, or make changes to their offer even before you talk
[1899.40 --> 1904.02]  with anyone. And here's the kicker. It's totally free. This isn't going to cost you anything. It's
[1904.02 --> 1907.44]  not like you have to go there and spend money to get this opportunity. And if you get a job through
[1907.44 --> 1912.24]  hired, they're even going to give you a bonus. It's normally $300, but since you're a listener of
[1912.24 --> 1917.66]  JS party, they're going to give you $600 instead. And even if you're not looking for a job, you can refer
[1917.66 --> 1926.52]  a friend and hired will send you a check for, get this $1,337 when they accept the job. As you can see,
[1926.52 --> 1931.30]  hired makes it too easy. Get started at hired.com slash JS party.
[1940.98 --> 1951.64]  All right. So what are some cool things that JavaScript can do that maybe aren't really
[1951.64 --> 1958.32]  apparent to others or some really cool, I guess, going along with the line, the topic of tips and
[1958.32 --> 1963.56]  tricks, things that JavaScript, the language can do. Jared, do you want to start off there?
[1964.20 --> 1973.86]  Sure. Yeah, absolutely. And this segment, I've internally named JS can do that. And I like that
[1973.86 --> 1979.38]  because that's how I read. If you guys have seen the VS can do that.com website where they basically
[1979.38 --> 1983.42]  show off VS code can do that, I guess not VS can do that, where they show off stuff that Visual
[1983.42 --> 1990.74]  Studio code can do. Every time I see that, I read it can do that. And so every time I see it, I'm just,
[1991.28 --> 1997.62]  so that's, so that's a side note. So what are some things that are not apparent, but you can do? So
[1997.62 --> 2003.54]  here's one that I learned relatively recently, and I think it's ES6 anyways. So it wouldn't have helped
[2003.54 --> 2010.56]  to know it previous to that. But we now have the spread operator, as you all know, the ellipsis,
[2010.66 --> 2017.56]  the dot, dot, dot, which has a couple of, a couple of things that it does. But one of those things is
[2017.56 --> 2025.56]  it allows you to basically expand an array into another one. And so if you combine that with sets,
[2026.08 --> 2031.70]  which is a, I think that's a relatively new class. Not sure, showing my ignorance a little bit there.
[2031.70 --> 2038.56]  Yeah, they're both from ES6. They're both ES6. Okay. If you combine those together, you have a really
[2038.56 --> 2046.00]  quick hand way of uniqueifying an array. So this is something that happens to me often, I'll have a,
[2046.08 --> 2053.90]  an array of elements, maybe it's a bunch of dates, like date objects. And there's possibilities that
[2053.90 --> 2059.58]  there's duplicates in there. And maybe the user has clicked the same thing twice, or however it
[2059.58 --> 2065.70]  happens, they have merged two arrays together. And now I have a array with some overlaps. And it'd be
[2065.70 --> 2071.68]  nice to have a dot unique function, I believe like low dash and libraries like that will have a dot
[2071.68 --> 2078.12]  unique. But without those things, it's kind of a previously been a pain to just say, okay, given this
[2078.12 --> 2083.78]  an array, I want to uniqueify it. However, if you use the spread operator, let's say you have an array
[2083.78 --> 2090.22]  called, I'll get the most creative name foo. So you have an array called foo. And foo has,
[2090.50 --> 2096.32]  you know, five elements in it. If you want to uniqueify that array, you can basically create a
[2096.32 --> 2102.74]  new set and pass the array to the set. So the set, the array is instead is what you're passing to the
[2102.74 --> 2109.14]  set constructor. And a set has to have unique elements. That's part of what sets are. So there's
[2109.14 --> 2115.62]  no duplicates and sets. And that will give you a set of unique elements, but you didn't want a set,
[2115.70 --> 2119.80]  right? We started with an array, want to finish with an array. So that's where the spread operator
[2119.80 --> 2126.64]  comes in. So if you pass the spread of that set into an array, it basically converts it back.
[2127.42 --> 2132.70]  So I'll put the actual code, I guess, in the notes, as I'm describing it orally here, and it's
[2132.70 --> 2137.92]  sounding ridiculous in my brain. So that way you can look at it. But it's like this really cool
[2137.92 --> 2144.06]  shorthand where you can basically uniqueify an array by passing a set with a spread operator,
[2144.28 --> 2148.52]  combining those two together. I've used that recently. And I thought that is neat. I didn't
[2148.52 --> 2156.18]  know JS could do that. Last one for me, this one's really brief, but use it all the time.
[2156.22 --> 2161.64]  Anytime you have a bunch of like, or a singular falsie value, you know, like those things that
[2161.64 --> 2168.26]  aren't false with a capital F, but they're falsie like null undefined empty string zero,
[2168.44 --> 2173.50]  I believe. Although I might get into some of the JavaScript words there is zero true. I can't
[2173.50 --> 2178.80]  remember. Anyways, if you have those, it is false. Very good. So zero things that are falsie,
[2179.00 --> 2186.08]  but you don't have the actual Boolean value. Uh, you can use the bang bang operator,
[2186.08 --> 2192.98]  which is also fun to say. And that will basically, uh, convert it into Boolean. So the same thing on
[2192.98 --> 2198.12]  the true side, if you have something that's truthy, but you actually want true, if you do bang bang,
[2198.12 --> 2204.08]  and then the variable, uh, it's a double negation and it will Booleanize it and then convert it.
[2204.56 --> 2210.20]  And so you can go from falsie to false. And that's nice to have. And so those are my two things that
[2210.20 --> 2215.94]  JS can do that hopefully, uh, if you didn't know, now, you know, Jared, I just have to ask a
[2215.94 --> 2222.20]  very serious question when you're using that operator. Uh, do you actually blurt out bang bang?
[2222.86 --> 2225.42]  If you were working in an office, would everybody just look at you?
[2226.08 --> 2230.24]  I don't blurt it out, but I definitely say it in my head every single time.
[2231.62 --> 2240.24]  I love that. I feel like I do do that. I do say it kind of goes, there's that song bang bang. Um,
[2240.24 --> 2245.70]  that like opens up kill bill. Is it share? I think it's share. Potentially. I know Quentin Tarantino
[2245.70 --> 2249.96]  as a fan, cause there's a version that's very kind of chilled out and it opens up kill bill,
[2250.04 --> 2254.64]  I believe. And, uh, it's a spectacular song. So I do think of that as well.
[2254.76 --> 2260.78]  It makes me think of that. Um, I don't know whether this is an American or an Australian ad,
[2260.88 --> 2263.40]  but the, um, easy off bam cleaner.
[2264.02 --> 2266.18]  What? Easy off bam cleaner.
[2266.54 --> 2272.02]  Yeah. It's called easy off bam. And their tagline is bam. And the dirt's gone. And I'm just thinking
[2272.02 --> 2278.52]  like bang bang and the fake bullion's gone. You should start an advertisement for this feature.
[2278.98 --> 2283.70]  Anyway, that's what I thought of. Uh, report real time feedback from the chat room. Uh,
[2283.70 --> 2290.26]  apparently the bang bang song is by Nancy Sinatra, not by Cher. Maybe there's another Cher cover.
[2290.66 --> 2296.40]  Oh, possibly very popular. Very good song. Yeah. And I also did a search for it. And the first thing
[2296.40 --> 2303.92]  that came up was Jesse J and Ariana Grande and Nicki Minaj. So, uh, all generations are welcome.
[2304.54 --> 2309.26]  There you go. So Suze, on your list of things that JS can do, you have binary literals,
[2309.52 --> 2312.62]  which I don't even know what that is. So please, uh, school us.
[2312.90 --> 2316.64]  Yeah. I was like really excited, but also frustrated to find out that I think this has
[2316.64 --> 2323.10]  been a feature since ES 2015. And so I felt like I was super, super late to the potty,
[2323.10 --> 2329.62]  but only finding out about it. So, so, uh, JavaScript supports things like, um, by sort of bites,
[2329.68 --> 2335.42]  I guess, in hexadecimal format. Um, and it's, it's supported that for a really long time. And,
[2335.42 --> 2340.58]  and so some of you might know that I write a lot of JavaScript hardware libraries and just
[2340.58 --> 2347.54]  general projects with JavaScript hardware. And so using, um, hex in JavaScript is pretty common for me,
[2347.54 --> 2354.24]  um, in order to kind of send op codes and things like that to hardware. Um, but sometimes you just
[2354.24 --> 2360.90]  want it to be in the full binary format. So, you know, instead of, um, you know, instead of having
[2360.90 --> 2367.84]  like FF as the hex code, you can actually have like eight ones in a row, right? I'm pretty sure
[2367.84 --> 2375.44]  that's 255. Someone correct me if it's not. Um, and so that is so convenient to have that. And then
[2375.44 --> 2381.16]  the way that you write it out is you have zero B and then you write your bits from there. And it
[2381.16 --> 2385.96]  doesn't just support like, um, you know, eight, eight bits, it supports like longer than that. So
[2385.96 --> 2393.32]  it's pretty cool. Um, I really needed it recently when I was, uh, working on a steganography project
[2393.32 --> 2399.68]  where I was trying to encode messages in images. And then I was trying to then decode the message back
[2399.68 --> 2405.42]  out of the images. And because you're working with like a bit at a time, um, using hexadecimal
[2405.42 --> 2411.30]  is actually really frustrating and, and having to, you, you kind of have to write the bits out in
[2411.30 --> 2417.54]  string format and then somehow figure out like a function to then convert that properly back into
[2417.54 --> 2422.80]  a hex code. And so that's now unnecessary. And I wish I'd known about it earlier.
[2422.96 --> 2424.60]  Oh, you need a time travel device.
[2426.66 --> 2430.22]  Where did I put that time travel device and go back and teach yourself that,
[2430.30 --> 2433.30]  or you can go back and listen to this episode past you.
[2433.30 --> 2435.86]  Yeah. I haven't, I like Jared, I hadn't really
[2435.86 --> 2441.20]  heard or understood what these were. Uh, but is this like specifically like being able to write,
[2441.28 --> 2447.06]  like, um, if you wanted to write like two 55 in binary, you could do zero B and then eight ones.
[2447.06 --> 2448.72]  Is that what you're talking about?
[2449.10 --> 2454.94]  Yes, exactly. Rather than having to do like zero X F F. And then that's really the only sort of,
[2455.02 --> 2457.64]  I guess, like that's the closest you can get to actually representing
[2457.64 --> 2461.10]  something that you can manipulate with bit shifting and things like that.
[2461.74 --> 2462.98]  Oh, very cool.
[2463.64 --> 2467.86]  So you can actually like, you know, because like not all of us are that great at being able to
[2467.86 --> 2471.72]  flip flop between, you know, looking at a hex number and knowing approximately what that is
[2471.72 --> 2476.46]  in bits. And so having it spelled out, like, I guess that's the point of a binary literal,
[2476.46 --> 2482.04]  like actually seeing it all of the ones and zeros is super helpful even when you're debugging,
[2482.04 --> 2486.20]  but even just being able to reason about your program. Um, because especially when you're
[2486.20 --> 2491.28]  doing bit masks and things like that, you don't have to wonder what exactly was that bit mask
[2491.28 --> 2495.38]  that I'm using. You can literally see them all laid out, you know, next to each other,
[2495.38 --> 2496.76]  which is kind of amazing.
[2497.82 --> 2502.68]  Interesting. Yeah. That would be really helpful. Fun side note. Uh, I think one of the very first
[2502.68 --> 2507.26]  things that kind of got me into programming was a book on steganography that I got when I was in
[2507.26 --> 2515.06]  high school and it's just a really cool field. Yeah. I, I just feel like I was it when I was a
[2515.06 --> 2520.58]  kid, I was really into like, um, cryptography and things like that, um, and ciphers and all that kind
[2520.58 --> 2526.30]  of stuff. So I got really excited just because I had books similar to that, but not steganography
[2526.30 --> 2531.94]  ones. And so steganography kind of makes me feel nostalgic about, you know, hiding data and
[2531.94 --> 2533.40]  encoding and things like that.
[2533.40 --> 2538.42]  Yeah. I just think it would be so fun to do like ultimate Easter eggs with stuff like that,
[2538.46 --> 2546.18]  like hiding things. I don't know. But speaking of, uh, bitwise operations, um, one of the,
[2546.18 --> 2549.44]  the cool JS can do that, uh, tricks that I had involved.
[2549.90 --> 2550.44]  You said it wrong.
[2550.86 --> 2552.00]  JS can do that.
[2552.20 --> 2552.74]  There you go.
[2552.74 --> 2563.28]  Uh, one of my, um, cool tips, I guess is, uh, using the bitwise operator, which is
[2563.28 --> 2569.64]  the, the tilde symbol on your, on your keyboard. Um, and specifically using that with, uh,
[2569.64 --> 2578.08]  something like index of to basically convert that to, uh, a, a, uh, truthy, falsy value
[2578.08 --> 2582.88]  for finding something in an array. Because like, if you used index of, and the thing that
[2582.88 --> 2588.60]  you're looking for is the at index zero in the array, well, that would return falsy, but
[2588.60 --> 2594.10]  the, I don't fully understand what it does, but the bitwise operator, um, shifts that so that,
[2594.10 --> 2599.84]  uh, it would actually be one and the negative one, uh, that would be returned. If nothing was found
[2599.84 --> 2606.04]  will be shifted into zero. So that will return falsy. Um, it's not something that I typically use
[2606.04 --> 2610.20]  a lot, unless I'm just like quickly trying to do something, uh, like a quick example,
[2610.20 --> 2614.84]  because it's not the most, um, accessible code in terms of obscure.
[2614.84 --> 2621.24]  Yeah. But it's a cool quick trick, but we also have better APIs in ES 2015 to handle that. There's
[2621.24 --> 2628.20]  a find method, uh, that you can use on arrays to return or a find index, uh, that will allow you to,
[2628.20 --> 2634.72]  uh, run a function. And if it returns true at any point, then that means that whatever exists in the
[2634.72 --> 2639.18]  array and you don't have to specifically be looking for the index and then figuring out if it's not
[2639.18 --> 2645.62]  negative one. Right. Totally. I see the tilde used in a very similar fashion when working with hardware,
[2645.62 --> 2650.42]  where we don't have those nice APIs. And a lot of the time what you have is C. And so it is really,
[2650.42 --> 2657.96]  really a nice trick to get stuff into like a zero or one or, you know, just trying to be able to treat
[2657.96 --> 2663.90]  it as a true ball, which is really cool. So can you bang, bang, bang, bang, bang, bitwise index of,
[2663.90 --> 2671.66]  wouldn't that work? Oh man. Yeah. And that would return true or false. Wow. Um, the other cool trick,
[2671.66 --> 2679.52]  uh, that, that also kind of came out of ES 2015 is, uh, the, um, destructuring. So specifically
[2679.52 --> 2687.54]  array destructuring in this example, where you can say like const a, uh, BC inside of square brackets
[2687.54 --> 2692.38]  equals this array. And it will take the first three values from that array and put those into those
[2692.38 --> 2696.82]  variables. So then you can access them just through those variables. And that's really helpful for
[2696.82 --> 2703.38]  avoiding having to say like, Oh, you know, this array sub zero is this, and this array sub one is
[2703.38 --> 2708.94]  this. And having that all over, it kind of lets you better name the variables and use those names
[2708.94 --> 2713.16]  throughout so that your code is more legible. And one really cool trick that you can do with that
[2713.16 --> 2721.00]  is, uh, combine that with like regular expression, um, methods in JavaScript. Uh, so one example is the
[2721.00 --> 2728.50]  match string, um, method. So on a string, there's a match function. You can call that and pass in a
[2728.50 --> 2731.98]  regular expression to it. And inside of that regular expression, you can have captures. So the,
[2731.98 --> 2738.34]  the parentheses, and then what you, what gets returned from there is an array that contains,
[2738.34 --> 2742.96]  uh, everything that was captured. So the, everything that was captured from the regular expression is the
[2742.96 --> 2748.02]  first thing in the array. And then each of the little sub captures within there, uh, will be the next
[2748.02 --> 2754.54]  items in the array. So at sub one, it'll be the first thing to, uh, will be the next thing and so on.
[2754.60 --> 2762.30]  And so you can use that destructuring to name those variables. So one example that, um, uh, I kind of
[2762.30 --> 2769.22]  think of is the ability to like, for example, get the month, day, and year from a date string. So if you
[2769.22 --> 2776.90]  had 2018 dash zero six dash one, four, you could match those, like match the first four numbers to
[2776.90 --> 2783.66]  this variable. So capture that the next two as the month capture that in the next two, uh, in between
[2783.66 --> 2790.88]  the dashes as, um, the day. And you can actually, if you want to skip the, the first value in the
[2790.88 --> 2795.92]  array or skip the first end number of values, you can just put commas inside of that destructuring.
[2795.92 --> 2801.42]  So it will just skip that and give you the next item in there. So you can say, for example, uh,
[2801.42 --> 2807.22]  const and then open square brackets, comma year, month, day, close the square bracket, and then
[2807.22 --> 2811.62]  call that function. And you'll get back three variables, the year, the month, and the day that
[2811.62 --> 2817.28]  just match exactly what those are. So it's a pretty cool way to use those, um, and make your code more
[2817.28 --> 2820.38]  accessible, um, just by making it easier to read.
[2820.38 --> 2824.66]  Mm. That's a spectacular feature. Now, what would happen in the case of a non-match
[2824.66 --> 2830.46]  or maybe a partial match in this case, would you have undefined in those variables or what would
[2830.46 --> 2838.32]  they end up as? Uh, yeah, I think you would have, uh, undefined in there. Um, real time feedback
[2838.32 --> 2841.90]  as he pops open his console and executes it.
[2843.00 --> 2848.82]  Or you would end up with like, you know, if I'm just thinking like stuff could end up like
[2848.82 --> 2854.74]  in a different order even. Yeah. So like if you have something that's not as concrete about
[2854.74 --> 2859.46]  matching, like it's like, Oh, it could be this or maybe this, then stuff could get moved around.
[2859.46 --> 2863.88]  So, you know, one entry might not be what you're expecting just because you got less results back
[2863.88 --> 2870.54]  or something like that. Yeah, exactly. So there could be some potential potholes in, in here. Um,
[2871.00 --> 2875.32]  I would think in lots of cases you might want to, yeah, absolutely. I think the, a match,
[2875.32 --> 2880.28]  a non-match, you might actually want to raise or, you know, follow a different code path altogether
[2880.28 --> 2885.52]  if you can't get that to hit. But that'd be kind of be up to the circumstance. Did you get our
[2885.52 --> 2890.00]  real time follow up? Did you try it? Yeah. Yep. Uh, you just get undefined back. Okay.
[2890.16 --> 2897.04]  Pretty easy to check for. That's cool. The, the, the little, uh, the commas, like the pre-leading
[2897.04 --> 2902.20]  commas when you don't want variables there is a little bit esoteric. I prefer it to be more explicit
[2902.20 --> 2906.34]  and maybe like, uh, I've seen other languages where it'll be like, you'd prefix it with an
[2906.34 --> 2911.90]  underscore and say like, or have it say unused or something. And that would indicate that there,
[2911.90 --> 2916.16]  that you expect a thing there. Cause when I first see this comma and we'll put this little snippet
[2916.16 --> 2920.10]  in the notes as well, so y'all can look at it. But when I see that comma, I think it was accident.
[2920.28 --> 2924.06]  Like I was even going to ask you, do you have a, you have a typo there? So it's just a little bit,
[2924.06 --> 2930.40]  uh, esoteric, but super handy. Yeah. I agree with that. The, the benefit of that is it's not creating
[2932.20 --> 2936.70]  using something like const. You're not locking that variable in the scope to be that value.
[2937.26 --> 2942.14]  Uh, so there, there's one nice caveat to it, but, uh, you're right. It does look a little bit
[2942.14 --> 2944.08]  like a syntax error when you first look at it.
[2950.54 --> 2955.24]  Hey everyone. I'm Tim Smith, senior producer here at changelog. You know how important it is to stay
[2955.24 --> 2960.38]  in the know and our weekly newsletter helps you and thousands of other developers do exactly
[2960.38 --> 2966.58]  that. It's the developer news that matters, nothing more and nothing less. Visit changelog.com
[2966.58 --> 2967.66]  and subscribe today.
[2982.66 --> 2988.88]  All right. So let's talk about, uh, clean get history. Now this is an article, uh, that the
[2988.88 --> 2994.78]  changelog.com actually posted, uh, uh, I don't know when exactly, but, uh, a little while ago.
[2995.08 --> 3001.66]  Uh, and it's an article from GitLab, uh, called keeping, uh, get hit your, get history clean or
[3001.66 --> 3006.72]  how and why you would want to. And, uh, I thought it'd be an interesting topic to, to go over while
[3006.72 --> 3012.40]  it's not JavaScript specific. It is something that we all typically have to work with, uh, especially
[3012.40 --> 3018.78]  if we're dealing with Git, which seems like everyone is at this point. So, um, I thought we'd jump
[3018.78 --> 3024.86]  right into it and talk about, um, what the article is, is trying to convey and some of the, the
[3024.86 --> 3029.78]  useful scenarios and maybe some opinions. When I brought this up, Jared kind of mentioned that
[3029.78 --> 3035.96]  this is the ultimate, um, uh, what did you say? The ultimate, the biggest bike shed, the biggest
[3035.96 --> 3044.26]  bike shed. Yeah. And that's something that I really feel like, um, I really feel when I'm
[3044.26 --> 3048.72]  bringing up issues with like Git history and, you know, trying not to complain too much about
[3048.72 --> 3055.90]  it because maybe it doesn't matter, but to me it does. Um, and so, yeah, uh, the first
[3055.90 --> 3061.06]  thing in this article, um, really kind of talks about, uh, why meaningful history is important.
[3061.06 --> 3069.40]  And they had a few examples, but I didn't really think that they, they gave much of a, of a reason
[3069.40 --> 3075.70]  why it's meaningful to have a clean history. Uh, but from that, uh, they, they just put kind of
[3075.70 --> 3081.48]  understanding the flow of change on a project and being able to quickly find where bugs were introduced.
[3081.94 --> 3088.88]  Um, Jared or Suze, do you have any, any, um, pros or cons or, or yays or nays as to why you might
[3088.88 --> 3094.58]  prefer a clean Git history or whether you don't care at all? I definitely am in favor of having a
[3094.58 --> 3100.02]  good, clean Git history, um, in almost all cases. And so I will admit that when I'm doing,
[3100.02 --> 3105.22]  working on a dumb project that I don't intend on either sharing publicly or having anyone else work
[3105.22 --> 3112.30]  on it, I tend to kind of, um, I tend to just, you know, have silly cathartic, you know, Git messages
[3112.30 --> 3116.94]  that are silly. And that's just my way of rebelling because, you know, I do care so much about it when
[3116.94 --> 3122.68]  I'm actually working with people. But I think for me, um, the biggest advantage in having a nice,
[3122.68 --> 3130.22]  clean Git history is when you work with, um, different people on teams. And, um, I know that,
[3130.22 --> 3136.12]  that, that the, um, article mentions things like Git bisect, for example. And so let's say there's a
[3136.12 --> 3141.74]  bug that's been introduced. Um, and let's say you've got this, um, continuous integration, um,
[3141.74 --> 3148.84]  set up for releasing, um, software. And so you've got several team members work all coming together.
[3148.84 --> 3154.22]  And if the CI has kind of missed something and production breaks, or there's like this really
[3154.22 --> 3162.30]  weird thing, um, that QA found, you can first look at all the Git messages, um, where they're,
[3162.30 --> 3168.86]  they're accurately descriptive, right. Um, which I use first because it's the fastest thing you can do.
[3168.96 --> 3173.96]  And so going, burning down the list of stuff that actually went into that release is really,
[3174.06 --> 3178.20]  really useful. So you can actually kind of see maybe there's keywords in that Git commit message
[3178.20 --> 3183.20]  that kind of points at a specific feature and that feature might be the thing that has the bug in it.
[3183.20 --> 3191.00]  So I really appreciate having descriptive, um, but succinct Git messages, um, on commits. And then if
[3191.00 --> 3198.56]  you, if you don't actually find anything, having neat, um, having kind of neat commits that are very
[3198.56 --> 3206.16]  contextually, uh, heavy allows you to run Git bisect in order to kind of jump between, um, different
[3206.16 --> 3211.50]  pieces of work that were done in order to find that bug. So I guess they're like my top two reasons
[3211.50 --> 3217.88]  why you would want to clean history. Um, and they both come down to it's way, way quicker to debug
[3217.88 --> 3219.72]  something when it goes wrong.
[3219.72 --> 3227.02]  So I definitely agree with everything Sue's just said, and I am pro clean commit history.
[3227.02 --> 3233.14]  Uh, I would bring the question of what exactly does clean mean? Because, uh, I think people define it
[3233.14 --> 3241.22]  differently depending on who you are. Um, but specifically I'm, I'm an advocate of, of high
[3241.22 --> 3248.24]  quality commit messages and, um, providing like a single line summary and then allowing yourself to go
[3248.24 --> 3256.86]  into context and detail, um, down below. Cause I've often found actually just recently, I've found a
[3256.86 --> 3264.72]  circumstance where I made a change probably maybe a year or two ago to a specific file. This is like
[3264.72 --> 3272.70]  an engine X configuration. And I was sitting here staring at the code and I was wondering why is that
[3272.70 --> 3277.48]  config in there? I don't know what it does. There was a comment on it, which was like the worst comment
[3277.48 --> 3281.92]  ever. It described the setting. And it's like, I know better than that, but I definitely wrote that
[3281.92 --> 3288.40]  comment, which basically said what the setting was. Um, so not useful comment in the code. And
[3288.40 --> 3292.58]  then I was like, okay, well, I'll just get blame this and figure out why did I set this? Because
[3292.58 --> 3297.10]  that's what I want to know, right? Like that's why history matters because later on we become
[3297.10 --> 3304.80]  archeologists or, you know, uh, Sherlock Holmes is, or in your case, you know, Dr. House, Nick, and we need
[3304.80 --> 3309.82]  to find out like why, like more about it. We need that context. And I went to get blame and I checked
[3309.82 --> 3316.24]  out the line and I checked out the commit and the commit message was identical to the comment above
[3316.24 --> 3324.94]  the freaking line of code. And I thought that is a terrible job by me. I've basically like past me,
[3325.00 --> 3331.28]  just screwed current me out of like being able to know something. And so, I mean that alone,
[3331.28 --> 3336.40]  I mean that happens all day, every day, let alone you extrapolate to like teams and larger things.
[3336.72 --> 3343.50]  This is me basically, you know, removing context from myself, but that's where those things need to
[3343.50 --> 3349.02]  live. And, uh, when you don't have high, I'll just say specifically high quality commit messages.
[3349.20 --> 3353.98]  We talk about clean history. Are we talking about like lat, like not merge commits and like keeping
[3353.98 --> 3361.44]  the actual branching clean as well. Um, but specifically on, on comments, uh, commit messages,
[3361.44 --> 3366.02]  like make those good. It's worth your time. Unless like Sue says, you're like a throwaway thing
[3366.02 --> 3370.66]  or you're just, you have more fun to just like say something silly or nobody will ever see it.
[3370.66 --> 3374.14]  But if it's like, if the code matters, then the commit messages should be good.
[3374.14 --> 3379.06]  Yeah, I totally agree with that. Um, I will go as far as to say that I, I really want the
[3379.06 --> 3383.82]  history to be clean as well. Um, typically that means that I avoid merge con
[3383.82 --> 3389.68]  or sorry, merge commits, uh, any way that I can. And I'll just squash and rebase everything when
[3389.68 --> 3395.70]  I'm going to master, uh, to keep things nice and linear when I'm looking at the, the history tree.
[3395.70 --> 3400.72]  Uh, to me that, that makes more sense. I can see an argument where merge commits help as well,
[3400.72 --> 3404.40]  because you might just have that one commit, but then you can see a breakdown of everything
[3404.40 --> 3410.78]  that happened within there, but also that those, um, the commits within the merge should also be
[3410.78 --> 3416.14]  cleaned up so that you don't have a bunch of, uh, superfluous commits that really don't mean
[3416.14 --> 3421.90]  anything. A great example of something that I've seen on, on projects before is like, uh,
[3422.06 --> 3427.26]  they'll just merge every, all of the commits in without changing anything or squashing anything
[3427.26 --> 3432.10]  down. And so you'll see, uh, one specific example that I had was I was going through and I was trying
[3432.10 --> 3438.72]  to figure out why this line in a file was the way it was. And so I did what you do. I get blamed it
[3438.72 --> 3445.78]  and found, um, not necessarily, I didn't care who the person was that made the change, but I just
[3445.78 --> 3451.14]  wanted to see what, why it was made in that commit. And, uh, I scroll up to the top and see the commit
[3451.14 --> 3456.64]  message. And it was just fixing code climate errors or fixing JS lint errors and or JS hint errors,
[3456.80 --> 3462.76]  whatever. And, um, that really wasn't helpful to me because they, they didn't prune that out of there.
[3462.92 --> 3467.60]  So, uh, it really didn't give me any context about what errors were around that. So I would have to
[3467.60 --> 3473.14]  find that commit and then look at the messages around that maybe to help figure out why the code
[3473.14 --> 3479.28]  changed. Um, so that that's one big, big, uh, reason that I like to keep the history clean.
[3479.86 --> 3486.86]  Another reason is, um, I like to present the code in the way the history of the code in the way that
[3486.86 --> 3492.28]  it should have occurred instead of the way that it actually occurred. Um, and that that's kind of
[3492.28 --> 3497.60]  important, uh, to me, I guess on some of the projects that I go into, uh, I do consulting.
[3497.60 --> 3504.10]  And so, um, before I deliver code to a customer, um, you know, we can have a whole bunch of internal
[3504.10 --> 3511.16]  commits and bugs and, and all sorts of messages, but pruning that, uh, and cleaning it and presenting
[3511.16 --> 3516.46]  it in the way that it should have occurred instead of the chaotic way that it did occur, uh, helps to
[3516.46 --> 3522.80]  keep the customer's confidence in us high. So I like doing that. So on devil devil's advocate on
[3522.80 --> 3528.14]  that would be that you're, you say you're keeping a clean history, but actually you are changing
[3528.14 --> 3534.88]  history to better suit your needs. So you could say you're, you're rewriting history and there's
[3534.88 --> 3540.00]  plenty of people that believe that the trade-offs there are worse than the trade-offs of having,
[3540.00 --> 3545.00]  you know, too many branches and some commits that didn't mean anything. And these other things,
[3545.00 --> 3549.22]  cause that actually represents history. Whereas you are rewriting history. How dare you?
[3549.70 --> 3551.50]  Yeah. Good books aren't written, Jared. They're rewritten.
[3554.40 --> 3556.76]  I think that's a quote by Michael Crichton.
[3558.24 --> 3559.04]  That's a good one.
[3559.12 --> 3563.14]  There is such a thing as rewriting history too much, right? Where some people get a little
[3563.14 --> 3568.26]  overzealous. Uh, well, I guess in my opinion of, of trying to squash things down too much,
[3568.26 --> 3572.80]  trying to, you know, achieve too much with one commit just for the sake of cleanliness. What's,
[3572.80 --> 3576.40]  what are people's takes on that? There's no such thing. No, I agree.
[3578.76 --> 3583.02]  The one thing that I really look for is, is keeping attribution. Uh, so I wouldn't want to
[3583.02 --> 3585.86]  squash down somebody else's commits and then make them my own.
[3586.44 --> 3590.26]  Absolutely. I've definitely, I mean, specifically with like long running branches,
[3590.26 --> 3595.44]  like a feature branch, that's a large feature and maybe multiple people worked on it. You know,
[3595.44 --> 3600.84]  you're not going to be rebasing it throughout its lifespan because maybe it's already like on,
[3600.84 --> 3607.22]  on GitHub and people are committing to it. Um, in those circumstances, I'm okay with a merge commit
[3607.22 --> 3611.76]  there because it's kind of a thing. Like it's kind of a historic event. It's part of the history.
[3611.76 --> 3616.68]  It was like, this thing was a big moving branch alongside the main branch. And then when did it
[3616.68 --> 3621.98]  come back in? Right. When was it merged? And so I don't have it that, that doesn't bug me as much.
[3622.14 --> 3626.52]  That being said, if I'm working solo on a specific thing and I'm on a branch, I will,
[3626.52 --> 3633.78]  I'll rebase and I will squash in that circumstance. So I'm, I'm not hardcore on either side of the
[3633.78 --> 3640.72]  fence. That makes sense. One dislike that I have that I've seen from time to time is, um, when,
[3640.90 --> 3647.20]  when somebody is merging in master to a feature that's like long running and they're not rebasing.
[3647.20 --> 3653.32]  And so they run into conflicts, uh, merge conflicts and they fix them. And a lot of people commit, um,
[3653.32 --> 3657.46]  on the command line with like the dash M flag, so they can like write a message.
[3657.82 --> 3663.84]  And sometimes they'll forget that by default, you know, merging something in and when you have
[3663.84 --> 3669.50]  conflicts and then, um, fix them and commit it, it will still append the normal, you know, um,
[3669.50 --> 3674.04]  merge commit message. And some people accidentally override that and they'll just write something like,
[3674.04 --> 3680.02]  um, fixing merge conflicts. And then you completely lose context of what happened. And sometimes
[3680.02 --> 3687.56]  it just makes it look more convoluted. Um, and that for some reason kind of, um, annoys me when you,
[3687.72 --> 3692.64]  when you lose that merge commit in the first place, because it's really sometimes only useful for showing
[3692.64 --> 3698.32]  the history of when somebody actually put, um, master back in and brought it up to speed.
[3698.32 --> 3704.24]  Yeah, definitely. And on the topic of kind of longer running feature branches, I think that that's,
[3704.82 --> 3710.00]  um, one area that it's difficult to keep the history clean, uh, because you can constantly want to be,
[3710.00 --> 3715.70]  um, bringing in like updates. If you need updates from like master, uh, to work in that longer
[3715.70 --> 3721.30]  running feature branch, uh, that can be difficult. And you, you can resort to, uh, things like merge,
[3721.44 --> 3726.52]  merging down into that and then merging that back up. And that's where, uh, maybe I'm not doing it
[3726.52 --> 3731.64]  right, but that's where I've run into a lot of, um, problems where I just give up and I don't really
[3731.64 --> 3736.20]  understand the history at that point because there's the same commits being merged down. And then
[3736.20 --> 3740.56]  they like, it's almost like when you look at the graph, it looks like they exist in two places,
[3740.56 --> 3745.64]  even though they, they really don't, but it, uh, it gets confusing and convoluted from there.
[3746.14 --> 3751.94]  Agreed. I've definitely made a huge mistake once when working for a large team that, um,
[3752.30 --> 3757.44]  were definitely moving much faster than a previous team I was on. So, you know, it was at the point in
[3757.44 --> 3762.56]  my career where I moved from a small team that didn't have continuous integration into a larger team
[3762.56 --> 3767.66]  that had a lot of continuous integration. And so for long running features where you can't always
[3767.66 --> 3772.66]  just incrementally ship it under feature flags and things like that. Um, I got to a point where
[3772.66 --> 3779.24]  I had to, you know, um, merge master in or rebase master in, and I had let it go too long without
[3779.24 --> 3784.88]  realizing, and there was so many commits coming in and, uh, you know, there were changes to the same
[3784.88 --> 3792.90]  files that, um, I was working on and I ended up with a rebase, um, like a rebase session with
[3792.90 --> 3801.72]  conflicts in like, I think 144 different steps. And so I had to fix the conflicts and then do like,
[3801.72 --> 3808.94]  you know, get rebase dash dash continue like up to a hundred times. And I was so both like ashamed of
[3808.94 --> 3812.66]  myself, even though, you know, there's a first time for everything when that kind of thing happens.
[3812.66 --> 3819.20]  And also just the sheer, you know, size of the issue that I had and like, how am I possibly ever
[3819.20 --> 3824.80]  going to deploy this? Related story. I was live streaming on Monday afternoons, uh, last Monday.
[3824.88 --> 3829.78]  And I had, I had been a little while as we're open sourcing our show notes so that you can edit
[3829.78 --> 3834.30]  the show notes on GitHub and also edit it from the CMS. That way people can help us make the show notes
[3834.30 --> 3840.08]  better. And I've been, I've been like Twitch streaming while I do that. And it had been about a month
[3840.08 --> 3843.90]  and a half since I worked on that particular feature. And so on Monday I was back at it.
[3843.92 --> 3847.56]  I was like, all right, let's do this. And I got started. And the first thing I did is when I went
[3847.56 --> 3854.04]  to rebase master and I spent about 45 minutes of that Twitch stream rebasing. It was the most boring,
[3854.04 --> 3858.52]  like stupid. And I was like, I couldn't remember like what I was doing. And I was just like,
[3858.52 --> 3864.56]  this is not, this is not good streaming, but it wasn't 144 in a row. That's for sure.
[3864.80 --> 3869.74]  Solving merge conflicts is probably one of the most difficult things to do on a stream as well,
[3869.74 --> 3875.68]  because you need like a hundred percent concentration. And I have definitely failed
[3875.68 --> 3879.62]  at trying to resolve tricky things like that on stream. And I'll just say to people,
[3879.78 --> 3883.92]  Hey, I'm going to actually abort this. I'm going to do it off stream. And then we're going to move
[3883.92 --> 3890.00]  on to another thing. Um, but you know, watch the repo if you want to see me resolve this off stream
[3890.00 --> 3895.28]  for sure. And that, that crazy rebase, um, sorry, that like intense rebase that I talked about earlier,
[3895.28 --> 3899.46]  I actually took it home with me that night because I didn't want a single interruption.
[3899.46 --> 3904.68]  And so I think I worked from 7 PM till 10 PM that night. And that obviously cut into my personal
[3904.68 --> 3910.02]  time, which meant I never made that mistake ever again, but I totally agree about the stream stuff.
[3910.26 --> 3916.74]  It just feels so boring. And also you just feel like you don't have your best brain to actually
[3916.74 --> 3918.94]  fix it. And it's like a double whammy.
[3918.94 --> 3923.90]  Yeah. I couldn't imagine doing, trying to do that live. Um, that would be, that would be awful
[3923.90 --> 3930.36]  and probably boring, but also at the same time, uh, it's reassuring to hear that, you know, everyone
[3930.36 --> 3938.02]  goes through these problems. So it's a, it's a good thing overall. Um, now the article kind of goes
[3938.02 --> 3943.62]  into four different scenarios and they're all kind of based around rewriting history. And we kind of
[3943.62 --> 3948.88]  already talked about that. And when you rewrite history, you do end up having to force push back up.
[3948.94 --> 3955.20]  And so I was curious what your thoughts are on, on force pushing. Uh, do you have any qualms with
[3955.20 --> 3963.82]  that? Every time I do it, I feel like I've failed. With that being said, I do it all the time.
[3967.12 --> 3971.24]  Not all the time, but yeah, I mean, you're not supposed to do it, right? It messes up everybody
[3971.24 --> 3978.24]  else, but I've, I've lost work as a result because somebody else did that and had no option,
[3978.24 --> 3984.40]  but to redo that work. You know, I came in in the morning after, you know, working on something the
[3984.40 --> 3991.10]  night before and I came in and I, I pulled everything down and you don't, there's no way
[3991.10 --> 3995.58]  to really see that coming, right? It's just a routine fetch and merge or a routine pull.
[3995.88 --> 4001.32]  And I realized that all of my work was gone because a colleague had set up there. They didn't like
[4001.32 --> 4008.68]  merge, uh, commit. So they set up their gig config to just do a rebase. And somehow that had erased
[4008.68 --> 4014.30]  the stuff that I'd pulled up. So because, um, they, they thought that they had to do dash F if
[4014.30 --> 4019.26]  you ever like rebase on master. So something happened and they ended up just force pushing
[4019.26 --> 4024.98]  up and it just totally erased my stuff. And so usually I have the motto of if you're working by
[4024.98 --> 4029.32]  yourself and you're force pushing, because you know, you're trying to hide embarrassing mistakes
[4029.32 --> 4033.70]  that you made on your own personal GitHub repo, that's okay. Um, but if you're working with teams,
[4033.82 --> 4037.76]  um, there's almost no reason to really take that risk.
[4037.76 --> 4042.40]  So I'm going to get controversial here. Adam in the chat room is also saying that, uh,
[4042.76 --> 4047.12]  if you're, if you ever have to force push, you're doing it wrong. I take pride in my force pushing.
[4047.12 --> 4055.40]  I'm going to be honest, uh, in keeping, in keeping with the spirits of, um, the history that should
[4055.40 --> 4060.08]  have happened instead of what did happen. Uh, and the scenarios that this article kind of goes through,
[4060.12 --> 4065.06]  it goes through changing the most recent commit, changing a specific commit, um, adding,
[4065.06 --> 4070.72]  removing or combining commits. So, uh, interactive rebasing, and then a complete fresh start. Uh,
[4070.72 --> 4077.26]  those are all rewriting history. And then you have to, to force push from there. And I'm completely
[4077.26 --> 4084.26]  comfortable force pushing when I know that it's, uh, my own feature branch and nobody else should have
[4084.26 --> 4091.22]  really been on that doing anything. So I'm ideally not affecting anyone. Uh, GitHub does actually let you
[4091.22 --> 4097.32]  specify like you can never not push force push to master. So it will fail that for you. Uh, and
[4097.32 --> 4102.44]  that's a good thing to set. I would never do it on master except for when I did it a week ago. Um,
[4102.68 --> 4110.54]  and that was to remove sensitive information. Uh, but ideally I did communicate with my whole other
[4110.54 --> 4114.84]  team of one other person and let him know. So it wasn't a big deal. That's the other thing.
[4114.84 --> 4121.72]  Communication is, is very important with that. Um, but I, I think that, uh, amending commits is
[4121.72 --> 4126.20]  something that I do quite often. And then I'll just force push that you can also, uh, there,
[4126.28 --> 4132.34]  there's a better flag than dash dash force. There's dash dash force with lease. And so it will do a
[4132.34 --> 4136.56]  force push, but only if no other commits have been pushed to that. So if somebody else did push
[4136.56 --> 4142.94]  something up to your branch, um, it will fail your force push because you have commits that, um,
[4142.94 --> 4146.74]  because other commits have occurred since you last pushed.
[4146.84 --> 4150.44]  That sounds like that should be the default for dash dash force. Exactly. And then you should
[4150.44 --> 4154.02]  change it to like dash dash force. Yes. I know what I'm doing. Kind of a flag.
[4154.48 --> 4159.20]  If you're going to do the other one, you know? Yeah. Force with lease. I mean, who comes up with
[4159.20 --> 4164.26]  these, these command, these flags, like, yeah, like L E A S E, like you have a lease on an apartment.
[4164.46 --> 4169.62]  Yep. All right. No comment. I don't know. I I'm very comfortable with, with that. And that's
[4169.62 --> 4177.48]  kind of how I, how I help to maintain a clean get history. GitHub also does a lot, uh, more recently
[4177.48 --> 4183.32]  with, with allowing you to do that straight from a pull request where you can, uh, specify that you
[4183.32 --> 4188.36]  want to merge this pull request, or you want to rebase and then merge this pull request. So it
[4188.36 --> 4193.38]  would ideally do, uh, just a fast forward merge and not actually have a merge commit, or you can do a
[4193.38 --> 4196.48]  squash and merge. So it'll squash all of the commits from that pull request down into one
[4196.48 --> 4200.58]  and then merge that. And that's pretty cool because when it's tied to a pull request like
[4200.58 --> 4205.08]  that, um, gets also keeping track of that branch. You can restore that branch if you need to later
[4205.08 --> 4210.88]  on, uh, which is really helpful for later debugging, but that's a GitHub specific feature.
[4210.96 --> 4215.24]  I'll tell you another reason why that's cool is because you don't have to know all of the
[4215.24 --> 4220.94]  intricacies of how to do it from the command line stuff. Like I'm a command line user had been
[4220.94 --> 4226.40]  my entire career. I've been using Git for a decade. I cannot remember how I, if you told me to
[4226.40 --> 4231.52]  squash these and rebase or something from the command line, I would be in the Git man pages
[4231.52 --> 4235.68]  for like 15 minutes getting it right. I think that's awesome because that brings that feature,
[4235.80 --> 4240.14]  which is very nice for when you want to use it, you know, behind a big green button and that's
[4240.14 --> 4240.62]  spectacular.
[4243.62 --> 4249.52]  All right. Thank you for tuning into JS party this week. Tune in live on Thursdays at 1 PM U S
[4249.52 --> 4255.22]  Eastern at changelog.com slash live. Join the community and Slack with us in real time during the shows.
[4255.22 --> 4259.64]  Head to changelog.com slash community and do us a favor, share this show with a friend,
[4259.94 --> 4264.64]  radio snap, a podcast, go into overcast and favorite it. And thank you to fastly,
[4264.70 --> 4269.36]  our bandwidth partner had to fastly.com to learn more. And we move fast to fix things around here
[4269.36 --> 4274.76]  at changelog because of roll bar. Check them out at rollbar.com. We're hosted on Leno cloud servers
[4274.76 --> 4279.70]  at a Leno.com slash changelog. Check them out and support this show. Our music is produced by
[4279.70 --> 4284.82]  Breakmaster Cylinder. And you can find more shows just like this at changelog.com. Thanks for tuning
[4284.82 --> 4286.24]  in. We'll see you next week.
