[0.00 → 17.88] Welcome to the Changelog episode 0.4.4.
[18.08 → 19.12] I'm Adam Stachowiak.
[19.38 → 20.24] And I'm Wend Netherlands.
[20.42 → 21.36] This is the Changelog.
[21.42 → 23.36] We cover what's fresh and new in the world of open source.
[23.70 → 26.70] If you found us on iTunes, we're also on the web at thechangelog.com.
[27.08 → 27.92] We're also up on GitHub.
[27.92 → 34.32] At thegithub.com slash explore, you'll find some training repos, some feature repos from our blog, as well as the audio podcasts.
[34.64 → 38.68] If you're on Twitter, follow ChangeLog Show and our new Twitter handle, ChangeLog Jobs.
[38.86 → 39.62] And I'm Adam Stack.
[40.32 → 42.78] And I'm Penguin, P-E-N-G-W-Y-N-N.
[43.22 → 46.14] Talked to Aaron Patterson this week, a.k.a. Tinder Love.
[46.72 → 48.30] Yeah, tenderlovemaking.com.
[48.32 → 50.02] Did you guys talk about tender lovemaking?
[50.76 → 52.20] No, not in that context.
[52.34 → 55.44] We talked about committing to Ruby Core, which he's a Ruby committer.
[55.44 → 57.86] He's got many gems.
[58.28 → 60.84] He's got quite the repo list out on the GitHub.
[61.36 → 68.64] And the rubycommitters.org that he's currently crowdsourcing for design help to list all the committers to the Ruby language.
[68.94 → 69.70] Wow, very cool.
[69.80 → 70.40] Sounds like fun.
[71.00 → 71.98] Hey, you want to get buzzed at work?
[72.70 → 73.16] I don't know.
[73.22 → 73.50] Maybe.
[74.16 → 76.04] Not talking about alcohol or even caffeine.
[76.18 → 77.84] We're talking about buzzed.com.
[78.26 → 79.68] Drop the E before adding the D.
[79.68 → 85.50] Your City Real Time is looking for Go developers, JavaScript, Cappuccino, Cocoa, and even PHP.
[86.14 → 90.76] And if you'd like us to feature your job on the show, head to the changelog.com slash jobs to get started.
[91.18 → 94.74] When posting, select Advertise on the changelog, and we'll take care of the rest.
[95.32 → 99.18] If you're a jobseeker or someone who's interested in jobs that relate to open source,
[99.18 → 105.00] we'll be posting interesting GitHub jobs that embrace open source to our new Twitter handle, changelog jobs.
[105.38 → 110.28] Special thanks to Kevin Miller, a.k.a. Kev M, on Twitter for his great feedback.
[110.66 → 111.60] We really appreciate it.
[112.14 → 115.92] Let's talk to James Edward Gray about the upcoming Red Dirt Rubicon in April.
[116.22 → 116.72] Let's do it.
[117.30 → 121.92] This week's show is sponsored by Red Dirt Rubicon, the second annual Ruby conference in Oklahoma City.
[122.30 → 124.94] Joined today by one of the organizers, James Edward Gray II.
[125.80 → 128.08] James, why don't you tell us a little bit about the conference?
[128.08 → 137.44] Red Dirt is our attempt to do Ruby conference programming in unusual ways that people have never seen it done before.
[137.98 → 146.26] So one thing we did last year, and we're doing again this year is to divide the conference into pre-selected topics
[146.26 → 149.16] that we think are currently interesting to people.
[149.16 → 157.78] And this year's topics will be Ruby implementations, Rails APIs and extensions, cloud services,
[158.08 → 159.94] and JavaScript.
[160.48 → 161.22] Who's keynoting?
[161.78 → 169.20] We will have Aaron Patterson from AT&T Interactive and Dr. Nick from Engine Yard.
[169.86 → 172.98] The conference is upcoming April 20th through the 22nd.
[173.32 → 174.94] Where can they go to find more information?
[175.64 → 178.62] The Red Dirt RubyConf.com.
[178.62 → 180.22] Be sure and check it out.
[189.02 → 195.16] We're chatting today with Aaron Patterson, a.k.a. Tinder Love on GitHub and other social networks.
[195.38 → 198.50] So Aaron, for those outside the Ruby community, why don't you introduce yourself?
[200.02 → 201.60] My name is Aaron Patterson.
[201.60 → 205.50] I go by Tinder Love online pretty much everywhere.
[207.64 → 210.88] I work on many different Ruby projects.
[211.18 → 217.38] Probably I'm most famous for one that I work on with Mike D'Alessio called Nokogiri,
[217.62 → 220.72] which is an XML and HTML parsing library.
[220.94 → 224.94] But I have a myriad of other projects too.
[226.50 → 227.18] Cool.
[227.28 → 228.88] So Tinder Love, where did that come from?
[228.88 → 238.06] Um, that, so it came from my blog, um, tendralovemaking.com.
[238.72 → 247.48] And, uh, basically the way I got that is I was hanging out with, um, a bunch of my girlfriends
[247.48 → 253.88] and they were talking about, you know, girlfriends, plural, friends that are friends that are women.
[255.08 → 255.68] Okay.
[255.90 → 256.46] Okay.
[256.46 → 265.88] Uh, and, and they were talking about, oh, what's, what's the, uh, the grossest thing a guy can ever say to you?
[266.46 → 274.46] And my one, my one friend was like, oh, if he says, I want to make Tinder Love to you, that would be the grossest.
[274.46 → 274.86] Grossest.
[275.20 → 278.70] So I registered the domain name.
[278.78 → 280.42] I had to, I was laughing so hard.
[280.56 → 284.52] I registered the domain name and then, uh, sent it to her the next day.
[284.52 → 293.78] Well, the next question that I wanted to ask, you know, the very first time that I saw you on, uh, Twitter or GitHub was, is that your real hair?
[297.26 → 299.04] Um, yes.
[302.86 → 305.82] So can we edit this part out?
[305.88 → 307.56] Do we have to, do I have to say this?
[307.56 → 311.30] As with all our segments, we'll have to, to judge the entertainment value of it.
[311.76 → 312.06] Okay.
[312.22 → 318.98] So, so, um, uh, that is up to the viewer to decide.
[320.84 → 323.38] But it's your online persona nonetheless, right?
[323.78 → 324.10] Right.
[324.26 → 324.64] Yes.
[325.10 → 328.84] Well, it fits very nicely with, um, it seems like your taste in music.
[328.84 → 337.60] You had a tweet this weekend that was, uh, hot linking to a hot-blooded, I guess.
[338.12 → 338.56] Exactly.
[338.92 → 339.40] Absolutely.
[340.92 → 341.36] Cool.
[341.44 → 342.22] Well, getting into the Ruby.
[342.34 → 346.28] So Nova Gear is probably, um, what you're most famous for.
[346.36 → 349.42] You also have, um, mechanized and some others out there.
[349.54 → 354.80] Uh, but you're most recently, I guess in October you joined, uh, the Ruby core team, right?
[355.42 → 356.48] Uh, yeah.
[356.48 → 358.82] October 2009, a little over a year.
[358.84 → 360.22] You know, and I read that timestamp.
[360.36 → 361.74] I can't believe it's 2011 or anything.
[361.90 → 367.24] So yeah, it's been over a year now, but, uh, so what's it like, um, being a Ruby committer?
[368.12 → 371.90] Uh, oh, it's, I mean, it's all right.
[371.94 → 374.02] It's more, I don't know.
[374.04 → 379.42] It's probably stricter than any other, any other, um, project I've worked on.
[379.48 → 384.92] I mean, it's definitely the biggest, um, open source project I've worked on before.
[385.12 → 388.34] So, um, I don't know.
[388.34 → 392.40] It's, it's got its own challenges compared to the other projects I work on for sure.
[393.90 → 396.08] So that leads me to Ruby committers.org.
[396.40 → 398.70] So here's how I think this went down.
[398.78 → 402.48] You know, you wanted to tell the ladies that you're a Ruby committer, and they're like, what's
[402.48 → 402.76] that?
[402.90 → 406.36] And there's just no page to demonstrate your Ruby prowess, right?
[408.92 → 411.28] No, no, not at all.
[411.78 → 417.98] Um, I, I came up with this, I came up with this because, um, uh, you gooey who is the
[418.12 → 423.82] she is the, um, the branch manager for one night Ruby one nine two.
[423.82 → 428.74] Uh, she maintains a list of all the Ruby core committers.
[428.74 → 436.00] And, but apparently like in Japan, it's not legal to hot link images.
[436.00 → 442.98] And so she can't, she couldn't make a page that listed all the Ruby core committers.
[443.24 → 445.40] And, um, I don't know.
[445.46 → 450.20] I'm honestly, I'm not sure about the legality here in the United States, but I figure if I
[450.20 → 452.36] get any cease and desist, I can just take it down.
[452.36 → 452.64] Right.
[452.64 → 459.58] So I decided, I decided we should, uh, put together a website for it at least.
[459.94 → 460.44] Yeah.
[460.48 → 465.52] I mean, especially for folks that are so critical to getting everybody's favourite language, uh,
[465.52 → 469.82] out the door with, uh, relative speed, you know, I think that deserves their own page,
[469.82 → 472.70] but, uh, so a little light on the CSS I'm seeing.
[473.30 → 473.70] Yeah.
[473.70 → 477.58] I understand there's some sort of, uh, contest going on to, to style this thing.
[478.08 → 478.52] Yeah.
[478.60 → 478.82] Yeah.
[478.82 → 485.58] So, so basically what the deal is, is, um, I, I might be able to code okay, but I can't
[485.58 → 487.74] style myself out of a wet paper bag.
[487.96 → 494.70] So I decided to put up the most, just give it the most basic markup possible.
[494.70 → 501.64] And then, um, I, I wanted to run a contest basically to just get, get people excited about
[501.64 → 504.74] it and get people to, you know, submit designs and stuff.
[504.74 → 511.14] And so far it's been, I mean, I've only had the contest up for a day, and I've already got,
[511.24 → 513.64] you know, a handful of really awesome entries.
[514.20 → 515.30] So what'd you build it with?
[516.16 → 518.74] Um, it is built on rails, of course.
[518.96 → 521.04] All the way with rails, no Sinatra or.
[522.00 → 531.02] Um, no, I mean, I, I am lazy and building the app with rails was very easy.
[531.02 → 532.02] So I just did it.
[532.02 → 534.28] So how long have you been slinging Ruby?
[535.12 → 543.04] Um, I started programming Ruby in, uh, 2005, I think.
[543.16 → 543.56] Yeah.
[543.56 → 545.72] Around 2005 is when I started programming Ruby.
[546.08 → 550.30] Um, my first, I just did it as a hobby at first though.
[550.82 → 558.62] Um, my first professional experience was probably shoot 2006 or 2007.
[558.62 → 559.44] Something like that.
[559.44 → 562.02] So how did you get into the Ruby language via rails?
[562.26 → 564.54] Like most of us or other avenues?
[565.32 → 572.56] Um, well, actually the way I started out with it was, um, so I used to be, I used to be a
[572.56 → 573.28] Pearl programmer.
[573.54 → 574.14] No.
[574.52 → 576.34] And yes, yes, I did.
[576.72 → 579.20] And I loved, I love being a pro programmer.
[579.20 → 579.94] It was really fun.
[580.04 → 581.90] I liked, um, dynamic languages.
[581.90 → 588.10] And then, um, I was basically forced to become a Java programmer.
[588.88 → 597.64] Uh, it, so I, I was a pro programmer before the first, you know, dot com bubble and, you
[597.64 → 598.72] know, the bubble collapsed.
[599.00 → 605.46] And basically it was like, okay, you need to become a Java programmer or, you know, go find
[605.46 → 606.00] a new job.
[606.00 → 608.62] So I was like, all right, I'll become a Java programmer.
[609.62 → 614.76] But I really missed, I really missed, um, dynamic languages while I was a Java programmer.
[614.76 → 622.00] And I kept waiting for Pearl six and kept waiting and waiting, and it didn't come.
[622.56 → 624.66] Well, then it hadn't come.
[624.80 → 630.20] And I learned about Ruby, and I was like, this, this is exactly what I was waiting for.
[630.66 → 635.64] And just started programming Ruby little, a little later I learned about rails.
[636.22 → 640.70] So I, I guess I was not introduced to Ruby via rails.
[640.70 → 646.34] Uh, Nagari, I think, uh, is one of those that, uh, the first time I saw it, it was just
[646.34 → 649.22] as a dependency for almost every other gem that I was installing at the time.
[649.34 → 653.20] Why don't you give, give folks some background on what this, uh, gem does.
[654.02 → 654.46] Sure.
[654.60 → 654.92] Sure.
[655.10 → 662.24] Um, Nagari is a library for, uh, parsing, um, XML and HTML.
[662.92 → 664.96] Uh, it's pretty fast.
[665.30 → 668.30] Um, it's now three years old.
[668.30 → 671.90] Um, it was built on top of lib.
[672.02 → 672.56] XML too.
[673.72 → 676.88] Um, I don't know.
[677.00 → 678.74] I, I can give you more history.
[678.96 → 679.56] I don't know.
[679.64 → 680.72] What were you building at the time?
[680.80 → 684.68] Uh, you need to scrape some stats off of a fantasy football side or something like that.
[685.22 → 691.30] Yeah, no, I, I was basically what, what happened was, is, you know, I was maintaining, I was
[691.30 → 692.76] maintaining a mechanized gem.
[692.76 → 699.78] Um, so this, actually this all leads back to, um, how I learned Ruby pretty much is when
[699.78 → 706.06] I started learning Ruby, I decided to start porting, porting libraries from, uh, Pearl over
[706.06 → 706.50] to Ruby.
[707.98 → 713.48] And, uh, one of the things that I used a lot in Pearl was mechanized, and I found somebody
[713.48 → 715.60] had already written a mechanized gem.
[715.60 → 721.78] Um, so, but I found tons of bugs in it and that eventually just led to me taking over
[721.78 → 722.22] the gem.
[722.92 → 728.96] Uh, unfortunately back then the backend for mechanized used, um, REX ML.
[729.64 → 733.18] Uh, REX ML is the XML library that ships with Ruby.
[733.30 → 735.88] It's a pure Ruby XML parsing library.
[736.34 → 740.56] But, um, lots of people complained that that was really slow.
[740.56 → 749.18] So, uh, eventually I switched the backend to Apricot by Y and that worked, that was working
[749.18 → 749.90] really well.
[750.12 → 753.06] But, uh, I started getting, I started getting bugs.
[753.20 → 759.76] People were reporting bugs against mechanized and the bugs ended up being parser bugs in Apricot.
[759.90 → 764.60] And I couldn't like, I had a really hard time fixing the bugs in Apricot.
[764.80 → 768.40] So I ended up just submitting test cases, failing test cases and stuff.
[768.40 → 775.52] And unfortunately those didn't get taken care of and people kept complaining to me about
[775.52 → 776.00] the bugs.
[776.18 → 781.60] So, uh, I started taking a look at LibXML2 because it contains an HTML parser.
[781.84 → 788.36] And I found that actually LibXML2's HTML parser did the right thing where all of these people
[788.36 → 789.44] were reporting bugs.
[789.88 → 793.56] And that's how I started working on Nokogiri.
[793.56 → 797.66] So for the uninitiated, uh, mechanized is pretty much if you have a website, you have
[797.66 → 799.22] an API type of setup.
[799.22 → 799.46] Yeah.
[799.72 → 799.98] Yeah.
[800.08 → 800.28] Yeah.
[800.28 → 804.92] It's, it's basically a library where if you, if you have a website, and you need an API for
[804.92 → 806.38] the website, you can use mechanized.
[806.92 → 813.84] So it's perfect for mechanized is perfect for, let's say you have mainly like password
[813.84 → 818.02] protected websites or some sort of, some sort of website where you have to fill out forms
[818.02 → 820.06] and do navigation, things like that.
[820.06 → 825.16] So moving from Pearl to Ruby, you know, you mentioned, uh, one of the ways that you learned
[825.16 → 827.38] Ruby was to, to port libraries from Pearl.
[827.42 → 830.10] And I think that happens in every, uh, community.
[830.10 → 834.56] I know it happens now with, uh, in Node.js, you see a lot of guys coming from other communities
[834.56 → 840.20] and there's, you know, a hole in the, the library that, uh, needs to be filled.
[840.20 → 843.64] And so they start porting their knowledge from, from other languages.
[843.64 → 845.74] And sometimes that fits and sometimes it doesn't.
[845.74 → 852.32] What, um, differences between like, not just the syntax, but also the, the culture of Pearl
[852.32 → 853.54] to, to Ruby, did you find?
[854.58 → 860.84] Um, well, honestly, like I found, I found testing in Ruby to be much easier than it was in Pearl.
[861.20 → 867.16] Um, I'm, I'm, I mean, I've been out of the Pearl community for a really long time, so
[867.16 → 868.04] I don't know what it's like.
[868.04 → 874.58] I don't know what it's like today, but back then, you know, testing was not really, not
[874.58 → 878.80] really, um, as encouraged as it is in the Ruby community.
[879.42 → 881.26] And now it's like a, you know, rite of passage.
[881.44 → 884.26] You're not a Ruby developer unless you've written your own test library, right?
[884.90 → 885.88] Pretty much.
[886.02 → 886.30] Yeah.
[887.36 → 888.10] What's your favourite?
[888.94 → 892.36] Um, right now, my favourite, my favourite now is mini test.
[892.48 → 895.98] Actually, that is my favourite testing library.
[896.18 → 896.64] Why so?
[896.64 → 901.58] Um, well, it's very fast.
[902.34 → 904.06] Uh, it's very flexible.
[904.62 → 907.92] And also I work with the, uh, I work with the author.
[908.08 → 912.48] So whenever I run into problems, I can just be like, Hey, help.
[914.42 → 917.50] What's your favourite feature or two from one nine two?
[918.18 → 919.14] Oh boy.
[919.34 → 921.32] My favourite feature is the speed.
[923.78 → 926.06] Um, I, I don't know.
[926.06 → 930.40] I mean, I guess I, I really like one nine two.
[930.56 → 935.02] I really like one nine two because of the speed, obviously, but then also kind of selfishly,
[935.06 → 938.90] I like it because there are a couple libraries in that ship with one nine two that I wrote.
[939.10 → 944.00] So I like using, I like using my own software.
[944.00 → 945.00] Which are those?
[945.00 → 951.50] Um, I wrote, uh, psych, which is a new YAML parsing library.
[951.50 → 958.16] And then I wrote, um, fiddle, which is a wrapper around lib FFI.
[958.16 → 958.20] Okay.
[958.66 → 960.78] So tell the listeners about textile.
[961.38 → 967.22] Textile was a stupid hack that I did and a very stupid hack that I did.
[967.22 → 968.84] And apparently people seem to use it.
[969.34 → 971.14] Um, all it is, is a wrapper.
[971.14 → 972.54] It's got such a fun name.
[972.78 → 974.18] Yeah, I guess.
[974.68 → 975.50] I don't know.
[975.56 → 977.56] I'm kind of embarrassed about the name now.
[978.56 → 981.42] A guy named tender love creates a library called textile.
[981.50 → 981.88] What's not?
[982.08 → 982.30] Yeah.
[982.50 → 984.42] What is the world coming to?
[984.42 → 991.60] It's what it, all it is, is a wrapper around, um, Postgres's T search APIs.
[992.22 → 998.42] So Postgres, Postgres ships with, um, full text search on.
[999.00 → 1004.98] And, um, I was building the I was building the Nokogiri documentation website.
[1005.66 → 1009.88] And, uh, I wanted to put it on, I wanted to put it on Heroku.
[1010.66 → 1014.04] And I wanted people to be able to search my documentation.
[1014.42 → 1021.88] Um, and I found that, um, you know, Heroku has, uses Postgres for their databases on the
[1021.88 → 1022.18] backend.
[1022.18 → 1028.98] And I found that, um, I could just use Postgres's, uh, full text search capabilities.
[1029.34 → 1035.90] And I wasn't too happy with the, um, existing T search plugins.
[1035.90 → 1043.22] So I wrote my own called textile, and it has a very similar interface to like, um, thinking
[1043.22 → 1044.34] Sphinx something.
[1044.72 → 1046.70] So, I mean, that's all it is.
[1046.72 → 1048.90] It's just, it's, I don't know.
[1048.94 → 1051.82] I probably wrote it in like a few hours.
[1051.98 → 1054.40] It is a very easy hack.
[1055.66 → 1058.28] So where does Tinder love to apply his skills for hire these days?
[1058.80 → 1061.56] Um, I work for AT&T interactive.
[1062.56 → 1066.30] Um, they make yellowpages.com.
[1066.30 → 1069.78] So that's got to be like an enthralling Thanksgiving conversation.
[1069.96 → 1071.80] So mom, I'm, I'm coding the phone book.
[1073.76 → 1075.86] Well, I, that's not actually what I do.
[1075.98 → 1077.64] That's not actually what I do for them.
[1078.10 → 1081.44] Uh, and, but it is difficult to explain my job.
[1081.58 → 1088.10] Um, so what I do for AT&T interactive is I work on, I work on rails all day for them.
[1088.10 → 1088.54] Basically.
[1088.54 → 1091.30] I am an open source developer for AT&T interactive.
[1092.22 → 1098.04] So do you find yourself having to, um, contribute to, or, uh, having the privilege to commit, uh, commit
[1098.04 → 1102.28] to, um, Ruby as part of your day job or is this just something you do on the side?
[1102.90 → 1104.48] Uh, no, this is my day job.
[1104.98 → 1109.20] So you're going to be keynoting at Red Dirt Rubicon coming up, I guess, in April.
[1109.88 → 1110.72] Yes, I am.
[1111.00 → 1111.82] Picked a topic yet?
[1112.28 → 1113.32] No, I have not.
[1113.92 → 1115.94] Do you have any, do you have any suggestions?
[1115.94 → 1118.78] How I, uh, just gave up and learned to love Ruby.
[1119.70 → 1123.12] Uh, yeah, I should talk about something like that.
[1123.68 → 1125.12] Yeah, I'm not, I'm not sure what to talk.
[1125.12 → 1126.14] The art of Tinder lovemaking.
[1126.26 → 1128.26] I think that's what everybody wants to know.
[1131.14 → 1132.26] I should do that.
[1132.34 → 1133.00] That would be funny.
[1134.42 → 1135.28] Yeah, I don't know.
[1135.38 → 1136.50] I don't know what to talk about.
[1136.62 → 1142.42] Honestly, like it takes me forever to come up with, um, to come up with talks.
[1142.42 → 1145.26] Like I work a lot on the talks I give.
[1145.26 → 1147.40] So, I don't know.
[1147.54 → 1149.66] Believe me, I've been thinking about it every day.
[1149.94 → 1150.12] So.
[1151.16 → 1153.32] So do you know James Edward Gray personally?
[1154.20 → 1158.34] Um, personally, I guess.
[1158.58 → 1160.24] I've met him, I've met him.
[1160.30 → 1162.18] How many times have you installed faster CSV?
[1162.52 → 1164.70] I have no idea.
[1164.84 → 1166.02] More times than I can count.
[1167.14 → 1168.44] And you guys are pretty tight.
[1168.84 → 1169.82] Yeah, exactly.
[1169.98 → 1170.30] Yes.
[1171.30 → 1173.08] Do you find it in the Ruby community?
[1173.18 → 1176.48] Maybe, uh, you can show some light on this if you've been around longer than I have.
[1176.48 → 1180.60] I think I joined the community in 2006, uh, late 2006 or so.
[1180.66 → 1186.34] But a lot of times, you know, someone says a name of a Ruby dev, and I'm like, I don't think
[1186.34 → 1186.78] I know them.
[1186.78 → 1188.66] And then they start rattling off the list of gems.
[1188.78 → 1189.82] Hey, I know that guy.
[1190.08 → 1190.30] You know?
[1190.90 → 1191.34] Oh yeah.
[1191.40 → 1191.62] Yeah.
[1191.62 → 1193.10] That happens to me all the time.
[1193.38 → 1193.74] Absolutely.
[1194.70 → 1197.10] So do people approach you as the Nokogiri guy?
[1197.36 → 1197.58] Yeah.
[1197.64 → 1200.22] Either Nokogiri guy or tender love, I think.
[1200.52 → 1207.26] But that's probably unique to me because, um, nobody has a nick like that.
[1207.92 → 1210.34] So is your family aware of your online persona?
[1211.46 → 1215.08] I mean, wouldn't your number, like if you ever did your own consulting shop, wouldn't your
[1215.08 → 1216.40] number have to be a 900 number?
[1219.08 → 1220.48] Uh, probably.
[1220.48 → 1224.04] You can make money off people, you know, calling you otherwise what would be toll-free?
[1224.38 → 1225.26] I think so.
[1225.38 → 1225.60] Yeah.
[1225.98 → 1232.74] Um, I, I don't think my family knows about my online persona.
[1232.74 → 1236.26] If they do know, then I don't know that they know.
[1236.72 → 1237.56] What kind of car do you drive?
[1238.08 → 1240.22] Uh, I don't drive.
[1240.40 → 1241.18] I work at home.
[1241.34 → 1244.60] So I just totally see you driving around in like a, uh, El Camino.
[1245.24 → 1250.44] Oh, I would love to either an El Camino or probably my dream car would be like, uh,
[1251.04 → 1255.94] an IRON Z or, uh, a Fire bird with T-Tops.
[1257.04 → 1258.04] T-Tops.
[1259.04 → 1260.54] So what are you working on these days?
[1260.86 → 1263.48] What's, uh, got you excited that you just want to play with?
[1263.96 → 1271.86] Well, right now, right now, um, I've been mainly focusing on, um, speeding up rails,
[1271.86 → 1276.72] uh, reducing, trying to refactor active record mostly.
[1277.24 → 1281.48] Uh, I'm not sure if that's, it's, it's a lot of yak shaving.
[1281.82 → 1282.66] I, I'm excited.
[1282.80 → 1287.02] I have ideas in mind for what it will be in the future, but you know, right now on a day
[1287.02 → 1289.38] to day basis, it's not actually super exciting.
[1289.42 → 1294.00] Once I get it to be where I want it to be, then I think it'll be very exciting.
[1294.48 → 1296.14] Performance or syntax changes or?
[1296.56 → 1297.82] A little bit of both.
[1297.82 → 1305.38] Mainly right now, I mean, mainly right now it's performance, but, um, really what I'm,
[1305.58 → 1310.50] really what my goals are is I want to keep, I want to keep API and syntax pretty much the
[1310.50 → 1310.82] same.
[1310.82 → 1316.84] Um, but my goal is that as I refactor, um, as I refactor under the hood and improve the
[1316.84 → 1323.32] design under the hood, that, um, new features will just fall into place, right?
[1323.54 → 1330.56] Like the, the new features or better syntax or whatever will be a side effect of, um, uh,
[1330.56 → 1332.60] better architecture under the hood.
[1333.14 → 1338.00] So a lot of innovation went into Errol and, and the latest, um, active record in, in rails
[1338.00 → 1340.16] three played with no SQL much.
[1340.16 → 1341.98] Are you still a relational sort of dude?
[1342.60 → 1344.42] Yeah, I dabble with no SQL.
[1344.56 → 1345.56] I play with no SQL.
[1345.56 → 1353.40] Um, one of my, one of my coworkers is really into, um, uh, graph databases and graph technology.
[1353.98 → 1355.64] And so I do a lot of work.
[1355.74 → 1358.42] I do a lot of work with him, and it's pretty interesting.
[1358.42 → 1367.66] He works on, um, he mainly works in Java, but, um, with things like, um, Neo4j and, uh,
[1367.66 → 1370.46] graph stores rather than document stores.
[1370.66 → 1375.86] You know, old Comity programmers used to put SQL right there in the, the presentation layer.
[1376.00 → 1376.80] And that's the way it was.
[1376.82 → 1381.28] And we liked it, but, uh, you know, we've got all these newfangled, uh, wrappers and
[1381.28 → 1383.80] direction now for, for SQL.
[1383.98 → 1388.26] Do you think that's important for young developers to give them more of a safety scissors than a
[1388.26 → 1388.78] razor blade?
[1388.78 → 1389.90] I don't know.
[1390.00 → 1391.16] It's, I think it's important.
[1391.32 → 1391.98] It's important.
[1392.54 → 1396.54] In my opinion, it's important that people understand SQL.
[1397.36 → 1403.22] Um, some of the things that, some of the things that concern me are that, um, I understand
[1403.22 → 1409.30] that it's nice to have a higher level wrapper, like better, you know, better APIs to, um,
[1409.96 → 1411.76] you know, to generate these SQL statements.
[1411.76 → 1415.78] But at the end of the day, that's pretty much all you're doing is generating these SQL statements
[1415.78 → 1416.58] that go to your database.
[1416.98 → 1422.44] And if you don't understand how those work, probably you can't leverage the top end as
[1422.44 → 1422.74] well.
[1423.28 → 1429.96] Um, I, I would like to see people get less afraid of SQL and understand it more.
[1430.36 → 1434.28] I was looking at your commits, and they're all Errol for the last, as far as the eye can
[1434.28 → 1434.56] see.
[1434.68 → 1437.72] So seeing through some ways to go with what you've been working on.
[1438.36 → 1438.92] Let's see.
[1438.98 → 1440.20] What else have I been working on?
[1440.26 → 1443.20] It's well, I can tell you what I'm doing with Errol.
[1443.48 → 1445.58] Active record currently active record.
[1445.58 → 1447.94] It does a lot of string generation in the backend.
[1448.16 → 1454.50] The problem with that, the problem with that is one of, well, there are a few problems with
[1454.50 → 1454.74] that.
[1454.96 → 1457.06] Like one of the problems is performance.
[1457.88 → 1463.38] So what's happening is like, sometimes you'll have to look up, you know, it's, it's creating
[1463.38 → 1468.14] a it's creating a raw string that it's just going to send, you know, a chunk of SQL that
[1468.14 → 1471.20] it's going to eventually concatenate together and then send to the database.
[1471.20 → 1479.80] But the problem is every time you make these chunks of SQL, um, you'll have to go look up
[1479.80 → 1487.78] the database connection and in order to do quoting and looking up the database connection
[1487.78 → 1488.96] incurs cost.
[1488.96 → 1489.42] Right.
[1490.00 → 1498.42] So basically what I'm trying to do is, uh, defer that, defer that database connection, look
[1498.42 → 1502.50] up until, um, the very last possible minute.
[1502.50 → 1506.32] So that we only have to look up the database connection once.
[1506.32 → 1511.54] So you gather together all the things that you want to turn into a SQL statement, and then
[1511.54 → 1516.30] we just use one connection to quote all of them and then send them off to the database.
[1516.72 → 1520.62] So that's like recently, that's really what I've been focusing on.
[1520.92 → 1526.90] So as a gem developer and especially a developer of a very popular gem in Nokogiri, uh, where
[1526.90 → 1532.78] are we in the adoption of Ruby one nine and, and the gem ecosystem as a whole?
[1532.78 → 1536.38] I, to be honest, I'm not sure.
[1536.54 → 1539.68] I mean, at work we don't, well, no, that's not true.
[1539.80 → 1547.32] We run, we run one nine in production at work, but not all of our applications use one nine.
[1548.40 → 1558.68] Um, I can tell you that I'm getting a lot more, uh, not necessarily bug reports, but like
[1558.68 → 1563.50] support questions and, you know, whenever people ask me for support, I say, well, what's your
[1563.50 → 1564.16] version number?
[1564.30 → 1569.72] And I can tell you that, um, more frequently I'm getting people who are asking questions
[1569.72 → 1570.48] on one nine.
[1570.48 → 1577.36] So it's, uh, adoption is definitely picking up a lot more than, um, one nine one for sure.
[1577.90 → 1583.58] Recently this weekend, a, um, and I need to look up the name, but the, the gentleman that,
[1583.58 → 1590.40] uh, managed the Ruby install for Debian basically said he was no longer going to do it.
[1590.80 → 1591.54] Uh, yeah.
[1591.62 → 1597.40] Lucas, what's your take on, uh, you know, Ruby installs on Unix platforms and Linux platform
[1597.40 → 1601.86] platforms as, as opposed to RVM and some of the other, uh, install mechanisms?
[1601.86 → 1611.82] Well, I don't really use RVM, but, um, it's not because I have a problem with RVM at all.
[1611.94 → 1617.96] It's mainly just because of like, since I am a Ruby developer, I spent a lot of time compiling
[1617.96 → 1620.54] and running out of, uh, subversion.
[1621.16 → 1623.92] So that's just my use case.
[1623.92 → 1628.48] And it's a very like tiny, you know, tiny use case.
[1628.48 → 1634.96] But as far as packaging is concerned, like the problem that happened here in this case is that,
[1634.96 → 1641.78] um, the Debian release, um, the way that they do releases or the way that they release packages
[1641.78 → 1645.72] is just different from the way we do it on Ruby core.
[1646.66 → 1652.76] And the Debian folks came to us and said, you need to do your releases this way.
[1653.56 → 1656.78] And we said, no, we do it.
[1656.78 → 1658.48] We do it the way we want to do it.
[1658.96 → 1663.02] And so I don't know.
[1663.08 → 1665.26] It just, it depends on your opinion.
[1665.46 → 1671.94] It seems like Lucas also had a hang-up with a lot of the, um, I guess mailing lists are
[1671.94 → 1677.14] still Japanese, even though that, uh, you know, we've got a worldwide adoption of, of Ruby now.
[1677.14 → 1682.10] I mean, what's, I mean, do you have any problems, you know, keeping up to speed with, with the
[1682.10 → 1682.42] language?
[1682.42 → 1685.52] I mean, I'm assuming you don't speak Japanese, but that may be presumptuous.
[1686.42 → 1688.46] I do speak Japanese, actually.
[1688.72 → 1688.98] Do you?
[1689.50 → 1689.92] Yes.
[1691.00 → 1696.80] Uh, the thing is like, it's, it's kind of, it's kind of interesting because I'm on, I'm on
[1696.80 → 1698.02] the Japanese list too.
[1698.02 → 1704.04] Like I watch, I watch the Japanese list and I also watch the English list and I don't
[1704.04 → 1704.28] know.
[1704.44 → 1713.74] It's, it's, there is no truth to rumours about, you know, decisions being made on the Japanese
[1713.74 → 1715.24] list that nobody knows about.
[1715.24 → 1720.66] Uh, I mean, the thing is like most of the time, most of the time the conversations that
[1720.66 → 1725.74] I read on the Japanese list are very like, I've got a bug with blah, blah, blah, you know,
[1725.74 → 1729.82] very mundane, mundane emails.
[1730.08 → 1733.28] Most of the most of the difficult decisions are made on the English list.
[1733.80 → 1741.28] Uh, I think the problem is that just Japanese to, to Westerners is very inaccessible, right?
[1741.28 → 1747.22] Like you look at the language, and you're like, Oh crap, I have no idea what's going on.
[1747.48 → 1752.32] So I think it's more just fear maybe or something.
[1752.82 → 1757.88] So being able to speak Japanese, did that have any, did you learn it after you picked
[1757.88 → 1759.04] up Ruby or vice versa?
[1759.92 → 1761.98] Um, I learned it.
[1762.04 → 1764.58] Well, I learned it after I picked up Ruby.
[1764.58 → 1774.48] Um, I, I decided to learn it because I wanted to be able to communicate better with the, um,
[1775.12 → 1776.84] the Subsists in Japan.
[1776.84 → 1778.88] Like I knew, I knew it came from Japan.
[1780.08 → 1785.32] Um, I knew that, you know, there was, there was all this documentation.
[1785.32 → 1790.12] I found all this documentation in Japanese, and I was just like, I wish I could read this.
[1790.18 → 1792.98] So I decided to start learning it.
[1792.98 → 1795.74] So then I'm taking, you've attended RubyKyge?
[1796.08 → 1797.28] Yeah, several times.
[1797.42 → 1799.48] Uh, three times I think I've been.
[1799.84 → 1800.00] Yeah.
[1800.20 → 1801.32] And how's it compared to Rubicon?
[1801.72 → 1803.54] Well, it's kind of funny.
[1803.70 → 1808.94] Last, last year they said that, uh, I think this is very true that, um, RubyKyge isn't
[1808.94 → 1810.20] actually a Ruby conference.
[1810.20 → 1813.00] It's a C conference disguised as a Ruby conference.
[1814.00 → 1815.04] I can see that.
[1815.04 → 1821.34] Uh, that like it's, there are a lot more hacks.
[1821.34 → 1824.52] Like I see a lot more hacks on the VM.
[1824.90 → 1832.54] Um, it's not, you know, there, you see a lot more rails presentations here in the U S at
[1832.54 → 1833.20] Rubicon.
[1833.44 → 1834.72] Not so much there.
[1834.72 → 1839.38] Um, but I don't know.
[1839.38 → 1842.44] I really enjoy both conferences a lot.
[1842.56 → 1843.22] I really do.
[1843.72 → 1846.82] So then we'll have to get your impression of, uh, Red Dirt Rubicon.
[1846.92 → 1847.88] Will this be your first one?
[1848.50 → 1850.18] Uh, yes, it will be my first one.
[1850.24 → 1851.82] Ever been to Oklahoma City at all?
[1853.04 → 1855.72] Um, no, but I hear that there is good barbecue.
[1856.40 → 1857.20] Excellent barbecue.
[1857.74 → 1858.04] Excellent barbecue.
[1858.04 → 1859.22] I'm looking forward to that.
[1860.02 → 1860.98] Play your cards right.
[1861.04 → 1862.74] Might even have a tornado or two.
[1862.74 → 1865.26] Nice dust storm.
[1866.86 → 1868.18] I would enjoy that too.
[1868.40 → 1873.10] Well, at least watching as long as I can do it from the, uh, comfort of indoors.
[1873.96 → 1874.44] Yeah.
[1874.44 → 1879.64] Oklahoma City has got a nice tech scene for, uh, for a Midwestern town and outside of Silicon
[1879.64 → 1884.44] Valley or a major population centre, but, uh, Oklahoma City is growing and has its own,
[1884.48 → 1885.70] I guess, NBA team now.
[1886.22 → 1886.72] Oh, really?
[1886.90 → 1887.14] Yeah.
[1887.14 → 1887.70] I did not know that.
[1887.72 → 1888.48] Did not know that.
[1888.80 → 1891.16] So, um, should be fun times.
[1891.16 → 1895.22] Uh, Red Dirt Rubicon is in April, April 21st through the 23rd.
[1895.42 → 1900.32] So, um, you mentioned Pearl and Ruby, any other languages that you've picked up or want
[1900.32 → 1900.74] to pick up?
[1901.74 → 1909.98] Uh, lately I've been doing a lot of scheme, um, but I am very interested in Haskell too.
[1909.98 → 1915.60] So I think that that'll probably be my next, the next language I'm going to play with after
[1915.60 → 1918.44] I get done with my scheme vendor.
[1918.64 → 1919.14] How's that?
[1919.14 → 1919.92] There you go.
[1920.66 → 1924.56] So Haskell, um, so CoffeeScript appeal to you at all?
[1925.22 → 1928.70] Um, I think it's interesting, but I haven't programmed in it that much.
[1929.04 → 1930.76] I've been hooked on it lately.
[1930.84 → 1934.62] It seems like every JavaScript project I've picked up that I'm coding on by myself has been
[1934.62 → 1935.44] a CoffeeScript joint.
[1935.44 → 1938.32] Uh, yeah, it looks, it looks interesting.
[1938.32 → 1942.32] Like it looks like it would be a lot more fun to write than JavaScript.
[1943.04 → 1945.92] Who in the Ruby community would you want to pair program with?
[1946.40 → 1952.28] I would love to pair with, I'm trying to think of somebody I haven't paired with before that
[1952.28 → 1953.36] I would love to pair with.
[1954.02 → 1956.12] Probably I would love to pair with Jim Wei rich.
[1956.36 → 1957.32] That'd be a nice pair.
[1957.50 → 1958.62] Yes, I think so.
[1958.76 → 1961.24] A maker of Rake for those that, uh, might not know.
[1961.90 → 1964.28] Jim would be an excellent person to pair with.
[1964.28 → 1969.70] That's what you need to do is, uh, start up a, a promiscuous pairing service at Tinder
[1969.70 → 1972.50] Lovemaking where people can pay to pair programming with you.
[1974.44 → 1974.84] Yeah.
[1975.00 → 1975.34] Yeah.
[1975.50 → 1976.88] I remember what was it?
[1976.96 → 1980.68] Um, I think like, was it Hailstone?
[1980.84 → 1986.10] Some conference I went to where it was like, um, you get to pair with, you know, pair with
[1986.10 → 1987.76] a famous person or something like that.
[1987.76 → 1994.08] Uh, and I really wanted to enter cause, um, Jim was one of the people you could pair with.
[1996.92 → 2000.88] But, um, I guess I missed the, uh, entry deadline or something.
[2001.66 → 2002.10] Cool.
[2002.16 → 2005.20] Let us know what topic you choose for Red Dirt Ruby Jump.
[2005.28 → 2007.40] We'll see you in Oklahoma City in April.
[2007.84 → 2008.24] All right.
[2008.40 → 2008.90] Thank you.
[2021.44 → 2027.34] See it in my eyes.
[2027.76 → 2030.86] So how could I forget when?
[2030.86 → 2036.74] I found myself for the first time
[2036.74 → 2040.46] Safe in your arms
[2040.46 → 2043.68] As a dark fashion shot
