[0.00 --> 10.62]  Welcome back everyone.
[10.76 --> 13.58]  This is The Change Log, where our member-supported blog and podcast
[13.58 --> 16.14]  that come fresh and what's new in open source.
[16.74 --> 18.52]  You can check out the blog at thechangelog.com
[18.52 --> 22.04]  and our past shows at 5by5.tv slash changelog.
[22.10 --> 23.68]  I mentioned this just before the show started,
[23.80 --> 26.32]  but if you're listening live or you're listening on the podcast,
[26.32 --> 30.08]  you can go to 5by5.tv slash changelog slash latest
[30.08 --> 32.38]  to kind of catch up on some show notes while the show is going on.
[33.00 --> 35.98]  This show is hosted by myself, Adam Stachowiak, as well as Andrew Thorpe,
[36.04 --> 41.08]  but today Andrew won't be joining me because he is flying back from the Aloha State,
[41.20 --> 42.58]  so he was on vacation.
[42.86 --> 46.96]  But you can tune into this show live every Tuesday at 5 p.m. Central Standard Time
[46.96 --> 48.10]  right here at 5 by 5.
[48.64 --> 52.44]  And this is episode number 93, and today we're joined by Phil LaPierre.
[52.44 --> 56.62]  He is a product designer at ThoughtBot,
[57.00 --> 59.60]  and the creator as well as maintainer of Bourbon,
[59.70 --> 62.94]  which is a simple and lightweight mix-in library for SaaS.
[63.20 --> 65.20]  So, Phil, welcome to the show, my friend.
[65.38 --> 66.54]  Hey, Adam. Thanks for having me.
[67.34 --> 69.42]  That's quite the little intro I just did there, man.
[69.42 --> 70.94]  I don't think I've ever done one that long before.
[71.18 --> 71.80]  Yeah, well, yeah, yeah.
[71.80 --> 73.18]  I'm not really digging long intros.
[73.72 --> 74.72]  I feel welcomed.
[75.92 --> 80.28]  Well, you know, I've been a fan of ThoughtBot, for one,
[80.28 --> 82.14]  and the work you've been doing with Bourbon.
[82.26 --> 85.60]  So I thought now's a good time since Andrew can't make the show.
[85.76 --> 90.90]  You know, why not play on the side of the fence that I kind of thrive at a bit more?
[91.30 --> 94.44]  You know, I have fun when we do this show and we talk a bit more dev speak,
[94.52 --> 95.56]  which is always enlightening for me.
[95.66 --> 99.68]  But let's face it, I'm still learning to be a true hacker.
[99.90 --> 103.96]  So I just – I'm always playing catch-up when it comes to that kind of chat.
[104.04 --> 105.62]  But I figured, hey, SaaS, right?
[105.62 --> 109.92]  Design SaaS, product design, a lot of fun stuff you do there at ThoughtBot.
[109.92 --> 115.68]  Yeah, I mean, ThoughtBot's a great place to work, and I do product design here.
[115.90 --> 121.16]  So what that entails, for us, our role is actually – it's kind of a weird role, I think,
[121.24 --> 126.62]  than maybe a traditional product designer might have at another tech startup.
[127.20 --> 135.62]  But we do design as well as front-end development, so writing HTML and CSS and SaaS, for that matter.
[135.62 --> 140.24]  And we also write JavaScript when the time calls for it.
[140.46 --> 144.48]  But usually any kind of really heavy JavaScript we leave to the developers here.
[145.34 --> 147.68]  You mean on the product design side, right?
[147.80 --> 148.94]  Yeah, product design side.
[149.06 --> 152.50]  So like Backbone, for instance, we've done a bunch of Backbone apps.
[152.76 --> 154.62]  Like that's all developer-heavy stuff.
[154.62 --> 161.76]  So I don't necessarily touch a ton of Backbone code besides like Vue-specific stuff.
[163.84 --> 164.56]  But yeah.
[166.20 --> 166.64]  Cool.
[167.12 --> 171.26]  So for the uninitiated, not so much on ThoughtBot, but more specifically yourself,
[171.68 --> 174.76]  what's a good introduction for you for those who don't know who you are?
[174.76 --> 177.50]  Well, a good introduction for me.
[178.26 --> 184.46]  I would call myself a hacker, a designer, always kind of interested in tinkering with code,
[185.20 --> 191.90]  making things look pretty, work pretty, making things usable on the web.
[192.74 --> 198.90]  So just a designer by day and, I don't know, cool guy by night.
[199.82 --> 200.42]  Nice.
[200.56 --> 202.30]  So how long have you been working at ThoughtBot?
[202.46 --> 204.12]  I haven't caught up on that yet.
[204.12 --> 207.26]  Yeah, so I've been here coming up on three years this summer.
[208.08 --> 208.26]  Wow.
[209.32 --> 209.80]  Yep.
[210.36 --> 212.88]  June or was it July start date?
[213.32 --> 214.52]  July, late July.
[215.02 --> 217.30]  That's a good start date for a lot of people.
[217.38 --> 219.34]  I like starting new things in the summertime.
[219.66 --> 220.28]  I don't know about you.
[220.64 --> 221.14]  Yeah, certainly.
[221.58 --> 224.60]  I mean, it's been awesome and I'm here in the Boston office.
[225.62 --> 228.24]  And Boston's like such a beautiful city to live in.
[228.52 --> 228.76]  Yeah.
[229.12 --> 231.38]  The summers here are just absolutely phenomenal.
[231.38 --> 237.50]  And when you say Boston, you say that because not only do you have the Boston office, but
[237.50 --> 239.04]  you also have San Francisco.
[239.46 --> 241.60]  And I believe, don't you have one in Europe now too?
[241.84 --> 243.26]  Yeah, we've got one in Stockholm.
[244.70 --> 245.44]  Wow, man.
[245.64 --> 245.80]  Yeah.
[245.80 --> 249.74]  So we opened the Boston office last year, or sorry, the San Francisco office last year.
[250.36 --> 252.60]  Stockholm, I think, came after that.
[253.02 --> 260.84]  And we opened up a Denver office, or sorry, Boulder office, I think this past winter.
[260.84 --> 265.32]  So when are you guys going to Austin, or Houston for that matter, I guess?
[265.70 --> 265.72]  Yeah.
[266.22 --> 266.86]  I don't know.
[266.94 --> 267.48]  Good question.
[268.82 --> 274.02]  It's kind of crazy to see how fast we've sort of been growing in various cities.
[274.56 --> 281.28]  And it's been good to see the support by the tech community for us there.
[281.44 --> 283.08]  You know, it's really cool.
[283.08 --> 289.94]  And for those who are really interested in the history of ThoughtBot, I am planning to
[289.94 --> 293.16]  get Chad Pytel, the founder of ThoughtBot, on Founders Talk soon.
[293.30 --> 296.94]  So for those who listen to Founders Talk, as well as the changelog, stay tuned for that
[296.94 --> 297.18]  episode.
[297.26 --> 298.80]  I'll definitely announce that.
[298.90 --> 299.80]  I can't wait to talk to Chad.
[299.86 --> 303.64]  I've talked to Chad a couple of times at different Ruby and Rails meetups, everything
[303.64 --> 306.46]  from like RailsConf to Lone Star RubyConf.
[307.08 --> 309.22]  Had some fajitas with him, I think, at one point in time.
[309.46 --> 310.78]  And he's a cool dude, man.
[310.80 --> 312.74]  I mean, I'm really proud of what you guys have done.
[312.74 --> 318.52]  Not only in, I mean, as a business and, you know, progressing, you know, business, the
[318.52 --> 323.28]  business of software, as you guys say, but, you know, just your tenacity for open source
[323.28 --> 324.26]  and your commitment to the community.
[324.34 --> 330.44]  I mean, it's, it's, it's, there's not many else out there quite like ThoughtBot.
[330.52 --> 331.90]  And you guys really do an awesome job.
[332.28 --> 332.78]  Yeah, thanks.
[332.92 --> 339.58]  Well, it's, it's really awesome that we've got Fridays to really be able to do what we
[339.58 --> 341.38]  call investment, investment days.
[341.38 --> 346.38]  And that's really where we get to contribute to open source or work on one of the products
[346.38 --> 347.96]  that we're developing internally here.
[348.64 --> 353.96]  So I think that really helps like push a bunch of stuff out to the open source community and
[353.96 --> 359.44]  get, you know, pull requests taken and issues resolved for all of our open source tools.
[360.08 --> 363.24]  So the entire day of Friday is dedicated to that?
[363.50 --> 363.80]  Yeah.
[363.80 --> 364.28]  Wow.
[365.96 --> 371.06]  I mean, that's, I mean, we can talk about maybe a bit later on, but that's touching on
[371.06 --> 372.42]  a subject I want to talk to you about.
[372.50 --> 377.68]  And I'm hoping you can share some details just around, like, it's been a trend the last few
[377.68 --> 378.40]  shows of the change law.
[378.42 --> 381.60]  I don't know if you're a listener of the change law, but just talking about sustaining
[381.60 --> 382.26]  open source.
[382.26 --> 387.48]  And, you know, you got a lot of people who really give their heart, blood and soul to
[387.48 --> 388.32]  a project.
[388.98 --> 394.26]  And, you know, not really at the community's intentions, but somehow that person that maintained
[394.26 --> 397.32]  that leader kind of gets wound down or get run down.
[397.54 --> 402.24]  And, you know, it's, that's been various topics over the last couple of years, but we've
[402.24 --> 406.88]  been seeing a trend more and more just talking about sustaining open source.
[406.88 --> 414.70]  And I know that at the bottom of all of ThoughtBot's open source projects, I'm trying to look up
[414.70 --> 419.82]  my notes because it says bourbon, well, I guess project name entered here, blah, is
[419.82 --> 422.22]  maintained and funded by ThoughtBot.
[422.30 --> 426.46]  And it just goes to show you what you said there with dedicating entire Fridays to open
[426.46 --> 426.74]  source.
[426.84 --> 431.72]  So we've kind of gone a little bit of a preamble there, but I don't mind diving a little bit
[431.72 --> 432.44]  deeper into it.
[432.44 --> 438.88]  But what does that do for, let's say, your culture as, as designers, developers, makers
[438.88 --> 441.12]  of the web at ThoughtBot?
[442.12 --> 443.44]  You mean that kind of commitment?
[443.94 --> 444.12]  Okay.
[444.40 --> 452.90]  Um, I mean, it's, it's really awesome in, you can feel that, that, uh, strive inside our office
[452.90 --> 455.66]  for wanting to contribute back to the community.
[455.66 --> 461.34]  Um, and I, and I think that's why we're getting such great, great stuff, um, that's coming
[461.34 --> 463.58]  out of, out of, uh, ThoughtBot.
[464.42 --> 469.76]  Um, because it's something that like people get to team up on Fridays and really work together
[469.76 --> 475.82]  to, you know, produce amazing open source tools and really like improve the community.
[475.82 --> 482.64]  Um, so I think it's, it's, yeah, it's something that, you know, it, it transcends, I guess,
[482.84 --> 488.94]  um, sort of the standard office culture where you just go in and kind of work on your, your
[488.94 --> 490.62]  project every single day.
[490.62 --> 495.70]  Cause it's, you know, it keeps you new and keeps you fresh to have, um, a good open source
[495.70 --> 498.44]  project that you can contribute to on Fridays.
[498.44 --> 503.02]  And since there's so many different open source tools, you know, you, it's, it's not like
[503.02 --> 503.80]  you're limited to one.
[503.90 --> 505.90]  You can contribute to a bunch of others.
[505.90 --> 506.28]  So.
[506.86 --> 507.04]  Right.
[508.24 --> 513.00]  And for those who may not be too familiar with ThoughtBot, shame on you if you're not,
[513.48 --> 518.16]  um, you guys mainly are, uh, a Ruby in Rails.
[518.62 --> 521.96]  Uh, I guess, I don't even know if shop really applies to you guys anymore.
[521.96 --> 528.12]  It's more like, uh, I mean, cause you, when you span four to five offices or potentially five
[528.12 --> 533.00]  offices soon, hopefully, um, you know, I don't know if you're a consider software shop, but
[533.00 --> 535.66]  you guys are mainly on the Ruby rail stack.
[535.82 --> 538.08]  Uh, obviously you do some stuff in JavaScript as well though, right?
[538.48 --> 543.50]  Yeah, we do some stuff in JavaScript, um, as far as branching into, um, backbone JS.
[544.28 --> 546.62]  Uh, but we've also started to venture into iOS.
[546.62 --> 552.34]  And so we've hired on some iOS specific developers who are phenomenal at what they do.
[553.34 --> 557.68]  Um, so yeah, we're starting to take on more clients, uh, since we're a, uh,
[557.68 --> 561.06]  consultancy, um, that are iOS specific.
[561.48 --> 561.92]  Yeah.
[562.44 --> 564.86]  Let's, um, let's talk about bourbon.
[564.98 --> 566.08]  Let's talk about SAS.
[566.38 --> 571.20]  Um, I can't imagine anyone listening to the show that isn't at least a little familiar
[571.20 --> 571.82]  with bourbon.
[572.46 --> 577.46]  Um, definitely interested in and familiar with SAS because I think for a while there,
[577.46 --> 581.86]  we had a drinking contest on the show that every time we said SAS or compass or something
[581.86 --> 584.58]  like that, it was, uh, it was time to drink.
[584.58 --> 588.68]  Um, but, uh, and I don't do that anymore, obviously, but nonetheless.
[589.82 --> 595.48]  Um, so for those who may not know SAS bourbon, what is, you know, what's, what is SAS?
[595.88 --> 596.16]  Yeah.
[596.38 --> 605.26]  Well, SAS is a preprocessor that, um, sort of, uh, an, uh, level of abstraction on top of
[605.26 --> 605.80]  CSS.
[605.80 --> 612.30]  Um, so it allows you to do things that you wouldn't normally otherwise be able to do in
[612.30 --> 620.94]  CSS, like, um, nest declaration blocks, um, do, uh, loops, um, if statements, that sort
[620.94 --> 625.10]  of thing and compiles all out to standard CSS.
[626.48 --> 629.94]  And then, and then, uh, I guess bourbon on top of that is.
[630.10 --> 630.56]  Yeah.
[630.58 --> 635.32]  So bourbon on top of that is a SAS on crack or SAS on steroids or, you know, SAS.
[635.32 --> 636.52]  Supercharged.
[636.72 --> 637.14]  Yeah.
[637.26 --> 642.36]  You know, I see that like bourbon is something that really is like an API that helps, uh,
[642.42 --> 648.44]  designers and developers to be able to write their CSS faster and better.
[648.92 --> 656.12]  Um, specifically it started out mostly with, um, specifics for a vendor prefix properties
[656.12 --> 663.42]  for the different browsers like, um, Chrome, um, Opera, Mozilla, right.
[663.42 --> 665.10]  Uh, Firefox, that sort of thing.
[665.16 --> 669.24]  And so it was just a wrapper so that it, it made it so that you could write, um, just
[669.24 --> 673.74]  faster code and it would just output what you basically wanted it to for all those specific
[673.74 --> 674.10]  browsers.
[674.10 --> 678.04]  So you are like unencumbered by, um, the browser.
[678.50 --> 682.64]  Well, I guess even the staticness of CSS itself, right?
[682.64 --> 688.96]  Cause if you can loop through or, you know, do some programmatic like things in SAS, you
[688.96 --> 695.44]  can, you know, with one line, I guess maybe a crazy high powered mix in and one line of
[695.44 --> 699.62]  SAS, you can probably, you know, write a hundred plus lines of CSS.
[700.18 --> 700.98]  Yeah, absolutely.
[700.98 --> 706.46]  I've done some really cool stuff, um, with that, like, uh, just some really cool for
[706.46 --> 710.32]  loops that just run through and just generate like, uh, animations are pretty good for that.
[710.32 --> 718.26]  So like, if you want to, um, output, um, let's see, like an nth child that, that sort of
[718.26 --> 724.10]  animates or sorry, iterates through say 20 children and say, add a, add a duration to
[724.10 --> 726.88]  every increment, uh, child that increments up to.
[726.88 --> 731.12]  Um, so like the first one might get, um, animated in at like one second.
[731.22 --> 735.94]  Second one might animate in a, uh, two seconds, third one at three seconds, rather than having
[735.94 --> 741.02]  to write all those out, you can just wrap that into a nice loop in SAS and it, you know,
[741.02 --> 743.64]  stays really compact code and outputs what you're looking for.
[745.04 --> 750.54]  When we talk about bourbon, uh, I know that, uh, for those listening that are familiar with
[750.54 --> 755.38]  SAS, there's also, uh, maybe even you got introduced to SAS because of compass.
[755.38 --> 761.38]  So there's this, there's this, you know, other, I guess, mix in framework, uh, very similar
[761.38 --> 766.82]  to bourbon that kind of was, was the, even the inspiration, um, for bourbon.
[766.94 --> 772.54]  Some know SAS because of compass, um, for you, what was it that kind of got you into SAS?
[772.62 --> 776.06]  What was it that you got you excited to even attempt to do bourbon?
[776.36 --> 780.58]  Was it something that, uh, you know, it was a thought bought thing and you kind of took it
[780.58 --> 782.04]  over or where did this come from?
[782.04 --> 788.24]  Um, well, initially started when I first joined thought, uh, they, uh, they were using SAS
[788.24 --> 795.96]  on other projects and, uh, each of the designers that we had here, you know, we, um, like the
[795.96 --> 800.34]  way we structure our projects is that, um, each project gets one designer and there might
[800.34 --> 802.70]  be multiple projects going on at the same time at the company.
[802.70 --> 810.32]  But the problem with, um, that I, that I ran into was that I would write mix ins in SAS to
[810.32 --> 816.46]  do something like at the time, generate a border radius, um, for all the different, um, browsers.
[817.16 --> 819.68]  And, you know, I might call it border radius.
[819.94 --> 825.16]  Um, someone else, one, another designer might call it rounded corners that mix in.
[825.16 --> 830.50]  And so it became this is huge pain to, to jump on different projects and have consistent
[830.50 --> 838.56]  language, um, to, um, when you're writing the SAS to, you know, to, to call those different
[838.56 --> 839.00]  mix ins.
[839.10 --> 841.46]  And so I was like, this needs to be fixed.
[841.46 --> 848.06]  And so I released a gem with the help of, uh, thought bot, um, that basically took all
[848.06 --> 851.50]  those things that we are writing and using across all of our projects and wrapped it up
[851.50 --> 854.48]  into, um, one gem called bourbon.
[854.92 --> 860.26]  And so then we started using that and, you know, we had done, um, an exploration in compass,
[860.46 --> 861.82]  taking a look at that.
[862.06 --> 869.04]  Um, but unfortunately, you know, I think like it's, it's an awesome project and, um, the stuff
[869.04 --> 872.98]  that Chris has done with it is just phenomenal where he, you know, has built it to where it
[872.98 --> 874.38]  is to this, to this point.
[874.82 --> 879.68]  Um, but I know when I first, first tried using it, I ran into a ton of issues just trying to
[879.68 --> 880.38]  get it installed.
[880.38 --> 884.66]  Um, there was like a configuration file that I just kind of didn't want to have to deal
[884.66 --> 885.08]  with.
[885.48 --> 890.34]  Um, it was, it was kind of wrapped up in with a blueprint at the same time.
[890.94 --> 895.82]  And so it just felt like this big sort of cumbersome thing that I was throwing into my
[895.82 --> 900.66]  like nice, fresh, clean, lean project, um, that I was just getting started.
[900.66 --> 905.58]  And it just, it felt like it just did way too much than, than what I wanted it to do.
[905.58 --> 909.76]  And so I wanted something, I desired something just slim and just really easy, something that
[909.76 --> 910.78]  I could totally understand.
[910.78 --> 918.82]  And, um, took, you know, took the, um, kind of was opinionated in a way and said like,
[918.92 --> 922.08]  these are what, these are the defaults that you're going to want when you start this projects.
[922.54 --> 924.46]  So, um, take it and run with it.
[924.98 --> 925.34]  Yeah.
[925.36 --> 930.62]  This, um, so Bourbon was originally, uh, at least from what I understand, was originally championed
[930.62 --> 931.90]  by Chad Mazzola, right?
[931.90 --> 934.02]  And that was originally called SAS mix-ins.
[934.86 --> 939.92]  Uh, I mean, you know, I think that like, um, we were all sort of at the same time had
[939.92 --> 942.78]  our own, uh, mix-in libraries that we were using.
[943.44 --> 948.36]  And so I think it was under his like repo or something we were contributing into it.
[948.36 --> 955.42]  But then, um, you know, I think, yeah, I think it was just sort of under his repo that we sort
[955.42 --> 957.62]  of started and transferred it over to the Thoughtbot repo.
[957.88 --> 962.60]  But, um, yeah, I mean, his, his, uh, contribution to it were, were pretty huge.
[962.60 --> 969.40]  Like he did the, um, button mix-in, which is basically generates, you know, with one line
[969.40 --> 976.14]  of code, you can generate an entire, um, I don't know, probably like 50 line, uh, button,
[976.34 --> 978.74]  you know, like super quick.
[978.74 --> 981.00]  So it's, it's easy for like prototyping and stuff.
[981.94 --> 987.32]  So I guess on that note, then when we think about, um, not only SAS, when we think about
[987.32 --> 993.54]  what bourbon provides to someone who's using SAS to write their CSS, I know this is a lot
[993.54 --> 997.30]  of inceptions potentially here for some of the listeners, if you're not, if you're just
[997.30 --> 999.74]  catching up, but you know, what is the aim?
[999.80 --> 1000.98]  What is the purpose of bourbon?
[1001.04 --> 1003.66]  I know you said a unified API, but I don't know.
[1003.68 --> 1005.72]  You even said the, the button example there.
[1005.76 --> 1009.60]  Can you give another example of how, you know, what it makes, what makes sense to put something
[1009.60 --> 1010.62]  into bourbon?
[1010.74 --> 1014.98]  What, what gives it the ability to be part of the, part of the library?
[1015.40 --> 1015.52]  Yeah.
[1015.52 --> 1021.04]  Um, so there's sort of these principles that I have defined, uh, kind of loosely about,
[1021.04 --> 1025.54]  you know, what belongs in bourbon and what bourbon is and what it should be.
[1026.14 --> 1030.42]  Um, and you know, I think that it should be, you know, everything contained in bourbon should
[1030.42 --> 1034.76]  be as close to this, uh, actual CSS spec syntax as possible.
[1035.50 --> 1042.40]  Um, so when you're calling, um, when you create a mix in for something like, uh, a linear gradient,
[1042.60 --> 1045.50]  you know, we want to call it, we've got a, like,
[1045.52 --> 1051.00]  the way you define it in CSS, you'd do, you'd use the, um, background image property and then
[1051.00 --> 1053.94]  your value, you'd pass a linear gradient and then your colors.
[1054.26 --> 1060.42]  And so we've got this in bourbon, we've got this, um, uh, background image mix in,
[1060.54 --> 1062.96]  and that calls a linear gradient function.
[1062.96 --> 1064.52]  And in there you pass your colors.
[1064.52 --> 1067.66]  Um, same with something like, uh, transition mix in.
[1067.66 --> 1074.60]  In CSS, you traditionally have a transition, um, value and then you'd pass the, um, arguments
[1074.60 --> 1075.04]  to it.
[1075.16 --> 1076.14]  Same thing with bourbon.
[1076.22 --> 1079.40]  We want to call that, uh, same transition mix in.
[1080.44 --> 1086.14]  Um, and so another thing that I see, um, I want it to be pure SAS.
[1086.14 --> 1088.62]  So bourbon is a completely pure SAS library.
[1088.62 --> 1094.94]  And what that means is that you can, um, take bourbon, the project directory, and you can
[1094.94 --> 1101.22]  dump it into, um, any SAS project and it's going to work, um, without any hitch.
[1101.48 --> 1106.66]  So it's not tied into Ruby, which something like compass is tied to Ruby.
[1106.66 --> 1115.32]  Um, cause it has all these external functions and, um, directives that, uh, use Ruby, um,
[1115.32 --> 1117.76]  to compile to like output the CSS.
[1118.94 --> 1126.28]  So rather than just using straight SAS, it makes it a little bit less, I guess, um, I guess
[1126.28 --> 1128.04]  fluid to, to not have any issues.
[1128.04 --> 1132.46]  I mean, I have to say myself, I've been using bourbon as well as need on a, on a project
[1132.46 --> 1136.22]  recently, but, uh, sadly I haven't gotten deep enough into the design yet of that project
[1136.22 --> 1139.14]  to really appreciate and enjoy the things about bourbon.
[1139.26 --> 1144.14]  So that's, was perfect for this call just to kind of get the, the lay of the land from
[1144.14 --> 1144.82]  the maker himself.
[1144.82 --> 1148.12]  But, uh, what I did notice was that there was no issues.
[1148.32 --> 1150.94]  Um, it's a rails project, asset pipeline, the whole deal.
[1151.02 --> 1155.14]  And there's been issues in the past, which I haven't been closely following.
[1155.14 --> 1157.62]  So if these issues are non-issues now, then I apologize.
[1157.86 --> 1162.68]  But, you know, there had been in the past issues with getting compass going with asset pipeline.
[1162.76 --> 1165.82]  They were trying to do some of the things, same things and different stuff like that.
[1165.82 --> 1170.74]  But what I noticed with bourbon was that, you know, your, your read me install directions
[1170.74 --> 1177.20]  were simple, you know, just add the gym, a bundle install and pretty much good to go.
[1177.38 --> 1178.66]  No issues with getting started at all.
[1179.06 --> 1179.16]  Yeah.
[1179.22 --> 1182.66]  I mean, that's the cool thing about having a mixing library is that it's just pure SAS.
[1182.66 --> 1185.54]  So like anywhere SAS works, bourbon's ready to go.
[1186.74 --> 1189.98]  And so it makes it platform agnostic as well.
[1189.98 --> 1196.06]  So like for something like, um, so the creator of SAS, uh, Hampton Catlin.
[1196.26 --> 1196.92]  Yeah.
[1197.06 --> 1205.48]  So he, um, and, uh, Aaron, uh, loong just created, um, this recent project called SAS C.
[1205.86 --> 1207.18]  Have you heard about this?
[1207.70 --> 1208.74]  I sure have.
[1208.78 --> 1208.98]  Yeah.
[1209.28 --> 1209.54]  Okay.
[1209.54 --> 1219.20]  So SAS C is basically, um, a lib SAS wrapper, uh, that compiles, um, like SAS using C plus plus.
[1220.40 --> 1224.88]  Um, and so this is good for, for people who either don't have Ruby or just want to use,
[1224.88 --> 1228.28]  um, like SAS on a C plus plus project.
[1228.82 --> 1234.66]  Um, and so you can, you can install that and optionally install your, uh, uh, or compile your,
[1234.66 --> 1238.80]  your, um, SAS files using the SAS C library.
[1238.80 --> 1242.92]  But it's cool that like you can take bourbon and you don't have to, it's not like you have
[1242.92 --> 1246.96]  to port it because things are written in a, you know, a language like Ruby.
[1246.96 --> 1249.04]  It's like, it's just anywhere SAS works.
[1249.34 --> 1250.22]  So does bourbon.
[1251.42 --> 1251.78]  Yeah.
[1251.78 --> 1252.94]  I never really thought about that.
[1252.98 --> 1257.92]  I mean, I guess that was one of the original things because if we rewind back a bit, the
[1257.92 --> 1258.98]  change has been around for a while.
[1258.98 --> 1264.14]  We've been around since 2009 and I was pretty excited about, um, this project.
[1264.14 --> 1267.22]  And I think I even wrote a, like a pretty lengthy article on it.
[1267.22 --> 1268.88]  I'll put it in the show notes back.
[1270.86 --> 1274.70]  Looks like July 7th of 2011 was a couple of days after you guys first released this.
[1274.74 --> 1277.46]  And it was pretty lengthy about, you know, what you guys are doing and what's up with
[1277.46 --> 1277.56]  it.
[1277.56 --> 1286.18]  But at the time I really didn't quite capture the, the necessity, I guess, or the, this
[1286.18 --> 1290.08]  being a feature, I guess, of bourbon that no matter where SAS works, it works.
[1290.08 --> 1290.68]  Mm-hmm.
[1290.72 --> 1295.76]  I guess because I was, I was so tied to, um, what compass had done.
[1295.82 --> 1297.64]  I was really excited about some other things it was doing.
[1297.84 --> 1302.18]  I think even things that Bauer, um, now does Twitter's Bauer.
[1302.28 --> 1302.84]  Are you familiar with that?
[1302.88 --> 1306.50]  It's kind of like, uh, uh, a package manager for the web in general.
[1306.72 --> 1309.08]  Uh, sort of, I've kind of briefly checked it out.
[1309.08 --> 1314.10]  Kind of like carcoculting HTML, CSS, and JavaScript around and being able to easily put it into
[1314.10 --> 1315.16]  a project.
[1315.28 --> 1318.04]  In this case, in Bauer's case, it's, you know, get powered.
[1318.14 --> 1321.06]  So it's super powerful just to put it in a repo.
[1321.54 --> 1324.82]  Um, and then, you know, suck it into your project and whichever way.
[1324.90 --> 1327.32]  But I was kind of excited about these other features that compass had.
[1327.32 --> 1334.16]  And I feel like, um, compass was really great for a lot of things, but, uh, but this one
[1334.16 --> 1339.24]  downfall of kind of like having to have Ruby and that's kind of the starting issue for a
[1339.24 --> 1340.32]  lot of people using SAS.
[1340.48 --> 1345.22]  So I guess as a designer, when you talk to other designers that, you know, they're like, you
[1345.22 --> 1348.74]  know, Hey, Phil, I want to get into what you're doing more or, you know, how do I get started
[1348.74 --> 1348.96]  here?
[1348.96 --> 1352.88]  Like one of the biggest hurdles is, you know, how do I use SAS?
[1352.98 --> 1354.46]  How do I use that in general?
[1354.46 --> 1359.38]  How do I get set up and, um, just, it doesn't really help, you know, bourbon doesn't really
[1359.38 --> 1363.46]  help getting started with SAS easier, but it makes it a lot easier to get involved with
[1363.46 --> 1368.38]  a mix in library because of its focus on being SAS purists.
[1369.02 --> 1369.70]  Yeah, exactly.
[1370.48 --> 1376.42]  Um, and I think there's, you know, people have come out with, um, like GUI wrappers that
[1376.42 --> 1377.46]  compile SAS.
[1377.76 --> 1383.32]  Um, some of the big names are, uh, code kit, uh, hammer for Mac.
[1383.44 --> 1383.64]  Yeah.
[1383.64 --> 1388.08]  Um, so it's been like, it's a pretty cool projects too, for anybody out there listening
[1388.08 --> 1389.52]  those hammer.
[1389.72 --> 1391.04]  I just recently checked out.
[1391.16 --> 1394.34]  I've known about code kit for a while and there's one other one I think that is on your
[1394.34 --> 1396.20]  list of ones you support.
[1396.28 --> 1397.62]  I can't recall the name of it though.
[1397.98 --> 1399.12]  Uh, there is.
[1399.12 --> 1402.10]  And that one is, um, live reload.
[1402.66 --> 1403.26]  Live reload.
[1403.32 --> 1403.94]  Yes, of course.
[1404.00 --> 1404.20]  Yeah.
[1404.40 --> 1404.62]  Yep.
[1405.54 --> 1405.76]  Yeah.
[1405.76 --> 1406.86]  So, so those are great.
[1406.86 --> 1412.16]  And bourbon is, is, uh, integrated into all those projects, but you know, it's, it was
[1412.16 --> 1417.78]  easy for me to work with the developers, um, to get that implemented because it's not like
[1417.78 --> 1423.36]  there was any executables that needed to be run because it, you know, they all compile
[1423.36 --> 1423.80]  SAS.
[1424.00 --> 1429.06]  So they just were able to throw bourbon really in there and it was able to, it was good to
[1429.06 --> 1429.30]  go.
[1429.30 --> 1438.32]  So this might be a, a somewhat of a flame war of a topic, but I'm just kind of curious.
[1438.74 --> 1444.12]  Um, you've been using SAS long enough to know that there's been two different syntaxes.
[1444.12 --> 1451.82]  I'm just curious for those who are still kind of hanging out in the SAS SAS world and not
[1451.82 --> 1453.22]  the S CSS world.
[1453.22 --> 1456.48]  And I'm not even sure if you call it SAS ECSS or SCSS.
[1456.88 --> 1461.58]  And next thing you know, you're tongue twisting and nobody's talking about, but, um, you know,
[1461.66 --> 1465.18]  what are your thoughts on just that, uh, SAS versus SCSS?
[1466.28 --> 1469.32]  Um, you know, what do you say to people when they're like, oh, I'm still using the old way.
[1469.86 --> 1470.02]  Yeah.
[1470.84 --> 1475.38]  Um, so we use, uh, the SCSS syntax.
[1475.82 --> 1480.00]  And so that's the more verbose, um, curly brackets, all that kind of thing.
[1480.00 --> 1487.62]  Um, so I was recently, recently talking to, um, Rita Lambden, who's a designer here at
[1487.62 --> 1496.00]  Thoughtbot and he came up with this, uh, great idea of trying to use the SAS syntax for, um,
[1496.42 --> 1499.14]  working on things like neat or bourbon.
[1499.66 --> 1503.02]  Um, neat is our grid framework that sort of ties in with bourbon.
[1503.78 --> 1509.98]  Um, so, so when we work on client projects, we're writing actual CSS that like outplayed,
[1510.00 --> 1516.30]  outputs, I think that's where SCSS really shines is because then you get, you know, the,
[1516.30 --> 1523.62]  the traditional, um, uh, logical, uh, hierarchy of things using the curly brackets and, um,
[1523.62 --> 1525.10]  the colons and all that sort of thing.
[1525.60 --> 1530.46]  But when it comes to when you're actually doing like what I would call programming in SAS,
[1530.66 --> 1537.06]  I think that's where, um, S, uh, SAS can actually really be useful.
[1537.06 --> 1542.26]  So if you think of something like, um, if you think of in comparison of CoffeeScript to
[1542.26 --> 1543.62]  JavaScript, right.
[1543.96 --> 1549.76]  I love CoffeeScript because it just takes away a lot of that like pain of, um, you know,
[1549.82 --> 1553.14]  opening, closing curly brackets and all that.
[1553.14 --> 1556.94]  So I would sort of put it in, in those, in that sort of perspective.
[1556.94 --> 1563.40]  Um, but I, I will say that I actually haven't tried to use, uh, SAS, uh, in bourbon yet,
[1563.40 --> 1567.64]  but I think that's something that I would love to try in the future and see if that actually
[1567.64 --> 1570.50]  works out as we've sort of hypothesized.
[1571.64 --> 1577.10]  So what you're saying is, is you kind of got one little toe into the proverbial SAS pool.
[1578.94 --> 1579.76]  Yeah, exactly.
[1579.76 --> 1583.00]  I was, I'm surprised to hear that.
[1583.10 --> 1588.40]  Honestly, I thought you would be a lot more pro SCSS and not, not to say that you're not,
[1588.50 --> 1593.68]  but just, I kind of expected this, uh, um, you know, kind of stern opinion.
[1593.92 --> 1600.46]  Well, I mean, like I, I think if I'm writing CSS, that's going to output, um, you know,
[1600.52 --> 1608.04]  just like your CSS would, I think SCSS, I prefer to use that, but in the same way that I love
[1608.04 --> 1614.78]  CoffeeScript, I could, and, and if you look at, um, oh God, in bourbon, there's like the
[1614.78 --> 1619.94]  linear gradient mix in, there's some mix ins that are just so insanely huge, right?
[1620.24 --> 1622.36]  Kind of like, it's so hard to follow.
[1622.36 --> 1628.58]  And so I could totally imagine myself writing, using SAS to just basically, you know, do all
[1628.58 --> 1633.62]  the logic and all that kind of stuff in a much more concise and clear manner.
[1633.62 --> 1638.94]  Um, I'm going to your source code now to pull that up. Cause you're, you're absolutely right.
[1638.96 --> 1644.68]  I mean, in this case I can see, yeah, I, and I think I've done this too in my past where I've
[1644.68 --> 1647.72]  kind of teetered in the line of, and you know, I don't want to spend a ton of time on this.
[1647.72 --> 1651.26]  Cause I mean, I think that people talk about this quite a bit and it's been discussed on the
[1651.26 --> 1655.88]  SAS way. It's been discussed on other blogs and I don't want to bring up the can of worms again.
[1655.94 --> 1660.48]  This is not the intention. I just kind of wanted to get your opinion on, um, you know,
[1660.48 --> 1664.34]  for those who are still hanging out in what might be considered the old world. Cause if
[1664.34 --> 1669.30]  you talk to Hampton, you know, he's not really, he's not really for, if I recall correctly,
[1669.44 --> 1674.50]  sorry, Hampton, if I'm wrong, but I'm pretty sure that he's kind of against the older SAS
[1674.50 --> 1679.10]  way and kind of focusing on one syntax and that way the community isn't fractured and there's
[1679.10 --> 1682.86]  not two ways to do things. And, you know, it makes it a little easier to, you know, provide
[1682.86 --> 1685.44]  long-term support and so on and so forth.
[1685.44 --> 1688.66]  Right. Do you, are they like planning on killing the old?
[1689.42 --> 1695.40]  No, no. As Nathan, Nathan Weisenbaum, one of the, uh, he took over the maintaining of
[1695.40 --> 1702.08]  SAS when Hampton, um, I think when Hampton went to Wikipedia and had less time to be involved,
[1702.16 --> 1707.20]  I'm pretty sure that, uh, Nathan took over Chris, uh, kind of co-piloted with Nathan and
[1707.20 --> 1711.82]  they've committed to not deprecating the old syntax. And I know it's here, here to say,
[1711.82 --> 1718.70]  but I just know that there's differing opinions, you know, Nathan is the, uh, done a fantastic
[1718.70 --> 1722.84]  job with SAS and has done a great job leading it and maintaining it and, and progressing over
[1722.84 --> 1728.82]  the years. But, you know, the inventor, uh, Hampton and him have differing opinions from
[1728.82 --> 1733.18]  what I understand on some things. And that's going to happen. Like creative developers.
[1733.18 --> 1735.94]  I mean, you're kidding me. And you're going to have some different opinions. It's going to
[1735.94 --> 1736.34]  happen.
[1736.34 --> 1741.88]  Yeah. So, yeah, I'd be curious to see what, uh, to hear what, uh, Rita Lamden says,
[1741.96 --> 1747.68]  cause he's working on neat and his, one of his goals for launching neat 2.0 was to actually convert
[1747.68 --> 1756.80]  neat to use entirely the, uh, S, uh, SAS syntax. So I don't know. I'd like to try it out too and,
[1756.80 --> 1761.10]  and see kind of what the pros and cons are. Admittedly, I haven't really used that syntax.
[1761.66 --> 1764.30]  Um, I've just been sticking to SCSS for a while.
[1764.30 --> 1771.02]  And so you mentioned the linear gradient, uh, which is if you're looking at the, by any chance,
[1771.02 --> 1777.18]  if you're listening to this live or, um, or on the podcast feed, you can go to, uh, github.com
[1777.18 --> 1783.42]  slash thoughtbot slash bourbon, uh, dive into the asset style sheet, CSS three folder. There's a linear
[1783.42 --> 1790.74]  gradients, uh, sorry, a linear gradient, uh, partial there that is, you know, quite programmatic too.
[1790.74 --> 1795.74]  I mean, so we're coming from the world, you know, we, we opened up the call by saying that you're,
[1795.74 --> 1802.22]  um, you know, a designer primarily, but you're also kind of getting into hacking and stuff like that.
[1802.26 --> 1805.56]  And you have been over the past years and why wouldn't you, your work at thoughtbot. So you,
[1805.56 --> 1810.44]  you definitely have to put your hacker hat on at some point, um, to, to truly thrive there and do,
[1810.54 --> 1816.60]  and have fun too. Right. But, um, one thing that for me with SAS, whenever I started to,
[1816.60 --> 1821.68]  to do a lot more with it, so if you're coming from the CSS world where it's static, you know,
[1821.72 --> 1825.80]  what you type is what you get basically. And then you come to the SAS world, whether,
[1826.04 --> 1830.02]  regardless of syntax, it, the functions are all still the same. You still have access to all the
[1830.02 --> 1836.56]  same SAS functions and APIs and, you know, different, uh, different abilities. Uh, but one thing was
[1836.56 --> 1840.36]  pretty cool was like, you know, you can start to use variables, right. And you can start to do,
[1840.36 --> 1847.24]  um, things like returning values. Like for example, in line, uh, line 10 of this particular file we're
[1847.24 --> 1852.38]  talking about, you have type of in there, right. And you can kind of determine what you pass into
[1852.38 --> 1856.72]  it as an argument. What comes back, you can determine if it's a list or if it's a color,
[1856.84 --> 1861.00]  if it's a color with pixels, you know, all these different things is like pretty cool. So all that
[1861.00 --> 1865.98]  to say is, uh, is that it seems like, you know, if you get into SAS and you really kind of dig in and
[1865.98 --> 1869.88]  really have fun with it, that you can learn if you're not a programmer, you can kind of learn some of the
[1869.88 --> 1876.26]  programming basics by, by using it and, you know, enjoying it. Yeah. That's one thing where,
[1876.26 --> 1882.46]  you know, I started, uh, you know, working on bourbon. I don't think I realized the like impact
[1882.46 --> 1890.34]  that it would have on my, I guess the outcome of like hacking on this and just how much I learned
[1890.34 --> 1896.32]  and what that translated into my learning of programming. Um, just deep diving right into the
[1896.32 --> 1903.78]  SAS documentation and, you know, learning about interpolation and type of, and, um, and then just
[1903.78 --> 1909.14]  all these different things and creating different functions. Um, it just really like gave me a much
[1909.14 --> 1916.82]  better understanding of these basics of programming. Um, and what that turned into is now I've started to,
[1916.82 --> 1922.24]  uh, learn coffee script and, and learn coffee script pretty well. Um, and so now, you know,
[1922.24 --> 1927.30]  I'm kind of working on a hacking on my own side project right now. That's completely, um, written
[1927.30 --> 1932.96]  in coffee script. It's actually using meteor JS, which I know you're talking to, uh, such a grief
[1932.96 --> 1940.14]  just a few weeks ago, um, about, and, you know, I absolutely love meteor, but like just from the past,
[1940.18 --> 1946.10]  like two years, two years, yeah, maybe two years working on bourbon. It's like, I think helped me grow
[1946.10 --> 1953.48]  to the point where I can work entirely on a meteor project because of like the basics that I've learned
[1953.48 --> 1959.56]  from SAS. Yeah, absolutely. I mean, uh, conditionals, I mean, that's like the, you know, programming
[1959.56 --> 1965.50]  one-on-one is if this, then, you know, those, those types of things and confirming if a value is true
[1965.50 --> 1971.16]  or false or all these different things. I mean, that's, that's pretty wild. And one of the, I think
[1971.16 --> 1976.08]  one of not so much the most complex mixing inside of bourbon to kind of key off of some of this
[1976.08 --> 1982.96]  conversation, but, um, one of them is the, uh, is the add-on for position. And I mean, like even
[1982.96 --> 1988.92]  that one there is of, I mean, if you think about position in CSS, it's, it's not a really complex,
[1988.92 --> 1993.74]  um, you know, property and value. It's, it's pretty cut and dry, right? It's either position
[1993.74 --> 1999.80]  relative, absolute fixed, and you've got some, you know, places it can be, for example, on the page
[1999.80 --> 2005.78]  and whatnot. But this particular mix in, in SAS, well, the SES, SES system fix is, uh,
[2006.22 --> 2013.38]  is 42 lines. I mean, it's like you said earlier that, um, the S CSS syntax kind of makes it a bit
[2013.38 --> 2017.52]  more verbose, but it's a little easier to read in this case. But nonetheless, I mean, you have a pretty
[2017.52 --> 2024.16]  simple thing in CSS to do, but you've got this 42 line mix in that uses type of, and, you know,
[2024.20 --> 2030.50]  uses the list. And, you know, you're confirming if, if, uh, what you passed into position, if it's a list
[2030.50 --> 2035.38]  or not, and, and, you know, kind of, uh, returning the thing way early on and you're doing things
[2035.38 --> 2041.98]  with top and nth. And that's a really pretty neat thing. Like, so if you're just a CSS, uh, hacker
[2041.98 --> 2046.24]  and you're doing it really well and you're picking up SAS and you're kind of getting into it, this is a
[2046.24 --> 2052.18]  particularly cool mix in, I would say to, to like learn all the different things that are in SAS that
[2052.18 --> 2058.68]  happen in this mix in. Yeah. I would say one of the, like the, probably the most advanced mix in
[2058.68 --> 2064.50]  is probably the, uh, background and background image mix in because those have to take the linear
[2064.50 --> 2072.04]  gradient and radial gradient functions. But with recent changes that happened to, um, the spec of
[2072.04 --> 2079.06]  linear and radial gradients, you'll know that the position changed. So like if you used to call,
[2079.06 --> 2086.84]  uh, let's, if you used to call top comma, um, red comma orange, that would be a, a gradient that went
[2086.84 --> 2094.18]  from the top to the bottom, um, vertically red to orange. But then in, in the spec just recently
[2094.18 --> 2103.30]  changed to, you have to add two to the position. So now two top, uh, red orange, and they also flipped
[2103.30 --> 2110.00]  the way the browser renders that or S or something, there was something a little, uh, wishy-washy about
[2110.00 --> 2114.88]  that. So I think, I think that was the case where they flipped the actual gradient or something. Um,
[2114.88 --> 2120.56]  and so I had to figure out in order to, in order to keep backwards compatibility, I had to figure out
[2120.56 --> 2127.90]  the position. I had to flip the position for the like new browser. Um, and still like when you,
[2127.90 --> 2132.84]  when you give a gradient, you can also give it color stops. Um, so there's actually a lot going
[2132.84 --> 2139.08]  on in something like the, uh, background image mix in where I call external functions. And so on
[2139.08 --> 2145.12]  line 31, you'll see gradient position parser. Well, that's going to parse the actual position to be,
[2145.22 --> 2151.66]  you know, is it top? Is it bottom? If it is top, flip it to bottom. Um, and then things like render
[2151.66 --> 2157.62]  gradients. And so that's passing in all those things and passing the vendors. And basically,
[2157.62 --> 2161.76]  it's like all these different files that it's sort of passing these arguments to,
[2161.86 --> 2168.56]  and it's returning back and it's just basically compiling the like gradients. And I, you know,
[2168.62 --> 2174.26]  it's just like, it's kind of crazy to see this like, uh, programming in SAS because you wouldn't
[2174.26 --> 2179.80]  really expect like all the, like this to be possible to do this in something that's not a
[2179.80 --> 2186.18]  programming language. Right. It's, you know, you're mentioned too, of the, of the spec changing
[2186.18 --> 2194.10]  and how you'd mentioned earlier, you know, what bourbon is to SAS basically is this common API to,
[2194.10 --> 2199.68]  you know, CSS that you're going to actually end up not having to write because it, you know,
[2199.72 --> 2203.14]  SAS is basically outputting it for you. But, you know, what you just mentioned there though,
[2203.14 --> 2209.76]  is a really good reason to use SAS and specifically use, uh, bourbon or even compass in this case,
[2209.76 --> 2214.94]  you know, to, to not have to go back. And I mean, imagine if you had to go back to all your projects
[2214.94 --> 2219.90]  and, you know, update that thing. But if all you had to do was install the latest version of bourbon,
[2220.28 --> 2224.46]  keep calling the same, the same, you know, the function with the same amount of arguments or
[2224.46 --> 2229.00]  whatever. And somehow with inside of bourbon, inside those functions, you handled that for
[2229.00 --> 2235.22]  them. I mean, you kind of maintain forward compatibility with a little bit, uh, a little bit less work
[2235.22 --> 2239.78]  and I guess a lot more time on your hands. Yeah, absolutely. I think that's one of the,
[2239.78 --> 2246.64]  the benefits of something like bourbon is when you, you sort of like outsource your, um, vendor
[2246.64 --> 2252.70]  prefixes and stuff. It's like, you know, people, you no longer have to worry about, you know, keeping
[2252.70 --> 2257.98]  that code up to date when specs change, because I'm going to take care of that for you.
[2259.02 --> 2263.82]  You know, like all you have to do is update bourbon and it's just, you know, as it should,
[2263.82 --> 2268.70]  it should output the latest spec and the backwards compatibility as the way that you
[2268.70 --> 2271.28]  initially put it in maybe a year ago. Yeah.
[2275.34 --> 2280.62]  I guess since we're keying off this a little bit further, what, what are some of the biggest
[2280.62 --> 2284.32]  things? I mean, we touched on a little bit, but I'm kind of curious to a more specific answer,
[2284.40 --> 2289.08]  but what are some of the biggest things you've learned with creating as well as maintaining
[2289.08 --> 2293.28]  bourbon? Not so much just in, you know, about SAS or CSS,
[2293.82 --> 2298.56]  but just kind of in general as a, as a person who makes things on the web.
[2299.00 --> 2304.70]  Yeah. Um, I think open source stuff is in touching upon what we talked about a little
[2304.70 --> 2311.40]  bit about earlier is that it's kind of a pain in the ass to maintain. Um, just because there's,
[2311.58 --> 2315.00]  there's always pull requests and there's always issues and it's finding time to get around to it.
[2315.00 --> 2322.76]  And, um, who was it that did that talk? Um, was it fat that that was like, yeah, just that sort of,
[2322.76 --> 2328.70]  um, why do I hate open source or it was some, some kind of title like that. And, you know,
[2328.70 --> 2335.00]  after maintaining this for two years, it's, it's a lot of work, but it's like the rewards are
[2335.00 --> 2340.72]  beneficial to have a project that like, like when I install bourbon on a new project, I'm like,
[2340.72 --> 2344.64]  this is just the way that it should work. Like, I'm so happy that I created this and that I don't
[2344.64 --> 2349.54]  have to worry about all this other extraneous stuff that traditionally we did have to handle
[2349.54 --> 2355.68]  a few years ago. Um, so, I mean, it's nice. And, and plus like having the community be able to
[2355.68 --> 2362.02]  contribute to it and make suggestions and bring up issues. It's, it's, you know, extremely helpful
[2362.02 --> 2366.74]  because it might, they might not be issues that I would run across. So, so it's awesome to have the
[2366.74 --> 2372.68]  community there and helping, but it's also like, oh man, like there's just so much going on that
[2372.68 --> 2376.86]  sometimes I don't have time to get to the pull requests or issues as soon as I would like to.
[2379.10 --> 2383.62]  So you touched on sustaining open source there. I mean, that's not exactly what you said,
[2383.66 --> 2387.68]  but it's this topic that's kind of, like I said, trending on the changelog at least. And
[2387.68 --> 2393.32]  we've definitely talked about, I think every show since we've relaunched the show, um, I don't know
[2393.32 --> 2398.30]  if you know, but we had this little hiatus tail into last year. Uh, relaunched the blog in January
[2398.30 --> 2404.34]  and relaunched the show, I believe in April, I think it was. Um, we had this little hiatus, so we
[2404.34 --> 2410.08]  definitely aren't back, but nonetheless. Yeah. Um, um, it's good to have you back. Yeah. Thank you. I
[2410.08 --> 2413.36]  mean, we, we've really enjoyed doing this show and you know, it's fun having these kinds of
[2413.36 --> 2418.94]  conversations with you and others to, I mean, cause I think that people think this and maybe other
[2418.94 --> 2424.00]  podcasts cover this, I don't know, but, um, it's nice to hear the benefits and rewards,
[2424.00 --> 2429.76]  uh, of open source, even though, like you said, like a better term, it's a pain in the ass. It
[2429.76 --> 2436.70]  can be sometimes, you know? Yeah. I always love the times when people like tweet at me or, you know,
[2436.76 --> 2441.80]  tweet like, Oh, I'm like love bourbon justice covered it. It's just helped my process so much.
[2442.08 --> 2446.52]  Those are like inspirational and, and things that sort of keep me going on this project
[2446.52 --> 2451.84]  is to hear people's successes with it. And when people use it on their, you know, new projects,
[2451.84 --> 2459.76]  like it feels good. It feels like this is a valuable, um, like my time is valuable here and
[2459.76 --> 2465.98]  people are, are getting use out of it. So cool. Yeah. So it's going to work on. So if you're
[2465.98 --> 2471.84]  listening to this live or on the podcast at this very moment, go to Twitter, tweet at Phil
[2471.84 --> 2477.72]  LaPierre. Um, we'll have it in the show notes if you can't spell it, but, uh, um, I can spell
[2477.72 --> 2481.92]  it. Nope. No problem. But, uh, tweeted him and if you're using bourbon and you love it,
[2482.18 --> 2487.64]  tell him right away, cause that's going to give him such motivation. So, um, but so talking
[2487.64 --> 2491.76]  on sustaining open source, uh, it says the bottom bourbon is maintained and funded by
[2491.76 --> 2496.80]  thoughtbot Inc. We talked about, uh, you know, thoughtbot Fridays, open source Fridays, and the
[2496.80 --> 2503.52]  fact that you guys are committing to that. Um, uh, I guess what do you think is happening
[2503.52 --> 2508.82]  in helping sustain open source? So your, your company helps, um, helps you by paying for your
[2508.82 --> 2513.48]  time. What do you think are other creative ways that you see open source being sustained
[2513.48 --> 2519.04]  since you're familiar with fat and his conversation around how, why he hates open source or whatever
[2519.04 --> 2522.66]  his topic was? I can't recall the title either, but pretty cool, pretty cool talk.
[2522.66 --> 2528.02]  I, you know, I think a lot of these things are coming out of, um, projects that people
[2528.02 --> 2533.00]  like products that people are working on. So even if someone's company doesn't pay them
[2533.00 --> 2537.42]  to work on open source, it's like, if you are working on a product at your company and
[2537.42 --> 2542.58]  you find something that you can extract out something that other people use, I think that's
[2542.58 --> 2546.72]  where we can, you know, that's where a lot of this open source tools are coming from these
[2546.72 --> 2550.66]  days and can be maintained because as long as you're keep sort of updating your project
[2550.66 --> 2554.54]  and, you know, keep developing whatever open source tool it is that you've created.
[2554.76 --> 2559.78]  I think that's where we can see a lot of great stuff, um, coming to the open source community.
[2561.06 --> 2567.18]  Um, and I see, um, it looks, I think I saw recently that, uh, Chris Epstein got a job at LinkedIn
[2567.18 --> 2571.50]  and he's going to be working on a SAS like entirely.
[2572.78 --> 2576.24]  I would mean to catch up with him cause I've, I've kind of been in my own little hole, but,
[2576.24 --> 2581.28]  and considering, you know, uh, I run the change log, I should be a bit more up to date on some
[2581.28 --> 2585.88]  of these things, but that's, I knew he went to LinkedIn, but I didn't know that they were giving
[2585.88 --> 2590.44]  him freedom to do a lot more of SAS and compass. Yeah. I think it's a lot of, I think he's going
[2590.44 --> 2596.90]  to be working on SAS, uh, entirely. I mean, correct me if I'm wrong, Chris, but I think that's just
[2596.90 --> 2604.44]  phenomenal because, you know, SAS is sort of like this, uh, amazing tool that the industry is adopting
[2604.44 --> 2611.28]  and continues to adopt. And it's just really think changing the way that we, we write CSS and
[2611.28 --> 2617.96]  architect our projects and share code. It's really phenomenal. So kudos to him for, for, uh,
[2617.96 --> 2620.64]  for, for keeping up on top of SAS.
[2620.84 --> 2626.40]  And he is, he is such the right person to, I mean, together with Nathan, of course, but I mean,
[2627.10 --> 2633.54]  Chris is so smart. I mean, uh, talk circles around me when it comes to just CSS architectures,
[2633.54 --> 2637.82]  you know, not, not SAS itself. Cause I mean, that's a means to an end. I mean, it's a good
[2637.82 --> 2643.02]  means to an end obviously, but at the end of the day, SAS compiles down to CSS. So it's not like
[2643.02 --> 2649.44]  anybody who's got their, their SAS jerk hat on, for example, like I, I know, uh, on the SAS way,
[2649.64 --> 2655.96]  a good friend of mine, um, Canary Mason is what he used to be on, um, on Twitter, but I think now he
[2655.96 --> 2662.90]  goes by coding designer. Um, his name's Mason. He wrote a blog post about being a SAS jerk cause he's just so
[2662.90 --> 2666.52]  excited about SAS and he wants to tell everybody about SAS. Right. It's like, you know, this thing
[2666.52 --> 2671.32]  has changed my life. And he's like, you know, I just realized I was a SAS jerk. It's a talk. It's a
[2671.32 --> 2677.98]  little topic on there, but you know, Chris is, um, you know, we get so passionate about it, but Chris
[2677.98 --> 2683.24]  is, is a super smart, uh, when it comes to all this stuff. But at the end, like I said, in the end of
[2683.24 --> 2688.68]  the day, it does just come bow down to CSS. So we're still writing and still touting the
[2688.68 --> 2693.12]  awesomeness of CSS. We're just making it a little easier to get there faster. And like you said
[2693.12 --> 2698.84]  earlier with a more consistent API to project from project to project and getting started a lot
[2698.84 --> 2703.94]  easier. Like, like I said earlier with my project, it was so easy to get, uh, uh, to get bourbon in
[2703.94 --> 2708.28]  place. It was just way too easy, you know? I mean, maybe not way too easy, but definitely good.
[2708.68 --> 2712.46]  Yep. Let's talk about, uh, if you don't mind, I want to talk about one more thing around
[2712.46 --> 2717.00]  what you've done in, uh, in bourbon that may go a little unnoticed, but it's kind of neat,
[2717.00 --> 2722.70]  at least from what I saw of it was that, uh, not only did you provide this, um, you know,
[2722.78 --> 2727.78]  this SAS mixing library called bourbon, but if you install it as a, as a Ruby gem and not just
[2727.78 --> 2733.94]  move the SAS into your project, um, you kind of get access to, uh, these command line tools and
[2733.94 --> 2739.74]  they're powered by Thor and, you know, kind of diving it a bit more to open source and just being,
[2740.16 --> 2743.80]  you know, coming from the design side to the developer side and kind of straddling that,
[2743.80 --> 2748.06]  straddling that line a bit more, I thought it was pretty neat how you guys use Thor.
[2748.48 --> 2753.62]  I guess it's pretty rudimentary to do it, but, uh, for, you know, other hackers, but it's really
[2753.62 --> 2758.96]  cool how you can like do, you know, bourbon install and it runs a Thor script. And for those who don't
[2758.96 --> 2765.16]  know about Thor, um, you, you, who the cats wrote this thing, I guess kind of accidentally. Um, and
[2765.16 --> 2768.94]  then, and then it kind of became this thing and I've loved Thor. You've probably heard Wynn say it on
[2768.94 --> 2772.96]  past shows. If you're a long time listener of the changelog that, you know, I was always stoked
[2772.96 --> 2778.06]  by Thor. I thought it was pretty cool. It's like, it's like rake, uh, but it's not rake, it's Thor.
[2778.60 --> 2782.82]  So it's straight Ruby, but you're doing some really cool copying and stuff. And you're also
[2782.82 --> 2786.74]  providing, uh, some command line there. What, what part did you play? And like,
[2786.74 --> 2795.42]  I guess just introducing that to bourbon. Uh, the part I think I played was, um, there was a thorn in my
[2795.42 --> 2800.96]  side of, I have to copy and paste this project to every single, this, you know, this folder to
[2800.96 --> 2806.86]  every single project that I want developers help. And so that's when Mike Burns really came to my
[2806.86 --> 2812.90]  rescue. And, uh, you know, I sort of said, this is what I want out of bourbon. This is what I wanted
[2812.90 --> 2818.22]  to do to make it easy so that you can update bourbon and install it really easy from the command line.
[2818.96 --> 2824.64]  And Mike Burns, the rescue comes out and, uh, you know, writes Thor and, or, you know, the,
[2824.64 --> 2831.38]  the script that, that runs the Thor. So yeah, the file we're mentioning, uh, he's talking about.
[2831.38 --> 2835.98]  So Mike Burns, I think I actually met Mike, uh, when I met Chad at, uh, Lone Star RubyConf a couple
[2835.98 --> 2841.78]  of years ago, but, uh, the file, it might be a little bit melodramatic to, or not melodramatic,
[2841.90 --> 2846.16]  but just kind of verbose to mention the file name, but I'll put it in the show notes. But if you go
[2846.16 --> 2850.98]  into the lib folder inside of the bourbon folder in that folder, there's a file called generator.
[2850.98 --> 2856.56]  And inside there, you open up a class to Thor and it's just really like, if you want to learn,
[2856.56 --> 2862.72]  uh, like a really simple, but very useful way to use Thor, just file copying and stuff like that is,
[2863.04 --> 2867.76]  this is a really neat way to make your own command line for lack of better terms. So just hop on
[2867.76 --> 2872.66]  into terminal and do your own thing. And in this case, you know, everything begins with bourbon
[2872.66 --> 2876.82]  because that's the module. That's the Thor module that you're, you're making. But I just thought
[2876.82 --> 2880.98]  this is such a neat addition to it because you're right. If you're in a, uh, you know,
[2881.00 --> 2886.42]  if you're in a non-rails project or whatever, then like you had said, you have to like go and copy
[2886.42 --> 2890.38]  and paste and not only that, but like you can even do bourbon update, which pulls back from the gem.
[2890.38 --> 2897.14]  If you, if you've updated the gem and pulls that new bourbon, uh, style sheets down into your project,
[2897.14 --> 2901.78]  it's just, I think it's pretty awesome. Yeah, it is great. You know, I've got to give all the credit
[2901.78 --> 2906.52]  to the developers because I just stated my problem and they came to the resolution. So yeah,
[2906.86 --> 2914.82]  to the rescue. Um, you know, let's, let's maybe, maybe, uh, maybe one feature request on that would
[2914.82 --> 2920.16]  be, uh, or, or a question. Maybe you don't know this answer, but, uh, we talked about it, uh, a little
[2920.16 --> 2924.98]  earlier when we had our sound check, but I'm curious with all the awesome command line tools you
[2924.98 --> 2931.76]  shipped with that as, as powered by Thor, but why no bourbon watch in your read me and documentation
[2931.76 --> 2937.58]  and stuff. You still are suggesting people to use SAS watch. Yeah. Well, in an honesty,
[2937.58 --> 2943.96]  there's really no need for a bourbon watch. Um, when bourbon was released initially, we did have
[2943.96 --> 2949.90]  one dependency on a Ruby file and that's where, um, a bourbon watch would have really come in handy
[2949.90 --> 2956.58]  because, you know, you had to actually, when you pass a SAS watch, you had to pass, um, pass a flag,
[2956.60 --> 2960.98]  which called that particular Ruby file. So that was kind of a pain. But now that we've done away
[2960.98 --> 2967.86]  with that Ruby file and it's all complete, um, purely SAS really, you, you know, you just run
[2967.86 --> 2973.46]  SAS watch and then point it to your, your, uh, directory where your SAS files are and it just
[2973.46 --> 2981.16]  runs. So really the, the bourbon, if we did create a bourbon watch, it would just be a wrapper for
[2981.16 --> 2989.06]  SAS watch. So in honesty, it's, it's not, uh, that important. I think, you know, it's, I don't want to
[2989.06 --> 2995.26]  create another level of abstraction for using these tools when there's already so much going on that
[2995.26 --> 3000.18]  I think a SAS watch just gives you a better understanding of the tools you're using.
[3001.14 --> 3004.58]  Gotcha. Yeah. I figured that might've been the reason I was thinking maybe
[3004.58 --> 3009.78]  sort of bourbon watch, it could be like bourbon mix or something on this, uh, on this name, you know,
[3009.82 --> 3015.62]  this bourbon. And as you mentioned earlier, neat is, is part of the ecosystem too. So I, we got
[3015.62 --> 3020.70]  through this entire show so far without even mentioning how cool the name is and maybe even
[3020.70 --> 3026.82]  a backstory on where the name came from. Yeah. Um, let's see, what's the backstory on bourbon?
[3026.82 --> 3037.18]  I think it was, um, I mean, I love bourbon, so just drinking it is, is amazing on the palate. So
[3037.18 --> 3044.32]  I think that's where, uh, one of the, um, strong, um, ties for the name came from. So there was, I think
[3044.32 --> 3050.50]  we just, we're looking for something that sort of, um, tied into the fact that it's, we wanted to make
[3050.50 --> 3057.58]  like the philosophy behind bourbon, which is a pure SAS library, um, something that was close to the
[3057.58 --> 3064.78]  actual CSS syntax. And so initially I think I had proposed, uh, bourbon vanilla because bourbon vanilla,
[3064.78 --> 3072.92]  um, is a type of vanilla. That's actually the most popular type of, uh, vanilla out there, uh,
[3072.92 --> 3076.58]  that's sold on the market. So initially it was that, and then we were just like, well, let's just
[3076.58 --> 3082.66]  call it bourbon because we love bourbon and it's just has a great ring to it. And plus, I mean,
[3082.66 --> 3089.46]  let's face it. Thoughtbot is not, um, bad at naming things. I mean, from like suspenders to
[3089.46 --> 3095.26]  clearance, cocaine. I thought that was actually kind of comical. Uh, although I'm not a fan of cocaine,
[3095.38 --> 3100.20]  but it was pretty cool. Yeah. You think that we're just a bunch of like druggies over here or
[3100.20 --> 3104.80]  something, but yeah, well, it's just a, it was a cool, I like how in the, in the parentheses,
[3104.80 --> 3110.44]  it says, uh, command lines, you know, for, yeah, this is, I'll put that in the show notes too. So
[3110.44 --> 3115.60]  those listening, if you haven't seen cocaine yet, uh, not that cocaine, uh, thoughtbots cocaine,
[3115.96 --> 3120.08]  check out the show notes. We'll put it in there. It'll be, uh, this is episode 93. So if you're
[3120.08 --> 3124.94]  listening, you can go to five by five dot TV slash change law slash 93. If you're listening on the
[3124.94 --> 3132.52]  podcast, it'll, it'll already be live. Um, yeah. I mean, so what's, what's next for the bourbon
[3132.52 --> 3139.08]  ecosystem? So you've got neat, you've got bourbon itself. Are you going to keep pushing the boundaries?
[3139.32 --> 3144.94]  What's next? Yeah. So, well, we recently came up with neat, um, which Rita Lambden has been doing
[3144.94 --> 3151.52]  an amazing job on, uh, which is our grid framework. That's a semantic grid framework that, uh, is for
[3151.52 --> 3159.12]  building fluid grids, extraordinarily easy and doing it all, um, in your, your SAS, as opposed to,
[3159.12 --> 3165.92]  uh, polluting your, um, HTML with classes and stuff. Um, so that's just a phenomenal library and
[3165.92 --> 3172.90]  tons of praise on that. Um, we're sort of, we not sure if we officially launched it yet, but I wanted to
[3172.90 --> 3179.60]  this summer when we sort of do our company retreat is get, um, the designers together to really, uh, launch,
[3179.60 --> 3188.20]  um, this thing we're called, we're calling bidders. Um, I think it might be public somewhere on our,
[3188.20 --> 3194.10]  uh, Thoughtbot, uh, repo. Yeah. It's on your GitHub for sure. Yeah. So I think, yeah. So that's really
[3194.10 --> 3199.96]  basically a starting point that we're using on all of our projects now, uh, which gives you, um, basic
[3199.96 --> 3206.48]  variables, basic form styling, things that really you can, you know, you can just copy the folder right in
[3206.48 --> 3212.92]  and it sort of does these things that you, uh, you know, normally set up on every single project.
[3213.18 --> 3220.86]  So it saves time and effort. Um, that's meant for prototyping, right? And it's not meant to be the
[3220.86 --> 3227.90]  earned all starting point for your styles. Um, I mean, it's, it's, it's something that we want you to
[3227.90 --> 3234.96]  put into your project and change. So not necessarily like a gem, you wouldn't be able to change those.
[3234.96 --> 3240.64]  So you'd, you'd have those variables set by default, like these, we want you to actually just be
[3240.64 --> 3245.28]  changing. So yeah. So it's usually it's start with like when you start a project from scratch,
[3245.28 --> 3250.00]  throw that in there and change and modify those as your project evolves. And I think that's,
[3250.00 --> 3254.18]  that turns into a good set for a final project.
[3254.18 --> 3260.80]  So just for those who are thinking boilerplates, frameworks, whatever you want to call them,
[3261.46 --> 3266.16]  this isn't meant to be like a Twitter bootstrap or a Zurb foundation. It's meant to,
[3266.36 --> 3272.68]  it's meant to be like a decent starting point for default prototyping, but you're encouraged to
[3272.68 --> 3275.30]  change them to make it your own and be a good starting point.
[3275.30 --> 3282.14]  Yeah, absolutely. Um, we had sort of did some, um, prototyping on this thing called UI smash.
[3282.84 --> 3287.72]  Um, maybe I'm overstepping my boundaries here, but we were exploring something that would be sort of
[3287.72 --> 3295.78]  like, um, UI components that you could use in, um, your project. So something like a dropdown mix in
[3295.78 --> 3300.66]  where you could just call that and you'd have a simple dropdown, um, the CSS generated anyways,
[3300.66 --> 3308.64]  and you just pair that with some HTML. Um, so there was, I'm not exactly sure what happens
[3308.64 --> 3312.88]  that happened to that library. I think we're still developing it. And I, like I said, when we do the
[3312.88 --> 3316.64]  company retreat, I think we need to hash this out and figure out, is this something we want to
[3316.64 --> 3323.48]  continue to push forward? Um, because you know, I still use the components. I copy them into my new
[3323.48 --> 3329.76]  projects and they're just phenomenal, like starting points to get modules just built extraordinarily fast
[3329.76 --> 3337.96]  and easy. Well, uh, so bourbon neat and bitters and potentially something else, or is that something
[3337.96 --> 3345.54]  else? Bitters? Um, I think bitters we've extracted out and bitters is its own thing now. So the other
[3345.54 --> 3353.10]  thing would be UI smash or smash. So yeah, smash. I guess that stems from giant robots smashing into
[3353.10 --> 3358.98]  other giant robots. Well, so if you, um, yeah, I think so. You guys are too cool, man. Honestly.
[3360.16 --> 3364.98]  Yeah. We've got the naming down on some, on some cool things. I like that. Uh, bourbon is sort of
[3364.98 --> 3371.14]  turning into, um, shooting off into like, you can, uh, like neat, right. The name of neat is you can ask
[3371.14 --> 3377.44]  for, you know, your bourbon neat or whiskey neat, which is just simply whiskey in a glass. Um, and then
[3377.44 --> 3385.06]  bitters is an ingredient that they add to, if you get like, uh, um, uh, whiskey smash, they'll add
[3385.06 --> 3390.86]  bitters to that to give it some flavor. Um, and so I think smash really comes from like, you can get a
[3390.86 --> 3397.62]  whiskey smash or like a temple smash I think is a popular drink. So it's all cool, cool plays on
[3397.62 --> 3404.44]  drinks. That's no, that's super neat. I mean, I think it's, I mean, that's what makes, I think, uh,
[3404.44 --> 3409.42]  Wynn has said this a ton of times when he hosted the show, uh, back in the day, but, uh, we'd give
[3409.42 --> 3414.48]  cool points, you know, pluses to projects we'd feature on the change law because of their read
[3414.48 --> 3420.72]  me. I think I can't recall what it was, but somebody somehow got the DeLorean in there.
[3420.74 --> 3425.96]  And if you want to get Wynn's interest, man, do an eighties throwback, um, and put it in your
[3425.96 --> 3430.32]  read me somehow. Um, as a matter of fact, just speaking to Wynn and some things he is doing
[3430.32 --> 3437.10]  recently, um, you know, GitHub just released their OctoKit, um, both their C library as well
[3437.10 --> 3444.04]  as their Ruby wrapper, uh, for their API. And early, you know, early in the development of OctoKit,
[3444.08 --> 3448.36]  it was actually called OctoPussy because, and it wasn't meant to be dirty. I mean, not, not one
[3448.36 --> 3453.42]  little bit. It was a throwback to James Bond and, you know, that OctoPussy from way back when. And it
[3453.42 --> 3460.02]  was also, you know, you had, uh, you know, GitHub has, you know, the, the Octo thing, you
[3460.02 --> 3463.66]  know, so that's kind of like legs. I mean, so that was Wynn's humor, but nobody got it.
[3463.68 --> 3468.10]  Right. Yeah. And so they're like, yeah, that's not such a good name. And, you know, uh, I forget
[3468.10 --> 3472.72]  who it was that helped rename it to OctoKit, but, uh, at first I was like, wow, that's a
[3472.72 --> 3477.68]  cool name. And then like on the, uh, you know, in the read me was this old James Bond
[3477.68 --> 3482.72]  poster with OctoPussy and all that good stuff. And I think in the end, you know, it just probably
[3482.72 --> 3487.18]  wasn't the best name, but it was meant, it was no harm, no foul, right? It wasn't meant
[3487.18 --> 3492.88]  to be derogatory or, you know, dirty or crass. It's just, just humor. And so that was kind
[3492.88 --> 3498.68]  of cool. But, uh, anyways, um, so I want to ask you, there's a couple more questions I
[3498.68 --> 3502.58]  want to ask you before we tail off the show, but, uh, specifically because you've kind of,
[3502.68 --> 3507.36]  uh, you kind of came from what I understand, you came into ThoughtBot more on the designer
[3507.36 --> 3512.36]  side of the, of the line. And now you kind of straddle, if not totally stand across both
[3512.72 --> 3517.08]  designer and developer, uh, pretty easily nowadays. Is that about right?
[3518.02 --> 3526.68]  Uh, well, I would say that's partially right. Um, I don't really know Ruby. So, you know,
[3526.68 --> 3531.42]  since we are Ruby on rail shop, I have no experience really writing much Ruby, so I can't really
[3531.42 --> 3537.86]  jump in, um, that sort of backend development stuff. But if we're talking front end stuff
[3537.86 --> 3542.78]  and writing JavaScript, uh, coffee script, that's more what, where I sort of straddle
[3542.78 --> 3547.96]  the line of like front end developer slash designer. Gotcha. Uh, but, but you know,
[3547.96 --> 3553.80]  our role at thought, my role at ThoughtBot as a designer is to sort of be that like I, I
[3553.80 --> 3559.62]  do write code as well as design versus other, you know, agencies are like a designer role
[3559.62 --> 3563.72]  would just be doing like Photoshop mockups and doing design. And then you'd have your
[3563.72 --> 3567.72]  front end development role, which they do front end development. So sort of combining
[3567.72 --> 3572.58]  a one, but I think it makes for better design, uh, better interaction design and just the
[3572.58 --> 3576.44]  whole process, I think is much more fluid and you get better results when you sort of
[3576.44 --> 3580.06]  have a designer who can do front end development.
[3580.72 --> 3586.42]  So I guess on that note, then what would some suggestions be from you to those out there
[3586.42 --> 3590.40]  who are trying to better straddle that line, trying to get to go from their designer side
[3590.40 --> 3593.92]  to teetering on the developer side a bit more, maybe not learning Ruby, but, you know,
[3593.92 --> 3598.34]  learning more about JavaScript, coffee script, um, and, you know, kind of diving a little bit
[3598.34 --> 3602.14]  more into development. What kind of suggestions could you give to those that are listening to
[3602.14 --> 3609.58]  the show? Yeah, I'd say, um, I mean, for me, my, uh, look, my knowledge about programming
[3609.58 --> 3618.36]  sort of extended from being in SAS and trying to really use the features that SAS has. So I'd say
[3618.36 --> 3625.06]  explore SAS and those advanced features and try and look at your code and, and, uh, write that,
[3625.26 --> 3630.40]  um, some more advanced, um, loops and if statements and that sort of thing where you
[3630.40 --> 3638.98]  think they, uh, could be useful. Um, and then I would say start a side project. Um, I, I recently
[3638.98 --> 3646.30]  started a meteor JS project and that's just helped me grow so much for, uh, you know, learning JavaScript
[3646.30 --> 3651.66]  and coffee script, um, and doing it all on my own and asking the developers that I have here,
[3651.84 --> 3657.90]  any questions that I have. Um, so, I mean, I think side projects, like I learned by doing,
[3658.00 --> 3662.88]  so anytime I've got a cool side project, I'm always learning. So, you know, I just encourage
[3662.88 --> 3668.26]  anyone else to pick something up and, uh, start doing. Gotcha. Yeah. Definitely learn by doing. I,
[3668.26 --> 3674.90]  that's, um, you know, to, to just key off that a little bit, that's exactly what I'm doing. I,
[3675.00 --> 3678.90]  you know, I kind of surprised myself recently. I didn't know I knew as much Ruby as I did
[3678.90 --> 3683.74]  until I was like hanging out at code school, just randomly just watching some of their,
[3683.92 --> 3688.40]  some of their stuff. And, uh, and I'm like in the code challenges and they're like, uh,
[3688.46 --> 3693.62]  refactor this. And I'm like, I refactor it and I'm just messing around, like just totally not
[3693.62 --> 3698.46]  trying to like learn or act as if I know Ruby. Cause I've always said,
[3698.46 --> 3701.80]  and I'm self deprecating when it comes to this, I'm always like, yeah, I can read Ruby,
[3701.86 --> 3706.80]  but I can't write it, you know? And I don't know why, but I would give myself less credit
[3706.80 --> 3711.34]  than I deserved. Uh, but so anyways, I'm refactoring the code and I hit return. I'm like,
[3711.38 --> 3716.10]  and they're like, congrats, you're right. And I'm like, whoa. And then I go to the next one and it's,
[3716.10 --> 3721.28]  uh, you know, conditional logic or whatever. And it's like refactor this. And I'm like,
[3721.28 --> 3725.30]  all right, I feel a bit better about this one. I'll try it. And I'm like, I'll move to this,
[3725.38 --> 3729.66]  there, this, there. And I'm like, and I hit return and I have no idea if it's going to be right.
[3729.66 --> 3734.22]  And I totally surprised myself and it's right. And I'm like, whoa. So, you know, recently I've
[3734.22 --> 3741.68]  kind of gotten that same learn by doing stint myself where, you know, people that, that, uh,
[3742.88 --> 3746.30]  that maybe want to learn more about programming. I think programming is like super liberating,
[3746.40 --> 3751.24]  man. And you can learn how to build anything if you want it. But some people, they just think
[3751.24 --> 3755.44]  like, Oh, that's, that's some, you know, super smart nerd. Only nerds can learn that,
[3755.48 --> 3759.70]  you know, or only like super geeks or whatever. Like anybody can learn it. You just kind of
[3759.70 --> 3763.88]  put your mind to it and learn by doing, I think you're right on the side projects though, is,
[3763.88 --> 3769.00]  is having something super passionate, um, that you like, and you want to build and just,
[3769.44 --> 3773.68]  you know, no holes, no bars, just doing what it takes to try and figure out how to learn
[3773.68 --> 3778.50]  to make it and ask somebody. I know we had Avdi Grim recently on the show and we,
[3778.50 --> 3783.40]  the topic was, uh, you know, pair with me and paired programming and, you know, that whole thing.
[3783.40 --> 3788.86]  And, you know, reach out to somebody like, like Phil said, he loves to get, uh, you know, mentions,
[3789.00 --> 3793.86]  maybe, maybe Phil, you can pair with somebody and give them some of some guidance, some assistance.
[3794.04 --> 3796.26]  I don't want to hold you to that, but maybe, maybe.
[3796.50 --> 3801.44]  Yeah, absolutely. I'd love to give any kind of feedback that, that someone wants on a project
[3801.44 --> 3805.90]  they're working on or trying to help someone sort of up their game for whatever it is. So
[3805.90 --> 3810.68]  totally open to working with the community. So I got a couple of rapid fire questions and
[3810.68 --> 3817.68]  we'll tail into the final two, uh, two ending, uh, questions we have here that are, that are,
[3817.68 --> 3821.68]  uh, traditional for the Chinese law. But, uh, so a couple of rapid fire questions,
[3821.86 --> 3831.56]  Hamill or HTML? HTML. Vim or Sublime Text? Definitely Vim. Definitely Vim. So I'm so surprised
[3831.56 --> 3837.80]  by that one. I guess maybe Thoughtbot is more pro Vim than Sublime Text? Yeah. Um, well,
[3837.90 --> 3844.22]  so I would, so all the developers when I joined were using Vim and I was the first designer to adopt Vim.
[3844.58 --> 3852.02]  Nice. Um, at the time I was using Coda and I reached this point where Coda wasn't doing,
[3852.28 --> 3858.26]  it just didn't have the power I was looking for. It just, I was just felt like I was being
[3858.26 --> 3865.78]  limited, limited so hard by what Coda's capabilities were that it, the only thing that was left to do
[3865.78 --> 3870.54]  was really just move to Vim. And since I had all these, you know, Vim nerds in my office,
[3870.54 --> 3876.80]  it was like any question I did have, they were right there like helping me with. So yeah,
[3876.80 --> 3882.46]  I absolutely love Vim. It's so powerful and I can't imagine going back to any other text editor.
[3882.46 --> 3888.30]  Nice. Are there any resources that you use besides, I guess, your, your comrades to learn Vim,
[3888.38 --> 3892.34]  right? Are there any like learning resources you really thought were pretty good you could mention?
[3893.30 --> 3899.68]  Um, I mean, I think I just really Googled for like the basics of learning Vim, um, how to jump
[3899.68 --> 3904.44]  between words, that sort of thing and navigate around is really probably really important, but
[3904.44 --> 3909.98]  I would say there's a lot of, uh, plugins, like there's, uh, SAS syntax plugins, which really help you,
[3909.98 --> 3916.12]  um, uh, and like autocomplete ones, which help you just write CSS faster, um,
[3916.64 --> 3923.74]  in Vim. And I don't know, I don't really have anything in particular besides, uh, Ben Ornstein.
[3925.04 --> 3931.68]  This guy's a Vim master. Um, he's got some, some, uh, pod, uh, I think there's a screencast that he
[3931.68 --> 3938.92]  recently released. Um, we've got learn prime, which is awesome for any developer that's, uh, looking to get
[3938.92 --> 3947.06]  better at Ruby. Um, I think that's, uh, learn.thoughtbot.com forward slash prime. Um, in that
[3947.06 --> 3952.84]  we've got, um, screencasts for Vim. Um, and I think we've got, we definitely have more coming
[3952.84 --> 3959.80]  that are in the works right now. So check it out. Yeah. And I guess to, to pay homage to,
[3959.80 --> 3965.86]  to Dan Benjamin, the founder of five by five. Uh, he'd also, I just was reminded by this whenever you
[3965.86 --> 3972.30]  were talking that he actually done, um, a peep code called smash into Vim. And, uh, if you're
[3972.30 --> 3976.34]  interested, that's a little dated, but I'm sure it's all still the same. Like Vim has changed,
[3976.34 --> 3982.52]  uh, not, not tons. I mean, it's, I mean, VI Vim, it's been on Unix systems and that's kind of one
[3982.52 --> 3990.00]  of the pluses to, to, uh, using Vim too. I know that, uh, Wynn has always been a huge text mode slash Vim,
[3990.00 --> 3995.44]  um, uh, proponent. I've personally, I use sublime text. I think it's pretty awesome.
[3995.44 --> 3999.48]  Yeah. I like it. I mean, it works. Everybody has their own taste though. Right. And that's
[3999.48 --> 4005.90]  why I love those rapid fire questions. So a couple more, uh, Chrome or Safari Chrome though.
[4006.12 --> 4013.78]  I wish Chrome had Safari's animation, like smoothness and rendering because Safari is like
[4013.78 --> 4020.38]  super smooth. I wish they would like just have a baby, right? Like I like, I'm like you, I like,
[4020.46 --> 4024.74]  there's something that's like about Safari and something that's a lot about Chrome and you know,
[4024.74 --> 4029.14]  you just can't have both. And then now that, you know, I was going to ask you a bit about this,
[4029.14 --> 4032.36]  but it's, I don't want to go too deep into the show, but maybe we can talk about this in the
[4032.36 --> 4037.16]  after dark, but, uh, any thoughts you might have on blink and just the fact they, you know,
[4037.20 --> 4041.68]  they went their own way and what their plans are there. So I know you with, uh, using and doing
[4041.68 --> 4045.68]  bourbon, you've kind of got into spec a lot more. So maybe we could talk about that in the after dark
[4045.68 --> 4053.30]  though. But next rapid fire is Photoshop or fireworks sketch sketch. Oh, there you go.
[4053.62 --> 4057.58]  But if I were to truly answer that question, I would say fireworks because that's what I use
[4057.58 --> 4062.52]  before sketch. Gotcha. And so you recently moved to sketch. Yeah. I recently moved to sketch
[4062.52 --> 4070.44]  because I don't do a lot of heavy sort of graphical work. A lot of it is, is stuff that sketch can
[4070.44 --> 4078.08]  handle. That's like vector based, um, web sort of mockups. Yeah. Um, yeah. I'm using sketch myself.
[4078.08 --> 4083.00]  And the only reason that I kind of get perturbed with it with one little interface bug, if you do
[4083.00 --> 4088.04]  command option three, it kind of highs the left and right paint, uh, panels to kind of go like a more,
[4088.14 --> 4092.34]  more full screen, the same concept of being in Photoshop and clicking F, you know, that kind of
[4092.34 --> 4096.06]  thing. And then when you bring them back and you kind of move your, your canvas around,
[4096.06 --> 4102.42]  the right hand, uh, pain is kind of jacked up. I, I didn't submit a bug to it, but I'm sure it's
[4102.42 --> 4107.40]  easy to fix, but I like sketch too. Yeah. They've been doing an awesome job, uh, squashing bugs
[4107.40 --> 4111.86]  recently. So yeah, I'm sure they'll get that worked out, but I didn't know command option three did
[4111.86 --> 4115.90]  that. I've been like wanting that feature. So yeah, I wish there was a way to like go really full
[4115.90 --> 4120.66]  screen, but it just takes your current window and just gets rid of the left and right hand, uh,
[4120.66 --> 4125.64]  panel. You're still top bar still there, but, uh, if you're listening to this developers, a sketch,
[4125.78 --> 4130.04]  uh, make something that kind of goes full screen and does that. I kind of like that. I like getting
[4130.04 --> 4134.84]  all the interface away and focusing on the design and, and then kind of being able to toggle back
[4134.84 --> 4140.40]  and forth from tools to no tools. I agree with you there. Um, so yeah, let's, let's wrap up then.
[4140.50 --> 4146.24]  So we've got, um, one thing we like to ask on the show is kind of a call to arms. It's, you know,
[4146.24 --> 4151.22]  what areas of bourbon, uh, and I guess even this ecosystem of bourbon, so neat bitters,
[4151.68 --> 4155.54]  uh, smash in the future, whatever comes from that, you know, what areas of bourbon,
[4155.90 --> 4160.42]  maybe even, you know, just other things you might have in mind, where would you like to see the
[4160.42 --> 4165.76]  community kind of help, uh, step in and kind of help? Is it, uh, helping mitigate issues or just,
[4166.14 --> 4170.56]  you know, what is it that, that, uh, bourbon and what you're working on could really use in the
[4170.56 --> 4176.00]  community? Yeah, I think it's definitely issues and pull requests. Um, because there's some,
[4176.00 --> 4180.94]  I've got some pull requests right now that I just don't have a clear answer to,
[4181.16 --> 4186.48]  and I don't want to, I don't want to, you know, take the pull requests and implement it into bourbon
[4186.48 --> 4191.84]  if it's, I don't know if it just doesn't feel right. So I think take a look at the pull requests
[4191.84 --> 4196.12]  and provide feedback because that's really going to help me get a better understanding of what the
[4196.12 --> 4201.86]  community wants, um, and how I can, you know, get that integrated into bourbon and same with issues.
[4201.86 --> 4208.48]  There's some issues that are sort of outstanding. Um, that would be nice. Um, one particular place,
[4208.48 --> 4213.74]  um, that's already in bourbon that that would be nice to get some help with is the button mix in
[4213.74 --> 4220.66]  because it's a little bit, you know, it could use more button styles and, uh, it could use some
[4220.66 --> 4225.58]  cleanup too. So that'd be pretty awesome to get someone to, you know, submit a pull request to that.
[4225.58 --> 4231.92]  Yeah, absolutely. Well, uh, we'll definitely have links to bourbon, uh, both bourbon IO as well as,
[4231.92 --> 4240.48]  um, on GitHub. So, uh, if you're listening to this help, squash some pull requests, uh, or not so
[4240.48 --> 4245.60]  much pull requests, but give some feedback to issues. And, um, yeah, that I know how helpful that can be
[4245.60 --> 4252.44]  for sure. So another cool question we'd like to ask, uh, as the tail end usually is, uh, and you can
[4252.44 --> 4256.30]  answer either of these, I guess I'm going to ask you two questions technically in one, because just
[4256.30 --> 4261.86]  because you're a designer primarily in, in, uh, you know, straddling the line of hacker and developer.
[4261.86 --> 4266.90]  But so normally the question is who is your programming hero, but I'll ask you both who is
[4266.90 --> 4274.56]  your programming hero and who's your design hero? Uh, so I'll start with design hero. Um, recently I've,
[4274.94 --> 4282.32]  uh, I think Brett Victor has been doing some amazing stuff. Um, just those, uh, Vimeo videos,
[4282.32 --> 4287.64]  that he's released about, um, you know, really how like, you know, he, he seems like this
[4287.64 --> 4293.60]  interdisciplinary designer that, um, really steps into the line of developer, but also
[4293.60 --> 4298.76]  understands like so much more. Like, you know, he has all these like crazy math equations in
[4298.76 --> 4305.34]  these demos that he's showing and just really shows how like, you know, as a, as a user, you can have,
[4305.48 --> 4310.14]  get a much better understanding of a system when you can directly input and manipulate that system
[4310.14 --> 4316.84]  in like a visual way. So his stuff is just kind of blown, blowing my mind lately. And I think
[4316.84 --> 4323.74]  blowing the design industry's mind lately. Um, and I would also say for design hero, I think Drew
[4323.74 --> 4329.48]  Wilson, I know you, you, you mentioned him earlier. I think he does an awesome job, um, straddling that,
[4329.64 --> 4335.82]  that same line of being designer developer. Um, cause he had released, uh, what is it?
[4335.82 --> 4340.84]  Space box space box space box. Yeah. Yeah. So I think, you know, I'm always really inspired by
[4340.84 --> 4347.96]  designers who can actually develop applications and write code as well. So he is definitely on the
[4347.96 --> 4356.98]  list of someone I always keep an eye on for projects. He releases, um, programming dev hero. Um,
[4356.98 --> 4366.00]  I would say probably everyone who's contributed to SAS, um, SAS is just, you know, my sort of,
[4366.00 --> 4372.20]  it feels like it's a good saving grace for CSS. So, you know, that's like Chris, Chris Epstein,
[4372.72 --> 4379.52]  uh, Nathan Weisenbaum all the way, you know, back to Hampton, like just anyone who's had their hands
[4379.52 --> 4386.60]  in contributing to SAS. Thank you. That's awesome, man. And speaking of Hampton, um, June 25th,
[4386.60 --> 4391.72]  we're actually going to be joined here on the change law, June 25th. Hampton was going to come
[4391.72 --> 4396.70]  on this week, uh, but due to some travel stuff, he wasn't able to tie it up. So I thought it would
[4396.70 --> 4402.44]  kind of be cool to, to have you on Phil as kind of a preamble before Hampton, just maybe to tee off
[4402.44 --> 4407.62]  our, our, uh, little SAS fiesta for the next couple of weeks, you know, so we'll have you on this week,
[4407.64 --> 4411.86]  obviously, which we're doing and then not next week, but the week after, uh, Hampton will be on the show.
[4411.86 --> 4418.00]  So if you're a listener of the change law, Phil, you should tune in. Awesome. I met, uh, I actually
[4418.00 --> 4422.46]  met Phil. I also want to give a shout out to one of the coworkers that you work with. Um,
[4423.14 --> 4428.56]  Joe Oliveira. He's a, he's a super neat dude, man. I met him at, um, at less conf and I also met
[4428.56 --> 4436.32]  Hampton and super rad dude, both of them. And, uh, um, yeah, Joel's does a really good job of
[4436.32 --> 4440.72]  representing who you guys are as a community and who you guys are as a, as a team there at
[4440.72 --> 4445.08]  thought bodies does a great job. And then someone thinks Adam. Yeah, man. And Hampton
[4445.08 --> 4449.20]  dude's crazy, man. I love Hampton. He's so awesome. I can't wait to have him on the show.
[4449.28 --> 4454.30]  He's going to be such a lot, such, such fun, but, um, yeah, for sure. All right. Well,
[4454.30 --> 4457.42]  that's, uh, that's pretty much the show. You know, Phil want to thank you for, for joining
[4457.42 --> 4462.68]  us today, man. It's really fun talking about SAS, bourbon, neat design, CSS and everything
[4462.68 --> 4467.22]  in between sustaining open source. You know, I want to personally thank you for, from the rest
[4467.22 --> 4472.12]  of the SAS community for your work on bourbon and your, and your support. Um, and just kind
[4472.12 --> 4476.90]  of being knee deep in the specs sometimes and kind of, you know, being in the, in the trenches
[4476.90 --> 4481.32]  for lack of better terms, man. I mean, it's really awesome to, to have you on the show,
[4481.40 --> 4484.70]  man. Yeah. Well, thanks Adam. It's a, it's been a pleasure. Thanks for having me.
[4484.86 --> 4492.34]  Absolutely. And so follow Phil on Twitter. He is a Phil LaPierre full name, uh, L-A-P-I-E-R.
[4492.34 --> 4497.70]  If you don't know how to say LaPierre, uh, this has been episode number 93. I did mention
[4497.70 --> 4501.02]  that, uh, we'll be joined by Hampton in a couple of weeks. We're not sure of who next
[4501.02 --> 4505.12]  week's guest is Andrew. I think he's taking care of that. So next week's guest is got
[4505.12 --> 4509.40]  a question mark next to it. If it's you came to talk to you, uh, show notes for this
[4509.40 --> 4515.34]  show will be available at five by five dot TV slash change log slash 93. Thanks for tuning
[4515.34 --> 4516.70]  in to this show.
[4522.34 --> 4527.56]  I'll see you next week.
[4527.58 --> 4529.64]  Bye.
[4540.64 --> 4541.02]  Bye.
[4542.60 --> 4543.10]  Bye.
[4543.18 --> 4543.70]  Bye.
[4547.56 --> 4547.72]  Bye.
[4548.48 --> 4550.50]  Bye.
[4551.06 --> 4551.54]  Bye.
[4551.56 --> 4552.04]  Bye.
