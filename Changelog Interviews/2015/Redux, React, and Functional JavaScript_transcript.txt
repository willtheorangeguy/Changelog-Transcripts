[0.00 --> 2.98]  I'm Dan Abramov, and you're listening to The Change Log.
[11.90 --> 15.86]  Welcome back, everyone. This is The Change Log, and I'm your host, Adam Stachowiak.
[15.96 --> 26.50]  This is episode 187, and on today's show, the topic at hand is Redux, and we're talking with Dan Abramov, the mastermind behind Redux.
[26.50 --> 41.60]  Not only did we dive deep into Dan's past and where he came from to become a software developer, but we also dove deep into JavaScript, Redux, React, talked a little bit about Elm and ClojureScript and functional programming in JavaScript as a whole.
[42.14 --> 47.88]  Dan shared tons of advice and tons of great insight into the inner workings of Redux.
[48.30 --> 54.30]  We had four awesome sponsors, Codeship, TopTile, Braintree, and also Linode.
[54.30 --> 56.80]  Our first sponsor is Codeship.
[57.14 --> 61.58]  In the new year, January 12th, they have a free webinar you have to check out.
[62.12 --> 68.34]  Codeship's engineer, Laura Frank, is going to give an overview of Docker's ecosystem, Docker Compose, Docker Machine.
[68.80 --> 75.50]  She's going to talk about containers, and you'll learn about Docker images, why they're so powerful, and how you can start running services in containers.
[75.50 --> 85.60]  And when it comes to web apps and Docker, you'll understand how to develop your web apps using Docker, working with images, registries, and running services in containers.
[85.82 --> 89.80]  The link to this webinar is rather long, so I'm going to put it in the show notes.
[89.80 --> 98.32]  But you can also go to resources.codeship.com and look for webinars in that list, and it's going to link to the same webinar I'm talking about.
[98.48 --> 100.62]  Or head to the show notes and click the link there.
[100.92 --> 108.90]  Again, totally free, January 12th, 2016, from noon Eastern Standard Time to 1 p.m. Eastern Standard Time.
[108.98 --> 109.80]  That's one hour.
[110.14 --> 111.44]  And now on to the show.
[111.44 --> 118.70]  Everyone, we're back.
[118.80 --> 123.70]  We have Dan Abramoff here, maker of Redux and so much more.
[124.04 --> 127.50]  But, Jared, this show got started by an issue.
[127.60 --> 131.10]  Can you tell the story about the issue that got ponied up to get Dan on the show?
[132.40 --> 133.72]  No, I don't remember the issue.
[133.84 --> 134.34]  Can you tell it?
[134.52 --> 134.98]  Oh, man.
[136.20 --> 137.20]  Put me on the spot, bro.
[137.20 --> 143.04]  Well, actually, it was – how do we say his name?
[143.12 --> 143.48]  Let's see.
[143.58 --> 145.48]  His name is Kevin McGee.
[146.32 --> 146.64]  Okay.
[146.92 --> 148.32]  And he posted an issue.
[148.48 --> 148.76]  Let's see.
[148.82 --> 152.10]  It was about November 10th, so not too long ago.
[152.14 --> 156.58]  And he said, consider interviewing Dan Abramoff, project lead, mastermind.
[156.68 --> 162.06]  Dan, you got a mastermind, bro, of Redux, a predictable state container for JavaScript apps.
[162.06 --> 167.00]  So we kind of knew about Redux already, but that's how this got started.
[167.20 --> 172.24]  Dan, you chimed back in, and we said, hey, get in touch with us.
[172.32 --> 174.98]  We'll start communicating around dates, and so here we are.
[175.12 --> 176.10]  So welcome to the show, Dan.
[176.70 --> 177.32]  Thank you.
[178.86 --> 189.60]  And one of the ways we love to open up this show lately, it's been a growing trend to kind of dive a little bit deeper into who our guests are.
[189.60 --> 196.30]  So aside from being the mastermind, the project lead behind Redux, who is Dan?
[196.36 --> 196.88]  Who are you?
[197.12 --> 198.00]  How do you introduce yourself?
[199.22 --> 203.98]  Well, I'm a 23-years-old guy from Russia.
[204.66 --> 206.12]  I have a wife and a cat.
[206.12 --> 208.46]  I just moved to London.
[209.54 --> 213.00]  Before that, I lived in St. Petersburg, which is pretty much my whole life.
[213.16 --> 215.98]  I lived a little bit in Moscow, but mostly St. Petersburg.
[217.02 --> 218.76]  And I don't know, I guess that's it.
[219.00 --> 224.64]  I haven't really done much to have something to tell about myself in this way.
[225.16 --> 226.20]  What brought you to London?
[226.20 --> 232.10]  I'm actually starting, I have already started working here.
[232.32 --> 233.44]  I work at Facebook now.
[234.02 --> 235.04]  So I'm in boot camp.
[235.18 --> 237.72]  It's not, I'm not doing actual work right now.
[237.82 --> 250.00]  I'm just helping out different teams and kind of learning about the Facebook internal structure, about different teams that are there, what kind of tools they use, the infrastructure, the people, and stuff like that.
[250.00 --> 260.94]  And I'll go to MPK, which is, okay, I started actually talking with these crazy abbreviations that they use.
[261.34 --> 268.12]  So I'm going to Menlo Park in January for two weeks as part of my boot camp.
[268.40 --> 273.26]  And later I graduate from the boot camp and I'll be working on the React Native team in London.
[274.02 --> 274.34]  Interesting.
[275.02 --> 277.34]  So what does the boot camp involve?
[277.34 --> 298.12]  It involves, you go to classes to, I assume, learn some things, some internal tools and languages that they use and just kind of get to know what different people, different people on Facebook are working on because there are so many teams.
[298.62 --> 299.78]  There are so many projects.
[300.28 --> 302.48]  I'm actually pre-allocated to React Native.
[302.48 --> 316.22]  So most of people in boot camp, they go through boot camp to later choose a team, but I'm just going through boot camp to, I don't know, to do something different before working on React Native.
[317.20 --> 327.12]  And it's also a great way to kind of socialize and to get to know a lot of people because you're going to need people later when you work in the projects.
[327.12 --> 330.56]  So Facebook is very social inside.
[330.72 --> 344.48]  I did not actually anticipate it to be so, but Facebook is very people oriented and people use Facebook to communicate inside Facebook and they ping each other all the time.
[345.02 --> 349.40]  And it's best to know as many people as you can to do your job efficiently.
[349.40 --> 350.96]  That's interesting.
[351.08 --> 355.38]  Is there any particular challenges that you're facing now as you step in?
[355.40 --> 359.74]  It sounded like you were not so much not social, but it was a surprise to you.
[359.84 --> 361.44]  Is that, do you have any concerns there?
[362.22 --> 363.26]  No, not really.
[363.66 --> 371.88]  I think the main concern for me right now is to figure out my kind of life kind of issues like settling in.
[371.98 --> 374.16]  I need to find an apartment to rent.
[374.16 --> 382.26]  I'm currently living in a temporary apartment in London, but it's going to expire in a couple of months.
[382.54 --> 383.76]  So I need to do that.
[383.84 --> 385.30]  I need to get the insurance.
[385.64 --> 389.88]  I need to get some kind of numbers so I can go to hospital or whatever.
[390.84 --> 393.48]  Just a lot of life stuff that I have to deal with.
[394.28 --> 396.66]  And I never moved to another country before.
[397.40 --> 400.92]  And when I was in Russia, my mother used to do that for me.
[400.92 --> 403.92]  So the paperwork is kind of surprising.
[404.16 --> 404.60]  Yeah.
[405.00 --> 406.88]  You mentioned you have a wife and a cat.
[406.98 --> 410.18]  So I imagine they're with you or they're on their way soon.
[410.34 --> 411.44]  What's the situation there?
[412.02 --> 412.94]  Yeah, they're with me.
[414.36 --> 420.54]  Actually, UK has very strict restrictions with regards to moving paths.
[420.54 --> 429.58]  So we had to hire a company that would take the pad with a special agent and through a special airline.
[429.94 --> 432.02]  And it costs a lot of money.
[432.28 --> 435.00]  But yeah, we have the cat here now.
[435.16 --> 436.10]  You must love that cat.
[436.80 --> 437.00]  Yeah.
[437.00 --> 439.46]  Let's go back a bit.
[439.72 --> 441.62]  And you mentioned you're 23 years old.
[441.62 --> 443.08]  So you're not old.
[443.18 --> 444.30]  You're not young.
[444.58 --> 450.04]  So just to kind of give some perspective here, I'm 36, about to be 37 here this coming March.
[450.86 --> 452.06]  Jared, you're 33, right?
[452.84 --> 453.08]  Right.
[453.08 --> 454.56]  So you're 23.
[454.68 --> 459.68]  You're basically 10 years and a few more younger than the two others on the call with you.
[459.80 --> 464.96]  So not that matters in terms of your age, but just kind of diving back a bit in your history.
[464.96 --> 469.86]  Can you talk a bit about what you've been doing in the last couple of years?
[469.94 --> 471.12]  What got you into programming?
[471.68 --> 474.02]  Where have your interests been lying in the past couple of years?
[475.04 --> 479.38]  I started programming when I was 12 years old, I think.
[480.20 --> 483.62]  And it actually started, it wasn't on purpose.
[484.30 --> 489.96]  We did have programming in high school, but I didn't like it because it was Pascal mostly.
[490.90 --> 492.26]  And I didn't understand it.
[492.26 --> 496.38]  I didn't understand why we need to sort a race and that kind of stuff.
[496.46 --> 497.22]  So I wasn't interested.
[498.48 --> 502.88]  And I actually got into programming when doing different school assignment.
[504.24 --> 505.96]  I loved PowerPoint.
[506.52 --> 514.60]  So PowerPoint was my favorite software when I was a kid because I like to create effects
[514.60 --> 519.12]  and animations and to schedule animations one after another.
[519.76 --> 521.52]  And I love this kind of stuff.
[521.52 --> 529.02]  And I think once I found a menu called Service Micros.
[529.56 --> 535.84]  So macros, if you don't remember in Microsoft Office, you can record some actions and then
[535.84 --> 538.42]  press play and they are automatically repeated.
[538.84 --> 538.98]  Right.
[539.08 --> 541.58]  And you can actually edit that code.
[541.66 --> 547.58]  It generates Visual Basic code and you can edit it and the macros do something different.
[547.58 --> 555.52]  And so I was hooked back then and I bought some books and my grandma used to go with me to
[555.52 --> 560.82]  the bookshop and every few weeks she would buy me a new book as a treat.
[561.50 --> 566.72]  So I started with Visual Basic, but later I transitioned to the net, C Sharp.
[566.72 --> 570.20]  And eventually I got a job when I was 18.
[570.66 --> 573.08]  So this is how I started programming.
[573.44 --> 574.38]  What was that job at 18?
[574.38 --> 578.84]  It was a job at an outsourcing company in Russia.
[579.54 --> 584.80]  So it's a joint Russian-American company called DataArt.
[585.32 --> 592.52]  They do projects for different enterprises like financial companies, that kind of thing.
[592.52 --> 600.42]  And it was fun in the beginning because I got a real job finally, right?
[600.68 --> 601.08]  Right.
[601.30 --> 605.86]  It was fun and I got to get paid for what I like to do.
[606.62 --> 609.60]  So I learned a lot there.
[609.82 --> 614.34]  But later it was just too much enterprise stuff.
[614.56 --> 617.12]  Like, I don't know if you know Microsoft SharePoint.
[617.56 --> 617.90]  Yes.
[618.56 --> 618.84]  Yeah.
[618.84 --> 620.36]  That's the worst.
[620.68 --> 621.16]  Unfortunately.
[621.34 --> 621.72]  Right, Jared?
[621.72 --> 625.86]  Yeah, 2007 it was back then.
[626.44 --> 633.40]  And so everybody kept using very old software, very complicated software, piles of complicated
[633.40 --> 634.96]  software, one on top of the other.
[635.14 --> 636.96]  And I was just really tired of that.
[637.50 --> 644.58]  And on the other hand, my skills were mostly in native development, meaning Windows native
[644.58 --> 645.04]  development.
[646.50 --> 650.54]  And I didn't know how to create mobile apps or I
[650.54 --> 652.48]  I didn't know how to create websites.
[653.38 --> 659.64]  And I felt a little bit scared that maybe I just can't do, maybe I cannot learn it.
[659.72 --> 661.20]  Maybe it's too complex for me.
[661.20 --> 664.80]  So I stayed away from it for a while.
[664.80 --> 666.86]  But after that, I quit my job.
[667.96 --> 674.36]  And I was lucky enough that my mother could support me for like six months and pay my rent
[674.36 --> 676.48]  while I learned web technologies.
[676.48 --> 683.86]  So I went to an internship, which is not exactly an internship.
[683.86 --> 691.90]  It's just it was a volunteer club of people helping one Russian entrepreneur build his
[691.90 --> 693.12]  websites and projects.
[693.12 --> 697.18]  So the conditions were that we don't get any money.
[698.18 --> 702.22]  But on the other hand, we just get to learn different things for free.
[702.34 --> 707.62]  And he doesn't care that we're not actually good because he just wants things done and
[707.62 --> 708.34]  we want to learn.
[708.34 --> 718.26]  So we had this club and I learned Git and CSS and jQuery and Python Django just by helping
[718.26 --> 719.42]  him do his projects.
[720.06 --> 723.72]  And there were like 10 people there, but we had a lot of fun.
[724.18 --> 730.70]  And later after that, I got some idea about JavaScript, although I wasn't really an expert.
[730.70 --> 736.08]  I didn't know what is this and, you know, these kinds of JavaScript gotchas.
[737.58 --> 741.78]  But anyway, I was looking for a job and I got a job at a startup.
[743.28 --> 748.54]  So I was working at a Russian startup, which pretended not to be Russian.
[749.54 --> 751.56]  It is called Stampsy.
[752.68 --> 758.64]  It's like a medium, but for images and multimedia content, videos, audios.
[758.64 --> 766.98]  And back then we were focused on creating an iPad application that would allow you to create
[766.98 --> 773.58]  and consume this kind of multimedia content, like small magazines that you can create right
[773.58 --> 774.40]  in the application.
[775.52 --> 781.76]  And I didn't have any iOS experience, but again, I was lucky to be somewhere where I could learn
[781.76 --> 782.32]  on the go.
[782.82 --> 783.72]  And this probably helped.
[783.72 --> 789.98]  I think this is something that helped the most in my career, that I was lucky to find
[789.98 --> 799.20]  several places where I'm always able to learn at the go and not come with some large portfolio
[799.20 --> 799.76]  or whatever.
[800.58 --> 805.16]  So I learned iOS while working on an iOS application.
[805.16 --> 809.78]  And both me and one of the other developers, we knew C Sharp.
[809.96 --> 814.70]  We didn't know Objective-C and Swift did not exist back then.
[815.26 --> 819.28]  So we just, we wrote the iPad app in C Sharp.
[820.10 --> 822.40]  And we used Xamarin back then.
[823.26 --> 828.70]  And it was a hybrid app because the editor, the part where you actually create the post,
[828.70 --> 837.16]  it needed to be based on the web technologies because we wanted to bring it to the web later.
[838.36 --> 840.38]  So it was a hybrid app.
[840.44 --> 843.16]  We had to learn a lot about the breaches, that kind of stuff.
[843.74 --> 845.84]  So it was a lot of fun to build it.
[845.84 --> 849.92]  And when we released it, it was featured by Apple on the first day.
[850.60 --> 859.64]  And it stayed pretty, like it stayed featured and it was in top 100 for a while, for a couple
[859.64 --> 860.00]  of weeks.
[860.46 --> 866.10]  But people didn't really use it in the ways that we hope they would use it.
[866.74 --> 871.44]  And after the initial interest, it just fell.
[871.74 --> 873.14]  Like nobody remembered it.
[873.14 --> 879.66]  And so we stopped working on it and we started working on the web version instead because
[879.66 --> 885.50]  we figured that the people who have professional looking beautiful content, they don't have
[885.50 --> 887.08]  this content on their iPads.
[887.70 --> 893.46]  And what they usually have on iPads are low quality photos, which are not exactly the content
[893.46 --> 893.92]  we wanted.
[894.80 --> 900.74]  So we then created the web version and we had no idea how to build a web application.
[900.74 --> 904.98]  So we learned a little bit of Backbone.
[905.48 --> 912.56]  And it kind of worked for some time until the application got dynamic.
[912.94 --> 920.02]  And we had these pop-ups and model windows, tabs inside them, and a complicated drag and
[920.02 --> 920.96]  drop post editor.
[920.96 --> 927.64]  And it was very hard to create a really dynamic, really interactive UI with Backbone.
[928.32 --> 932.72]  So this is when we started looking at React and kind of played a little bit with it.
[933.40 --> 937.36]  And gradually we rewrote our app in React and Flux.
[937.36 --> 945.94]  And this is basically how I got involved in React community because it was still very young.
[946.46 --> 956.96]  And I mean, when we added React to Stemsy, I think the React router didn't exist.
[957.76 --> 957.86]  Wow.
[957.86 --> 960.28]  So this was the time before React router.
[961.12 --> 965.78]  And when it finally came out, I was like, hey, it's time to switch from Backbone completely.
[967.54 --> 969.34]  So we switched to React.
[969.46 --> 973.38]  And when we had a redesign, we had a chance to switch to Flux.
[973.38 --> 978.30]  But later, and I mean, it was a great experience.
[978.48 --> 979.76]  I learned a lot there.
[980.34 --> 987.60]  But I quit from Stemsy in April 2015 because they ran out of funding.
[987.82 --> 989.00]  The numbers weren't good.
[989.70 --> 990.98]  People are using it.
[991.06 --> 996.22]  There are many users, like, I don't know, maybe 40,000 or something.
[996.56 --> 1001.22]  They post their content, but it wasn't skyrocketing or something.
[1001.22 --> 1003.18]  It was just a linear growth.
[1004.18 --> 1007.44]  And a couple of weeks ago, our founder died.
[1008.36 --> 1009.60]  So that's, yeah.
[1010.26 --> 1014.64]  I've been through a situation like that where I'm working somewhere and your founder passes away.
[1014.80 --> 1016.62]  And it's a big shock.
[1017.08 --> 1017.52]  Yeah.
[1017.90 --> 1024.54]  It's such an unusual thing to go through because not only do you feel lost personally,
[1024.58 --> 1026.12]  but you also feel lost corporately.
[1026.12 --> 1026.36]  Yeah.
[1026.36 --> 1032.14]  And it's so rough to kind of share that with your comrades, you know?
[1032.92 --> 1033.12]  Yeah.
[1033.40 --> 1033.58]  Yeah.
[1034.12 --> 1037.24]  So that was by the time I wasn't working there anymore.
[1037.50 --> 1039.14]  I was doing open source stuff.
[1039.14 --> 1045.90]  And I kind of lived by doing some contacts, doing some contact work.
[1046.02 --> 1048.18]  And it worked pretty well, I would say.
[1048.82 --> 1055.52]  But it's hard to switch between open source and contact work for me because I just hate switching context.
[1056.18 --> 1058.86]  It's hard for me to work on many things at once.
[1058.86 --> 1061.78]  So I was looking for a full-time job.
[1062.00 --> 1063.42]  And I spoke to Facebook before.
[1064.08 --> 1067.66]  And they were like, hey, you can come to US.
[1067.98 --> 1071.24]  But no, you can't because you can't get a visa to US.
[1071.26 --> 1071.54]  Right.
[1072.26 --> 1075.06]  Because I don't have, I dropped out of the college.
[1075.28 --> 1076.42]  I don't have the degree.
[1076.96 --> 1077.72]  And I don't have...
[1077.72 --> 1077.88]  What?
[1077.98 --> 1078.66]  You dropped out?
[1079.32 --> 1079.66]  Yeah.
[1080.40 --> 1081.08]  I did.
[1081.08 --> 1084.10]  So I couldn't get a visa to US.
[1084.28 --> 1088.52]  And they said, hey, maybe you can get a visa to London later.
[1088.86 --> 1090.46]  But we don't have a team there yet.
[1090.48 --> 1092.12]  So let's keep in touch.
[1092.76 --> 1097.34]  And later in the conference, I was interviewed by the team.
[1098.84 --> 1099.40]  Very...
[1099.40 --> 1100.58]  It wasn't planned.
[1101.22 --> 1105.42]  I basically skipped to the second day of the conference because I was on the interviews.
[1106.24 --> 1107.58]  But this is how I got hired.
[1107.58 --> 1118.08]  And the past six months, we're just about preparing all the documents and passing English exam and all the kind of things you need to do to go to UK.
[1118.36 --> 1118.90]  And I'm here.
[1119.42 --> 1119.96]  There you go.
[1120.14 --> 1121.22]  Well, congrats on that.
[1121.32 --> 1121.58]  I mean...
[1122.30 --> 1122.54]  Yeah.
[1122.54 --> 1128.30]  It sounds like your trip to where you are now from where you came from is pretty interesting.
[1128.44 --> 1130.24]  I mean, just to kind of repaint it for the listeners.
[1130.84 --> 1132.54]  You came from a PowerPoint background.
[1132.88 --> 1135.70]  I don't know if that's exactly accurate, but that was your first love, so to speak.
[1135.70 --> 1141.78]  And then you got into C Sharp because of just your natural progression, then jQuery and Backbone, and now where you're at now.
[1141.92 --> 1147.32]  And you said you started your first job in anything at 18, and now you're 23.
[1147.50 --> 1158.02]  So in five years, you've gone from someone who was just kind of fluent and maybe just getting started with native, as you'd mentioned, with Windows.
[1158.28 --> 1159.30]  And now, look at you.
[1159.30 --> 1163.46]  You're at boot camp at Facebook, which is awesome.
[1164.24 --> 1165.02]  Yeah, it's cool.
[1166.04 --> 1168.74]  You have thanks to your grandma and your mom, too, for helping out.
[1168.76 --> 1171.02]  Your grandma bought you some books, which was...
[1171.02 --> 1171.10]  Yeah.
[1171.10 --> 1172.20]  Who doesn't love their grandmas, right?
[1172.80 --> 1173.02]  Yeah.
[1173.10 --> 1177.10]  And then their mothers to step in and support them whenever the town needs it.
[1177.12 --> 1178.04]  That's such an awesome thing.
[1178.12 --> 1183.36]  So I guess now that you're, in quotes, famous, you can give back.
[1184.06 --> 1184.76]  Yeah, exactly.
[1184.92 --> 1186.74]  At least I hope to do that.
[1187.04 --> 1187.68]  I mean, I'm not...
[1187.68 --> 1187.90]  Right.
[1188.54 --> 1192.10]  I'm not doing a lot, but I open source and stuff.
[1192.62 --> 1195.58]  So maybe one more topic before we go into the break here.
[1195.94 --> 1200.36]  You'd mentioned that you weren't really...
[1200.36 --> 1208.80]  I'm kind of piecing together something I heard elsewhere and then something I heard here, which was React is what inspired you to contribute to open source.
[1209.18 --> 1209.36]  Yeah.
[1209.38 --> 1215.24]  You hadn't really been doing anything around open source, and you'd mentioned how it was hard to do day job and open source together.
[1216.08 --> 1216.30]  Yeah.
[1216.30 --> 1226.10]  Can you talk a bit about your first steps into open source and what that looked like for you as someone who came from a world where maybe you weren't contributing or doing much with it?
[1226.10 --> 1232.02]  Yeah, I think it is really about React being a young ecosystem.
[1233.08 --> 1242.66]  So if you're an open source, if you're someone who considers maybe contributing to open source, but you don't know where to start,
[1242.66 --> 1249.78]  you probably shouldn't create like another HTTP library or something like that because a lot of those exist.
[1250.46 --> 1259.14]  But what you probably should do is find the ecosystem that is young but promising.
[1260.48 --> 1271.04]  And this is kind of how I got lucky with React because I needed to build some things for my job because they did not exist at the time and they were necessary.
[1271.04 --> 1275.72]  And React provided enough value so that we didn't want to give it up.
[1276.16 --> 1278.92]  But then we had to contribute to the ecosystem, right?
[1279.04 --> 1287.10]  So this is how it got started for me because my job demanded actually doing something around React that did not exist at the time.
[1287.10 --> 1295.06]  And on the other hand, I had this personal project called React Hotloader.
[1295.66 --> 1302.08]  And I was really inspired by the idea of putting two and two together.
[1302.58 --> 1308.40]  There was React with declarative rendering model and there was Webpack with its hot model replacement.
[1308.40 --> 1313.78]  And I wanted to bring them together because it just made sense to me.
[1313.92 --> 1318.70]  Like I want this kind of workflow that I saw in Brad Victor videos.
[1318.82 --> 1329.26]  Although I know Brad Victor hates people like me probably because we only take the easy parts from his talks and not the really important and complex parts.
[1329.26 --> 1335.68]  But anyway, I was inspired by him and I wanted to do something of that sort and share it.
[1336.10 --> 1337.42]  And it was my personal project.
[1337.60 --> 1340.84]  I remember my wife was like, what the hell are you doing?
[1340.94 --> 1341.92]  And it was 5 a.m.
[1342.02 --> 1346.44]  And I was in the bed and I made this ugly hack.
[1346.84 --> 1355.30]  Like I changed React internal code just to get it to work somehow so I can record a fancy screencast demo in it.
[1355.30 --> 1355.68]  Wow.
[1355.92 --> 1361.60]  So I had a fancy demo that only worked for like a single file correctly.
[1362.04 --> 1367.18]  And it was full of hacks, but it looked like it actually works.
[1367.42 --> 1372.64]  And I recorded this video and Christopher, Christopher, I'm not sure.
[1372.78 --> 1372.98]  Shadell.
[1373.44 --> 1373.56]  Yeah.
[1373.68 --> 1374.84]  Yeah, he shared it.
[1375.96 --> 1377.20]  Instant fame, right?
[1377.74 --> 1378.14]  Yes.
[1378.14 --> 1385.20]  It was like 50 or 70 retweets and it was a lot for me when I had maybe 30 followers.
[1386.44 --> 1387.98]  So this is how it got started.
[1388.14 --> 1391.00]  And I really felt that people want this.
[1391.12 --> 1392.28]  People want this to exist.
[1392.42 --> 1393.90]  And I also want to exist.
[1394.50 --> 1401.46]  So when I went for a holiday, I swam a little in the sea.
[1401.46 --> 1410.70]  But after that, I would just go and code for several hours to get this into shape where it actually works for more than one person.
[1411.64 --> 1413.58]  And the feedback was amazing.
[1413.80 --> 1416.12]  And I think this is what made me quote famous.
[1416.68 --> 1416.80]  Yeah.
[1417.38 --> 1419.26]  It's an interesting story there too.
[1419.52 --> 1424.70]  It reminds me of the phrase, and tell me if you've heard this before, Dan, by any means necessary.
[1424.70 --> 1427.36]  You know, you have to get somewhere.
[1428.38 --> 1443.10]  And I can remember a talk I heard back at Lone Star Ruby Conference, the very first one, this guy was talking about just shelling out and how it was such a bad thing to do from Ruby code inside of a Rails app or Ruby app.
[1443.22 --> 1446.44]  And, you know, kind of breaking what is considered the rules, so to speak.
[1447.10 --> 1450.30]  And it sounds like you're not bound by rules.
[1451.42 --> 1451.86]  Yeah.
[1451.86 --> 1456.46]  To a degree, obviously, but if you have to get somewhere, you're going to get there.
[1457.22 --> 1457.42]  Yeah.
[1457.72 --> 1477.64]  And it's also, I think, it's very important that even if you have a day job, if it's possible, you need to try to have a broad view of what's happening in ecosystem around you and different ecosystems around you.
[1477.64 --> 1488.08]  Because a lot of people get locked into a certain ecosystem like React ecosystem or Ember on Angular, and they love the framework or they hate the framework, whatever.
[1488.24 --> 1492.82]  But they just, they don't talk to people outside the bubble.
[1492.82 --> 1494.42]  And it's a big problem.
[1494.42 --> 1495.26]  Yeah.
[1495.26 --> 1501.54]  But most really interesting projects, they're on the borders of the ecosystem.
[1501.54 --> 1517.42]  Most interesting projects happen when one ecosystem collides with another ecosystem or when a project, a person takes a lesson from one ecosystem and brings that to another ecosystem.
[1517.42 --> 1519.42]  So I think this is really important.
[1519.42 --> 1529.42]  And this is something I'm trying to do in ways that I can just point people to some nice things that exist elsewhere.
[1529.42 --> 1545.96]  And maybe people creating those things don't really care that much for us, but we need to get inspired by them and we need to steal their good solutions and find ways to figure out if these solutions will help us too.
[1546.30 --> 1550.90]  So there needs to be a healthy exchange of ideas, even between competing frameworks.
[1550.90 --> 1553.42]  Yeah, I 100% agree.
[1553.50 --> 1564.94]  And I'm glad you said that because that's definitely a good point to bring up, especially when you talk about your entrance into open source and React and how you looked at the ecosystem and how can I bring value back, but also not sticking inside that bubble.
[1565.74 --> 1568.26]  Very important aspect to think about.
[1568.50 --> 1570.20]  That's a good spot to take a break.
[1570.24 --> 1571.26]  So we're going to take a quick break.
[1571.44 --> 1578.24]  When we come back, we're going to dive deeper into Redux, React, and this journey you've been on.
[1578.24 --> 1579.32]  So let's take that break.
[1579.52 --> 1580.14]  We'll be right back.
[1580.90 --> 1593.64]  Our friends at TopTile launched a scholarship program for female developers to support aspiring female computer scientists, developers, and software engineers to help achieve their goals through financial support and also mentorship.
[1594.18 --> 1601.68]  Each scholarship winner will receive a $5,000 scholarship that can be used towards education and professional development goals.
[1601.68 --> 1608.12]  You can spend this money on anything you want from coding boot camps to online programming courses, textbooks, you name it.
[1608.12 --> 1615.94]  You also get one-on-one mentoring, an entire year of weekly one-on-one mentoring with a TopTile senior developer.
[1616.46 --> 1623.92]  And this person is going to help you with topics like project guidance, choosing an academic or career path, and also preparing for interviews.
[1624.26 --> 1627.98]  Head to TopTile.com slash scholarships to learn more and also to apply.
[1627.98 --> 1657.96]  All right.
[1657.98 --> 1664.68]  Thank you for sharing that value back in and sharing that back with the audience here listening about how you came into open source and how you give back.
[1665.14 --> 1666.80]  It's really, really, really interesting.
[1666.92 --> 1668.44]  So thank you for sharing that with us.
[1669.02 --> 1670.26]  Now it's time to dive a little bit deeper.
[1670.26 --> 1678.20]  Obviously, a lot of people are coming to this podcast thinking, I want to hear about the deepest parts of Redux when it comes to what Dan has to say about it.
[1678.28 --> 1681.38]  So how do we begin this conversation?
[1681.50 --> 1687.36]  Do we just kind of dive in and talk about what Redux is, or is there a better place to begin to start unraveling this story?
[1688.36 --> 1693.18]  It depends on whether you want to come from technology or from history perspective.
[1693.18 --> 1706.04]  Because usually when I explain Redux, I explain it from where it came from and what was I trying to solve when I started working on it.
[1706.20 --> 1707.04]  Let's begin there then.
[1707.14 --> 1707.56]  That's good.
[1708.60 --> 1708.76]  Yeah.
[1708.76 --> 1709.02]  Okay.
[1709.02 --> 1722.04]  So I don't know if you know about Flux a lot, but Flux is like Facebook's solution to more to the data layer in React apps.
[1722.04 --> 1724.82]  And it's not the dominant solution anymore.
[1725.64 --> 1730.98]  Facebook is actually moving to Relay, which is a different framework they released this year.
[1732.32 --> 1737.98]  So Flux is more, it's often described as a part and not a framework.
[1738.66 --> 1744.34]  But after Facebook released Flux, there were lots of different takes on Flux architecture.
[1744.34 --> 1754.94]  And some of these takes actually lost some benefits of Flux because either intentionally or unintentionally.
[1756.04 --> 1762.92]  And they also added some value, like better support for server rendering, for example.
[1763.82 --> 1770.60]  But anyway, by the time I started working on Redux in June 2015.
[1770.60 --> 1775.16]  And by that time there was a lot of frameworks, a lot of Flux frameworks.
[1775.82 --> 1784.34]  I think the most popular ones were Alt Flummox and Flexible.
[1784.84 --> 1786.80]  So these were the most popular ones.
[1787.02 --> 1793.38]  And of course the vanilla Facebook Flux implementation, which I think all of them actually use internally.
[1794.56 --> 1798.66]  So I did not want to create a Flux framework.
[1798.66 --> 1804.90]  I tried to not do that for the longest time I could.
[1805.36 --> 1807.34]  I resisted it a lot.
[1808.30 --> 1812.76]  And I kind of liked Flummox and I used it in some of my projects.
[1813.24 --> 1823.72]  But I had this conference talk that I needed to give because in February I signed up to give a talk at React Europe conference.
[1823.72 --> 1829.12]  And the title of my talk was Hot Reloading with Time Travel.
[1829.12 --> 1838.32]  So the way I came up with that is that I wanted to talk about React Hot Loader and about this kind of workflow with Hot Reloading.
[1838.72 --> 1848.96]  And when you just edit a component and see the changes reflected in your browser without refreshing the page, without losing the current state.
[1848.96 --> 1853.22]  It's been a huge productivity boost for my workflow and I wanted to share it.
[1853.70 --> 1856.02]  But I thought that people have already seen that.
[1856.92 --> 1866.26]  And I mean, there was a talk at React conference, the first React conference, that mentioned Hot Reloading.
[1866.72 --> 1871.30]  Although we did not demo it, I still felt that I don't want to repeat that exactly.
[1871.30 --> 1871.56]  Right.
[1872.24 --> 1876.66]  So I was looking for more inspiration in Brad Victoria's videos.
[1876.92 --> 1883.42]  And he had this time travel kind of thing where you play a game and then you can rewind to any moment.
[1883.62 --> 1893.30]  And you can change the code and you can actually see how it's going to happen in the future given the same actions.
[1893.30 --> 1900.32]  Like in the game, you walk to the right and jump.
[1900.84 --> 1913.20]  And if you change the arguments through the jump function, you're going to see how that jump that has already happened is going to change life as you edit the arguments.
[1913.20 --> 1918.14]  So this was something that really excited me.
[1918.76 --> 1923.66]  And I wanted to incorporate that in my talk, but I didn't know how.
[1924.18 --> 1931.34]  And I made a very quick proof of concept of time travel with overriding React set state method.
[1931.76 --> 1934.00]  The method on the component where you set the state.
[1934.00 --> 1946.64]  I did some kind of ugly hack where I placed a slider next to every component and I overrided set state method to record every previous state.
[1946.94 --> 1949.32]  And the slider would move between those states.
[1949.76 --> 1955.56]  So, of course, this is not useful in any real application because you have, I don't know, hundreds of components.
[1955.90 --> 1959.28]  And it's not useful to have slider in front of every component.
[1959.84 --> 1962.66]  But it kind of proved that this is possible.
[1962.66 --> 1964.88]  And I met a bet.
[1965.24 --> 1967.48]  I wanted to go to the conference.
[1967.76 --> 1974.90]  I would not have been able to afford the ticket if I went as a regular person.
[1975.18 --> 1978.08]  So I needed to become a speaker.
[1978.74 --> 1987.18]  So I submitted a proposal for my talk called Hot Reloading with Time Travel without actually knowing how to implement time travel.
[1988.12 --> 1988.76]  Nice.
[1988.86 --> 1989.36]  That's awesome.
[1989.36 --> 1993.08]  Yeah, I had a few months to actually do that.
[1993.46 --> 2003.22]  But I was busy with a different project, a different project called React D&D, a drag and drop library that I started writing at my job.
[2003.22 --> 2007.72]  But I wanted to rewrite it for 1.0 and I was busy with that.
[2008.18 --> 2018.82]  And then it was June and I only had one month until the conference and I needed to figure out how to make a beautiful time travel demo somehow.
[2018.82 --> 2035.86]  And by the time I had the feeling that Hot Reloading is a little bit useless in Flux applications because most of the time you work on this tour, on the logic of data mutations and not on the components.
[2035.86 --> 2040.46]  I mostly had my designer friend work on the components directly.
[2040.46 --> 2043.26]  But I was working on the mutation logic.
[2043.92 --> 2048.58]  And I could not hot reload it because the state is local, it's in local variables.
[2048.90 --> 2058.08]  And if you execute this module, this kind of part of the script again, you're going to have the initial values for these variables.
[2058.08 --> 2060.10]  So you lose the state every time.
[2061.00 --> 2068.32]  And you also lose the components are still subscribed to the old version of the store you're working on.
[2068.54 --> 2084.20]  So if you re-execute that module, if Webpack Hot Model Replacement rewires all the required statements to point to this new version, it's still not going to work because components are already subscribed to the old store that is not the one you're working on.
[2084.20 --> 2114.18]  So this was a big problem for me.
[2114.20 --> 2121.20]  I think sometime during this period, I read a document called Elm Architecture.
[2122.20 --> 2124.48]  And Elm is a programming language.
[2124.92 --> 2131.80]  It compiles to JavaScript, but it's a different, it's a functional programming language created by Evan Tsaplytsky.
[2131.80 --> 2137.88]  And actually, I didn't understand the document fully.
[2138.80 --> 2148.12]  And this is like a confusing moment because I know later Evan was a little bit angry about me not mentioning him in the talk.
[2148.12 --> 2159.04]  And he had every right to do that because indeed Redux Architecture, a big part of it is pretty much a ripoff of Elm Architecture.
[2159.04 --> 2165.24]  But in my defense, I would just say that I think I didn't fully understand Elm Architecture.
[2165.60 --> 2167.68]  And it was just somewhere in my subconscious.
[2168.56 --> 2172.22]  And in fact, the first version of Redux, it was not like Elm.
[2172.32 --> 2173.52]  It was more like Flux.
[2173.52 --> 2183.38]  And it was Andrew Clark, actually, the Flux guy, who helped me figure out how to make it much better.
[2183.38 --> 2191.86]  I think he helped figure out the fundamental reducer composition pattern that we use in Redux for building scalable apps.
[2192.82 --> 2197.98]  And Andrew had a ton of influence in Redux.
[2197.98 --> 2212.96]  And this is another moment where I think it's not very common for a maintainer of a popular open source library like Flammox, which was very popular at the time, to just give up on it and say,
[2213.34 --> 2219.00]  hey, I'm going to join this competing project because I think that it's better.
[2219.36 --> 2223.08]  And I'm just going to tell my users that I'm making the final release.
[2223.36 --> 2225.28]  And now I'm going to work on that instead.
[2225.28 --> 2230.86]  So Andrew had a very large influence on Redux.
[2231.24 --> 2235.04]  He helped figure out reducer composition, which made it more like Elm.
[2235.30 --> 2242.12]  And he also designed the extension system for Redux, the middleware and straw enhancers.
[2242.30 --> 2243.16]  It was his ideas.
[2243.80 --> 2253.42]  So initially Redux had a single author in NPM package JSON, but I changed it to be us both because that's the truth.
[2253.42 --> 2258.96]  It's a nice example of what you were saying earlier about keeping your eyes open on these other ecosystems.
[2259.20 --> 2261.84]  Here you are reading the Elm architecture.
[2263.62 --> 2270.44]  Well, you're not doing Elm directly, but you're taking ideas from there and bringing them over to the areas that you're trying to solve problems.
[2270.44 --> 2271.44]  Yeah.
[2271.86 --> 2276.28]  So Redux comes out of this desire to have an awesome conference talk, basically.
[2276.78 --> 2278.06]  That's what I'm getting out of this.
[2278.48 --> 2280.12]  Which is a new thing to me.
[2280.24 --> 2284.96]  It's like upcoming conference talk, demo-driven development, basically.
[2285.62 --> 2287.14]  Yeah, conference-driven development.
[2287.56 --> 2288.38]  Yeah, there you go.
[2288.38 --> 2295.84]  Turns out it seems like it's generally useful for lots of things, not just wowing your friends at conferences.
[2295.84 --> 2299.34]  You say it's inspired by Flux.
[2299.84 --> 2310.26]  Is the big differentiation between Redux and Flux is this idea of a single store for your entire application state, whereas Flux has multiple stores?
[2310.34 --> 2311.66]  Is that the big differentiator?
[2312.08 --> 2312.84]  Or am I missing something?
[2312.84 --> 2315.24]  Yes, that's the big difference.
[2315.48 --> 2320.20]  And I think it's in how we choose to separate the concerns.
[2321.12 --> 2331.64]  So in Flux, you separate the concerns with having different stores, but you also separate the event subscription because you have components subscribing to different stores.
[2331.80 --> 2338.60]  And you also separate the street because you have different stores managing different parts of the street.
[2338.60 --> 2345.30]  But in Redux, we actually keep the street and the subscription in a single place in the store.
[2346.02 --> 2353.56]  And to separate concerns, we create many reducers, which are just functions that tell how state is transformed.
[2354.64 --> 2362.68]  And this is kind of similar to how React has one root component, but it's composed out of many components.
[2362.68 --> 2368.04]  So in Redux, you have one root reducer that tells how state is updated.
[2368.54 --> 2373.40]  But you can call functions from other functions and you can have as many reducers as you want.
[2374.06 --> 2378.22]  And it's like a reducer tree managing your application state.
[2378.22 --> 2384.08]  So you manage the time travel by basically running those same reducers in the opposite order?
[2384.58 --> 2388.12]  The way it works is that there is a big difference.
[2388.32 --> 2391.68]  When people say time travel, they sometimes mean different things.
[2392.64 --> 2398.94]  And in Flux, some Flux frameworks actually support time travel, but not the way Redux supports it.
[2398.94 --> 2415.28]  So what's more common is that you can travel between existing history and you can make your components render any point in time that previously existed.
[2415.68 --> 2417.96]  But this is not exactly what Redux does.
[2418.36 --> 2425.16]  So what Redux lets you do is that you can go back to some previous state, like a couple of actions ago.
[2425.16 --> 2434.48]  Then you can change the code of your reducers and it's going to re-execute all actions after and before that.
[2434.90 --> 2442.52]  So that you're like traveling to a parallel world where the code was different.
[2443.02 --> 2447.60]  And so all the states were actually different because it changed the code that computes them.
[2448.18 --> 2450.86]  And of course, it's not efficient to do that in production.
[2451.00 --> 2452.40]  This is only meant for development.
[2452.40 --> 2458.32]  But basically, we keep all the actions and if the code changes, we re-evaluate them from the beginning.
[2459.24 --> 2470.94]  Yeah, so the practical benefits of that seem, like you said, they're the best in development where you can try many code paths or many different reducers or functions and see what the differences are like.
[2471.58 --> 2476.78]  What other advantages fall out of this idea of being able to move forward and backward?
[2476.78 --> 2479.88]  It's not so much about moving forward and backward.
[2480.14 --> 2486.58]  I mean, it's very cool for impressing your friends and for debugging really weird state and mutation issues.
[2486.58 --> 2498.62]  Like when you have some control that updates really fast and you have Ajax response coming in and then you're not sure that in the middle state something broke, but you're not sure why.
[2498.94 --> 2501.18]  So you can step back and see, oh, I'm in this state.
[2501.50 --> 2503.24]  I'm going to edit the component.
[2503.76 --> 2505.72]  The component not renders correctly.
[2506.06 --> 2506.88]  It's hot reloads.
[2506.88 --> 2510.36]  Now you're going to go back forward to the current state.
[2510.48 --> 2512.94]  And so you can see everything that is happening.
[2513.52 --> 2522.74]  And if in some cases the state was not updated correctly, you can see where exactly, because you have the whole history of every action and the state after that.
[2522.82 --> 2524.68]  And you can inspect it in a tree view.
[2525.30 --> 2528.78]  So you can see where exactly it went wrong.
[2529.04 --> 2532.26]  You can fix the code and make sure that now it is correct.
[2532.26 --> 2541.56]  And if you make a mistake, if you make your reducer crash in development, it's just going to say that there has been an error, like fix your code.
[2541.70 --> 2543.74]  The error occurred after this action.
[2544.22 --> 2547.20]  So you fix the code and then it re-evaluates again.
[2548.32 --> 2551.02]  Hopefully you fix the error and it renders something different.
[2551.54 --> 2556.34]  So it's a whole, another, a different, more efficient developer workflow.
[2556.34 --> 2563.40]  But this is just one of the benefits that slides out of this model with single state.
[2564.08 --> 2570.28]  So other benefits are that it's easy to replay user actions.
[2570.86 --> 2576.50]  So, for example, you can log every action that happens in case you're debugging some kind of issue.
[2577.04 --> 2583.80]  You can log every action, you can serialize them, and then you can replay them on your computer and reproduce the bug.
[2583.80 --> 2586.40]  And this is possible with Flux too.
[2586.90 --> 2592.32]  But with Flux, you need to be very careful to implement it in a very specific way.
[2592.96 --> 2596.08]  And in fact, some teams at Facebook don't implement it that way.
[2596.30 --> 2599.86]  But you need to be very careful to be predictable.
[2600.28 --> 2604.16]  And I think Redux makes it easier by imposing more constraints.
[2605.10 --> 2607.86]  It also seems like a more simple mental model.
[2607.86 --> 2614.58]  The one thing that I noticed with Flux and started looking at it is, man, there's a lot of moving parts.
[2614.72 --> 2616.16]  There's a lot of things to think about.
[2616.86 --> 2621.12]  And there's a lot of diagrams to digest here before I start building my application.
[2621.78 --> 2624.24]  And then it was choose your framework.
[2625.24 --> 2627.40]  Your Flux implementation, I should say, not your framework.
[2627.40 --> 2638.88]  But which Adam reminds me of, one of my favorite parts in our recent season two of Beyond Code was Jonathan Burkholz's quote, where he said, we do not need another Flux framework.
[2639.06 --> 2641.34]  We have about 50,000 Flux frameworks.
[2642.48 --> 2642.74]  No more.
[2642.90 --> 2644.76]  That was, yeah, no more, he says.
[2644.84 --> 2649.76]  So that was kind of a shared opinion amongst JavaScript developers at that time.
[2649.76 --> 2652.32]  That was March of last year.
[2652.84 --> 2653.70]  Or March of this year.
[2654.24 --> 2658.48]  At which time, yeah, we were being overwhelmed with a new Flux implementation.
[2658.98 --> 2659.62]  Felt like daily.
[2660.96 --> 2663.42]  But there's lots of complexity there.
[2663.46 --> 2666.70]  It seems like Redux is just a simplified model.
[2667.48 --> 2674.02]  And having a single state object, similar to the way you think about your React components, right?
[2674.02 --> 2677.70]  Where you have a single root component, and it's just a tree of components.
[2677.94 --> 2684.90]  Now on your state, you just have one object, and that object is just an asset tree of other objects and what have you.
[2686.20 --> 2688.10]  Is that the biggest win, in your opinion?
[2689.12 --> 2694.36]  I think another really big win is that the testing is so much easier.
[2694.88 --> 2699.10]  I think this comes up every time I ask people, like, what do you like about Redux?
[2699.10 --> 2710.32]  People say testing, because it's not convenient to test the Flux stores, because they kind of depend on the dispatcher.
[2710.56 --> 2716.62]  And, you know, it's like banana gorilla problem where you want the banana, but you get the gorilla in the whole world.
[2716.84 --> 2717.92]  I never heard that before.
[2718.48 --> 2719.20]  Banana gorilla?
[2719.48 --> 2720.00]  Is that what it's called?
[2720.72 --> 2721.20]  Yeah.
[2721.54 --> 2724.20]  And this is a typical object-oriented problem.
[2724.20 --> 2728.60]  But in Redux, the reducers are just pure functions.
[2728.86 --> 2732.64]  So you can just import a single reducer that manages some part of your tree.
[2733.20 --> 2743.70]  And if you want to test it, you don't need any kind of, like, you don't need to set everything up to set up some marks.
[2743.70 --> 2751.08]  Or if you ever read the Facebook dispatcher kind of guide to test, then there is some stuff you need to do to make it work.
[2751.60 --> 2758.86]  But in Redux, you just call the function with some arguments, and you make assertions on its return value.
[2759.52 --> 2761.66]  And this is testing Redux.
[2762.00 --> 2765.24]  And, of course, not all parts are tested as easy as this.
[2765.74 --> 2767.62]  There are some parts that are harder to test.
[2767.62 --> 2771.72]  But most of your application logic lives in the reducers.
[2771.94 --> 2776.76]  And this is the part that is easiest to break because it's dealing with a lot of state.
[2777.46 --> 2779.66]  And this part is very easy to test in Redux.
[2779.98 --> 2781.36]  So this is another big win.
[2781.50 --> 2792.06]  I think I've started seeing a lot more testing in open source examples that use Redux than I saw in Flux using application examples.
[2792.68 --> 2793.42]  Very good.
[2793.42 --> 2799.98]  Well, I think this is just the first principle of three core principles that you state about Redux.
[2800.06 --> 2801.10]  We're going to take a quick break.
[2801.62 --> 2806.48]  And on the other side, we're going to dive more into the implementation and the principles of Redux.
[2807.26 --> 2814.00]  So our listeners can get a taste of not just the history and the why it exists, but even more of the how.
[2814.64 --> 2815.94]  So let's pause here.
[2816.02 --> 2818.78]  And on the other side, we'll talk about those three principles.
[2819.02 --> 2819.28]  Be right back.
[2819.28 --> 2849.26]  Thank you.
[2849.28 --> 2879.26]  Thank you.
[2879.28 --> 2883.68]  For your first $50,000 in transactions fee free.
[2883.88 --> 2887.16]  Go to BraintreePayments.com slash changelog.
[2887.16 --> 2891.50]  All right, we are back.
[2891.50 --> 2896.18]  Dan, I want to have you go through some of these principles of Redux.
[2896.18 --> 2902.52]  It's a small library, as you said, but it has a very intentional structure and opinions.
[2902.52 --> 2904.92]  And so I think the principles are very important.
[2904.92 --> 2913.96]  One we've talked about, that's the single source of truth, which is that the whole state of the application is in a single object tree within a single store.
[2914.54 --> 2919.58]  That also is a big differentiator from other Flux implementations where you have multiple state stores.
[2919.58 --> 2921.58]  You also have two other principles.
[2921.58 --> 2922.14]  You also have two other principles.
[2922.14 --> 2924.86]  State is read-only is your second principle.
[2924.98 --> 2927.76]  And the third one is changes are made with pure functions.
[2927.76 --> 2931.28]  Can you walk us through state is read-only and what that means?
[2932.16 --> 2932.76]  Yeah, sure.
[2932.76 --> 2935.42]  So this is what I took from Flux.
[2935.64 --> 2941.42]  And I think Flux really cleared my mind about how to write predictable code.
[2942.10 --> 2949.74]  Because before Flux, I was using Backbone and I had these models that were calling methods on other models.
[2949.74 --> 2955.54]  And if you can imagine a user object, a user can follow another user.
[2956.24 --> 2961.56]  And when the user begins this operation, you need to make it optimistically.
[2961.72 --> 2964.40]  You want to update the UI right away.
[2964.96 --> 2971.56]  So the method needs to change the count of followers and followees.
[2971.82 --> 2975.00]  And it needs to change the boolean fields on both objects.
[2975.36 --> 2977.40]  And then it needs to make the request.
[2977.40 --> 2980.04]  And if the request fails, it needs to roll them back.
[2980.44 --> 2986.88]  But if there is a concurrent request, you need to be careful to roll it back to correct value and so on.
[2986.92 --> 2990.68]  So it's very crazy with traditional MVC.
[2991.40 --> 2996.14]  And what Flux gave us is that Flux said, hey, you don't have setters.
[2996.78 --> 3000.26]  You don't actually, you don't change your objects.
[3000.38 --> 3002.66]  You don't put methods on them that change them.
[3002.66 --> 3008.34]  And instead, you've got this source of truth, which is multiple stores in Flux or single store in Redux.
[3008.66 --> 3015.28]  And you've got these actions, which are objects, plain JavaScript objects describing what you want to happen.
[3015.64 --> 3020.54]  Like user followed users, user followed user began.
[3021.00 --> 3022.24]  And you have two IDs.
[3022.40 --> 3025.40]  So this is an object describing the change.
[3025.40 --> 3039.20]  And after that, when the request comes through, you dispatch another action that says that user followed user success or failure with the IDs of these users.
[3039.20 --> 3051.38]  And so every change in the application, every mutation that you want to make to the street, you express it as a plain object describing what happened like a newspaper.
[3052.24 --> 3055.96]  So this is what Flux suggested.
[3056.20 --> 3058.94]  And this is also what I kept in Redux.
[3058.94 --> 3064.52]  So you want to actually react to the actions, of course.
[3065.22 --> 3071.26]  And in Flux, you register a callback in the store so it can change its internal state.
[3071.60 --> 3073.42]  But in Redux, you don't do that.
[3074.02 --> 3082.80]  In Redux, you just write a function that takes the current state, the action, and it returns the next state of your application.
[3083.24 --> 3085.36]  And this is the function we call the reducer.
[3085.36 --> 3089.54]  It's a pure function, so it cannot mutate the previous state.
[3089.96 --> 3097.80]  What it needs to do is to create a copy of the state that is updated according to this action.
[3098.40 --> 3101.84]  So the state is read-only, and you have these action objects.
[3102.64 --> 3105.26]  And the way that you change things is with pure functions.
[3105.28 --> 3108.20]  That's your third principle, which you call reducers.
[3108.32 --> 3110.14]  Can you explain reducers in more detail?
[3110.14 --> 3117.86]  Yeah, so the name reducer comes from array reduce method that is on every array.
[3118.56 --> 3121.68]  It's pretty standard in most functional languages.
[3122.10 --> 3124.22]  It's also called fault.
[3125.36 --> 3128.38]  Array reduce method, it accepts a callback.
[3128.92 --> 3133.06]  So this callback is what we call a reducer because it's an argument to reduce.
[3133.60 --> 3135.06]  But what is reduce?
[3135.06 --> 3141.56]  Array reduce is an operation that lets you create a single value out of multiple values.
[3142.04 --> 3151.42]  So you can use array reduce to calculate a sum of integers, for example, or to reverse a list,
[3151.90 --> 3157.52]  or to pretty much do any kind of accumulation over some kind of stream of values.
[3157.52 --> 3166.24]  And in case of Redux, the signature of the reducer is state and action.
[3166.80 --> 3170.88]  It accepts two arguments, state and action, and it returns the next state.
[3171.52 --> 3179.60]  So it's very similar to the signature of this callback, where it has accumulator value, and it returns the accumulator.
[3179.60 --> 3185.62]  So the state is being accumulated, and of course, in Redux, it is accumulated over time.
[3186.02 --> 3189.08]  You don't reduce really actions at runtime.
[3189.58 --> 3191.48]  But the conceptual model is very similar.
[3191.66 --> 3193.46]  So this is why we call them reducers.
[3194.12 --> 3198.38]  And there is just one reducer you need to specify when you create this draw.
[3198.80 --> 3202.20]  And usually in the docs, we call it the root reducer.
[3202.20 --> 3206.40]  But in reality, you want to keep your code modular.
[3206.82 --> 3212.40]  So you create reducers for every part of the state, and you can keep them nested.
[3212.84 --> 3221.48]  So you can have, for example, entities, reducer that manages all kinds of entities, like users, hosts, whatever.
[3222.06 --> 3224.26]  You can have a reducer that manages authentication.
[3225.04 --> 3227.48]  You can have reducer that manages routing.
[3227.48 --> 3232.66]  And all different stateful parts of your app can be managed by different reducers.
[3233.26 --> 3237.84]  And they are just combined to create this single root reducer that you give to Redux.
[3238.40 --> 3244.36]  So you have the single state object, and with larger applications, obviously, you have more state to manage.
[3245.16 --> 3248.48]  Your reducers are returning a new version of that state.
[3248.62 --> 3252.94]  So it's an immutable state that returns a new version after the changes have been applied.
[3252.94 --> 3264.30]  Any memory or performance issues with copying the same object over and over again and just minor modifications to it that you found?
[3265.16 --> 3271.28]  Yeah, I mean, it really depends on your application because there are some downsides in terms of memory.
[3271.76 --> 3279.62]  But then there are upsides in terms of you being able to figure out what needs to be re-rendered and what does not need to be re-rendered.
[3279.62 --> 3287.04]  Because if you have immutability, you can do reference check, reference identity check.
[3287.70 --> 3291.28]  And this is in Redux, it's enabled by default.
[3291.46 --> 3298.42]  So if you use React Redux bindings for React, it's never going to re-render something that has not changed.
[3298.42 --> 3315.80]  And because re-rendering is usually more expensive than creating a few objects, Redux has good performance benefits compared to some flux frameworks that are not, like, they don't have favor immutability.
[3315.80 --> 3320.06]  And this is exactly the reason OM is so fast.
[3320.34 --> 3331.42]  You know, there is the ClojureScript library called OM that pioneered the concept of a single state object and actually made people treat it seriously.
[3331.42 --> 3336.88]  David Nolan is the author of OM.
[3337.40 --> 3344.48]  And he wrote an article back then called The Future of JavaScript MVC Frameworks.
[3344.78 --> 3346.40]  And it's a pretty old post.
[3346.58 --> 3348.54]  It's been a couple of years since then.
[3348.90 --> 3352.10]  And David re-wrote OM a couple of times.
[3352.54 --> 3356.20]  And he's now working on OM Next, which is kind of similar to Relay.
[3356.20 --> 3359.90]  So it's, the world has since moved on.
[3360.60 --> 3368.80]  But it still explains why it's possible to have very fast applications despite immutability.
[3369.12 --> 3375.70]  And if you have performance problems, the first thing you can do is you can use a library like Commutable.js.
[3376.16 --> 3381.58]  So by default, we don't suggest you to do that because it's just easier to work with regular objects.
[3381.58 --> 3385.32]  And a lot of people don't want to learn two APIs at the same time.
[3386.20 --> 3389.04]  So we don't use Immutable.js in examples.
[3389.82 --> 3399.56]  But if you have performance problems because of very large lists and your dispatching, like 10 actions per second, which is probably a bad idea anyway.
[3400.16 --> 3402.34]  Like what kind of UI needs that?
[3402.34 --> 3405.28]  But if you do that, it's fine.
[3405.58 --> 3413.64]  But Immutable.js gives you immutable data structures that have structural sharing inside.
[3413.82 --> 3421.02]  And this is like implementation detail that makes them much more memory efficient because it's not a monolithic object.
[3421.02 --> 3426.52]  But under the hood, for example, an immutable array is some kind of tree.
[3426.74 --> 3428.28]  And I'm really bad at computer science.
[3428.36 --> 3429.52]  As I said, I've dropped out.
[3429.86 --> 3432.78]  But it's a tree of objects you don't really access.
[3433.28 --> 3442.08]  But if you make a copy that just adds a new value at the end of the array, the whole array is not actually being copied.
[3442.08 --> 3448.48]  It's just a new object is created that points mostly to that existing tree.
[3448.70 --> 3452.68]  And it has like another key that points to the part that you added.
[3453.28 --> 3455.36]  And they share the same memory.
[3455.62 --> 3459.00]  So they share the same tree when possible because they're immutable.
[3459.24 --> 3460.34]  They're not going to change later.
[3460.84 --> 3464.44]  This is why they're able to do that without performance problems.
[3464.44 --> 3467.98]  And this is how you can reduce memory usage with Redux.
[3468.40 --> 3470.46]  But really, you should profile your app.
[3470.56 --> 3472.66]  You should understand the trade-offs.
[3473.10 --> 3481.58]  You should build a prototype with the kind of amount of memory and speed that you want.
[3481.70 --> 3483.26]  And just stress test it.
[3483.36 --> 3485.00]  If it doesn't work for you, fine.
[3485.06 --> 3486.54]  You can use Flux or something else.
[3486.90 --> 3488.08]  If it works for you, it's great.
[3488.52 --> 3491.50]  And again, we don't force you to use immutability.
[3491.50 --> 3494.70]  Like, if you really want to, you can mutate things.
[3494.82 --> 3498.82]  It's just we don't encourage it until you know why you're doing it.
[3499.54 --> 3503.38]  And it's also possible to use many stores in Redux if you want to.
[3503.68 --> 3507.12]  Because at this point, it works exactly like Flux, right?
[3507.20 --> 3511.42]  You just have many stores and you can subscribe to different stores that you care about.
[3512.08 --> 3513.86]  And again, this is doable.
[3514.10 --> 3517.40]  This is just not something we encourage until you profile your app.
[3517.40 --> 3521.28]  And you know that this is something that will improve its performance.
[3521.50 --> 3522.80]  Because usually it's not.
[3523.78 --> 3524.12]  Very good.
[3524.20 --> 3532.98]  So let's change pace a little bit and talk about integrating a Redux into user interface libraries and frameworks.
[3533.74 --> 3536.68]  So obviously, it was built with React in mind.
[3537.24 --> 3539.70]  So it plays well with React.
[3540.00 --> 3540.86]  Let's start there.
[3540.86 --> 3546.52]  Maybe give a brief story of how you use Redux with React.
[3547.02 --> 3551.66]  And then I'll ask some questions about some other popular libraries for user interface stuff.
[3552.34 --> 3552.52]  Yeah.
[3552.68 --> 3560.62]  So initially, when I first wrote the first prototypes of Redux, it had React support built in.
[3560.62 --> 3562.28]  It depended on React.
[3562.28 --> 3568.48]  But early in the course, we decided this was silly because it is not related to React per se.
[3569.10 --> 3573.00]  And we can just make a separate binding library.
[3573.78 --> 3574.84]  So this is what we did.
[3574.98 --> 3576.66]  And it was a good decision in hindsight.
[3576.66 --> 3594.26]  And we have a library called React Redux that is officially supported, that is performant and made specifically to connect React components to Redux stores.
[3594.26 --> 3602.38]  With a specific philosophy approach to that, that I used to call it smart to dump components.
[3602.90 --> 3605.56]  But people don't like to call components dump.
[3606.30 --> 3613.28]  So now we call them container and presentational components so that components don't get offended.
[3614.56 --> 3622.42]  And container components are the components that are aware of Redux.
[3622.42 --> 3625.12]  They get the data from Redux store.
[3625.38 --> 3627.52]  They are subscribed to the Redux store.
[3628.10 --> 3631.38]  And usually they specify the behavior of your app.
[3631.46 --> 3633.10]  Like, what happens when I click that?
[3633.82 --> 3639.64]  And presentational components are usually not aware of Redux.
[3639.98 --> 3642.14]  They receive all the data by props.
[3642.86 --> 3650.46]  And if you want to move from Redux to something else, you can keep them and just change your container components.
[3650.46 --> 3657.92]  And React Redux actually provides you a helper called Connect that will generate the container components for you.
[3658.70 --> 3661.12]  So this is basically what React Redux offers.
[3662.20 --> 3662.52]  Very good.
[3662.60 --> 3665.14]  So let's say I don't want to use React.
[3665.42 --> 3668.66]  Maybe I prefer jQuery or Ember.
[3670.42 --> 3673.86]  If and how can you work with Redux in these other environments?
[3673.86 --> 3688.86]  So in case of jQuery, that would not be very useful because Redux assumes that it can give you the previous state of the app and the next state of the app.
[3688.86 --> 3695.28]  And you're somehow going to figure out how to re-render your app in response to the state change, no matter what changed.
[3696.08 --> 3705.82]  And if you write jQuery code, it's going to be problematic for you to actually check for every single field that might have changed and update the domain response.
[3706.32 --> 3709.22]  But this is exactly the problem that React is solving.
[3709.22 --> 3715.68]  So frameworks that have similar conceptual model to React work really well with Redux.
[3716.32 --> 3723.88]  And I know there's been an experiment to make it work with Ember, but I'm not sure if anyone supports it today.
[3724.54 --> 3733.26]  But I'm pretty sure people are using Redux with Angular, both the first version and the second version.
[3733.26 --> 3751.74]  And if you saw a post called Change Detection in Angular 2, which was like half a year ago maybe, it detailed that Angular is moving away from its previous model and is going to be more like React with top-down data flow.
[3752.52 --> 3759.62]  So this explains why Redux plays so well with Angular 2 and people are starting to use it together.
[3759.62 --> 3780.24]  Another advantage I think would fall out of having a single object for the state of the application is that if that object is serializable, which it probably should be, it seems like it would be pretty straightforward to be able to send that object from a server and basically boot your application into a state.
[3780.54 --> 3782.30]  Rehydration, I guess, is another term used.
[3782.66 --> 3785.32]  Is that something that Redux supports?
[3785.32 --> 3794.34]  Yeah, this was one of the other things I wanted to make sure is fixed in Redux.
[3794.34 --> 3815.48]  Because a lot of flux, some flux frameworks made this complicated, in my opinion, in terms of you had to implement separate methods to actually tell the stores how to hydrate and how to serialize and deserialize the state.
[3815.48 --> 3833.88]  And I felt like it's not really good to force this on developer because it's hard for developers to keep this up-to-date and to remember to change these methods anytime they change the state structure.
[3834.40 --> 3837.66]  So I really wanted this to be built in.
[3837.94 --> 3840.44]  And this is really simple in Redux.
[3840.44 --> 3849.10]  It is similar to how our Alt framework does it, although I think it's even simpler with a single store.
[3849.52 --> 3853.08]  But basically, you just create a store on the server for every request.
[3853.62 --> 3856.14]  You prefill it with the data you care about.
[3856.26 --> 3864.64]  Like you can dispatch async actions, make sure you fetch the data that is required for the first render on the server.
[3864.64 --> 3870.64]  And when it's done, you can just call then, use that promise then.
[3871.18 --> 3874.30]  And in the callback, you say that, okay, I'm ready to render.
[3874.48 --> 3878.42]  I'm just going to render my app with the state.
[3878.42 --> 3887.40]  And also, I'm going to call store.getStraight method to get the state object.
[3887.78 --> 3890.52]  And yeah, indeed, pass it down to the client.
[3890.76 --> 3895.44]  And then in the client, you just pass the state object as a second argument to create store.
[3895.66 --> 3899.94]  And boom, it got the state you get from the server.
[3899.94 --> 3901.60]  Very nice.
[3901.74 --> 3903.08]  That sounds pretty awesome.
[3904.68 --> 3905.24]  Let's see.
[3905.34 --> 3905.66]  What else?
[3905.74 --> 3914.74]  Any other major points of the architecture, the implementation, maybe even the ecosystem on Redux that you want to go into before we hit this next break?
[3914.82 --> 3926.14]  I know you did mention that you seem to be very intentional with trying to create or spawn an ecosystem for tools and extensions.
[3926.40 --> 3927.98]  Can you maybe touch on that?
[3927.98 --> 3928.30]  Yeah.
[3928.30 --> 3928.94]  Yeah.
[3929.36 --> 3934.22]  So what I realized is that I'm not going to have all the time in the world.
[3935.26 --> 3950.60]  And when I was using Flux, I really wanted to have some kind of extensions like recording, replay, that kind of stuff that is easily implementable outside the framework itself.
[3950.60 --> 3962.42]  But the problem was that either most Flux frameworks, they were not made to be extensible by default.
[3962.42 --> 3970.32]  So unlike Express framework, which did a great job at being extensible, this is why it's so popular and core on the server.
[3971.00 --> 3976.84]  On the client, Flux frameworks didn't offer compelling extension points.
[3976.84 --> 3979.62]  And they made decisions for you.
[3979.72 --> 3983.30]  For example, some frameworks embraced promises.
[3983.62 --> 3989.34]  And there was a built-in way to support dispatch and async actions with promises.
[3989.74 --> 3991.38]  And the framework would know what to do.
[3991.38 --> 4000.06]  But then somebody wants to use channels or observables or some other async abstraction that the Flux framework doesn't handle.
[4000.70 --> 4006.24]  Or its handling of promises gets in the way in some cases.
[4006.70 --> 4007.70]  And you don't want that.
[4007.70 --> 4013.14]  So I felt like I don't want to make these decisions for the users.
[4013.72 --> 4021.04]  I want to make the decisions that the users might not have enough context to make.
[4021.30 --> 4028.04]  Like I want to enforce purity, even if the users are not sold on the benefits of the purity yet.
[4028.04 --> 4033.32]  And I want to enforce that all changes happen through actions.
[4033.34 --> 4035.34]  Because this is important for me.
[4035.46 --> 4037.84]  This makes a lot of nice things possible.
[4038.06 --> 4039.90]  So these decisions I want to make.
[4040.38 --> 4046.38]  But I don't want to choose the async abstraction because people just use different abstractions.
[4046.46 --> 4050.62]  And I don't want to be the person who gets to decide here.
[4050.68 --> 4056.68]  I want to give the freedom to choose any abstractions complementary to Redux to the user.
[4056.68 --> 4060.70]  And we tried several ways of doing that.
[4060.94 --> 4071.42]  And this is exactly where Andrew Clark's help was so instrumental is that he designed the current API of middleware and store enhancers.
[4072.04 --> 4074.68]  And there is a lot of middleware for Redux.
[4075.00 --> 4077.60]  And I would say that some of it is pretty complicated.
[4077.92 --> 4080.22]  And I probably wouldn't do it that way.
[4080.62 --> 4084.46]  But people are still experimenting with what's possible, what makes sense.
[4084.46 --> 4091.00]  And there are some really nice examples of what I can do with middleware.
[4091.10 --> 4097.86]  Because it's just an extension pointing to Redux where you kind of override this for dispatch and action API.
[4097.86 --> 4100.14]  And you can do anything there.
[4100.36 --> 4107.86]  Like you can catch errors inside Redux and send them to error reporting service.
[4108.42 --> 4110.98]  Or you can support promises natively.
[4111.20 --> 4113.26]  Or you can support observables or channels.
[4113.62 --> 4119.16]  Or you can log every action with the middleware, with the logger middleware, and so on.
[4119.16 --> 4127.94]  So it's pretty awesome that people are working on this, are experimenting, and creating a lot of userland solutions through common problems.
[4127.94 --> 4130.44]  So we don't have to reinvent the wheel with every project.
[4131.32 --> 4131.58]  Very good.
[4131.64 --> 4133.86]  Sounds like a great place to take a break.
[4133.86 --> 4137.28]  On the other side, we'll talk about getting started with Redux.
[4137.96 --> 4142.44]  And of course, we have a good chance to shout out your free video series there, Dan.
[4142.92 --> 4148.04]  We also have a theoretical question for you about perhaps the grass being greener on a different side of the fence.
[4148.18 --> 4150.88]  So stay tuned for that, and we will be right back.
[4150.88 --> 4156.82]  Our friends at Linode are huge fans of the show, and they're excited to support what we're doing here at the ChangeLog.
[4157.12 --> 4165.32]  And they want to invite every single listener of the ChangeLog to try out one of the fastest, most efficient SSD cloud servers on the market.
[4165.88 --> 4172.04]  You can get a Linode cloud server up and running in seconds with your choice of Linux distro, resources, and also no location.
[4172.04 --> 4175.44]  And they've got eight data centers spread across the entire world.
[4175.88 --> 4180.74]  North America, Europe, Asia Pacific, and plans start at just $10 a month.
[4181.18 --> 4184.56]  They've got hourly billing with a monthly cap on all plans and add-on services.
[4185.18 --> 4190.64]  Get full root access for more control, run VMs, run containers, or even your own private Git server.
[4191.12 --> 4196.70]  Enjoy native SSD storage, 40-gigabit network, and Intel E5 processors on your servers.
[4197.32 --> 4199.72]  Use the code CHANGELOG10 with unlimited uses.
[4199.92 --> 4203.72]  Tell your friends it doesn't expire until December 31, 2016.
[4204.56 --> 4205.50]  That's next year.
[4205.96 --> 4208.22]  Head to linode.com slash changelog to get started.
[4208.60 --> 4209.72]  And now back to the show.
[4210.88 --> 4213.64]  All right, we are back with Dan Abramov.
[4213.74 --> 4214.70]  Dan, we're all excited.
[4215.00 --> 4216.56]  Redux sounds really cool.
[4217.26 --> 4219.74]  A lot of huge wins in using it.
[4220.38 --> 4222.56]  The question is, how do you get started?
[4223.04 --> 4226.68]  And I'm sure many of our listeners are wondering, what's the best way?
[4226.68 --> 4230.04]  Of course, there's many ways you can just start Googling, reading docs.
[4230.04 --> 4239.78]  But if you had brand new eyes and you're coming to Redux as a potential user, what were the first steps that you would take to get started on your way to success?
[4240.46 --> 4241.16]  Great question.
[4241.16 --> 4248.78]  I think I would start with watching my video series, which I created exactly for this purpose.
[4248.78 --> 4254.98]  I watched people learn Redux for a couple of months by now.
[4254.98 --> 4263.34]  And I've seen people making the same kind of mistakes or the same kind of misunderstandings of Redux.
[4263.52 --> 4268.78]  And people missed out on some powerful patterns that Redux offers.
[4268.78 --> 4279.36]  So I was contacted by the guys from Eckhet, which is an awesome video tutorial site.
[4280.06 --> 4282.08]  They've got free and paid videos.
[4283.30 --> 4293.52]  And I think initially they just contacted me to record something about hotel ordering, but I never got to do it.
[4293.52 --> 4303.84]  And they sent me the equipment, the mic I'm talking to right now is actually their present to me, so to say, their investment.
[4304.34 --> 4310.94]  And I kept saying like, yeah, guys, I know I feel so bad about it, but yeah, I'll get around to doing something.
[4311.58 --> 4315.76]  And later Redux came out and a lot of people requested Redux tutorials.
[4315.76 --> 4328.24]  And Joel was, and a lot of people inside Eckhet who work for Eckhet, who record videos for Eckhet, wanted to do Redux tutorials.
[4328.46 --> 4332.20]  But Joel insisted that, hey, we need to give Dan some time.
[4332.60 --> 4333.56]  He's going to do it.
[4334.10 --> 4335.42]  Let him be the first.
[4335.54 --> 4342.18]  And I'm very grateful to Joel for this opportunity and for bearing with me for so many months.
[4342.18 --> 4351.34]  But anyway, it was November and I previously I raised some money to work on React loader and Redux for three months.
[4351.66 --> 4360.34]  And I actually saved it up a little bit so I could work one more month without doing any full-time job before joining Facebook.
[4360.34 --> 4376.64]  And I decided to dedicate this time to creating a bunch of tutorial videos that are targeted at people who kind of, who know JavaScript, but they may not be experts.
[4376.64 --> 4381.52]  And who know some React, but not much more than that.
[4382.16 --> 4390.42]  And who are curious how to build a simple application with Redux without prior Flux experience.
[4391.08 --> 4394.60]  So I recorded 30 lessons over the course of a month.
[4394.80 --> 4398.18]  They are bite-sized, like three or four minutes each.
[4398.70 --> 4402.34]  And they touch on the concepts I think are the most important.
[4402.94 --> 4403.84]  I'm very sorry.
[4403.98 --> 4405.06]  It's a to-do app.
[4405.06 --> 4409.00]  I'm building a to-do app during this tutorial.
[4409.94 --> 4416.60]  But I actually, yeah, I know some people hated it, but I get a lot of great feedback.
[4417.16 --> 4425.72]  And personally, I think to-do app is the best medium for explaining how to structure state mutations in some kind of framework.
[4425.72 --> 4433.02]  And of course, my video series, it doesn't touch on asynchronous requests yet.
[4433.14 --> 4434.80]  And a lot of people were sad about it.
[4434.80 --> 4441.10]  But we really need solid foundations before you can jump to making async requests.
[4441.10 --> 4455.66]  So if you're looking for a solid understanding of Redux fundamentals, of Redux patterns, and in fact, of how Redux is implemented, because in some lessons I just show how you can implement this Redux function in 10 lines.
[4455.66 --> 4458.66]  It's a great way to start.
[4458.66 --> 4463.40]  And these tutorials, they are free and they will be free.
[4463.40 --> 4468.40]  This is something I wanted to give back to community before joining an entire company.
[4469.28 --> 4472.40]  So, yeah, I think you should check those out.
[4472.58 --> 4486.38]  And if you like them, feel free to buy a subscription to say thank you to the people who gave me the opportunity to actually work on that and host it for free and who gave me the equipment, of course.
[4486.38 --> 4486.82]  Yeah.
[4486.82 --> 4489.94]  So, this is a good start.
[4490.22 --> 4494.54]  And after that, I think you're prepared enough to work through the docs.
[4495.02 --> 4501.72]  The basic parts of the docs is pretty much the same we cover in these video tutorials.
[4502.12 --> 4503.70]  But there is the advanced section.
[4503.84 --> 4504.82]  It covers asynchronous.
[4505.68 --> 4507.44]  It covers middleware.
[4507.90 --> 4509.78]  So this is something you want to read after that.
[4510.42 --> 4512.82]  And you should check out some...
[4512.82 --> 4522.26]  I have an ecosystem page in the docs that links to great articles, tutorials, examples that I personally vetted.
[4522.60 --> 4523.78]  These are really good.
[4524.62 --> 4527.30]  So I recommend you look at them.
[4527.86 --> 4530.42]  And I want to highlight one example in particular.
[4530.64 --> 4532.96]  It's called Sound Redux.
[4532.96 --> 4545.00]  And this is just a SoundCloud client built by a guy called Entry that is built on top of Redux.
[4545.18 --> 4551.72]  And it's not a lot of code, but it gives a pretty good idea of how a real-world Redux application is structured.
[4551.72 --> 4557.72]  The to-do application, is that the same one that you used in the presentation for your...
[4558.60 --> 4560.02]  What was it before, Jared?
[4560.14 --> 4563.88]  Was it a conference talk as something development, basically?
[4564.02 --> 4568.28]  Was it the hot reloading talk you gave at React Europe in 2015, this year?
[4569.14 --> 4570.36]  No, not exactly.
[4570.38 --> 4570.98]  Not the same one?
[4571.42 --> 4578.88]  No, it's just in the conference, I just wrote part of the to-do app live at the conference, which is pretty great.
[4578.88 --> 4579.50]  That was really cool.
[4579.58 --> 4580.08]  I like that.
[4580.08 --> 4583.72]  It was nice to see you break your own code and be like, where is it?
[4583.78 --> 4584.48]  Okay, here it is.
[4584.66 --> 4586.42]  And you kind of walked everybody through it.
[4586.66 --> 4593.56]  You kind of see this, your mind unfolding on how you're pulling back the data from different objects and stuff like that.
[4593.60 --> 4594.46]  It's pretty interesting.
[4594.66 --> 4595.14]  I like that.
[4596.12 --> 4609.62]  Yeah, but this one, actually, I think in the video tutorials, I show some things that I did not think about completely when I was writing the docs.
[4610.08 --> 4623.26]  So tutorials are actually a better source right now than the docs because I changed the way I recommend to build React Redux applications a little bit for the tutorials.
[4623.26 --> 4624.44]  Cool.
[4624.44 --> 4633.56]  And as you could tell, we did a bit of research to kind of dig into this call with you and just searching on YouTube for your name.
[4633.66 --> 4636.00]  And then also Redux was very helpful.
[4636.18 --> 4642.68]  And upon that journey, I stumbled upon this kind of pulling different ideas together that you shared.
[4642.68 --> 4649.78]  It seems like you're all for functional programming in JavaScript versus something like Elm or ClojureScript.
[4650.46 --> 4659.10]  And it sounded to me like you were advocating more like go down the Redux path and functional programming in JavaScript versus these other functional languages.
[4659.30 --> 4661.82]  Can you talk a bit about your thoughts and opinions on that?
[4661.82 --> 4663.42]  I wouldn't say that.
[4664.08 --> 4666.06]  I mean, you really should.
[4666.42 --> 4669.74]  And this is me giving an advice that I don't follow.
[4670.20 --> 4672.06]  So you probably shouldn't pay attention.
[4672.54 --> 4680.52]  But I think you should go out of your way to use different things that exist elsewhere, like ClojureScript and Elm,
[4680.52 --> 4689.08]  just to get a sense of these ideas and how different constraints can make these ideas work.
[4689.48 --> 4695.74]  Because a lot of Elm's ideas work so great because in Elm, you have a completely static typing.
[4696.12 --> 4697.22]  It is completely pure.
[4697.76 --> 4701.92]  So it is a different environment from JavaScript, a very different environment.
[4701.92 --> 4710.12]  And if you want to enforce similar things, you start thinking like, can I bring these constraints in some way to JavaScript?
[4710.60 --> 4711.66]  Or even should I?
[4712.00 --> 4718.86]  Or should I take advantage of JavaScript's powerful sites that these constraints eliminate?
[4719.48 --> 4724.74]  So you should definitely check out those projects, those different languages.
[4724.74 --> 4731.22]  And if you like them, of course, you should use them and collaborate them.
[4731.84 --> 4734.46]  And there are many Elm enthusiasts out there.
[4734.54 --> 4735.04]  I know that.
[4735.66 --> 4739.40]  But what I'm saying is that please let us know.
[4739.94 --> 4747.62]  Like, if you find some really neat pattern or some really nice way to build UI applications,
[4747.62 --> 4756.32]  and you only share it with your language community, and you don't really speak about it at JavaScript conferences,
[4757.14 --> 4761.12]  it's a problem for us, and it's sad for us.
[4761.60 --> 4766.80]  And I think you should go out of your way to evangelize the good things you learn elsewhere.
[4767.48 --> 4773.08]  And maybe somebody will get inspired by your talk and build something cool in JavaScript,
[4773.22 --> 4774.64]  even if you don't work in JavaScript.
[4774.64 --> 4783.20]  And of course, people like David Nolan and Evan and pretty much everywhere in ClojureScript and Elm ecosystem are doing exactly that.
[4783.62 --> 4784.78]  So big thanks to them.
[4785.76 --> 4786.96]  Let me ask you this.
[4787.02 --> 4792.26]  So you've poked your head up from your Sublime Text, and you're surveying the ecosystem,
[4792.46 --> 4794.42]  and you're seeing cool things that Elm is doing.
[4794.92 --> 4797.74]  And you're seeing cool things with Ohm in ClojureScript.
[4797.74 --> 4808.62]  These other languages, functional languages, building very similar type apps that Redux and React are building.
[4809.42 --> 4817.34]  And do you ever think, well, maybe I should just go hop in that pool and see if the water really is warm?
[4817.84 --> 4820.24]  Or do you always come back to JavaScript?
[4820.24 --> 4821.84]  And if the latter, why?
[4821.92 --> 4822.82]  What brings you back?
[4823.38 --> 4825.84]  Why aren't you saying, wow, Elm is amazing.
[4825.94 --> 4828.46]  I'm going to hop in all in on Elm?
[4828.46 --> 4831.78]  I think it's practical concerns.
[4832.00 --> 4834.54]  And I'm not saying that Elm is impractical.
[4834.70 --> 4840.58]  In fact, the opposite, because I know that some large applications are being built in Elm right now.
[4840.96 --> 4847.18]  And you should check out Richard Fieldman, I believe, who is advocating a lot for Elm.
[4847.30 --> 4851.64]  And he's writing a blog about how they use Elm in production.
[4851.64 --> 4860.78]  So if you're a small startup that is willing to try something like this, it's an amazing learning opportunity.
[4861.14 --> 4871.12]  So if I went back three years ago and I was offered a job doing Elm, I would take it.
[4871.12 --> 4881.44]  Even if I didn't know Elm, just because it's a very vibrant community and it feels like they are doing a lot of right things.
[4881.84 --> 4887.10]  But I can't do that right now because now I'm working for a big company.
[4887.84 --> 4893.20]  And before I used to just do a lot of projects in React ecosystem and I was busy with my own projects.
[4893.46 --> 4899.74]  I was busy with supporting them and I can't really go ahead and do something else and abandon everyone.
[4899.74 --> 4903.30]  So it's just not something I can do right now.
[4903.40 --> 4904.68]  But I'd like to try it.
[4904.96 --> 4905.10]  Yep.
[4905.86 --> 4907.30]  So the man's getting you down.
[4908.10 --> 4908.26]  Yeah.
[4908.60 --> 4910.90]  But it's fun.
[4911.88 --> 4914.44]  There is so much learning in JavaScript world too.
[4914.74 --> 4915.18]  Absolutely.
[4915.32 --> 4916.44]  It's moving so fast.
[4916.92 --> 4917.22]  Yeah.
[4917.44 --> 4922.90]  So I'm actually counting on JavaScript in terms of good ideas.
[4922.90 --> 4926.82]  It feels like good ideas are surfacing in JavaScript eventually.
[4926.82 --> 4932.44]  So it's a bit slower, but it's worth looking at too.
[4933.26 --> 4936.92]  Well, we are getting to that time of our closing questions.
[4937.04 --> 4942.16]  Jared, is there anything else you wanted to cover before we tail out and start asking some of our closing questions?
[4942.58 --> 4950.16]  No, I'm super excited to hear about Dan's open source radar considering he seems to have his thumb on the pulse.
[4950.40 --> 4950.54]  Yeah.
[4950.56 --> 4951.22]  Let's start there then.
[4951.22 --> 4955.82]  And so Dan, the question basically is what's on your open source radar?
[4956.12 --> 4961.10]  You can also flavor that as language radar, pattern radar, library radar.
[4961.36 --> 4965.12]  You know, what's out there that maybe you haven't had a chance to touch or play with yet?
[4965.16 --> 4968.12]  And if you had a weekend, what would it be that you play with?
[4968.12 --> 4969.12]  Okay.
[4969.48 --> 4976.80]  So don't count on this being too interesting because I haven't been keeping up with what's happening lately.
[4977.62 --> 4984.72]  But I'd say I'm really excited about some lower level languages because I'm a higher level language person.
[4985.24 --> 4992.72]  And I'm always feeling like I don't know anything when I speak to people who are low level.
[4992.72 --> 5003.16]  So I'm pretty excited about languages like Rust and Swift that are more low level, but not as painful to work with as C.
[5003.58 --> 5005.60]  So they have some functional niceties.
[5006.34 --> 5012.26]  And if I had some time, I definitely played with some lower level language like Rust.
[5012.26 --> 5025.50]  And in terms of JavaScript frameworks, you probably heard that anyway, but I'm excited about Rx reactive extensions, which have been rewritten right now.
[5025.62 --> 5027.30]  There is Rx 5 beta.
[5027.94 --> 5035.04]  It's currently developed by Netflix mostly because they use it a lot.
[5035.04 --> 5045.20]  And Ben has done an amazing job of figuring out what needs to go into this release because it's a bit different from all previous releases.
[5045.82 --> 5047.40]  And it's very performant.
[5048.02 --> 5050.08]  They are focusing on performance a lot.
[5050.72 --> 5060.38]  And if there is one pattern, if you know promises, but you don't know observables, you are doing yourself a disservice.
[5060.38 --> 5065.46]  So you should go ahead and read about Rx, read about observables.
[5065.68 --> 5069.56]  Don't confuse them with Ember observables or KVO.
[5069.84 --> 5071.54]  This is not about key value observation.
[5072.04 --> 5077.42]  This is about observable pattern and reactive programming.
[5077.66 --> 5080.98]  It's very interesting and helpful, even if you don't plan to do that.
[5080.98 --> 5089.94]  And then there is a framework called Cycle developed by Andre Stalt.
[5090.54 --> 5095.14]  And again, if you followed my Twitter, you probably already heard of that a thousand times.
[5095.34 --> 5096.16]  But it's interesting.
[5097.30 --> 5103.30]  It's like bringing a Haskell-like approach to UI, to JavaScript.
[5103.30 --> 5110.26]  Keeping side effects at the edges of your application is something that he calls drivers.
[5111.32 --> 5115.78]  And your whole UI logic is built on observables.
[5115.94 --> 5122.32]  So you specify how observables of user input map to observables of the virtual DOM.
[5123.16 --> 5127.04]  And I'm not saying this is the future, but it's really interesting.
[5127.26 --> 5128.60]  It's something you should check out.
[5128.60 --> 5133.48]  And of course, Elm, I already said that Elm is an interesting language.
[5134.08 --> 5140.42]  You should watch Evan's talks about Elm and how he tries to make it user-friendly in terms
[5140.42 --> 5145.34]  of compilation errors, in terms of the development experience.
[5146.26 --> 5148.60]  This is really illuminating and interesting.
[5149.48 --> 5151.18]  So Elm is a good one.
[5151.94 --> 5157.32]  Other than that, I'm not sure I have something to say because I haven't been giving up.
[5157.32 --> 5159.82]  No, I think you said plenty.
[5159.96 --> 5162.66]  I think you've been keeping up more than you gave yourself credit for.
[5163.26 --> 5168.98]  Quick note, if you are interested in Rust, check out episode 151, where we had Steve and
[5168.98 --> 5173.74]  you, the cats, on the show, all around the Rust language.
[5174.24 --> 5177.56]  In fact, we had a nice tweet about that recently.
[5178.10 --> 5179.28]  Somebody who loved that show.
[5180.16 --> 5181.28]  Let's see if I can find it.
[5181.36 --> 5181.58]  Yes.
[5181.66 --> 5182.20]  So here we are.
[5182.26 --> 5183.14]  Real-life retweet.
[5183.14 --> 5187.64]  Olivier Morel says, nice interview by Changelog about hashtag Rustlang.
[5188.20 --> 5190.70]  Could give it a try in the following week's smiley face.
[5190.86 --> 5191.50]  So there you have it.
[5193.00 --> 5194.36]  My first ever real-life retweet.
[5194.86 --> 5195.66]  Check out that show.
[5195.96 --> 5196.82]  Next question for you, Dan.
[5196.86 --> 5199.48]  And the final one is programming hero.
[5199.48 --> 5207.36]  So do you have somebody who inspires you or you look up to a mentor, a hero that you would
[5207.36 --> 5211.14]  like to give a shout out to on the show and tell us why they are your programming hero?
[5211.82 --> 5212.48]  Yeah, sure.
[5212.74 --> 5220.44]  Although I think we have a little unhealthy obsession with personalities in JavaScript,
[5220.44 --> 5227.64]  the world and elsewhere in programming because people, and me included, we learn different
[5227.64 --> 5235.60]  things because we have the privilege to actually, like I said, I was able to not pay my rent
[5235.60 --> 5240.32]  because my mom did that and my grandma bought me the books and I could afford to drop out
[5240.32 --> 5243.62]  of the college and not worry about the job for some time and so on.
[5243.62 --> 5252.04]  So this privilege accumulates and I don't think it's very healthy to say like, hey, these people
[5252.04 --> 5252.70]  are heroes.
[5253.12 --> 5256.88]  Let's put them on t-shirts and everywhere and worship them.
[5257.34 --> 5258.98]  I don't advocate them.
[5259.64 --> 5266.42]  But I think for me, the people I look up to, there are several of them.
[5266.90 --> 5271.30]  Some of them are from React team because I like React a lot.
[5271.30 --> 5279.98]  And one of them is Jordan, Jordan Walker, I'm not sure, who actually came up with React.
[5280.30 --> 5283.56]  And despite people saying like, this is a crazy idea, it's not going to work.
[5284.50 --> 5295.84]  He was just persistent enough to keep trying to, you know, make it something that, to prove
[5295.84 --> 5302.76]  that this concept, this declarative rendering is actually useful and this crazy, dumb, different
[5302.76 --> 5303.60]  idea can work.
[5304.12 --> 5306.66]  And so this is something I really admire.
[5306.86 --> 5313.82]  And he's doing some really interesting experiments at Facebook that you can't really see if you're
[5313.82 --> 5314.60]  not working at Facebook.
[5314.80 --> 5317.10]  So there is another benefit of working at Facebook.
[5317.32 --> 5318.54]  You can see Jordan's stuff.
[5318.54 --> 5327.22]  And I also look up to Sebastian Markbager, who's one of the core React team members, because
[5327.22 --> 5333.56]  he's just so, he's very, he's very, he's engaging with the community.
[5334.18 --> 5340.40]  And he's, he has a high, very high level vision of the project.
[5340.40 --> 5344.74]  But on the other hand, he also dives into very low level details.
[5345.20 --> 5354.56]  And he cares a lot about the APIs and how to not force the users to learn functional concepts,
[5354.84 --> 5360.90]  but gradually teach them and provide escape hatches in case where we can't educate them
[5360.90 --> 5362.38]  enough or we don't know enough.
[5362.38 --> 5370.56]  So this compassionate kind of way to develop open source software is something I think
[5370.56 --> 5376.36]  I, I, I was inspired by Sebastian in how he does that.
[5377.02 --> 5386.98]  And if I had to pick another person I admire, I think that would be Steve, Stephen Klubnik,
[5386.98 --> 5392.28]  I think from the Rust community, because he's just so nice on Twitter.
[5393.56 --> 5400.08]  He, he reminds me that software is mostly about people and solving people's problems
[5400.08 --> 5406.58]  and not about the code or the kind of, you know, of course it is about the code,
[5406.68 --> 5408.76]  but it's the code to solve people's problems.
[5408.98 --> 5410.66]  And so community comes first.
[5411.50 --> 5415.48]  Well, Dan, we've had a fun, long, deep conversation with you,
[5415.48 --> 5420.18]  not only about your roots, where you came from, but also some of the inspirations that
[5420.18 --> 5426.72]  led to creating Redux and all the work you've been doing to get to work at Facebook.
[5427.14 --> 5434.04]  And I want to rewind kind of a sort of a bit and just re-mention this unique path you took
[5434.04 --> 5440.42]  to pitch a talk that you didn't quite have fully ready, this tutorial fully ready.
[5440.64 --> 5441.58]  You got that.
[5441.64 --> 5444.76]  And that was a big ticket to one, being able to afford to go to that conference.
[5444.76 --> 5451.60]  And two, being able to be, to have the visibility to Facebook and get to this job that you now have.
[5451.64 --> 5455.32]  So I think that's really inspiring to the listening audience thinking like,
[5455.64 --> 5460.52]  if you want to make it, you just kind of have to hack your way there and get there by any means necessary.
[5460.82 --> 5463.30]  So I got to applaud you on, on that front.
[5463.34 --> 5467.88]  Is there anything that, any advice, anything you want to share back to the audience as we close out the show?
[5467.88 --> 5472.84]  I think it's really important to find your audience.
[5472.84 --> 5485.24]  This is in relation to what I said with regards to finding the ecosystem, a young ecosystem where you can make impact.
[5485.80 --> 5487.46]  So this is what worked for me.
[5487.56 --> 5497.82]  I found an ecosystem where my work can yield some impact because it's just, there's just so little stuff that my work can be valuable.
[5497.82 --> 5503.28]  And when you do that, you have an opportunity to gain the audience.
[5503.52 --> 5506.98]  And I think this is what was really important to me.
[5507.12 --> 5508.28]  I got a Twitter account.
[5508.60 --> 5509.74]  I started tweeting.
[5510.00 --> 5516.16]  I started writing some Medium articles, sharing what I found, what I learned.
[5516.16 --> 5519.48]  And the audience kept growing.
[5519.72 --> 5521.46]  And this helped me with everything.
[5521.64 --> 5529.42]  This helped me with the connections, with being on the conference, with getting here in the UK.
[5530.16 --> 5535.30]  So find the ecosystem, find the audience and share your work.
[5535.64 --> 5539.96]  If you can, I mean, not everybody has the privilege to be able to do that.
[5539.96 --> 5546.06]  But if you can, it's a good way to have a better job in the future.
[5546.86 --> 5547.10]  Well said.
[5547.18 --> 5547.60]  Well said.
[5548.42 --> 5550.54]  Well, thank you, Dan, for joining us.
[5550.62 --> 5554.34]  And thanks also to our wonderful listeners who listen every single week to this show.
[5554.42 --> 5555.62]  We ship this show on Fridays.
[5556.90 --> 5559.32]  And also to our members who support us.
[5559.56 --> 5567.02]  If you're out there and you're thinking, man, I love the ChangeLog and I want to support what they're doing, you can go to changelog.com slash membership and join the community for just 20 bucks a year.
[5567.02 --> 5569.60]  And we'll give you an all-access pass to everything we do.
[5569.76 --> 5571.48]  It's access to our members in Slack room.
[5572.10 --> 5576.04]  Exclusive discounts we get from our favorite products, a.k.a. our trusted partners.
[5577.00 --> 5579.94]  We also give you half off of our super awesome ChangeLog T.
[5580.02 --> 5581.62]  Who would want to hack in a ChangeLog T, Jared?
[5581.66 --> 5582.04]  I don't know.
[5582.18 --> 5582.64]  That's crazy.
[5583.38 --> 5584.40]  Pretty much all I wear, bro.
[5584.60 --> 5584.84]  I know.
[5584.98 --> 5585.98]  That's what I'm wearing right now.
[5586.06 --> 5586.70]  It's comfy.
[5587.50 --> 5589.68]  But, Dan, again, thanks so much for joining us.
[5589.74 --> 5593.20]  I also want to say thanks to our awesome sponsors for supporting this show.
[5593.70 --> 5595.40]  Today's show is sponsored by CodeShip.
[5595.40 --> 5599.04]  TopTile, Braintree, and also Linode.
[5599.80 --> 5601.36]  But that's the tail end of the show.
[5601.50 --> 5603.32]  So, everyone, let's say goodbye.
[5603.80 --> 5604.08]  Goodbye.
[5604.30 --> 5604.68]  Thanks, Dan.
[5605.08 --> 5605.50]  Bye-bye.
[5605.72 --> 5606.58]  Thank you for having me.
[5607.40 --> 5608.40]  Bye-bye.
[5608.40 --> 5609.40]  Bye-bye.
[5609.40 --> 5610.40]  Bye-bye.
[5610.40 --> 5611.40]  Bye-bye.
[5611.40 --> 5612.40]  Bye-bye.
[5612.40 --> 5613.40]  Bye-bye.
[5613.40 --> 5614.40]  Bye-bye.
[5614.40 --> 5615.40]  Bye-bye.
[5615.40 --> 5616.40]  Bye-bye.
[5616.40 --> 5617.40]  Bye-bye.
[5617.40 --> 5619.40]  Bye-bye.
[5619.40 --> 5620.40]  Bye-bye.
[5620.40 --> 5621.40]  Bye-bye.
[5621.40 --> 5622.40]  Bye-bye.
[5622.40 --> 5623.40]  Bye-bye.
[5623.40 --> 5624.40]  Bye-bye.
[5624.40 --> 5625.38]  Bye-bye.
[5625.70 --> 5627.40]  Bye-bye.
[5627.40 --> 5629.62]  Give me a pois' to us.
[5629.62 --> 5630.78]  Bye-bye.
[5630.78 --> 5631.50]  Bye.
[5631.50 --> 5631.96]  Bye.
[5631.96 --> 5632.30]  Bye-bye.
[5632.30 --> 5633.42]  Bye-bye.
[5633.48 --> 5634.20]  Bye-bye.
[5634.28 --> 5635.68]  Bye-bye.
[5641.08 --> 5641.68]  Bye-bye.
[5641.76 --> 5643.62]  Bye-bye.
[5643.62 --> 5644.08]  Bye-bye.
[5644.08 --> 5645.76]  Bye-bye.
[5645.76 --> 5645.90]  Bye-bye.
[5645.90 --> 5646.16]  Bye-bye.
[5646.16 --> 5646.88]  Bye-bye.
[5646.88 --> 5647.24]  Bye-bye.
[5647.24 --> 5648.24]  Bye-bye.
[5648.24 --> 5648.68]  Bye-bye.
[5648.68 --> 5649.12]  Bye-bye.
[5649.12 --> 5650.30]  Bye-bye.
[5650.30 --> 5651.42]  Bye-bye.
[5651.48 --> 5652.04]  Bye-bye.
[5652.04 --> 5652.36]  Bye-bye.
[5652.42 --> 5653.86]  Bye-bye.
[5653.86 --> 5654.60]  Bye-bye.
