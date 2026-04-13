[0.00 --> 11.32]  Let's do it. It's Go Time.
[11.82 --> 17.80]  Welcome to Go Time, your source for diverse discussions from all around the Go community.
[18.38 --> 24.78]  Connect with us on Mastodon at GoTime at changelog.social, on Twitter at GoTimeFM,
[24.78 --> 29.80]  and follow Changelog on YouTube for clips and highlights from all of our pods.
[30.24 --> 33.64]  Head to youtube.com slash changelog and subscribe today.
[33.94 --> 38.54]  Big thanks to our partners at Fastly for ensuring Go Time reaches you super fast all around the world.
[38.74 --> 40.64]  Check them out at Fastly.com.
[40.88 --> 47.40]  And to our friends at Fly, host your app servers and database close to your users, no ops required.
[47.92 --> 50.04]  Learn more at fly.io.
[50.44 --> 51.62]  Okay, here we go.
[51.62 --> 60.44]  So today we have a very exciting episode.
[60.74 --> 62.38]  I am personally excited about that.
[62.46 --> 63.44]  I think you can hear that.
[63.96 --> 70.04]  We will be talking more about hacking with Go, but this one will be with the angle of AI.
[71.00 --> 73.58]  And yes, today is March 14th.
[73.58 --> 74.54]  Today we're recording this.
[74.54 --> 76.78]  GPT-4 was just announced a couple of hours ago.
[76.92 --> 79.90]  So this is what we were talking about at the soundcheck before we started.
[80.36 --> 81.04]  This and breakfast.
[81.74 --> 83.64]  I am joined by Joni.
[83.70 --> 84.12]  Hi, Joni.
[84.18 --> 84.62]  How are you doing?
[85.08 --> 85.86]  I'm doing well.
[85.94 --> 86.58]  Good to be here.
[86.82 --> 88.18]  It's always nice to co-host together.
[88.64 --> 89.34]  It is indeed.
[89.34 --> 96.36]  And we have two awesome guests that this is their appearance number 7755 in our show.
[96.84 --> 101.00]  And we're always happy that you're back to tell us more interesting things about hacking.
[101.92 --> 106.46]  Ivan and Jags, would you gentlemen like to introduce yourselves?
[107.16 --> 107.34]  Okay.
[107.42 --> 107.76]  All right.
[108.04 --> 109.32]  So hello, everyone.
[109.58 --> 111.08]  It's nice to be back on the podcast.
[111.76 --> 117.50]  My name is Ivan Kwiatkowski and I'm a French cybersecurity researcher and I work for Kaspersky.
[117.50 --> 121.42]  My name is Juan André Herrero Sade, which is why Jags is fine.
[121.98 --> 125.48]  And I am senior director at Sentinel Labs.
[126.16 --> 135.04]  So you both are hackers who are not using Go in your everyday life, but you have come across Go in your cybersecurity adventures.
[135.88 --> 139.14]  And you have interesting things to tell us about that.
[139.56 --> 144.08]  So maybe we will start with the latest malware that was written in Go.
[144.38 --> 145.34]  There's quite a bit of it.
[145.82 --> 146.08]  Yes.
[146.22 --> 146.80]  Please tell us.
[146.80 --> 152.94]  Like, honestly, it's, uh, I didn't think it would be this widely adopted at first for a malware.
[153.58 --> 154.84]  Uh, most mal, okay.
[154.86 --> 157.32]  So we got to kind of split it up a little bit, right?
[157.32 --> 160.68]  Like a lot of malware devs, in my opinion, are in two categories.
[160.68 --> 166.44]  You either have like the old school VXers, as we used to call them that are, you know, using C, maybe C++.
[166.44 --> 178.58]  And the more you go like higher levels of nation state sponsored guys, like you're very likely to deal with, you know, guys and gals that are writing with C++ and these sort of, uh, very well-established frameworks that you can imagine.
[178.58 --> 182.72]  Like a defense contractor was involved with building, there's quality assurance to it, etc.
[182.72 --> 194.46]  Or you get people who are just using like compiled Python or like some, you know, visual basic, uh, auto IT, like really kind of garbage attempts at just sort of stealing things quickly.
[194.46 --> 208.80]  And then now we see like Go and Rust picking up, but mostly Go in my opinion, which I'm, I'm actually grateful that it's not as much Rust, but I don't think you, a lot of you would be impressed with the caliber of stuff that you find in the wild.
[209.14 --> 216.50]  There's definitely a lot of great red team tooling, which thankfully is not being used quite as much in the wild yet, but it's out there, right?
[216.58 --> 223.18]  So Go is becoming kind of like an essential desirable platform for malware developers, I suppose.
[223.18 --> 225.40]  Remind us what does red team mean?
[225.60 --> 226.18]  Oh my God.
[226.32 --> 226.94]  Yeah, sorry.
[227.00 --> 228.30]  I'm totally out of my element here.
[228.40 --> 244.00]  So normally we tend to define folks in the cybersecurity space under a few different colored hats, but red teams are usually the penetration testers, people doing quote unquote offensive operations, but in a controlled environment, right?
[244.00 --> 247.42]  So you might hire them for your fortune 500 company.
[247.66 --> 252.90]  They come in, they break in, you know, they hack into it just for the sake of showing you look, there's all these vulnerabilities.
[252.90 --> 254.42]  Everything is set up really poorly.
[254.66 --> 255.52]  This is how you fail.
[255.96 --> 259.38]  And then you have the blue teamers who, you know, might be doing the network defense.
[259.56 --> 270.12]  And I think we vaguely fit into the blue team side of things, but more because we're, I guess, like doing AV signatures and reverse engineering and hunting for malware.
[270.12 --> 274.00]  But I guess Ivan and I are kind of like weird ducks in that space.
[274.18 --> 277.28]  Yeah, I think probably they call that purple team in a way, right?
[277.38 --> 280.78]  They are the guys that look at what the blue and red teams are doing together.
[280.92 --> 291.54]  They just watch the traffic and try to maybe, I don't know, count points, but also write signatures, you know, to try to detect all the everything that was taking place, make sure that they don't miss it in the future.
[291.54 --> 295.46]  So it's kind of a observer role, which I think we kind of fit in.
[296.24 --> 296.40]  Yeah.
[296.84 --> 297.66]  It keeps things fun.
[297.82 --> 304.66]  It also means you like kind of get to judge everyone else's use of Go, which is, I think, nicer than having to write it ourselves in some ways.
[304.76 --> 308.28]  Like I actually love Go, but I won't pretend to be a competent developer.
[308.86 --> 312.08]  Go makes me feel like a little bit better about what I output.
[312.08 --> 321.68]  But I'm a genius compared to some of the malware that you see like floating out in Go, especially a lot of the Chinese groups have been picking up Go.
[321.88 --> 328.64]  Or like during the invasion of Ukraine, we saw a fake ransomware called Party Ticket that was written in Go.
[329.18 --> 330.58]  Wait, what's a fake ransomware?
[330.92 --> 336.26]  Well, so during the invasion of Ukraine, there were a ton of pieces of Wiper malware that were used.
[336.42 --> 337.12]  So just like, you know.
[337.14 --> 338.26]  What's a Viper malware?
[338.26 --> 338.70]  A Wiper.
[338.86 --> 341.94]  So like you get on a computer and you just delete everything.
[341.94 --> 342.38]  It's a computer.
[342.60 --> 344.04]  It just wipes the whole system.
[345.18 --> 345.86]  All right.
[347.46 --> 348.56]  I'm in the wrong pocket.
[348.80 --> 348.94]  No.
[349.10 --> 352.46]  So, you know, you get that's what a Wiper is supposed to do.
[352.48 --> 353.14]  It just gets on there.
[353.22 --> 353.88]  It wipes everything.
[353.98 --> 354.68]  It deletes everything.
[354.68 --> 355.96]  And then the computer stops working.
[355.96 --> 356.26]  Right.
[356.66 --> 358.44]  It's stupid when it's one computer.
[358.78 --> 366.00]  It's interesting when you get 3000 machines at like the Ministry of Foreign Affairs that suddenly all, you know, go kaput at the same time.
[366.18 --> 369.92]  As part of the distractions of what was going on at that time, they dropped a piece.
[369.92 --> 374.86]  What I said was a fake ransomware because they clearly never tested it.
[374.98 --> 376.90]  Like it clearly wasn't meant to be ransomware.
[376.98 --> 380.60]  They were never going to actually unlock anybody's device.
[380.60 --> 381.88]  It was just a distraction.
[381.88 --> 394.60]  And I say that because they committed like the obvious concurrency mistake that I think every noob at Go has done at some point where like, you know, you just don't.
[394.60 --> 397.94]  You don't manage your threads the right way.
[398.16 --> 406.50]  And you see that like the this Go ransomware like just nukes the computer within like four minutes because there's just so many runaway threads.
[406.50 --> 406.90]  Too much.
[406.94 --> 407.34]  And like just.
[407.58 --> 407.68]  Yeah.
[407.92 --> 408.90]  Things don't even.
[409.04 --> 411.92]  It doesn't even get to the point where it'll encrypt anything.
[411.92 --> 415.16]  It's just like a local denial of service attack.
[415.16 --> 417.22]  So it's not really ransomware.
[417.36 --> 419.56]  It just, you know, dresses up like one.
[419.62 --> 420.40]  Self-denos.
[420.94 --> 421.30]  Exactly.
[421.42 --> 422.18]  It's a bad program.
[422.68 --> 422.82]  Yeah.
[423.22 --> 432.78]  I actually would tend to second that observation in the sense that I've rarely seen actual good samples of GoLang malware.
[432.78 --> 440.62]  The kind of stuff that we tend to see are existing groups that have their established malware families that they are still using to this day.
[440.72 --> 448.68]  But what they want to do is have droppers or first stage type malware that they can throw away on many computers.
[449.26 --> 454.96]  And then if that machine is interesting, then they will drag their actual piece of important malware there.
[455.52 --> 460.50]  But those first stage malware, those droppers, as we call them, they tend to be kind of throwable.
[460.50 --> 464.14]  Like they write one of them in a week in Go language.
[464.28 --> 465.90]  They write another one later in Rust.
[466.22 --> 468.98]  And then when they arrive in a machine, they start typing commands.
[469.04 --> 470.30]  They try to deploy something.
[470.40 --> 471.04]  If it works, great.
[471.10 --> 477.74]  If it doesn't work, then because maybe the antivirus is blocking the attempt, then they just pull another one from the shelf and so on.
[477.76 --> 483.24]  So they try to create many, many different ones, as many as they can in as many different languages as they can.
[483.32 --> 485.64]  And they do not master any single one of those languages.
[485.64 --> 490.96]  They just read some, they piece together maybe some stack overflow questions until they get something working.
[491.26 --> 494.44]  And at the end of the day, they have some piece of software that does something.
[494.56 --> 498.76]  But I mean, if you were to look at it from an engineering standpoint, probably you would be appalled.
[499.36 --> 501.30]  Yeah, well, now they have GPT-4, right?
[501.30 --> 511.26]  So no, I don't want to say that because I'm going to fall into the same like ambulance chasing that's been happening in cybersecurity where everyone's just like, GPT-4 is going to kill all of us.
[511.34 --> 513.54]  Like every attacker now uses GPT-4.
[513.64 --> 516.36]  And like we're sitting here, there's plenty of open source malware.
[516.60 --> 518.48]  Like they don't need GPT-4 at all.
[518.78 --> 520.24]  If anything, they're being lazy.
[520.24 --> 526.06]  Yeah, and also, where was this outrage when GitHub Copilot was released, right?
[526.42 --> 538.36]  Because probably a much more efficient way of writing software currently than, you know, just asking chat GPT or whatever OpenAI API to output code page by page, right?
[538.76 --> 540.32]  I feel seen right now.
[540.68 --> 543.72]  I feel very seen.
[543.90 --> 547.52]  Yeah, ask chat GPT to write your concurrency and go for you.
[547.52 --> 553.24]  So GPT-4 unlocked, what, like 20 minutes before we got on this call?
[553.80 --> 557.94]  And I'm just like asking it a bunch of rapid fire questions just to see like, are you doing better?
[558.06 --> 558.74]  Are you better at this?
[558.78 --> 563.36]  Like it did some impressive things, but like it does allow for like peak laziness.
[563.36 --> 568.70]  Like, oh, it's just like, okay, write me a deployment script for an entire like elastic search cluster and bash go.
[568.82 --> 571.38]  And you're just like, I mean, I hope it works, right?
[571.44 --> 572.50]  We'll see if it works.
[572.50 --> 578.56]  But on another level, as far as like lazy DevOps, you know, there's something there.
[578.78 --> 583.98]  Well, the next thing in that set of actions is that throw that script and say, what's missing here?
[584.10 --> 584.98]  What's the pitfall?
[585.54 --> 585.88]  Improve that.
[586.02 --> 586.50]  Just ask it.
[586.62 --> 587.24]  Does it work?
[587.36 --> 588.12]  Does your script work?
[588.20 --> 588.74]  Maybe it knows.
[588.96 --> 590.88]  How can you improve that?
[591.10 --> 591.76]  I mean, it does.
[591.84 --> 592.76]  It will give you ideas.
[593.16 --> 593.60]  It will.
[593.60 --> 606.80]  I think the thing that's missing, and I have no idea what OpenAI's plans are for the future, but the obvious thing that's missing is just having some kind of like a REPL where it's writing the code, running it, writing the code, sort of like decoding.
[606.80 --> 613.42]  Because if you just throw errors at it, like you just copy paste your errors, like it'll just keep fixing the thing.
[613.52 --> 617.94]  As long as you keep it out of like hallucination mode, which there's no warning, right?
[617.96 --> 618.88]  It doesn't turn red.
[619.12 --> 625.42]  But like when it starts just telling you fake APIs and like call functions that don't exist, packages that were never written.
[625.42 --> 629.12]  And as long as you're out of that uncanny valley, you're okay, right?
[629.14 --> 630.30]  It's going to keep fixing itself.
[630.50 --> 637.38]  So you need some kind of like lang chain implementation that's just writing the code and running it and then debugging it as it goes.
[637.82 --> 637.86]  Wow.
[637.96 --> 646.32]  So when you say that the code, the malware code that was going around is bad and concurrency and everything, I need to know, does it have any tests?
[646.72 --> 648.42]  Oh, well, we wouldn't know.
[648.52 --> 649.36]  We wouldn't know, right?
[649.36 --> 651.78]  Because we're getting the compiled deployed version.
[652.46 --> 652.70]  But...
[652.70 --> 653.60]  It doesn't have tests in them, yeah.
[653.60 --> 658.58]  I'm just gonna, I'm gonna guess that there were no tests written for it.
[658.88 --> 673.74]  That said, I feel like we shouldn't be too harsh on developers that don't write, you know, tests, but that maybe, I'm not trying to draw any sympathy for our like Russian wartime malicious operators, but rather for myself.
[675.44 --> 681.36]  I mean, if you mean unit tests, I'm going to go out on limb and tell you that probably, very likely not.
[681.36 --> 687.02]  If you mean testing return values and making sure that error is nil, that sometimes you would get that, yes.
[687.64 --> 696.58]  I think you've had better luck, Ivan, because like you did Sunburst and sort of like the interesting solar winds attack that some folks may have heard about.
[696.72 --> 697.06]  Yes.
[697.06 --> 700.02]  That supply chain attack included malware.
[700.44 --> 702.06]  Ivan actually analyzed that one.
[702.14 --> 705.76]  And so like, I feel like that's one where you go, okay, this is slightly better written.
[705.98 --> 707.64]  And, you know, it definitely works, right?
[708.00 --> 710.12]  Compared to some of the other things that you analyze.
[710.48 --> 710.90]  It does.
[710.98 --> 711.10]  Yeah.
[711.16 --> 713.82]  This one, like it was actually my first experience with Go.
[713.82 --> 717.56]  So at the time I had no idea whether or not it was proper Go language.
[718.14 --> 725.88]  Although like experiencing Go, it felt like the language was kind of trying to prevent you from like not using it properly as much as it could.
[726.46 --> 732.86]  But in retrospect, yeah, it does feel like SunShuttle was kind of a good student there.
[733.12 --> 740.28]  Like they, they were really actually testing for all the like return values when it felt like it was needed.
[740.28 --> 743.60]  But overall, the structure seemed to make a lot of sense.
[743.80 --> 747.96]  So yeah, I suppose it was on the higher end of Golang malware.
[748.32 --> 752.62]  Trying to put myself in the shoes of like all these experienced Go devs who listen to this show.
[752.80 --> 755.06]  Like we must sound so silly right now.
[755.14 --> 759.30]  Like honestly, it's just, we're dealing with a very different crowd.
[759.30 --> 768.70]  Like I think Ivan described it really well when it's like, okay, you have certain well-established groups that want new components, mostly for the first stage, right?
[768.70 --> 777.74]  So they want a piece of malware whose sole role is to land on your computer, assess where it is, and then deploy more special malware.
[778.18 --> 780.46]  So for that, you can be super lazy, right?
[780.48 --> 787.98]  You're just writing a loader in Go, you write a loader in Rust, and then you just see what's going to run without like the antivirus really like going into a frenzy.
[788.14 --> 789.38]  And then you don't care, right?
[789.40 --> 793.18]  You deploy your .NET stuff or whatever it is that you've been already sitting on.
[793.18 --> 801.86]  I think it's few teams that are really adopting Go from the perspective of established native Go devs.
[802.00 --> 807.98]  And that might actually just reflect some of like the government hiring cycles at some of the teams that we're dealing with, right?
[807.98 --> 819.64]  Like how many, you know, brand new grads that have done Go in university are now working in like the Chinese Ministry of State Security yet, right?
[819.64 --> 821.70]  And same with the Russians and so on.
[822.02 --> 827.94]  There's almost like a generational thing that we're, I'm not going to say we're waiting on, but that I expect is having some effect.
[828.04 --> 831.26]  So now we see Russian ops picking up with like Kubernetes and stuff.
[831.28 --> 836.46]  And you're like, okay, those are not the same old dudes that I've been dealing with for the past 15 years.
[837.00 --> 838.58]  I'll go even further there, right?
[838.58 --> 850.16]  I would say that when we see those new droppers that I've churned out every other week, it really feels like this is some sort of, you know, interval hazing for all the interns that are coming in.
[850.16 --> 855.60]  They arrive, you know, they don't have the clearance or ability to work on the Sears stuff yet.
[855.74 --> 861.30]  So what they say, probably they are tasked with writing some quick dropper in whatever language they've been learning recently.
[861.54 --> 862.50]  And this is what they do.
[862.50 --> 867.86]  And then maybe in six months or when they are finally hired or so on, then they move to other stuff.
[867.98 --> 874.56]  But it really feels like this is the kind of, I would say, internal circuit that they are going through.
[874.72 --> 881.10]  Like for new hire, then you write a dropper and then maybe if you did a good job, you can go and handle the actual operations.
[881.30 --> 882.72]  They're being hazed by Go.
[882.96 --> 883.40]  Exactly.
[883.92 --> 885.56]  Or Rust or Pascal, actually.
[885.56 --> 896.42]  I'm finding sort of the way y'all are talking about sort of state-sponsored, like security breaches and malware and all this.
[896.80 --> 900.36]  Like it's like a regular job, right?
[900.40 --> 908.00]  And when you go to, you know, you join a company and you, you know, if you're a junior or straight out of school, right, you don't get access to the critical path stuff, right?
[908.00 --> 911.96]  Like maybe, you know, you get put on some bug duty or whatever it is, right?
[912.00 --> 916.72]  But there's a process you go through to get promoted into working with better stuff.
[917.06 --> 926.30]  But when we think of hackers, we think some, you know, kid in their basement, right, with Cheetos all over their T-shirts and, you know.
[926.56 --> 928.86]  The 400-pound hacker from like the Trump era.
[928.88 --> 929.20]  Right.
[929.32 --> 929.48]  Yeah.
[929.54 --> 934.14]  It's like this, yeah, this stereotypical stuff you see in the movies from the old days.
[934.14 --> 937.78]  It's like, but this is completely not what it is.
[937.78 --> 941.40]  This is like formalized, like a job job.
[941.90 --> 943.46]  It depends on who you're dealing with, right?
[943.48 --> 950.00]  Like I think Ivan and I, in a way, I think we're not tooting our own horns.
[950.08 --> 954.34]  It's rather we like, we focus on a very specific part of cybersecurity, right?
[954.34 --> 963.80]  You're analyzing what we call APTs, advanced persistent threats, which is like a, it's just a euphemism for like, this is probably a government-sponsored.
[964.14 --> 965.32]  You know, set of hackers.
[965.32 --> 973.06]  Because it's hard for us to like make the attribution past like a little cluster of malware to saying, okay, this is this intelligence agency or whatever.
[973.36 --> 974.82]  But you get to see everything, right?
[974.82 --> 978.34]  Like this year we've had hacktivists become like a big thing again.
[978.34 --> 1000.44]  And with those, like you can have the, you know, basement dweller children that are in Anonymous and they just want to like DDoS a website all the way to, you know, you have some hardcore black hat that nobody's seen in 20 years who suddenly decides to hack hacking team or hack some like big company and just dump all, like the Panama Papers, for example.
[1000.44 --> 1006.88]  Random hacker, nobody knows, hacks into this place, steals all their data, posts it out there just for the sake of anarchy.
[1007.04 --> 1008.30]  And then, you know, everything melts down.
[1009.08 --> 1010.12]  So you get everything.
[1010.38 --> 1017.30]  And then for us, I think we tend to, like, I don't want to speak for you too much, Ivan, but like, I think we tend to focus a lot on like the government side of the house.
[1017.30 --> 1021.98]  It's like these, these guys tend to do more interesting things from the defense side of things.
[1021.98 --> 1031.90]  Yeah, absolutely. And the comment I would like to add on this is that, yeah, it's true that we have this vision of the hoodie wearing hacker that is been fed to us by Hollywood.
[1031.90 --> 1035.12]  And we kind of want to believe in it because it's kind of, it's an appealing image.
[1035.12 --> 1042.82]  But at the same time, as Jags was mentioning, we kind of focus on those threat actors that tend to be intelligent services and intelligent services.
[1043.06 --> 1046.04]  Like they may hire people that wear hoodies, like that's their business.
[1046.14 --> 1048.90]  But at the same time, you know, they have customers, right?
[1048.94 --> 1050.04]  There is an intelligent cycle.
[1050.04 --> 1056.38]  They have to produce information for other departments, other services, maybe for the executive level.
[1056.82 --> 1057.56]  You know, and this.
[1057.80 --> 1058.28]  It's a job.
[1058.54 --> 1059.62]  Exactly. It's a job.
[1059.72 --> 1062.98]  And they have to provide, they have to deliver at the end of the day.
[1063.12 --> 1071.56]  And so they really need to set up all sorts of processes where if Bob is sick, called in sick one day, then Alice needs to be able to fill in.
[1071.64 --> 1073.34]  And so they have to have those repeatable processes.
[1073.34 --> 1077.64]  They have to have those programs that everyone, every operator knows how to use.
[1077.64 --> 1084.58]  And they need to be able to move around across people because this is like a production factory, right?
[1084.58 --> 1086.36]  Like the spice has to flow.
[1086.54 --> 1090.56]  They cannot ever stop because basically this is the job.
[1091.36 --> 1091.84]  Right.
[1092.36 --> 1093.44]  That's a beautiful part.
[1093.86 --> 1095.66]  It changes country to country, too.
[1095.80 --> 1101.08]  Like we're so much more formal in the West, like especially in like US, Five Eyes in general.
[1101.20 --> 1107.90]  Like you can tell there's a production pipeline that involves like defense contractors and like the defense industrial base, right?
[1107.90 --> 1110.78]  Like a Raytheon or a Northrop Brumman will get involved in that.
[1110.78 --> 1122.78]  And then you look at certain like European countries and it's obvious that at some point someone in an intelligence agency like hired like five hoodie wearing French dudes in a room somewhere and they built a whole platform.
[1123.18 --> 1123.38]  Right.
[1123.86 --> 1125.94]  So like country to country, you'll get something different.
[1126.06 --> 1134.60]  The Chinese, like the reason we get pummeled by so many Chinese attacks is they're really undiscerning in their targeting.
[1134.60 --> 1138.62]  So they'll go, OK, we really need to get into this pharmaceutical company.
[1138.82 --> 1147.70]  And they'll pass that requirement to like the state sponsored guys, to the random hoodie guys, these dudes that just like do hack for hire over there.
[1147.70 --> 1150.38]  And like you'll see 12 teams hitting the same target.
[1150.48 --> 1153.02]  You're like, please, like this is, be stealthy.
[1153.10 --> 1155.94]  Like at least pretend you're trying not to get caught.
[1156.12 --> 1157.50]  So it's culture to culture.
[1157.62 --> 1158.82]  Every place is a little different.
[1159.06 --> 1164.46]  I will say, though, like despite what Jack just said, eventually they managed to get in, though.
[1164.60 --> 1165.22]  Oh, for sure.
[1165.44 --> 1167.20]  So like we're having a laugh here.
[1167.32 --> 1169.62]  But at the end of the day, like it works.
[1170.26 --> 1182.02]  I mean, if you have 12 teams, right, like trying to find a hole, I mean, if it's I usually tell people like, look, it's like security and like, you know, reducing your surface area.
[1182.02 --> 1185.12]  Like you have to think of these things as mitigation efforts.
[1185.48 --> 1194.10]  If a group of people or a state sponsored situation happens to you, chances are they are going to find a way to get in.
[1194.10 --> 1200.46]  And it's either if it's not your security or your software, your file or whatever it is going to be, you know, some weak link in the chain in terms of a person.
[1200.46 --> 1200.86]  Right.
[1200.92 --> 1205.06]  Who has some sort of vulnerability or they fall for some phishing attack or whatever.
[1205.16 --> 1207.42]  But if somebody is after you, they will get in.
[1207.54 --> 1207.68]  Right.
[1207.98 --> 1208.28]  Oh, yeah.
[1208.34 --> 1209.44]  And actually, it's never the firewall.
[1209.64 --> 1211.50]  It's it's always the phishing.
[1211.50 --> 1211.94]  Yeah.
[1212.06 --> 1220.34]  There's so many there's so much focus on like, oh, there people are using these like unpatchable zero day exploits and all the software.
[1220.46 --> 1221.46]  You're like, yeah, sure.
[1222.04 --> 1226.56]  But what about like the 95 percent of attacks that were just like someone opened an attachment?
[1226.82 --> 1230.68]  Someone put their credentials into like a fake Facebook website.
[1230.80 --> 1231.34]  They got email.
[1231.34 --> 1234.82]  Like that is a lot of attacks and people discount them.
[1235.02 --> 1238.20]  But look at what's happening now with the rise of supply chain attacks.
[1238.32 --> 1249.88]  So like my first unpopular opinion on this show was, you know, software devs may be like some of have some of the worst security in all of the Internet.
[1249.88 --> 1254.40]  Because like we, you know, I'm not going to say we in this case, I will toss it on you guys.
[1254.40 --> 1257.40]  Like there's a certain amount of hubris.
[1257.40 --> 1263.98]  There's a lot of installing random stuff and a lot of reliance on package managers.
[1264.54 --> 1268.52]  No one wants to run an EDR, XDR, AV install.
[1268.92 --> 1270.08]  Everything is root.
[1270.72 --> 1278.92]  But like there's all the SSH keys and PGP keys and things that you use to like change prod are on your laptop.
[1278.92 --> 1286.70]  So like we've seen plenty of ops and some that have been like leaked and publicly documented where you're like, okay, they were obviously going.
[1287.24 --> 1291.74]  You know, they were fishing through LinkedIn to get to the devs.
[1291.86 --> 1294.34]  They know these are like the sys admins for the company.
[1294.54 --> 1297.88]  You walk in, you already have root passwords.
[1298.10 --> 1302.62]  You already have access to the entire environment and you have the keys to hit prod.
[1302.86 --> 1307.04]  And that's the beginning of a lot of what you might consider like supply chain attacks, right?
[1307.04 --> 1317.52]  If I can change your code base, I can add malware directly to the update pipeline that you use and I can hit every single downstream customer that you have.
[1317.88 --> 1320.60]  And that might have been esoteric like 10 years ago.
[1321.00 --> 1323.00]  We're like knee deep in it now.
[1323.04 --> 1324.78]  Like it's happening all over the place.
[1324.78 --> 1327.12]  The brewing song was definitely spot on.
[1327.48 --> 1336.02]  But I do wonder if Go being so conservative on libraries and, you know, the repeating recommendations to just stick to the standard library.
[1336.18 --> 1340.06]  Is this in any way helping things and making Go slightly safer?
[1340.46 --> 1346.98]  I think it creates a central point of failure in some ways, but it isn't one that I think is bad.
[1347.28 --> 1347.50]  Right.
[1347.50 --> 1352.66]  Like I think, I think Go is in a much better situation because of what you're describing sort of conservatively.
[1352.92 --> 1359.94]  There's still a way to get to it, but I think we'd be unfair to the Go users to equate it with something like pipey.
[1360.06 --> 1360.50]  Right.
[1360.54 --> 1363.42]  Like pipey, you know, it's, it's a show.
[1363.58 --> 1363.96]  Sorry.
[1364.40 --> 1367.10]  And then it's really bad.
[1367.14 --> 1375.56]  And you have a ton of like name typos squatting and like people stealing developer accounts and then replacing well-known packages with trojanized packages.
[1375.56 --> 1384.14]  We actually discovered a similar, well, we worked on a similar supply chain attack for the rust crates.io.
[1384.46 --> 1389.06]  And like they were super responsive, super nice, like really engaged.
[1389.24 --> 1403.70]  But essentially somebody created a fake developer profile that squatted on a known developer and changed the rust decimal package in the hopes that like people would, you know, accidentally install that.
[1403.70 --> 1409.38]  It would pull a second stage piece of malware that was designed to be on CICD pipelines.
[1409.82 --> 1417.52]  So it's like, you're trying to hit a production pipeline specifically for the purposes of hitting downstream customers eventually.
[1418.08 --> 1419.54]  Oh, it's, it's wild, man.
[1419.58 --> 1420.40]  It's getting crazy.
[1420.92 --> 1421.28]  It is.
[1421.36 --> 1423.48]  I would say it doesn't have to be black and white though, right?
[1423.56 --> 1424.00]  Indeed.
[1424.18 --> 1427.70]  We have Python where everyone can create an account of upload libraries.
[1427.70 --> 1432.52]  Actually, a former coworker, Felix Emey, now working at a French company called Sequoia.
[1432.68 --> 1441.68]  He did some research recently where he found on GitHub some project that automatically backdoors a copy of an existing library and uploads it on pip.
[1441.80 --> 1442.56]  Like it's automated.
[1442.78 --> 1444.74]  Like you can create hundreds per day if you want to.
[1445.14 --> 1445.70]  There's this.
[1445.86 --> 1452.92]  And at the other end of the spectrum, you have something like a go where I get, I'm getting that there are too many outside libraries.
[1452.92 --> 1456.02]  Or at least you are discouraged to use them because it's all batteries included.
[1456.52 --> 1472.22]  Like maybe there is some middle ground there we could reach where, you know, we can get some trusted or curated package of or repository of libraries where people could download stuff without one, pulling the whole planet with every left padding or something.
[1472.64 --> 1473.60]  And two, where it.
[1474.84 --> 1476.04]  That never gets old.
[1476.22 --> 1477.34]  No, it never does.
[1477.46 --> 1477.62]  Right.
[1477.98 --> 1479.94]  And then second, probably where.
[1479.94 --> 1481.72]  We should add that to the show notes.
[1482.56 --> 1482.68]  Yeah.
[1482.92 --> 1483.66]  For those.
[1484.32 --> 1498.58]  And then maybe when people upload packages there, they could go through some sort of review by the Golang team if they have the resources for this, at least to curate some sort of standard extended library that could be useful to other people.
[1498.84 --> 1503.88]  I think you just like suggested that we get our own crates.io or Pypey.
[1504.08 --> 1504.52]  Maybe.
[1504.52 --> 1507.40]  Like not to, you know, I think that's how you end up there, right?
[1507.40 --> 1515.00]  You go, well, what if we had like a single centralized way to like vet packages and like the developers will up, you know, thumbs up, thumbs down.
[1516.48 --> 1519.90]  It's, I think that's how you end up in that situation anyways.
[1520.24 --> 1522.04]  I meant it like maybe an Apple store.
[1522.16 --> 1523.36]  Like don't make it open bar.
[1524.02 --> 1524.38]  Yeah.
[1524.38 --> 1527.40]  Well, that's how I think about like the Google repo though.
[1527.48 --> 1533.98]  Like they do seem to have some more standardized sort of packaging there and, you know, things are relatively well maintained.
[1534.48 --> 1536.12]  But I don't know.
[1536.12 --> 1538.88]  Yeah, we can't really trust any of it.
[1538.98 --> 1547.16]  I think to Natalie's point, like it's cool that folks tend to rely mostly on, you know, the standard libraries.
[1547.16 --> 1556.58]  It's already packaged there, but there's some inevitability to it when you start like pushing GitHub repos and everybody, everybody pulls someone else's project at some point.
[1556.76 --> 1558.84]  I just think that it's, I don't know.
[1558.94 --> 1560.28]  A Go is not the prime target.
[1560.70 --> 1561.90]  I'll just put it that way.
[1562.08 --> 1565.10]  Go is not the prime target precisely because of what you're describing.
[1565.10 --> 1567.50]  That said, it's super useful.
[1567.50 --> 1585.42]  And like, since we started the conversation with GPT-4, like, I think it's the best language to have ML generated because it's so fascistic to borrow Ivan's expression, sort of fascist Python, that it's perfect for an LLM.
[1585.52 --> 1587.60]  It's just the, it's super standard, right?
[1587.62 --> 1590.28]  You have the things sort of shaped the same way.
[1590.36 --> 1591.60]  The conventions are the same way.
[1591.60 --> 1600.46]  Like we don't, you don't need as much of a style guide because there's not a lot of room for deviation and you have standard patterns for concurrency, standard patterns for a bunch of things.
[1600.58 --> 1609.76]  So personally, I find that GPT generated Go code is for me, most of the time, compilable out of the box.
[1609.76 --> 1610.80]  Is it perfect?
[1611.00 --> 1612.34]  Is it doing what I want it to do?
[1612.44 --> 1613.26]  Not necessarily.
[1613.82 --> 1615.26]  In many cases, no.
[1615.50 --> 1617.48]  But like, it's, it compiles, right?
[1617.50 --> 1624.46]  Which is more than you can say for a lot of Python, a lot of other code, at least up to GPT-3.5.
[1625.16 --> 1627.82]  It's, you know, GPT-4, I don't know yet, right?
[1627.84 --> 1628.66]  Like we got to go test.
[1628.78 --> 1631.40]  It's been, you know, it's been alive for 40 minutes.
[1631.40 --> 1634.68]  But so along those, along those lines though, right?
[1634.76 --> 1647.14]  So if we can use, if we can use these tools to generate the code that is doing the attacking, can we use these tools to generate code or to understand code that is attacking and defend against these things?
[1647.14 --> 1655.04]  So personally, I'm really invested in some of the powers that LLMs are providing for defenders.
[1655.60 --> 1657.32]  It's not a one-to-one corollary.
[1657.58 --> 1661.86]  Like Ivan, you wrote one of the first, most useful tools, I think.
[1661.98 --> 1663.44]  I don't know if you want to talk about like Geppetto.
[1663.90 --> 1664.50]  Yeah, sure.
[1664.80 --> 1668.32]  Maybe I can go back to it after you're done or I can talk to you about it right now.
[1668.46 --> 1668.66]  Sure.
[1668.76 --> 1668.88]  Yeah.
[1668.94 --> 1671.10]  So sorry, just to kind of couch the concept.
[1671.10 --> 1678.90]  It's not necessarily for building tools that we could really use LLMs, but actually for interpreting a lot of code when we're doing reverse engineering.
[1679.44 --> 1683.58]  Reverse engineering malware is a fairly esoteric task.
[1683.74 --> 1685.92]  There's very few people that are good at it.
[1686.32 --> 1692.04]  So it's one of those talents that is just immensely in demand and not easy to produce.
[1692.20 --> 1699.12]  Like you can't just go to a specific school or a specific program and you're going to like walk out being like, all right, I'm a reverse engineer.
[1699.12 --> 1710.30]  It tends to come from a certain amount of like some coding practice, being really into like, I don't know, cracking game licenses or like, or making game mods.
[1710.62 --> 1711.72]  A few neuroses as well.
[1711.80 --> 1711.94]  Yeah.
[1712.02 --> 1718.26]  And a few neuroses, a good stash of Adderall, you know, something in there that sort of pushes you in that direction.
[1718.26 --> 1738.76]  So I saw Ivan's tool, which, you know, I'll let you talk about and ended up actually designing like a whole university course around the use of his tool, the use of just ChatGPT in general, because what it ends up doing is being really good at summarizing and interpreting C pseudocode and assembly.
[1738.98 --> 1741.16]  And you can be like, what is this function doing?
[1741.54 --> 1741.62]  Right.
[1742.14 --> 1742.36]  Yeah.
[1742.36 --> 1755.16]  So maybe I can introduce it in a few words, you know, back then when ChatGPT was initially released and it was, everyone was out there and being worried about whether or not they would still have a job in a few years.
[1755.60 --> 1757.98]  I was asking myself the exact same questions, right?
[1758.04 --> 1761.74]  And I was just wondering, okay, so can ChatGPT do my personal jobs?
[1761.74 --> 1773.18]  So I took some code that was some pseudocode that was generated by my analysis tool, some code from malware that I don't own the source code of.
[1773.44 --> 1777.78]  But I took that and put it on ChatGPT and I was like, okay, so this is a C function.
[1778.02 --> 1778.64]  What does it do?
[1778.72 --> 1783.54]  Because basically my job is to look at those functions, try to understand what they are.
[1783.64 --> 1788.58]  Then when I look at all the functions in an unknown program, then maybe I can tell my employer what the malware is actually doing.
[1788.58 --> 1794.96]  And to my extreme surprise, ChatGPT turned out to be quite good at this.
[1795.44 --> 1796.40]  Like extremely good.
[1796.68 --> 1802.62]  And when you think about it in retrospect, it kind of makes sense because ChatGPT is a language model.
[1803.06 --> 1810.92]  Code is a language and ChatGPT tends to be extremely good at understanding, interpreting and rephrasing that kind of stuff.
[1811.04 --> 1815.82]  And so what it does is you give it some unknown code that has been generated by automated tools.
[1815.82 --> 1818.86]  The code will not have any variable names.
[1818.94 --> 1823.14]  It will not have any meaningful comments or meaningful function names, that kind of stuff.
[1823.34 --> 1830.84]  But it's still code and ChatGPT is able to extract meaning out of it and provide it as human language.
[1831.68 --> 1840.46]  And so what I did then was after my initial shock, create a plugin that directly pipes my work tool with OpenAI's API.
[1840.46 --> 1843.34]  So initially it was the DaVinci-003 model.
[1843.44 --> 1847.78]  Now I switched to the latest one, which is the GPT-3.5.
[1848.54 --> 1853.56]  But so what I do is my tool now sends the pseudocode to ChatGPT.
[1853.68 --> 1857.24]  And ChatGPT, well, or the OpenAI model.
[1857.44 --> 1859.60]  Sorry, I know that this is not exactly the same necessarily.
[1859.80 --> 1866.20]  But anyway, OpenAI's API just returns to me a comment that is, okay, this function, this is what it does.
[1866.20 --> 1871.12]  And then maybe I have to check it a little bit to verify that it's consistent with what I'm seeing.
[1871.20 --> 1878.42]  But overall, I just press a combination of hotkeys and then the AI is just doing my job and then I have to piece the things together.
[1878.68 --> 1881.30]  So it's really saving a lot of time.
[1881.52 --> 1887.70]  And I think it's seen a lot of adoption in the community considering the activity on GitHub.
[1887.70 --> 1890.02]  So we'll add the link to this in the show notes.
[1890.42 --> 1897.92]  And I have to propose the idea of what you just said as the very last step of gluing it all together and seeing how it works.
[1898.14 --> 1902.86]  Use the fact that what was released today has a larger input size.
[1902.94 --> 1906.06]  Like you can put a lot more tokens into it and maybe it will do that for you as well.
[1906.52 --> 1908.02]  Yeah, I'm excited about it.
[1908.16 --> 1913.74]  Like I, to be honest, like I haven't said anything, Ivan, but I've been like fiddling with your tool so much.
[1913.74 --> 1928.18]  And then just sitting there being like, okay, how can I use this like recursively so that we go from like interpreting a specific function to going through a specific like branch of control flow, summarizing the summaries, like etc.
[1928.40 --> 1932.56]  And then how do I get like, give me a summary of what this whole program does.
[1932.92 --> 1933.20]  Right.
[1933.24 --> 1936.32]  It's like getting to like extreme levels of laziness.
[1936.32 --> 1938.44]  This is a work in progress.
[1938.56 --> 1943.90]  The main limit that I've been hitting is the number of tokens per request to OpenAI's API.
[1944.78 --> 1947.40]  It's like there are ways, but it needs some fiddling.
[1947.80 --> 1950.34]  And it costs a lot in tokens every time you fail.
[1950.62 --> 1954.80]  Because when you go recursively in a program, then, you know, it can go very deep.
[1954.88 --> 1956.48]  It can be thousands of function calls.
[1956.48 --> 1968.30]  So I'm kind of fiddling with this myself, but haven't been able to find a way to get it to generate results that are meaningful enough that I would spend 10 or 20 bucks per request.
[1968.60 --> 1971.14]  But that's a matter of cost, right?
[1971.66 --> 1972.40]  That's just cost.
[1972.48 --> 1975.12]  Because if somebody's footing that bill for you, right?
[1975.20 --> 1976.74]  Say you have a limited budget.
[1977.12 --> 1977.60]  Then what?
[1977.94 --> 1978.24]  What?
[1978.48 --> 1979.16]  Nobody is.
[1979.16 --> 1982.40]  Well, you heard it here, folks.
[1982.44 --> 1985.44]  If you're listening and you want to sponsor, you know, Ivan.
[1986.70 --> 1989.88]  OpenAI needs to come, you know, open the purse for us.
[1990.96 --> 1995.50]  Honestly, it's not that expensive, but I can see how it can just be a runaway thing.
[1995.56 --> 1997.42]  Like we definitely have to put some guardrails in there.
[1997.62 --> 1999.38]  Again, just to make it accessible for folks.
[1999.38 --> 2003.58]  When you're reverse engineering code, most of the time you've lost most of the labeling.
[2005.60 --> 2007.66]  Malware not generated by Go.
[2007.66 --> 2011.96]  So it's very, it can be hard to tell what's library code, like standard library code.
[2012.04 --> 2020.98]  So you could easily go down the full path of reverse engineering open SSL that was statically compiled into a binary, right?
[2021.00 --> 2021.52]  Which is terrible.
[2021.58 --> 2022.30]  You don't want to do that.
[2022.36 --> 2027.14]  And I think that's where you get into like cost prohibitive uses of ChatGPT, possibly.
[2027.38 --> 2034.42]  If you're going to try to go through 45,000 functions of which 70% of it was standard library code,
[2034.44 --> 2035.84]  or there was no reason for you to do that.
[2035.84 --> 2038.04]  So we kind of have to build some guardrails there.
[2038.46 --> 2042.10]  That said, I mean, Go is a lot easier to reverse engineer.
[2042.44 --> 2047.50]  Like on some level, I'd be pretty happy for a lot of malware devs to go the Go path.
[2047.66 --> 2048.08]  Absolutely.
[2048.34 --> 2049.96]  Because it just, I love it.
[2050.02 --> 2051.44]  Like I love reverse engineering Go.
[2051.56 --> 2052.92]  It used to be a nightmare.
[2053.18 --> 2055.12]  And now it's a lot easier.
[2055.12 --> 2062.58]  And you have no idea how many Go like puns you've just crammed into just one sentence.
[2063.02 --> 2066.74]  Like I love that you don't realize that because you're not in the Go community day to day.
[2066.92 --> 2069.24]  Like I like, you know, you're just mentioning it.
[2069.30 --> 2070.62]  I was just like, bing, there's another one.
[2070.74 --> 2071.58]  Bing, there's another one.
[2071.78 --> 2073.16]  I don't even have my own gopher.
[2073.26 --> 2073.96]  I'm not there yet.
[2074.06 --> 2074.50]  It's not.
[2074.50 --> 2075.58]  It's funny.
[2075.68 --> 2079.14]  We talked about, I was talking to Natalie about a recent publication we did.
[2079.48 --> 2087.50]  So Alex Belinkowski was on my team, found this piece of Chinese APT malware that was written in Go.
[2087.50 --> 2095.40]  And for the first time ever, he caught them basically creating a really simple Go binary.
[2095.68 --> 2099.68]  It includes Yaegi, that like Go interpreter.
[2100.40 --> 2102.76]  So it's, you know, some open source Go interpreter.
[2102.76 --> 2106.00]  So it's a really simple binary that just runs this interpreter.
[2106.30 --> 2113.14]  And then it like decodes all this Go source code that's being kept as like base 64 encoded string.
[2113.30 --> 2117.46]  And then gets Yaegi, like the interpreter, to run it live on the system.
[2117.88 --> 2123.86]  So the idea is if, you know, if a piece of, you know, if an AV or whatever, an antivirus decides to check the malware,
[2124.00 --> 2126.18]  you're like, well, this seems fairly innocuous, right?
[2126.22 --> 2129.66]  It's just, it's having like, just, it looks like a REPL or whatever.
[2130.06 --> 2132.70]  It turns out to just be staged malware.
[2132.94 --> 2144.10]  Yeah, this is a good illustration of how, you know, in many cases, like good software development practices are very orthogonal to the objectives that the malware developers are trying to meet.
[2144.50 --> 2146.58]  If that's not a reason to follow the good practices.
[2149.00 --> 2149.64]  I don't know.
[2149.68 --> 2152.88]  There's plenty of good Go offensive tooling out there.
[2153.44 --> 2154.60]  Most people haven't caught on.
[2154.82 --> 2155.68]  I'm okay with that.
[2155.76 --> 2158.80]  Like, I'm not about to point them in the direction of it, but it's already there.
[2158.80 --> 2161.32]  Like, these people are just not looking at the right projects.
[2161.68 --> 2161.84]  Yeah.
[2162.00 --> 2163.92]  Why are you still on Cobalt Strike, guys?
[2164.12 --> 2164.98]  Like, what's up with that?
[2165.36 --> 2170.98]  I will say that you were trashing the poorly written Go one and the well-written one you're still researching.
[2171.16 --> 2173.04]  So really just goes to prove that point.
[2173.40 --> 2175.66]  You know, make our lives more interesting, please.
[2176.14 --> 2179.18]  It's a bizarre situation to be in, right?
[2179.18 --> 2184.76]  Like, where half the time we're talking about how we want to defend people and we're trying to help people, you know, defend their networks.
[2185.12 --> 2196.46]  But there is some, like, slightly evil streak where you kind of sit there and go, like, you know, it would be awesome to find this insane, like, Stuxnet level, like, piece of malware that no one has seen before.
[2196.46 --> 2199.26]  And, like, spend all your time nerding out on it.
[2199.82 --> 2201.86]  It's like waiting for a train wreck to happen.
[2201.98 --> 2205.04]  It's like being really excited of a pileup on the highway.
[2205.04 --> 2208.44]  Like, it's just, you know, there's something messed up about the whole thing.
[2208.58 --> 2209.94]  Yeah, we don't usually talk about that.
[2211.54 --> 2212.24]  Like Bruno.
[2212.36 --> 2213.12]  We don't talk about Bruno.
[2214.66 --> 2216.52]  No, this is between me and my therapist.
[2219.04 --> 2228.16]  So, Ivan, the tool that you wrote, Geppetto, which is in the show notes, you said that you recently used it for comparison of Go code with and without generics.
[2228.16 --> 2228.20]  Yes.
[2228.42 --> 2240.96]  So, I did not use it in this specific case because, well, first of all, I didn't really try to look at the code generated by the Go compiler under Geppetto because I didn't have the chance yet.
[2240.96 --> 2250.94]  And I'm not sure I was going to react because, again, the output of iDice decompiler when it comes to Go code can tend to be a little bit broken or extremely broken depending on the Go version.
[2251.08 --> 2252.30]  So, I did not try that too much.
[2252.82 --> 2254.26]  I'm not sure it's going to work very well.
[2254.26 --> 2263.42]  But in any case, yes, I was expecting that you would be asking me a question about generics because this is something that you tend to do every time I show up in a podcast with you.
[2263.80 --> 2265.48]  So, this time, I came prepared.
[2267.86 --> 2284.24]  So, what I did was I created a very small program from the official Go tutorial and looked at the – I took the sample code, compiled it, and went to Ida to see the difference between a function that wasn't generic and this –
[2284.24 --> 2287.12]  and the equivalent that wasn't generic.
[2287.78 --> 2289.74]  And I was kind of expecting something.
[2289.98 --> 2291.12]  It turned out to be the case.
[2291.32 --> 2302.54]  Before I spoil it, the reason why I was expecting something and wondering if it was going to be true is because, as I mentioned in previous podcasts, Go language tends to do things on its own, right?
[2302.54 --> 2322.68]  And if you are used to seeing something in C or in C++ and you look for it in Go language, it usually is not going to be the same because, you know, the Go developers really looked like they started from scratch and they wanted to do things better and, you know, without, I don't know, sitting on top of the shoulders of very broken giants.
[2322.68 --> 2327.56]  So, what they did here is actually the same thing as C++.
[2328.10 --> 2336.10]  So, in C++, when you have template functions, what the compiler does is it generates a copy of the function for each type that is actually used in the program.
[2336.56 --> 2338.48]  And Go did exactly the same here.
[2338.48 --> 2356.08]  So, if you have a generic function that can receive as arguments either an integer or a float, for instance, or maybe a string, whatever, then in the compiled program, you will have one version of the function which receives an integer as an argument and where everything inside the function is related to integers.
[2356.08 --> 2359.86]  And then you will have the exact same copy of the function but with the different types.
[2360.54 --> 2373.28]  And then when the program is calling the specific function that is a response to the generate type that is being used currently, then it just invokes the instance of the function that was generated by the compiler.
[2373.78 --> 2384.44]  So, in effect, it's doing exactly the same thing as C++, which is it creates copies and then, you know, since it knows which type is going to be used at compile time, it just adds a call to the right function.
[2384.44 --> 2386.70]  So, yeah, that's how it works.
[2387.32 --> 2387.94]  Real simple.
[2388.54 --> 2389.88]  You're like, yeah, this is just it.
[2390.02 --> 2390.54]  It's like a real simple.
[2390.76 --> 2391.18]  Easy peasy.
[2391.56 --> 2391.82]  Yeah.
[2392.16 --> 2392.72]  It's funny.
[2393.24 --> 2394.96]  Our tooling breaks really easily.
[2395.20 --> 2404.64]  Like, there's a lot of, I think, things that are already rudimentary to the development community that when it comes to the reverse engineering community is not great.
[2404.74 --> 2406.66]  Like, we don't have a lot of good maintenance of our tools.
[2406.66 --> 2420.28]  So, for example, Ivan, like, mentioned that IDAPro, which is like the decompiler disassembler that most reverse engineers use, when it tries to handle Go, it just kind of breaks and doesn't do very well.
[2420.52 --> 2422.10]  It's because of really simple stuff.
[2422.18 --> 2426.82]  Like, they never envisioned having to have multiple return arguments.
[2427.32 --> 2427.98]  Super stupid.
[2427.98 --> 2430.86]  It cannot handle the multiple return thing.
[2430.92 --> 2437.48]  So, it has to do these, like, function prologues and, like, just trying to handle how you're going to store this stuff.
[2437.64 --> 2440.78]  And, yeah, you would think that it would be easier for us to patch our tooling.
[2441.04 --> 2442.12]  It really is.
[2442.12 --> 2453.62]  I think a more fundamental problem is that in the specific case of IDA, and I think also Ghidorah's decompiler, is that they try to, they see some code and they try to decompile it as C, right?
[2453.64 --> 2454.96]  And they can only generate C code.
[2455.06 --> 2459.86]  And the thing is, it turns out that not everything can be expressed in C, especially Go programs.
[2459.86 --> 2473.28]  And so, you know, when they try to, like, go up one level, but they try to, like, create the corresponding C code, then, of course, there is no way that they're ever going to be able to create some meaningful C representation of whatever they are seeing.
[2473.40 --> 2477.68]  And so, of course, stuff ends up missing or, you know, they create variables that don't exist.
[2477.98 --> 2482.82]  It just breaks down because the assumption initially is just, turns out to be wrong.
[2483.36 --> 2487.56]  If anyone listening to this show is building a reverse engineering tool in Go, please reach out.
[2487.64 --> 2489.22]  We want to talk with you in the next episode.
[2489.22 --> 2489.78]  Please.
[2490.02 --> 2490.68]  Yeah, seriously.
[2491.02 --> 2491.68]  Many questions.
[2491.98 --> 2492.92]  Someone, please.
[2494.02 --> 2494.86]  That would be amazing.
[2495.36 --> 2505.92]  I do feel a certain tinge of jealousy when I see, like, all of the CICD developments and, like, the community that comes around sort of building tools around the tools that you folks are using.
[2506.36 --> 2507.62]  Definitely a tinge of jealousy.
[2507.80 --> 2510.46]  We do not have quite as active a development community.
[2511.00 --> 2514.54]  I think it's more a, let me caveat that.
[2514.62 --> 2518.00]  I think it's more a reflection of how few of us there are working in the space.
[2518.00 --> 2519.84]  We tend to be very bogged down.
[2519.84 --> 2523.68]  And what you'll get is, like, Ariel will release a cool plugin.
[2523.88 --> 2526.06]  And then he'll go back to doing work.
[2526.30 --> 2531.74]  So you don't have people sitting around, like, just iterating on tools, improving them.
[2531.74 --> 2536.24]  How do I start this whole new project for reverse engineering or, like, a new framework?
[2536.24 --> 2546.66]  Usually that would mean that some really good RE has stepped away from checking out any malware for, like, three months to go develop this thing.
[2546.74 --> 2551.76]  And, like, there's this difficulty gauging whether that's the best use of their time or not.
[2551.76 --> 2553.00]  Yeah, it's true.
[2553.08 --> 2555.50]  For most of us, development is kind of a side job.
[2556.24 --> 2567.98]  And it's unclear that any of our employers would be willing to, like, spend six months of our time to generate this awesome, I don't know, framework that would help the whole community.
[2568.60 --> 2571.42]  Maybe even for internal use, they might be reluctant.
[2571.42 --> 2579.06]  I feel like I've, I mean, I don't travel, you know, like, the security circles like y'all do.
[2579.20 --> 2587.86]  But, you know, I've come across tools that seem like they were built for that intent, like providing developer workflow, developer experience, that kind of thing.
[2587.96 --> 2589.90]  The one I can think of is, I think, Ruby-based.
[2589.90 --> 2594.42]  I think Metasploit is sort of, to me, represents sort of that framework.
[2594.66 --> 2601.18]  It provides tooling and ways of hooking into things, like, to make the job, right, of doing that work, you know, easier.
[2601.40 --> 2604.82]  So is anything like that these days?
[2605.14 --> 2609.10]  What you describe, like, you're absolutely right.
[2609.22 --> 2610.22]  It's a great framework.
[2610.44 --> 2611.34]  It's for attacking.
[2612.00 --> 2615.44]  So we don't get as many frameworks for, like, defensive stuff.
[2615.44 --> 2615.64]  For defending.
[2616.16 --> 2618.32]  Instead, you get these, like, factory models.
[2618.54 --> 2619.90]  Like, oh, just run Metasploit.
[2619.98 --> 2620.80]  Go to Cobalt Strike.
[2620.92 --> 2622.04]  Like, there's, don't worry about it.
[2622.04 --> 2624.92]  Just four options and it'll output, like, new malware for you.
[2625.06 --> 2629.34]  Like, we're on the other side with, like, Soviet tools from, like, the late 90s.
[2629.40 --> 2630.00]  Just try.
[2630.30 --> 2633.88]  Like, it's just, it doesn't, it doesn't, there's no corollary there, right?
[2634.26 --> 2636.10]  It's more fun to attack than it is to defend.
[2636.44 --> 2637.30]  Is that what you're telling me?
[2637.60 --> 2639.18]  I think it's more accessible.
[2639.18 --> 2648.10]  I don't know that it's more fun, but it's because I'm, like, the weird kind of nerd that, like, just really enjoys doing reverse engineering and malware hunting.
[2648.44 --> 2651.00]  And so for me, I like that better.
[2651.26 --> 2658.62]  I think it would be really weird to be in the offensive security space but not attack anyone for real.
[2659.42 --> 2661.04]  Like, maybe that's a weird thing to say.
[2661.12 --> 2662.86]  Like, that might be my unpopular opinion.
[2662.86 --> 2671.30]  It's just, like, I don't know why you would go into offensive and then never break the law and, like, never hack anybody for fun, right?
[2671.36 --> 2674.28]  It's just a bunch of paid engagements for enterprises.
[2674.28 --> 2678.60]  Sounds like the most boring use of superpowers ever.
[2679.42 --> 2682.00]  A lukewarm defense of recreational hacking.
[2682.12 --> 2682.88]  You heard it here first.
[2683.02 --> 2683.62]  Yeah, exactly.
[2683.62 --> 2690.10]  Well, no, it's just, like, you don't get Superman and then, like, all he does is, like, just get cats off of trees.
[2690.60 --> 2692.12]  Like, that's a nice side hustle.
[2692.40 --> 2695.06]  But the idea that, like, you have superpowers.
[2695.16 --> 2697.32]  You can break into these systems.
[2697.68 --> 2704.04]  You can, you know, you can just traverse through places you're not supposed to be in and get your hands on things you're not supposed to have.
[2704.56 --> 2708.26]  And you just kind of choose to, like, rob a candy store.
[2708.26 --> 2708.98]  Right?
[2709.06 --> 2711.58]  It just, it doesn't make that much sense.
[2711.64 --> 2712.88]  So, I'm happy on the defensive.
[2713.04 --> 2718.12]  Like, that's the worst answer to, like, I think it's much more exciting to be on the defensive side of things.
[2718.24 --> 2721.34]  But it's just, like, a Rubik's Cube that's kind of turning itself.
[2721.68 --> 2724.20]  No, but I would, I think you're essentially correct there.
[2724.32 --> 2729.86]  I think that probably most of the defenders know that they shouldn't be trusted with such a power.
[2730.40 --> 2734.58]  And all the attackers know it, too, but they just do it anyway.
[2735.08 --> 2736.52]  They're living on the edge, man.
[2736.52 --> 2739.60]  This is why you go work for, like, the NSA or something, right?
[2739.66 --> 2741.54]  Like, they're recruiting super heavy right now.
[2742.20 --> 2751.92]  So, for anybody who's lost their job at Google or whatever and is bored and doesn't smoke weed and wants to serve their country for, like, less money than what they were making.
[2752.12 --> 2753.06]  And are U.S. citizens.
[2753.18 --> 2756.12]  And are U.S. citizens and have not been arrested.
[2756.76 --> 2758.86]  And there's a few different caveats there.
[2758.98 --> 2764.72]  But essentially, you can go serve your country at the NSA and presumably do cool stuff.
[2764.72 --> 2767.28]  Don't ask how this reminds me.
[2767.38 --> 2768.78]  I owe IKEA an apology.
[2770.68 --> 2771.70]  Stage is yours.
[2773.76 --> 2774.66]  More, please.
[2776.58 --> 2781.70]  Some episodes ago, I was comparing poorly written code to IKEA furniture.
[2782.06 --> 2782.46]  Ooh.
[2782.86 --> 2783.26]  Ouch.
[2783.26 --> 2785.80]  Not despite of unpopular opinion.
[2785.96 --> 2787.50]  Did you get a cease and desist or something?
[2787.94 --> 2788.32]  No.
[2788.56 --> 2789.60]  That's what I was going to ask.
[2789.74 --> 2791.64]  It's not allowed in Sweden ever again.
[2791.88 --> 2794.88]  It's not a Swedish company as people think, apparently.
[2795.60 --> 2795.82]  Yeah.
[2795.92 --> 2796.54]  No longer.
[2796.92 --> 2799.38]  It was and still branded as one.
[2799.38 --> 2808.46]  But a friend of mine who is a cloud consultant was helping IKEA to migrate to the cloud and to also adopt Go.
[2808.66 --> 2809.88]  Please don't say China.
[2810.36 --> 2810.66]  No, no.
[2810.82 --> 2813.92]  And then they mentioned to him that Go is nice and everything.
[2814.16 --> 2816.92]  But she trashed us on Go time and that's not nice.
[2817.24 --> 2818.12]  So I apologize.
[2818.60 --> 2819.34]  I'm sorry about that.
[2819.34 --> 2820.02]  Oh, wow.
[2820.56 --> 2821.04]  Wow.
[2821.60 --> 2822.68]  It made it far.
[2823.36 --> 2824.56]  I know, right?
[2824.56 --> 2825.66]  It was not cool for me.
[2826.08 --> 2827.06]  And I will do better.
[2827.06 --> 2827.50]  Wow.
[2828.16 --> 2830.52]  She trashed us on Go time.
[2830.54 --> 2834.86]  You have to shoulder the weight of responsibility that comes with wielding this microphone.
[2835.64 --> 2836.04]  Wow.
[2836.24 --> 2836.56]  Wow.
[2836.70 --> 2837.70]  That is amazing.
[2837.76 --> 2838.74]  That's such an amazing story.
[2838.92 --> 2845.38]  Well, hopefully IKEA will, you know, hear a word that, yeah, JK, Nadia didn't really mean it.
[2845.58 --> 2846.80]  We'd love to have you on the podcast.
[2848.02 --> 2849.06]  Actually, yeah, we would.
[2849.14 --> 2849.32]  Yeah.
[2849.36 --> 2850.48]  If they're using Go for stuff.
[2850.56 --> 2852.54]  I mean, yeah, I think that would make a fun, full, fun episode.
[2852.54 --> 2854.02]  So there you go, IKEA.
[2854.02 --> 2857.28]  You've received a formal invitation from the folks at Go Time.
[2857.44 --> 2859.00]  Come talk to us about the things you're doing.
[2859.36 --> 2860.32]  And a formal apology.
[2860.86 --> 2861.76]  And a formal apology.
[2862.46 --> 2863.18]  Great meatballs.
[2863.72 --> 2864.20]  It's great.
[2864.56 --> 2865.24]  Everything's great.
[2865.62 --> 2871.06]  Speaking of popular opinions, could it be time to switch to some of that, Natalie?
[2871.06 --> 2871.16]  Bye-bye.
[2876.16 --> 2879.08]  I actually think she'd probably leave.
[2887.26 --> 2891.64]  Well, Johnny, as the person who brought this up, do you have one for us?
[2892.68 --> 2894.42]  Not to put you on the spot or anything.
[2894.42 --> 2898.76]  I will say that as we were doing the sound check, there was one sound that was a bit off.
[2898.92 --> 2901.04]  And I did, like, literally point fingers.
[2901.60 --> 2903.06]  So first this, now putting you on the spot.
[2903.22 --> 2903.66]  Sorry, Johnny.
[2903.92 --> 2905.48]  It seems like it's my apology podcast.
[2906.60 --> 2907.78]  Your apology tour.
[2908.28 --> 2909.10]  Yeah, your apology tour.
[2910.52 --> 2911.42]  Unpopular opinion.
[2912.68 --> 2913.88]  How about we circle back to me?
[2913.98 --> 2921.28]  Because I'm trying to think of how to articulate mine in a non-IKEO offending way like you've done.
[2921.28 --> 2924.36]  I was not part of unpopular opinion.
[2924.64 --> 2925.36]  That's the worst part.
[2925.70 --> 2926.26]  That's right.
[2926.78 --> 2932.94]  I feel like I've dropped so many unpopular opinions just casually through the length of the show.
[2933.38 --> 2936.30]  Do you have one for wrapping up?
[2936.54 --> 2938.26]  I don't know if it's an unpopular opinion.
[2938.50 --> 2941.88]  Well, I can make it an unpopular opinion in the context of this podcast.
[2941.88 --> 2953.24]  But, like, I feel like Python 3.11 is trying to copy some of the better syntactic features of Go for relevance.
[2953.24 --> 2974.30]  And the part where I think it's an unpopular opinion is I could see a world where it continues or further dominates in, like, programming language market share by just stealing a couple of decent ideas and, like, continuing to live as the lazy person's scripting language.
[2974.30 --> 2977.94]  So if you have to summarize that into a tweet that we can vote upon.
[2979.94 --> 2986.38]  If I had to tweet this out, like, 140 characters just be Python 3.11 is going to kill Go.
[2986.78 --> 2987.08]  Okay.
[2987.30 --> 2990.90]  Which is probably going to make it high in the unpopular opinion board.
[2991.26 --> 2991.46]  Yeah.
[2991.56 --> 2992.76]  I mean, it's super unpopular.
[2992.88 --> 2994.22]  It's not that I agree with it.
[2994.22 --> 3007.92]  But I'm saying, like, if you just steal a couple of ideas and then the laziest freaking programming language that most people use to, like, just kind of script their way out of a paper bag suddenly has a couple of, like, the nice features of Go.
[3008.04 --> 3013.56]  And you go, just stick around here until I'm ready to wade into the pool of being an actual good developer.
[3014.08 --> 3016.04]  I'm going to just be cool over here.
[3016.26 --> 3016.36]  Right.
[3017.30 --> 3019.02]  The AI will change that.
[3019.12 --> 3021.04]  And we have to have another podcast about this.
[3021.04 --> 3024.80]  This is a topic that barely even opened, but we were definitely planning to.
[3025.70 --> 3027.34]  Ivan, do you have an unpopular opinion?
[3028.02 --> 3028.24]  Yeah.
[3028.30 --> 3034.02]  I tried to think of one, but, you know, it's a kind of completely different field from programming.
[3034.42 --> 3036.58]  So it kind of makes me feel inadequate now.
[3037.68 --> 3044.04]  But anyway, yeah, the one that I thought of was actually, I don't think that there is such a thing as free will.
[3044.24 --> 3050.20]  So I think that everything that you've ever thought and everything that you will ever do is actually a chemical process in your brain.
[3050.20 --> 3055.14]  That is a result of the state that was in your brain at T minus one millisecond.
[3056.00 --> 3067.58]  And in that sense, unless you can prove to me that there is some sort of soul or spirit or something, then you cannot, like, I would not be able to place the location where this free will would be located.
[3068.10 --> 3069.10]  You went broad, man.
[3069.22 --> 3070.44]  Like, you really...
[3070.44 --> 3071.28]  Oh, yeah, I did.
[3071.66 --> 3072.04]  Sorry.
[3072.58 --> 3074.58]  This is what security does to people.
[3074.62 --> 3076.20]  Also, Java is crap.
[3076.92 --> 3077.28]  Yeah.
[3077.64 --> 3078.20]  Oh, wow.
[3078.20 --> 3082.54]  Also, here's his other bomb I'm going to drop.
[3082.64 --> 3085.38]  We have no free will and screw Java, right?
[3085.72 --> 3086.28]  Screw Java.
[3086.52 --> 3086.78]  Fair.
[3087.06 --> 3087.18]  Yeah.
[3088.46 --> 3089.98]  Those things are related in his mind.
[3090.74 --> 3091.58]  That is beautiful.
[3092.12 --> 3093.30]  Straight nihilism, man.
[3094.18 --> 3102.62]  I, my unpopular opinion and I don't know, like, I have a nasty habit of thinking my opinions are unpopular, but they end up being popular.
[3102.62 --> 3104.70]  Except that one time I actually did have an unpopular opinion.
[3105.32 --> 3120.50]  But anyways, my unpopular opinion is that I think with the advent of these generative AI tools that can understand language and generate language and everything else, while it is easy to leverage these tools.
[3120.50 --> 3127.02]  And I speak from somebody who pays for GitHub Copilot and I use it and I like it.
[3127.46 --> 3138.86]  While these tools may make the act of building and writing code easier and faster, the responsibility, right, still lies with you, the developer.
[3138.86 --> 3147.24]  I think we're entering an age where you're going to learn not really how to write code, but how to proofread code.
[3147.42 --> 3156.26]  Because if you can have machines, like a model generate code for you, then the only thing you're doing is verifying that it's doing the right thing.
[3156.26 --> 3166.54]  And right now I find that about 50% of the things I'm generating from something like a GitHub Copilot, like I have to tweak because it's not quite what I want.
[3166.60 --> 3169.96]  But that's still 50% of typing that I don't have to do, right?
[3169.98 --> 3171.80]  So it has, it does help me.
[3171.84 --> 3174.04]  It has given me a boost of productivity, no doubt.
[3174.68 --> 3176.04]  And I'm glad to pay for it.
[3176.06 --> 3179.24]  But the responsibility of understanding what it is that it's generating.
[3179.24 --> 3188.50]  And to me, it's like back in the day where I'd look at a website and I was learning how HTML or how website work, I'd do view source.
[3189.24 --> 3193.00]  I think, you know, corollary here being that you can get the equivalent of a view source.
[3193.18 --> 3196.64]  You can get source code, right, from the cloud, from something in the cloud.
[3197.16 --> 3201.54]  But it was still up to me to understand what HTML tags were.
[3201.68 --> 3202.68]  What does a P tag do?
[3202.80 --> 3204.20]  What does a image tag do?
[3204.32 --> 3207.10]  What does it, you know, if I add this attribute to this tag, what does it do?
[3207.10 --> 3209.12]  Like, you still have to understand, right?
[3209.12 --> 3212.12]  You get a leg up, but you still have to understand what it is that you're getting.
[3212.32 --> 3228.14]  So just because you're going to get tools doesn't mean the responsibility of said code, either the productivity, whether it's the benefit or the chaos that ensues from you using that code and, you know, shipping into production and all that stuff.
[3228.54 --> 3230.72]  You are still responsible for that code, right?
[3230.72 --> 3241.28]  And I would probably be harsher on you as a developer who commits generated code and doesn't really verify it, proofreads it, and fix it.
[3241.78 --> 3247.94]  I'd be much harder on you knowing that's what you did, right, if you actually wrote the code yourself, right?
[3247.96 --> 3250.02]  If you wrote the code yourself, I know, okay, it's human error.
[3250.32 --> 3253.34]  Maybe we need better practices for code review and everything else.
[3253.34 --> 3259.48]  But if you're just blindly generating code and getting in there and shipping it, then I'm going to be much harsher on you.
[3260.16 --> 3263.88]  The BuzzFeed listicles basically write themselves, right?
[3263.94 --> 3273.90]  Like this developer checked in random chat GBT code to Google 3 and took down like half of ads for like 45 minutes, right?
[3273.90 --> 3278.74]  There's ways in which you can see the laziness kind of like potentially kicking in.
[3278.84 --> 3279.60]  I think you're right.
[3279.76 --> 3292.52]  And it's interesting because you see certain like, I see certain developers like on YouTube, I'll still watch people who can actually program even if I can't, who are just talking about like, oh, well, there's this productivity boost from Copilot.
[3292.68 --> 3296.20]  There's also this drag that comes with having to like sit there and interpret code.
[3296.62 --> 3297.22]  Welcome to my word.
[3297.48 --> 3298.26]  Yeah, exactly.
[3298.38 --> 3299.64]  Like that's what we do all day.
[3299.72 --> 3300.70]  Like there's no problem.
[3300.70 --> 3303.50]  I'm like most of we don't, I can't speak again.
[3303.66 --> 3304.48]  I don't know how much you do.
[3304.56 --> 3306.92]  I've been personally, I don't write that much code.
[3307.46 --> 3310.10]  Most of the time I'm trying to interpret code.
[3310.22 --> 3319.58]  So the idea that I have a thing that's going to write, you know, 70% relevant code for me and I could just template that that's, you know, massive on my end.
[3320.00 --> 3329.54]  But yeah, I don't know how it actually affects the sort of day to day and the ritual and the process of folks that are more caught up in generation than for us.
[3329.54 --> 3329.76]  Right.
[3329.76 --> 3330.36]  Yeah.
[3330.36 --> 3335.36]  Although, I mean, from my perspective, your opinion, Johnny, seems to be extremely popular.
[3336.54 --> 3337.42]  I told you.
[3338.72 --> 3349.96]  I can't for the life of me imagine like some guy breaking stuff because he pasted code from either Stack Overflow or GitHub Copilot and then complaining and then getting a positive response from Reddit or Twitter.
[3350.16 --> 3351.62]  Like I don't see that happening ever.
[3351.62 --> 3356.36]  I remembered my unpopular opinion and I'm actually glad that I'd forgotten it.
[3356.48 --> 3357.48]  I think we're good.
[3357.68 --> 3358.90]  Let's let Natalie.
[3359.28 --> 3360.44]  Let sleeping dogs lie.
[3362.44 --> 3363.08]  I'm okay.
[3363.12 --> 3364.02]  I don't need the hate mail.
[3364.12 --> 3364.52]  It's fine.
[3364.52 --> 3369.04]  So my unpopular opinion is about music, specifically Eurovision.
[3369.04 --> 3371.70]  And it has some background story.
[3372.26 --> 3373.90]  So last year there was a band that was...
[3373.90 --> 3374.80]  Did you offend them as well?
[3375.28 --> 3376.88]  Oh, you're about to.
[3377.08 --> 3377.22]  Okay.
[3377.22 --> 3378.72]  No, no, no, no, no.
[3378.76 --> 3379.26]  I love them.
[3379.92 --> 3380.50]  No, no.
[3380.58 --> 3381.16]  I like them.
[3381.70 --> 3383.68]  So there's a great band that's called...
[3383.68 --> 3386.54]  Their new name is Electric Cowboy.
[3387.12 --> 3389.86]  And in the beginning they had the name Eskimo Cowboy.
[3389.98 --> 3391.16]  They applied for the Eurovision.
[3391.32 --> 3393.18]  Many people loved them last year, 2022.
[3394.02 --> 3397.36]  They were rejected partially because of the name.
[3397.44 --> 3399.06]  That's one of the reasons they changed it.
[3399.94 --> 3401.58]  And then they ended up being...
[3401.58 --> 3406.00]  Not making it to the Eurovision to be the German entry.
[3407.36 --> 3411.08]  For all the American listeners, Eurovision is like a competition of all...
[3411.08 --> 3415.24]  Of music between the European countries and some editions like Australia.
[3415.50 --> 3417.60]  It's like The Voice but with nationalism.
[3418.22 --> 3420.28]  It's something that was...
[3420.28 --> 3423.14]  That started after all the world wars as a...
[3423.14 --> 3425.52]  Like this is where we all laugh at ourselves in a good way.
[3425.52 --> 3427.68]  So it's always glamorous and amazing.
[3428.38 --> 3430.70]  It's always around May or so.
[3431.10 --> 3433.16]  And then the winning country gets to host it and so on.
[3433.20 --> 3435.98]  And every year like the entries is a wide range.
[3436.06 --> 3438.46]  It's a super fascinating, fun, love it.
[3438.96 --> 3442.98]  So the German band Electric Cowboy, they did not make it.
[3443.04 --> 3446.60]  And then there were petitions to allow them to be the entry.
[3446.86 --> 3447.78]  And this was...
[3447.78 --> 3451.36]  Germany generally works in the sense that if enough people sign the petition,
[3451.50 --> 3453.60]  the government has to take it seriously and discuss that.
[3453.96 --> 3455.18]  This is not a government issue.
[3455.18 --> 3455.48]  Yeah.
[3455.88 --> 3457.10]  But Germans do petitions.
[3457.22 --> 3457.84]  So there was a petition.
[3457.96 --> 3460.68]  This was not accepted by the Eurovision Committee for Germany.
[3461.06 --> 3462.14]  Whoever is responsible.
[3462.70 --> 3464.80]  And they were eventually rejected.
[3465.06 --> 3468.86]  There was another entry which was nice but made it super low and was...
[3468.86 --> 3472.46]  Okay, so I'm not really Eurovision material, if you ask me.
[3473.46 --> 3475.96]  And then this year's entry is a...
[3475.96 --> 3476.74]  It's a good band.
[3476.82 --> 3477.32]  It's a nice band.
[3477.38 --> 3478.02]  I didn't know them.
[3478.02 --> 3482.46]  It almost feels like another version of this rejected band.
[3482.46 --> 3483.46]  But...
[3483.46 --> 3485.60]  And this is probably where I'm offending them.
[3485.66 --> 3486.24]  I think you're nice.
[3486.30 --> 3489.36]  You're not as good as Electric Cowboy.
[3489.64 --> 3491.48]  And here comes the unpopular opinion.
[3491.84 --> 3493.20]  Germany made a mistake here.
[3493.20 --> 3496.40]  And they should have corrected this year.
[3496.40 --> 3498.82]  But they solved it in a patch.
[3499.32 --> 3500.78]  Here's the long unpopular opinion.
[3501.38 --> 3502.94]  Good luck summarizing that into a tweet.
[3502.94 --> 3506.36]  I was trying to duck out of the screen.
[3506.74 --> 3509.34]  You know, just be left out of this one.
[3509.44 --> 3513.72]  Well, hey, if we have a Twitter blue, we can actually post a whole book in a tweet now.
[3514.00 --> 3515.00]  So it'll...
[3515.00 --> 3517.08]  You can basically do whatever you want on Twitter now.
[3517.22 --> 3518.54]  The rules are out.
[3519.12 --> 3520.56]  You can't use the API.
[3520.88 --> 3525.18]  But for $8, like, you could probably take a tour of the data center at this point.
[3529.12 --> 3530.74]  I hear an apology next episode.
[3531.44 --> 3531.96]  No, no.
[3532.06 --> 3532.80]  This one's fine.
[3532.94 --> 3533.94]  We're okay with this.
[3534.38 --> 3537.20]  We don't know if Twitter will still be here for the next episode.
[3537.48 --> 3538.06]  So it's just...
[3538.06 --> 3539.88]  They don't have a PR department anyway.
[3540.10 --> 3541.40]  So, like, there's nobody to complain.
[3541.74 --> 3541.90]  Oh.
[3543.56 --> 3544.12]  It's true.
[3544.26 --> 3544.64]  It's true.
[3545.30 --> 3545.92]  Oh, God.
[3546.14 --> 3546.22]  Yeah.
[3546.22 --> 3546.54]  Wow.
[3546.74 --> 3546.96]  Wow.
[3547.46 --> 3547.68]  Yeah.
[3547.76 --> 3551.46]  Maybe Elon will hear your rant.
[3551.58 --> 3552.96]  And maybe Elon will show up on the show.
[3553.26 --> 3555.70]  And Elon, if you're listening to GoTime.
[3555.86 --> 3556.24]  GoTime.
[3556.36 --> 3556.84]  And you should.
[3556.92 --> 3557.90]  This is very good content.
[3558.18 --> 3558.86]  Mr. Musk.
[3559.26 --> 3560.46]  If you do hear...
[3560.46 --> 3562.08]  We know that many of your companies use Go.
[3562.40 --> 3562.78]  Please join.
[3562.78 --> 3563.42]  We do.
[3563.54 --> 3563.80]  We do.
[3564.26 --> 3564.72]  So, yeah.
[3564.90 --> 3566.50]  Come join us for an episode.
[3566.88 --> 3567.70]  We'd love to host you.
[3567.90 --> 3572.84]  We'll all smoke weed and just talk about Go and not make fun of Twitter.
[3573.24 --> 3574.38]  It'll be perfect.
[3576.14 --> 3579.00]  We can promise some of those things, but it'll definitely be fun.
[3579.00 --> 3580.20]  All right.
[3581.16 --> 3582.22]  Many thanks for joining.
[3582.48 --> 3584.92]  Still some open conversation topics.
[3585.12 --> 3586.98]  So, maybe in episode five coming up.
[3587.12 --> 3587.58]  Who knows?
[3588.12 --> 3589.70]  Have a great rest of your day.
[3589.94 --> 3592.12]  Everybody who listened or will listen to this later.
[3592.46 --> 3593.56]  And thank you, Ivan.
[3593.70 --> 3594.30]  Thank you, Jax.
[3594.34 --> 3594.90]  Thank you, Johnny.
[3594.90 --> 3596.08]  Thanks, guys.
[3596.08 --> 3596.10]  Thanks, guys.
[3601.92 --> 3602.90]  All right.
[3603.12 --> 3604.54]  That is GoTime for this week.
[3604.86 --> 3605.54]  Thanks for listening.
[3606.12 --> 3609.78]  If you dig it, share the show with your friends and colleagues at work.
[3609.78 --> 3616.38]  And if you get a lot of value from GoTime and our other pods, return some value with a Changelog++ membership.
[3616.82 --> 3622.58]  As a thanks for your support, we hook you up with an ad-free feed, extended episodes, and more.
[3622.58 --> 3626.60]  Check it out at changelog.com slash plus plus.
[3627.44 --> 3630.56]  Thanks once again to our partners for helping us bring GoTime to you.
[3630.84 --> 3633.58]  Check out fastly.com and fly.io.
[3633.82 --> 3636.38]  Thanks also to our breakmaster in residence.
[3636.72 --> 3639.50]  The mysterious BMC bumps out all of our beats.
[3640.10 --> 3651.22]  Next time on GoTime, Matt and Natalie welcome Lee Anthony from The Whales Project and Andy Williams from Fine to discuss building cross-platform GUI apps in Go.
[3651.22 --> 3652.92]  Stay tuned right here.
[3653.04 --> 3656.08]  We'll ship that episode in your podcast app next week.
[3656.08 --> 3657.08]  Bye.
[3681.22 --> 3685.04]  Bye.
[3685.08 --> 3686.28]  Bye.
[3686.34 --> 3687.72]  Bye.
[3687.92 --> 3687.98]  Bye.
[3688.02 --> 3688.30]  Bye.
[3688.36 --> 3689.48]  Bye.
[3689.54 --> 3689.98]  Bye.
[3689.98 --> 3690.74]  Bye.
[3691.10 --> 3692.52]  Bye.
[3692.56 --> 3694.14]  Bye.
[3694.14 --> 3694.40]  Bye.
[3694.42 --> 3695.34]  Bye.
[3695.56 --> 3695.78]  Bye.
[3701.20 --> 3702.16]  Bye.
[3702.16 --> 3705.84]  Bye.
[3705.90 --> 3706.98]  Bye.
[3706.98 --> 3708.08]  Bye.
[3708.10 --> 3709.12]  Bye.
[3709.38 --> 3710.48]  Bye.
