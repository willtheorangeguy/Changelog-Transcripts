[0.00 --> 6.70]  Bandwidth for Changelog is provided by Fastly. Learn more at Fastly.com. We move fast and fix
[6.70 --> 11.42]  things here at Changelog because of Rollbar. Check them out at Rollbar.com and we're hosted
[11.42 --> 18.32]  on Linode servers. Head to linode.com slash Changelog. This episode of GoTime is brought
[18.32 --> 24.26]  to you by Airbrake. Airbrake is full stack error monitoring for Go applications. Get real-time
[24.26 --> 28.98]  error alerts plus all the info you need to fix any error fast. And in this segment, I'm talking
[28.98 --> 34.40]  to Joe Godfrey, CEO of Airbrake about why getting to the root cause of errors is so important.
[34.82 --> 39.32]  Look, Adam, to me, root cause is everything. All software has bugs. We all know that. And
[39.32 --> 44.74]  when you find a bug or when you can't find a bug, the amount of time that typically gets
[44.74 --> 48.32]  spent trying to chase around and figure out how to reproduce the problem and what's the
[48.32 --> 52.28]  cause of the problem, even like what part of the code kicked it off or what sort of actions
[52.28 --> 57.84]  drive it. I mean, that's hours and hours of time wasted spent chasing your tail instead
[57.84 --> 61.40]  of actually fixing the problem, improving the customer experience and getting back to
[61.40 --> 65.94]  building more features, which is really what your company is all about. So to me, being
[65.94 --> 71.02]  able to really understand like what is the root cause of this problem is the key factor
[71.02 --> 74.34]  to being able to solve that problem and get back to doing what's most important, which
[74.34 --> 78.24]  is building new features and improving your product and quite frankly, fixing the customer
[78.24 --> 81.84]  experience. It's broken as long as that bug is out there. All right. Check out Airbrake
[81.84 --> 87.32]  at airbrake.io slash go time. Go time listeners get airbrake for free for 30 days. Plus you
[87.32 --> 93.50]  get 50% off your first three months. Try it free today. Once again, airbrake.io slash go time.
[102.90 --> 106.00]  Hey everyone. This is Florin and it's go time.
[106.00 --> 119.24]  This is go time. A panel of go experts and special guests every single week discussing
[119.24 --> 124.00]  the go programming language, the community and everything in between. We record live
[124.00 --> 129.34]  every Thursday at noon Pacific, 3 p.m. Eastern. Tune in at go time.fm.
[129.34 --> 144.22]  All right. It is go time episode. I think based on this document, 74, 75 episode 75. And I'm
[144.22 --> 148.62]  Adam Stokovic. I never host this show. In fact, I've never hosted this show. I just come on as a
[148.62 --> 154.40]  thing on the wall or something like that, but I'm not ever in the limelight here, but today I'm going
[154.40 --> 159.18]  to host it because why not? Right. And I got, obviously I can hardly see here. So say hi, please.
[159.34 --> 163.76]  Hi everybody. And I hate when we do that. So I always listen to Eric or Brian say, Hey,
[164.06 --> 168.12]  so say hi. Cause it's like somebody said in the chat a while back that it was like, uh,
[168.56 --> 172.02]  like the circus, you asking somebody to do something. It's so it's weird thing. I'll never
[172.02 --> 178.20]  do that again. Oh, Brian, Brian always rebels against that. He does. And I do too. And then I did it.
[178.70 --> 185.32]  So, you know, the cycle continues and we've got a long time listener, a first time caller,
[185.32 --> 190.72]  pinnacle person in, in go from what I can tell. I'm, I'm merely an outsider here, but
[190.72 --> 194.32]  Florian Patan, you're here. Thank you so much for joining us today. Say hello.
[194.94 --> 196.80]  Oh, Hey everyone. Happy to be here.
[197.28 --> 200.52]  Did I do a good job on the name? Was it, it was mostly okay, right?
[201.24 --> 203.70]  Yeah. Mostly okay. Let's go with that.
[203.70 --> 210.96]  So for those catching on the rebroadcast and or live show of this, uh, it's difficult to say his name,
[211.02 --> 215.48]  but I've got it. So that there you go. And today from what I understand, we're talking about
[215.48 --> 220.76]  Goland, which is not Goland. It's Goland. It's an IDE from our friends at Debt Brains.
[221.32 --> 227.28]  And then we're also talking about go to the community, which is fun. And particularly the fact
[227.28 --> 233.50]  that you help lead the go for Slack, which is considering how much it's grown over the years,
[233.52 --> 239.20]  it's gotta be a big job. So, uh, but let's maybe start with your version of, you know,
[239.20 --> 243.40]  who you are in the go community, what you're doing, how people understand who you are.
[244.40 --> 251.74]  Okay. Sure. That, that sounds fine. So, um, yeah, well, I've started with go roughly five years ago,
[251.74 --> 260.68]  I guess. Um, back then I kind of did a lot of PHP and I was okay. Let's see if I can learn something
[260.68 --> 271.36]  else. Um, I couldn't learn Scala. I was like, not really my cup of tea and yeah, I found go. And
[271.36 --> 279.94]  ever since then, I switched to it full time. Um, I became, uh, like initially a member of the go,
[279.94 --> 289.12]  uh, Slack channel after that I became an admin here. Um, and ever since I've gotten a bunch of other
[289.12 --> 297.58]  go jobs officially and like maintain some pet projects and got involved in the, uh, JetBrains extension
[297.58 --> 307.18]  for, uh, for go. And one thing led to another. And five years later here, I am working now for them
[307.18 --> 313.12]  officially as a developer advocate. This is like breaking news though, right? Like this is
[313.12 --> 317.70]  day one or day two from what I understand of you being a JetBrains employee.
[318.20 --> 323.90]  Yeah, pretty much. It's the first week I'm officially, uh, at JetBrains. Uh, before that,
[324.00 --> 328.58]  I think people assumed I'm part of the JetBrains team, although I wasn't.
[328.72 --> 329.42]  Cause you're so active.
[329.42 --> 338.30]  Uh, oh yeah, pretty much. It's the editor that I personally use. I, I enjoy using and,
[338.30 --> 343.80]  you know, I, I know it's a bit of a sensitive topic here because everybody's used to their
[343.80 --> 351.90]  own workflows, their own, um, editors and yeah, people can, can get a bit, um, more passionate
[351.90 --> 359.78]  about this, but yeah, overall, like I like this one. And I guess here we are.
[359.78 --> 366.58]  Right. Well, you got Emacs, Vim, of course you can't ever, you know, avoid those two, right?
[366.66 --> 371.98]  There's not technically editors, but they, they, they are, um, yeah, they are.
[373.04 --> 378.12]  Then you've got a VS code, which has become, uh, Carlos you use VS code, right?
[378.12 --> 380.82]  Yeah. That's what I've been using for a long, for a while.
[381.12 --> 383.54]  For a while though, you were using Electron, weren't you?
[384.70 --> 387.70]  Not Electron, sorry, Atom. My bad. I always skip those up.
[389.36 --> 391.94]  And I, I don't, what made you switch away from that?
[392.94 --> 397.96]  I don't remember anymore. I was having some troubles and I think he was, there was a speed
[397.96 --> 402.78]  issue too. And yeah, I don't remember basically.
[402.78 --> 411.46]  Well, I use VS code, but I don't do any Golang programming at all. Nothing whatsoever. Uh,
[411.46 --> 416.70]  which makes me totally an imposter here, but, uh, you know, the, the tagline for Golang is
[416.70 --> 418.82]  capable and ergonomic.
[419.82 --> 424.02]  Yeah. Let's talk about that. What does ergonomic mean in this context?
[424.02 --> 430.84]  In this context, it means that it allows you to, to do whatever you need to do and focus
[430.84 --> 438.18]  on the code and let the ID, uh, figure out for you, uh, where your mistakes are as soon
[438.18 --> 447.30]  as you, you do them or help you suggest fixes, uh, on for them. So let's say, um, you have
[447.30 --> 453.86]  a mistake in your code. Uh, you, you can quickly correct it. Uh, sometimes the ID itself
[453.86 --> 462.10]  being able to, to provide, uh, fixes for, for it. Um, and it also allows you to use it
[462.10 --> 468.62]  not only in goal context, but also for web development. So for things like TypeScript or
[468.62 --> 475.78]  I've seen now, there's a, there's more support for Vue JS as a framework. There's like a bunch
[475.78 --> 484.90]  of, uh, React, Node JS support by default in, in the ID. Uh, so, uh, it allows you to, to
[484.90 --> 490.78]  focus on development, not, not only for Go, but even if it's tailored for it, but also for,
[490.78 --> 498.02]  uh, a lot of other languages. So, um, it, it also, like many people don't know this, but
[498.02 --> 505.14]  like one of the, the tip to actually start using the ID is unplug your mouse or turn off
[505.14 --> 510.10]  your touchpad because you can do everything with, with just a keyboard.
[510.10 --> 518.50]  Hmm. And so the way you got involved in this was through community aspects, plugins. Is that right?
[518.50 --> 528.34]  Yes, pretty much. So, uh, when I started learning Go, um, my editor back then was IntelliJ IDEA and, uh,
[528.34 --> 535.94]  I noticed there was a plugin, which wasn't really maintained at the time. And I learned Java in
[535.94 --> 538.58]  order to write Go basically.
[538.58 --> 542.18]  Learn Java to write Go. You don't hear that often.
[542.18 --> 543.62]  Yes.
[543.62 --> 549.86]  It's like actually that I'm, I'm concerned that there's actually some sort of internet
[549.86 --> 552.82]  searches right now for your address to come and get you or something like that. Cause you
[552.82 --> 556.82]  shouldn't say stuff like that. Is that true? I mean, does that happen often?
[556.82 --> 563.14]  Uh, I, I don't think it happens that often. Um, more often it happens that people may already
[563.14 --> 570.90]  know Java and they are switching to Go, but I simply wanted to improve my development experience.
[570.90 --> 578.82]  And, um, yeah, because the plugin was open source at the time, uh, I could just jump in, send PRs
[578.82 --> 585.86]  and became one of the contributors to the open source plugin. Um, and yeah, basically started learning
[585.86 --> 589.78]  Java alongside with Go because I was so much into Go.
[589.78 --> 598.10]  So the IT, I see here that the IT is, you need to pay for it. It's after your trial is up, right?
[598.10 --> 601.14]  Yeah. Yes, that's correct. You.
[601.14 --> 610.90]  So if people do a plugin, do they also get paid? Uh, do they have ability to sell a plugin?
[610.90 --> 621.30]  Uh, yes. So, um, there is a plugin that's available for Intel GIDI Ultimate. Um, the open source plugin that
[621.30 --> 627.38]  I used to maintain at some point JetBrains took over it, uh, still developed it as an open source, uh,
[627.38 --> 632.90]  project. And then they realized that they are spending way too much, uh, time on it. And they
[632.90 --> 639.78]  said, okay, we need to focus more resources on it, I guess. And that's how the, the, like, we started
[639.78 --> 649.70]  having a proper ID from, from them. Um, you need to pay for it. Um, but you, you can also get it for free.
[649.70 --> 658.26]  If you're an open source developer, or if you're a student, there's a, uh, discount for, for their
[658.26 --> 665.30]  licenses, like for, for one year. Um, and if you have some other discounts as well, like user groups,
[665.30 --> 672.10]  for example, can get licenses for free. If they, they meet a certain requirement in terms of, uh, how
[672.10 --> 678.18]  often they, they happen and, uh, how many people they, uh, they have attending. So there, there's a lot
[678.18 --> 685.78]  of, um, giving back to the community as well. Not, not just, uh, you know, asking for money from
[685.78 --> 691.62]  developers, uh, which is a nice thing. Uh, you don't really see that in too many companies, I guess.
[693.22 --> 698.90]  Interesting. I'm looking on the different options. When you click on buy, it actually gives you a couple
[698.90 --> 703.46]  of different ways you can. And then one of the ways you can find that is, is, uh, is the four
[703.46 --> 707.54]  open source projects, which is free. It says non-commercial open source projects can qualify
[707.54 --> 714.50]  for free licenses to Goland and other JetBrains tools, provided they meet a simple set of criteria.
[715.14 --> 719.46]  Are you familiar with that? Uh, the, the restrictions or constraints around that?
[719.46 --> 727.46]  Uh, I'm not very familiar as it's, uh, you know, first week here, uh, but I'm, I'm happy to, to follow
[727.46 --> 734.66]  up on that. Uh, usually if you, if you just write to them, they're very quick to, to reply. So, um,
[735.54 --> 742.58]  yeah, just if you're listening to this, just feel free to, to write to, uh, to the sales team and ask
[742.58 --> 745.62]  them and they will be happy to talk with you.
[745.62 --> 751.70]  So why does this, why do you choose this editor over other options? Like we talked about
[752.26 --> 757.30]  that, you know, the tried and true. I know that, uh, that Brian and Eric, I'm pretty sure they're Vim
[758.42 --> 763.22]  candidates. Uh, Carlos, you use VS code. I use VS code. I'm sure there's lots of others out there
[763.22 --> 768.34]  listening that use VS code because it's very supportive of go, but why do you, why choose Goland
[768.34 --> 772.10]  over other options? What, why is it perfect for you?
[772.10 --> 782.42]  Uh, so for me personally, it's the, um, inspection engine that, um, allows you to detect in real time
[782.42 --> 788.18]  issues that you have with the ID, uh, with, with your code from the ID. So for example, if you have a,
[789.30 --> 796.50]  compiler errors, you don't need to necessarily wait for, uh, to go build tool to actually compile your code.
[796.50 --> 804.50]  The ID will know that, or it's the fact that it integrates with other, um, tools or languages,
[804.50 --> 814.50]  such as for example, um, if you're working, uh, with a database like Postgres, you can type a SQL query.
[814.50 --> 825.22]  And if you use either the standard library database SQL or a library like, um, PGX or, uh, SQL X or
[826.10 --> 833.78]  Mark's, uh, Mark Bates, uh, slash pop, it will recognize that the string is all, is a SQL query.
[833.78 --> 841.94]  It will start offering you auto-completion for, for SQL. And it will even tell you things like,
[841.94 --> 847.14]  oh, you're, you don't have that column in the database. Do you want to add it? Or, uh, it allows
[847.14 --> 852.90]  you to preview the queries that you have. So there's a lot of intelligence in there. There's also,
[852.90 --> 863.94]  uh, for me, what I've found that's really, um, useful is the refactoring support. So if, if you want to,
[865.06 --> 871.06]  to rename something, or if you want to move, uh, types around, you can do that with, which is pretty,
[871.06 --> 879.30]  pretty useful. Um, and in general, the auto-completion engine is really, uh, spot on into
[879.30 --> 885.78]  figuring out what you want to type as soon as you type it. Hmm. So can you speak to any of this
[885.78 --> 890.18]  Carlyce to like a, an alternate, how, how it works with VS code for you with some of the things he's
[890.18 --> 898.82]  mentioning? Um, I haven't enabled anything basically like not, I mean, I have the go plugin, but I
[898.82 --> 904.90]  haven't souped it up. So I don't know. I know that they, they can't auto-complete things. I just
[904.90 --> 914.50]  haven't set it up and other stuff like, uh, correcting, it will highlight, um, things that
[914.50 --> 922.58]  will be caught on like code formatting and a bunch of things to tell you if it's an error or if it's
[922.58 --> 932.26]  a warning, it will tell you all of that. And you can, you have the option to make it more on your face
[932.26 --> 942.18]  or just quietly warn you of these, uh, notify you of these either errors of warnings. And so I, I haven't
[942.18 --> 950.98]  used go land, go land. So I don't know how it compares, but it sounds like it does. VS code does
[952.02 --> 961.38]  mostly, or if not all of it. I don't know. Uh, yeah. So we, um, in, in terms of features,
[962.34 --> 968.02]  some of these features you'll find in other editors like VS code or Atom, or, uh, I think in,
[968.74 --> 974.90]  uh, VI or Emacs as well. I'm not really sure because those are things that I haven't tried as editors,
[974.90 --> 982.26]  sorry. Uh, but, uh, whereas in those editors, you, for example, need to install the plugin and then you
[982.26 --> 988.10]  need to install additional tooling and so on for, uh, for this ID, you just need to install the ID and
[988.10 --> 994.26]  you're ready to go. Like you don't have any other, uh, setup need. Let's say you just have
[994.98 --> 1002.58]  not to install go the ID and you just start working on, on your project. And also every time we
[1003.62 --> 1008.90]  release an update, you get all the features and so on without having to further update the tools.
[1008.90 --> 1017.94]  And yeah, that would be another, um, difference between this, uh, approach and what other editors
[1017.94 --> 1018.42]  are doing.
[1018.42 --> 1022.58]  Mm. Are you familiar with the DEP integration portion of this?
[1022.58 --> 1026.10]  It sounds like, uh, there's some integration with DEP, the open source project there.
[1026.10 --> 1033.54]  Oh yes. So we, we just released that like in a couple of weeks ago in, in the latest release in
[1033.54 --> 1044.26]  2018.1. And, um, what it allows you to do is it allows you to have a, uh, project that uses DEP and
[1045.22 --> 1051.86]  it figures out when, whenever you change the imports or you add the dependency on a code that doesn't,
[1051.86 --> 1060.26]  uh, uh, uh, when you add the dependency on a library that's not imported yet or not in your, uh, vendor, uh, folder,
[1060.26 --> 1067.54]  it, uh, figures out that it needs to run DEP and it works its magic in the background to, uh, invoke the
[1067.54 --> 1070.50]  necessary commands so that you can just continue typing.
[1070.50 --> 1072.82]  That is pretty cool.
[1072.82 --> 1077.78]  Why, why is that important to go developers having that kind of integration?
[1077.78 --> 1087.30]  I, I guess for like, if you come from other languages, let's say, um, Ruby, Python, PHP,
[1087.30 --> 1091.86]  uh, that, that kind of integration, you will see already in other editors there.
[1092.42 --> 1100.34]  And, uh, for us, it, it's something that's missing. Um, it's something that, um, especially because of the,
[1100.34 --> 1106.90]  the fact that you actually, uh, need all the, all the code to be there in order to compile the project.
[1106.90 --> 1116.18]  Right. Uh, you would, you would want to, to take that out of the user task and not, not have the user
[1116.18 --> 1123.46]  have to go in, in the command line and now say, okay, now I need to go in, in my definition file or
[1124.02 --> 1128.98]  let that figure it out to the version that I need and then run DEP and SHEER, right?
[1128.98 --> 1137.38]  Uh, you would need to do that manually, or you need to run DEP and SHEER, add and then the, uh, dependency itself.
[1139.14 --> 1145.14]  And that's what the ADE does in background now for you. You don't have to take your focus away from
[1145.14 --> 1148.42]  the code, right? You can still have the context in, in front of you.
[1148.42 --> 1157.30]  Yeah, I guess for, uh, uh, new people coming in to go, you know, it's one more thing to learn on top
[1157.30 --> 1165.62]  of everything that they have to learn. So having a easier to manage in the IDE, I can see that being
[1165.62 --> 1173.62]  a benefit and also, you know, for the same reason, people use Git integration in their IDs. Um, I, I don't
[1173.62 --> 1181.06]  own because I learned to do it on the command line. So I, I trust that I always know what's going on
[1181.06 --> 1184.90]  there as opposed to the idea I need to learn another thing. So.
[1185.62 --> 1190.58]  I had the same feeling until recently. Honestly, I, I was such a purist to say,
[1191.38 --> 1198.66]  I have, uh, aliases. I know Git. I'm smart. I'm cool enough. I can use the terminal. I can use
[1198.66 --> 1203.30]  Git on the terminal and take it from me. I dare you. That was my opinion.
[1203.62 --> 1208.34]  And then I sort of use this VS code and I was like, huh, I could just commit this one file
[1208.34 --> 1212.66]  right here. Cause it's, it's a click. And so what I ended up doing is doing both.
[1213.30 --> 1218.26]  It's not a replacement. It's, it's not an either or it's a both scenario for me. Uh,
[1218.26 --> 1222.26]  Florin, what about you? Is it, is it a both or an and or for you for
[1222.26 --> 1226.02]  Git integration and say an IDE or a VS code type thing? How do you work with that?
[1226.02 --> 1233.22]  So I'm mostly working from command line. Um, I, I, I, I haven't managed to,
[1233.22 --> 1239.70]  to, to switch fully to the IDE side. Uh, I, I do use the IDE for doing things like, uh,
[1240.42 --> 1244.74]  differences between, um, files when, whenever there's a conflict and so on,
[1244.74 --> 1252.98]  I find it so much more convenient to do. Yeah. Um, and, um, there are some, some features now that I,
[1252.98 --> 1259.78]  I was reading about in, in the latest releases that I will definitely give, uh, give them a more,
[1259.78 --> 1267.22]  um, careful consideration because you can now do things like, uh, partially commit a file. So
[1267.70 --> 1274.18]  let's say if you change a few things in a file and you, you don't want to commit the whole, uh, file.
[1274.18 --> 1279.94]  Now you, you can just select the areas that you want and you can commit that and then have the rest of the
[1279.94 --> 1285.46]  the file not committed, which sounds pretty interesting. Uh, if, if you have a workflow
[1285.46 --> 1291.78]  where you add, let's say debugging functions or some, some debugging values, but you don't want to
[1291.78 --> 1297.86]  commit them. Um, that's so interesting. Yeah. I've actually, I'm on a different context,
[1297.86 --> 1301.78]  but I might be working on, let's say like a SAS document and I'm writing styles for,
[1301.78 --> 1306.98]  let's say changelaw.com or something. And I don't want to commit every new rule set that I've changed.
[1306.98 --> 1313.94]  I only want to commit, you know, these five lines. I'm, I'm with you. Like the partial committing
[1313.94 --> 1319.06]  is really, really interesting to me because I don't even know if I know or could under,
[1319.06 --> 1326.66]  could remember the syntax to get to do that in the terminal. Oh yeah. That, that, that's the,
[1326.66 --> 1332.42]  the problem for me as well. Like I, I wouldn't figure out the, the whole syntax at all. And there are
[1332.42 --> 1338.18]  other things as well, like task management, for example, which allows you to work on various
[1338.18 --> 1347.46]  tickets and group them in work units so that you can quickly switch between, um, let's say, uh, one,
[1347.46 --> 1354.82]  one task and another, uh, with just a click of a button or, um, yeah, you'll have all the changes done
[1354.82 --> 1360.34]  there. I didn't even know you could do that. Are you talking about commits or tracking?
[1360.34 --> 1367.62]  Uh, so neither of them, like you've, let's say for example, you're working on a certain task right
[1367.62 --> 1373.78]  now, uh, and then someone else comes to you quickly and you want, uh, ask you to do something.
[1373.78 --> 1377.94]  You can basically tell the ID, okay, these, these are the changes that I'm doing,
[1379.38 --> 1385.38]  mark them as such, and let's start a new, uh, session to, to edit the code.
[1385.38 --> 1391.86]  And this session will be, let's say a debugging session or, or something that you, you showed
[1391.86 --> 1400.42]  to the person and you, you can basically have, um, two, two different change sets, uh, at the same
[1400.42 --> 1408.66]  time, not interfering with each other as of the, the latest, um, version allowing you to, to basically
[1408.66 --> 1411.94]  work on two tasks in the same file. Let's say if you want.
[1411.94 --> 1416.26]  And you're not branching anything. It's just, that's something that the idea is doing.
[1417.06 --> 1418.10]  Yes, pretty much.
[1418.10 --> 1419.14]  That's pretty cool. Yeah.
[1419.14 --> 1424.98]  I'm looking at the, the UI for this too. It looks like what happens is you can select
[1424.98 --> 1429.78]  certain lines and say, you know, I want to commit these, you know, these lines. And then it looks
[1429.78 --> 1434.74]  like you get the option to like check boxes in the diff and the gutter of the diff. So you can say like,
[1434.74 --> 1439.30]  I want these changes. Cause you're looking at the diff to say, what should I commit? At least it,
[1439.30 --> 1444.10]  it seems that way from what I'm seeing here. And you can say, I want to just commit these four lines
[1444.10 --> 1448.74]  here. And you check the box next to the diff that says, this is what's being added versus like, you
[1448.74 --> 1454.18]  know, the, the track version versus your version. And, you know, boom, you put that into the, you commit
[1454.18 --> 1460.42]  that and ship it up to a branch or whatever you're doing to master. If you got that and life moves on.
[1460.42 --> 1465.54]  Yeah. Pretty much. That's, that's the workflow that you have.
[1465.54 --> 1469.70]  Yeah. I think, you know, if we're asking the question of like, how do you choose
[1470.90 --> 1476.18]  which editor? I mean, that would, that's a never ending war that will always go on. But when you
[1476.18 --> 1482.34]  add the, the three letters, I D E after something, you know, it's, it stands for, you know, much more
[1482.34 --> 1487.54]  than just simply saying, Hey, this is an editor. This is an integrated tool and integrated development
[1487.54 --> 1491.54]  environment. As a matter of fact, it's what it, what it means. But you know, why, uh,
[1491.54 --> 1495.78]  why do you think somebody chooses, let's say an IDE or not like Carly, see in your case,
[1495.78 --> 1500.26]  you're, you're using VS code. It works great for go. But as you said, uh, to your own admission,
[1500.26 --> 1504.90]  you haven't really given it, you haven't souped it up as you had said, you know, so you didn't make
[1504.90 --> 1511.62]  it have any special powers to make developing go programs or go languages, you know, based projects,
[1511.62 --> 1516.26]  any easier for yourself, you know, auto completion, different stuff like that. Why do you think
[1516.26 --> 1522.90]  that, do you think an IDE is for a beginner, for a novice? Is it for an expert? Like who,
[1522.90 --> 1527.94]  who uses an IDE and why do they choose an IDE over say anything else that isn't?
[1527.94 --> 1530.58]  I don't even like this question.
[1535.94 --> 1544.26]  An IDE is for anybody. I, I mean, I see people who are extremely experienced using IDs
[1544.26 --> 1552.02]  and I see, you know, obviously IDs are for beginners. And I think, um, um, especially an
[1552.02 --> 1558.34]  IDE that lets you get off the, off the ground running with not much thought, like VS code,
[1558.34 --> 1565.86]  this one, um, is great for beginners because you don't need to, uh, you know, you're not required
[1565.86 --> 1571.78]  to learn a bunch of things and then you can soup it up as you go along, as you find the need for things.
[1571.78 --> 1579.54]  Um, and it just, an IDE makes a lot of things easier, uh, rather than, I don't know, what would
[1579.54 --> 1582.26]  you, what was the alternative? Like notepad?
[1582.26 --> 1586.90]  Well, it's kind of a trick question. It's kind of a trick question. The reason why I say that is
[1586.90 --> 1593.62]  because it's like, to me, um, you can be a purist and revolt, right? I'm command line only,
[1593.62 --> 1598.90]  or I'm Vim only. Take it from me. If Brian was here, he'd be saying that. I'm sure. Uh,
[1598.90 --> 1603.46]  I've heard him say it before. Uh, so I'm just emulating him in that, in that, uh, in that fact,
[1603.46 --> 1610.26]  but, um, you got somebody who's, who's just wants to be efficient. That's how I think of it.
[1610.82 --> 1616.90]  You know, I've over my years of, of working on projects, I started out as a purist and over time,
[1616.90 --> 1623.78]  I actually said this other day, I started out as a purist and now I'm a pragmatist, right? And that
[1623.78 --> 1630.10]  just means that I'm doing it the long form way because I know how to use get on the command line,
[1630.10 --> 1634.82]  for example, or I know how to do this. Cause I know all the documentation or this function or
[1634.82 --> 1639.30]  whatever it might be. I know it by heart. So I'm going to hand type it. Don't auto complete
[1639.30 --> 1642.82]  anything for me. Cause I want to make sure every character is the way I want it to be. So it's
[1642.82 --> 1648.10]  control. Then you got the other side, which is like, well, I just want to not save time. Cause I got
[1648.10 --> 1652.98]  family or a life or other things. I don't know. You just want to be more efficient. So to me,
[1652.98 --> 1659.54]  it seems like now my opinions towards IDEs have changed that may be there for people who care
[1659.54 --> 1664.74]  about efficiency rather than simply saying you're a new person or you're a expert or whatever.
[1664.74 --> 1671.78]  Yeah. In my case in specific, in regards to get and how I use get in the command line and not in my
[1671.78 --> 1677.94]  ID is because I learned getting the command line. So it's sort of like laziness because for me to use
[1677.94 --> 1682.58]  the idea, I have now I have to learn how the, that this particular idea works in me in who knows,
[1682.58 --> 1686.58]  maybe tomorrow I'm changing ID. Cause it's a thing that I do. I change it. I for once in a while,
[1686.58 --> 1692.98]  then now I have to learn the other one. And if I don't use, keep using the command line, I'll forget.
[1693.62 --> 1698.02]  And then all of a sudden I need to use it on the command line. Oh, how do I do that again?
[1698.02 --> 1702.90]  So for me, it's pragmatic to keep using it because I already know and I don't want to forget.
[1702.90 --> 1710.34]  Yeah. And, and I like your contrast between a purist and pragmatic. And I also, I also moved
[1710.34 --> 1717.78]  from being a purist and purest in the sense of having consistency. Like if I have, if I'm using
[1717.78 --> 1723.86]  one ID, I have to put all my efforts into learning everything about this idea or whatever, like a
[1723.86 --> 1728.82]  Vim, for example, I went through a phase where I was trying to just use Vim and I learned a ton,
[1728.82 --> 1735.38]  but that didn't work for me because, and let me just finish my, my, my, uh, observation about
[1735.38 --> 1742.58]  contrasting purist versus pragmatic because now I'm, I'm more pragmatic and I say, why just use one,
[1742.58 --> 1748.42]  use both, use two, use three. You don't have to just use one tool that does the same thing. So
[1749.62 --> 1756.18]  I use my idea always has a Vim integration because Vim can be very, very productive. It can be a lot
[1756.18 --> 1761.62]  faster using Vim. So what happened to me when I was a purist, trying to be a purist and use just Vim,
[1762.42 --> 1768.58]  I would learn a bunch of commands, right? That I use all the time. And then I have to open a new file
[1768.58 --> 1774.58]  or I have to like move a file. And I'm like, how do I do that again? Because I didn't do that very often.
[1775.38 --> 1781.14]  You know, like I am moving my cursor around. I'm doing that all the time. So, okay, I memorize
[1781.14 --> 1787.38]  those commands, but now I need to open a new file. Oh, I mean, when you're on a brand new project,
[1787.38 --> 1792.26]  you're doing that all the time, but when you're working with legacy, you're not doing that very
[1792.26 --> 1798.98]  often. So I just kept running to that wall. Like I couldn't do everything without banning my mind
[1798.98 --> 1802.90]  and trying to remember and looking things up all the time. So I was like, nah.
[1802.90 --> 1807.14]  How about you? How do you feel? How do you feel about this? What you're saying?
[1807.14 --> 1814.50]  Well, that's the thing. I feel that, you know, if it works for you, then yeah, that's the thing.
[1814.50 --> 1819.70]  Like you being productive is the most important thing at the end of the day, because as you said
[1819.70 --> 1825.70]  earlier, you may have family, you may have other things that you want to care about. And honestly,
[1825.70 --> 1832.26]  if you ask any of your users, they wouldn't care in which IDE or editor or command line you write.
[1832.26 --> 1838.82]  They just want their product to work. Right. So for me being efficient is trumps everything
[1838.82 --> 1844.66]  in terms of like, oh, no, my editor is cool. Oh, no, my IDE is better. Right.
[1844.66 --> 1851.22]  But that's not something that you should aim for. You should aim to have an environment that allows
[1851.22 --> 1857.70]  you to be as productive as you can be. And it helps you when you need to. It doesn't stand in your way.
[1857.70 --> 1863.30]  I like this productive as you can be. And I think let's pull in some some of the commentary here in
[1864.18 --> 1869.14]  inside of go time FM slack. So if you're listening to this in the aftermath, meaning it's produced,
[1869.14 --> 1874.26]  you're listening to another podcast feed, you can listen live every week. We broadcast live on Thursdays
[1874.82 --> 1880.34]  and you can have things like this mentioned on the show where Corey Linus says command line or bust
[1881.22 --> 1886.66]  typical. I like that. So he's definitely a fan of Brian. He's he's he's in that vein of like
[1887.62 --> 1894.74]  take it from me. I dare you. And then you've got other comments. This one is from Fernando.
[1895.94 --> 1901.14]  What's he seeing here? He's saying I basically use VS code for projects, which I like this this idea here.
[1901.14 --> 1906.42]  I use VS code for projects and any single file one off editing, maybe something that's happening inside a terminal.
[1906.82 --> 1911.70]  I'll just pop it up in Vim. So it's like I'm going to use the tool that's available for me in the right context.
[1911.70 --> 1915.94]  Maybe I don't know everything about Vim and I could just use it for quick in and outs.
[1915.94 --> 1920.74]  That makes sense because Vim's everywhere pretty much, you know, using the tools that are that are
[1920.74 --> 1925.38]  available to you to make and make it efficient. But, you know, go specifically programming and go,
[1926.02 --> 1932.34]  you know, you may want to use something that's a bit more souped up in Carlyseus terms for for you.
[1932.34 --> 1937.14]  So who else? There's some others. There's some other mentions of Git.
[1938.18 --> 1945.30]  You got towers, a tool for using Git. You've got something else we just mentioned was it's mad
[1946.26 --> 1950.50]  maggot. That's kind of a weird name for a project is magic, but maggot.
[1951.54 --> 1953.86]  I don't know if that's how you pronounce it, but that's what it says.
[1953.86 --> 1960.66]  Oh, yeah. It's the Emacs integration. I've I've heard people that, you know, they use that and
[1960.66 --> 1963.62]  then forget how to use the command line.
[1964.50 --> 1968.34]  Well, basically saying, you know, the different tools can be souped up. As you said, Carlyse,
[1968.34 --> 1971.38]  you can you can do some stuff to VS Code. You can do some stuff to Vim. Obviously,
[1972.26 --> 1975.70]  there's endless ways you can, you know, fine tune Vim to your control.
[1975.70 --> 1980.26]  Everything can be souped up. But an IDE seems to be
[1981.62 --> 1985.78]  specifically souped up for a particular language and or workflow.
[1987.46 --> 1994.82]  Yeah. And if you if you think about it, like, I know this is something that not many people want to
[1994.82 --> 2002.42]  acknowledge. But as soon as you start your customizing your Vim or Emacs or whatever setup you have,
[2002.42 --> 2007.14]  it becomes pretty much an IDE because it's your integrated development environment, right?
[2007.70 --> 2013.78]  You configure it the way you want. You add any plugins, any workflows you want. And that's pretty
[2013.78 --> 2020.34]  much it. With something like GoLand, you kind of take all that integration and you adapt
[2022.34 --> 2030.50]  that integration to your workflow. You say, oh, no, I don't want, let's say, automatic commits or whatever.
[2030.50 --> 2036.90]  You turn that off or you turn it on if you want it and so on. So the integration is already there.
[2036.90 --> 2039.70]  You just need to tell it how to behave for you.
[2039.70 --> 2047.54]  Can you export those settings? Can you have everything in the file? Because with Vim, it's true
[2047.54 --> 2051.30]  what you said, but at least you can have all of that configuration in one place and you can
[2051.94 --> 2055.46]  move it around machines. And that's sort of easy to do.
[2055.46 --> 2062.34]  Oh yeah, you can definitely do that. And there's actually now a plugin that I think we bundle in
[2063.62 --> 2069.30]  by default. I'm not really sure how the default setup looks anymore, but you basically have a plugin
[2069.30 --> 2076.98]  which is meant for syncing your settings in the cloud. So basically whatever you configure in one
[2076.98 --> 2085.14]  machine from the key mapping to what plugins you use and so on, whenever you, let's say, go home,
[2085.14 --> 2089.86]  you can have the same setup synchronized via the cloud.
[2089.86 --> 2092.34]  What's that plugin name? Do you know the name?
[2092.34 --> 2098.66]  I think it's the ID sync settings. I'll give it to you in a minute.
[2098.66 --> 2098.98]  Gotcha.
[2098.98 --> 2100.18]  I just don't have it right now.
[2100.18 --> 2100.26]  Yeah.
[2100.26 --> 2100.82]  Yeah.
[2100.82 --> 2107.54]  That's interesting. So, I mean, that's something I do, uh, back to the purist method is like most
[2107.54 --> 2113.86]  hardcore developers, I use dot files and I do my best to commit any changes to my dot files,
[2114.50 --> 2119.70]  back to my dot files repo and manually. I don't know if there's an automatic way to do this,
[2119.70 --> 2123.46]  but I manually sync those things up. So I tend to go back and forth from a
[2123.46 --> 2130.82]  iMac pro to a MacBook pro when I'm mobile and I do code on both. And, uh, in my case,
[2130.82 --> 2136.58]  I use VS code and I have those settings that you're talking about, Carlicia synced to my dot
[2136.58 --> 2142.98]  files. So I actually have them remapped. Um, let me recall what, what tool I'm, I'm using for that.
[2142.98 --> 2147.22]  I'll think about that here in a second, but essentially just sync my stuff through dot files
[2147.22 --> 2151.14]  and it's a manual process and there's times when they're out of sync and I'm not sure if they are
[2151.14 --> 2155.70]  in sync. So having some sort of cloud integration sounds kind of nice, but it takes that purist
[2155.70 --> 2160.18]  method away. It now it's pragmatists. It's like, well, I guess I can use the cloud, right? The cloud
[2160.18 --> 2160.90]  never lies.
[2160.90 --> 2167.86]  Oh, it's there for you to use, right? Like why not use it? We program on the cloud most of the time
[2167.86 --> 2175.22]  these days, or at least we, we hear about the cloud. So might just as well use it for your editor as well.
[2175.22 --> 2184.02]  Mm-hmm. Might as well. Huh? Yeah. It's called the ID settings sync. And I think it's bundled in by
[2184.02 --> 2190.34]  default because you can't uninstall it. Yeah. I was hoping to find this real quick. I use this one
[2190.34 --> 2199.06]  thing from ThoughtBot. If you've heard of ThoughtBot's laptop project on GitHub, it's great for setting up a
[2199.06 --> 2205.46]  new machine. But as part of laptop, they've done some other things to make, you know, new dev environments
[2205.46 --> 2212.26]  easy to not only create, but also to, you know, pull in .files and such. So they have this pretty
[2212.26 --> 2217.82]  interesting project that I can't recall the name of it now, but I'll find it and I'll put it in the show
[2217.82 --> 2219.14]  notes. If you're listening to the show notes.
[2219.14 --> 2238.26]  This episode of GoTime is brought to you by ActiveState. ActiveState gives you a faster way to build
[2238.26 --> 2244.02]  and secure open source runtimes from your first line of code on through to production. Every second you
[2244.02 --> 2250.02]  spend building your GoDistro or open source language distro is less time spent on doing the work you
[2250.02 --> 2254.98]  love. You got better things to do. You know it. I know it. And with ActiveState, you can focus on your
[2254.98 --> 2260.10]  code and leave the open source to them. Your teams can standardize with Go builds from ActiveState for
[2260.10 --> 2265.22]  your specific use. You'll have less friction in the development cycle, and that means you can deliver
[2265.22 --> 2272.82]  apps faster. Try ActiveState and see why it was chosen by IBM, Microsoft, NASA, Siemens, PepsiCo,
[2272.82 --> 2278.42]  and more. Discover for yourself why millions of developers trust ActiveState to build their
[2278.42 --> 2283.70]  open source language distros. Check them out at ActiveState.com slash GoTime. Once again,
[2283.70 --> 2285.78]  ActiveState.com slash GoTime.
[2302.82 --> 2309.86]  Let's move on. Let's talk about some of the things you've done. From what I understand,
[2309.86 --> 2314.34]  how long has the Slack community been in place, the Go4 Slack? A couple years now? Five years?
[2314.34 --> 2316.98]  I think roughly four years.
[2316.98 --> 2317.70]  Four years.
[2317.70 --> 2321.94]  No less than four years, for sure. Maybe five years.
[2321.94 --> 2322.58]  Five years.
[2322.58 --> 2325.94]  Bill Kennedy would know. I think he was the one who started it.
[2325.94 --> 2330.02]  Oh yeah, he's the one that started the whole thing.
[2332.10 --> 2339.46]  And Tim just dropped a little link in there, and what I was thinking was called RCM. So going
[2339.46 --> 2343.86]  back to what I just said, so I'm going to bring it back real quick. It's RCFile.management is what
[2343.86 --> 2348.74]  that is. It's from ThoughtBot. So check that project out. It'll be in the show notes.
[2348.74 --> 2356.74]  So four years. Who started this? Was it one person? Was it a ghost? Who did this? Who made this place possible?
[2357.86 --> 2359.22]  I think it was Bill Kennedy.
[2360.58 --> 2369.78]  Oh yeah, it was Bill and a few others that started the whole thing, which grew up immensely in the last
[2369.78 --> 2377.86]  couple of years, actually. And it's been a while since I looked, but wow. Okay. This is a lot more than
[2377.86 --> 2385.78]  than several years ago when I joined. 25,823 as of this recording. That's how many people were in
[2385.78 --> 2389.30]  general, which probably means that's how many people are in the community in general, right?
[2389.30 --> 2393.54]  Because general is the primary channel. And I think you have to actually, can you actually
[2393.54 --> 2397.94]  even leave general? You can't leave general. No, unfortunately, Slack doesn't allow you to
[2397.94 --> 2404.66]  do that. But you can mute it. Yeah. You can mute it if you want. Okay. Why would you want to do that?
[2404.66 --> 2410.82]  Well, maybe you're there for, you know, one of the channels rather than the, the, the, you know,
[2410.82 --> 2414.10]  I look at this kind of like Twitter, you know, general is the firehose.
[2414.58 --> 2417.46]  I'm joking. It's muted for me. It's too much.
[2417.62 --> 2419.06]  Too hard to keep up with. I mean, you'll just.
[2419.26 --> 2420.02]  It's impossible.
[2420.52 --> 2424.90]  Yeah. Well, it's for one, it just would sound off all the time unless you've got it muted. It's not
[2424.90 --> 2428.54]  muting because you're like, I don't want to listen. It's just more like, don't tell me every time
[2428.54 --> 2432.48]  something's happening because I will literally never get work done. I would just sit here and watch general
[2432.48 --> 2437.12]  all day long and be like, Hey, what'd you do today? Uh, I was in go for Slack watch in general.
[2437.92 --> 2446.64]  Yeah. But Florin does watch it frequently. Right. And actually that is one of the things that I
[2446.64 --> 2455.20]  wanted to ask, um, how you have seen the character of go for Slack changing over these years. Cause
[2455.20 --> 2461.36]  you're super active. Well, that's the thing. Like I don't think it changed that much because
[2461.92 --> 2467.68]  if you look at the community, it's probably one of the best communities out there. I just love it.
[2467.68 --> 2474.56]  It's all the people here are friendly. They, uh, help you whenever you have a problem or you're trying
[2474.56 --> 2481.12]  to, to work through something either. If you're complete beginner, not necessarily with go, but
[2481.12 --> 2488.56]  like with programming or a go newbie, um, or even someone that's, you know, more experienced that
[2488.56 --> 2495.92]  can come in either ask in general or in goal and newbies or in any of the dedicated channels we have
[2495.92 --> 2501.92]  here and people will be there, uh, guiding you or, you know, if they don't know the answer,
[2501.92 --> 2508.88]  they would at least point you to, let's say the mailing list or the, the go tracker, or who knows what
[2508.88 --> 2514.48]  other resource it's available that explains the, uh, how to solve your particular need.
[2516.24 --> 2523.36]  And that's, that's something that that's really cool. I'm happy that I found this community, uh,
[2523.36 --> 2529.84]  when I did. And even though it looks a bit scary when, when you say, Oh, there's like 26,000 people
[2529.84 --> 2536.40]  in general, I'm not going to ask a question because who knows who's watching. I mean, I'm not good enough to,
[2536.40 --> 2543.52]  to answer. Like nobody should feel like that because everybody's here to, to help each other
[2544.32 --> 2546.88]  and to, to learn from each other. And that's great.
[2548.32 --> 2554.40]  Do you guys feel like Slack is the, you know, not so much the epicenter, or at least one of maybe
[2554.40 --> 2559.04]  several epicenters you got obviously face-to-face meetups, you got conferences, you got different
[2559.04 --> 2565.20]  things happening, but do you feel like go for Slack is the place to be if you are a go programmer?
[2565.20 --> 2572.96]  I would say yes. Do you feel like if you're not in it, you're missing out?
[2572.96 --> 2577.36]  Uh, it, it depends. Go ahead, Kyrlissia.
[2580.00 --> 2585.60]  Dying to jump in. I wouldn't say that. I wouldn't say that, especially because people have different
[2585.60 --> 2591.12]  modes of working. That is sort of like saying, if you're not on Twitter, you're not a real, like you,
[2591.12 --> 2596.64]  you, you, you not a real developer. Cause I think that's what the question, how the question was
[2596.64 --> 2601.60]  first phrased. Well, not so much they're not a real developer, but just like if they're missing
[2601.60 --> 2605.52]  out, like what I'm trying to get at is like, is this the place to be? Should you be here?
[2605.52 --> 2612.80]  Definitely missing out. Yes. Yes. Because a lot, a lot of conversation happens and a lot of
[2612.80 --> 2619.44]  connections happen on go for Slack. And if you're not participating, you're missing out. Yeah. But
[2619.44 --> 2625.44]  that doesn't mean you're not getting connections and getting benefits from other, um, from other
[2626.16 --> 2634.00]  venues or channels. Um, but definitely missing out. There's a lot, just the volume that goes through
[2634.00 --> 2642.40]  the go for Slack is crazy. They in the job, champ jobs channel. Um, there's so many channels.
[2643.28 --> 2649.44]  There's something for everybody. Oh yeah. There's like a review channel. If you want to have your
[2649.44 --> 2656.16]  code reviewed by people, you can come here and ask for a review and people will do it. Like it doesn't
[2656.16 --> 2662.80]  really matter how big the project is or anything like that. While we're trying to invite people,
[2662.80 --> 2669.60]  I'm seeing Bill Kennedy, uh, in Slack mentioned, he says, uh, and quote, uh, not everyone can
[2669.60 --> 2673.84]  participate here because of our code of conduct rules. The ML is very powerful. I didn't know there
[2673.84 --> 2679.44]  was machine learning behind the scenes on this, but, uh, can somebody clue me into what he's talking
[2679.44 --> 2686.32]  about here? Oh, so he's, uh, referring to the code of conduct that we have and to the, uh,
[2686.32 --> 2691.28]  go on, uh, mailing mailing list. When you say ML, I'm thinking machine learning. Okay. Just so you
[2691.28 --> 2697.36]  know. No, we, we refer to it as the go on knots and go on dev. Gotcha.
[2697.36 --> 2703.44]  I was like, dang, the, the, we got machine learning behind the code of conduct and getting
[2703.44 --> 2711.04]  into this go for select. That's a lot. Anyways, uh, my bad acronym replace with men list moving on.
[2711.04 --> 2717.76]  All right. So who, who, what does this mean? Who can't participate then? Like what, what is it
[2717.76 --> 2722.72]  filtering out? Like particular people or particular types of people or just, just things you shouldn't
[2722.72 --> 2729.12]  do? Some people don't participate because they don't agree with the code of conduct or, or they
[2729.12 --> 2736.88]  infringe on the code of conduct, code of conduct. And some people do that not knowing. And you know,
[2736.88 --> 2743.20]  there are a bunch of admins who are active participants on Slack and the, there is a series
[2743.20 --> 2748.88]  of, there is a procedure to handle that. Right. So the first step is to let the person know, Hey,
[2748.88 --> 2753.52]  you know, you're saying this and we have a code of conduct and that, that goes against the code of
[2753.52 --> 2760.88]  conduct. Most people are like, Oh, I'm so sorry. I did not know. And they, they, we asked them to
[2760.88 --> 2768.88]  edit or delete whatever was infringement and they happy to do it and they happy to be informed and
[2768.88 --> 2775.60]  not, so they don't continue to infringe. Right. And it's a very rare minority will rebel against
[2775.60 --> 2784.56]  they will not comply and they have to be removed from the space. And if they don't agree to abide,
[2784.56 --> 2792.16]  they can't rejoin because the same thing will keep happening. The suspensions happen in perpetuity or
[2792.16 --> 2798.88]  is it temporary suspensions? How does, how do these things get decided and how much work is it for the
[2798.88 --> 2806.72]  individuals involved? Um, it depends on a case by case basis, I guess. Uh, some of them are just like,
[2806.72 --> 2815.04]  you know, maybe we will say, Hey, you needed to call off, take a few days off, uh, come back later.
[2815.76 --> 2822.88]  Or some of them are more permanent because you know, they really go well beyond the code of conduct or,
[2823.44 --> 2829.60]  you know, common sense because that's what it really is. At the end of the day, we try to be as
[2829.60 --> 2838.00]  inclusive as possible here and welcome everyone to join us and learn, but sometimes people
[2839.84 --> 2847.12]  infringe on it. Yes. And I'm also an admin. So I participate in this conversation and that's how
[2847.12 --> 2854.48]  I can pipe in. Uh, we don't have, we are volunteers, right? And we don't have a tool to suspend people and
[2854.48 --> 2859.36]  keep track of that. So what we can say is we're giving, we are letting you know, and people usually
[2859.36 --> 2864.56]  comply. In some cases we say, we, we're letting you know, and the person still, you know, doesn't
[2864.56 --> 2869.84]  calm down or, and we say, Hey, you know, we're giving, you know, giving you a warning. We're going to let
[2869.84 --> 2876.96]  it go this time. Right. And if it, it really depends on the situation. So if we, if the
[2878.24 --> 2882.16]  infraction, I would say infringement, if the infraction reoccurs,
[2882.16 --> 2886.48]  or maybe sometimes we say, if it happens again, we're going to have to kick you out.
[2886.48 --> 2888.40]  Yeah. So it's sort of like
[2888.40 --> 2892.00]  Alas, the jet for it basically. Yeah.
[2892.00 --> 2894.00]  You're giving them several chances to correct.
[2894.00 --> 2899.92]  The middle of the road there is that we, we warned that we're going to give them another chance.
[2899.92 --> 2905.76]  Otherwise we don't have a way to just suspend and for 30 days and then check if, you know,
[2905.76 --> 2909.44]  who needs to be brought back in. You're going to have to be kicked out.
[2909.44 --> 2913.12]  So do you, by saying that then, so there's no list of who
[2914.24 --> 2919.04]  is banned or has been removed for whatever reason, there's no tracking of these things.
[2919.04 --> 2923.68]  So it's sort of like a personal scenario where you have a small collective, I'm just assuming this,
[2923.68 --> 2928.48]  you got a small collective of people who are admins and you've got memory and you're using your memory
[2928.48 --> 2933.44]  to, to recall people's infringements. You're not keeping lists or tabs on people basically.
[2933.44 --> 2940.80]  No, no, exactly. And also it wouldn't make sense because we don't have a requirement that people
[2940.80 --> 2947.92]  use their real name so they can join with a different username and name and you'll be,
[2947.92 --> 2951.36]  I think it'll be a waste of time. If people really want to
[2951.36 --> 2959.20]  do with speech, whatever, whatever way they want to speak, they can, they have resources,
[2959.20 --> 2964.16]  recourse, they can just join in with a different accounts. But so it's really,
[2964.16 --> 2966.32]  we just need to be on top of it all the time.
[2966.32 --> 2967.04]  Yeah.
[2967.04 --> 2971.28]  Switching gears a little bit. Go ahead, Florin, if you got, if you want to mention something.
[2971.28 --> 2978.00]  Sorry. So yeah, I was actually reading the chat here and Bill says that we have the message history,
[2978.00 --> 2983.68]  which is true. Pretty much we, we have the history from the beginning of this Slack. So
[2983.68 --> 2990.32]  roughly four or five years of messages. And we have a private room where all the admins are
[2991.28 --> 2999.28]  chatting together. And whenever an incident comes up, we, we talk together there, but you also, for
[2999.28 --> 3006.40]  example, if someone notices something when, whenever we, we don't look, you can either ping us directly
[3006.40 --> 3015.52]  or you have a channel called admin help, admin dash help. And that's how we, we have a history of what
[3015.52 --> 3021.52]  happened because yeah, we, we are humanists as well. And as Carlesias said, volunteers.
[3021.52 --> 3028.88]  Yeah. And, and every other, uh, the admins, we have an understanding that we, whenever we approach
[3028.88 --> 3036.48]  people, first of all, we do it in private, um, and we do it with taking that the, with the
[3036.48 --> 3044.88]  understanding that with intention of, how do I want to say this? Help me for, and we think that we,
[3044.88 --> 3049.76]  we start out thinking that the person didn't want, didn't know about the code of conduct or needs a
[3049.76 --> 3056.00]  little bit of guidance. We would never try to shame or say, Oh, you did wrong. And that was so wrong.
[3056.00 --> 3061.60]  It is. That's not what it's about. It's really about keeping the space safe for everybody and
[3061.60 --> 3066.96]  comfortable and kid friendly. Although that's debatable, what kid friendly should be, but
[3069.20 --> 3069.84]  Yeah, it's tough.
[3069.84 --> 3077.44]  Yeah. Pretty much. That's the hardest part. Like trying to make sure that, you know, we give as much
[3077.44 --> 3084.16]  opportunity to people to express themselves, but at the same time, not making it so in an uncomfortable
[3084.16 --> 3091.60]  manner for others. And, uh, yeah, we are fortunate enough that these kinds of things happen very
[3091.60 --> 3100.32]  rarely, like probably once a month or less where we actually need to take action against anything here.
[3101.84 --> 3107.76]  Maybe since we're talking about the, you know, earlier on in this conversation, how the numbers of
[3107.76 --> 3114.08]  people involved in go for slack have grown over the years, uh, it's kind of keying into evolution.
[3114.32 --> 3119.36]  You know, maybe we could talk about the other point here, which is how the community compares to maybe
[3119.60 --> 3123.76]  other languages. Maybe that speaks to maturity in terms of like the community and the
[3124.40 --> 3127.36]  different tool sets around it. What do you, what do you all feel around
[3128.24 --> 3132.72]  what helps this community be a good community? You know, not, not so much just go for slack, but the conferences,
[3132.72 --> 3139.04]  how do you feel the go community compares to other languages? Good and bad.
[3140.48 --> 3146.48]  So, um, at least from, from what I can see in, in our community, um, pretty much everything starts
[3146.48 --> 3152.88]  from the top and like the people that started the language behaved in a certain way. Then, you know,
[3152.88 --> 3161.52]  when the language started to grow, the type of persons that got into the language were in of a certain,
[3161.52 --> 3169.28]  uh, manner, right? Of a certain behavior. And I think that's something that, um, persisted throughout
[3169.28 --> 3178.00]  its growth phase until now. Um, I, I generally feel that there's not much difference between what we
[3178.00 --> 3184.56]  have today in the go community and what we had maybe three, four years ago, just because
[3184.56 --> 3191.36]  whenever people come in, let's say in contact with the mailing list or with the go for slack,
[3192.00 --> 3198.56]  they see that kind of behavior. And at some point people will just try to emulate what they see. And
[3198.56 --> 3203.36]  if, you know, all they see is some, someone being friendly to them, someone being helpful,
[3204.08 --> 3210.72]  uh, giving them the respect they deserve, but they will do the same for the next person that comes in and
[3210.72 --> 3218.72]  uh, joins the community. And other languages, I, uh, I guess, uh, at some point they grow
[3220.16 --> 3227.20]  a lot bigger than what we currently have in go. I, I still think we are maybe, uh, let's say small
[3227.20 --> 3236.72]  to medium community. Right. And we are not as big as let's say the, maybe C plus plus or C community, or
[3236.72 --> 3245.12]  maybe even other scripting languages. Right. So there you have a lot more people. Uh, I don't know
[3245.12 --> 3254.56]  if they grew in the same way as the go community grew or it's maybe just because go happened. So
[3255.44 --> 3262.80]  recently compared to the others, and we are just able to, to teach go first as part of becoming go
[3262.80 --> 3268.64]  programmers, not only to, to be programmers, but also be nice to each other and good community
[3268.64 --> 3278.08]  members, good citizens. Yeah. That makes sense. What, what do you think? You know, when I look at
[3278.08 --> 3282.72]  the good community, what I like most about it, or at least the, you know, let's say an outsider's
[3282.72 --> 3288.00]  perspective, cause I still feel like an outsider. Um, even though I've kind of been involved, I go to
[3288.00 --> 3293.76]  every go for con since the second one, I don't miss a go for con. I'm part of this cast here for
[3293.76 --> 3300.88]  this podcast and stuff. And, but I still feel like an outsider. But what I, what I see is I just tend to
[3300.88 --> 3309.36]  see people who are encouraging, uh, welcoming and, and just general care for others. And I'm not saying
[3309.36 --> 3313.12]  I don't see that elsewhere. I'm just not, I'm more involved in this community than I would say others.
[3313.12 --> 3318.48]  So I can't say it's a comparison to say, this is how it is here. And it's not that way there,
[3318.48 --> 3325.44]  but that's what I see as good attributes for this community is like, you just seem like you care
[3325.44 --> 3330.96]  about the future of the community, which has deep implications to how you act in the community.
[3330.96 --> 3339.44]  You agree? Yes, pretty much. I completely agree. And one thing to say too, is, um,
[3339.44 --> 3347.28]  um, when go guys started and when it goes to the community started growing, it was at a point where
[3348.32 --> 3356.40]  other communities had gone through a lot of experiences about, uh, dealing with harassment,
[3356.40 --> 3361.04]  dealing with infractions to code of conduct, or not even having a code of conduct,
[3361.04 --> 3365.20]  and dealing with the consequences of that. So when the goal community started developing,
[3365.20 --> 3372.00]  they got a lot of, they had all of that experience to, to inform them.
[3373.12 --> 3380.56]  So that was a big difference that go is a newer community. So it's really almost unfair to compare
[3381.44 --> 3385.28]  because we have the benefits of having that experience from other communities. Right.
[3385.28 --> 3389.52]  Yeah. You've had a chance to kind of restart, so to speak, even though you're not re anything,
[3389.52 --> 3395.28]  you're, you're just starting somewhat fresh because go is, goes about as old as the change long is.
[3395.28 --> 3397.60]  And we started around the same time, 2009 ish.
[3398.72 --> 3404.96]  Yeah. So you, you're starting out with the benefit of having information that other communities started
[3404.96 --> 3413.76]  out not having, because that just hadn't happened publicly enough to really come into consciousness.
[3413.76 --> 3414.96]  Right. Yeah.
[3414.96 --> 3419.60]  But the good thing about the goal community that I also, we can also not discredit it,
[3419.60 --> 3428.96]  what is the willingness to embrace that experience and say, we are going to avoid the, you know,
[3428.96 --> 3434.56]  we're going to avoid that at all costs. Like we're going to do everything we can to keep this community
[3434.56 --> 3445.68]  safe and inclusive and, uh, you know, for now and for the future. So that really deserves some big credits.
[3447.44 --> 3452.24]  And like, and like, and like for Lauren was saying, it comes from the top. So that really helps too.
[3454.08 --> 3460.72]  There's one note here to talk about, which, uh, Florence, it sounds like you've got some thoughts that you put into this,
[3460.72 --> 3466.56]  which is, uh, what I wish the good community will do going in the future. So what does that mean to you?
[3467.60 --> 3470.72]  And it's bold too. So I'm, I'm thinking like, maybe it's even more important to you.
[3471.92 --> 3480.08]  Well, uh, yeah, it's bold as in, you know, probably we, we should talk about it because we are here now.
[3480.08 --> 3486.40]  Right. And we drew a lot in, in the past years, uh, as a community as a whole. And I'm sure,
[3486.40 --> 3492.32]  you know, we, we just see a small portion of the community. We don't see necessarily all,
[3492.96 --> 3499.28]  all that's happening in the community outside of, let's say go for Slack or the main English. Not
[3499.28 --> 3507.60]  many people may join these places or, you know, uh, not many people may even speak, uh, English to,
[3507.60 --> 3515.60]  to be able to, to join, uh, these community. And I, I would really love to see, um, more people
[3515.60 --> 3521.44]  coming forward and, uh, helping them, uh, come forward and say, Hey, look, I'm a Go developer.
[3521.44 --> 3530.72]  I'm trying to learn Go and you know, my native languages, maybe let's say Romanian or some other
[3530.72 --> 3537.28]  language. Right. And be able to, to help them out with documentation in their language or be able to
[3537.28 --> 3548.32]  encourage them to speak at conferences, um, helping them move forward, uh, as a whole community. Right.
[3549.12 --> 3556.32]  Um, I was talking to, to Dave Cheney about this and he mentioned that, you know, the Go community in
[3556.32 --> 3564.72]  Asia is so big and we don't know so much about it because we don't really know how to interact well
[3564.72 --> 3570.24]  with that community. I would love to, to see more openness to, to that. I would love to,
[3571.12 --> 3576.64]  to benefit from their experience. Right. Because we have a lot of things that we can learn from there.
[3577.60 --> 3583.12]  And I would love to not have people write the HTTP routers anymore because that's getting old.
[3583.12 --> 3585.12]  Speaker 1
[3585.12 --> 3586.12]  Speaker 1
[3586.12 --> 3589.44]  Speaker 1 How are we missing out on China? What's the barrier there?
[3589.44 --> 3591.36]  Speaker 1
[3591.36 --> 3595.12]  Language only? Or is it the culture?
[3595.12 --> 3596.56]  Speaker 2
[3596.56 --> 3602.40]  Um, that's a good question. And that's something that would be interesting to, to solve because
[3603.20 --> 3607.92]  on one hand, yes, probably there is some, some language barriers. If you, if you look at,
[3607.92 --> 3614.00]  let's say all the resources that, that we have, the majority of them are in English, right?
[3614.00 --> 3614.24]  Yeah.
[3614.24 --> 3615.36]  Speaker 1
[3615.36 --> 3619.84]  So, and books that have to be translated take time, like documentation, even there's
[3619.84 --> 3624.72]  a translation process that, you know, things tend to happen in English. From what I understand,
[3624.72 --> 3630.32]  this is actually regurgitating some of a podcast I did before while at node interactive, uh,
[3630.32 --> 3636.32]  the language node, um, or I guess this is not even a language. It's more like, uh, something on top
[3636.32 --> 3641.68]  of anyways, node, the platform. I was at that conference and I was talking to, um,
[3642.80 --> 3647.20]  Shia Liu, who was actually talking about, she was from China, from Shanghai, and she was talking
[3647.20 --> 3652.88]  about the great firewall of China. And essentially it's in the case of JavaScript and node, but I
[3652.88 --> 3657.28]  think it applies probably for the Go community as well as that the barrier was, was a language
[3657.28 --> 3665.28]  difference in the fact that learning it and, you know, kind of keeping up, uh, was, uh, was a latency
[3665.28 --> 3673.44]  because of the translation process and the ability to communicate back and also the literal, uh, digital
[3674.32 --> 3680.08]  firewall that, uh, may or may not be in place between China and, uh, the rest of the internet.
[3680.08 --> 3688.48]  Yes. And I think that that's one of the nice things that, uh, the Go team and Google managed to do
[3688.48 --> 3696.08]  recently, probably a couple of months ago, they've, uh, they managed to take the golang.org and make it
[3696.08 --> 3704.56]  accessible in China. Right. And I know, uh, someone that I've met on go for Slack was, uh, he's from Iran
[3704.56 --> 3713.04]  and the same thing, like he couldn't access basic things like go doc.org. Right. And now he can,
[3713.92 --> 3720.80]  and that's pretty much great because now we have more people that can learn Go and we can learn from
[3720.80 --> 3727.76]  them as well. So, so yeah, that's the thing that those are some of the, the, the steps that I think
[3727.76 --> 3734.32]  we need to take. Translating books is another for sure. Um, being able to, to have more
[3734.32 --> 3744.00]  diversity, uh, in conferences, in, um, meetups in resources in general, or even if you think about,
[3744.72 --> 3752.00]  um, let's say, uh, online courses that we have, I, I would be interested to know how many courses are
[3752.00 --> 3760.08]  available in, not in English. Mm. Hmm. Yeah. I, I haven't seen any
[3760.08 --> 3768.40]  investigation that has been done to explore the question that you asked Adam, which was, um,
[3768.40 --> 3775.44]  what is the, what are the barriers? I think guessing that language is a big barrier, um,
[3776.56 --> 3783.44]  would be an easy answer to guess, right? I would guess that too. And because you can,
[3783.44 --> 3790.48]  I would say the, this is actually, we can verify this, but I would say the majority of people in
[3790.48 --> 3795.04]  China don't speak English and you can extrapolate that majority of programmers don't speak English
[3795.04 --> 3797.60]  by default, right? Statistically speaking.
[3797.60 --> 3802.16]  That's an assumption, I think. Uh, and I made that same assumption and, and the, I linked it up in the,
[3802.16 --> 3806.24]  in the Slack, but it'd also been the show notes. That was my assumption going into this conversation,
[3806.24 --> 3813.04]  which actually took place, you know, like December, 2016. So this is a two year old conversation
[3813.04 --> 3818.48]  roughly that I have with Shia Liu. And that, that was my assumption was that it was just simply a
[3818.48 --> 3824.96]  language barrier. In fact, many of the programmers or people pursuing programming careers and, or just as
[3824.96 --> 3832.16]  a hobby in China, a lot of China is bilingual or at least pursues bilingualism. Uh, but specifically
[3832.16 --> 3838.56]  programmers are forced in a lot of ways to not only, uh, have Chinese as their first language,
[3838.56 --> 3845.28]  but then English as their second, because, because that most of what happens in education and, or
[3846.16 --> 3850.72]  innovation happens in programming in English, you know, that's the limitation there.
[3850.72 --> 3856.72]  Yeah. You, we can talk in terms of many, and I would never disagree with that, but you, we can always
[3856.72 --> 3866.16]  say, I mean, we will have to look very closely and say, and explore, well, what really is happening.
[3866.16 --> 3871.12]  We can assume anything because you can say, oh, there are many. And a lot of people who are working
[3871.12 --> 3877.76]  with innovation are being forced to take English, but as in the private setting, or is that being taught
[3877.76 --> 3884.32]  in school, but it was a free. That's what I'm saying. Because if, if it's not free, if it's not free and
[3884.32 --> 3891.76]  accessible to everyone, then people are being excluded. And I think some of those people might
[3891.76 --> 3897.52]  be developers that would, could otherwise be learning or maybe having an easier time to learn
[3898.16 --> 3903.44]  the language and how to do things well properly and how to take it. In other words, how to take
[3903.44 --> 3909.60]  advantage fully of what the language has to offer. If that wasn't something that they were struggling
[3909.60 --> 3917.28]  with or they had to like pay a fortune for. So in that sense, unless it's being provided for free
[3918.00 --> 3923.12]  to all the potential programmers, programmer population, but in any case,
[3925.44 --> 3931.20]  if that was, but it is an assumption, right? I have not, I have zero knowledge about China in that
[3931.20 --> 3938.56]  regards. But so if that was the case, just take, for example, the survey that the Go language team
[3938.56 --> 3947.04]  puts out every year. That survey is in English. So anybody who's using Go or wants to like,
[3947.04 --> 3952.72]  he's using Go, was interested in using Go and doesn't know enough English to read that survey,
[3954.00 --> 3958.64]  won't be counted, accounted for, right? Their experiences, their opinions won't be accounted for
[3958.64 --> 3963.92]  because the result of that survey goes right back into the, to the Go language team for them to make
[3963.92 --> 3970.08]  decisions on how to develop the, everything around the language itself and everything around the language.
[3972.80 --> 3979.52]  I was trying to scan it really quick to see if, uh, if there was even an ask in this survey of like,
[3979.52 --> 3984.80]  what is your primary language and not programming language, but you know, speaking language.
[3984.80 --> 3985.76]  Yeah.
[3985.76 --> 3990.80]  Because it happens to Jared and I on the change often. And some, and in a couple of cases that
[3990.80 --> 3995.20]  happens accidentally where we don't even know until we didn't even consider it until afterwards,
[3995.20 --> 4000.64]  because we're just idiots sometimes. But we've had conversations with people that, uh,
[4001.60 --> 4005.92]  don't speak English firsthand. And we didn't realize that we actually had a full conversation.
[4005.92 --> 4009.92]  And at the end, they're like, Ooh, I'm tired. And we're like, why we're getting, we're just,
[4009.92 --> 4013.76]  we're, we're rearing to go. We're still excited. You know, we just had a great conversation.
[4013.76 --> 4018.00]  And I'm like, well, I just had to think really hard because my brain thinks in one language and
[4018.00 --> 4025.92]  I'm speaking in another, how, how fatiguing it is on somebody to, to real time, just in time,
[4025.92 --> 4030.56]  translate, uh, not to be, not to be, uh, drop that pun in there, but it's pretty good. It's like,
[4030.56 --> 4035.52]  just in time, you're sort of like, uh, real time translating your thoughts from one language to
[4035.52 --> 4040.88]  another and speaking and how fatiguing it is. But I think it'd be good to add that to the future
[4040.88 --> 4044.48]  surveys. Like, you know, cause it would, it wouldn't start to inform the community.
[4044.48 --> 4048.64]  Like we examined this a few podcasts back on this show where we were like, you know,
[4049.12 --> 4052.72]  what was the impact of the survey? What did we learn from it? And that's one thing we,
[4053.68 --> 4058.16]  at least I'm not seeing if somebody is, it's at least showing countries. So I mean,
[4058.16 --> 4064.96]  they could at least give you some indicators with 25% of the survey participants being in the
[4064.96 --> 4071.60]  United States of America. Uh, top five is us Germany, UK, Canada, France, and Russia. So
[4073.20 --> 4078.88]  that's a, how was that? Six. That was six. My bad. I can't count. That's zero base index.
[4080.40 --> 4084.96]  Uh, let's, let's move on a little bit. Anything to talk about more about this before we go into maybe
[4085.76 --> 4090.08]  projects and news or free software Friday, we got three minutes and 27 seconds.
[4090.08 --> 4098.56]  Yeah. I think one, one last thing that we can add here is it's, it's not just the, the language barrier,
[4098.56 --> 4105.12]  which maybe, but as Carlycia touched a bit at some point, it's also being able to have those resources
[4105.12 --> 4112.64]  maybe at a lower cost or for free, because, um, that's also a big part of, uh, being able to,
[4112.64 --> 4120.96]  to learn something. Um, some, sometimes you like for, for, let's say, uh, many people, $5 can be nothing,
[4121.52 --> 4130.48]  but for some of them can be maybe half a week or a week worth of food. Right. So yes, that there's also,
[4131.52 --> 4135.76]  this component as well, and many, many others. And it would be interesting that, you know, if the
[4135.76 --> 4143.76]  community starts thinking about those kinds of problems as well. Well, I mean, uh, not to elongate
[4143.76 --> 4149.36]  it a little further, but I'll say this as a, as a, as a response to that is, is I think it's important
[4149.36 --> 4154.96]  if you're going to say that to, to then maybe attach at least your own opinion on who might be
[4154.96 --> 4159.20]  responsible for making that happen. So is it the community's problem? Is it Google's problem?
[4159.20 --> 4164.64]  Because they primarily, you know, operate the language and, or a, a big artifact of the community.
[4165.44 --> 4171.60]  Um, because translations is not new to the web. It's a difficult thing to program around. It's a
[4171.60 --> 4177.12]  difficult thing for CMSs to deliver. And it's an even more difficult thing to do as a, as yet one
[4177.12 --> 4182.40]  more thing to do as a maintainer and, or author and, or educator to now not only communicate in your
[4182.40 --> 4188.48]  primary language, but then have the responsibility to translate it. So whose responsibility do you think
[4188.48 --> 4192.32]  this falls upon us as a community or, or who, and who pays for it?
[4193.20 --> 4199.84]  I, ideally, I think it would be us, the community because at a certain point, there's only so much
[4199.84 --> 4207.44]  Google can do. They should, uh, should help us for sure if possible, but we should start seeing some,
[4208.32 --> 4215.12]  some of this in the community just because it, it would show a, um, increase in the level of maturity
[4215.12 --> 4224.96]  for this, for the community. Right. Yeah. I guess, um, you have to think what is the desired outcome
[4224.96 --> 4230.96]  of the language, right? What is the purpose? What is trying, where are they, for example, ask the,
[4230.96 --> 4238.08]  what does the goal language team has in mind for the language? What do they want to accomplish and
[4238.08 --> 4243.92]  how do they want to accomplish? Uh, for me, an answer to that question in that to any question
[4243.92 --> 4249.84]  that applies to the community in general should, doesn't have to be one or the other. And I think
[4249.84 --> 4256.16]  it should be both, it should, should be a concert between, uh, concerted, how do you say that?
[4256.16 --> 4264.64]  Concorded efforts? Yeah, that's it. Right. Between the language team and the community and companies.
[4265.52 --> 4273.44]  Um, so for me, for example, I see that the language team should sort of like have a direction and help,
[4273.44 --> 4280.88]  could help kick things off and enable local communities to pick things up and run with the ball,
[4281.68 --> 4289.60]  so to speak. Uh, but just relying on just one or rely on the, just on, on, on the other. I don't see
[4289.60 --> 4296.00]  how that can work. I'll say this then to the listening audience and, and those who listen after this live
[4296.00 --> 4301.60]  show is like, if you're listening to this and you've got better answers than we do reach out. Like,
[4301.60 --> 4308.40]  if you know somebody who's actively working to translate and or expand beyond the English only
[4308.40 --> 4314.08]  language for documentation or translating to your localized language, if you've got somebody that's
[4314.08 --> 4318.00]  been doing this kind of work and they've got far more insight than we do, or maybe even better
[4318.00 --> 4324.32]  opinions, not that ours are bad, reach out please. And that'd be, that'd be good. I think that's that,
[4324.32 --> 4328.88]  that portion there could use, uh, some additional attention. Cause that's the hard part is like,
[4328.88 --> 4333.04]  you know, who does the work is always the hardest question to answer, right? Who does the work?
[4334.56 --> 4340.48]  All right. Um, free software Friday. Let's let's, I put three more minutes back on the clock.
[4341.04 --> 4346.16]  So we've got three minutes, we've got free software Friday and we got maybe some go news. So let's
[4346.16 --> 4350.32]  combine them. Uh, Carlos, you go first. Any news, any projects?
[4350.32 --> 4356.16]  I don't, I didn't get anything. No, any news. What kind of news? Any news?
[4359.52 --> 4361.84]  No news. All right. Florin, any news?
[4362.64 --> 4368.08]  I'm fortunately not for me. No news. All right. You gotta have a project at least. Give me a project.
[4368.08 --> 4371.04]  Well, a project for free software for Friday. I can definitely do.
[4371.04 --> 4377.92]  Okay. And it would be, what's impacting you? Well, it would be Delve, uh, the Go debugger, um,
[4377.92 --> 4384.56]  that's maintained by, uh, mostly by Derek and Alessandro. And they are doing a fantastic job to,
[4384.56 --> 4393.52]  to get that working. It's available in all editors that, uh, that we have today. And yeah,
[4393.52 --> 4400.80]  the amount of work and, uh, helpfulness from, from that team is, is just great. And thank you.
[4401.04 --> 4409.68]  For all the efforts behind it. Awesome. Well, I have no go news, but, uh, I do have a project that I
[4409.68 --> 4416.64]  just came upon today and I'm actually cheating because we did a live show. The first live show
[4416.64 --> 4423.68]  we did for JS party today, uh, just before go time. Uh, first one we've done in a while,
[4423.68 --> 4428.88]  cause we're just bringing it back, but I'm going to borrow what Christopher Hiller mentioned,
[4428.88 --> 4435.44]  which was going dark on GitHub. And I think this is super interesting because I love dark interfaces.
[4436.48 --> 4442.80]  Um, specifically around just interfaces. I hang out in too often. I just prefer like if YouTube gives
[4442.80 --> 4447.04]  me a dark option, I'm using dark option. If go overcast gives me a dark option, I'm using dark.
[4447.04 --> 4452.80]  I wish Slack gave me a dark option cause I'd use that. Uh, and this is pretty interesting because you
[4452.80 --> 4458.72]  can, uh, check out the repo, uh, follow the link in the top, uh, or it just says user styles.org slash
[4458.72 --> 4463.52]  whatever for the styles relation to a page. And if you're using Google Chrome or whatever you're using,
[4463.52 --> 4469.28]  it will probably tell you to install something called stylish. And that allows you to ship some
[4469.28 --> 4475.20]  customized settings. I'm sure that most people listen to this podcast, hang out on GitHub way too
[4475.20 --> 4482.56]  often, uh, or maybe just often enough. And your eyes may appreciate this mention because GitHub dark
[4482.56 --> 4488.72]  is super cool. I've already switched. I'm not going back. And in fact, it's making me really want
[4488.72 --> 4493.76]  changelog.com to be dark too. So we've already got a dark version of it on slash podcast and slash
[4493.76 --> 4501.44]  community. However, um, we don't have an actual mode for dark and that bums me out. So I'm going to
[4501.44 --> 4505.84]  work on putting a trailer card into the system and getting that worked into our agile workflows and,
[4505.84 --> 4512.40]  and, uh, our, our agile ish workflows cause we're never perfectly agile, but anyways,
[4513.20 --> 4515.84]  how do you guys feel about going dark on GitHub? What do you think about this?
[4515.84 --> 4522.08]  This is so funny cause I could second every word you said. I, oh my gosh, I just installed it.
[4522.08 --> 4528.80]  It's everything is dark. I do everything dark. Just like you said, overcast, anything that can be
[4528.80 --> 4535.36]  dark is will be dark. Yep. Pretty much. I have it already installed actually. So I was like, huh,
[4535.36 --> 4543.92]  I know that one. So, uh, you linked up a dark Slack too. Oh yes. We do the live shows, Florin,
[4543.92 --> 4548.96]  you're like I said, you first time or long-time listener, first time caller. You're always in there.
[4549.68 --> 4554.56]  Usually the first with links, not to discount anybody else's efforts, but you're always so fast.
[4554.56 --> 4559.76]  I don't know how you do it, but dark theme for Slack. I gotta, but this is going to mess with my
[4559.76 --> 4565.76]  theme though. So I like our Slack because I have a, a change log branded specific sidebar theme.
[4565.76 --> 4570.16]  Does it jack with the sidebar themes? Oh no, you can still keep your sidebar if you want.
[4570.16 --> 4573.12]  Okay. I don't want to mess my sidebar up. I like my sidebar.
[4574.56 --> 4579.52]  Well, cool. That's it for this show. Thanks so much for, uh, you know, tuning in for one. Thank you for
[4579.52 --> 4585.68]  your attention and, uh, and listening to this show to the regulars in Slack. Thank you to the
[4585.68 --> 4590.80]  future regulars listening right now. Thank you. Please join us. Go to, where do they go to join?
[4590.80 --> 4593.44]  Go for Slack. Do we even say where's the best place to go?
[4594.96 --> 4603.12]  Oh, um, it's a bit of a longer one. It's, uh, invites, uh, dot Slack, dot golang bridge.org.
[4603.12 --> 4609.92]  Is there a way we can find a shorter version for that? Uh, we can work on it. Yeah, we need,
[4609.92 --> 4620.16]  we need a shorter one. We need to actually talk to, uh, the go folks and, uh, and get something from
[4620.16 --> 4627.20]  them like golang.org slash Slack or slash community. We need something that's much shorter and like
[4627.20 --> 4633.60]  community-wide, not just go for bridge or go bridge-wide, like something that they actually,
[4634.16 --> 4638.16]  something that's off their URL to make it much easier. Cause I know that I want to invite people.
[4638.72 --> 4642.56]  And I always was like, I even asked you the other day, Carlos did to get Tim in. I'm like,
[4643.04 --> 4645.52]  how do I get somebody into this Slack? I don't even know.
[4645.52 --> 4655.12]  So the general channel has, it's in the general channel, uh, what a topic box, but just to, uh,
[4655.12 --> 4662.08]  comment some more, you, you are thinking the go language language team, they don't want to keep
[4662.08 --> 4668.40]  track of those things. Cause like if, if it's on their website or something, then it's sort of
[4668.40 --> 4675.12]  implied that they are endorsing it and they are very careful about giving the impression that they
[4675.12 --> 4680.64]  are endorsing something in particular, especially if they don't have the bandwidth to, to keep track
[4680.64 --> 4686.80]  of what's going on. So that might not happen. That's basically what I'm telling you.
[4686.80 --> 4694.48]  Well, okay. So here's a better thing is, uh, goland.org slash help. The third link down is go for Slack,
[4695.20 --> 4702.32]  but that links to a blog post written by Bill Kennedy in 2014, which doesn't have a clear link either.
[4702.32 --> 4707.92]  I'm just saying, find a better way to get people in. Oh yeah. So we can go back to update the link
[4707.92 --> 4712.72]  to that go for Slack one. If that's editable, then just send people to go in that over slash help and
[4712.72 --> 4717.28]  say, look for go for Slack. And that'll link to the invite. Boom. Oh yeah. It should definitely be
[4717.28 --> 4722.64]  there. It's there. Oh, I see what you're saying. Yeah. You can send the PR now and fix that.
[4722.64 --> 4727.60]  I'm going to do it. I'm going to fix this. Unless you beat me to it. Somebody's going to beat me to it.
[4727.60 --> 4731.04]  I'm going to fix it either while I'm talking or after the show. One of the two.
[4732.16 --> 4738.08]  Yeah. The only problem is that we'll need to wait for the next go deployment for that to work. So.
[4738.80 --> 4744.40]  Yeah. Real problems. All right. Well, that is officially the end of the show.
[4744.40 --> 4749.44]  Thank you so much again for tuning in. We will see you next week.
[4749.44 --> 4759.12]  All right. That's it for this week's episode of go time. I hope you enjoyed it. Do us a favor,
[4759.12 --> 4764.16]  go on overcast, go on Apple podcast, go on wherever you're listening to this podcast,
[4764.16 --> 4770.08]  favorite it, share it, like it, tweet it, whatever you got to do. Help us promote this show to your
[4770.08 --> 4776.48]  friends and fellow gophers. Bandwidth for go time and changelog is provided by Fastly. Head to
[4776.48 --> 4781.36]  fastly.com to learn more. And we move fast here at changelog and fix things because of rollbar.
[4781.52 --> 4787.52]  Check them out at rollbar.com. And we're hosted on Linode servers. Head to linode.com slash changelog.
[4787.60 --> 4792.48]  Check them out. Support this show. Our music is produced by Breakmaster Cylinder. And you can find
[4792.48 --> 4797.62]  more shows just like this at changelog.com or an Apple podcast or an overcast or wherever you
[4797.62 --> 4801.30]  subscribe to podcasts. Thank you for tuning in and we'll see you next week.
[4806.48 --> 4807.48]  Bye.
