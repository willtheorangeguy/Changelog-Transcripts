[0.00 → 19.42] Welcome to the Changelog episode 0.5.2. I'm Adam Stachowiak.
[19.74 → 24.00] And I'm Won Netherlands. This is the Changelog. We cover what's fresh and new in the world of open source.
[24.42 → 28.42] If you found us on iTunes, we're also on the web at thechangelog.com. We're also up on GitHub.
[28.42 → 35.06] Head to GitHub.com. You'll find some trendy repos, some feature repos from the blog, as well as our audio podcasts.
[35.66 → 39.78] If you're on Twitter, follow Changelog Show, Changelog Jobs, and me, Adam Stack.
[40.38 → 42.82] And I'm Penguin, P-E-N-G-W-Y-N-N.
[43.62 → 47.82] This episode is sponsored by GitHub Jobs. Head to thechangelog.com.com to get started.
[48.42 → 52.08] If you'd like us to feature your job on this show, select Advertise on the Changelog.
[52.28 → 54.30] I'm posting your job, and we'll take care of the rest.
[54.30 → 63.40] Our friend Encoder, a startup focused on tools and services for video website developers, is looking for a smart person who is also a Ruby and Rails engineer.
[63.68 → 68.98] Perks include stock options and a growing startup, relocation assistance to the Bay Area, and freedom.
[69.32 → 73.44] They trust you. Check it out at LG.Gd slash 9g.
[73.44 → 83.60] And our friends over at Store MV, the Tumblr for e-commerce, are looking for a lead champion of codes, a Rails engineer, and a president of beautiful things, a UI designer.
[84.12 → 88.62] Both are full-time positions, and based on a recent tweet, they're offering a 5K bonus.
[88.84 → 91.44] Check it out at LG.Gd slash 9h and 9i.
[91.44 → 96.52] That would be our buddy John Crawford, who I ran into down at South by Southwest.
[96.74 → 98.60] We had a fun time in Austin.
[99.02 → 102.20] Bailed a little early on the conference, but had to get back to some work stuffs.
[102.40 → 104.24] But handed out a lot of stickers.
[104.38 → 107.02] Met a lot of fans of the show.
[107.14 → 108.86] Got to meet a lot of you in person.
[109.08 → 111.86] Some fun times down there, but I understand you had some fun times.
[112.90 → 115.36] Back home, interviewing John Long from Serve.
[115.36 → 116.74] Yeah, I went solo on this one.
[116.82 → 119.04] I talked to John Long of Radiant and Serve fame.
[119.14 → 123.04] We covered all things Radiant, the community, optimism, and open source.
[123.36 → 127.60] We also talked a little bit about website prototyping with Serve, which is pretty awesome.
[127.64 → 128.82] And I hear you guys use it at HP.
[129.28 → 129.78] We do.
[129.92 → 134.32] I'm anxious to hear this episode, because if you're building a Rails application,
[134.84 → 138.06] and you've looked at Statistic or some other prototyping tools,
[138.16 → 145.04] take a look at Serve, because it's by far the easiest drop-in replacement once you actually get to your Rails application.
[145.04 → 147.60] It's just the view layer that you can just snap right in there.
[148.14 → 148.70] Yeah, Serve is awesome.
[148.82 → 153.46] It's perfect for those who love those common Rails front-end tools like Tamil, SAS, and Compass.
[153.80 → 157.66] It's pretty easy to deploy to Heroku, but a simple brochure or website.
[157.84 → 159.96] It's production-ready, so you can deploy to Heroku.
[160.08 → 161.18] It's really, really awesome.
[161.76 → 163.78] You guys also talked about Radiant and some of the backstory.
[164.30 → 166.58] Yeah, a lot about the first Ruby CMS.
[166.90 → 172.78] We also talked about John's stint into design and how he got involved with the Ruby Lang website
[172.78 → 174.34] and what that led to for Serve.
[175.04 → 178.46] Sorry, I guess ultimately it was Serve, because Serve kind of came from Radiant,
[178.54 → 180.94] but it was really the kickstart for Radiant.
[181.82 → 182.50] Fun episode.
[182.66 → 183.18] Should we get to it?
[183.44 → 184.02] Let's do it.
[192.66 → 195.94] We're joined today by John Long, proprietor of Wise heart Design.
[196.16 → 199.30] I'm running this show solo today, so John's with me.
[199.30 → 200.66] He's the creator of Radiant CMS.
[200.84 → 206.06] We're going to talk about this and a lot of fun front-end developer stuff in this wild world of open source.
[206.18 → 207.16] But, John, how are you today?
[207.68 → 208.38] Doing well.
[208.52 → 208.86] Doing well.
[209.86 → 213.84] So, John, for the folks who do not know who you are, I don't know why they wouldn't,
[214.06 → 217.64] but why don't you give a brief introduction about who you are and what you've been up to.
[219.10 → 219.44] Okay.
[220.56 → 223.98] I do freelance design work.
[223.98 → 226.40] I've been doing it for a number of years now.
[227.46 → 239.20] And I guess at the beginning of my freelance career, I was involved in the redesign of Ruby Lang.
[240.16 → 241.86] So, a lot of people know me from that.
[241.86 → 254.68] And for Ruby Lang, I also created Radiant CMS, which is a content management system that is well-known in the Rails world.
[255.98 → 257.16] So, yeah.
[257.52 → 258.20] That's who I am.
[259.36 → 260.36] I live at home.
[260.60 → 261.68] I have a dog, Lily.
[263.86 → 264.38] Yeah.
[264.38 → 266.16] Very cool.
[266.22 → 268.98] That's actually how I know you from back in the day.
[269.26 → 272.24] And I love the design that you did for the Ruby website.
[273.38 → 274.30] It's definitely awesome.
[274.36 → 277.10] But I didn't know that Radiant came out of that project.
[277.14 → 277.74] What was that like?
[280.40 → 286.38] That was at a point in my life where I was really optimistic about the value of open source contributions.
[286.38 → 294.66] In the sense that I actually took about six months and programmed Radiant CMS.
[295.00 → 297.52] I was living at home with my parents.
[297.86 → 299.80] I had a job in Chicago.
[300.28 → 302.00] I had moved back.
[302.36 → 305.42] And I thought, I want to do freelance stuff.
[305.68 → 312.62] So, what would be better than to have a content management system that you wrote for websites?
[312.62 → 313.02] Yeah.
[313.16 → 314.94] So, yeah.
[315.08 → 322.26] It was kind of like doing my own little startup that was kind of open source aims, I guess.
[323.20 → 326.52] And, yeah.
[326.60 → 329.16] During that year, launched Radiant.
[329.92 → 332.26] It ended up kind of paying off.
[333.54 → 340.86] I made contact with the Pragmatic programmers through that experience.
[340.86 → 346.54] And I was able to do some work for them, which was another great sort of portfolio piece.
[347.40 → 355.50] But as I look back on it, it probably wasn't the best way to start a freelance career, I guess.
[356.94 → 358.54] By developing a CMS, you mean?
[358.96 → 359.22] Yeah.
[359.32 → 367.42] Well, I mean, I haven't actually ended up doing a lot of websites that are like CMS-focused kind of thing.
[367.42 → 373.90] So, I had, in my other job, we had done a lot of content management stuff.
[374.96 → 380.58] But that wasn't where I ended up, like, carving out my little niche.
[380.72 → 387.70] I ended up more in the web app space rather than the website space.
[387.90 → 391.00] And Radiant's much more in the website space.
[391.00 → 394.84] So, it's interesting.
[395.14 → 400.58] So, when you actually picked up the idea of the CMS, were you starting to work on Ruby Lang?
[400.86 → 405.62] Or was this a project that kind of started in parallel with it for a niche or a need that they needed?
[406.48 → 411.46] Well, at the time, Rails had just kind of come out.
[411.46 → 418.02] And Ruby Lang was, let's see, how did that all work?
[418.90 → 420.12] I was working in Chicago.
[420.76 → 430.64] And at a certain point, I was just like, man, the Ruby website is just terrible.
[430.88 → 436.04] I mean, it's very, like, it used a lot of red in the header and different things like that.
[436.28 → 437.18] Red everywhere.
[437.34 → 438.06] Red and pink.
[438.06 → 440.88] And it was hard to read.
[441.60 → 443.44] It was basically just a blog.
[444.26 → 450.88] And I was getting to use Ruby at work as a developer and just felt like it needed something better.
[451.02 → 456.94] So, I sent a post out to the mailing list and suggested that we form an identity team,
[456.94 → 470.00] much like the Mozilla Firefox identity team, which had just had great success in designing the Firefox icon and all those kinds of things.
[470.00 → 472.68] And the idea caught on.
[472.68 → 478.42] And I ended up getting to be part of that team.
[480.30 → 482.20] We did the design and everything.
[482.40 → 483.38] We got all of that rolling.
[484.06 → 487.96] And then it was like, well, how are we going to deploy this thing?
[487.96 → 494.52] And why the lucky stiff was actually on the Ruby identity team at the time.
[494.52 → 501.76] And he gave a go at it using, he had a command line based thing.
[502.26 → 505.74] It was kind of like a precursor to maybe Jekyll.
[505.74 → 514.98] It like generated, and then I don't know if it FTPS things over how it works exactly, but you ran it on your local box.
[515.78 → 520.54] And we gave a go with that.
[520.76 → 524.78] And it like didn't work for what we were trying to do.
[524.78 → 530.90] So, we were stuck with a lot of, I guess, Ruby-like solutions that just weren't really well done.
[531.24 → 538.10] And I had had some experience at my old job doing a text pattern site.
[539.30 → 542.96] I had written a custom.
[543.48 → 548.84] We used a lot of RHTML running on mod Ruby.
[548.84 → 559.16] So, it was really more akin to PHP or something like that because it was just ERA plus some custom classes that we had written.
[560.00 → 570.68] And so, I had written kind of a emulating system around that and was real opinionated over what I thought should be in a content management system.
[571.14 → 578.42] I saw that Rails was there, and I thought, wow, I could just, you know, spend some time, a couple of months, hack this thing together.
[579.44 → 585.58] And so, I kind of made a commitment to do it, and it was sort of like once it was out of my mouth, I had to do it.
[586.04 → 597.12] And I don't think I really anticipated it was going to take like six months to do the major development on Radiant or five months or something like that.
[597.12 → 605.18] But we were able to get that done, launch the Ruby website successfully.
[605.32 → 609.72] I think it ended up being around August by the time we had all the pieces in place.
[609.72 → 614.76] They had to do like a server upgrade so that it could run Rails and some different things like that.
[614.76 → 623.92] And so, what was it that actually took Radiant to become, I guess, more of the more mainstream Ruby CMS available out there?
[623.92 → 626.10] I mean, it was the first.
[626.52 → 635.92] And I think that being the first and also being...
[635.92 → 643.62] Well, we made a commitment kind of early on.
[645.52 → 652.86] David, the way that he talked about Rails and the continued development and all those types of things,
[652.94 → 657.54] what Rails was going to be and what it wasn't going to be, like, that was all fresh in the air.
[657.54 → 663.62] And, like, everybody was breathing this, you know, stuff.
[663.82 → 664.32] The Kool-Aid.
[664.44 → 666.26] Yeah, drinking the Kool-Aid, not breathing it, but drinking the Kool-Aid.
[666.26 → 666.90] Yeah, exactly.
[667.66 → 676.84] And I was like, yes, yes, Radiant is going to just be focused on this one area.
[676.96 → 682.28] And the way that I'm going to serve those other things is I'm going to do a plug-in system from the beginning.
[682.28 → 692.00] And having made that commitment after Lucy-Radiant, it took, like, several more months to build the plug-in system for it.
[692.66 → 699.40] And I think I ended up writing the basic idea for it.
[699.40 → 715.92] And Sean Tribes, at a certain point, started working on something he called Shards, which was a way of allowing programmers to declare where certain partials should be included in views.
[717.20 → 721.46] So you could monkey patch to insert controllers and things like that you needed to,
[721.46 → 729.64] but Shards allowed you to make modifications to the views so that two plug-ins that overrode the same view wouldn't conflict.
[730.40 → 734.82] Instead, you could plug in pieces into the view instead of overwriting.
[735.62 → 740.20] So, yeah, it kind of grew like that.
[740.42 → 748.26] And once we had the plug-in system in place, it really sort of developed on its own.
[748.26 → 764.02] And since maybe the first eight months or so, there's been, like, just a group of people using it and developing stuff for it.
[764.76 → 766.54] We've done different things since then.
[766.60 → 768.28] We've got an extension registry.
[769.74 → 772.88] It's like over – there's over 200 plug-ins for it.
[772.88 → 782.94] But because there's kind of this ecosystem there, even though I feel like we're still learning a lot about –
[782.94 → 788.96] and, frankly, just we don't have enough time to make Radiant what we want it to be, what we know it can be.
[790.50 → 797.30] Even though it's still green in some ways, there's a lot of people that are passionate about using it and enjoy it.
[797.30 → 801.58] So it's really the community that kind of formed around it.
[802.78 → 805.22] And it required a lot of effort in the beginning.
[805.38 → 814.58] I don't think that I could have launched Radiant kind of successfully if I hadn't been pretty devoted to it in the beginning.
[814.58 → 824.64] But it's become sort of a self-sustaining community to where now I'm – I turned over the lead development to Sean Cribs.
[825.22 → 827.00] At one point, Sean has gone on.
[827.10 → 829.30] Jim Gay has taken up that mantle.
[829.50 → 831.54] We've got several people that are on the core team.
[832.92 → 840.50] I mean, it's – I really feel like I could step out of the picture, and it would still, you know, continue to go.
[840.50 → 846.10] So I haven't done that yet because I still have vision for where the product can go.
[846.50 → 853.78] And we haven't totally achieved what I was wanting to achieve with the product when we first introduced it.
[854.04 → 862.24] But I think that's – the community itself is the main reason that Radiant has done so well.
[862.24 → 873.18] So in terms of being that go-to CMS within the Rails community, there are certainly other content management systems now.
[875.00 → 880.74] And I'm not real aware of the communities that are around those.
[880.84 → 886.32] But it still seems that Radiant – it's the community that kind of holds it all together.
[886.32 → 894.20] So when you look at Radiant and what it is now, but you said a couple of times there which you still have vision for,
[894.30 → 900.72] what is the vision in comparison to where it is now and where you'd like to see Radiant, whether you're part of the team or not?
[901.04 → 901.32] Yeah.
[901.32 → 911.62] I think for me a big sort of part of this is seeing it be able to compete head-to-head with tools like WordPress,
[913.82 → 915.68] particularly on a usability level.
[917.68 → 922.00] I feel like we have some ground to cover there.
[922.00 → 931.56] Some of it, too, is just getting good pieces in place to handle like the asset management side of it and different things of that nature.
[931.78 → 944.80] And part of our – part of the push with the asset management – asset management still hasn't made it into core.
[944.80 → 951.90] And one of the big development efforts right now is that we're going to begin launching into,
[952.02 → 957.50] particularly as we move to Rails 3, is dividing up the core so that different parts are easy to take out.
[958.90 → 969.76] And once we have that kind of design in place, it'll be easier to have like a default asset management solution
[969.76 → 976.80] that if you'd like a different approach, you can plug in that different approach, and it would still like work with the rest of the system.
[977.94 → 990.86] So some of that – some of it – some of it has to do with we've been working through the best way to build a modular plug-in type architecture within Rails.
[990.86 → 1000.08] So there's a piece there, and then there's a piece with just the usability, the friendliness of it.
[1002.88 → 1007.34] I've actually been using WordPress a lot on one of our church's websites,
[1007.34 → 1018.56] and it definitely has – it's a lot more user-friendly to the end user.
[1018.56 → 1025.98] But Radiant is a lot more powerful in terms of like what it allows you to do with the code,
[1026.16 → 1030.32] which is where it's really, really fun to use.
[1030.56 → 1035.90] But it's still got a ways to go in terms of competing with something like WordPress head-to-head.
[1036.66 → 1043.32] So WordPress is more of a user-friendly kind of GUI kind of scenario where you can also still develop plug-ins,
[1043.32 → 1051.88] but it seems like Radiant is more of a hacker CMS mostly that, like you said, underneath the code you can really dive in and do a lot more with it.
[1052.06 → 1053.78] Is that about the case?
[1054.52 → 1054.78] Yeah.
[1056.16 → 1064.50] I mean, just for instance, the macro language that Radiant uses for its templates, Radius,
[1064.50 → 1071.90] is accessible throughout the system, whether you're on a page or you're in a layout,
[1072.22 → 1075.26] or we've also got a concept kind of partial to come snippets.
[1077.02 → 1079.96] So you can use the macro language wherever you are.
[1079.96 → 1098.56] And part of Radiant's sort of ethos is that the idea that, like Ruby, we want it to be a system that provides a tremendous level of power,
[1098.76 → 1104.86] but it's very accessible to people that are, like, coming on board and learning.
[1104.86 → 1110.16] So even though you might discover a page that has Radius tags in it, for instance,
[1110.74 → 1117.86] if you're just a content editor, you can go in and, like, make changes relatively easily
[1117.86 → 1122.46] with only understanding, like, markdown or textile or something like that.
[1124.12 → 1133.62] So there definitely is a lot more, I guess you could say, raw power in what Radiant allows you to do.
[1134.86 → 1135.54] Out of the box.
[1135.66 → 1139.22] But it's still not as user-friendly to the end user.
[1140.62 → 1147.08] And so as we continue to develop the interface, I saw you had a blog post about having more design saltiness in it,
[1147.10 → 1149.90] and you were doing some prototyping with the navigation and whatnot.
[1150.04 → 1156.60] How do you get more designers involved to not only make Radiant an awesome CMS from a backend standpoint,
[1156.74 → 1162.08] how you have asset management and ease of deployment and those kinds of scenarios,
[1162.08 → 1166.84] but how do you also design this interface in an open source community that makes sense?
[1167.92 → 1170.16] Yeah, I mean, that's really kind of an open question.
[1172.74 → 1178.22] It's the one area of Radiant that I have not been able to, like,
[1178.96 → 1185.52] completely relinquish to someone else, being the design piece of it.
[1185.52 → 1191.04] And it's something that we're experimenting with.
[1191.24 → 1198.44] One of the things that we're doing is we have a separate project where all the HTML development takes place.
[1198.54 → 1200.68] We actually use SERVE for that.
[1202.28 → 1209.20] And the idea being that a designer wouldn't have to, like, understand Rails and all those things in order to contribute.
[1209.38 → 1213.96] He could just, you know, as a prototype project, say, I've got this idea for something.
[1213.96 → 1218.10] And, you know, work it on GitHub or whatever.
[1218.46 → 1225.52] And then everybody would be able to download it and check it out and see what it looked like before it went into development kind of thing.
[1226.28 → 1236.12] So I think part of it for us, WordPress has definitely gotten a lot more exposure, for instance.
[1236.12 → 1239.54] And there are a lot of designers who use it.
[1240.60 → 1248.10] And so they have had more input into the design itself from the community.
[1248.52 → 1253.96] And the Radiant community is not that big yet in the same sense.
[1253.96 → 1268.12] So I think that part of it is just we haven't gotten to a point where we have a lot of designers that are, you know, have spare cycles and want to contribute to the way that the CMS works.
[1268.12 → 1275.08] And part of it is we need to do a better job of, like, bringing those people into the community, I guess.
[1276.34 → 1284.22] And still experimenting with different approaches and how design can take place in more of a collaborative kind of way.
[1284.22 → 1288.74] I think it's certainly difficult in this source world.
[1288.88 → 1294.24] I mean, if you're just a – let's just say a designer, not so much someone who dabbles in a lot of the code.
[1294.34 → 1295.84] Maybe you're just the designer piece of it.
[1295.86 → 1299.20] Or maybe you're dabbling more into, you know, HTML prototyping.
[1299.26 → 1301.70] But you're not using tools like CAME, SAS, Compass.
[1301.86 → 1306.40] You're still kind of on the actual language itself, HTML and CSS.
[1306.40 → 1311.04] And then you enter this world of Git and GitHub, and it gets a little intensive.
[1311.40 → 1315.20] And now you've been introduced to the command line if that's never been a place for you before.
[1315.32 → 1322.48] So it can be kind of hard to jump into these environments and, you know, use your true skills in this unusual world.
[1323.42 → 1323.60] Yeah.
[1323.74 → 1334.04] I mean, I think for sure, and particularly Rails is not an easy environment for a designer who doesn't know a lot to jump in and work with.
[1334.04 → 1350.42] I mean, when you compare it to stuff like WordPress and so many people out there that are using WordPress and don't know anything about, you know, or SAS or Git, you know.
[1350.54 → 1354.76] I mean, they FTP the thing over to their, you know, server.
[1355.72 → 1356.08] FTP?
[1356.08 → 1356.56] They love it.
[1356.64 → 1358.50] I mean, it's just – yeah, FTP.
[1358.76 → 1360.20] Who does that anymore, right?
[1360.22 → 1360.64] Right.
[1360.90 → 1362.20] Most of the world does.
[1362.20 → 1369.26] And, you know, Rails is awesome, but it's a foreign language to so many people.
[1369.70 → 1372.20] And so –
[1372.20 → 1378.14] Well, you know, if they're using FTP, they must not be even using any version control systems either.
[1378.28 → 1382.64] So just thinking Git, thinking, what about the version of my code?
[1382.70 → 1383.54] That doesn't make any sense.
[1383.54 → 1383.94] Yeah.
[1384.18 → 1392.36] I mean, getting a theme and just making modifications, and you've got – you know the story.
[1392.66 → 1395.88] You make a change, and you call it index.old.html.
[1396.34 → 1396.78] Right.
[1396.90 → 1398.26] All of that type stuff.
[1398.92 → 1399.28] Yeah.
[1399.58 → 1402.48] Your version in the actual ways you rename the files and whatnot.
[1402.48 → 1412.18] And then you even have like an old directory above it so that you can put those old files after they've cluttered the file system that you're trying to mess with.
[1412.30 → 1422.18] So speaking of the designers and trying to prototype, you mentioned serve as part of Radiant and you use serve to actually prototype the interface for Radiant.
[1422.18 → 1429.56] And looking also at Radiant, I see a lot of similarities in how you list pages and how that hierarchy kind of gets displayed in that UI.
[1429.76 → 1432.92] And in serve, it's more of like right there in TextMate.
[1433.50 → 1439.04] Was that just a natural extraction from the visual UI that was in Radiant?
[1439.82 → 1451.82] I think that a lot of that is the result of building a lot of content-heavy sites at my old job.
[1452.18 → 1457.70] And I began to think in terms of like a hierarchy of pages.
[1458.84 → 1469.16] And that was something that I was at the time really frustrated with about a lot of CMSs is they didn't – and even I don't even – I don't know.
[1469.26 → 1471.80] Does WordPress allow you to arrange things in a hierarchy now?
[1474.10 → 1478.16] I don't use it enough to know, but I think they have a pretty okay UI.
[1478.34 → 1480.80] I think you can order the pages, I think.
[1480.80 → 1486.00] Yeah, I think they use kind of a concept of menus, but maybe the pages are all flat or something.
[1486.78 → 1496.84] I'm not sure how it works exactly, but I know that when I was working on Radiant in particular,
[1497.12 → 1504.88] I was really wanting it to be something that kind of reflected that concept of the URL
[1504.88 → 1509.10] and content being structured underneath URLs.
[1509.10 → 1516.32] So – and in a very similar way to the way that it works on the actual file system.
[1516.48 → 1525.12] So when I was working on serve, a lot of the same concepts sort of fell out in that regard.
[1525.12 → 1533.16] So before we dive too deeply into talking about serve and what it is, let's let the listeners actually know what serve is.
[1533.24 → 1534.24] So Radiant is a CMS.
[1534.54 → 1535.00] It's deployed.
[1535.12 → 1535.66] It's got a UI.
[1535.88 → 1538.42] It's got a whole different deploy structure.
[1538.54 → 1540.32] But what is served in comparison?
[1540.32 → 1553.58] So at its smallest serve is a rack-based web server for files.
[1554.24 → 1559.74] It handles ERV, HALL, SAS.
[1559.74 → 1560.74] It's got a UI.
[1560.74 → 1562.76] You can integrate Compass into it.
[1565.08 → 1572.20] So that's kind of the technical, like, what it is being a web server.
[1572.94 → 1582.44] It's also – or the way that I would describe it is it's a rapid prototyping framework for web applications
[1582.44 → 1585.94] and specifically Rails applications.
[1585.94 → 1593.14] And what I mean by that is that Rails applications have your model, your view, your controller.
[1594.28 → 1600.62] And serve is basically like having a Rails' application without the models and the controllers.
[1600.78 → 1601.98] You just have the views.
[1602.94 → 1612.82] So as a designer, if that's the part that you mostly work on, that serve allows you to just focus on the views
[1612.82 → 1620.46] without having to build out or have built out for you the other components, the models and the controller.
[1621.98 → 1628.82] So you're able to prototype what you want the application to be in HTML and CSS
[1628.82 → 1634.28] without worrying about how the back end is going to run and all of that kind of stuff.
[1635.32 → 1636.36] So, yeah.
[1636.36 → 1645.58] So prototyping, this is obviously a fun thing anyway because I know that as a front-end developer designer in the Rails slash Ruby world,
[1646.30 → 1651.60] trying to iterate and trying to prototype before was always a pita.
[1651.70 → 1652.78] It was always a pain in the butt.
[1653.26 → 1659.34] And now that I know about serve, my life is so much happier now just being able to easily pick up a project
[1659.34 → 1664.64] with all my fun tools in it and build it out based on URLs and all that good stuff.
[1664.76 → 1669.84] So URL-based design, it seems like in serve you pay a lot of attention to that.
[1669.92 → 1671.34] You have this notion of redirects.
[1671.82 → 1675.94] What are some other cool features that the listeners should know about for serve?
[1677.30 → 1682.34] Well, in regard to URLs, one of the things that serve does is,
[1682.34 → 1687.16] like some web servers do or can be set up to do,
[1687.74 → 1694.56] by default it allows you to append a slash to a file name without the extension
[1694.56 → 1702.86] in order to get a slash-based URL instead of a URL that ends in an extension.
[1702.86 → 1712.48] So one advantage to it when you compare it to, like, normal HTML is that it actually allows you
[1712.48 → 1720.50] to begin to prototype those URLs in addition to the HTML that you're going to want for the application.
[1721.04 → 1725.34] It does have redirects, a very simple syntax there.
[1725.86 → 1730.78] You just open up an empty file with an extension redirect on it
[1730.78 → 1733.36] and put the URL in that you want it to redirect to,
[1733.46 → 1735.60] and then it will redirect over to that other URL.
[1736.66 → 1741.40] And that's handy because there are a lot of times when you're programming
[1741.40 → 1748.20] or doing an application, and you want there to be kind of a creation action
[1748.20 → 1754.12] or something of that nature that creates and then redirects to a new URL.
[1754.12 → 1763.60] So having the ability to put a redirect in the place of where that action will be is helpful.
[1764.10 → 1773.96] You can also do email templates for text-based emails for prototyping that aspect,
[1774.06 → 1775.34] which gets sent out from the server.
[1775.86 → 1779.10] And it's not that you couldn't just have a text file or something like that,
[1779.10 → 1784.62] but SERVE's got it in place so that you can put the headers that you want on that email.
[1785.06 → 1787.20] It just renders in the browser as HTML,
[1787.96 → 1792.40] but it would allow you to kind of specify spec for the developer.
[1793.22 → 1795.90] You know, this is the address that I want it to be sent from.
[1796.58 → 1798.26] This is what the subject should be.
[1798.40 → 1801.36] This is the text of the email, the URL, that kind of thing.
[1801.36 → 1808.24] So there are just a number of aspects that are particularly familiar to Rails developers
[1808.24 → 1815.66] that SERVE tries to make easy for the designer to give hints to the developer
[1815.66 → 1818.10] as to how the application should work.
[1819.28 → 1824.50] And so do you also have tie-ins to helpers and other tools that link to?
[1824.66 → 1828.26] And you've got a number of different helpers there that are just kind of baked into normal Rails,
[1828.26 → 1831.32] so porting your view code is pretty seamless.
[1832.14 → 1832.50] Yes.
[1833.02 → 1838.36] We do have a number of the really common view helpers from Rails,
[1839.34 → 1845.52] link to, you have access to the request and the response, parameters,
[1847.76 → 1855.12] a couple of text messaging ones for, like, escaping stuff, that kind of thing.
[1855.12 → 1863.56] And then you can also put your own view helpers in a module, and those would get imported into the application.
[1864.08 → 1871.44] And what's interesting about that, if you're a designer, and you're working on an application
[1871.44 → 1876.64] and occasionally you want to write something to make it, you know, you know a little bit about Ruby,
[1876.64 → 1886.06] but maybe not a lot, and you want to write something to sort of indicate a certain output or something like that,
[1886.06 → 1893.10] but if you throw it in a view helper, then the developer has that, like, as a guide as he pulls it into the application.
[1893.10 → 1900.20] And your view helper could be completely stubbed out in that it returns the same response every single time.
[1900.20 → 1907.38] But then the developer would go in and each, like, actually make it work with RIP data or whatever it is.
[1908.12 → 1917.02] And there's a nice decoupling, essentially, between what the designer is kind of focused on
[1917.02 → 1924.30] and what the developer can be focused on in the back end, because the developer can also come in and put in some common view helpers
[1924.30 → 1931.70] to allow the designer to be more flexible in the way that he's designing.
[1933.38 → 1940.24] But it doesn't have to be the same as what's currently in the application, I guess.
[1941.04 → 1945.02] So they can work a little bit more independently, the designer and the developer.
[1945.02 → 1952.10] Sometimes if you're working in a Rails' application as a designer, you can change one line of code,
[1952.28 → 1955.28] and it, like, messes up something unintentionally.
[1955.80 → 1961.06] And so it's a little bit more guarded when you're working in your own space,
[1961.10 → 1963.30] which is a really nice aspect of serve.
[1964.80 → 1969.42] So as a user of serve, what are some of the fun things that you like best about it,
[1969.48 → 1971.20] and what are some of the fun ways that you use it?
[1971.20 → 1982.24] I really love prototyping in general as it relates to applications,
[1982.78 → 1991.88] and particularly having the ability to do layouts and partials in that Ruby-friendly way
[1991.88 → 1995.34] that I love about Rails View templates.
[1995.34 → 2000.24] I think that's where a lot of the fun is for me with serve.
[2002.66 → 2009.00] I can remember on one of the early applications I worked on,
[2009.44 → 2010.78] sitting down with a client,
[2011.54 → 2018.40] and we were working through the application,
[2018.60 → 2021.32] and I had a layout designed for the application.
[2021.32 → 2024.36] And we were like, what should go on this screen?
[2024.46 → 2025.74] What should the fields be?
[2026.34 → 2029.04] And he would tell me, and I would just type inputs in,
[2029.14 → 2033.02] and it just came alive, like, before our eyes kind of thing.
[2033.10 → 2034.78] So I already had some styles in there.
[2035.64 → 2042.94] And because I wasn't actually working with, like, static HTML files or something like that,
[2042.94 → 2053.12] there wasn't a lot of code that I had to write in order to prototype the idea of something.
[2053.22 → 2056.76] And I went back later after that time with the client
[2056.76 → 2059.76] and was able to dress up the forms a little bit,
[2059.88 → 2061.72] change the style, a little couple of things.
[2062.08 → 2064.72] But just being able to capture that really rapidly,
[2064.92 → 2067.24] right in front of the client's eyes,
[2067.24 → 2072.14] what they were thinking should go on that page kind of thing.
[2072.94 → 2076.42] was really, really helpful.
[2078.42 → 2081.84] And that project itself went through,
[2082.76 → 2087.66] we actually went back and redesigned the look and feel of it.
[2088.68 → 2091.60] And that was a matter of swapping in a new layout,
[2091.78 → 2094.70] and it, like, all flowed and worked,
[2094.70 → 2097.36] like, in the separate prototype application.
[2097.36 → 2107.18] So I think, like, the maintenance of your HTML mockups
[2107.80 → 2113.46] is probably the biggest thing that I like about Serve,
[2113.56 → 2115.02] in that it cleans that up.
[2115.08 → 2118.56] It allows me to use the patterns that I'm familiar with in Rails,
[2118.56 → 2123.58] but I'm not working directly in the Rails space either,
[2123.72 → 2125.90] so I'm not getting in the way of the developer,
[2126.78 → 2128.18] making the changes.
[2128.96 → 2132.12] It allows me to be a lot more conceptual, I think,
[2132.88 → 2135.68] in the sense of just sort of dreaming about what a feature should do
[2135.68 → 2138.58] instead of being worried,
[2138.84 → 2140.48] I need another controller here,
[2140.48 → 2143.32] that kind of thing.
[2143.64 → 2146.90] And actually, because I do both design and development,
[2147.38 → 2149.90] that's almost needed for there to be that separation,
[2150.08 → 2153.26] because I begin thinking too much about the back end,
[2153.70 → 2156.42] and pretty soon I've lost time
[2156.42 → 2159.24] where I should have just been writing HTML and CSS.
[2159.24 → 2161.78] Right, you probably generate a controller,
[2162.06 → 2163.10] and next thing you know,
[2163.10 → 2166.54] you're writing out the view code in your controller and whatnot,
[2166.72 → 2168.04] and then dropping out to the view
[2168.04 → 2170.74] instead of actually crafting the UI and thinking about that.
[2170.90 → 2171.22] Yeah.
[2171.46 → 2172.40] Kind of keeps you focused.
[2172.98 → 2175.40] And, I mean, there's...
[2175.40 → 2179.04] I work with a lot of web applications,
[2179.58 → 2182.98] and we make changes, significant changes at times.
[2182.98 → 2185.16] And if I was having to think about
[2185.16 → 2189.30] or adjust the way, like, the controllers worked
[2189.30 → 2190.42] and all of that kind of thing,
[2190.92 → 2193.94] just to prototype out a new way of doing something,
[2194.34 → 2195.54] there are times when, like,
[2195.56 → 2197.66] we decide not to go down that path,
[2198.46 → 2202.16] not to spend the money to develop that feature that way.
[2203.14 → 2207.78] And because we're able to prototype it in HTML,
[2209.42 → 2210.60] get the feel for the flow,
[2210.60 → 2211.58] get the feel for the features,
[2211.58 → 2213.34] the way the feature is actually going to work.
[2213.68 → 2215.42] We don't end up having to spend those dollars
[2215.42 → 2220.38] on the development at that stage, too.
[2221.28 → 2223.94] Or even a separate branch that somehow gets merged,
[2224.10 → 2226.26] and it's kind of the mess that causes.
[2226.98 → 2227.30] Right.
[2228.64 → 2230.80] That tends to be the road that I'm in.
[2230.86 → 2232.34] I end up being on a team,
[2232.90 → 2235.68] and somehow I end up in my own redesign branch,
[2235.72 → 2236.96] and I'm, like, the only person there.
[2236.96 → 2239.10] I'm, like, the designer in the front end
[2239.10 → 2241.50] doing all the prototyping that you're talking about.
[2241.58 → 2245.16] And I've got devs in other corners of the Git repo
[2245.16 → 2246.22] that are doing their own thing.
[2246.30 → 2248.56] And it's like, at what point do we merge,
[2248.72 → 2251.70] and what kind of havoc is this going to cause?
[2252.06 → 2252.30] Yeah.
[2252.60 → 2256.30] I mean, you probably have to get somebody
[2256.30 → 2257.48] when you're in that situation
[2257.48 → 2259.84] to come, like, sit by you while you do the merge.
[2260.14 → 2261.86] Yeah, you're kind of scared to do it.
[2261.94 → 2263.64] You're kind of like, I don't want to merge this branch
[2263.64 → 2265.20] because I don't know what's going to happen.
[2265.88 → 2266.16] Yeah.
[2266.32 → 2268.02] I always feel a little bit guilty
[2268.02 → 2269.64] when I, like, do that kind of stuff
[2269.64 → 2273.32] because I'm not, like, in the code of, you know,
[2273.34 → 2274.02] all the time,
[2274.06 → 2276.46] and I just know that I'm going to break something
[2276.46 → 2277.34] unintentionally,
[2277.42 → 2279.20] and then the developer's going to come back
[2279.20 → 2279.72] and be upset.
[2279.98 → 2281.62] And I had the good fortune of working
[2281.62 → 2282.84] with really nice developers,
[2282.84 → 2284.58] but it's still like,
[2284.94 → 2286.52] oh, what am I going to do here?
[2288.52 → 2291.56] So I appreciate Serve a lot
[2291.56 → 2292.44] from that perspective,
[2292.56 → 2294.32] that it's my world, you know.
[2294.70 → 2296.52] I can feel free to break things
[2296.52 → 2299.16] and, you know, as I'm moving stuff around,
[2299.26 → 2300.06] then it's not a big deal.
[2300.58 → 2303.16] So we talked about Serve as a rack app.
[2303.20 → 2305.08] We also talked about it being, you know,
[2305.16 → 2306.96] heavily guarded for prototyping,
[2307.06 → 2309.78] but what happens when your prototype graduates?
[2309.88 → 2311.32] Let's say you're not building a Rails app,
[2311.32 → 2312.82] you're just building a UI in general,
[2312.92 → 2314.22] just, let's say, a brochure website
[2314.22 → 2317.84] or a light website with maybe 15 pages,
[2317.94 → 2318.98] 10 pages, something like that,
[2318.98 → 2321.00] that isn't very dynamic,
[2321.28 → 2322.68] it's pretty static,
[2322.68 → 2323.76] and what do you do
[2323.76 → 2325.54] when that kind of application grows up?
[2327.76 → 2331.86] Well, I mean, it is a rack application service,
[2332.22 → 2334.44] so you can deploy it just like you can
[2334.44 → 2336.50] any other rack application,
[2336.78 → 2339.60] which means you can, you know,
[2339.60 → 2345.18] deploy on Heroku or whatever Ruby host you like.
[2346.40 → 2347.76] So it is useful that way.
[2347.82 → 2351.26] You can also use things like Rack Cascade
[2351.26 → 2354.00] with a Rails application, for instance,
[2354.46 → 2357.82] running on Rack to Cascade.
[2357.82 → 2364.72] If the application itself doesn't have that URL,
[2364.96 → 2367.58] then it goes to the serve application
[2367.58 → 2371.48] to fetch that content, essentially.
[2372.20 → 2373.22] So there's some nice,
[2373.28 → 2375.04] because it is a Rack app,
[2375.42 → 2377.32] there's some really nice things that you can do
[2377.32 → 2381.94] in terms of integrating it with existing stuff
[2381.94 → 2383.38] or running it on its own
[2383.38 → 2386.20] at a different place.
[2387.30 → 2388.52] Yeah, I almost see serve as kind of like
[2388.52 → 2390.08] the perfect pages control
[2390.08 → 2392.00] that I've always wanted in my Rails app,
[2392.24 → 2394.02] and it's almost kind of you want to see
[2394.02 → 2395.18] the two play hand-in-hand,
[2395.26 → 2396.82] because you have this Rails app
[2396.82 → 2398.50] that has got a full back end,
[2398.54 → 2400.92] but you also have this lightweight marketing
[2400.92 → 2402.78] slash brochure website on the front of it
[2402.78 → 2404.24] to pin up to,
[2404.24 → 2406.00] but how do you build those
[2406.00 → 2408.72] in a normal MVC kind of schema
[2408.72 → 2409.60] in a Rails app?
[2410.88 → 2412.42] Yeah, I think that there's actually
[2412.42 → 2416.80] some room there for serve to grow.
[2417.86 → 2419.52] It would be great one day
[2419.52 → 2421.30] to be able to share layouts
[2421.30 → 2424.32] between your serve application
[2424.32 → 2425.52] and your Rails application
[2425.52 → 2426.56] without a lot of work.
[2429.02 → 2430.80] There actually is some old,
[2430.90 → 2432.02] crusty code in there,
[2432.02 → 2433.72] I think, that ran on Rails 2.
[2434.24 → 2436.60] that allows you to,
[2436.60 → 2440.62] yeah, run,
[2440.78 → 2443.06] you could mix in to a controller
[2443.06 → 2444.06] in Rails
[2444.06 → 2446.52] the serve functionality, basically,
[2446.88 → 2449.04] and then it would become
[2449.04 → 2449.90] your page controller
[2449.90 → 2452.12] and have access to the same things
[2452.12 → 2452.96] that Rails does.
[2456.24 → 2459.22] It hasn't been worked on in a while,
[2459.22 → 2462.36] so it probably would break
[2462.36 → 2463.20] if you tried it.
[2463.20 → 2464.42] Oh boy.
[2464.78 → 2465.04] Yeah.
[2465.96 → 2467.16] Well, you mentioned that
[2467.16 → 2471.24] when you tackled the grand project,
[2471.36 → 2473.48] which was Radiant back in 06,
[2474.24 → 2475.56] that you kind of felt like
[2475.56 → 2476.86] you were trying to really tackle
[2476.86 → 2477.64] something big,
[2478.00 → 2479.68] but then not long ago
[2479.68 → 2481.58] you started a project called Acoustic,
[2481.66 → 2483.90] which intends to kind of bridge the gap
[2483.90 → 2486.20] between a Ruby slash natural world
[2486.20 → 2487.86] and maybe even kind of bring
[2487.86 → 2488.88] some of the things we know about
[2488.88 → 2490.00] in Django and Rails
[2490.00 → 2491.94] into a more lightweight
[2491.94 → 2493.14] Ruby web framework.
[2493.28 → 2494.30] What is Acoustic?
[2494.36 → 2494.96] What is this about?
[2496.18 → 2496.54] Yeah,
[2496.80 → 2498.48] this is really,
[2498.70 → 2500.68] Acoustic is sort of my,
[2500.68 → 2501.04] like,
[2501.72 → 2502.38] pipe dream
[2502.38 → 2504.66] web framework
[2504.66 → 2505.48] kind of thing.
[2505.48 → 2509.08] it's one of those things
[2509.08 → 2510.44] that I almost feel like foolish
[2510.44 → 2511.16] working on
[2511.16 → 2511.68] because, like,
[2511.74 → 2512.88] everybody has,
[2514.48 → 2516.64] Rails is such an awesome framework
[2516.64 → 2519.24] and Sinatra is amazing.
[2519.48 → 2520.38] It does small stuff.
[2520.62 → 2520.70] Like,
[2521.76 → 2523.50] there's a room for anything else
[2523.50 → 2524.10] kind of thing.
[2524.10 → 2527.76] And I feel like Rails
[2527.76 → 2528.64] has come a long way
[2528.64 → 2529.98] in terms of modularity,
[2530.34 → 2532.06] particularly with Rails 3,
[2532.42 → 2534.20] but it still seems
[2534.20 → 2536.44] really heavy at times.
[2538.04 → 2538.60] And
[2538.60 → 2542.38] I've written a little bit
[2542.38 → 2543.76] about this on my blog.
[2546.04 → 2547.06] I wrote a post,
[2547.24 → 2548.54] what Rails could learn
[2548.54 → 2549.24] from Django,
[2550.12 → 2551.36] different things like that.
[2551.36 → 2554.32] and really trying to
[2554.32 → 2557.08] remove
[2557.08 → 2558.52] maybe the number of files
[2558.52 → 2559.72] that you have to create
[2559.72 → 2560.48] in order to work
[2560.48 → 2562.04] within the application,
[2562.34 → 2563.34] give you more flexibility
[2563.34 → 2564.36] in terms of where
[2564.36 → 2565.62] things are.
[2566.62 → 2567.64] One of the things
[2567.64 → 2568.94] that Acoustic allows you
[2568.94 → 2570.08] to do is have your controllers
[2570.08 → 2570.82] and your views
[2570.82 → 2572.96] all in the same directory.
[2574.36 → 2574.82] So,
[2575.78 → 2577.32] what's the advantage of that?
[2577.42 → 2577.60] Well,
[2577.68 → 2578.44] if you're trying to
[2578.44 → 2579.36] structure something
[2579.36 → 2580.46] modular,
[2580.46 → 2581.56] well,
[2581.62 → 2582.48] in a modular way,
[2583.04 → 2586.22] you could essentially
[2586.22 → 2587.24] have a part
[2587.24 → 2589.30] of the application
[2589.30 → 2590.42] that was like
[2590.42 → 2592.14] a Git submodule
[2592.14 → 2593.32] because you're able
[2593.32 → 2594.00] to
[2594.00 → 2597.28] have that,
[2597.50 → 2598.40] just that folder,
[2598.54 → 2599.22] those controllers,
[2599.46 → 2600.04] those views,
[2600.18 → 2600.74] all of that
[2600.74 → 2603.02] in a separate repository.
[2603.02 → 2605.38] So,
[2605.58 → 2606.44] Acoustic is,
[2607.68 → 2609.96] it's aim is to be
[2609.96 → 2611.06] maybe a more modular
[2611.06 → 2612.78] Rails-type framework,
[2613.50 → 2614.84] but it's still
[2614.84 → 2616.00] very much a toy,
[2617.00 → 2618.78] like it's not fully
[2618.78 → 2619.28] implemented
[2619.28 → 2620.80] in any way,
[2620.96 → 2621.78] like you couldn't
[2621.78 → 2623.84] download Acoustic
[2623.84 → 2625.16] and run anything
[2625.16 → 2626.04] on it right now.
[2626.04 → 2630.08] it's got a router
[2630.08 → 2630.80] in it,
[2631.00 → 2632.84] it's got a basic
[2632.84 → 2634.02] controller structure,
[2634.54 → 2636.28] but I'm still
[2636.28 → 2637.08] building out
[2637.08 → 2638.32] like major
[2638.32 → 2639.78] portions of functionality
[2639.78 → 2641.24] and so,
[2641.50 → 2641.86] and it's,
[2641.94 → 2643.04] really right now,
[2643.08 → 2643.54] it's kind of a
[2643.54 → 2644.62] back burner project.
[2644.62 → 2647.36] the hope
[2647.36 → 2648.08] with it
[2648.08 → 2648.66] would be that
[2648.66 → 2648.98] maybe
[2648.98 → 2650.20] it would either,
[2650.66 → 2651.04] someone
[2651.04 → 2653.18] would adopt it
[2653.18 → 2654.00] and it would become
[2654.00 → 2654.98] something real
[2654.98 → 2656.10] or that
[2656.10 → 2657.16] it would influence
[2657.16 → 2658.16] the design of
[2658.16 → 2659.56] stuff like Rails
[2659.56 → 2660.44] maybe eventually.
[2662.20 → 2663.02] You mentioned
[2663.02 → 2663.74] earlier in the call,
[2664.02 → 2664.72] like really
[2664.72 → 2665.46] early in the call,
[2665.58 → 2667.38] that you were
[2667.38 → 2668.30] highly optimistic
[2668.30 → 2669.50] about open source
[2669.50 → 2670.58] back in the day
[2670.58 → 2671.00] when you were
[2671.00 → 2671.40] starting to work
[2671.40 → 2671.90] with Ruby Lang
[2671.90 → 2672.38] on the redesign
[2672.38 → 2673.94] and Radiant.
[2673.94 → 2674.78] has your focus
[2674.78 → 2675.38] changed towards
[2675.38 → 2676.38] being highly optimistic
[2676.38 → 2676.90] because you just
[2676.90 → 2677.32] said that
[2677.32 → 2678.60] you hope that
[2678.60 → 2679.02] it kind of
[2679.02 → 2679.44] influences
[2679.44 → 2679.84] or maybe
[2679.84 → 2680.78] somebody adopts it
[2680.78 → 2681.96] and assumes
[2681.96 → 2683.60] that the open source
[2683.60 → 2684.32] world is just,
[2684.88 → 2685.20] yeah,
[2685.28 → 2685.74] that's kind of
[2685.74 → 2686.22] optimistic.
[2686.66 → 2687.36] It's got three
[2687.36 → 2687.88] watchers.
[2688.68 → 2688.88] Yeah,
[2689.08 → 2689.34] well,
[2689.50 → 2693.18] I am very
[2693.18 → 2694.22] optimistic about
[2694.22 → 2694.70] open source
[2694.70 → 2695.16] in general.
[2695.32 → 2695.92] I guess what I
[2695.92 → 2698.58] meant in reference
[2698.58 → 2699.32] to that was
[2699.32 → 2701.20] that open source
[2701.20 → 2702.60] is valuable to,
[2702.92 → 2703.70] extremely valuable
[2703.70 → 2704.28] to the person
[2704.28 → 2705.70] who is starting
[2705.70 → 2706.54] a freelance
[2706.54 → 2708.02] business.
[2708.90 → 2709.80] And the thing
[2709.80 → 2710.40] that I learned
[2710.40 → 2711.00] is that,
[2711.18 → 2711.32] yes,
[2711.36 → 2712.28] it can be,
[2713.14 → 2714.12] but it can also
[2714.12 → 2714.68] be,
[2716.04 → 2718.10] it can sort of
[2718.10 → 2719.02] take over your life,
[2719.14 → 2719.94] which is what it did
[2719.94 → 2721.18] with me and Radiant
[2721.18 → 2723.34] for a number
[2723.34 → 2723.96] of months.
[2724.20 → 2724.32] You know,
[2724.36 → 2724.54] just,
[2724.98 → 2726.16] I was committed
[2726.16 → 2727.24] to not letting
[2727.24 → 2727.76] our question
[2727.76 → 2728.90] go unanswered
[2728.90 → 2729.90] on the mailing list
[2729.90 → 2731.92] and things like
[2731.92 → 2732.18] that.
[2732.26 → 2732.64] And it just,
[2733.30 → 2733.64] you know,
[2733.98 → 2735.08] I couldn't have
[2735.08 → 2735.62] done it if I
[2735.62 → 2736.30] wasn't living at
[2736.30 → 2737.02] home with my
[2737.02 → 2737.56] parents at the
[2737.56 → 2738.18] time kind of
[2738.18 → 2738.42] thing.
[2740.42 → 2740.90] So,
[2741.20 → 2742.90] I think that
[2742.90 → 2743.72] when I say I
[2743.72 → 2744.10] was really
[2744.10 → 2744.96] optimistic about
[2744.96 → 2745.62] open source
[2745.62 → 2746.36] back then,
[2746.76 → 2747.34] I was really
[2747.34 → 2748.30] optimistic that it
[2748.30 → 2748.70] was going to,
[2748.70 → 2748.90] like,
[2749.02 → 2749.82] bring in business
[2749.82 → 2750.56] and let me do
[2750.56 → 2751.94] some cool things.
[2751.94 → 2752.50] And I feel
[2752.50 → 2753.32] like I was
[2753.32 → 2754.78] fortunate to
[2754.78 → 2755.32] get the
[2755.32 → 2756.08] projects and
[2756.08 → 2756.62] things that I
[2756.62 → 2757.00] did,
[2757.26 → 2758.04] and some of
[2758.04 → 2758.44] it was a
[2758.44 → 2758.98] result of my
[2758.98 → 2759.40] open source
[2759.40 → 2759.68] work,
[2759.78 → 2760.32] but my time
[2760.32 → 2761.18] could have
[2761.18 → 2761.64] probably been
[2761.64 → 2762.36] spent way
[2762.36 → 2762.74] better,
[2763.36 → 2763.54] you know,
[2763.54 → 2763.96] even just
[2763.96 → 2764.70] cold calling
[2764.70 → 2765.22] people,
[2765.56 → 2766.18] offering my
[2766.18 → 2766.62] services,
[2767.32 → 2768.26] than working
[2768.26 → 2769.02] on a
[2769.02 → 2769.56] open source
[2769.56 → 2770.12] project for
[2770.12 → 2770.64] six months.
[2770.94 → 2771.34] But I'm
[2771.34 → 2772.04] glad I did
[2772.04 → 2772.20] it,
[2772.32 → 2772.48] too.
[2772.62 → 2772.84] I mean,
[2772.86 → 2773.20] it was a
[2773.20 → 2773.42] great
[2773.42 → 2774.04] experience.
[2774.62 → 2774.72] So,
[2775.58 → 2777.92] I don't
[2777.92 → 2778.06] know,
[2778.16 → 2778.72] it's just
[2778.72 → 2779.68] more in
[2779.68 → 2780.12] terms of
[2780.12 → 2781.50] thinking about
[2781.50 → 2782.24] where I
[2782.24 → 2783.12] put my
[2783.12 → 2783.88] energy in
[2783.88 → 2784.60] and all
[2784.60 → 2785.16] of that
[2785.16 → 2785.42] kind of
[2785.42 → 2785.78] stuff in
[2785.78 → 2786.18] the future.
[2786.82 → 2787.88] I'm much
[2787.88 → 2788.62] more aware
[2788.62 → 2789.36] of the
[2789.36 → 2790.20] effort that
[2790.20 → 2790.92] it takes to
[2790.92 → 2791.48] run a
[2791.48 → 2792.02] successful
[2792.02 → 2792.66] open source
[2792.66 → 2793.20] project.
[2794.44 → 2795.12] And maybe
[2795.12 → 2795.46] I'm a
[2795.46 → 2796.48] little more
[2796.48 → 2797.24] jaded than
[2797.24 → 2797.92] I should be
[2797.92 → 2798.90] about that
[2798.90 → 2801.02] as a result
[2801.02 → 2801.46] of working
[2801.46 → 2801.92] on something
[2801.92 → 2802.34] that's kind
[2802.34 → 2802.92] of as large
[2802.92 → 2803.52] as Radiant.
[2804.98 → 2805.46] But,
[2805.82 → 2806.06] yeah,
[2806.44 → 2807.34] that's kind
[2807.34 → 2807.60] of what I
[2807.60 → 2807.78] meant.
[2808.56 → 2808.72] Yeah,
[2808.78 → 2809.36] I know that
[2809.36 → 2810.28] Radiant has
[2810.28 → 2810.92] done really
[2810.92 → 2811.28] well in
[2811.28 → 2811.58] that's got
[2811.58 → 2812.54] a huge
[2812.54 → 2812.80] community.
[2812.92 → 2813.04] I mean,
[2813.06 → 2813.32] you've even
[2813.32 → 2813.68] got your
[2813.68 → 2814.20] own GitHub
[2814.20 → 2814.88] group to
[2814.88 → 2815.76] manage that.
[2816.32 → 2816.52] And I
[2816.52 → 2817.12] think inside
[2817.12 → 2817.64] of that
[2817.64 → 2818.84] group,
[2819.36 → 2820.00] you've got
[2820.00 → 2821.60] 49 members
[2821.60 → 2821.94] of that
[2821.94 → 2822.18] group,
[2822.28 → 2822.56] you've got
[2822.56 → 2823.58] 39 repos
[2823.58 → 2824.20] in that
[2824.20 → 2825.16] group.
[2825.34 → 2825.46] So,
[2826.08 → 2826.70] obviously,
[2827.10 → 2828.18] we should be
[2828.18 → 2828.80] optimistic about
[2828.80 → 2829.32] open source,
[2829.48 → 2830.12] and you did a
[2830.12 → 2830.86] great job with
[2830.86 → 2831.54] leading this and
[2831.54 → 2832.08] starting this.
[2832.64 → 2833.24] But speaking
[2833.24 → 2834.50] towards the
[2834.50 → 2835.96] community that's
[2835.96 → 2836.58] prompt up around
[2836.58 → 2836.90] Radiant,
[2836.98 → 2837.36] what were some
[2837.36 → 2837.70] of the things
[2837.70 → 2838.16] that you think
[2838.16 → 2839.30] you and the
[2839.30 → 2839.72] community did
[2839.72 → 2840.32] right to
[2840.32 → 2841.06] enforce?
[2841.06 → 2841.74] And help
[2841.74 → 2842.40] elevate and
[2842.40 → 2843.36] provide support
[2843.36 → 2843.58] to the
[2843.58 → 2844.04] Radiant community
[2844.04 → 2844.98] and Radiant
[2844.98 → 2845.56] as a project?
[2848.94 → 2849.94] I think
[2849.94 → 2852.96] the early
[2852.96 → 2853.88] success of
[2853.88 → 2854.58] Radiant was
[2854.58 → 2855.80] the result of
[2855.80 → 2857.30] the plug-in
[2857.30 → 2857.74] system.
[2858.28 → 2859.14] I was very,
[2859.28 → 2859.92] very dogmatic
[2859.92 → 2860.60] about what
[2860.60 → 2861.46] would go in
[2861.46 → 2861.88] and what
[2861.88 → 2862.42] wouldn't go
[2862.42 → 2862.70] in.
[2862.70 → 2864.70] and I
[2864.70 → 2865.12] look back
[2865.12 → 2865.62] on that
[2865.62 → 2866.42] dogmatism
[2866.42 → 2866.94] now,
[2867.10 → 2867.68] and I'm
[2867.68 → 2868.52] grateful for
[2868.52 → 2868.88] it in
[2868.88 → 2869.50] some ways,
[2869.60 → 2869.80] but I'm
[2869.80 → 2870.20] also,
[2870.66 → 2871.86] I also
[2871.86 → 2873.04] realized that
[2873.04 → 2875.04] one of the
[2875.04 → 2876.28] important things
[2876.28 → 2876.72] about an
[2876.72 → 2877.12] open source
[2877.12 → 2878.32] project is
[2878.32 → 2878.76] that you
[2878.76 → 2879.42] have a
[2879.42 → 2879.88] way for
[2879.88 → 2880.24] people to
[2880.24 → 2880.58] be able to
[2880.58 → 2880.80] make
[2880.80 → 2881.54] contributions.
[2881.54 → 2884.72] in the
[2884.72 → 2885.12] beginning,
[2885.46 → 2885.88] I was
[2885.88 → 2886.40] really,
[2886.40 → 2887.12] really guarded
[2887.12 → 2888.76] about stuff,
[2888.84 → 2889.30] and part of
[2889.30 → 2889.98] it was that
[2889.98 → 2891.08] the tools that
[2891.08 → 2891.82] were available,
[2892.92 → 2893.40] subversion,
[2893.56 → 2894.38] we had our own
[2894.38 → 2895.44] subversion repository,
[2895.44 → 2896.64] and the
[2896.64 → 2897.26] tools just
[2897.26 → 2899.20] didn't allow
[2899.20 → 2900.12] you to take
[2900.12 → 2900.98] contributions
[2900.98 → 2902.12] like in the
[2902.12 → 2902.58] way that it
[2902.58 → 2903.20] happens on
[2903.20 → 2903.48] GitHub.
[2905.28 → 2905.84] Now,
[2906.08 → 2906.70] on GitHub,
[2907.40 → 2908.14] if you trust
[2908.14 → 2908.52] somebody,
[2908.60 → 2909.06] you can press
[2909.06 → 2909.48] a single
[2909.48 → 2910.20] button and
[2910.20 → 2910.70] their changes
[2910.70 → 2911.30] get merged
[2911.30 → 2911.60] in,
[2912.18 → 2912.54] kind of
[2912.54 → 2912.80] thing.
[2914.04 → 2914.30] Now,
[2914.70 → 2915.52] you should be
[2915.52 → 2915.98] running the
[2915.98 → 2916.68] test on that
[2916.68 → 2917.36] before you do
[2917.36 → 2917.64] that,
[2917.74 → 2919.04] but the
[2919.04 → 2919.84] point is that
[2919.84 → 2921.00] it's that
[2921.00 → 2921.90] easy now
[2921.90 → 2923.84] to pull in
[2923.84 → 2924.42] changes from
[2924.42 → 2924.94] other people,
[2925.04 → 2925.24] so,
[2925.44 → 2926.16] at the
[2926.16 → 2926.68] time,
[2926.84 → 2927.42] I can
[2927.42 → 2928.24] remember when
[2928.24 → 2929.02] Sean started
[2929.02 → 2930.00] using Git
[2930.00 → 2931.26] and GitHub
[2931.26 → 2931.94] came out,
[2932.04 → 2932.40] and this was
[2932.40 → 2932.88] before
[2932.88 → 2934.04] Radiant
[2934.04 → 2935.72] was doing
[2935.72 → 2936.00] that.
[2936.08 → 2936.32] At the
[2936.32 → 2936.74] time,
[2936.96 → 2937.66] we were a
[2937.66 → 2937.92] lot
[2937.92 → 2938.46] more guarded
[2938.46 → 2938.92] about,
[2939.08 → 2939.34] like,
[2939.56 → 2940.12] who could
[2940.12 → 2940.84] commit stuff
[2940.84 → 2942.08] and how,
[2942.22 → 2942.58] and there's
[2942.58 → 2943.54] definitely,
[2944.12 → 2944.76] it's a
[2944.76 → 2945.58] challenge because
[2945.58 → 2946.50] you want to
[2946.50 → 2947.64] be clear about
[2947.64 → 2948.52] the direction
[2948.52 → 2949.14] you're going
[2949.14 → 2949.50] in,
[2950.20 → 2951.86] but you
[2951.86 → 2952.48] also don't
[2952.48 → 2953.20] want to,
[2953.20 → 2953.62] like,
[2953.70 → 2954.16] discourage
[2954.16 → 2954.82] creativity
[2954.82 → 2955.74] and
[2955.74 → 2957.66] contributions
[2957.66 → 2958.98] because there's
[2958.98 → 2959.34] going to come
[2959.34 → 2959.56] a lot of
[2959.56 → 2960.02] time if
[2960.02 → 2960.34] your open
[2960.34 → 2960.94] source project
[2960.94 → 2961.74] is successful
[2961.74 → 2963.24] when you
[2963.24 → 2963.68] just get
[2963.68 → 2964.40] burnt out
[2964.40 → 2965.84] if you're
[2965.84 → 2966.36] doing all
[2966.36 → 2966.56] of the
[2966.56 → 2966.88] work,
[2967.10 → 2967.38] right?
[2967.38 → 2969.62] So I
[2969.62 → 2970.32] think one
[2970.32 → 2970.56] of the
[2970.56 → 2971.26] things that
[2971.26 → 2972.60] I think
[2972.60 → 2973.64] about more
[2973.64 → 2974.44] is,
[2974.78 → 2975.32] like,
[2975.38 → 2975.76] how can
[2975.76 → 2977.24] I allow
[2977.24 → 2977.90] someone else
[2977.90 → 2978.28] to take
[2978.28 → 2978.80] over this
[2978.80 → 2979.46] responsibility?
[2981.04 → 2981.68] And it's
[2981.68 → 2982.34] hard because,
[2982.50 → 2982.68] like,
[2983.60 → 2986.32] well,
[2986.46 → 2987.28] I'm a
[2987.28 → 2988.08] perfectionist.
[2988.16 → 2988.40] I'm a
[2988.40 → 2989.24] perfectionist in
[2989.24 → 2989.72] terms of the
[2989.72 → 2990.12] way that I
[2990.12 → 2990.86] look at code.
[2991.02 → 2991.34] I'm a
[2991.34 → 2992.10] perfectionist in
[2992.10 → 2992.38] the way I
[2992.38 → 2992.64] look at
[2992.64 → 2993.62] interfaces and
[2993.62 → 2994.72] all that kind
[2994.72 → 2995.00] of stuff.
[2995.00 → 2995.38] And so,
[2995.86 → 2996.08] like,
[2996.12 → 2996.64] if something
[2996.64 → 2997.30] is not
[2997.30 → 2998.64] perfect when
[2998.64 → 3000.04] it goes into
[3000.04 → 3000.74] the application,
[3000.86 → 3001.28] there's a part
[3001.28 → 3001.66] of me that,
[3001.66 → 3001.86] like,
[3001.96 → 3002.30] dies,
[3002.54 → 3003.34] you know?
[3003.96 → 3004.70] It's just,
[3004.86 → 3005.98] it's so important
[3005.98 → 3006.66] to me that it,
[3006.66 → 3006.88] like,
[3006.96 → 3007.72] it is right.
[3007.72 → 3009.10] and yet,
[3009.44 → 3012.32] I've had to
[3012.32 → 3013.80] kind of learn
[3013.80 → 3015.56] to back down
[3015.56 → 3016.76] from that and
[3016.76 → 3017.32] recognize,
[3017.48 → 3017.90] you know what,
[3017.94 → 3018.90] this is the
[3018.90 → 3020.34] way that,
[3020.42 → 3020.86] like,
[3020.90 → 3021.80] it works when
[3021.80 → 3022.34] you're on a
[3022.34 → 3022.68] team.
[3023.22 → 3023.48] You know,
[3023.52 → 3024.02] one person
[3024.02 → 3024.46] contributes
[3024.46 → 3024.88] something,
[3024.96 → 3025.38] it may not
[3025.38 → 3025.76] be,
[3025.76 → 3026.14] like,
[3026.24 → 3026.78] the best,
[3027.30 → 3028.26] but it's,
[3028.26 → 3028.48] like,
[3028.58 → 3029.48] filling a gap.
[3030.12 → 3031.04] It's progress.
[3031.36 → 3031.52] Yeah,
[3031.58 → 3032.16] it's progress.
[3032.44 → 3032.98] It's going in
[3032.98 → 3033.28] the right
[3033.28 → 3033.70] direction.
[3033.70 → 3034.38] And,
[3034.62 → 3036.18] so,
[3036.48 → 3037.74] I think,
[3038.26 → 3039.34] in some ways,
[3040.70 → 3041.28] as far as the
[3041.28 → 3041.92] way that Radiant
[3041.92 → 3042.22] went,
[3044.26 → 3045.14] I was really
[3045.14 → 3045.86] fortunate,
[3046.42 → 3047.84] well,
[3047.90 → 3048.22] I was really
[3048.22 → 3048.80] fortunate that
[3048.80 → 3049.32] Sean Cripps
[3049.32 → 3049.96] came along,
[3050.08 → 3050.54] in particular,
[3051.46 → 3054.12] in that he
[3054.12 → 3055.08] was able to
[3055.08 → 3056.80] slowly kind
[3056.80 → 3058.16] of wrench
[3058.16 → 3058.88] the code
[3058.88 → 3059.44] away from
[3059.44 → 3060.16] my fingers
[3060.16 → 3061.58] and start
[3061.58 → 3062.42] submitting stuff
[3062.42 → 3063.22] and then at
[3063.22 → 3063.80] different point
[3063.80 → 3064.62] Sean gave
[3064.62 → 3065.80] other people
[3065.80 → 3066.54] to their
[3066.54 → 3067.10] rights to
[3067.10 → 3067.64] their project
[3067.64 → 3068.16] that,
[3068.92 → 3069.42] you know,
[3069.50 → 3070.52] at some point
[3070.52 → 3071.12] you kind of
[3071.12 → 3071.74] realize that,
[3071.82 → 3071.98] like,
[3072.00 → 3073.10] you can't do
[3073.10 → 3074.16] it all
[3074.16 → 3076.06] yourself and
[3076.06 → 3077.46] that if
[3077.46 → 3078.52] anything's going
[3078.52 → 3078.96] to happen,
[3079.48 → 3080.52] you've got to,
[3080.52 → 3081.18] like,
[3081.32 → 3081.88] turn over the
[3081.88 → 3082.38] reins and let
[3082.38 → 3083.02] people go with
[3083.02 → 3083.16] it.
[3083.34 → 3084.80] And people
[3084.80 → 3085.54] grow into
[3085.54 → 3086.18] these things,
[3086.22 → 3086.86] which is really
[3086.86 → 3087.58] neat to me,
[3087.84 → 3089.12] watching the
[3089.12 → 3089.62] way that open
[3089.62 → 3090.40] source works.
[3090.40 → 3093.44] we've definitely
[3093.44 → 3094.22] seen on
[3094.22 → 3094.74] Radiant,
[3095.22 → 3096.52] our developers,
[3096.68 → 3096.90] like,
[3097.08 → 3097.76] grow in
[3097.76 → 3099.26] the way that
[3099.26 → 3101.44] they interact
[3101.44 → 3102.08] with people
[3102.08 → 3103.56] and the
[3103.56 → 3103.92] way that
[3103.92 → 3105.04] their coding
[3105.04 → 3106.10] style improves
[3106.10 → 3107.32] and various
[3107.32 → 3107.82] things like
[3107.82 → 3108.10] that.
[3108.10 → 3109.16] And giving
[3109.16 → 3109.76] them kind
[3109.76 → 3110.84] of a home,
[3111.22 → 3111.98] a place
[3111.98 → 3112.36] where they
[3112.36 → 3114.14] can do
[3114.14 → 3116.18] that is
[3116.18 → 3118.36] really vital
[3118.36 → 3120.36] to successful
[3120.36 → 3120.98] open source,
[3121.06 → 3121.42] I guess.
[3123.26 → 3124.22] So it's
[3124.22 → 3126.70] been a
[3126.70 → 3127.72] learning experience
[3127.72 → 3129.42] working with
[3129.42 → 3129.80] Radiant.
[3130.92 → 3131.78] I think
[3131.78 → 3134.24] I've been
[3134.24 → 3135.22] really fortunate
[3135.22 → 3137.42] the way that
[3137.42 → 3137.90] things have
[3137.90 → 3138.56] fallen out.
[3139.46 → 3140.56] My dogmatism
[3140.56 → 3141.04] could have killed
[3141.04 → 3141.54] the project
[3141.54 → 3142.16] in the beginning.
[3143.22 → 3144.72] I recognize
[3144.72 → 3145.42] that now,
[3145.54 → 3147.38] but it
[3147.38 → 3148.08] came really
[3148.08 → 3148.84] close at a
[3148.84 → 3149.40] certain point.
[3149.66 → 3150.32] And it
[3150.32 → 3150.76] was just
[3150.76 → 3151.46] because we
[3151.46 → 3153.30] decided we're
[3153.30 → 3153.70] going to do
[3153.70 → 3154.28] an extension
[3154.28 → 3155.20] system that
[3155.20 → 3158.16] didn't happen
[3158.16 → 3158.86] because people
[3158.86 → 3160.42] had a place
[3160.42 → 3160.84] where they
[3160.84 → 3162.10] could work
[3162.10 → 3162.50] out their
[3162.50 → 3163.14] frustrations
[3163.14 → 3163.68] with the way
[3163.68 → 3164.10] that Radiant
[3164.10 → 3164.84] was in a
[3164.84 → 3165.38] different way.
[3167.48 → 3168.84] So when
[3168.84 → 3169.08] you're not
[3169.08 → 3169.66] hacking on
[3169.66 → 3170.30] the client
[3170.30 → 3171.16] projects that
[3171.16 → 3171.94] you do,
[3172.46 → 3172.94] you mentioned
[3172.94 → 3173.52] that you work
[3173.52 → 3174.40] with Turanian
[3174.40 → 3175.46] and a few
[3175.46 → 3176.22] other client
[3176.22 → 3176.62] projects that
[3176.62 → 3177.02] you work on,
[3177.06 → 3177.22] but when
[3177.22 → 3177.42] you're not
[3177.42 → 3177.82] doing that
[3177.82 → 3178.00] and you're
[3178.00 → 3178.40] not hacking
[3178.40 → 3178.70] away at
[3178.70 → 3179.62] serve or
[3179.62 → 3181.18] this fun
[3181.18 → 3181.60] dream called
[3181.60 → 3182.30] Acoustic or
[3182.30 → 3182.92] maybe even
[3182.92 → 3184.38] managing or
[3184.38 → 3185.14] working on
[3185.14 → 3185.68] Radiant,
[3185.80 → 3186.28] what other
[3186.28 → 3186.92] open source
[3186.92 → 3188.78] projects got
[3188.78 → 3189.22] you excited
[3189.22 → 3190.16] that you like
[3190.16 → 3190.44] to mess
[3190.44 → 3190.92] around with?
[3193.12 → 3194.42] I am very
[3194.42 → 3195.46] excited about
[3195.46 → 3196.50] Compass right
[3196.50 → 3196.84] now.
[3198.68 → 3199.56] That's a big
[3199.56 → 3199.88] one.
[3199.88 → 3202.98] I am not
[3202.98 → 3203.44] as much
[3203.44 → 3203.94] of like a
[3203.94 → 3204.94] contributor to
[3204.94 → 3205.56] other open
[3205.56 → 3206.22] source projects
[3206.22 → 3206.78] as I probably
[3206.78 → 3207.60] should be.
[3208.64 → 3209.50] I did
[3209.50 → 3210.28] commit some
[3210.28 → 3211.98] or work
[3211.98 → 3212.32] on some
[3212.32 → 3212.86] different parts
[3212.86 → 3213.34] that were
[3213.34 → 3214.62] in early
[3214.62 → 3215.26] versions of
[3215.26 → 3215.62] Rails.
[3218.76 → 3219.32] Definitely
[3219.32 → 3220.28] having fun
[3220.28 → 3221.50] with Rack.
[3222.94 → 3223.68] Just getting
[3223.68 → 3224.20] to delve in
[3224.20 → 3224.64] with that a
[3224.64 → 3224.94] little bit
[3224.94 → 3225.64] with serve
[3225.64 → 3226.86] has been
[3226.86 → 3227.26] fun.
[3228.70 → 3229.64] I find it
[3229.64 → 3230.40] really fascinating
[3230.40 → 3230.98] that such a
[3230.98 → 3231.78] simple interface
[3231.78 → 3232.60] can be
[3232.60 → 3233.58] extended in
[3233.58 → 3234.04] so many
[3234.04 → 3235.38] cool ways.
[3237.34 → 3238.38] There's a
[3238.38 → 3239.30] little application
[3239.30 → 3240.00] out there
[3240.00 → 3242.04] and actually
[3242.04 → 3242.50] it's a
[3242.50 → 3243.28] rack handler
[3243.28 → 3244.72] called
[3244.72 → 3246.26] Rack Lobster
[3246.26 → 3247.82] which like
[3247.82 → 3249.38] is a web
[3249.38 → 3250.22] application that
[3250.22 → 3250.90] prints out a
[3250.90 → 3251.76] lobster on the
[3251.76 → 3252.06] screen.
[3252.06 → 3254.00] I can
[3254.00 → 3254.56] remember when
[3254.56 → 3255.12] I discovered
[3255.12 → 3255.64] that thinking
[3255.64 → 3256.14] that was the
[3256.14 → 3256.70] most hilarious
[3256.70 → 3257.20] thing.
[3260.50 → 3261.14] Yeah.
[3262.18 → 3263.02] Doing a
[3263.02 → 3263.30] little bit
[3263.30 → 3263.90] with jQuery
[3263.90 → 3264.42] plugins
[3264.42 → 3265.82] occasionally.
[3268.46 → 3269.14] Writing
[3269.14 → 3269.60] some of my
[3269.60 → 3270.00] own.
[3271.70 → 3272.36] I've done a
[3272.36 → 3272.64] lot with
[3272.64 → 3274.00] prototypes and
[3274.00 → 3274.46] there's a
[3274.46 → 3276.00] library by
[3276.00 → 3276.92] Dan Webb
[3276.92 → 3280.12] that adds
[3280.12 → 3280.82] some class
[3280.82 → 3281.74] selector stuff
[3281.74 → 3282.98] to prototype
[3282.98 → 3284.30] that I
[3284.30 → 3284.58] enjoy.
[3284.72 → 3284.96] That's
[3284.96 → 3285.14] called
[3285.14 → 3285.72] Low Pro.
[3289.16 → 3289.60] Yeah.
[3290.12 → 3290.68] That would
[3290.68 → 3291.06] be a couple.
[3292.66 → 3293.36] I think
[3293.36 → 3293.98] one of the
[3293.98 → 3294.72] fun ones
[3294.72 → 3295.48] that I'd
[3295.48 → 3295.68] like to
[3295.68 → 3296.30] dive deeper
[3296.30 → 3296.78] in with
[3296.78 → 3297.52] you would
[3297.52 → 3298.62] be what
[3298.62 → 3298.88] you like
[3298.88 → 3299.14] about
[3299.14 → 3299.38] Compass.
[3300.90 → 3301.74] You said
[3301.74 → 3302.02] Compass
[3302.02 → 3302.48] specifically
[3302.48 → 3302.82] and not
[3302.82 → 3303.20] SAS.
[3303.30 → 3303.56] I'm kind
[3303.56 → 3303.86] of curious
[3303.86 → 3304.16] why you
[3304.16 → 3304.46] just said
[3304.46 → 3304.72] Compass.
[3304.72 → 3306.00] I guess
[3306.00 → 3306.36] I kind
[3306.36 → 3306.66] of think
[3306.66 → 3307.06] of Compass
[3307.06 → 3307.56] and SAS
[3307.56 → 3307.96] as being
[3307.96 → 3308.36] sort of
[3308.36 → 3308.88] the same
[3308.88 → 3309.48] thing now.
[3310.52 → 3310.84] Right.
[3311.14 → 3311.76] I kind
[3311.76 → 3311.96] of do
[3311.96 → 3312.10] too.
[3312.16 → 3312.34] I just
[3312.34 → 3312.54] wondered
[3312.54 → 3312.80] if there
[3312.80 → 3313.04] was
[3313.04 → 3314.66] what was
[3314.66 → 3314.92] happening
[3314.92 → 3315.30] in Compass
[3315.30 → 3315.76] more so
[3315.76 → 3316.34] than SAS.
[3317.80 → 3318.06] Yeah.
[3318.22 → 3318.38] I mean
[3318.38 → 3319.46] both of
[3319.46 → 3320.28] those projects
[3320.28 → 3320.82] are definitely
[3320.82 → 3321.44] evolving.
[3323.06 → 3323.76] I guess
[3323.76 → 3324.40] the joy
[3324.40 → 3325.38] that I get
[3325.38 → 3326.04] out of it
[3326.04 → 3326.50] on a daily
[3326.50 → 3326.88] basis
[3326.88 → 3327.22] is just
[3327.22 → 3327.66] the stuff
[3327.66 → 3328.52] that Chris
[3328.52 → 3328.94] Epstein
[3328.94 → 3329.52] has put
[3329.52 → 3330.94] into Compass
[3330.94 → 3333.28] all the
[3333.28 → 3334.00] CSS3
[3334.00 → 3334.52] stuff.
[3334.72 → 3336.60] being able
[3336.60 → 3337.52] to take
[3337.52 → 3337.88] advantage
[3337.88 → 3338.26] of that
[3338.26 → 3338.68] in a way
[3338.68 → 3339.32] that works
[3339.32 → 3339.74] across
[3339.74 → 3340.28] browsers.
[3341.04 → 3341.96] I love
[3341.96 → 3342.68] that stuff.
[3343.02 → 3343.42] I don't
[3343.42 → 3343.96] think I
[3343.96 → 3344.34] would be
[3344.34 → 3344.70] messing
[3344.70 → 3345.16] around
[3345.16 → 3346.06] with CSS3
[3346.06 → 3346.94] if it
[3346.94 → 3347.24] wasn't
[3347.24 → 3348.08] for Chris
[3348.08 → 3348.56] and Compass
[3348.56 → 3349.14] because it's
[3349.14 → 3350.20] just a pain
[3350.20 → 3350.58] to write
[3350.58 → 3351.16] all of those
[3351.16 → 3351.88] attributes
[3351.88 → 3352.68] like 80
[3352.68 → 3353.18] times.
[3354.18 → 3354.36] Yeah.
[3354.72 → 3355.36] It is
[3355.36 → 3355.82] probably the
[3355.82 → 3356.16] biggest.
[3357.06 → 3357.56] I think
[3357.56 → 3358.10] that there's
[3358.10 → 3358.80] any CSS
[3358.80 → 3359.24] developer
[3359.24 → 3359.72] listening to
[3359.72 → 3360.16] this podcast
[3360.16 → 3360.70] right now.
[3360.80 → 3360.96] If you
[3360.96 → 3361.34] haven't
[3361.34 → 3361.62] touched
[3361.62 → 3362.08] SAS
[3362.08 → 3363.14] or Compass
[3363.14 → 3363.70] you owe
[3363.70 → 3364.08] it to
[3364.08 → 3364.84] your future
[3364.84 → 3365.54] career to
[3365.54 → 3366.14] go get
[3366.14 → 3366.36] started
[3366.36 → 3366.86] right now.
[3368.54 → 3368.98] Especially
[3368.98 → 3369.38] when you're
[3369.38 → 3369.66] talking about
[3369.66 → 3370.14] CSS3.
[3370.22 → 3370.86] I just saw
[3370.86 → 3372.32] a tweet
[3372.32 → 3373.32] today from
[3373.32 → 3374.88] one of our
[3374.88 → 3375.42] good friends.
[3375.50 → 3376.22] Let me see if I can
[3376.22 → 3377.10] refresh my tweet
[3377.10 → 3377.80] screen, so I don't
[3377.80 → 3380.38] recall his name.
[3382.50 → 3382.90] Geez,
[3383.02 → 3383.96] he's so well
[3383.96 → 3384.34] known too.
[3384.40 → 3385.62] I can't recall
[3385.62 → 3386.32] why his name
[3386.32 → 3387.22] isn't coming to
[3387.22 → 3387.82] my mind.
[3387.82 → 3388.72] but he works
[3388.72 → 3390.14] at India,
[3390.86 → 3391.70] is really
[3391.70 → 3392.60] well known for
[3392.60 → 3393.26] writing tons and
[3393.26 → 3393.50] tons of
[3393.50 → 3393.84] plugins.
[3394.12 → 3394.94] He's more of a
[3394.94 → 3395.76] developer than he
[3395.76 → 3396.42] is a designer but
[3396.42 → 3396.86] he's also a
[3396.86 → 3397.16] designer.
[3398.32 → 3398.88] And his name
[3398.88 → 3399.62] is Mike.
[3400.32 → 3400.98] Can't recall his
[3400.98 → 3401.38] last name.
[3402.10 → 3402.58] So horrible.
[3403.10 → 3403.50] Anyway,
[3403.94 → 3404.48] sorry Mike.
[3405.32 → 3407.00] But he had said
[3407.00 → 3407.84] basically that,
[3408.38 → 3409.02] Geez I totally
[3409.02 → 3409.64] lost the train of
[3409.64 → 3410.04] thought that I was
[3410.04 → 3410.84] even talking about.
[3411.16 → 3411.68] Basically he was
[3411.68 → 3412.36] just saying that
[3412.36 → 3415.20] because of
[3415.20 → 3416.40] SAS and because
[3416.40 → 3416.86] of Compass,
[3416.86 → 3418.62] he's,
[3419.04 → 3419.56] or because of
[3419.56 → 3420.34] CSS3 he's like
[3420.34 → 3420.98] never touching
[3420.98 → 3421.90] Photoshop ever
[3421.90 → 3422.76] anymore.
[3423.00 → 3423.66] He's pretty much
[3423.66 → 3425.58] just having fun in
[3425.58 → 3426.22] Illustrator and
[3426.22 → 3427.02] writing the browser.
[3428.10 → 3428.54] And that's kind of
[3428.54 → 3429.10] my take too.
[3429.20 → 3429.80] As soon as I picked
[3429.80 → 3431.50] up CSS3 I pretty
[3431.50 → 3432.34] much don't even do
[3432.34 → 3432.50] that.
[3432.58 → 3433.30] And I probably am
[3433.30 → 3433.98] like you, I wouldn't
[3433.98 → 3434.84] have picked up CSS3
[3434.84 → 3437.06] sooner as I have
[3437.06 → 3438.58] or even have as
[3438.58 → 3439.90] much fun with it if
[3439.90 → 3440.52] it weren't for just
[3440.52 → 3441.88] writing one line to
[3441.88 → 3443.04] put out border
[3443.04 → 3444.04] radius versus
[3444.04 → 3444.42] eight.
[3445.40 → 3445.80] Yeah,
[3445.80 → 3447.44] I love that
[3447.44 → 3448.28] aspect of it.
[3449.04 → 3449.48] SAS,
[3449.74 → 3451.10] I could say a lot
[3451.10 → 3452.04] on SAS too.
[3452.24 → 3455.96] Just the way
[3455.96 → 3456.64] that it allows me
[3456.64 → 3457.20] to kind of write
[3457.20 → 3457.90] my own,
[3459.04 → 3459.78] to structure my
[3459.78 → 3460.84] code well as I'm
[3460.84 → 3461.40] writing CSS.
[3463.28 → 3464.94] I haven't so much
[3464.94 → 3465.46] developed,
[3466.52 → 3467.06] I wouldn't call it
[3467.06 → 3468.58] a library of SAS
[3468.58 → 3469.62] code that I use
[3469.62 → 3471.80] so much as I tend
[3471.80 → 3472.94] to copy modules
[3472.94 → 3473.98] from project to
[3473.98 → 3474.34] project.
[3475.34 → 3476.96] So I have a
[3476.96 → 3478.32] typography module
[3478.32 → 3479.22] that's got a lot
[3479.22 → 3480.58] of defaults in it
[3480.58 → 3481.44] for the way that I
[3481.44 → 3482.48] like to do the
[3482.48 → 3483.54] style, you know,
[3483.54 → 3484.28] my typography.
[3486.28 → 3487.48] And being able to
[3487.48 → 3488.98] do that, share the
[3488.98 → 3489.96] code in that way
[3489.96 → 3491.42] is huge.
[3493.00 → 3493.92] And the way that
[3493.92 → 3495.36] I'm able to create
[3495.36 → 3496.58] small little modules
[3496.58 → 3498.82] that do one thing
[3498.82 → 3502.16] and then use
[3502.16 → 3502.78] that everywhere
[3502.78 → 3503.44] throughout my
[3503.44 → 3503.84] code.
[3504.78 → 3505.18] Yeah,
[3505.30 → 3506.16] I love it.
[3506.74 → 3507.10] It's great.
[3507.10 → 3507.42] Yeah,
[3507.58 → 3508.32] I think, you know,
[3508.40 → 3509.10] Compass being able
[3509.10 → 3509.84] to framework in
[3509.84 → 3510.62] general, like it's,
[3511.14 → 3511.78] people might be
[3511.78 → 3512.74] misguided with what
[3512.74 → 3513.60] Compass is and,
[3513.82 → 3513.96] you know,
[3513.98 → 3514.82] when you say it's a
[3514.82 → 3516.24] CSS frame working tool,
[3516.68 → 3517.30] in the end,
[3517.38 → 3518.16] the libraries within
[3518.16 → 3518.86] it aren't really
[3518.86 → 3519.46] frameworks like,
[3519.54 → 3519.98] for example,
[3520.60 → 3521.70] Blueprint and
[3521.70 → 3522.76] 960GS,
[3522.94 → 3523.38] those aren't really
[3523.38 → 3523.76] frameworks,
[3523.86 → 3524.66] those are more so
[3524.66 → 3525.68] libraries,
[3525.90 → 3526.90] as Chris would say.
[3526.90 → 3528.56] and Compass,
[3528.82 → 3529.14] theoretically,
[3529.28 → 3530.06] is the frame working
[3530.06 → 3530.54] tool because it
[3530.54 → 3531.34] allows you to truly
[3531.34 → 3533.12] create a framework
[3533.12 → 3533.98] of your working
[3533.98 → 3534.48] style.
[3534.74 → 3534.82] Like,
[3534.86 → 3535.60] I'm sure you have
[3535.60 → 3537.00] a structure for
[3537.00 → 3537.78] your Sass that
[3537.78 → 3538.68] makes sense within
[3538.68 → 3540.20] working with Sass
[3540.20 → 3540.60] and Compass,
[3540.72 → 3541.38] and I do too,
[3541.50 → 3542.68] and that's really
[3542.68 → 3543.36] what I love about it.
[3543.38 → 3543.52] It's like,
[3543.54 → 3544.60] you can kind of
[3544.60 → 3545.20] get into your
[3545.20 → 3545.74] grooves,
[3546.04 → 3546.46] find your
[3546.46 → 3547.18] optimizations,
[3547.50 → 3548.16] find your ways
[3548.16 → 3548.78] that you streamline
[3548.78 → 3549.52] the way you do
[3549.52 → 3550.02] things,
[3550.20 → 3551.20] and you can just
[3551.20 → 3552.34] like pattern that
[3552.34 → 3553.26] with Compass and
[3553.26 → 3553.94] Sass and just
[3553.94 → 3554.24] go.
[3555.48 → 3555.84] Yeah.
[3556.90 → 3558.30] I mean,
[3558.32 → 3558.84] I think Fancy
[3558.84 → 3559.60] Buttons is a good
[3559.60 → 3560.78] example of a
[3560.78 → 3562.72] framework,
[3563.00 → 3563.40] I guess,
[3563.82 → 3564.14] within,
[3564.48 → 3565.24] just being distributed
[3565.24 → 3565.84] with Compass,
[3566.60 → 3568.74] well,
[3569.20 → 3569.94] with Compass in
[3569.94 → 3570.32] mind.
[3572.10 → 3572.78] Just so,
[3572.94 → 3574.62] for those of you
[3574.62 → 3575.26] that don't know,
[3575.88 → 3576.58] Fancy Buttons
[3576.58 → 3578.24] contains a lot of
[3578.24 → 3579.16] CSS code for
[3579.16 → 3580.08] styling buttons
[3580.08 → 3581.24] in a bulletproof
[3581.24 → 3581.58] way,
[3581.58 → 3583.96] and if you
[3583.96 → 3584.48] use it on a
[3584.48 → 3584.88] project,
[3585.56 → 3586.88] you get access
[3586.88 → 3587.36] to a couple
[3587.36 → 3588.04] of mix zones
[3588.04 → 3589.50] that would
[3589.50 → 3590.34] allow you to
[3590.34 → 3592.28] create buttons
[3592.28 → 3593.04] with a single
[3593.04 → 3593.72] line of code.
[3593.94 → 3594.18] You just
[3594.18 → 3594.76] don't like the
[3594.76 → 3595.34] colour that you
[3595.34 → 3595.74] want,
[3596.56 → 3597.36] pass a couple
[3597.36 → 3598.14] of options in,
[3598.20 → 3598.88] and it does
[3598.88 → 3599.34] the rest.
[3600.52 → 3600.90] I almost think
[3600.90 → 3601.26] you should have
[3601.26 → 3602.22] made that project
[3602.22 → 3602.58] called,
[3602.58 → 3603.28] it should have
[3603.28 → 3603.60] been called
[3603.60 → 3604.40] Magic Buttons
[3604.40 → 3605.50] or something
[3605.50 → 3606.14] like that.
[3606.56 → 3606.80] Yeah,
[3606.88 → 3607.18] I don't know.
[3607.40 → 3607.92] Because it's like
[3607.92 → 3608.28] magic.
[3608.28 → 3610.06] If you know
[3610.06 → 3610.44] Brandon,
[3610.68 → 3612.22] Fancy's kind
[3612.22 → 3612.58] of cool.
[3612.94 → 3613.42] It's the most
[3613.42 → 3615.36] excellent Fancy
[3615.36 → 3616.28] Buttons project.
[3617.24 → 3617.50] Yeah.
[3618.04 → 3618.56] We love
[3618.56 → 3618.82] Brandon.
[3618.88 → 3619.26] He's been on
[3619.26 → 3619.90] the show before.
[3620.04 → 3620.52] You know that.
[3621.82 → 3622.62] Brandon's awesome.
[3623.14 → 3623.66] I met him a
[3623.66 → 3624.32] couple years ago
[3624.32 → 3625.52] at my friend's
[3625.52 → 3625.96] conference,
[3626.18 → 3626.62] Lesson,
[3626.62 → 3628.34] and he's a good
[3628.34 → 3628.54] guy.
[3628.66 → 3629.46] I certainly look
[3629.46 → 3629.98] up to him and
[3629.98 → 3630.60] his code and
[3630.60 → 3631.26] what he does,
[3631.96 → 3633.22] and he's big
[3633.22 → 3635.30] in the Sass
[3635.30 → 3635.64] and Compass
[3635.64 → 3636.08] where he's done
[3636.08 → 3636.46] a lot,
[3636.62 → 3636.98] and Fancy
[3636.98 → 3637.52] Buttons is
[3637.52 → 3638.08] super,
[3638.08 → 3638.74] super cool.
[3639.08 → 3639.50] But that's
[3639.50 → 3639.88] what I love
[3639.88 → 3640.42] a lot about
[3640.42 → 3640.84] Compass and
[3640.84 → 3641.22] a lot about
[3641.22 → 3641.42] Sass.
[3641.48 → 3642.04] So I echo
[3642.04 → 3643.04] whenever I'm
[3643.04 → 3644.34] not doing
[3644.34 → 3645.02] pretty much
[3645.02 → 3645.48] anything I do
[3645.48 → 3646.46] do is in
[3646.46 → 3646.86] and around
[3646.86 → 3647.32] the Compass
[3647.32 → 3647.92] ecosystem.
[3648.12 → 3648.54] I've got
[3648.54 → 3650.04] a bootstrap
[3650.04 → 3650.82] for Serve
[3650.82 → 3651.50] that I do
[3651.50 → 3651.90] that's got a
[3651.90 → 3652.20] lot of my
[3652.20 → 3653.40] fun things
[3653.40 → 3653.78] in it because
[3653.78 → 3654.08] I've been
[3654.08 → 3654.70] using Serve
[3654.70 → 3655.50] quite a bit.
[3657.78 → 3658.48] So yeah,
[3658.68 → 3658.94] Sass,
[3659.02 → 3659.44] Compass is
[3659.44 → 3660.00] always in my
[3660.00 → 3660.64] projects and
[3660.64 → 3661.22] Hamill as
[3661.22 → 3661.40] well.
[3661.68 → 3664.14] But I don't
[3664.14 → 3664.80] cry when I
[3664.80 → 3665.22] can't have
[3665.22 → 3665.50] Hamill,
[3665.64 → 3666.26] but I can
[3666.26 → 3666.68] certainly feel
[3666.68 → 3667.02] the pain.
[3667.02 → 3668.00] Yeah,
[3668.48 → 3670.12] I think I
[3670.12 → 3670.48] could live
[3670.48 → 3670.98] without Hamill,
[3671.06 → 3671.44] but I probably
[3671.44 → 3671.84] couldn't live
[3671.84 → 3672.58] without Fans
[3672.58 → 3672.86] now.
[3673.10 → 3673.32] It's just
[3673.32 → 3674.58] so much
[3674.58 → 3676.64] as a part
[3676.64 → 3676.96] of what
[3676.96 → 3677.48] saves me
[3677.48 → 3678.36] time on
[3678.36 → 3679.26] my projects.
[3679.26 → 3680.72] Well,
[3680.76 → 3680.86] John,
[3680.88 → 3681.20] we certainly
[3681.20 → 3681.92] appreciate you
[3681.92 → 3682.26] coming on
[3682.26 → 3682.60] the show
[3682.60 → 3682.98] and sharing
[3682.98 → 3683.36] your feelings
[3683.36 → 3683.88] about open
[3683.88 → 3684.52] source and
[3684.52 → 3685.48] your continued
[3685.48 → 3686.50] optimism for
[3686.50 → 3687.22] open source
[3687.22 → 3688.98] as well as
[3688.98 → 3689.54] the work that
[3689.54 → 3689.88] you've done
[3689.88 → 3690.50] with Radiant
[3690.50 → 3690.82] and building
[3690.82 → 3691.32] that community
[3691.32 → 3692.28] and the work
[3692.28 → 3692.52] you're doing
[3692.52 → 3692.98] on Serve
[3692.98 → 3694.58] and all the
[3694.58 → 3694.98] stuff that you
[3694.98 → 3695.36] bring to the
[3695.36 → 3695.70] community and
[3695.70 → 3696.20] the ecosystem.
[3696.72 → 3697.74] I know that
[3697.74 → 3698.12] Wynn and I
[3698.12 → 3698.98] both certainly
[3698.98 → 3700.30] enjoy what you
[3700.30 → 3701.22] do and I think
[3701.22 → 3701.58] you're an awesome
[3701.58 → 3702.34] designer and it
[3702.34 → 3702.94] was fun having
[3702.94 → 3703.48] you on the show.
[3703.72 → 3704.16] So thanks for
[3704.16 → 3704.56] coming on.
[3704.56 → 3705.04] Yeah,
[3705.18 → 3705.36] well,
[3705.42 → 3705.80] I really
[3705.80 → 3706.42] appreciate the
[3706.42 → 3706.94] invite.
[3708.00 → 3708.54] It's just
[3708.54 → 3708.76] great.
[3708.88 → 3709.26] I love what
[3709.26 → 3709.98] the changelog
[3709.98 → 3711.16] does, and it's
[3711.16 → 3711.60] fun to be on
[3711.60 → 3711.84] the show.
[3712.34 → 3712.70] Awesome.
[3712.82 → 3713.16] Thanks.
[3713.16 → 3713.28] Thanks.
[3734.56 → 3735.56] Thanks.
[3735.56 → 3736.56] Thanks.
[3736.56 → 3737.56] Thanks.
[3737.56 → 3738.56] Thanks.
