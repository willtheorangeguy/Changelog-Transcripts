[0.00 --> 18.52]  Welcome to the ChangeLog episode 0.3.6.
[18.78 --> 19.74]  I'm Adam Stachowiak.
[20.32 --> 21.20]  And I'm Wynne Netherland.
[21.40 --> 22.32]  This is the ChangeLog.
[22.38 --> 24.32]  We cover what's fresh and new in the world of open source.
[24.82 --> 27.80]  If you found us on iTunes, we're also on the web at thechangelog.com.
[27.80 --> 30.82]  And we're also up on github.com forward slash explore.
[30.92 --> 34.98]  You'll find some trendy repos, some feature repos from our blog, as well as the audio podcasts.
[35.20 --> 37.10]  If you're on Twitter, follow ChangeLog Show.
[37.34 --> 38.02]  And I'm Adam Stach.
[38.62 --> 41.08]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[41.62 --> 42.46]  Fun episode this week.
[42.52 --> 46.04]  Talk to Pragmatic Badger, the fellows over there that put on the Django Dash.
[46.20 --> 47.80]  That's kind of like the Rails Rumble, right?
[48.50 --> 50.92]  Right, or the Node Knockout, which we covered in 033.
[51.34 --> 53.62]  These 48-hour coding competitions.
[54.24 --> 58.36]  Yeah, we're also going to be talking to the Rails Rumble guys whenever their competition wraps up, too.
[58.42 --> 59.30]  So that'll be kind of fun as well.
[59.84 --> 60.74]  Looking forward to that.
[60.78 --> 62.42]  I guess this is the first year with Rails 3.
[62.52 --> 66.04]  We'll see what people can do in the new version of Rails and the Rails Rumble.
[66.56 --> 67.14]  Yeah, absolutely.
[67.64 --> 72.32]  I also want to mention that we're working with Jason Seifer of the Dev Show and Ruby Show of Fame.
[72.50 --> 74.54]  He runs GeniusPool.com.
[74.64 --> 79.18]  It's a job board that connects employers and job seekers in a very targeted way.
[79.18 --> 86.08]  They have the Genius Pool Network, which gives extra opportunities for promoting your job to the right kind of audience.
[86.30 --> 89.46]  So we're a part of it, and the Dev Show is a part of it.
[89.52 --> 90.50]  The Ruby Show is a part of it.
[90.56 --> 93.38]  So if you're hiring a developer, head to GeniusPool.com right now.
[93.78 --> 94.40]  Post a job.
[94.46 --> 97.00]  And if you check the box next to the change log for an extra $100,
[97.58 --> 100.10]  we'll read your posting live on air in a future podcast.
[100.34 --> 100.98]  GeniusPool.com.
[101.66 --> 102.42]  Fun episode this week.
[102.46 --> 103.02]  Should we get to it?
[103.48 --> 104.04]  Let's do it.
[104.04 --> 113.44]  All right.
[113.46 --> 117.54]  We're joined today by Christian, Daniel, and Matt from Pragmatic Badger,
[117.82 --> 119.72]  the organizers behind Django Dash.
[120.20 --> 124.32]  So Daniel, why don't you go first, introduce yourself, who you are, and why we should care.
[125.08 --> 126.30]  I'm Daniel Lindsley.
[126.52 --> 130.24]  I'm the primary organizer of the Django Dash.
[130.24 --> 135.24]  I've been running the contest for three years, but this year have been joined by Matt and Christian.
[136.02 --> 143.18]  And I am primarily a developer, but I do a little bit of design if Christian lets me touch the mouse again.
[143.68 --> 144.50]  I'll go next then.
[145.72 --> 149.36]  I, Christian Metz, I'm our designer.
[149.48 --> 155.38]  I make things pretty and worry about how people interact with whatever it is we're working on.
[155.38 --> 161.88]  And slow things down from time to time, but it's all good.
[163.38 --> 168.02]  And I'm Matt Croydon, and I know better than to touch Christian's templates.
[169.70 --> 175.84]  So Daniel, tell us a little bit about how the Django Dash came about and how it got started and how many years you've been doing it.
[175.84 --> 176.28]  Okay.
[177.34 --> 181.52]  So in 2008 was the first Django Dash.
[181.68 --> 186.46]  I was actually a full-time Ruby on Rails programmer at the time.
[187.30 --> 195.06]  But I've been in the Django community ever since 0.90 was released of Django back in, I think, 2006.
[195.06 --> 208.16]  And I kind of was looking around, and I had just finished a Pi Week competition, which is a make-a-python-based video game contest that you get a full week to do.
[208.50 --> 212.52]  And I was really excited off of that because I had enjoyed it a lot.
[212.68 --> 218.24]  And I looked around and saw the Rails Rumble, obviously, and as well as a couple other contests, and thought,
[218.24 --> 224.46]  man, it'd be really awesome if the Django community had something like this because there was no contest like that.
[225.06 --> 236.56]  So by myself in my side time, I put together a site, got some people interested in it, and we did the first Django Dash in 2008.
[236.96 --> 241.94]  Had about 40 or 50 contestants, or I should say teams competing.
[242.06 --> 243.34]  There was probably about 75 people.
[244.48 --> 250.52]  And had some hiccups, but it went really well and wanted to continue on doing it for the community.
[251.10 --> 253.34]  So you guys just wrapped the 2010 competition.
[253.34 --> 255.50]  How many entries did you have this year?
[256.32 --> 261.24]  We had, originally we had approximately 55 teams sign up.
[261.38 --> 269.80]  However, just as the effect of being an event between a lot of people, final competing teams were about 43, I believe.
[270.26 --> 274.04]  And 75 people competed out of the 105 that had registered.
[274.04 --> 281.06]  So a little bit down from last year's competition, but we had a really strong showing from everybody.
[281.30 --> 282.42]  So it was okay.
[283.04 --> 285.12]  So give us an overview of the rules of the competition.
[285.12 --> 290.72]  So the Django Dash has a couple critical rules.
[290.82 --> 298.20]  First of all, it's a 48-hour contest, so you get 48 hours based off of central time to start a project.
[298.40 --> 300.42]  You get no code, no pixels ahead of time.
[300.42 --> 306.52]  You can do on-paper designs, but no digital assets ready before you start the competition.
[307.36 --> 313.28]  Teams can be up to three, though we've had some really strong two- and even one-person competitors in the past.
[315.38 --> 316.74]  Third-party code is allowed.
[316.74 --> 325.54]  New to us this year in our rules is that you're allowed to use DVCS, so via GitHub or Bitbucket's post-commit hooks.
[326.50 --> 332.24]  You're allowed to just have your own repo, commit to it as you want through the competition, and then we just pull down the data.
[334.34 --> 337.96]  And also new to us this year is that all entries must be open source.
[338.58 --> 345.28]  So whatever you build during the 48-hour competition should be publicly available to others, have a license, and all that jazz.
[345.28 --> 348.22]  So what CVSs were you using in previous years?
[349.46 --> 358.28]  In the previous two years, we had standardized on Subversion, partially because it's the minimum barrier to entry.
[358.58 --> 367.86]  Django itself is hosted in Subversion just simply because everyone can get to Subversion, whether you're using Git or Mercurial or Subversion itself or something else.
[368.24 --> 373.14]  It's like lowest common denominator, so it's easy for everyone to get up and going.
[373.14 --> 385.96]  It also, in the previous years, made it easier to judge exactly how much people were committing as well as just getting a full that no one was cheating, making sure things were shut down on time and stuff.
[386.20 --> 391.86]  Because I was all by myself, I needed something that was easy and I could kind of control through the process.
[391.86 --> 397.46]  But a lot of people wanted DVCS and I did too because I hate running Subversion servers.
[398.22 --> 402.20]  So this year we decided, hey, this is the year to go DVCS.
[403.06 --> 408.58]  And via post-commits hooks, it worked out really great with both GitHub and Bitbucket.
[408.58 --> 412.20]  Matt and I weren't officially involved last year.
[412.28 --> 416.00]  We did jump in to help as when Daniel was working on this.
[416.88 --> 419.96]  And Subversion was one of the things that was a pain point.
[420.38 --> 424.32]  Just making sure everybody had accounts, everybody's things were working correctly.
[424.48 --> 435.78]  And it was quite a bit easier to let them put their own repos on GitHub or Bitbucket and just pull in their commits as they happen.
[435.78 --> 442.42]  And I'm curious, what was the ratio of Git repositories versus Mercurial in the projects that were submitted?
[442.82 --> 446.44]  There were a lot more Git repositories.
[446.74 --> 453.44]  I believe out of the 55 teams that were signed up, we had 53 GitHub and 2 Bitbucket.
[454.12 --> 459.82]  But the 2 Bitbucket teams that competed actually did commit to their repos quite a bit.
[459.90 --> 462.46]  And one of them was in our top 10 team's interest.
[462.46 --> 467.30]  So we wanted to provide better support for that.
[467.42 --> 470.16]  And there have been, in the past, many more people that wanted it.
[470.26 --> 473.76]  But this year, it just fell out that there were more Gitters than Mercurialers.
[473.98 --> 476.92]  So who wins in a Bitbucket versus GitHub deathmatch?
[477.74 --> 479.52]  I think GitHub wins.
[480.98 --> 481.86]  GitHub wins?
[482.12 --> 482.32]  Yeah.
[482.56 --> 486.20]  I think statistically, GitHub has taken the match.
[486.20 --> 490.70]  So Bitbucket, I'm not as familiar with Bitbucket.
[490.80 --> 494.42]  It comes from a Python heritage, I guess?
[494.96 --> 495.22]  Yes.
[495.34 --> 497.48]  They are a full Django shop.
[497.86 --> 504.32]  The primary guy who runs it, Jesper, is actually the gentleman who created Piston,
[504.54 --> 510.02]  which is a big, relatively popular Django API, plug-in app.
[510.02 --> 516.12]  They run on Django 1.2, a recent version of Piston, full Mercurial.
[516.44 --> 520.86]  And they shoot to provide many, if not all, the same features that GitHub does.
[521.36 --> 523.48]  And their site is actually really quite good.
[524.44 --> 529.20]  It's mostly, it actually literally comes down to, do you prefer Git or Mercurial?
[529.68 --> 532.54]  And they do a really good job of supporting stuff.
[532.64 --> 533.46]  They're very responsive.
[533.46 --> 536.40]  And they just launched on some new hardware.
[536.52 --> 537.76]  So their site is really fast now.
[538.04 --> 540.38]  So they're really great people to work with.
[540.70 --> 545.86]  I can't say enough good things about Jesper, as well as Chris on the GitHub side.
[546.56 --> 547.44]  And they're good.
[547.48 --> 548.30]  They're great sponsors.
[548.48 --> 549.24]  They're very responsive.
[549.38 --> 552.62]  They were happy to host everybody's repos and just happy things all around.
[553.12 --> 557.50]  So Daniel, you mentioned you were full-time Ruby on Rails before organizing the Django Dash.
[558.08 --> 560.62]  So I guess you're a Rubyist and a Pythonista.
[560.62 --> 565.34]  So what is the best feature from Python that Ruby has not yet ripped off?
[567.50 --> 568.02]  Man.
[572.28 --> 573.44]  Whitespace indentation?
[573.64 --> 574.72]  Oh, sorry.
[576.66 --> 578.74]  I think my favorite is explicit imports.
[580.14 --> 584.78]  In Python code, you can sort of import everything from somewhere.
[584.94 --> 586.82]  But you generally import the things you need.
[586.82 --> 593.46]  And it makes it much easier to take someone else's code, figure out what they're using, where it comes from, and what it relies on.
[594.00 --> 597.68]  And it definitely makes it something I appreciate about Python.
[597.68 --> 606.48]  My actual, my preference personally is actually Django's, or not Django, I'm sorry, Python's module system.
[607.90 --> 619.12]  I prefer the way that code is structured in a Python module to the more Ruby way where you have a top-level file that's named what you want the package to be named.
[619.12 --> 622.46]  And then there's the lib folder that has everything kind of strewn inside of it.
[623.58 --> 632.50]  Versus with Python, it's just like, hey, drop an init.py someplace, and you can structure the module a little bit, I guess, more samely to me.
[632.72 --> 636.88]  Like, I don't just look at a module that's not just lib, and in there is who knows what.
[637.24 --> 639.34]  Like, I can see exactly how the structure looks.
[639.34 --> 643.58]  It's small, and you can do it other ways, obviously.
[644.38 --> 649.32]  So from a web development perspective, what was it like transitioning from Rails to Django?
[650.06 --> 659.34]  You know, all the bike shedding and kind of the BS on each side, really, Django and Rails are a lot more alike than they are separate.
[659.34 --> 665.78]  I mean, you have two really dynamic, powerful languages that follow very similar setups.
[665.94 --> 670.12]  I mean, you've got, you know, your database forms the foundation of everything.
[670.30 --> 673.88]  Above that, you've got a really competent ORM system.
[675.20 --> 680.72]  Controllers versus views are, like, just two different ways of looking at things.
[680.88 --> 683.50]  Honestly, you write your application logic in very similar ways.
[683.50 --> 696.66]  Middleware is there, and both of them both have decent template systems, and really, I find it personally relatively easy to move between them versus moving between other things.
[698.40 --> 706.52]  So I think, yes, there are a lot of differences, but I think they're very minor in comparison to a lot of other frameworks out there that people use.
[707.44 --> 711.50]  Do you think today's web developer really needs to be a multi-language developer?
[711.50 --> 714.76]  Absolutely. Absolutely. That's my opinion.
[714.94 --> 733.72]  I don't know how Christian and Matt feel on that, but my personal goal is to learn at least one new language or one new framework or one new way of looking at things every year because I view myself primarily as a programmer, and it just comes by extension that I work primarily within Python and Django.
[733.72 --> 744.48]  But being well-rounded opens you to new ideas, new perspectives, new ways of attacking things, and I think just really improves you personally overall.
[744.48 --> 751.40]  I think it's great to be knowledgeable in lots of different languages and be picking up stuff.
[752.04 --> 764.30]  I've been doing a lot of, along with the rest of the world, a lot of Node.js stuff recently, and it's great to come into a language and an environment and sort of look at, okay, what here is the same?
[764.30 --> 773.22]  What's the same as sort of everything I know and what's new here and kind of focusing on what's a little different and what you haven't maybe done before?
[773.86 --> 778.28]  I think the listeners might think we have a conspiracy to mention Node in every episode.
[778.40 --> 779.00]  We really don't.
[779.08 --> 780.32]  It's just that hot.
[780.32 --> 792.62]  One of the future episodes we're putting together right now is an async slash evented web episode where we'll talk about Twisted and talk about Event Machine and Node and some of those others.
[792.76 --> 794.42]  But why is Node so popular?
[794.54 --> 796.86]  Why is it hitting such a chord with developers right now?
[797.68 --> 805.14]  I think for me it's fun and extremely easy to do the right thing and do really proficient things.
[805.14 --> 814.18]  I know there's lots and lots of async platforms out there, but I think honestly none of them is as fun to work with as Node is.
[814.74 --> 821.18]  I personally prefer the really strong callback and event setup that is present in Node.
[823.20 --> 825.12]  I've done Twisted a little bit before.
[825.30 --> 833.44]  I've done some gEvent stuff or eventlet in Python, and I looked at Event Machine for a while while I was doing Ruby stuff.
[833.44 --> 844.52]  And that in conjunction with all the threading models and the multiprocessing model and stuff, I really, to me, callbacks and events make much more sense.
[844.68 --> 846.38]  And it is, like Matt said, it's a lot of fun.
[846.56 --> 854.78]  The hype is kind of crazy, but there are some really good libraries out there right now, and it's coming along, and it's interesting.
[856.16 --> 857.70]  So, Christian, you're the designer of the group, right?
[858.48 --> 859.08]  I am.
[859.08 --> 865.58]  So, I guess this would be perfect for the white space aware community in Python.
[865.78 --> 869.38]  So, what inroads, if any, have Hamill and SAS made in the Python community?
[872.24 --> 873.66]  Hamill, not very much at all.
[876.00 --> 885.04]  And I think it's just because a lot of us, myself included, feel like it's too much abstraction from the HTML that I want to get at.
[885.04 --> 891.34]  So, SAS, however, is sort of more polarized.
[891.60 --> 894.56]  There's people who like it a lot and people who hate it a lot.
[894.92 --> 905.56]  And we've been using it for one of our own projects, forkinit.com, so plug for that, which is a recipe management site.
[905.56 --> 912.38]  So, it's my first time actually working with SAS in a serious use it to power a project sense.
[912.86 --> 914.66]  And I'm really liking it.
[914.78 --> 927.58]  I don't feel entirely comfortable with it yet in the sense that I do things that I feel like I need to reorganize them a bit more and use it better because it's still new and a different way of thinking about things than I have been for years.
[928.00 --> 930.22]  But enjoying it, and it's definitely helping a lot.
[930.22 --> 933.18]  What integration with your Python project do you have?
[933.36 --> 936.84]  Are you just using it from a command line standpoint, or are there hooks in your project?
[937.48 --> 939.74]  Right now, we're using it from a command line.
[940.10 --> 946.76]  While we're doing local development, we run Compass to keep things compiled, and we just check in the compiled CSS.
[947.14 --> 950.60]  We don't do anything live with SAS right now.
[951.10 --> 952.44]  And don't let Christian lie to you.
[952.50 --> 956.30]  He's got some serious development chops, so he's not just Mr. Designer either.
[956.74 --> 957.06]  Awesome.
[957.76 --> 959.18]  So, what's the state of Python?
[959.18 --> 959.94]  Is it growing?
[960.22 --> 962.96]  Because Ruby seems to be not cooling off.
[963.04 --> 964.94]  What's the state of the Python universe?
[965.84 --> 968.64]  I think that Python is still continuing to grow.
[970.26 --> 973.26]  I've heard of a lot of new and bigger sites that have been launching.
[973.50 --> 975.70]  I know lots of people that have been getting into it.
[976.72 --> 979.54]  It seems like, to me, there's more and more prolific projects.
[979.70 --> 982.40]  And it's not just Django-driven.
[982.40 --> 994.44]  Like, there's other people who are using it with other frameworks like Flask or WebPy or just like doing App Engine stuff and stuff.
[994.44 --> 996.44]  And I think it's growing.
[996.44 --> 998.62]  I think a lot of people are coming around to it.
[998.62 --> 1001.42]  And it's just like Ruby.
[1001.42 --> 1011.28]  You have a huge number of positive gains from using this active dynamic language that's seeing a lot of work with a lot of different VMs.
[1011.28 --> 1014.92]  And it's a really good time for dynamic languages.
[1014.92 --> 1021.24]  Speaking of virtual machine optimization, what are your thoughts on the development of PyPy and Unladen Swallow?
[1021.24 --> 1021.88]  Awesome.
[1024.86 --> 1026.40]  I'm continually blown away.
[1026.62 --> 1032.28]  I don't actively use either of them, but have installed both of them in the past.
[1032.52 --> 1040.68]  And just watching how their performance numbers are getting better and better all the time and how much more compatible they're getting.
[1040.84 --> 1044.76]  I mean, PyPy sat for a long time being really fast, but it was just the subset of Python.
[1044.90 --> 1047.06]  You couldn't use it with a lot of other modules.
[1047.06 --> 1049.18]  And some stuff was just horrifically slow.
[1049.18 --> 1053.42]  But they're improving stuff across the board these days, and it's getting better and better and better.
[1053.70 --> 1055.20]  So it's really impressive.
[1056.10 --> 1059.16]  I'm personally very excited about the development of PyPy in particular.
[1059.88 --> 1064.60]  The main reason for me is that I'd love to contribute to the Python core, but I can't because I'm not a C developer.
[1065.46 --> 1069.02]  I'm pretty sure the Ruby equivalent to PyPy is Rubinius, correct?
[1070.32 --> 1071.12]  Yeah, Rubinius.
[1071.76 --> 1077.76]  I've been watching that too just because I try to keep at least interested in what the Rails and Ruby community are doing.
[1077.76 --> 1083.28]  And, yeah, they're very analogous, and it's really interesting watching both of them develop.
[1084.20 --> 1086.36]  What Dash projects really stood out to you this year?
[1087.22 --> 1087.46]  Ooh.
[1087.46 --> 1112.70]  So Read the Docs is pretty impressive because they've taken Sphinx documentation and let you – basically given you a site where everyone can host their docs easily with just a post-commit hook on their end.
[1113.00 --> 1113.86]  So that's interesting.
[1113.86 --> 1120.14]  The team that won Great Big Crane has a phenomenal continuous integration system.
[1120.68 --> 1125.76]  If you go to their website, it's actually – it's just an about page, which does them a big disservice.
[1126.06 --> 1129.72]  But if you install it, man, it is crazy.
[1129.86 --> 1132.32]  It's actually better than Hudson, in my opinion.
[1133.32 --> 1133.54]  Hmm.
[1133.62 --> 1134.50]  I'll have to give that a try.
[1134.98 --> 1136.58]  I've been spending a lot of time with Hudson lately.
[1136.90 --> 1138.48]  Will it email you when a test fails?
[1138.48 --> 1138.96]  Yeah.
[1139.20 --> 1139.60]  Yeah.
[1139.80 --> 1140.02]  Yep.
[1140.36 --> 1143.22]  And it has a really nice user interface.
[1143.50 --> 1146.14]  I like it better than Hudson, so I'm a big fan of Hudson.
[1147.62 --> 1149.30]  So you say it's not PIP-based?
[1149.46 --> 1149.62]  Yep.
[1149.96 --> 1155.70]  I wish it were PIP-based, but, I mean, for 48 hours and what they are probably used to, still phenomenal.
[1156.60 --> 1157.62]  So those two are good.
[1157.62 --> 1166.92]  And I kind of crushed on Minoria, which was done by two of the lead Pinax devs.
[1167.08 --> 1171.72]  They did an open-source, massively multiplayer city-building game.
[1171.82 --> 1179.12]  So you could think of it as like an RPG meets SimCity meets 8-bit graphics.
[1179.12 --> 1182.06]  And so that was pretty cool.
[1183.22 --> 1187.34]  I really enjoyed the Servertail project.
[1187.86 --> 1197.58]  It was definitely cool to see a Django project focusing more on some of the real-time stuff that people might think Django isn't so good at.
[1197.80 --> 1199.92]  And I think that proved them wrong pretty well.
[1200.24 --> 1203.76]  How did the entries this year compare to years past as far as quality?
[1203.98 --> 1206.32]  I think we saw much higher quality this year.
[1206.32 --> 1217.22]  The top eight or nine sites easily could just go out and launch today and have something that's really, at least really impressive.
[1217.38 --> 1222.26]  And many of them could probably, you know, charge or put ads on that and be doing pretty well for themselves.
[1222.96 --> 1225.58]  Whereas in years past, it's been a smaller number.
[1226.38 --> 1235.08]  We had a lot more teams compete and produce full working projects by the end of the competition this year than we have any previous year.
[1235.08 --> 1239.00]  And it was just, it was really, really good.
[1239.14 --> 1242.68]  Judging was a very, very difficult process this year.
[1243.18 --> 1250.60]  Not because it was hard to work with the projects, but because they were so good in the quality of the code and design and everything was so much higher.
[1251.24 --> 1255.54]  In past years, have you seen any of the entries actually evolve into full-blown projects?
[1255.76 --> 1257.70]  I know that's often the case in the Rails Rumble.
[1257.70 --> 1260.82]  I wish I could say yes, but it hasn't really happened.
[1261.60 --> 1268.90]  From the previous two years worth of stuff, there's only a small handful of sites that I'm aware of that are still online and active.
[1270.94 --> 1275.02]  And a lot of them didn't see much future development as far as I saw.
[1275.62 --> 1281.38]  I think that might change this year, but just because of what was entered and what was there.
[1281.58 --> 1282.62]  But time will tell.
[1282.62 --> 1293.12]  You know, one of the things I like about these competitions is they allow you to work on other teams outside of, especially if you have a small company that you're used to working with the same folks day in and day out.
[1293.56 --> 1301.82]  A lot of times these types of competitions allow you to form virtual teams outside of that company and work with other people and pair with other people and exchange ideas.
[1302.24 --> 1305.74]  So sometimes the upside is beyond even what you create.
[1305.74 --> 1306.54]  Oh, totally.
[1308.08 --> 1315.48]  It's really impressive to watch how the teams have actually become more geographically distributed and more global.
[1315.78 --> 1322.54]  We had a lot of non-Western teams enter this year.
[1322.84 --> 1325.20]  And we had a couple teams from Australia.
[1325.48 --> 1331.68]  We had a couple teams from Russia, from Europe, from just all over.
[1331.68 --> 1333.90]  And I think we even had an Asian team or two.
[1334.60 --> 1341.32]  And it was just – it was really excellent to see just a lot of separate people working together.
[1341.78 --> 1351.34]  And hanging out in the IRC channel was fun because there was just people constantly talking and collaborating, even across teams, helping each other out.
[1351.36 --> 1353.12]  And it was really great to watch.
[1353.12 --> 1362.58]  You know, I've found that to be a plus if you've got a really widely distributed team as far as being in the States and Asia, Australia, and Europe.
[1362.58 --> 1368.80]  Then if you have that around-the-clock coverage, folks can code while other folks catnap.
[1369.08 --> 1370.90]  So really your project keeps going.
[1370.90 --> 1379.24]  One of the things I want to talk about this – or speak to this year is that by having the code hosted in the open on Bitbucket and GitHub,
[1379.82 --> 1390.00]  and then when we're running the change – the commit list on the website, all those linked back to the actual commits on the hosting sites.
[1390.26 --> 1391.98]  So either on GitHub or Bitbucket.
[1391.98 --> 1397.76]  And like last year, since it was all in subversion and all sort of hosted in private, you couldn't actually see what each other was doing.
[1397.90 --> 1399.22]  You could see, you know, yes, somebody committed.
[1399.36 --> 1403.68]  We ran a commit log, but it wasn't a I can click through and actually see what they're doing.
[1403.92 --> 1409.18]  So there was a lot more people, you know, watching each other's commits, talking about them, doing a lot more,
[1409.60 --> 1414.12]  interacting in the IRC channel this year than there has been in years previous, and that was a lot of fun.
[1414.58 --> 1414.74]  Cool.
[1414.84 --> 1420.00]  This is the part of the show where we kind of turn it upside down and ask our guests what's on your open source radar.
[1420.00 --> 1421.92]  So, Daniel, we'll start with you.
[1422.02 --> 1425.68]  What outside of Django Dash has got you excited?
[1426.02 --> 1427.10]  It can be in the Python community.
[1427.16 --> 1429.72]  It can be anywhere that you just want to check out.
[1430.18 --> 1435.78]  I've been doing a lot of Node stuff lately, not because of the hype, but just because it's interesting, it's fun,
[1436.36 --> 1440.84]  and you get to play with a different domain of projects than I normally get to.
[1441.44 --> 1442.20]  I miss Gopher.
[1442.82 --> 1443.86]  Just going to get that out there.
[1443.88 --> 1444.96]  Gopher was fun, wasn't it?
[1445.52 --> 1447.00]  The Lynx browser?
[1447.00 --> 1452.68]  Yeah, dude, I was all about the browsing of my terminals when I was a little boy.
[1454.00 --> 1460.96]  But open source-wise, at work, we just published our first iPhone application.
[1461.14 --> 1462.28]  We used PhoneGap to do that.
[1462.80 --> 1467.00]  So I've been definitely interested in seeing what PhoneGap is doing.
[1467.10 --> 1467.98]  It's actually really clever.
[1467.98 --> 1476.26]  I'm not sure if you guys have looked into it at all, but it allows HTML and JavaScript to talk to Objective-C
[1476.26 --> 1483.92]  and implement native iPhone widgets and do other things, but you can still run a lot of your app using HTML and JavaScript
[1483.92 --> 1484.80]  and things you already know.
[1484.80 --> 1492.18]  So that allowed us to get something out there that we wouldn't have otherwise been able to do.
[1493.08 --> 1500.30]  And I'm actually definitely interested in being a bit more involved in that community and helping pick some of the things I didn't like about it.
[1500.44 --> 1504.00]  But there's a lot of promise there, and I'm excited to see that happen.
[1504.00 --> 1510.46]  Unlike the rest of the world, I haven't had a chance to actually do anything in Node yet, which makes me sad because I love JavaScript.
[1512.08 --> 1518.76]  I do think JavaScript is probably the most important language out there right now, not just because of Node,
[1519.06 --> 1527.16]  but because of how much browsers are improving and how much JavaScript can affect everything that we do on the Internet.
[1527.16 --> 1533.18]  So I'm excited to do something with that at some point.
[1534.28 --> 1540.92]  And I do actually think that's one of the appeals of Node, is that there are a lot of front-end developers and designers
[1540.92 --> 1550.72]  who have picked up programming from the JavaScript side and have had a certain amount of hesitance to get into other languages
[1550.72 --> 1552.06]  and dig deeper in things.
[1552.06 --> 1557.62]  And I feel like having something there in JavaScript allows them to reuse some of that and get more involved
[1557.62 --> 1561.96]  and helping to fuel the interest, I think.
[1562.88 --> 1566.16]  It's really amazing what we can do with JavaScript when we're not shackled to the DOM.
[1566.44 --> 1566.84]  Indeed.
[1567.86 --> 1573.22]  You know, I came across the Django Dash, I guess, in Episode 015 with Leah Culver.
[1573.62 --> 1575.64]  She had mentioned it, and that was the first I'd heard of it.
[1575.66 --> 1579.12]  I was excited to hear that Python had its own competition.
[1579.36 --> 1580.82]  So did Leah compete this year?
[1581.04 --> 1581.72]  She did not.
[1581.72 --> 1585.76]  She was actually signed up, and she has competed, I believe, both of the last two years.
[1586.26 --> 1592.84]  She and Chris Wonstroth were signed up last year, and they did Leafy Chat, which was one of the top three finalists.
[1593.22 --> 1598.20]  They were signed up for this year, and I believe they had something else that came up that they couldn't get to.
[1599.32 --> 1599.72]  Understandable.
[1599.92 --> 1601.36]  Well, thanks for joining us today, guys.
[1601.72 --> 1602.64]  Fun competition.
[1602.98 --> 1604.78]  Hopefully we'll get some more Python on the changelog.
[1604.78 --> 1623.28]  See it in my eyes.
[1623.32 --> 1626.90]  So how could I forget when?
[1626.90 --> 1632.70]  I found myself for the first time.
[1632.70 --> 1636.40]  Safe in your arms.
[1636.40 --> 1638.52]  As a dark passion.
[1638.52 --> 1639.02]  caregiver.
[1639.14 --> 1639.68]  Be.
[1640.18 --> 1644.38]  I'm going to preocup about it.
[1644.56 --> 1646.06]  I'm not, I just sportsman.
[1646.06 --> 1647.46]  değilim.
[1647.46 --> 1647.86]  Be.
[1647.86 --> 1652.08]  I'm going to o FBI.
[1652.56 --> 1653.42]  So.
[1653.52 --> 1653.98]  three.
[1654.10 --> 1655.88]  I'm going to use the big wall.
