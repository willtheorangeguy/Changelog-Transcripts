[0.00 --> 2.78]  I'm Jeremy Rustin and you're listening to The Change Log.
[11.88 --> 15.88]  Welcome back everyone, this is The Change Log and I'm your host Adam Stachowiak.
[16.04 --> 20.92]  This is episode 196 and on today's show, Jared and I talk to Jeremy Rustin,
[21.28 --> 25.62]  the creator of TiddlyWiki, a unique non-linear notebook for capturing,
[25.62 --> 31.64]  organizing, and sharing complex information. It's written in JavaScript and sports a custom fake
[31.64 --> 36.68]  DOM. We talked to Jeremy about his nearly 40-year career in programming, hackability as a human
[36.68 --> 43.12]  right, Tiddlers, the atomic unit of data in TiddlyWiki, and so much more. We have three
[43.12 --> 51.10]  sponsors for the show, TopTow, Linode, and BMC Truesight Pulse. Our first sponsor of the show
[51.10 --> 57.34]  is our friends at TopTow, an exclusive network of top freelance software developers and designers.
[58.00 --> 62.88]  Top companies rely upon top top freelancers every single day for their most mission-critical
[62.88 --> 67.78]  projects and I'd love for you to get in touch with me if you'd like a personal introduction
[67.78 --> 74.54]  to our friends at TopTow. If you're an engineer or a designer, you'll be a part of a worldwide
[74.54 --> 80.88]  community that loves to work on awesome projects with the flexibility to travel and see the world
[80.88 --> 86.52]  and blog on the TopTow blog or apply for open source grants or even have access to scholarship
[86.52 --> 93.72]  options. Head to TopTow.com to learn more or email me adam at changelaw.com if you'd prefer
[93.72 --> 98.36]  a more personal introduction to our friends at TopTow. And now, on to the show.
[104.54 --> 112.76]  All right, we're back. We got an awesome show today. This one, Jared, like many shows of
[112.76 --> 119.44]  ours, begins as an issue. Issue 248 on our ping repo. Go to github.com slash the changelaw
[119.44 --> 124.10]  slash ping. You'll see a bunch of issues there. Contribute back. Recommend the show if you want
[124.10 --> 129.12]  to, but Jared, it was FND who commented back in July. This is kind of crazy. It goes back
[129.12 --> 130.92]  to when we were at GopherCon. Remember that time?
[130.92 --> 136.40]  I do, and this is a great suggestion. Definitely a project that had never hit either of our
[136.40 --> 142.24]  radars and may never have if it wasn't for FND. I wish FND would leave his name somewhere
[142.24 --> 145.32]  on the internet so we could actually thank him by name.
[145.44 --> 149.22]  We don't know if it's a he either because it's a fighter pilot and it's an avatar, I guess
[149.22 --> 149.70]  we assume.
[149.90 --> 150.44]  That's true.
[150.56 --> 153.40]  We're not even sure. It's a genderless, faceless person.
[153.88 --> 160.72]  It is. So, thank you, genderless, faceless person FND. And I do like to read off specifically
[160.72 --> 166.76]  what was said because it was intriguing. And he or she said that TiddlyWiki, which is what
[166.76 --> 171.76]  we're here to talk about, was one of the earliest single page applications and is in many ways
[171.76 --> 177.86]  both unusual and thought provoking. Its latest incarnation was rewritten from scratch, taking
[177.86 --> 184.80]  advantage of the JavaScript community's modern tooling. So that was FND's take on why TiddlyWiki
[184.80 --> 191.34]  is interesting. And also, he or she said Jeremy Rustin will be a great guest. So Jeremy, you're
[191.34 --> 192.90]  here. We really appreciate you joining us.
[193.94 --> 196.38]  Thank you, guys. Thank you very much, FND, as well.
[197.38 --> 201.28]  Yeah. So Jeremy, we like to get to know our guests a little bit at the top. And so I did
[201.28 --> 206.72]  a little bit of looking up. And on Twitter, I found an interesting bio which says that you're
[206.72 --> 212.10]  been learning to code since 1978. That's a long time.
[212.70 --> 223.02]  Yes. I wonder, the average age of your guests, I was thinking I'm probably hugely older. But
[223.02 --> 228.58]  hopefully I can pull out some interesting perspectives that come from that. I mean, I
[228.58 --> 236.12]  got a first computer in 1978, as it says there. It was long before the web and long before
[236.12 --> 240.14]  object-oriented programming, long before databases, if you can imagine that.
[240.14 --> 242.94]  So what did you cut your teeth on then? Was it just C or what?
[244.28 --> 251.42]  No. So my first computer was a crazy thing called the MK14. And it's just a circuit board
[251.42 --> 259.06]  that you soldered yourself. It had a processor called the AT60, also called the SCAMP, SC-MP.
[259.06 --> 267.60]  And it was, in fact, it was a bit of a precursor to the risk chips, in that one of the things
[267.60 --> 272.58]  that was regarded as freakish about it, it was intended for embedded applications, was
[272.58 --> 277.64]  that it didn't have a stack pointer. And instead, there were some conventions for using one of
[277.64 --> 283.80]  the general purpose registers as a stack pointer. And obviously, because it was the first processor
[283.80 --> 289.36]  I touched, I had no idea that that was such an unusual thing. But then, however many years
[289.36 --> 296.14]  it was later, 10, 15 years later, when I was working using the ARM chip, of course, I came
[296.14 --> 302.96]  across the same thing, where register 15 is the program counter. But anyway, it was a tiny
[302.96 --> 310.66]  8-bit processor with 128 bytes of RAM. I'm pretty sure the first program I wrote for it was a brute
[310.66 --> 319.06]  force multiplication program that added numbers together. And you programmed it with a hex keypad
[319.06 --> 325.52]  and a seven-segment display. So there was no basic interpreter or anything like that, because
[325.52 --> 333.50]  that's it. But nowadays, obviously, anybody who wants that experience simply picks up an Arduino
[333.50 --> 340.34]  or a Raspberry Pi or any of these fun little embedded processor cards. But there is something
[340.34 --> 347.62]  incredibly invigorating about working so close to the hardware, being able to relate what you're doing
[347.62 --> 354.54]  as a programmer with what you can see in the circuit diagrams and with what you can connect to the
[354.54 --> 363.68]  exposed ports. It's really fun. And programmers with my background are apt to feel almost a little
[363.68 --> 368.70]  sorry for people who've only had the chance to work in very high-level environments.
[369.50 --> 375.16]  Well, you must be excited about some of the Arduinos. You still have higher-level languages,
[375.34 --> 379.46]  but at least being able to feel like you're a little bit closer to the machine than we normally
[379.46 --> 380.62]  operate on the web.
[382.00 --> 386.42]  Oh, well, yeah. I mean, and also having had the experience of working close to the machine,
[386.74 --> 392.62]  I also really enjoy the experience of working as far away from the machine as possible in a way.
[393.02 --> 398.54]  You know, that's kind of the goal. We're trying to make computers tractable for humans. And in a way,
[398.62 --> 401.46]  that means making them less like computers.
[401.46 --> 406.18]  It's interesting to hear your take, too, on like, I never really thought about it, Jared, but, you know,
[406.18 --> 414.28]  how the MK14, the Sinclair MK14 was a thing back in those days. And, you know, Jeremy, your history
[414.28 --> 421.70]  and where you came from, like, you're a, you know, let's see, you're an older guest than we normally
[421.70 --> 426.76]  have on the show. So you have this history that goes back, I guess, to the early days of things
[426.76 --> 432.02]  taking place in the early surge of technology. And then now you see more and more like Arduino and,
[432.02 --> 438.16]  you know, these kits, so to speak, that had this resurgence over the last, you know, say, five years,
[438.22 --> 446.68]  how it was a thing and then how it's a thing again, you know, not 1977. Now it's, you know, 2014, 2015.
[448.28 --> 454.82]  And you certainly see those patterns endlessly repeating. And as mobile phones get 64-bit
[454.82 --> 460.60]  processors, there's something else even smaller who gets the 8-bit processors that used to drive
[460.60 --> 470.10]  mobile phones. And yes, it's a great process. I think as a enthusiast for computers, one sense in
[470.10 --> 477.04]  which I feel extraordinarily privileged is that obviously, right back since the 1970s,
[477.74 --> 485.60]  I've been keenly acquiring all the computers, you know, a kid. And one remarkable thing is every
[485.60 --> 492.58]  computer I've got right up to the MacBook Pro that I'm speaking to you on now has been better than the
[492.58 --> 499.94]  previous one. And that's amazing. If you think if we were horse riders, it wouldn't necessarily be
[499.94 --> 505.20]  true by the time you got to my age that every horse you acquired was better than the previous one.
[505.20 --> 506.04]  Not without a big price.
[506.04 --> 515.50]  But no, indeed, it's a tiny fraction of the price. But it's also terribly slow. You know, when in the 1970s,
[515.54 --> 523.52]  much of what we take for granted today was envisaged by, you know, by people who weren't that specialist.
[523.66 --> 529.54]  I remember my maths, when I was playing with tape recorders in the early 70s, my maths teacher,
[529.54 --> 537.04]  tell me that in the future, there would be tape recorders with no moving parts, which was a
[537.04 --> 542.64]  fascinating insight. And it took me ages to kind of understand exactly what he meant. And of course,
[543.04 --> 548.38]  he was kind of talking about MP3 players, which we then waited 30 years for. And it wasn't useful,
[548.38 --> 555.88]  I couldn't have got bet on based on his prediction. But it just reminds us that technology,
[555.88 --> 563.62]  while it's happening can seem like this tremendous rush. But actually, it can be terribly slow. And,
[563.62 --> 569.70]  you know, there's all of us on the sidelines saying, come on, give us a 300 dpi full color display,
[569.88 --> 575.54]  which I've been saying since the early 1980s. And it kind of didn't come true until a year or two ago.
[575.54 --> 576.86]  Wow, that's true. It took a while to get there.
[577.60 --> 578.38]  Indeed, indeed.
[578.56 --> 582.40]  Here's a question I've been thinking about lately. And I think, Jeremy, I'm going to use you as my test
[582.40 --> 586.94]  subject to ask it and see how it goes. So one thing I've been thinking about with software,
[587.56 --> 591.84]  you know, we cover open source software, and we all know how fast it moves. I think we'll talk to
[591.84 --> 596.40]  you later about JavaScript specifically, and how fast that ecosystem moves. And something that I've
[596.40 --> 603.12]  come to think about more and really appreciate is longevity. Because especially in tech, where we
[603.12 --> 607.94]  have a very startup, you know, disruption, fast moving, you know, companies are here today,
[607.94 --> 614.26]  gone tomorrow type of a worldview. Longevity is something that's really valuable. And so
[614.26 --> 619.02]  one thing I've been thinking back is like, for myself, what's the oldest piece of code
[619.02 --> 626.02]  that I've written, or that I wrote back in the day, which is still running, still working, still doing
[626.02 --> 631.90]  its job, you know, to the present, or maybe it just quit working. I just realized, oh, man, that was
[631.90 --> 637.18]  running for seven years, or whatever it happens to be. So I'd like to cast that at you, since you have
[637.18 --> 641.46]  such a long history of writing software, can you think back and think, what's the oldest bit of
[641.46 --> 647.40]  code that you wrote, that's still providing some value today? Gosh, that's an interesting question.
[647.74 --> 655.06]  I'm pretty confident that the software I wrote in Visual Basic in the early 90s, that is still being
[655.06 --> 662.06]  used, including icon designs that I made pretty incompetently, now that I've seen more icons.
[662.06 --> 669.56]  I worked for an investment bank in the 90s. And so it's anyone's guess what's still running there,
[669.56 --> 674.94]  because they do a very odd combination of tearing things out at the first opportunity,
[674.94 --> 679.96]  but also keeping the most inappropriate things running for 28 years. So they could easily
[679.96 --> 686.92]  stuff that too. But Visual Basic has been, you know, in the programming landscape has been one of the
[686.92 --> 695.74]  big survivors. Yeah, absolutely. I mean, it's left in the 90s. And all the time in my day job life
[695.74 --> 703.62]  outside of open source, I encounter surprisingly big business empires that are basically based on the
[703.62 --> 711.92]  back of a big, big fat Visual Basic application that's very, you know, typically is kind of molded
[711.92 --> 716.50]  around the needs of a specific vertical market. But still, you and I would look at it and go,
[717.04 --> 720.06]  see that icon in the top left? That's Visual Basic.
[720.74 --> 727.92]  Yeah, very cool. So you recently gave a talk called Hackability as a Human Right. And we're going to get
[727.92 --> 732.96]  into TiddlyWiki. I think maybe this, your perspective at this plays into the software that we're going to
[732.96 --> 738.38]  talk about today. But before we get to all that, I would like to ask if you're willing to give us a
[738.38 --> 744.00]  synopsis of this talk and your ideas behind this hackability as a human right.
[745.28 --> 753.44]  Yeah, so that talk was to a really fun conference called Wuthering Bites in the
[753.44 --> 760.12]  York, in the wilds of Yorkshire and Hebden Bridge. And it's a lot of the people that are hardware
[760.12 --> 766.80]  hackers. So I was trying to think of something to say that was, you know, focusing on what unites
[766.80 --> 771.30]  software and hardware hackers. Because although I had to solder together my early computers,
[771.70 --> 777.16]  I learned in the process that I'm not a hardware hacker. And having since then worked more closely
[777.16 --> 781.96]  with people who can wield a soldering iron, I know that it's not, you know, it's not my
[781.96 --> 788.22]  metier. And one of the words that software and hardware hackers use is, of course,
[788.70 --> 795.76]  hacking. And all I was trying to do was to play with the idea that hacking, what is hacking,
[795.76 --> 804.72]  and hacking, obviously, I mean, in the white hat sense, one has to, one has to specify. And to me,
[804.80 --> 811.36]  hacking is changing your environment, it's tweaking and improving your environment, typically through
[811.36 --> 818.66]  engineering, but often just through cunning. And to me, the an environment that you can't change an
[818.66 --> 823.26]  environment that you're prevented from changing is is essentially prison. You know, that's how prison
[823.26 --> 830.04]  works is, is everything happens to you, and you can't change anything in that environment. And so
[830.04 --> 837.58]  like those two extremes, the the idea that hacking is a sort of an engineering expression of a human
[837.58 --> 843.74]  urge that if we didn't have, you know, we were not that we would all be in prison if we didn't have,
[843.84 --> 848.68]  but that say our lives would be indistinguishable from prison if we didn't have that freedom.
[848.68 --> 855.34]  And so, you know, we regard not being in prison as a basic human right for people who aren't
[855.34 --> 861.94]  criminals. And I think it's, it's reasonable to, to say to the extent that it doesn't hurt other
[861.94 --> 865.48]  people, people should have the right to change their environment around them to suit them.
[865.84 --> 871.14]  And obviously, particularly in the realm of writing software and creating digital devices,
[871.14 --> 876.84]  changing the world around you. You know, it's not, it's not the James Bond villain thing of turning
[876.84 --> 881.64]  the oceans into a giant algae factory or something. We're just talking about improving the light
[881.64 --> 889.72]  switches, you know, that kind of thing. So, and I think I probably went on a bit about the aspects
[889.72 --> 897.28]  of all of that, that, that I find matter to me. And one of them that, that maybe is a good theme for
[897.28 --> 904.12]  us to explore a tiny bit, is that TiddlyWiki is unusual in open, amongst open source projects.
[904.36 --> 912.10]  Not that unusual, but fairly unusual in this, it's, it's primary target, people, user base,
[912.22 --> 917.98]  people who are not software developers, they're end users. And because there are, there's things
[917.98 --> 926.66]  like Firefox, for instance, a notable piece of open source software that's directly used by end users.
[926.66 --> 932.76]  But if you think about it, and if you look at the charts on GitHub, the vast majority of open source
[932.76 --> 939.20]  products are things made by, made by bunches of developers and consumed by a bunch of developers.
[939.72 --> 944.70]  And so open source is, a lot of it is a, is a conversation between developers.
[944.70 --> 951.94]  Now, the, the aspect of TiddlyWiki being, gosh, what was the original question?
[952.06 --> 957.76]  Oh, talking about the hackability as a human right, and how that plays into TiddlyWiki itself.
[958.14 --> 962.84]  I was going to bring that hackability point together with the observation that one of the
[962.84 --> 967.48]  unusual things about TiddlyWiki is that it's designed for end users. One of its properties
[967.48 --> 973.52]  is that it's, it's generative, it lets end users make things. And so I like to think that it brings
[973.52 --> 979.54]  some of the magical powers that developers have, because when, when we think of hacking,
[979.70 --> 987.84]  the digital realm that is accessible to developers pervades so much of our lives that if you have that
[987.84 --> 992.98]  capability as a software developer, you, you do have these mini godlike powers, you, you understand
[992.98 --> 999.20]  the technology around you, and you're able to shape it to your needs. And that, that's a remarkable
[999.20 --> 1005.72]  capability. It's a whole, it's a, it's a multiplication of the power of technology, you know,
[1005.72 --> 1010.50]  technology in the hands of a programmer, you can do anything with a computer in the hands of somebody
[1010.50 --> 1017.12]  who can't program, you can only do with it those things that the programmers equipped it to do for
[1017.12 --> 1022.62]  you. So I'm very interested in tools like TiddlyWiki, and there's, I think there's many others,
[1022.98 --> 1031.44]  that provide a palette of tools and capabilities for end users or people who aren't conventional
[1031.44 --> 1038.06]  software developers to achieve some of the goals that software developers take for granted all the
[1038.06 --> 1045.50]  time. And so does that make sense? So I'm kind of thinking that our duty as developers, we have this
[1045.50 --> 1051.40]  sort of natural ability to hack the digital world about around us. And rather than jealously guarding
[1051.40 --> 1057.30]  that tech, that those skills and those techniques, we should be trying to bring as much of that
[1057.30 --> 1064.32]  experience to ordinary people as we can. And the reason why I think that's necessary is through
[1064.32 --> 1071.16]  TiddlyWiki. I've seen that if you provide a tool that can do that, people will build technology to serve
[1071.16 --> 1079.38]  extraordinary tiny niches that would never get filled in the commercial way. So one of my favourite
[1079.38 --> 1086.38]  applications of TiddlyWiki is a volleyball teacher who has used TiddlyWiki to create this extraordinarily
[1086.38 --> 1093.82]  detailed, extensible lesson planning system. And in fact, it's not, it produces bits of paper,
[1094.12 --> 1099.28]  things that I think are printed out and given to pupils and teachers and so on. But it's also got a
[1099.28 --> 1105.54]  whole user interface for defining exercises, goals, goodness knows what stuff. And when you look at it,
[1105.54 --> 1110.68]  because I know nothing about volleyball, the thing that's really obvious is that it's riddled through,
[1110.68 --> 1114.62]  the creation of it was riddled through with the knowledge and understanding of volleyball.
[1115.26 --> 1119.92]  And so the person who built it as a volleyball expert was able to build something that very closely
[1119.92 --> 1125.78]  matched their needs because of their tool, because of being able to use a tool like TiddlyWiki.
[1126.48 --> 1132.02]  But without it, there was no way that any of us software developers were going to say,
[1132.02 --> 1135.98]  oh, yuppie, let's go and write the perfect software app for the volleyball industry.
[1138.14 --> 1143.02]  So that's where I was coming from with the hackability as a human right thing, this idea
[1143.02 --> 1149.54]  that kind of trying to frame it as an obligation for us, for developers. I think it's important to
[1149.54 --> 1157.44]  consider what you do in a thoughtful way. And one aspect of being a software developer is
[1157.44 --> 1163.42]  sort of ethical, philosophical considerations. And it's worth giving them a little.
[1163.50 --> 1168.76]  Yeah, I love that idea. You're bringing hackability to the masses. And as the ones who are,
[1168.90 --> 1174.02]  you know, the niched, the people with the current superpowers, right, the hackers of today,
[1174.54 --> 1179.08]  like, we can bring that to them, or we can just hoard it for ourselves. And so by building tools
[1179.08 --> 1185.94]  for end users that are extendable, are hackable, we're allowing a whole new class of things and ideas
[1185.94 --> 1189.36]  that we never would have come up with on our own. Awesome.
[1189.56 --> 1196.78]  If I've got time to mention a specific one that I like, it's a good example, is that I think Git,
[1197.54 --> 1202.66]  or I mean source code control in general, but today that means Git, is one of our superpowers
[1202.66 --> 1208.00]  as developers. That imagine that capability in the rest of our lives is the ability to make
[1208.00 --> 1212.60]  arbitrary changes to things completely safe in the knowledge that you can wind them back.
[1212.60 --> 1219.12]  That ability to experimentally change things is actually completely denied most people. If I
[1219.12 --> 1224.38]  think about my LinkedIn profile, so try and think of something that's the opposite of the concern of a
[1224.38 --> 1229.24]  software developer, I might want to change my LinkedIn profile to present myself differently.
[1229.94 --> 1236.64]  But there's no, you know, there's no rewind on GitHub, I can't go back to an earlier commit.
[1237.00 --> 1241.66]  There's just a whole bundle of apparently independent things that I can go in and change.
[1241.66 --> 1247.88]  And so that discourages experimentation. And we see that all the time with end user behavior.
[1248.16 --> 1255.98]  There's an old adage that a significant goal of users of software is to not mess up, to not be seen,
[1256.08 --> 1260.76]  to make a mistake. So, yes, there you go.
[1260.90 --> 1267.06]  I agree. I think it's a great example of the ability to rewind and start over and have that.
[1267.06 --> 1270.30]  Yes, I'm so sorry. I didn't complete the thought by connecting it to TiddlyWiki.
[1271.20 --> 1277.52]  They will, I think after the break, we'll be talking about the way that TiddlyWiki exists as a single file.
[1277.76 --> 1285.06]  And perhaps we'll touch on how that can give end users exactly this capability that we as developers get with Git.
[1285.06 --> 1289.06]  Yeah, absolutely. I think you teed it up well. Let's take our first break.
[1289.48 --> 1295.06]  When we get back, we will dive into TiddlyWiki and how all these ideas of yours play into that software
[1295.06 --> 1298.14]  and some of the success stories you've had with it. So we'll be right back.
[1298.14 --> 1305.02]  If you're looking for one of the most fastest, efficient SSD cloud servers on the market,
[1305.36 --> 1307.76]  look no further than our friends at Linode.
[1308.12 --> 1315.00]  You can get a Linode cloud server up and running in seconds with your choice of Linux distro, resources, and node location.
[1315.40 --> 1318.74]  And they've got eight data centers spread across the entire world.
[1318.88 --> 1324.60]  North America, Europe, Asia Pacific, and plans start at just $10 a month with hourly billing.
[1324.60 --> 1330.92]  Get forward access for more control, run VMs, run containers, run your own private Git server.
[1331.30 --> 1336.98]  Enjoy native SSD cloud storage, 40 gigabit network, Intel E5 processors.
[1337.48 --> 1341.06]  Again, use the code CHANGELOG10 with unlimited uses.
[1341.48 --> 1346.14]  Tell your friends. It expires later this year so you have plenty of time to use it.
[1346.38 --> 1349.10]  Head to linode.com slash changelog.
[1349.10 --> 1355.34]  All right, we are back with Jeremy Rustin talking about TiddlyWiki.
[1355.54 --> 1357.44]  And Jeremy, we're going to get into all the details.
[1357.58 --> 1359.06]  I love the idea of a tiddler.
[1359.24 --> 1363.12]  We're going to explain that, the single file, the extendability, the hackability.
[1363.36 --> 1368.00]  But before we get into all that, I want to hear about the conception of TiddlyWiki.
[1368.14 --> 1370.38]  You know, there's lots of wiki solutions out there.
[1371.08 --> 1376.28]  And wikis are, in my view, kind of a quintessential part of the web and the open web.
[1376.28 --> 1386.68]  And so all these wiki systems, most of them are open source systems because wikis kind of have that open idea ingrained in them from the beginning.
[1387.30 --> 1396.22]  And so can you take us back to the origin of TiddlyWiki and why you thought that this had to exist in a world where there were other wiki systems out there?
[1397.10 --> 1402.60]  TiddlyWiki is a direct origin as in why I started writing the code.
[1402.60 --> 1406.42]  And once I started writing the code, I learned other things that made me think other things.
[1406.52 --> 1416.10]  But the original motivation was based on a really simple observation that I'd been using wikis for maybe five or six years in various different work contexts by then.
[1416.32 --> 1419.06]  And found pretty much what everybody finds.
[1419.18 --> 1421.58]  They work really well in a technical community.
[1421.96 --> 1425.52]  They work less well as the community gets less technical.
[1425.52 --> 1437.18]  But more interestingly, I learned, as I guess everybody does, that the ability to refactor content in a wiki is incredibly important.
[1437.52 --> 1444.14]  And that a useful wiki that's shared within a group needs kind of constant tending.
[1444.38 --> 1448.30]  Everybody needs to be looking out for opportunities to improve it.
[1448.30 --> 1451.18]  And I'll call those improvements refactorings.
[1451.52 --> 1464.18]  And what you observe with people using, say, MediaWiki is if they're approaching, there's two perhaps archetypal refactorings with a wiki.
[1464.38 --> 1466.46]  One is to split a page into two.
[1467.14 --> 1472.24]  You know, in one existing page, you realize that there's a subtopic there that deserves its own page.
[1472.28 --> 1473.94]  You shift it off into a separate page.
[1473.94 --> 1479.12]  Or conversely, you've got two pages that you realize are about almost the same thing and you merge them together.
[1479.66 --> 1489.12]  And when you watch people doing that with MediaWiki particularly, you will see them open those various pages in different tabs so that they can more easily jump between them.
[1489.62 --> 1498.06]  And if you've got the keyboard shortcuts to hand for dealing with tabs, it can make that kind of refactoring actually pretty efficient.
[1498.06 --> 1504.36]  And, you know, when you switch between tabs, most browsers will retain the current selection within a text area.
[1504.52 --> 1508.82]  So it's quite easy to kind of line things up and get quite efficient that way.
[1508.94 --> 1514.30]  Although I'm sure the Emacs and Vim users will argue that there's more efficient ways to operate.
[1514.86 --> 1528.04]  Anyway, so it made me wonder whether there was a more direct way that the software could support the interactions necessary for users to perform those kinds of refactorings.
[1528.06 --> 1537.22]  And then I saw Gmail at the beginning of 2004 signed up at the 1st of April 2004, I believe, was when they launched it.
[1537.82 --> 1541.26]  And it seems extraordinary to a modern audience.
[1541.46 --> 1548.60]  But the innovation in Gmail was the way that it showed multiple email messages at once.
[1548.60 --> 1560.20]  Until that time, pretty much all email clients, you'd seen a list of individual emails in the thread, you selected one of them, and then the text of that email was displayed.
[1560.76 --> 1571.10]  And this idea of having the same user interface gadget that was used to display an individual message repeated down the page, to me, I thought that was really attractive.
[1571.10 --> 1572.82]  It made brilliant use.
[1572.98 --> 1590.14]  It's one of the things that is kind of second nature when you think about the web as a web page, but rather alien with a sort of more old-fashioned visual basic laying things out on a corkboard sort of view, which is rather that was the prevailing view at the time.
[1590.14 --> 1603.98]  So all I did was to combine those two existing ideas that I thought to create a wiki where the pages were shown as individual chunks on a page.
[1603.98 --> 1615.48]  So actually, I've explained it badly because I was already interested in the kind of philosophy of recording and reusing information.
[1616.20 --> 1630.46]  And one of the ideas that I think I evolved, but that probably means that I read it, was the idea, well, two linked ideas, really, that the purpose of recording information is so that we can reuse it.
[1630.46 --> 1636.00]  And that the way to optimize information for reuse is to chop it up into little bits.
[1636.78 --> 1648.92]  And those are kind of assertions that I have no formal proof of, but that's based on my experience of watching myself and other people working on stuff.
[1648.92 --> 1660.46]  And the small chunks of information thing is also, it was part of, at the time I had, I wanted to write as to be part of the blogosphere.
[1661.08 --> 1665.98]  But I knew that my tendency was to write very long pieces.
[1665.98 --> 1673.34]  I'd been trained in essay writing with lots of, I have to kind of kick myself to remove the rhetorical flourishes.
[1673.34 --> 1683.98]  So I rather liked the whole idea of building a tool that encouraged brevity, that encouraged concisely expressed ideas.
[1684.18 --> 1699.54]  So that by optimizing the tool for small chunks of text, you would avoid the problem that somebody faced with a massive blank text area will feel compelled to fill the text area with unnecessary embellishment and detail.
[1699.54 --> 1700.64]  Nobody likes blank either.
[1700.88 --> 1710.56]  You know, like it's, it's, if you see a blank page, you, designers out there that are familiar with Photoshop and a brand new document, it's like, it's this document you open up and it's just white.
[1710.56 --> 1714.82]  And it's, it doesn't encourage any sort of creation.
[1715.30 --> 1715.82]  Yes.
[1716.08 --> 1724.58]  Whereas in TiddlyWiki, when you add something to an existing wiki, your, you know, your new item will appear alongside the existing entries.
[1724.58 --> 1731.90]  It feels explicitly like you're, um, uh, uh, accreting onto an existing thing where it's presented.
[1731.90 --> 1732.34]  Yes.
[1732.44 --> 1734.54]  Presented with a white box.
[1734.64 --> 1736.30]  Although sometimes it's what you want.
[1736.38 --> 1740.10]  Um, it isn't necessarily conducive to thinking.
[1740.34 --> 1743.52]  So that was, that was kind of the idea.
[1743.52 --> 1750.72]  And I thought what needed to be, what I had a number of other sort of ideas floating around that seemed to connect with it.
[1750.72 --> 1753.42]  And at the time Flickr had just launched.
[1753.42 --> 1770.76]  And so I thought that the obvious thing to do was to create a service like Flickr that would be based on what I was calling micro content, um, small fragments of text that people would share and tag and arrange into albums and sequences and so on.
[1771.16 --> 1775.12]  Um, so pretty much Flickr for texts for small fragments of text.
[1775.12 --> 1776.12]  Flickr for text.
[1776.12 --> 1783.00]  And the very first thing I did to explore that was to create a prototype in JavaScript.
[1783.00 --> 1788.20]  And at the time I'd only had the, um, loosest experience with JavaScript.
[1788.20 --> 1795.28]  I'd looked at it from a distance and thought it looked like C and, um, and not really got much beyond that, but right.
[1795.32 --> 1796.44]  This tiny prototype.
[1796.44 --> 1800.34]  And at the time I didn't have access to a server.
[1800.68 --> 1805.06]  Um, and so, um, a friend of mine had a static server.
[1805.34 --> 1820.40]  Um, so the easiest way for me to, um, kind of publish this demo so that I could talk to people about it was to create it as a standalone HTML page with embedded JavaScript, you know, that, that ran the demo, so to speak.
[1820.40 --> 1839.84]  So I put out what I thought was, you know, what people do all the time, a simple JavaScript demo that I thought would, would maybe start a conversation and, uh, help me to explore the ideas that I was, um, expressing within it or help me to explore them with other people.
[1840.26 --> 1850.28]  Um, and what actually happened was it, it, it got a certain amount of, um, attention from a couple of, at the time it was blogs that used to.
[1850.40 --> 1856.00]  It would be how people obtained links to interesting stuff on the web and a blog called cocky covered it.
[1856.30 --> 1858.94]  And, um, yeah, yeah.
[1859.02 --> 1860.44]  It's like the oldest blog out there basically.
[1860.58 --> 1861.64]  I still read cocky.
[1861.68 --> 1862.06]  Yeah.
[1862.28 --> 1862.52]  Yeah.
[1862.64 --> 1863.22]  Every day.
[1863.62 --> 1870.28]  Well, back then it, it, it seemed like, um, being covered by entertainment weekly.
[1870.32 --> 1877.38]  That's not the exact, that's not the best example I think is it, but it felt like, um, a very, you know, very, um, big splash.
[1877.60 --> 1878.12]  Delighted.
[1878.34 --> 1879.00]  Absolutely delighted.
[1879.14 --> 1879.26]  Yeah.
[1879.26 --> 1895.46]  Um, and, um, so then there's a flood of people who don't know anything about wikis coming to this demo and they go, uh, when I say they, I mean the feedback that I then read particularly on, there was a bookmarking service called delicious at the time.
[1895.46 --> 1908.76]  And so one of the, um, and so one of the sort of ways that I got feedback then that would be kind of on Twitter now was the comments that people left as they bookmarked Italy wiki.com and the graph of people increasing.
[1908.76 --> 1926.50]  And the reaction to it was, um, um, and the, um, and the people's expectation, despite the fact that I'd build it as a demo was that it was a product.
[1926.50 --> 1937.98]  And so it got to be rather a, um, uh, so the way that I'd written tiddly wiki, you could, this initial demo of it was that you could make changes to it.
[1938.02 --> 1940.52]  So you could interact with this JavaScript application.
[1940.52 --> 1951.18]  And then when you tried to save your changes, it popped up a pop-up window that then JavaScript printed out your data in basically an HTML and you could copy and paste it elsewhere.
[1951.18 --> 1959.86]  And so what people were saying was that when you press save, it should actually save your changes so that the HTML file is modified.
[1960.04 --> 1965.08]  And I got incredibly frustrated, um, saying to myself and others, well, that's ridiculous.
[1965.22 --> 1966.08]  Of course you can't do that.
[1966.14 --> 1969.16]  An HTML file loaded in the browser can't save changes.
[1969.24 --> 1969.84]  That's absurd.
[1970.48 --> 1980.16]  Um, but, uh, then saw that somebody else had worked on a Firefox extension that let tiddly wiki save changes.
[1980.16 --> 1988.42]  So it used the privileged APIs that were available to Firefox extensions to access the file system and save the HTML file.
[1988.88 --> 1995.32]  And then I discovered that these same APIs were actually not that privileged and you could use them from an ordinary HTML file.
[1995.60 --> 2009.06]  So then suddenly, um, it was, well, I thought that was a rather nice example of something I found before that there are certain, there are certain situations that the best response to them is just to write code.
[2009.06 --> 2016.20]  And, you know, when people are giving you a hard time about shortcomings of a product or, um, then just write code.
[2016.28 --> 2019.14]  And it's often the most, the most useful response.
[2019.36 --> 2031.20]  And in this case, I'd unexpectedly, um, uncovered what I now think is a potentially important, but still much overlooked way of running software.
[2031.20 --> 2036.24]  Um, and it's basically, the idea is to treat the browser as a virtual machine.
[2036.24 --> 2042.24]  And, you know, you can, um, if you're paying attention, of course, the browser is quite explicitly a virtual machine.
[2042.34 --> 2043.88]  It's a virtual machine for running JavaScript.
[2043.88 --> 2053.32]  But start to think about the browser as being a virtual machine container in the same way as virtual machine containers, hypervisors.
[2053.48 --> 2056.04]  And you realize that it's not so very far away.
[2056.16 --> 2059.58]  You can provision a new virtual machine by pressing command T.
[2059.58 --> 2076.86]  Um, the computing power available within a browser tab, of course, um, exceeds that slice of computing power that, um, facebook.com or google.com is going to grant to your, um, uh, to your unique needs.
[2077.26 --> 2077.96]  It's good.
[2078.02 --> 2082.40]  I mean, you're, you're, you're, you're describing a little bit of the history of TiddlyWiki.
[2082.40 --> 2089.24]  You started off with this, this demo of an idea around these small chunks of text.
[2089.96 --> 2092.92]  And then you, you know, people got mad at you.
[2093.00 --> 2096.88]  And so you, you know, you decided I'm just going to code instead of reacting.
[2096.88 --> 2098.66]  I'm just going to, you know, keep coding.
[2099.16 --> 2105.12]  Um, at which point now you've decided that you're going to start storing all of the information in, in the browser.
[2105.50 --> 2107.68]  And you're going to start using it as a virtual machine.
[2107.98 --> 2112.00]  Um, so a little bit, you're giving us the background of how TiddlyWiki came to be.
[2112.00 --> 2122.62]  Maybe let's, let's, let's talk about this idea a little bit more of the unique, or excuse me, of the small, um, small chunks of text.
[2122.62 --> 2127.68]  So it seems like that's the idea that has continued forward as you've developed the software.
[2128.26 --> 2141.26]  Um, one thing that we pulled off of, I'm not sure if it's your website or a blog post, is that you said that, um, TiddlyWiki is based on the idea that information is more reusable if it is sliced up into the smallest,
[2141.26 --> 2143.26]  semantically meaningful chunks.
[2143.26 --> 2147.74]  Um, and then woven back together to make narratives and stories.
[2147.92 --> 2151.70]  And you call these Tiddlers, which I think I referenced earlier.
[2152.28 --> 2156.52]  Um, is that, that seems like the unique bit.
[2156.60 --> 2158.50]  That seems like it's unique take on the world.
[2158.74 --> 2159.04]  Yes.
[2159.04 --> 2163.90]  And it's, again, it's, it's, it's a bit accidental and a bit deliberate.
[2163.90 --> 2177.30]  Um, the word Tiddler came from writing the code that inside in the code, I was at first thinking, I'm dealing with objects, nodes, items, you know, all those words, records that we use for generic things that you deal with.
[2177.30 --> 2185.22]  And lots of apps generalize everything like, I don't know, I think WordPress does generalize everything to the point where basically everything is a post.
[2185.64 --> 2197.06]  Um, and so I needed a word to describe that thing and, um, had beforehand, um, come across the advantages of neologizing, you know, an unusual word.
[2197.06 --> 2202.42]  Um, and Tiddler, uh, came, um, comes from an English, English word.
[2202.68 --> 2204.30]  Tiddler just means small tiddly.
[2204.62 --> 2205.62]  It also means drunk.
[2205.74 --> 2206.98]  So it's kind of a joke.
[2207.18 --> 2212.42]  Um, uh, that were like Tiddlywinks comes from the game with the little Tiddlywinks.
[2212.44 --> 2213.46]  That's different again.
[2213.62 --> 2218.48]  I think that's just that it might be, that might, well, it might be the, the young person.
[2218.62 --> 2220.90]  Um, so, you know, a game for Tiddlers.
[2221.24 --> 2225.80]  Um, these are my, so you could say about my young children or something.
[2225.80 --> 2245.98]  But, um, uh, but it turned out that it was the right place to neologize that the idea of a Tiddler, although closely related to lots of similar ideas and other applications is, is so important and central to Tiddlywiki that it's worth neologizing and choosing a word that we get to define.
[2246.54 --> 2252.08]  Um, and that is pretty much the definition that you gave the idea of the smallest semantic unit.
[2252.08 --> 2259.80]  So one often, uh, when one uses Tiddlywiki, you might write, um, a stream of consciousness.
[2259.80 --> 2264.02]  You write for 10 minutes to capture what you just did for the previous hour.
[2264.32 --> 2272.28]  Um, and then I think, as I mentioned before, an archetypal Tiddlywiki refactoring would be to slice out chunks into separate Tiddlers.
[2272.28 --> 2279.10]  And then it's kind of the idea of active learning, that when you learn something, you write it down.
[2279.52 --> 2283.50]  Um, and that, that improves your chances of remembering it.
[2283.56 --> 2288.66]  If you write it down and then do something with it, use it, that improves your chances even further.
[2288.66 --> 2303.12]  So the idea that you'll record information, refactoring it, changing the title so that it makes more sense when you refer back to it in the future, giving it some tags so that it gets tied together into different categories.
[2303.52 --> 2308.62]  Um, weaving it together into, weaving it into different stories along with other items.
[2308.62 --> 2315.08]  Those kinds of, they're ways of exploring your data and kind of, sorry, exploring your information.
[2315.68 --> 2321.30]  Um, and, and crucially presenting snapshots of it to other people.
[2321.82 --> 2331.92]  Um, so, you know, a common, you think about people who do stuff in Excel, a common thing is they've got some unholy mess of spreadsheets and macros in the background.
[2331.92 --> 2342.60]  But what comes popping out at the far side is a fairly simple spreadsheet that everybody can understand, showing the disposition of sand and the sandhills or whatever it is.
[2343.60 --> 2349.58]  Uh, you know, one thing that FND said is, is first of all, that these, the way it's built is unusual and thought provoking.
[2349.68 --> 2352.04]  And it's probably this idea, because I think that is the uniqueness.
[2352.20 --> 2357.94]  When I think of a wiki, I think of the, the small, it's a bunch of pages, you know, and you edit a page and then you link pages.
[2357.94 --> 2358.26]  Yeah.
[2358.26 --> 2368.04]  And, you know, with WordPress, like they had posts and everything was a post and then they added some pages and then they started to like, you know, it started to expand beyond that idea.
[2368.36 --> 2376.12]  And so the software and then the nomenclature had to change and they started to, you know, started to get that square peg in a round hole.
[2376.68 --> 2387.44]  Um, and it seems like, uh, the, the, the same problem can happen with a page where, like you said, if you're refactoring or you're, I think of it like trimming the hedges, like you're, you're maintaining the wiki.
[2387.44 --> 2394.32]  You start to realize that like pages is not small enough for things to actually fit together in a way that you think about them in your mind.
[2394.50 --> 2408.24]  And so I think that the reason why it is unusual and thought provoking is because you, you're really focusing down on, uh, really small units of, is it just text or is a tiddler, can a tiddler be an image or a link?
[2408.44 --> 2409.74]  A tiddler can be an image.
[2409.74 --> 2421.78]  Um, links, you can, there are situations where it makes sense to, to use a tiddler to represent a link, but you can also have links embedded within a tiddler and you can have MP3 tiddlers, WAV tiddlers.
[2422.04 --> 2426.32]  I mean, you know, anything with a MIME type, you can do something within a browser it deals with.
[2426.56 --> 2429.12]  Very interestingly, it also works with SVG.
[2429.12 --> 2440.08]  Um, but to pick up your point about tiddler wiki, not seeming like a wiki, um, there's, um, the most common characteristic of a wiki is this idea of a wiki that anybody can edit.
[2440.08 --> 2443.12]  It's the kind of, um, a page that anybody can edit.
[2443.24 --> 2448.78]  It's the, um, highest expression, purest expression of the idea of a, of a shared space.
[2448.84 --> 2453.78]  It's a shared space with no rules and, um, no, no admins often.
[2453.78 --> 2459.58]  Um, but I always felt what was interesting about wikis wasn't that at all, although that is interesting.
[2459.58 --> 2464.74]  It was the way that wikis turn linking into part of the punctuation of writing.
[2464.74 --> 2471.62]  So I've always found hypertext and the previous developments in hypertext very interesting.
[2471.62 --> 2481.88]  And one of the, my observations is I think, um, hypertext is an expression of a fairly common set of beliefs about how our brains work.
[2481.88 --> 2486.72]  And our brains work to many of us feel without being too presumptuous.
[2486.72 --> 2493.78]  Um, that some of the time it's useful to think of our brains as lumps of things connected by lines, you know,
[2493.78 --> 2500.72]  as would be depicted in a mind map would be a very direct expression of that vision that people have.
[2500.72 --> 2507.16]  Now tiddly wiki doesn't seek to express those relationships graphically like a mind map, although it can.
[2507.24 --> 2514.18]  And there's a plugin to do mind mapping, but it seeks to give you a data structure that's rich enough to represent those kinds of structures.
[2514.18 --> 2526.82]  Um, so the tiddler within tiddly wiki, once you get to the level of detail beyond its smallness, um, it's a kind of universal data structure for thinking about items of data.
[2527.18 --> 2541.36]  And, um, it's in, you know, in computer science terms, it's a, it's just a hash map by title, um, of, and a tiddler is essentially, uh, a hash map of, of field values named field values.
[2541.36 --> 2549.14]  So it's a similar data model to, um, a lot of the no SQL databases at the moment, um, for instance.
[2549.62 --> 2564.12]  Um, and, um, yeah, that's turned out to be kind of easy to do because it's, um, uh, hypertext, as I say, we're 50 years into the history of hypertext.
[2564.12 --> 2575.52]  Um, and, uh, we've got some, um, there's some strong evidence that people like linking as a metaphor for, well, as a way of expressing relationships between items.
[2575.52 --> 2591.32]  As software developers, we certainly to define and have this nomenclature to, to things and understanding the depth and also your path to understand what a tiddler is and what it means to you and how it's a, an atomic unit.
[2591.32 --> 2597.46]  And it's the smallest atomic unit is, uh, is going to give us a lot of clarity, especially as we get into the more technical pieces.
[2598.12 --> 2599.44]  Um, let's take a break.
[2599.80 --> 2606.88]  And when we come back, we'll dive a little deeper into tiddly wiki, uh, how tillers plan to this larger technical piece.
[2606.96 --> 2608.10]  So we'll, we'll cover on the other side.
[2608.20 --> 2609.46]  So we'll be right back.
[2609.46 --> 2619.22]  We're excited to be working with BMC to spread the word about true site pulse, their infrastructure monitoring service with one second resolution.
[2619.22 --> 2627.16]  I talked to Mike Warren, the senior architect about the importance of alarming, but more importantly, the importance of more accurate alarming.
[2627.16 --> 2634.76]  We also talked about integrations and how that plays into communicating internally across your teams as well as outside your organization.
[2635.06 --> 2635.52]  Take a listen.
[2635.52 --> 2647.86]  So alarming comes in really handy when you have one second data, because we actually collected different resolutions and we aggregate that data into one second, 15 seconds, 60 seconds, five minutes.
[2647.86 --> 2653.90]  And what that allows us to do is we can actually pull out some of the noise and give you more accurate alarms.
[2654.24 --> 2656.38]  Now the question is, what do you do for me?
[2656.58 --> 2657.28]  Send me an email.
[2657.44 --> 2658.62]  Well, that's not going to be very helpful.
[2658.86 --> 2662.54]  Really what I want is I want to find a way to push that towards my team.
[2662.54 --> 2667.44]  So we're all knowing what's happening with the services, what's up, what's down, what's fixed, what's not.
[2667.74 --> 2669.10]  And that's where the integrations come in.
[2669.30 --> 2671.88]  So integrating in with things like your chat.
[2672.04 --> 2676.00]  How do I integrate into my other tools like PagerDuty or Ops Genie?
[2676.32 --> 2679.58]  So how do I take advantage of hooking up who's on call and who's not?
[2679.74 --> 2681.46]  And then potentially, how do I do automation?
[2681.74 --> 2688.74]  So fire off a web hook or potentially if you have another setup, you can set off an email and maybe that triggers something for you.
[2688.74 --> 2693.50]  But essentially, you end up with that full round trip with everybody involved in that process.
[2693.70 --> 2698.58]  And that's your developers and your operations team because both of them have to be involved and know what's happening.
[2698.84 --> 2702.94]  So kind of with that end-to-end level, we can pull the different stats from everywhere.
[2703.42 --> 2707.42]  We can share those dashboards between anybody in your team at a certain point in time.
[2707.42 --> 2713.18]  And we can embed those dashboards into any of your existing dashboards or monitoring tools or things you may have.
[2713.38 --> 2716.92]  And that gives you the ability to share that information outside your organization.
[2717.18 --> 2723.74]  So that way, you kind of have that one single piece that you can talk about, share about, and see those metrics everywhere.
[2724.28 --> 2727.60]  I, A, have the ability to have that communication with my team.
[2728.00 --> 2733.48]  And I, B, have the ability to have that same visualization across my team and external to our team.
[2733.48 --> 2738.04]  That was Mike Morin, the senior architect of BMC's TrueSitePulse.
[2738.22 --> 2745.18]  Head to bmc.com slash TrueSitePulse all in word to learn more and tell them Adam from the Chainsaw Log sent you.
[2748.60 --> 2750.04]  All right, we're back from the break.
[2750.16 --> 2751.68]  Tilly Wiki, Jeremy is here.
[2751.80 --> 2758.08]  We're talking, you know, we quite, we quite, we talked about breaking down each of the pieces.
[2758.08 --> 2765.96]  Tiddlers, as you called it, I love the, the backstory there, especially tying back to the UK where you're from.
[2766.26 --> 2771.58]  If, if you're listening to the show and you couldn't tell that's where Jeremy's from, then check your ears or something like that.
[2771.68 --> 2777.68]  But, Tilly Wiki is 98.5% according to GitHub JavaScript.
[2777.68 --> 2781.76]  How do you, you know, we cover that a lot around here.
[2781.84 --> 2782.80]  We have a weekly email.
[2782.98 --> 2785.36]  We're always seeing the, the ups and downs.
[2785.36 --> 2790.36]  And we even cover the, you know, the madness of frameworks in JavaScript and the fatigue that comes from it.
[2790.48 --> 2799.08]  So, having such a JavaScript depth to Tilly Wiki, how do you personally deal with the, this ever-changing JavaScript landscape?
[2800.84 --> 2801.98]  That's a good question.
[2801.98 --> 2807.64]  So, Tilly Wiki started in 2004 before any of those things existed.
[2807.98 --> 2815.52]  So, I had to write my own bits of code to smooth over the differences between different browsers.
[2815.74 --> 2817.64]  For instance, there was no jQuery.
[2818.44 --> 2827.22]  So, over the years, what I've discovered is that for reasons that are fairly specific to Tilly Wiki,
[2827.22 --> 2833.00]  is quite useful to keep it as clean as possible.
[2833.00 --> 2835.32]  So, it's pretty much self-contained.
[2835.82 --> 2841.86]  It doesn't use any external libraries, but you can use external libraries with it.
[2841.94 --> 2847.62]  So, there's a sense in which some of the considerations that you'd apply to a library actually apply to Tilly Wiki,
[2847.84 --> 2850.54]  even though it's, even though it's an application.
[2850.54 --> 2857.88]  So, I've been in a happy position of being able to watch and experiment with lots of JavaScript libraries.
[2858.24 --> 2865.34]  So, D3, for instance, which I guess now is probably five or six years old,
[2865.86 --> 2872.10]  was one of the things that helped me to understand the potential of SVG in the browser.
[2872.10 --> 2880.46]  So, SVG at that point, embarrassingly, we hadn't realized that a technology that had been broken in 2002
[2880.46 --> 2884.40]  had quietly got fixed over the following five or six years.
[2885.72 --> 2893.58]  More recently, things like Angular and Reactive, the kind of second wave of frameworks,
[2894.78 --> 2900.34]  I don't use those frameworks because, say, Tilly Wiki is kind of easy its own framework.
[2900.34 --> 2908.92]  Tilly Wiki has a, if you're conscious, this might be going a little bit too deep.
[2908.92 --> 2909.32]  That's okay.
[2909.32 --> 2910.60]  But some of what Tilly Wiki does is...
[2910.60 --> 2912.34]  If I could jump in, how is it...
[2912.34 --> 2915.46]  Describe how Tilly Wiki is its own framework.
[2915.62 --> 2919.62]  So, I mean, you'd mentioned, I think you mentioned React,
[2919.74 --> 2924.00]  and I couldn't remember what else you said because I was trying to follow along,
[2924.06 --> 2925.20]  but how is it its own framework?
[2925.90 --> 2926.78]  From a distance.
[2926.78 --> 2929.80]  This will seem like a circuitous answer, but hopefully we'll get there in the end.
[2930.34 --> 2936.20]  From a distance, what a Wiki is, is a piece of code that converts WikiText into HTML.
[2937.90 --> 2941.34]  In the case of Tiddly Wiki, particularly the new version,
[2941.34 --> 2948.34]  my goal was to make the WikiText powerful enough that the user interface of Tiddly Wiki itself
[2948.34 --> 2953.80]  could be written in its own WikiText, thus making it highly extensible, etc.
[2953.80 --> 2958.26]  And it's just like writing Chrome developer tools being written in JavaScript.
[2958.56 --> 2962.56]  It's kind of a logical approach.
[2963.36 --> 2970.20]  And so you can imagine then that the pipeline that goes from WikiText to the DOM needs to be interactive in that case.
[2970.20 --> 2978.76]  So what Tiddly Wiki does is it parses the raw text of the Tiddler into a pretty straightforward syntax tree.
[2979.32 --> 2984.70]  And then it executes that syntax tree into what Tiddly Wiki calls the widget tree,
[2985.06 --> 2992.34]  which is pretty much the virtual DOM tree that you see in things like React and Angular.
[2992.34 --> 3005.38]  And the virtual DOM tree, then there's a process that does, well, close to the minimum or a fairly good subset of the maximum updates,
[3005.52 --> 3007.18]  selective updates to the DOM.
[3007.18 --> 3018.40]  So if we've got a WikiText construction like a transclusion, which will be familiar to JavaScript programmers from ordinary web development templates,
[3018.56 --> 3028.60]  so double mustache in WikiText typically means transclude this other page, make it appear as if this page is here.
[3028.60 --> 3038.20]  And so in an interactive Wiki like Tiddly Wiki, you want to make sure that if the text of that target page that is being transcluded changes,
[3038.48 --> 3044.06]  then we get minimal DOM updates to update the transclusion, but not the text around it.
[3044.46 --> 3045.86]  And that's what Tiddly Wiki does.
[3046.42 --> 3051.66]  And that enables all the paraphernalia that you see in the user interface,
[3051.66 --> 3059.66]  things like tabs and dropdowns and everything else, is modeled as the state of Tiddlers.
[3059.66 --> 3062.76]  So the state of the user interface is modeled as Tiddlers.
[3063.00 --> 3067.16]  To update the DOM with the state of the user interface,
[3067.64 --> 3077.22]  we render one single WikiText template that expands out to be the entire DOM tree of the user interface.
[3077.22 --> 3083.22]  So what I described there was kind of talking about the internals of other libraries,
[3084.08 --> 3088.88]  and many of the people who use those libraries wouldn't necessarily think about them working in that way.
[3089.46 --> 3099.72]  And I find that when I read about these libraries, I have to kind of do some picking apart to relate my understanding of what they do to what I know about how Tiddly Wiki works.
[3100.24 --> 3102.58]  But it's good to see that we're all on the same page.
[3102.78 --> 3105.98]  You do stuff in JavaScript as much as you can.
[3105.98 --> 3107.94]  You don't touch the DOM unless you have to.
[3108.48 --> 3114.80]  Back in 2004, a very common idiom was that you kept maintained state in the DOM.
[3115.04 --> 3119.94]  And it's still an incredibly useful trick on the web and appropriate in a lot of circumstances.
[3120.70 --> 3129.06]  But all of these products, including Tiddly Wiki, gain enormously from moving all of the state into JavaScript variables
[3129.06 --> 3135.82]  and treating the entire DOM as essentially transient as something that you can recreate at will.
[3137.28 --> 3147.40]  So that stuff, those characteristics of Tiddly Wiki, interestingly, aren't, they're not appreciated in the terms I've just described them by the users.
[3147.40 --> 3152.38]  So it's a kind of, it's a very developer-ish quality that I'm describing.
[3153.02 --> 3157.68]  Which we're happy to hear as developers ourselves and developer audience.
[3157.80 --> 3160.00]  So feel free to share those details.
[3160.10 --> 3161.26]  They're absolutely interesting to us.
[3161.26 --> 3167.00]  So one thing that FND mentioned is that the, and maybe I missed it, so forgive me if I did,
[3167.48 --> 3172.14]  that this latest incarnation of what Tiddly Wiki is was rewritten from scratch.
[3172.38 --> 3174.78]  Was there like a big rewrite somewhere in the history?
[3174.98 --> 3176.56]  And what was the reason for that?
[3176.56 --> 3187.58]  There were a whole multitude of reasons, but the main one was that some of the quality of the code in the original Tiddly Wiki was pretty poor.
[3187.90 --> 3191.04]  I didn't know JavaScript when I wrote the first version.
[3191.46 --> 3200.14]  I thought it resembled C and I treated it like C for a few weeks and then gradually learned more and more about JavaScript.
[3200.14 --> 3212.12]  But it meant that there were decisions that were, there were decisions that were impossible to reverse because other people had written code, plugins and so on that was based on my code.
[3212.40 --> 3218.54]  So I really felt that to fix the internal architecture, we needed a complete rewrite.
[3218.54 --> 3231.48]  But there was also an opportunity in the change in the environment that JavaScript had shifted from being regarded as a niche embarrassment to become somewhat mainstream.
[3231.80 --> 3234.76]  So somewhere in 2011, Node.js launched.
[3235.34 --> 3242.16]  And I'd been waiting for that when I was working for BT about 10 years ago.
[3242.72 --> 3247.84]  I looked at Rhino so that it was possible to run JavaScript on the server.
[3247.84 --> 3249.16]  I used Rhino in fact in the day.
[3250.06 --> 3257.14]  Yeah, in the late 90s, the Netscape had some software that involved running JavaScript on the server.
[3258.40 --> 3270.42]  And looking at Rhino, making Tiddly Wiki as I had written it work in Rhino would have been almost impossible because Tiddly Wiki was heavily based on the DOM.
[3270.42 --> 3276.94]  There was no DOM in Rhino and there was no decent support for writing web applications, for writing web servers.
[3276.94 --> 3288.60]  So when Node.js came out, that seemed like a wonderful opportunity to fix one of the biggest frustrations for me about Tiddly Wiki,
[3289.00 --> 3295.38]  which was the limitations that stemmed from it running as a single HTML file in the browser.
[3295.38 --> 3302.46]  So it's the quality of Tiddly Wiki that leads to its most unique and unexpected features.
[3302.96 --> 3309.12]  But it also, as everybody listening to the podcast, has profound limitations.
[3309.54 --> 3313.22]  There are pretty severe limitations to what you can do in the browser.
[3313.74 --> 3322.84]  And I was confident that the ideas that we, the community, had explored with Tiddly Wiki were equally applicable to the server.
[3322.84 --> 3333.76]  So the opportunity, when Node.js came out, the idea of writing Tiddly Wiki as an isomorphic application became overwhelming.
[3334.48 --> 3346.12]  And I left the job that I was in, in order to do more flexible freelance consultancy work so that I could spend a bit more time on this rewrite.
[3347.02 --> 3351.16]  So how does the, how is the Wiki content persisted nowadays?
[3351.16 --> 3354.78]  It depends where you're running it.
[3355.02 --> 3357.64]  In a way, this is the easiest audience to explain it to.
[3357.74 --> 3365.22]  Imagine that we've got a function, just like I described, that takes a chunk of Wiki text and converts it to the DOM.
[3365.22 --> 3376.58]  So to run that on the server, we have an implementation of a very simple, I call it the fake DOM, but, you know, JavaScript, pure JavaScript implementation of the DOM APIs.
[3376.80 --> 3380.70]  So that on the server, we manipulate that fake DOM.
[3381.18 --> 3384.66]  And then we do an inner text on it to extract the HTML.
[3384.66 --> 3395.06]  So given that engine and its capability of running in both of those places, we can run in a bewildering number of configurations.
[3395.06 --> 3411.50]  So we can run entirely in the browser and we save changes using HTML5's download attribute, which is a standard attribute, a standard feature of HTML5 that allows JavaScript executing in the browser to prompt for a download.
[3411.50 --> 3420.10]  So in that case, the experience is that each time you press save, you get a fresh copy of your up-to-date copy of your document.
[3420.64 --> 3421.44]  And that's not bad.
[3421.52 --> 3427.46]  It means that you get cumulative backups or you can configure your browser to prompt you when you save.
[3427.56 --> 3432.80]  And then saving is a two-click operation, but you update the original HTML file.
[3432.80 --> 3440.14]  Or there's an extension for Firefox that allows TiddlyWiki to save directly to its own file.
[3440.54 --> 3453.04]  Or there's a NWJS-based desktop application that accesses a sort of custom browser that lets the single file configuration of TiddlyWiki again persist changes directly.
[3453.04 --> 3463.22]  Or you can run it under Node.js where individual TiddlyWiki are served over HTTP to another instance of TiddlyWiki running in the browser.
[3463.86 --> 3468.18]  And then your changes are persisted as individual files.
[3468.30 --> 3470.28]  So each Tiddler is an individual file.
[3470.28 --> 3484.74]  Or you can run TiddlyWiki in Amazon Lambda where it starts up, reads a whole load of Tiddlers from DynamoDB, mashes them together, and then squirts the files out to Amazon S3.
[3484.74 --> 3502.14]  So really, although it's packaged and presented as a product, and I highlighted how important to me it is that it serves the needs of end users, what it eats, in fact, functionally is a reusable JavaScript library for handling wiki text.
[3502.52 --> 3505.06]  And within TiddlyWiki, we reuse it endlessly.
[3505.06 --> 3511.08]  So I described how we convert wiki text like headings and lists and so on to HTML.
[3511.08 --> 3515.72]  But we use the same engine to convert style sheets.
[3516.28 --> 3522.86]  So inside TiddlyWiki's style sheets, we transclude what would in something like SAS be a variable.
[3523.12 --> 3528.00]  So we've got magic Tiddlers that contain, say, the background color of the page.
[3528.44 --> 3535.14]  And then in a style sheet, wherever you want to reference the background color of the page, you just transclude that Tiddler.
[3535.14 --> 3542.14]  And that's the characteristic that I think all developers love is the idea that you only introduce new mechanisms reluctantly.
[3543.24 --> 3553.72]  And when you do introduce a new mechanism, you make it pay its keep by using it orthogonally on lots of different problems that have the same shape.
[3553.72 --> 3557.28]  And I think you see that in lots of software.
[3557.72 --> 3570.70]  And as I say, TiddlyWiki uses the same pipeline, the same processing pipeline to do interactive rendering in the browser to produce static renderings on the server that then get served on a static web server.
[3571.80 --> 3582.72]  Plus all this internal stuff like the way it handles style sheets, the way that it handles color palettes, all that kind of thing is all wiki text mechanisms reused.
[3582.72 --> 3586.26]  And there's something very pleasing about it as the creator.
[3586.74 --> 3597.18]  But the idea is, as a user, it's tools that behave like that have this pleasing property that you learn how these components work.
[3597.46 --> 3602.44]  And ideally, you know, in a sequence where you learn about the gradually more complicated ones.
[3602.44 --> 3614.20]  And then kind of like a bicycle, they become they're kind of the internal structure is sufficiently apparent that you can have a strong mental model of how to use the tool.
[3614.30 --> 3617.94]  You can anticipate how it's going to behave in a situation where you haven't used it before.
[3617.94 --> 3624.24]  It turns into something that feels like an augmentation of your brain.
[3625.02 --> 3629.90]  And that takes us back to Vannevar Bush and the early hypertext pioneers.
[3630.28 --> 3636.40]  They were obsessed with the heretical idea that people would use computers interactively.
[3636.58 --> 3641.18]  So in their work, one of the challenges they faced was just persuading people that that was practical.
[3641.18 --> 3645.66]  And that the purpose of doing that was to extend our capabilities.
[3646.54 --> 3650.94]  You sent us a nice write up in Network World about TiddlyWiki.
[3651.08 --> 3652.24]  We'll link that up in the show notes.
[3652.24 --> 3661.30]  One thing they said in that, which I thought was super interesting, I think it plays into this idea of a single pipeline, is that TiddlyWiki is a quine.
[3662.58 --> 3664.14]  Some of us know what that is.
[3664.16 --> 3664.82]  Some of us don't.
[3665.42 --> 3666.62]  I've actually seen these before.
[3666.68 --> 3671.18]  I don't think Adam had, but they're quine, Q-U-I-N-E.
[3671.18 --> 3682.28]  It's the idea of a program that doesn't have any inputs, but as it's the process of it running, it outputs its own source or it outputs itself as the program.
[3682.42 --> 3688.70]  And I've only seen those as like mental gymnastics type of things like one-liners.
[3688.82 --> 3689.42]  How do you do that?
[3689.48 --> 3690.68]  Can you do this in this language?
[3691.10 --> 3692.42]  They're very short snippets.
[3692.56 --> 3697.52]  And it's kind of not a toy, but just a way of people to challenge themselves.
[3697.52 --> 3727.50]  Absolutely.
[3727.52 --> 3734.08]  Like an automaton that can reproduce itself is a fascinating thing, especially if you throw it in the lake of raw ingredients.
[3734.98 --> 3738.30]  So, yes, it's a kind of timeless vision.
[3739.32 --> 3739.60]  Love that.
[3739.76 --> 3740.48]  Absolutely love that.
[3740.58 --> 3742.72]  Well, let's take our final break.
[3743.14 --> 3745.88]  And we want to talk about a few other things on the other side.
[3746.52 --> 3749.74]  Specifically, we talk about deployment and all these different ways you can persist it.
[3749.74 --> 3763.12]  I want to talk to you about like what that looks like for your end users, you know, whether they're going to tiddlywiki.com or it's a one-click install on a shared hosting or like how the end users come to tiddlywiki and set up their own and use them.
[3763.12 --> 3770.48]  And then also we'll talk about getting started, helping out, getting involved, you know, if you're looking for helpers or not.
[3770.92 --> 3775.26]  So we'll discuss those things as well as our closing questions on the other side of this break.
[3775.26 --> 3779.46]  Here at the Change Law, we have two emails we'd love for you to subscribe to.
[3779.54 --> 3781.34]  The first is Change Law Weekly.
[3781.70 --> 3783.76]  And we've been shipping this email for several years now.
[3783.86 --> 3785.56]  We ship it every single Saturday morning.
[3785.96 --> 3788.48]  It's everything that hits our open source radar.
[3788.62 --> 3794.00]  It's our editorial last take on what happened this week in open source and software development.
[3794.42 --> 3797.24]  Go to changelaw.com slash weekly to subscribe.
[3797.78 --> 3800.16]  And our second email is Change Law Nightly.
[3800.16 --> 3808.18]  Every single night we ship this email out covering all the top new and top star repos on GitHub at 10 p.m. Central Time.
[3808.56 --> 3811.08]  It's all the latest stuff on GitHub before it blows up.
[3811.16 --> 3812.56]  It's often our own radar.
[3812.56 --> 3819.52]  We're often creating shows and finding new people, finding new projects, putting things on our own radar based on what we find in there.
[3819.72 --> 3821.22]  So we'd love for you to subscribe to that.
[3821.34 --> 3823.42]  Head to changelaw.com slash nightly.
[3823.54 --> 3824.82]  And now back to the show.
[3824.82 --> 3836.98]  So Jeremy, before the break you described all these different ways that you could persist your titillers into different backends.
[3836.98 --> 3840.04]  Even AWS Lambda, which is pretty interesting.
[3840.84 --> 3843.10]  And I started thinking, this sounds like a really awesome hacker tool.
[3843.34 --> 3844.20]  Like you can do it this way.
[3844.26 --> 3844.92]  You can do it that way.
[3844.94 --> 3845.90]  It's what hackers love.
[3846.04 --> 3846.96]  Like give me the flexibility.
[3847.24 --> 3847.82]  Give me the freedom.
[3848.26 --> 3849.82]  I want to run it on a Raspberry Pi.
[3849.94 --> 3852.10]  I want to put it on the DigitalOcean.
[3852.10 --> 3859.34]  But you also want this to be a general purpose, usable tool for anybody, not for just hackers.
[3859.56 --> 3865.24]  So what's the use case of somebody who's coming to it and they're just looking for a wiki or they're just looking for this web-based notebook?
[3865.60 --> 3866.80]  How do they use TiddlyWiki?
[3867.50 --> 3868.26]  Great question.
[3868.38 --> 3873.04]  My approach to it has actually evolved over the time of the rewrite.
[3873.04 --> 3885.02]  When I started the rewrite, I thought that it was important to present TiddlyWiki in all of its multifariousness.
[3885.06 --> 3888.36]  Not sure if that's the right word, but all of these different things that you could do with it.
[3888.86 --> 3894.74]  So I presented them or tried to present them on the site as if they were kind of peers.
[3894.74 --> 3911.18]  And what I found was that that was confusing for quite an important constituency, which is the people who were going to use the single file version of TiddlyWiki were terrified of GitHub, didn't have any understanding of the command line.
[3911.32 --> 3913.12]  So the non-developer types.
[3913.12 --> 3919.12]  So what I've ended up doing is making two pathways, if you like.
[3919.22 --> 3920.42]  Gosh, that's a ridiculous word.
[3920.54 --> 3931.52]  But one is people going to TiddlyWiki.com, we try to help them as quickly as possible to start using the standalone edition on their machines.
[3932.74 --> 3940.68]  And the GitHub, and it's GitHub.com slash germaline slash TiddlyWiki5, which is the rewrite version,
[3940.68 --> 3944.28]  is information for a developer audience.
[3944.60 --> 3951.66]  And that does try to give a taste of all of this, of all of these possibilities.
[3952.30 --> 3963.08]  But I think as other open source projects have found, when all of these interesting developments in the project, a lot of them aren't for me.
[3963.08 --> 3968.72]  They're scattered throughout the community and they're at very different stages of development.
[3968.72 --> 3974.14]  And some people have published at different times.
[3975.06 --> 3979.32]  So the community can seem very fractured.
[3980.32 --> 3986.58]  We've done a great job in open source of adopting tools that help to minimize that effect.
[3986.70 --> 3992.58]  And GitHub itself, of course, the word hub is right in that to remind us of its main purpose,
[3992.58 --> 3999.10]  is that it's the, what do you call it, the village green for open source development.
[3999.92 --> 4004.36]  Speaking of GitHub, I was on the TiddlyWiki GitHub page there.
[4004.46 --> 4006.28]  And I noticed something that was a little bit concerning.
[4006.56 --> 4009.32]  And I just wanted to talk to you about the state of it.
[4009.32 --> 4016.34]  Because actually one of our closing questions is sometimes, how can the open source community help support TiddlyWiki?
[4016.78 --> 4019.82]  Or the project that is important to you, in this case TiddlyWiki.
[4020.80 --> 4023.70]  And one thing I noticed is you've got a whole bunch of open issues out there.
[4023.88 --> 4025.32]  You've got a lot of pull requests.
[4025.62 --> 4027.44]  You've got 67 open pull requests.
[4028.42 --> 4030.38]  You've got 520 open issues.
[4030.38 --> 4037.38]  And so I'm just curious if maybe the demand and the interest in TiddlyWiki is overwhelming you.
[4037.54 --> 4038.76]  Or you've got it under control.
[4038.84 --> 4039.70]  What's the situation there?
[4040.82 --> 4045.52]  Interestingly, you're raising something that we in the community are trying to tackle at the moment.
[4045.98 --> 4053.14]  It's partly the result of a poor decision that we made last year, maybe the year before.
[4053.94 --> 4058.16]  So we use Google Groups as the mailing list for the project.
[4058.16 --> 4062.82]  And we've got a mailing list called TiddlyWiki and a mailing list called TiddlyWikiDev.
[4062.88 --> 4065.88]  The first for users and the second for developers.
[4066.50 --> 4069.58]  And I think pretty much we all hate it.
[4070.66 --> 4075.70]  But it happens to be where we tied our horse.
[4075.92 --> 4078.16]  That's a bad metaphor, but right at the beginning.
[4079.76 --> 4087.82]  And some of the non-developers, anyway, for various reasons, we decided to experiment with using GitHub issues for discussions.
[4088.16 --> 4101.36]  And so quite explicitly, we had the policy that it was okay to have basically anything that you wanted to discuss as an issue without a clear policy on closing the issues.
[4101.50 --> 4107.24]  We're moving now to a much more conventional and, I must say, familiar for me approach.
[4107.50 --> 4108.68]  Yeah, that's a lot of issues.
[4108.88 --> 4109.92]  I was worried.
[4109.92 --> 4117.76]  And you'll see, of those, I mean, a fifth of them are one person.
[4120.34 --> 4130.24]  And you should be extremely careful that I think that in open source, we are incredibly lucky whenever anybody opens their mouth.
[4130.24 --> 4137.04]  Even if they're saying something, the same thing as somebody else, any kind of feedback is like oxygen for an open source project.
[4137.56 --> 4143.98]  And it's obviously, it's only other people's interest that keeps any project like this alive.
[4143.98 --> 4148.40]  So, yeah, a bit of a misstep on how we handled issues.
[4148.54 --> 4156.86]  We're moving to issues being more explicitly needing, well, explicitly being the to-do list for the core developers.
[4157.42 --> 4162.76]  And there being basic requirements about actionability in order for them to remain open.
[4162.76 --> 4168.98]  And we will continue to host, I'm sure, lively discussions on closed issues.
[4168.98 --> 4178.30]  But we'll try and keep the open issues, the above-the-waterline issues, reflecting what we think is actually doable, actionable work.
[4178.70 --> 4180.48]  That makes sense for issues.
[4180.68 --> 4181.76]  But what about pull requests?
[4182.90 --> 4184.72]  Oh, well, I mean, A, I'm behind.
[4185.44 --> 4191.56]  But you'll see if you look back that some of those issues have been around for an embarrassingly long time.
[4191.56 --> 4196.34]  So, again, I've not had a clear policy on closing pull requests.
[4196.58 --> 4201.88]  So, if they, where they've gone off into a discussion, I've tended to just leave them open.
[4202.08 --> 4207.12]  And the reason is because I haven't been using pull requests or issues as my to-do list.
[4207.38 --> 4213.22]  I've been tending to fall back to using, essentially using email as my to-do list.
[4213.36 --> 4220.22]  You know, you respond to the tickets that, thanks to the noise on them, they've risen to the top of your inbox.
[4220.22 --> 4222.14]  So, squeaky wheels, just the oil.
[4222.22 --> 4231.42]  It's also, I think it kind of reflects our peculiar heritage as having a substantial audience that are not developers.
[4232.10 --> 4242.84]  So, a lot of those, a lot more of my tickets, I think, are open by non-developers than would be typical for a library or a framework or something.
[4242.84 --> 4247.40]  In terms of pull requests, I wonder.
[4247.64 --> 4254.82]  I think TiddlyWiki is also quite hard for new developers to get into because of some of the things we touched on.
[4254.92 --> 4256.14]  It is its own framework.
[4256.60 --> 4256.62]  Right.
[4256.62 --> 4265.22]  It's not like working in jQuery, not keeping state in the DOM is profoundly difficult for people who've only ever worked that way.
[4266.52 --> 4275.00]  So, we do, plus I'm sure other people have experienced the same thing, you have to have quite a high bar for what you accept.
[4275.00 --> 4277.34]  Well, how well do you document those things?
[4277.72 --> 4280.96]  Like, that, the DOM piece specifically, because it sounds pretty unique.
[4281.08 --> 4283.72]  It sounds pretty awesome.
[4283.84 --> 4287.32]  But, you know, how well is that documented that invites people into?
[4287.66 --> 4290.26]  Because I think docs might lend a hand there.
[4290.58 --> 4292.28]  Again, a very good question.
[4292.28 --> 4299.28]  And I think I, I personally, I'm not the, not always the best documenter.
[4299.88 --> 4305.28]  So, I can think that something is fully documented because I've precisely described it unambiguously.
[4305.84 --> 4319.60]  And yet, there's an enormous gulf between, in some cases, between that and what's needed for people to have a clear understanding if they lack the context of, you know, being inside my brain.
[4319.60 --> 4323.00]  So, so, yes, it's a challenge.
[4323.16 --> 4327.00]  And I guess where, what saved me.
[4327.22 --> 4334.78]  So, this rewrite has been going for five years or nearly five years now with pretty uniformly all the way through.
[4335.92 --> 4338.90]  People could come along and say the documentation could be improved.
[4339.56 --> 4340.96]  And yet, we've survived.
[4340.96 --> 4346.72]  And I think it's the universality of code that actually saves us.
[4347.24 --> 4355.62]  That for a small but significant part of my audience, they can verify how the software operates by looking at the code.
[4355.70 --> 4356.74]  And there's not that much of it.
[4356.80 --> 4358.46]  It's fairly neatly sliced up.
[4358.46 --> 4371.68]  And so, from a, if you've got, if you've got enough of an incentive, it's reasonably, reasonably tractable to find your way around and to see what the thing does.
[4372.36 --> 4374.98]  Well, there's different kinds of open source projects out there.
[4375.14 --> 4380.32]  Every, every maintainer or author runs their projects a little bit differently.
[4380.32 --> 4383.02]  And you've got 87 contributors over the years.
[4383.12 --> 4385.98]  And this is probably just since the 2011 rewrite.
[4386.08 --> 4387.46]  It's all we have history in Git.
[4387.94 --> 4393.36]  But if we go look at the contributions list, you know, you have over 5,000 commits personally.
[4393.56 --> 4395.68]  And the next closest is 158.
[4396.00 --> 4397.92]  So, we have an order of magnitude difference there.
[4398.18 --> 4401.74]  And is it fair to say that you're the primary developer, you know, on TiddlyWiki?
[4401.96 --> 4404.14]  And, you know, you have people who pitch in here and there.
[4404.36 --> 4407.46]  But it's not like a robust team that's working on it day in, day out.
[4407.46 --> 4411.18]  But that's absolutely true, yes.
[4411.34 --> 4412.60]  Is that, do you like it that way?
[4412.68 --> 4414.04]  Are you looking for more help?
[4414.44 --> 4418.70]  Or are you looking, or you'd like to keep on, keep it on, and like people can help in other ways?
[4420.22 --> 4432.08]  The, the most, some, the people who missed out of that analysis are the people who work on kind of other things within the ecosystem.
[4432.08 --> 4439.08]  So, for instance, this TiddlySpot is a hosting service that's been running for most as long as TiddlyWiki.
[4439.22 --> 4440.36]  And it's completely independent.
[4441.00 --> 4445.42]  And, you know, it's supported by people other than me.
[4446.10 --> 4454.88]  So, yes, in terms of the code, that does tend to be 98% Jeremy or 95% Jeremy, I'm not sure.
[4454.88 --> 4462.84]  But in terms of the ecosystem as a whole, it feels crucially like I'm less than 50%.
[4462.84 --> 4476.50]  Because, again, projects like TiddlyWiki, like all open source projects, it deals with the conflicting requirements of its user base by adopting a plug-in architecture so that we can encapsulate conflicting requirements in plug-ins.
[4476.50 --> 4486.56]  And in any project with plug-ins and a community, you'll see most of the innovation happens out in the plug-in space.
[4487.06 --> 4488.76]  And that's definitely how I like it.
[4488.80 --> 4493.64]  Because that way, there's a multiplicity of different things going on at once.
[4494.04 --> 4496.94]  Things aren't serialized on Jeremy's singular brain.
[4496.94 --> 4507.02]  So, it ends up, if you want a system like that to survive and be healthy, oddly, the core needs to be unbelievably conservative.
[4507.66 --> 4513.82]  You basically want to hardly change anything apart from, you know, let's rephrase that.
[4514.52 --> 4516.50]  Well, actually, you want to hardly change anything.
[4516.90 --> 4519.80]  But once you've got to where you need to get to.
[4519.80 --> 4524.70]  But what you do change, you need to pay incredible attention to backwards compatibility.
[4525.20 --> 4532.80]  Because plug-in architectures typically allow very tight coupling between the plug-ins and the host architecture.
[4533.24 --> 4538.28]  And so, you never really quite know what you might change that might inadvertently affect a plug-in.
[4538.28 --> 4550.38]  So, a lot of my job in the core is for sure there's an agenda of features and mechanisms that need to be added and improved.
[4550.80 --> 4557.54]  But a big part of dealing with the kind of daily development is that.
[4557.68 --> 4565.18]  It's kind of making sure that it works well as a platform for the ecosystem.
[4565.18 --> 4575.28]  Trying to encourage contributors, in many cases, to focus their efforts on working on plug-ins rather than the core.
[4575.40 --> 4579.38]  Because once you put something in the core of a project like TiddlyWiki, there's no going back.
[4579.48 --> 4580.78]  You can't then retract it.
[4581.30 --> 4582.98]  You can deprecate it.
[4583.08 --> 4587.00]  But if you want plug-in compatibility to carry on, you've got to keep the thing there.
[4587.00 --> 4593.80]  So, there's a kind of, it ends up, I'm making it sound like a horror movie.
[4594.60 --> 4597.04]  A room that you can never go back into.
[4597.04 --> 4609.16]  But honestly, it's joyful because what one sees as, you know, in exchange for, I can't treat the core as my plaything that I do what I like with.
[4609.22 --> 4611.02]  I have to be extremely respectful.
[4611.18 --> 4617.28]  And what I'm respectful of is this, let's say, the ecosystem in the sense of artifacts that people have created.
[4617.28 --> 4623.60]  But also the thousands of hours that people have invested in understanding the product.
[4623.74 --> 4623.88]  Right.
[4624.00 --> 4626.18]  Figuring out how to get the best out of it.
[4626.76 --> 4632.96]  And in the end, you know, the software is, in open source, is often a means to an end.
[4633.04 --> 4642.14]  And the end is a well-informed, purposeful community that can solve a bunch of problems together or alone that they couldn't do before.
[4642.14 --> 4655.50]  And I feel that we, again, because of this sense of TiddlyWiki being used not just by developers, therefore it's used in an incredibly wide array of situations and contexts.
[4656.66 --> 4663.00]  And yes, that feels like the most fun I can have as a developer.
[4664.60 --> 4666.26]  Writing code for other people.
[4667.24 --> 4667.26]  Awesome.
[4667.34 --> 4669.28]  I think that leads us right into our closing questions.
[4669.28 --> 4673.42]  You just mentioned all the different ways that people have been involved.
[4674.12 --> 4674.48]  Plugins.
[4675.36 --> 4677.92]  You know, obviously you had robust discussions in the issues.
[4678.06 --> 4680.28]  Maybe not the best place for them, but live and learn.
[4681.36 --> 4685.46]  So our first closing question for you kind of relates back to what we talked about just a moment ago.
[4685.54 --> 4697.32]  If you could have a clear call to action, you know, or a call for help to the open source community on how they can help you take TiddlyWiki even further or, you know, to new heights, what would you say to them?
[4697.32 --> 4700.10]  What's the best way people can hop in and help you out?
[4701.24 --> 4701.90]  It's interesting.
[4702.34 --> 4706.54]  I think what open source needs is people paying attention to it.
[4706.86 --> 4710.22]  As we touched on before, one of TiddlyWiki's shortcomings is documentation.
[4710.22 --> 4723.96]  One of the things that I've learned about documentation is that we can try to have a single body of reference documentation that completely accurately describes the behavior of the system.
[4724.06 --> 4725.52]  That would be a great thing to have.
[4725.78 --> 4727.46]  But it's actually not really what's needed.
[4727.62 --> 4738.70]  What's needed is introductory documentation that helps people up the on-ramp of using TiddlyWiki because of all the different directions that that can take.
[4738.70 --> 4749.12]  So, for instance, we've got reasonable coverage for people who want to use TiddlyWiki in that standalone single file configuration.
[4749.52 --> 4757.18]  But the material for getting up and running on Node.js is still not as straightforward and easy as it should be.
[4757.18 --> 4765.36]  So, helping with the documentation in TiddlyWiki is quite a good way to start because the documentation is written in TiddlyWiki.
[4765.54 --> 4770.70]  So, making a contribution to the documentation is itself working with TiddlyWiki.
[4770.70 --> 4782.82]  And then, for a long time at the beginning of TiddlyWiki, it was actually writing, beginning of the rewrite, it was writing the documentation that drove the development.
[4783.32 --> 4793.12]  I was busy writing the tech docs and then trying to write the features I needed of TiddlyWiki in order to present those documents.
[4793.12 --> 4805.18]  So, given the fact that you began on a Sinclair MK14, you've been hacking since, and the positive, the white hat version of hacking, not the negative.
[4805.54 --> 4817.44]  Given your expansive history with programming and languages and all the ups and downs of tech and how it's gone slow to you or gone fast to others, you've got to have a programming hero.
[4817.44 --> 4824.92]  I can't even imagine if it's just one, but if you could just give us one single programming hero, who might that be for you?
[4825.78 --> 4833.48]  Yeah, and I thought about this, and there's somebody who I became aware of in 1996.
[4834.08 --> 4840.50]  So, I guess I'll have other programming heroes from when I was younger, but it's Ward Cunningham.
[4840.66 --> 4843.26]  He's the developer of the original Wiki.
[4843.26 --> 4856.38]  And for me, the thing that actually first attracted my interest was a colleague showing me the thing first and then telling me that it was 700 lines of pearl.
[4857.40 --> 4872.12]  And I still think that's an incredibly impressive achievement, that such a powerful piece of software with profound implications that we've gradually learned as we've used it and built communities around it should be 700 lines of pearl.
[4872.12 --> 4902.10]  Pretty amazing stuff.
[4902.10 --> 4903.10]  I think that's what I think.
[4903.10 --> 4904.10]  I think that's what I think we've always learned as we've experienced in the world.
[4904.10 --> 4906.10]  I think that's what I've heard of, but I think that's the most inspiring thing.
[4906.10 --> 4913.30]  I think the most inspiring thing is that you haven't stopped.
[4913.30 --> 4919.62]  You know, is that 30 years later, how many ever years later, whatever the actual number is, you're still going.
[4919.62 --> 4923.38]  So there's something encouraging in open source or something encouraging in this community.
[4923.92 --> 4928.84]  And I think what, if you didn't say it directly, I think a lot of your thoughts and a lot of
[4928.84 --> 4932.60]  your passion shares that this is a rich, vibrant thing to do.
[4932.90 --> 4936.88]  And that it's, it's encouraging to those who might be listening to the show that's thinking
[4936.88 --> 4938.36]  is open source for me.
[4938.44 --> 4939.48]  You know, I'm not getting paid.
[4939.56 --> 4944.78]  I'm not getting retribution for it, but it's, it's inspiring to see that you've kept it
[4944.78 --> 4948.94]  going for all these years, but anything else you want to say in closing before we tell
[4948.94 --> 4949.26]  the show?
[4950.04 --> 4951.32]  Yeah, please.
[4951.72 --> 4955.32]  If you like what, if you like what you've heard, please give TiddlyWiki a try.
[4955.48 --> 4956.98]  It's the easiest thing in the world.
[4957.12 --> 4960.32]  Just go to tiddlywiki.com in your browser and give it a go.
[4960.86 --> 4961.22]  Fantastic.
[4961.48 --> 4963.66]  And as I said, it was awesome to have you on the show today.
[4963.80 --> 4966.02]  Thank you so much for spending this time with us.
[4966.02 --> 4969.82]  To the listeners out there, we thank you for sharing the time as well to hear Jeremy's
[4969.82 --> 4972.10]  past and his history he shared here today.
[4972.96 --> 4974.64]  And those who sponsored the show, we love you.
[4974.66 --> 4975.28]  We thank you.
[4975.58 --> 4977.24]  And our members, you guys rock.
[4977.24 --> 4979.92]  Up next, we do have some big shows.
[4979.98 --> 4984.34]  We've been mentioning these shows and we're excited about the next few weeks of the change
[4984.34 --> 4984.48]  law.
[4984.56 --> 4987.80]  We got the future of WordPress and Calypso with Matt Mullenweg.
[4988.26 --> 4993.24]  And we also have a big show we're working on with Matt's 20 years of Ruby.
[4993.24 --> 4997.12]  So if you're a Rubyist, if you've ever even thought about writing Ruby, if you've ever
[4997.12 --> 5001.24]  envied Ruby, you want to listen to this show and you want to tell every single person you
[5001.24 --> 5002.66]  know that we're doing the show with Matt's.
[5002.90 --> 5003.66]  It's going to be awesome.
[5003.66 --> 5004.82]  20 year history.
[5005.12 --> 5009.28]  We've also got Raquel Velez, RockBot, NPM in the pipeline.
[5009.44 --> 5010.36]  So stay tuned for that.
[5011.12 --> 5012.08]  And that's it, guys.
[5012.20 --> 5012.98]  So let's tail out.
[5013.10 --> 5013.94]  Let's say goodbye.
[5014.48 --> 5014.74]  Bye.
[5014.82 --> 5015.28]  Thanks, Jeremy.
[5015.36 --> 5015.94]  Thanks for coming on.
[5016.30 --> 5016.82]  Thanks, Jared.
[5016.92 --> 5017.42]  Thanks, Adam.
[5017.62 --> 5018.28]  Thanks very much.
[5018.34 --> 5018.50]  Bye.
[5018.50 --> 5018.56]  Bye.
[5018.56 --> 5018.60]  Bye.
[5018.60 --> 5018.64]  Bye.
[5018.64 --> 5018.72]  Bye.
[5018.72 --> 5020.60]  Bye.
[5020.60 --> 5020.72]  Bye.
[5020.72 --> 5022.60]  Bye.
[5022.60 --> 5022.72]  Bye.
[5022.72 --> 5022.78]  Bye.
[5022.78 --> 5022.82]  Bye.
[5022.82 --> 5022.88]  Bye.
[5022.88 --> 5022.92]  Bye.
[5022.92 --> 5022.94]  Bye.
[5022.94 --> 5023.00]  Bye.
[5023.00 --> 5023.02]  Bye.
[5023.02 --> 5023.04]  Bye.
[5023.04 --> 5023.06]  Bye.
[5023.06 --> 5023.12]  Bye.
[5023.12 --> 5023.16]  Bye.
[5023.16 --> 5023.54]  Bye.
[5023.54 --> 5024.04]  Bye.
[5024.04 --> 5024.12]  Bye.
[5024.12 --> 5025.16]  Bye.
[5025.16 --> 5026.08]  Bye.
[5026.08 --> 5027.12]  Bye.
[5027.12 --> 5027.60]  Bye.
[5027.60 --> 5028.12]  Bye.
[5028.12 --> 5029.16]  Bye.
[5029.16 --> 5029.68]  Bye.
[5029.68 --> 5030.10]  Bye.
[5030.10 --> 5030.66]  Bye.
[5033.66 --> 5034.10]  Bye.
[5034.10 --> 5034.38]  Bye.
[5034.38 --> 5035.02]  Bye.
[5035.12 --> 5035.44]  Bye.
[5035.44 --> 5035.64]  Bye.
[5035.64 --> 5036.14]  Bye.
[5043.94 --> 5048.02]  Bye.
[5048.02 --> 5048.24]  Bye.
[5051.76 --> 5053.16]  Bye.
