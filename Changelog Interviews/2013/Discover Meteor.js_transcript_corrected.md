[0.00 → 13.46] Welcome back everybody, this is The Change Log, we're a member supported blog and podcast
[13.46 → 16.14] that covers what's fresh and what's new in open source.
[16.26 → 23.14] You can check out the blog at thechangelog.com and our past shows at 5by5.tv slash changelog.
[23.26 → 26.80] And this show is hosted by myself, Adam Stachowiak, and Andrew Thorpe.
[26.90 → 27.26] Hey man.
[27.68 → 28.20] Hey, how's it going?
[28.20 → 31.04] It is an awesome, awesome day, man.
[31.66 → 36.94] You can tune in live to this show every Tuesday at 5pm Central Standard Time right here on 5by5.
[37.08 → 44.32] And this is episode number 91, and we're joined by Sasha Grief, a fantastic, and when I say fantastic, I mean in all caps,
[44.74 → 47.48] interface designer, as well as a guest contributor to The Change Log.
[48.00 → 50.94] And I guess now, Sasha, we can add Hacker to that list as well, right?
[51.06 → 52.24] So, welcome to the show.
[52.84 → 53.60] Hey guys, hi.
[54.52 → 56.90] So we got Sasha Grief on the call here.
[56.90 → 61.20] He's, he's wrote, you've written a book on something really cool, man.
[61.24 → 62.26] What did you write this book on?
[63.22 → 67.90] So, I've co-written a book on Meteor, a JavaScript framework.
[67.90 → 78.18] And Meteor kind of meteorically came onto the scene about a year and a halfback, which is a fun little rise for that framework.
[78.44 → 85.74] But before we dive deep into the show, why don't you give the listeners a mention of whom you are?
[86.20 → 86.72] What do you do?
[86.72 → 87.64] Sure.
[88.08 → 91.92] So, right now I'm living in Japan, in Osaka, Japan.
[92.54 → 97.04] And I mostly work on my own projects, such as the book.
[97.72 → 101.48] But before that, I used to do a lot of freelance design work.
[101.90 → 105.34] So, mostly UI design, web app design.
[105.34 → 114.78] And I worked for companies such as Chipmunk, Ruby Motion, and also Code Academy.
[115.04 → 120.10] So, a lot of startups and a lot of people in the tech world.
[121.32 → 126.44] But actually, even before that, my main background is computer science.
[126.44 → 135.54] So, yeah, I kind of have a weird background where I was first more of a coder than designer, and then now back to being a bit of a coder.
[135.74 → 138.58] I see the history I know of you is mostly in the design side.
[140.30 → 143.64] Yeah, well, I have always...
[143.64 → 147.36] When I say computer science, I went to college to study that.
[147.36 → 152.74] And if you've studied computer science, you know it has nothing to do with the web.
[153.06 → 157.62] And it's really different from what we do day to day.
[157.76 → 160.76] So, I didn't really enjoy that that much.
[160.94 → 164.68] And this is why I went on to work on the web.
[164.92 → 168.24] And the part I liked the most about that was design.
[168.42 → 172.64] So, I've kind of always followed my interest or tried to.
[173.40 → 176.40] And it's just seen where it takes me, basically.
[176.40 → 177.12] Yeah.
[178.12 → 180.54] Yeah, so you do bring up something good.
[180.68 → 185.54] That when you are a computer science student, and it's...
[185.54 → 187.04] I mean, I was a computer science student in college.
[187.14 → 188.50] It's a great thing.
[188.84 → 193.64] But what we tend to do now, there's kind of these two different paths you can take.
[194.08 → 196.24] And, well, there's a million different paths you can take.
[196.54 → 197.50] You know, cue the music.
[197.66 → 203.66] But when we graduated, when I graduated, you could either kind of go like the more traditional route
[203.66 → 205.92] or this kind of like emerging web technology route.
[206.72 → 209.92] And so, that kind of gets us to where we are now.
[210.78 → 212.92] And so, with one of the big new emerging...
[213.88 → 216.78] I don't know if you would call it a technology, but the framework of Meteor.
[217.84 → 218.72] Very exciting.
[219.90 → 221.38] It's a very neat project.
[221.64 → 223.62] I got involved very early on.
[223.94 → 226.00] And by involved, I mean I joined the mailing list.
[226.00 → 232.36] So, why don't you give us a kind of overview, Sasha, of what Meteor is.
[232.76 → 235.08] Yeah, why don't you give us an overview of what is Meteor.js?
[236.70 → 237.14] Okay.
[237.32 → 241.48] So, Meteor.js is a framework built on top of Node.
[241.48 → 246.16] And it's really a full-stack framework.
[246.16 → 250.80] So, it takes care of the server side and the client side.
[251.80 → 254.80] And it's made by a couple of guys in San Francisco.
[255.68 → 258.00] So, the company itself is Meteor.
[258.20 → 259.76] It's their whole product.
[259.76 → 262.82] And it's interesting for a few reasons.
[263.02 → 268.04] Because, first, it's entirely JavaScript since its Node.
[268.32 → 272.38] So, personally, I really like that you don't need any context switching between, you know,
[272.46 → 275.02] Ruby and JavaScript or PHP and JavaScript.
[275.02 → 280.08] And the other thing is its reactive and real-time.
[281.44 → 288.16] So, what that means, being reactive, is that any change to the data in the database
[288.16 → 291.86] will automatically get reflected in the user interface in the browser.
[292.68 → 296.12] And Meteor takes care of keeping all that in sync for you.
[297.32 → 302.04] And real-time means that these changes happen instantly, which is also pretty cool.
[302.04 → 309.22] Yeah. So, being on the web and when you're talking about state and different things like that,
[309.64 → 313.86] it's really cool to see something like Meteor that you have.
[314.40 → 317.36] It almost seemed like it was going to be a pipe dream for a long time.
[317.44 → 321.62] And I think, you know, Node.js, obviously, is something that's made this possible.
[321.88 → 326.46] But it almost seemed like to be able to write code on the server and on the front end,
[326.80 → 329.94] you know, in terms of web development, was a pipe dream for a long time, right?
[329.94 → 334.64] So, this is something that comes along, that, you know, Node comes along and then Meteor comes along.
[334.80 → 339.32] And this is the reason why I, you know, like I signed up on the mailing list so fast,
[339.36 → 343.00] was because it seemed like this, what I always, you know, thought of,
[343.02 → 345.70] and you heard people talk about it as this pipe dream, was starting to come to fruition.
[345.92 → 350.96] And that was, you know, people will essentially have to learn one language
[350.96 → 354.30] to be able to write an entire stack on the web, right?
[354.30 → 355.34] And that's really cool.
[356.04 → 360.20] So, for somebody like, you know, you, so we thought, Sasha, that, you know,
[360.24 → 365.86] you had more of a design background, but you've kind of blown the top off of it.
[366.12 → 370.44] But no, so for somebody who does tend to do more design work on the web,
[371.06 → 372.04] this is a great entry point, right?
[372.08 → 376.80] Because you no longer need to learn all these different technologies
[376.80 → 379.86] to be able to do, like, your own side project or your own gig.
[379.86 → 384.58] This is just one technology that you can learn in the sense of JavaScript,
[385.02 → 390.36] one language that you can learn to be able to do, you know, do a whole project, you know?
[390.46 → 394.82] So is that one of the probably most exciting things about Meteor, would you say?
[395.72 → 400.74] Yeah, I think it's really exciting and really important because, like, you know,
[400.78 → 402.12] we do this stuff all day.
[402.30 → 407.76] So for us, it becomes a second nature to make Ruby and JavaScript play nice
[407.76 → 408.54] and stuff like that.
[408.54 → 412.14] But for someone who's new, you know, they'll be like, okay,
[412.16 → 415.60] why do I have to learn two languages just to do what I want to do?
[416.28 → 422.22] So, and that's also the reason why I think Meteor is going to be fascinating
[422.22 → 425.34] for people like front-end engineers, designers,
[426.02 → 428.24] people who already know the syntax of JavaScript,
[428.62 → 433.82] but want to start their own, you know, side project or startup or whatever
[433.82 → 438.04] and don't want to learn yet another language just to have a database
[438.04 → 440.00] and have user accounts and all that.
[441.20 → 446.20] So what does Meteor look like for things like databases and that side of things?
[446.20 → 448.20] How does Meteor handle those problems?
[449.20 → 451.20] So Meteor works with MongoDB,
[452.20 → 455.94] and it's very tightly integrated.
[455.94 → 459.86] So it's not that easy to swap in another database,
[460.00 → 461.72] but people are working on that right now.
[463.14 → 470.34] And, yeah, because Meteor kind of replicates a subset of your database on the client,
[470.66 → 472.14] so in memory in the browser,
[472.96 → 476.56] and this way you can have very fast access to the data
[476.56 → 479.76] and you don't need to go back to the server every time.
[479.76 → 485.08] So, yeah, you use the MongoDB API both on the client and the server, basically.
[485.80 → 490.00] So there are a lot of tools that I think came out, you know, before Meteor.
[490.82 → 492.52] Well, I don't know if they came out before Meteor,
[492.62 → 496.06] but they were, you know, different solutions to different problems.
[496.32 → 498.34] Like, I think one of them was called Lawn Chair,
[498.74 → 501.92] and it was a, I think it was a it was,
[502.70 → 505.34] and I don't know if an implementation is the right word,
[505.34 → 511.16] but it was kind of built around this idea of the couch, you know, couch DB,
[511.68 → 513.56] or, you know, the NoSQL kind of stuff.
[513.68 → 518.54] And it was, in local storage, it was like a simple JSON database, right?
[518.78 → 522.86] When these tools came out and then Meteor came out, you know, after that,
[523.14 → 525.38] did Meteor use a lot of these tools,
[525.46 → 528.66] or did they rebuild all these things from scratch, I guess is my question.
[530.36 → 532.46] You'd have to ask the Meteor guys themselves,
[532.46 → 535.50] but I think they built a lot of it from scratch.
[535.64 → 536.42] I'm pretty sure they did.
[536.98 → 538.04] Yeah, they did.
[538.10 → 539.30] I just wanted to get you to say that.
[540.32 → 540.64] Okay.
[541.12 → 542.60] I think they did anyway as well.
[542.96 → 546.94] And that's one of the things that is almost refreshing,
[547.18 → 551.24] because, you know, right now it seems like the trend in open source,
[551.38 → 552.88] and the trend, I don't even know if it's open source,
[552.96 → 553.98] just the trend in development.
[554.14 → 557.28] I mean, you know, Adam and I work in a 9 to 5 together.
[558.74 → 560.58] I don't know if a 9 to 5 is the best way to put it,
[560.58 → 562.12] because it seems to be a lot more than that.
[562.12 → 562.38] Yeah, yeah.
[562.70 → 564.90] But we work on, you know, our day-to-day,
[565.08 → 567.64] or our real, you know, full-time job together.
[567.84 → 570.38] And even as not an open source project,
[570.44 → 573.14] the trend is to kind of leverage all the other tools that are out there.
[573.18 → 574.42] That's what makes open source beautiful.
[574.62 → 577.28] But it's almost refreshing with something like Meteor
[577.28 → 579.10] when they kind of say, you know what,
[579.42 → 581.04] obviously MongoDB is not,
[581.32 → 583.22] it wouldn't make sense for them to write their own database.
[583.46 → 585.06] But, you know, wherever possible,
[585.18 → 588.52] let's build our implementation of the solution
[588.52 → 590.60] so that we can make sure it all works together.
[590.60 → 592.24] And that's refreshing, I think.
[592.32 → 593.62] I'm excited to see that.
[594.00 → 595.58] You just hope that it doesn't, you know,
[595.64 → 597.46] create even more options for newcomers
[597.46 → 598.62] that have to figure out what to use.
[598.72 → 600.58] But, no, it's definitely something that's exciting.
[602.32 → 603.10] Yeah, I agree.
[603.20 → 605.68] And I think, you know, having more options,
[605.86 → 607.18] I agree it can be a problem,
[607.28 → 609.28] but Meteor is in a space, you know,
[609.30 → 611.72] it's not like one more front-end JavaScript framework.
[611.78 → 613.32] It's really a thing in itself.
[613.32 → 616.10] And I don't see many other frameworks like it.
[616.78 → 618.40] Yeah, how does it differ from,
[618.54 → 619.68] I think, what is the other,
[620.02 → 621.28] there's another big Node framework,
[621.38 → 622.32] I think it's called Express.
[623.32 → 624.32] I have never used it.
[624.38 → 625.08] Have you ever used it?
[626.04 → 626.94] No, I haven't,
[627.00 → 628.96] so I don't want to say something wrong.
[629.36 → 632.50] But, yeah, I don't think it's quite the same thing.
[632.92 → 633.94] Yeah, I don't think it is either.
[634.04 → 636.08] It would be interesting to actually not be an idiot
[636.08 → 637.04] on the subject myself
[637.04 → 638.32] and actually be able to clarify.
[638.32 → 638.86] But, hey.
[639.90 → 642.20] I guess the closest competitor is called Derby.
[643.12 → 645.66] They're the ones who do the most similar thing.
[646.60 → 646.72] Hmm.
[647.32 → 647.72] Derby.
[648.42 → 648.80] Yeah.
[649.06 → 649.82] I haven't heard of that one.
[650.06 → 650.80] I have not either.
[651.80 → 653.18] We'll have to reach out to those guys.
[653.72 → 655.50] Somebody should write Discover Derby.
[656.64 → 657.04] Right.
[657.14 → 657.56] Yeah, they should.
[657.80 → 658.44] Yeah, they should.
[658.66 → 658.98] They should.
[659.30 → 659.72] Well, there's,
[660.76 → 661.48] well, then it's kind of neat.
[661.54 → 663.98] I was hoping maybe you can share your thoughts on this
[663.98 → 666.86] and maybe just kind of glean into how you got into Meteor.
[666.86 → 669.20] But there's these seven principles of Meteor.
[669.34 → 670.08] It's data on the wire,
[670.20 → 671.46] one language, database everywhere,
[671.46 → 673.42] and a number of others, you know,
[673.48 → 677.02] cool buzzwords that are really meaningful to developers.
[677.30 → 679.26] But what was it that got you into Meteor?
[679.36 → 680.50] Like, how did you discover it
[680.50 → 682.60] and then ultimately write a book about it?
[684.02 → 685.88] So it's kind of a funny story
[685.88 → 689.54] because the original reason I learned Meteor
[689.54 → 690.92] was to build a sidebar.
[691.76 → 693.70] So sidebar is a site.
[693.84 → 695.20] It's a very simple site, actually.
[695.20 → 698.38] It's a list of the five best design links of the day.
[699.20 → 701.26] So you wouldn't think you would need Meteor
[701.26 → 702.34] to build something like that,
[702.56 → 705.94] like a plain HTML file would do just as well.
[706.68 → 710.36] But originally, my idea was to do something more
[710.36 → 711.98] like a hacker news for designers.
[713.28 → 714.46] And when I had this idea,
[714.54 → 716.54] I started looking around for frameworks
[716.54 → 719.20] and existing open source apps,
[719.26 → 720.68] and I couldn't really find anything.
[720.68 → 723.18] So I started working on my own.
[723.48 → 725.62] And I actually didn't do that.
[725.80 → 726.48] I actually hired,
[726.82 → 729.66] looked for someone to hire or work with on this project.
[730.44 → 733.88] And the guy I ended up finding was a Node.js developer.
[734.74 → 737.92] So we worked on that for maybe about a week.
[738.74 → 741.68] And then another friend told me about Meteor
[741.68 → 742.96] and said it was really cool.
[742.96 → 744.70] And he had just met the guys
[744.70 → 746.04] because he's in San Francisco.
[746.86 → 748.26] And they were a great team.
[748.62 → 751.26] So, I mean, since I wasn't the one
[751.26 → 753.02] doing any of the coding at that point,
[753.30 → 755.88] I said, hey, sure, I'll pass the information along.
[756.02 → 758.54] So I sent the link to my coder friend.
[758.80 → 760.62] And he said, oh, Meteor looks really cool.
[760.68 → 762.46] Let's use that for the project.
[762.46 → 766.26] And, like, one week later,
[766.42 → 769.32] I started not hearing back from him anymore.
[769.62 → 771.36] And I guess he got busy.
[773.00 → 777.28] So, yeah, I had this brand-new Meteor app
[777.28 → 779.36] and no coder anymore.
[779.58 → 780.62] So I said, okay, well,
[781.18 → 782.52] I'll see what I can do by myself.
[783.64 → 785.60] And I guess a couple of months later,
[785.72 → 786.30] I wrote a book.
[787.70 → 791.32] So Sidebar, you can check it out at sidebar.io.
[792.46 → 794.16] And it's cool, right?
[794.20 → 796.44] It's like it almost looks like Hacker News, right?
[796.66 → 798.54] Obviously, you picked similar colours.
[798.96 → 802.26] And it's like a beautiful version of Hacker News.
[802.64 → 803.80] And it doesn't seem to have
[803.80 → 805.38] as much of the negative comments on it.
[805.44 → 806.18] So I like that, too.
[806.32 → 808.18] It's also down to constraints, too.
[808.24 → 810.06] It's got five links a day.
[810.34 → 813.46] You're also pulling in some cool people.
[813.84 → 815.16] Not so much cool people,
[815.30 → 817.32] but good designers, known designers
[817.32 → 819.32] that either are establishing their own tribe
[819.32 → 820.20] or have their own tribe
[820.20 → 823.74] that they're sharing only one good design link per day.
[824.22 → 825.48] I guess the question is,
[825.54 → 827.88] is not long before that,
[827.94 → 829.48] maybe about six or seven months before that,
[829.52 → 830.76] you built the Toolbox.cc,
[830.98 → 833.34] which probably isn't in a similar space,
[833.38 → 835.94] but it's about sharing images and links.
[835.94 → 837.62] Why did you decide to,
[838.20 → 839.32] or I guess is there any plans
[839.32 → 841.06] to go back to the Toolbox.cc
[841.06 → 843.90] and rebuild this with Meteor?
[843.90 → 846.70] You know, it's like you're reading my mind
[846.70 → 849.20] because I'm actually thinking
[849.20 → 850.76] that it would be a very cool project
[850.76 → 851.58] to do just that.
[851.70 → 851.94] Yeah.
[852.52 → 854.26] Because the Toolbox is built on WordPress,
[854.66 → 858.98] but it doesn't use any of the features
[858.98 → 859.96] like comments or anything.
[860.30 → 862.12] So yeah, it would be pretty easy
[862.12 → 863.06] to build a Meteor.
[863.12 → 864.08] And I was thinking it could make
[864.08 → 866.24] for a good screencast or tutorial.
[866.74 → 867.78] Or another book.
[868.26 → 869.12] Or another book.
[869.32 → 870.28] WordPress to Meteor.
[870.42 → 871.76] I mean, that's your title right there, right?
[871.76 → 872.78] Right. Yeah, exactly.
[873.84 → 877.32] So now that we kind of know what Meteor is
[877.32 → 879.48] and talked about a couple of the projects,
[879.58 → 880.82] why don't we move on to the book?
[881.42 → 883.64] Discover Meteor was written by you and another guy.
[883.82 → 885.58] Who was the other guy that wrote it,
[885.60 → 886.72] if you want to introduce him?
[887.66 → 889.60] Okay, so the other guy is Tom Coleman.
[890.00 → 890.96] And I feel like you should say
[890.96 → 892.48] the book was written by Tom Coleman
[892.48 → 893.42] and another guy
[893.42 → 899.02] because he actually has much better credentials than me,
[899.18 → 900.38] at least in the Meteor community,
[900.38 → 903.98] because he's the main guy maintaining Meteor, right?
[904.18 → 907.92] Which is the third-party package manager for Meteor.
[909.06 → 910.12] And apart from that,
[910.94 → 914.16] he also has the router package,
[914.78 → 917.74] like one of the main router packages for Meteor
[917.74 → 920.22] and a couple other open-source Meteor projects.
[920.66 → 923.80] So yeah, he's a really smart guy.
[924.14 → 927.80] And I feel like outside the Meteor team,
[927.80 → 930.04] he's one of the people who know the most about Meteor.
[931.84 → 933.46] So you and him get together.
[933.54 → 935.98] How did you guys meet and decide
[935.98 → 938.36] that you were going to write a book together?
[938.36 → 942.54] So we started working together on Telescope.
[942.54 → 945.34] So Telescope is the open-source app
[945.34 → 947.04] that I ended up building with Meteor
[947.04 → 949.34] in order to build Sidebar.
[950.32 → 952.58] So I decided to make it open-source
[952.58 → 957.88] and I went looking for people to help me with the process.
[957.88 → 962.00] And Tom was probably the most helpful person.
[962.34 → 967.18] He helped me a lot with the more intricate parts of Meteor.
[967.68 → 971.96] And we just connected, and we started working together on this.
[972.22 → 972.86] And eventually,
[973.68 → 977.16] we felt that we learned so much building Telescope
[977.16 → 979.68] that it just made sense to write a book.
[979.68 → 982.74] So a little side note,
[982.78 → 983.92] it's not easy to find Telescope.
[984.00 → 988.64] I don't know if there's another URL besides the T-E-L-E-S-C dot P-E.
[989.46 → 990.86] But if you check it out,
[990.94 → 992.64] and I wanted to just mention this,
[992.76 → 995.22] those are probably the two coolest buttons
[995.22 → 996.52] that I've seen on the web
[996.52 → 999.18] are the try demo and fork on GitHub buttons on Telescope.
[999.94 → 1000.34] Thanks.
[1002.24 → 1002.92] I love them.
[1002.98 → 1004.84] So Telescope is a project
[1004.84 → 1007.52] that was actually before Discover Meteor.
[1007.52 → 1010.70] And when you guys are writing Discover Meteor,
[1010.82 → 1015.42] you essentially recreated a smaller version of Telescope for the book.
[1015.48 → 1017.56] And that's kind of the whole book, right?
[1017.60 → 1019.28] You kind of tutorial type book
[1019.28 → 1023.14] that takes you from zero to deploy of this other app.
[1024.00 → 1024.52] Exactly.
[1024.76 → 1027.86] So this Telescope is a social news app.
[1028.00 → 1030.40] So basically a Reddit or Hacker News clone.
[1031.10 → 1033.14] And the app you're building in the book
[1033.14 → 1036.30] is a smaller, lighter version of it called Microscope.
[1036.30 → 1039.60] And so it's also a Hacker News clone,
[1039.72 → 1043.48] but with a few less features compared to Telescope.
[1045.76 → 1046.20] Gotcha.
[1046.32 → 1048.96] So who would you say is the target audience
[1048.96 → 1050.34] for the book Discover Meteor?
[1052.24 → 1055.80] So I like to say there's like three target audiences.
[1056.70 → 1057.94] The first one,
[1058.42 → 1059.90] and I guess the easiest one to reach,
[1059.98 → 1061.52] would be existing Meteor developers.
[1061.52 → 1066.08] And so far we've had a perfect reception with them.
[1067.82 → 1069.68] But the second much bigger audience
[1069.68 → 1071.36] is just developers in general.
[1071.82 → 1075.00] So I believe there's a lot of interest for Meteor out there.
[1075.72 → 1077.32] And even people who are, you know,
[1077.40 → 1079.44] Rails developers or PHP developers,
[1079.82 → 1082.62] since they all already know JavaScript,
[1083.18 → 1083.54] probably,
[1083.54 → 1087.58] getting started with Meteor is not a huge leap for them.
[1088.80 → 1090.12] And I guess the last audience,
[1091.00 → 1092.72] which might be even bigger,
[1092.84 → 1093.86] is just, you know,
[1093.90 → 1096.32] people who don't see themselves as programmers at all.
[1096.40 → 1097.00] So designers,
[1097.98 → 1100.26] maybe people who, you know,
[1100.34 → 1102.10] marketing people who want to learn to code,
[1102.20 → 1102.78] business people.
[1102.78 → 1107.50] And maybe Meteor is still a little bit young for them,
[1107.62 → 1110.24] but I believe eventually it will become a pretty good option,
[1110.50 → 1110.72] you know,
[1110.78 → 1113.30] as their first programming environment.
[1114.62 → 1118.58] So the book would be very appropriate for them too.
[1120.10 → 1122.00] Yeah, I'm about halfway through the book right now,
[1122.04 → 1122.94] and I intend to write a
[1123.62 → 1126.22] write up on it on the changelog when I'm finished.
[1126.30 → 1126.98] So far it's a
[1127.42 → 1128.42] I'm really enjoying it.
[1128.58 → 1129.92] It's been a great book so far.
[1129.92 → 1133.38] Or is the book itself written in Meteor?
[1134.98 → 1136.24] Yeah, you could say that.
[1138.50 → 1139.16] So the
[1139.28 → 1139.46] the
[1139.60 → 1140.48] when you buy the book,
[1140.60 → 1143.12] you get access to the online version of the book,
[1143.14 → 1144.76] and that is a Meteor app.
[1145.86 → 1147.74] So the reason we,
[1147.78 → 1148.38] we did that,
[1148.48 → 1148.96] first,
[1148.96 → 1151.72] we couldn't find any other good solution to,
[1151.72 → 1152.58] you know,
[1152.64 → 1155.20] restrict access to only people who have bought the book.
[1155.96 → 1157.46] So we had to create our own.
[1158.38 → 1159.12] And we picked Meteor,
[1159.12 → 1160.42] well,
[1160.50 → 1160.84] first,
[1160.90 → 1161.78] if we didn't pick Meteor,
[1161.86 → 1163.04] people would ask us,
[1163.20 → 1163.34] oh,
[1163.36 → 1164.38] you're writing a book about Meteor.
[1164.46 → 1165.92] Why didn't you pick Meteor for the app?
[1166.00 → 1167.28] So that was the
[1167.34 → 1167.90] a big reason.
[1168.32 → 1169.18] And also,
[1169.42 → 1174.76] although right now there's like no real need for Meteor in that app,
[1174.84 → 1179.10] eventually we'd like to add things like maybe real-time annotations,
[1179.10 → 1183.10] or maybe showing you who else is reading the book at that time.
[1184.04 → 1186.98] And using Meteor gave us the freedom to,
[1187.10 → 1187.62] in the future,
[1187.72 → 1189.80] maybe add a lot of cool features like that.
[1190.84 → 1190.96] Yeah,
[1191.04 → 1192.48] real-time annotation would be cool.
[1192.74 → 1193.26] You would think,
[1193.36 → 1193.80] just because,
[1193.88 → 1194.10] you know,
[1194.58 → 1195.72] it's hard as an author,
[1195.82 → 1196.02] right?
[1196.08 → 1196.90] So you know,
[1197.70 → 1198.88] you know Meteor,
[1199.02 → 1199.50] you know,
[1199.50 → 1199.98] you know,
[1200.10 → 1201.50] core principles and,
[1201.50 → 1202.48] you know,
[1202.58 → 1203.46] software design,
[1203.62 → 1204.28] software development.
[1204.76 → 1206.40] So it's hard,
[1206.54 → 1206.72] I think,
[1206.80 → 1211.72] to kind of like reach the gamut of everybody because you might,
[1212.04 → 1212.50] you know,
[1212.56 → 1214.20] assume some gaps in knowledge that,
[1214.34 → 1216.50] that are probably assumptions we shouldn't make.
[1216.66 → 1219.82] So something like real-time annotation seems like it would be really cool for
[1219.82 → 1220.82] people to be able to like,
[1221.16 → 1222.06] if they know no,
[1222.16 → 1224.76] if they have no knowledge of programming at all,
[1224.76 → 1225.56] or if they have,
[1225.66 → 1225.82] you know,
[1225.86 → 1226.96] no knowledge of JavaScript,
[1227.24 → 1227.68] then they can,
[1228.04 → 1228.18] you know,
[1228.22 → 1231.70] some people can start conversations around pieces that might not make sense or,
[1231.78 → 1232.18] you know,
[1232.18 → 1234.04] might help clarify it and then,
[1234.36 → 1234.68] you know,
[1234.92 → 1237.86] potentially even get back into the book through another distribution of it.
[1237.88 → 1238.44] That'd be pretty neat.
[1239.26 → 1239.40] Yeah.
[1240.04 → 1244.32] And so what we've done now is we have a discuss comments in the sidebar,
[1244.76 → 1249.60] which is not as good as annotations on the actual text,
[1249.62 → 1252.92] but you can already see people like talking to each other and,
[1252.92 → 1255.08] and answering each other's questions.
[1255.08 → 1255.86] So that's pretty cool.
[1256.80 → 1259.24] So how's the popularity of this gone for you?
[1259.24 → 1260.36] Like what is the
[1260.48 → 1261.06] what have been the
[1261.22 → 1261.34] you know,
[1261.34 → 1263.30] channels that you've kind of pushed this out through?
[1264.86 → 1267.84] I guess that the main channel was just our mailing list.
[1268.08 → 1270.12] So for the past four months,
[1270.32 → 1272.48] basically ever since we had the idea for the book,
[1272.56 → 1279.32] we started collecting emails and wrote a blog on the discovermeteor.com.
[1280.78 → 1282.24] And apart from that,
[1282.38 → 1285.98] the meteor guys have helped us a lot with promotion,
[1285.98 → 1289.80] like featuring the book on their blog and in their mailing list.
[1289.80 → 1291.98] Um,
[1291.98 → 1294.98] we also had a lot of great reviews on sites like,
[1294.98 → 1295.28] uh,
[1295.28 → 1296.14] daily JS,
[1296.38 → 1296.64] uh,
[1296.64 → 1298.12] info queue and a few others.
[1299.62 → 1300.26] So yeah,
[1300.26 → 1301.18] I guess all that together,
[1301.18 → 1301.72] uh,
[1301.72 → 1303.38] ended up being a pretty good,
[1303.38 → 1303.72] uh,
[1304.36 → 1305.26] source of sales.
[1305.26 → 1307.10] And I think we,
[1307.10 → 1308.72] we just crossed like 1000 sales,
[1308.72 → 1309.08] I think.
[1309.30 → 1309.66] Wow.
[1309.76 → 1309.96] Oh,
[1310.00 → 1310.26] wow.
[1311.34 → 1312.08] That certainly shows,
[1312.08 → 1313.64] there's a definite audience there for,
[1313.72 → 1314.02] for sure.
[1314.08 → 1314.22] I mean,
[1314.22 → 1315.32] obviously there's a meteor audience,
[1315.44 → 1315.62] but,
[1315.72 → 1316.00] uh,
[1316.00 → 1317.68] just in general,
[1317.72 → 1318.30] it shows the
[1318.54 → 1318.74] I mean,
[1318.76 → 1320.44] you've only released it to about what,
[1320.50 → 1321.78] three or four weeks ago at the most.
[1322.64 → 1322.82] Uh,
[1322.84 → 1323.52] three weeks ago.
[1323.60 → 1323.80] Yeah.
[1323.92 → 1324.48] That's insane.
[1325.98 → 1326.84] That's pretty crazy.
[1326.84 → 1327.12] But,
[1327.20 → 1327.40] uh,
[1327.42 → 1328.04] you wrote a
[1328.38 → 1332.78] I mentioned the first part of the show that you were also a guest
[1332.78 → 1334.48] contributor on the change log.
[1334.48 → 1336.52] So for those tuning in,
[1336.62 → 1336.96] uh,
[1336.96 → 1339.24] Sasha's actually written on the change log.
[1339.30 → 1339.42] He,
[1339.50 → 1341.48] he wrote a post called six months with meteor.
[1341.98 → 1344.56] Why the future of the web is real time.
[1344.56 → 1346.32] And in there you made a very,
[1346.32 → 1347.92] a very bold statement.
[1347.92 → 1348.52] I would say,
[1348.60 → 1350.78] I would hope that maybe you can back up here on,
[1350.90 → 1351.34] on the show.
[1351.40 → 1352.58] You said the future is,
[1352.58 → 1355.70] you said the future is real time.
[1356.08 → 1356.44] And,
[1356.52 → 1356.70] uh,
[1356.70 → 1356.84] there,
[1356.92 → 1359.90] there was a lot of conversation about that on hacker news when we posted
[1359.90 → 1360.90] this link to there.
[1360.90 → 1361.08] And,
[1361.20 → 1361.78] uh,
[1361.78 → 1365.28] I think that was a pretty dramatic day for the change law too,
[1365.28 → 1366.82] because this post brought in,
[1366.88 → 1368.30] I don't even can't remember the number,
[1368.32 → 1368.92] but it was like,
[1368.92 → 1371.66] like 15,000 visits that day alone or something like that.
[1371.66 → 1373.78] So a lot of conversation on hacker news around,
[1373.78 → 1374.76] uh,
[1374.76 → 1375.04] you know,
[1375.32 → 1377.42] these types of statements and just using media in general.
[1377.42 → 1381.86] So what do you say when people ask you why the future of the web is real
[1381.86 → 1382.22] time?
[1383.06 → 1383.42] Yeah.
[1383.46 → 1383.88] First,
[1383.88 → 1384.70] you got me scared,
[1384.82 → 1384.94] Derek.
[1385.06 → 1386.76] I didn't remember what statement I made.
[1387.36 → 1387.72] No,
[1387.78 → 1388.90] I wasn't going to throw you under the bus.
[1388.96 → 1389.36] Don't worry.
[1390.26 → 1390.62] Okay.
[1390.70 → 1390.92] So,
[1391.00 → 1391.16] okay.
[1391.98 → 1395.36] The reason I said that is if you look at your computer,
[1395.52 → 1395.84] uh,
[1395.84 → 1397.48] almost everything is real time.
[1398.56 → 1398.88] Um,
[1399.64 → 1401.74] maybe not real time in the sense of,
[1401.74 → 1402.32] um,
[1403.00 → 1404.34] things happening in real time,
[1404.34 → 1406.64] but real time in the sense that you don't need to refresh,
[1406.64 → 1407.42] uh,
[1407.42 → 1408.54] windows to see changes.
[1408.54 → 1409.10] And,
[1409.10 → 1409.80] uh,
[1409.80 → 1410.90] there's not this idea of,
[1410.90 → 1411.08] uh,
[1411.72 → 1412.02] you know,
[1412.24 → 1413.18] page requests.
[1413.18 → 1413.66] So,
[1413.66 → 1414.62] uh,
[1414.62 → 1416.72] the example I always give is if you,
[1416.84 → 1417.08] um,
[1417.14 → 1418.36] if you open the same window,
[1418.36 → 1418.88] uh,
[1418.88 → 1420.44] on your Mac or windows,
[1420.56 → 1421.46] whatever in,
[1422.28 → 1424.22] or rather the same directory into windows,
[1424.22 → 1426.68] and you delete a file from one of these windows,
[1426.68 → 1428.94] it will also be deleted from the other one.
[1428.94 → 1429.28] You know,
[1429.32 → 1430.36] you don't need to refresh,
[1430.36 → 1430.94] uh,
[1431.16 → 1431.52] the window.
[1431.52 → 1433.58] There's no refresh button on the desktop.
[1434.54 → 1437.06] So why should it be different on the web?
[1437.18 → 1437.42] Right.
[1438.22 → 1443.98] And I think the re the only reason is different is because of technical limits that were there up to now.
[1443.98 → 1446.46] But as these limits go away,
[1446.46 → 1447.84] I think more and more,
[1447.84 → 1448.14] um,
[1449.04 → 1453.00] web apps and websites will move to a real time model.
[1453.54 → 1454.22] And again,
[1454.22 → 1455.96] I'm not saying real time in the sense of,
[1456.06 → 1456.14] Oh,
[1456.20 → 1456.56] everything,
[1456.94 → 1459.16] every update is happening one millisecond,
[1459.16 → 1459.82] you know,
[1459.82 → 1460.40] after it,
[1460.40 → 1460.96] it happens,
[1460.96 → 1461.28] but,
[1461.36 → 1462.18] uh,
[1462.18 → 1464.66] more in the sense of not having to refresh the page.
[1466.12 → 1466.60] Right.
[1466.60 → 1468.02] Real time in the sense that,
[1468.14 → 1471.24] that you're not having to initiate the
[1471.38 → 1471.54] to,
[1471.62 → 1472.54] to fetch the data,
[1472.62 → 1472.82] to,
[1472.82 → 1474.92] to update the state of what you're looking at.
[1474.92 → 1475.08] Right.
[1475.16 → 1479.02] So the page itself is in charge of keeping itself up to date.
[1479.70 → 1480.74] And on that note,
[1480.74 → 1485.36] you also said thinking in real time also influences your coding style.
[1485.44 → 1486.34] What did you mean by that?
[1487.94 → 1488.36] Okay.
[1488.38 → 1489.60] So this has to do more with,
[1489.60 → 1489.98] uh,
[1490.24 → 1490.90] reactivity.
[1491.74 → 1492.58] So meteor,
[1492.76 → 1493.14] um,
[1494.06 → 1495.78] uses like reactive programming.
[1496.60 → 1499.52] which means there are no callbacks and,
[1499.68 → 1501.20] or very few callbacks.
[1502.20 → 1504.72] And basically every variable,
[1504.88 → 1506.32] if a variable changes,
[1506.62 → 1507.54] um,
[1507.54 → 1511.56] it will be re-evaluated automatically without you needing to do anything about it.
[1512.22 → 1512.70] So,
[1512.82 → 1513.42] I mean,
[1513.44 → 1516.14] it can be very powerful, and it can be also very,
[1516.14 → 1518.16] very dangerous and very tricky.
[1519.38 → 1519.90] So,
[1520.02 → 1520.26] uh,
[1520.26 → 1521.44] to give you a practical example,
[1521.78 → 1523.02] uh,
[1523.02 → 1523.74] if you have your,
[1523.74 → 1523.98] uh,
[1523.98 → 1526.56] user object and that user object is,
[1526.60 → 1526.92] reactive,
[1527.28 → 1528.18] uh,
[1528.18 → 1530.50] anytime you change a property of the user,
[1530.62 → 1532.80] like their email or whatever,
[1532.80 → 1534.22] it will trigger,
[1534.22 → 1534.72] um,
[1534.98 → 1535.24] uh,
[1535.24 → 1539.36] re-computation of that variable anywhere where it's used.
[1539.36 → 1540.78] So if you're using that,
[1540.92 → 1541.82] you know,
[1541.82 → 1542.30] to check,
[1542.30 → 1542.68] uh,
[1542.68 → 1544.78] permissions in your,
[1544.78 → 1545.18] uh,
[1545.38 → 1546.12] router filter,
[1546.20 → 1546.64] for example,
[1546.64 → 1547.30] uh,
[1547.30 → 1548.24] that will rerun.
[1548.24 → 1549.44] Even if the
[1549.44 → 1552.86] the variable that you changed on the user actually has nothing to do with that.
[1553.46 → 1555.44] So these kinds of tricky,
[1555.44 → 1555.78] uh,
[1555.78 → 1556.76] things that you need to learn.
[1557.50 → 1560.88] And I don't think it's any better or any worse than the traditional way.
[1560.96 → 1563.18] It's just a different way of thinking and of coding.
[1564.46 → 1565.70] You bring up a good point.
[1565.70 → 1568.16] And this is just maybe a side note that I wanted to ask you.
[1568.26 → 1568.96] Are you,
[1569.26 → 1570.74] how close to actual,
[1570.74 → 1573.20] the Node.js community has this,
[1573.34 → 1573.94] has the meteor,
[1574.18 → 1574.44] you know,
[1574.44 → 1575.36] community gotten you?
[1576.80 → 1577.20] Um,
[1577.20 → 1578.44] not very close at all,
[1578.54 → 1579.02] I think.
[1579.56 → 1579.86] Well,
[1579.88 → 1581.98] you brought up something interesting when you said some,
[1582.16 → 1584.14] when you said that there aren't many callbacks in meteor.
[1584.62 → 1585.80] And if you've,
[1586.36 → 1588.34] and this is maybe a little rabbit hole,
[1588.40 → 1589.06] so stick with me,
[1589.06 → 1592.04] but if you've gotten into the Node.js community at all,
[1592.04 → 1594.86] and you've kind of got on the mailing list or gone to any of the
[1594.86 → 1595.32] uh,
[1595.58 → 1595.78] you know,
[1595.82 → 1597.26] chats that people talk about it,
[1597.26 → 1599.16] there's this debate that comes up often.
[1599.42 → 1600.24] And it's about,
[1600.32 → 1600.52] you know,
[1600.74 → 1603.24] pipes and streams and callbacks and this and that.
[1603.30 → 1603.40] And,
[1603.52 → 1603.60] you know,
[1603.60 → 1605.24] what's the right way to approach these solutions?
[1605.24 → 1606.64] And I was wondering,
[1606.64 → 1607.28] and maybe you,
[1607.38 → 1610.06] maybe you haven't really heard anything about it,
[1610.08 → 1612.60] but have you heard that in the meteor community,
[1612.68 → 1613.98] all that kind of debate with that,
[1614.08 → 1615.18] with that type of stuff?
[1616.70 → 1617.12] No,
[1617.18 → 1618.08] I'm pretty sure that,
[1619.02 → 1619.40] um,
[1619.94 → 1620.22] you know,
[1620.60 → 1621.50] meteor is different.
[1621.50 → 1623.58] And if you,
[1623.86 → 1626.46] if you don't like that way of doing things,
[1626.46 → 1630.16] you probably would not be using meteor because that's their whole,
[1630.16 → 1632.92] one of their main selling points is reactivity.
[1632.92 → 1633.42] And,
[1633.42 → 1634.24] uh,
[1634.24 → 1634.84] it's hard to,
[1634.84 → 1636.54] to dissociate that from meteor.
[1636.76 → 1638.26] So there's,
[1638.26 → 1640.10] so it is what makes meteor.
[1640.60 → 1641.10] Right.
[1641.18 → 1641.54] Exactly.
[1641.62 → 1642.66] It's a secret sauce,
[1642.72 → 1643.00] man.
[1645.40 → 1645.84] Cool.
[1647.10 → 1647.54] No.
[1647.60 → 1647.76] Yeah.
[1647.76 → 1648.34] The book,
[1648.56 → 1648.86] uh,
[1648.86 → 1649.90] discover meteor again.
[1650.24 → 1650.64] It's,
[1650.80 → 1651.34] it's a very,
[1651.44 → 1652.10] very good read.
[1652.34 → 1652.70] Um,
[1652.84 → 1653.04] I don't,
[1653.10 → 1653.64] it's not too,
[1653.88 → 1655.36] too difficult or too long,
[1655.38 → 1656.46] but it's definitely not,
[1656.48 → 1657.06] uh,
[1657.28 → 1657.86] one sitting.
[1658.08 → 1659.24] So it's,
[1659.42 → 1662.22] I find myself with far less time,
[1662.22 → 1662.72] uh,
[1662.72 → 1665.90] to read than I had before my wife and I had our first son,
[1666.04 → 1666.56] uh,
[1666.56 → 1666.98] obviously.
[1667.26 → 1668.44] And it's,
[1668.54 → 1670.48] I've been able to step away from the book and come back.
[1670.48 → 1673.66] And unfortunately I was hoping to finish it much quicker than I did.
[1673.66 → 1674.66] But one thing that,
[1674.76 → 1674.90] you know,
[1674.92 → 1675.46] I think is,
[1675.62 → 1676.48] is a
[1676.58 → 1677.08] is a good,
[1677.16 → 1682.62] a good thing to say about it is that I was able to step away and come back and not feel like I had lost too much time,
[1682.80 → 1682.96] you know,
[1682.98 → 1686.94] not feel like I was too overwhelmed with the amount of gap that I had spent.
[1687.28 → 1687.60] Uh,
[1687.70 → 1688.24] that's not a
[1688.32 → 1689.14] that's not a sentence,
[1689.32 → 1691.34] the amount of time that I had spent away from it.
[1691.40 → 1691.56] So,
[1691.82 → 1692.26] uh,
[1692.30 → 1692.56] again,
[1692.62 → 1692.84] I mean,
[1692.94 → 1693.98] I guess that's just me,
[1694.08 → 1695.42] another way for me to say it's,
[1695.54 → 1695.72] uh,
[1696.16 → 1696.60] it's a
[1696.72 → 1698.50] another way for me to be a fanboy of it and say,
[1698.54 → 1699.16] it's a great job.
[1699.76 → 1700.08] Thanks.
[1700.16 → 1700.62] That's great.
[1700.62 → 1702.62] And I'm glad you say it's,
[1702.78 → 1702.80] uh,
[1702.80 → 1703.50] you didn't read it.
[1703.50 → 1704.88] And in a single sitting,
[1704.88 → 1708.52] because we had a testimonial from someone who said something like,
[1708.64 → 1709.10] Oh,
[1709.10 → 1710.14] this book is so great.
[1710.24 → 1711.68] I just read it in two hours.
[1712.58 → 1714.28] And we're like,
[1714.36 → 1714.70] yeah,
[1714.82 → 1715.60] that wasn't the plan.
[1715.86 → 1716.50] I'm not sure if that's good.
[1717.54 → 1717.90] Well,
[1717.90 → 1718.24] especially,
[1718.36 → 1718.60] I mean,
[1718.66 → 1719.26] the way you,
[1719.40 → 1719.56] I mean,
[1719.56 → 1721.00] that also brings up a different subject too,
[1721.06 → 1722.62] which is the way you slice up the book too.
[1722.68 → 1724.20] The way you can buy it is much different than,
[1724.82 → 1725.16] um,
[1725.18 → 1726.18] let's say a different book.
[1726.18 → 1730.58] And I believe you even have a blog post about the pricing trilogy and all that.
[1730.58 → 1731.64] Maybe we can talk about that a bit,
[1731.74 → 1733.26] but if you go to,
[1733.26 → 1733.56] uh,
[1733.56 → 1735.36] discover media.com slash packages,
[1735.36 → 1737.66] you've got it sliced up into just the book,
[1737.70 → 1738.68] which is 39 bucks.
[1738.86 → 1740.04] And you've got the full edition,
[1740.16 → 1742.04] which has members area code,
[1742.14 → 1745.26] live instances and screencasts and all these other goodies that you're,
[1745.26 → 1746.18] you're packing into this.
[1746.18 → 1747.26] And that's the
[1747.26 → 1747.42] uh,
[1747.42 → 1749.32] the red giant package at 89 bucks.
[1749.44 → 1752.52] And then you get this forthcoming or coming soon edition,
[1752.62 → 1753.20] the premium edition.
[1753.34 → 1753.40] So,
[1753.48 → 1753.66] I mean,
[1754.14 → 1756.78] if you're sitting down in two hours of reading this,
[1756.78 → 1757.12] uh,
[1757.12 → 1758.84] then that's probably not a
[1758.92 → 1760.40] not the best way to do it.
[1760.40 → 1760.86] But what,
[1760.92 → 1761.74] what brought on this,
[1761.74 → 1762.50] this,
[1762.56 → 1762.92] I guess,
[1762.96 → 1764.56] type of way to release a book?
[1764.56 → 1765.70] Um,
[1766.94 → 1770.26] so it's actually a pretty common way of releasing books.
[1770.26 → 1771.16] I think at least,
[1771.16 → 1771.76] uh,
[1771.76 → 1773.72] maybe not for programming books,
[1773.72 → 1774.38] but for,
[1774.38 → 1774.68] you know,
[1774.68 → 1775.56] design books or,
[1775.56 → 1776.32] uh,
[1776.32 → 1777.00] business books.
[1777.00 → 1780.68] And I feel like the main guy who's doing that is Nathan Barry,
[1780.68 → 1783.98] who actually just came out with his third book.
[1784.10 → 1785.94] And every time he launches books,
[1785.96 → 1788.28] he has the system with three plans,
[1788.42 → 1788.92] three packages.
[1789.94 → 1790.42] And,
[1790.66 → 1790.90] uh,
[1791.46 → 1793.14] the first one will usually be,
[1793.14 → 1793.68] you know,
[1793.74 → 1795.00] priced well.
[1795.36 → 1796.00] I mean,
[1796.02 → 1796.38] not,
[1796.46 → 1796.92] not cheap,
[1797.00 → 1798.54] but not expect too expensive either.
[1798.68 → 1801.78] Then there's a middle one that's priced a little bit higher.
[1801.78 → 1805.28] And then the top one is priced usually like really expensive.
[1805.28 → 1808.62] And he prices his top package at,
[1808.66 → 1808.86] uh,
[1808.86 → 1809.46] $250.
[1810.40 → 1811.34] And we did,
[1811.34 → 1811.66] uh,
[1811.66 → 1812.70] 159.
[1813.78 → 1814.30] So,
[1814.30 → 1815.38] uh,
[1815.38 → 1816.44] what I learned from him,
[1816.44 → 1818.22] and he's been very open with his,
[1818.22 → 1818.44] uh,
[1818.44 → 1820.22] sales number is that the top package,
[1820.78 → 1821.18] uh,
[1821.56 → 1824.36] even though it will sell less in quantity in revenue,
[1824.36 → 1828.22] it will bring in a lot more revenue than all the other packages combined,
[1828.22 → 1828.76] just because,
[1828.76 → 1829.36] you know,
[1829.36 → 1830.46] it's so much more expensive.
[1831.40 → 1831.88] So,
[1832.00 → 1832.26] uh,
[1832.66 → 1833.48] you know,
[1833.52 → 1834.38] I felt that,
[1834.38 → 1838.04] we weren't sure at all if people would buy the top package,
[1838.16 → 1841.64] especially since it doesn't actually exist yet.
[1842.34 → 1842.76] But,
[1842.88 → 1843.20] um,
[1843.48 → 1843.88] you know,
[1843.90 → 1847.26] we didn't want to miss that opportunity, and we wanted to see if there was a
[1847.26 → 1847.76] market there.
[1847.92 → 1849.80] So we decided to,
[1849.90 → 1851.22] to make the effort to come out,
[1851.42 → 1852.02] come out with,
[1852.14 → 1852.34] uh,
[1852.40 → 1854.88] these three packages rather than a single price point.
[1855.54 → 1856.62] So have you,
[1856.92 → 1858.80] I don't know if you're willing to even disclose this,
[1858.80 → 1859.20] but have you,
[1859.30 → 1860.78] have you had many sales on the
[1860.86 → 1861.16] uh,
[1861.16 → 1862.56] on the premium edition?
[1862.56 → 1862.66] Hmm.
[1863.54 → 1863.98] So,
[1864.06 → 1864.22] yeah,
[1864.28 → 1864.90] surprisingly,
[1865.12 → 1865.34] uh,
[1865.34 → 1865.76] we did.
[1866.56 → 1869.08] So I think that the revenue breakdown is about,
[1869.24 → 1869.48] uh,
[1869.48 → 1871.12] the same for each package.
[1872.02 → 1873.36] So meaning we made,
[1873.42 → 1873.92] uh,
[1873.92 → 1876.04] almost as much with the top one as,
[1876.18 → 1876.38] uh,
[1876.42 → 1877.24] the other two ones.
[1877.30 → 1880.36] And I think if the top one was actually available at launch,
[1880.36 → 1881.16] uh,
[1881.16 → 1882.92] we would have made even more.
[1882.92 → 1883.36] Hmm.
[1883.76 → 1883.92] Uh,
[1883.92 → 1885.66] this is the third project in a row,
[1885.72 → 1887.54] I think where I've noticed a little,
[1887.54 → 1888.24] uh,
[1888.24 → 1889.40] funny nugget on the
[1889.40 → 1889.60] uh,
[1889.60 → 1891.42] products webpage that we've looked at.
[1891.50 → 1892.06] And on this one,
[1892.10 → 1895.68] I see codename red giant for the full edition and codename white dwarf for the
[1895.68 → 1896.46] premium edition.
[1896.70 → 1897.52] It's kind of neat.
[1898.06 → 1898.46] Yeah.
[1898.50 → 1899.00] It's the
[1899.00 → 1900.38] the life cycle of a star.
[1900.72 → 1900.90] Yep.
[1900.90 → 1903.96] So I guess the next step is a black hole,
[1904.12 → 1904.46] but yeah,
[1904.48 → 1905.70] I don't know if you should do that one.
[1905.86 → 1906.12] Yeah.
[1906.12 → 1907.18] It's not that appealing.
[1907.70 → 1908.10] Uh,
[1908.28 → 1908.62] Andrew,
[1908.74 → 1908.90] you're,
[1908.98 → 1909.44] you're so,
[1909.56 → 1910.18] you're so cunning,
[1910.28 → 1910.80] my friend.
[1910.90 → 1911.52] So cunning.
[1911.52 → 1915.46] So where do you get the reviews from typically for this that,
[1915.56 → 1916.20] that are on your,
[1916.64 → 1917.06] uh,
[1917.06 → 1917.78] that are on the site?
[1917.84 → 1921.56] Do you go out and ask people to write reviews or are these,
[1922.06 → 1923.38] have these been just submitted at,
[1923.50 → 1923.86] uh,
[1923.88 → 1925.58] the will of the readers?
[1926.82 → 1927.18] Um,
[1927.18 → 1929.16] some of them we've asked.
[1929.16 → 1929.64] So,
[1929.64 → 1930.16] uh,
[1930.16 → 1930.92] daily JS,
[1931.08 → 1931.62] info queue,
[1932.28 → 1933.28] a few reviews.
[1933.36 → 1933.44] Yeah.
[1933.50 → 1933.64] We,
[1933.70 → 1935.52] we asked because obviously before you launched,
[1935.60 → 1936.30] nobody knows you.
[1936.44 → 1936.62] So,
[1936.62 → 1937.30] you know,
[1937.30 → 1939.60] people are not going to come out of the blue and review your book.
[1940.50 → 1940.86] Uh,
[1940.86 → 1942.38] but other than that,
[1942.44 → 1942.68] uh,
[1942.68 → 1943.00] it's,
[1943.08 → 1943.30] uh,
[1943.30 → 1945.02] people just have been reviewing the book.
[1945.18 → 1945.34] We,
[1946.24 → 1946.64] like some,
[1946.78 → 1948.88] some of the reviews are actual reviews.
[1948.94 → 1950.10] People did on their blogs,
[1950.20 → 1950.98] some more quotes,
[1950.98 → 1952.60] and we also have a lot of tweets.
[1953.28 → 1953.94] So the
[1953.94 → 1954.84] the tweets are all,
[1954.92 → 1955.38] uh,
[1955.56 → 1956.00] spontaneous.
[1956.00 → 1957.06] We don't plant,
[1957.06 → 1958.02] uh,
[1958.02 → 1958.56] fake tweets.
[1958.56 → 1962.42] So I'm going to butcher his name because I've never actually known how to say it,
[1962.50 → 1963.00] but the
[1963.00 → 1963.32] uh,
[1963.32 → 1965.76] founder of meteors and Matt Deferrals,
[1965.96 → 1966.70] Deferrals.
[1966.90 → 1967.54] How do you say that?
[1968.42 → 1968.86] Deferrals?
[1969.30 → 1969.82] Deferrals.
[1969.94 → 1972.18] So he wrote a review for you, and it seems like,
[1972.18 → 1972.64] uh,
[1972.64 → 1979.16] that would be a good thing that maybe the meteor community itself or the meteor team are embracing this.
[1979.18 → 1979.74] So what is it?
[1980.02 → 1982.30] What kind of response have you gotten from them for writing this?
[1983.30 → 1983.94] Oh yeah.
[1984.00 → 1984.14] We,
[1984.20 → 1985.88] we've gotten a great response.
[1986.22 → 1986.60] Um,
[1987.66 → 1987.92] I mean,
[1987.92 → 1988.52] first,
[1988.58 → 1988.86] uh,
[1988.86 → 1989.08] we,
[1989.30 → 1991.24] we released the book in San Francisco,
[1991.24 → 1992.50] uh,
[1992.54 → 1994.40] at the release party and like,
[1994.42 → 1997.72] I think over 120 people from the local community came.
[1998.92 → 1999.40] So,
[1999.40 → 2000.38] I mean,
[2000.38 → 2001.34] that was our first,
[2001.40 → 2001.76] uh,
[2002.18 → 2002.64] uh,
[2002.64 → 2006.90] indicator that people in the meteor community were really looking forward to the book.
[2007.74 → 2008.52] And yeah,
[2008.52 → 2008.80] I mean,
[2008.80 → 2011.62] all the feedback we got from them was perfect.
[2011.62 → 2012.98] And even like,
[2013.48 → 2013.74] well,
[2013.90 → 2015.66] actually the feedback we got the most was,
[2016.12 → 2016.16] Oh,
[2016.18 → 2017.64] I wish I had this six months ago.
[2019.12 → 2019.52] Yeah.
[2019.92 → 2020.48] That bad.
[2021.34 → 2021.88] I mean,
[2021.90 → 2022.24] it's,
[2022.34 → 2022.50] well,
[2022.50 → 2022.70] it's,
[2022.70 → 2023.62] it's starting at the
[2024.14 → 2027.10] I think what is probably the easiest way to learn anything,
[2027.16 → 2027.30] right?
[2027.34 → 2027.58] Is,
[2027.62 → 2028.42] is by doing,
[2028.54 → 2028.80] you know,
[2028.80 → 2030.62] and you've got the screencast to go with it.
[2030.66 → 2031.26] And I guess,
[2031.30 → 2033.96] depending upon the package actually get when you get the book,
[2033.96 → 2035.08] but I mean,
[2035.08 → 2037.36] you can start the bite off as much as you like.
[2038.16 → 2038.48] Um,
[2038.48 → 2040.24] but it is learned by doing,
[2040.38 → 2040.74] which is,
[2041.08 → 2042.16] has been said many,
[2042.26 → 2042.70] many times.
[2042.70 → 2044.90] And that's the best way I know how to learn.
[2045.04 → 2045.30] I mean,
[2045.30 → 2046.72] that's how I learned for myself even,
[2046.82 → 2047.20] of course.
[2048.20 → 2050.46] So actually maybe I can talk about that a little.
[2050.62 → 2050.80] Yeah.
[2050.80 → 2051.24] Uh,
[2051.24 → 2053.82] this inspiration for the book structure was the
[2053.82 → 2056.34] the rails tutorial by Michael Hart.
[2056.66 → 2057.00] Hart.
[2057.10 → 2057.24] Yeah.
[2058.00 → 2059.04] And that's how I learned,
[2059.04 → 2059.30] uh,
[2059.30 → 2059.72] to,
[2059.90 → 2060.86] to code in rails.
[2062.06 → 2062.46] And,
[2062.58 → 2062.84] um,
[2062.86 → 2063.10] yeah,
[2063.26 → 2065.36] what I really liked with that book is that you were,
[2065.36 → 2065.60] uh,
[2065.60 → 2066.02] buildings,
[2066.26 → 2067.54] an actual real thing.
[2067.64 → 2068.56] It wasn't just theory.
[2068.66 → 2069.32] It wasn't just,
[2069.32 → 2070.06] uh,
[2070.06 → 2070.40] syntax.
[2070.40 → 2071.12] It was,
[2071.12 → 2071.86] uh,
[2071.86 → 2073.14] getting something out the door.
[2073.84 → 2076.70] I think what you were building with real tutorial was like a
[2076.70 → 2077.48] a Twitter clone.
[2077.60 → 2077.94] Is that right?
[2078.54 → 2078.70] Yeah.
[2078.70 → 2080.36] So what was it that,
[2080.36 → 2081.34] I can't,
[2081.40 → 2082.44] and you may have already said this,
[2082.54 → 2085.44] but telescope is,
[2085.78 → 2088.00] let me make sure I have this right.
[2088.16 → 2089.66] Telescope is kind of the
[2089.72 → 2091.66] the social news app part.
[2091.66 → 2094.20] And then you're actually using telescope for sidebar.
[2094.28 → 2094.78] Is that right?
[2095.34 → 2095.54] Yeah.
[2095.78 → 2096.92] So which part of,
[2097.04 → 2098.84] in the process of this creation of this,
[2098.96 → 2099.24] you know,
[2099.24 → 2099.98] set of tools,
[2099.98 → 2103.38] did you decide this is what makes sense to do for the book?
[2106.26 → 2106.70] Well,
[2107.00 → 2108.70] first,
[2108.84 → 2109.44] like we,
[2109.44 → 2111.52] we knew we wanted to reuse the
[2111.52 → 2113.56] the idea of telescope because it's,
[2113.66 → 2113.86] uh,
[2114.60 → 2117.58] it's this way it's in the continuity of what we were doing.
[2117.58 → 2120.30] And also people can maybe transition from,
[2120.30 → 2121.10] you know,
[2121.18 → 2123.58] microscope to telescope if they want to contribute,
[2123.58 → 2124.44] uh,
[2124.44 → 2125.56] to the open source project.
[2125.56 → 2128.14] So it was just all tied in,
[2128.26 → 2129.52] into a single,
[2129.52 → 2129.90] uh,
[2130.62 → 2131.40] app idea,
[2131.56 → 2132.00] I guess.
[2132.00 → 2133.64] but also like,
[2133.74 → 2135.02] it's actually a pretty good,
[2135.08 → 2135.42] uh,
[2136.18 → 2140.02] pretty good concept just to learn a language because you got user accounts,
[2140.14 → 2140.54] you have,
[2140.62 → 2140.72] uh,
[2140.72 → 2141.22] comments,
[2142.10 → 2142.62] um,
[2142.86 → 2144.20] and you also have,
[2144.34 → 2144.52] uh,
[2144.94 → 2146.66] a bit of the real time aspect with,
[2146.66 → 2146.86] uh,
[2146.86 → 2147.64] real time voting.
[2148.60 → 2150.74] So it just made sense to,
[2150.82 → 2151.88] to keep,
[2151.92 → 2152.04] uh,
[2152.04 → 2153.02] working on the same,
[2153.02 → 2153.28] uh,
[2153.40 → 2155.06] hacker news clone idea for the book.
[2155.86 → 2156.72] Have you actually,
[2157.04 → 2158.20] you said that it would,
[2158.30 → 2162.16] it would almost be able to encourage somebody moving and actually contributing to telescope.
[2162.16 → 2166.00] Have you noticed an increase in popularity in telescope since this?
[2167.96 → 2168.84] Not really,
[2168.84 → 2170.16] because I think at this point,
[2170.28 → 2170.50] you know,
[2170.54 → 2172.68] people who already knew telescope,
[2173.18 → 2173.56] um,
[2174.60 → 2174.88] I mean,
[2174.92 → 2182.94] or rather experienced meteor coders already knew telescope and new meteor coders are maybe not at the point where they would feel comfortable contributing yet.
[2182.94 → 2184.78] But in the long-term,
[2184.90 → 2187.20] I definitely expect it to help a telescope.
[2187.44 → 2187.52] Yeah.
[2189.28 → 2189.68] Gotcha.
[2189.80 → 2191.34] So telescope itself has,
[2191.52 → 2192.36] uh,
[2192.52 → 2192.84] you know,
[2192.90 → 2194.94] almost a thousand stars and 250 forks.
[2195.56 → 2196.28] So it seems like it,
[2196.28 → 2199.12] it in and of itself is a pretty popular project that you're working on.
[2200.22 → 2200.62] Yeah.
[2200.72 → 2203.10] And I just wish I had more time to work on it,
[2203.20 → 2204.20] but it's,
[2204.38 → 2204.54] yeah,
[2204.62 → 2205.42] it's pretty popular.
[2205.94 → 2207.96] So it's still fairly young.
[2208.06 → 2209.68] So I don't know how many of those,
[2209.70 → 2210.20] you know,
[2210.20 → 2213.52] forks are actually being used in production somewhere,
[2213.52 → 2213.86] but,
[2213.98 → 2215.10] uh,
[2215.24 → 2215.62] yeah,
[2215.62 → 2217.82] it's definitely amazing to see all the interest and,
[2217.98 → 2220.12] and what people are doing with it.
[2220.58 → 2223.06] So you say telescope is in beta.
[2223.42 → 2223.78] What,
[2223.84 → 2225.18] what makes it in beta and,
[2225.18 → 2227.08] and what's kind of the goal to get it out of beta?
[2229.00 → 2229.40] Um,
[2230.04 → 2230.62] so there,
[2230.84 → 2233.42] there are a few features that I'd like to add,
[2233.42 → 2234.38] um,
[2234.46 → 2236.06] like a search and,
[2236.06 → 2238.66] and also just,
[2238.66 → 2238.90] uh,
[2238.90 → 2240.70] cleaning up a lot of the code.
[2240.78 → 2241.20] Well,
[2241.24 → 2241.66] for example,
[2241.66 → 2242.26] uh,
[2242.26 → 2242.94] we learned a lot,
[2243.02 → 2243.18] uh,
[2243.18 → 2244.36] writing the book and,
[2244.96 → 2245.22] you know,
[2245.22 → 2249.24] we had to really think hard about which patterns are best to,
[2249.38 → 2250.08] to build microscope.
[2250.08 → 2254.44] So I would like to re-inject those patterns into telescope to make sure both,
[2254.44 → 2254.68] uh,
[2254.68 → 2255.40] code bases are,
[2255.40 → 2256.06] uh,
[2256.06 → 2256.48] coherent.
[2256.84 → 2259.84] So ideally telescope would be just like a bigger,
[2259.96 → 2261.42] more complex version of microscope,
[2261.42 → 2261.82] but,
[2261.90 → 2262.76] um,
[2262.76 → 2264.84] with all the same things in the same places.
[2264.84 → 2267.10] So that's something I need to do.
[2267.16 → 2267.78] And also just,
[2267.78 → 2269.08] uh,
[2269.08 → 2271.34] there are quite a few bugs to fix and,
[2271.34 → 2271.76] you know,
[2271.76 → 2273.42] things that work,
[2273.54 → 2274.86] but not as well as they should.
[2275.48 → 2276.76] So it's more of a general,
[2276.76 → 2277.26] um,
[2277.60 → 2277.84] yeah,
[2278.16 → 2279.52] polishing up of the project.
[2280.34 → 2282.64] With all these different projects that you got going on,
[2282.68 → 2285.72] where do you find yourself spending the majority of your time?
[2287.52 → 2288.84] So for the past month,
[2288.84 → 2290.24] it was definitely the book.
[2291.00 → 2291.40] Uh,
[2291.40 → 2293.50] I had a very bad habit in the past,
[2293.50 → 2294.94] or I guess I still do,
[2295.02 → 2296.82] but I'm trying to improve it is,
[2296.92 → 2297.66] uh,
[2297.66 → 2301.76] just being too unfocused and jumping from project to project.
[2303.08 → 2305.14] So it has some good sides,
[2305.14 → 2306.50] like some good points because,
[2307.52 → 2307.82] uh,
[2307.86 → 2308.34] first,
[2308.42 → 2308.56] well,
[2308.56 → 2310.72] it's fun to do, and you get to,
[2310.72 → 2311.62] uh,
[2311.62 → 2313.06] meet a lot of people and,
[2313.06 → 2315.36] and learn a lot of new things.
[2315.36 → 2316.72] But in the end,
[2316.72 → 2318.76] I feel like if you really want to achieve something,
[2318.76 → 2320.56] you need to focus all your energy on,
[2320.56 → 2321.38] on one project.
[2321.58 → 2323.34] So for the past month,
[2323.44 → 2323.84] I put,
[2323.92 → 2324.22] uh,
[2324.70 → 2325.72] sidebar on hold.
[2326.00 → 2327.72] Like I didn't add new features to it.
[2327.80 → 2329.02] I put telescope on hold,
[2329.02 → 2330.04] uh,
[2330.04 → 2333.34] same with folio and all my other projects and just focused on the book.
[2335.52 → 2336.52] Speaking of folio,
[2336.64 → 2338.00] I exchanged a tweet with you,
[2338.00 → 2338.50] uh,
[2338.50 → 2341.12] thinking of deep parts of last night as I was trickling away to bed,
[2341.12 → 2342.74] but I was kind of,
[2342.74 → 2343.96] just kind of laughing,
[2343.96 → 2344.44] I guess,
[2344.66 → 2345.86] happily,
[2345.86 → 2346.30] I guess,
[2346.30 → 2346.70] uh,
[2346.70 → 2349.04] as a friend might do to another friend,
[2349.04 → 2350.06] but you were like,
[2350.60 → 2352.36] I guess you didn't introduce folio,
[2352.48 → 2359.92] but folio is this community where designers can submit themselves and people who would like to work with freelance designers can come and request,
[2359.92 → 2360.44] uh,
[2360.44 → 2362.16] projects and mention projects.
[2362.16 → 2363.16] And it kind of goes out to this,
[2363.16 → 2364.14] um,
[2364.70 → 2365.10] I,
[2365.10 → 2365.98] I guess,
[2366.06 → 2366.44] uh,
[2366.74 → 2369.54] curated list of available designers based on you.
[2369.56 → 2370.26] And you've got this,
[2370.26 → 2371.30] um,
[2371.38 → 2372.32] somewhat big,
[2372.32 → 2372.88] I guess,
[2372.94 → 2375.28] waiting list of people waiting to get into as designers,
[2375.28 → 2375.74] into,
[2375.74 → 2376.56] into folio.
[2378.00 → 2378.40] Yeah.
[2378.46 → 2380.56] So I used to have like,
[2380.66 → 2380.94] you know,
[2380.94 → 2382.44] maybe 10 people a week applying,
[2382.44 → 2383.94] so that was okay.
[2384.74 → 2385.18] But,
[2385.30 → 2386.12] you know,
[2386.18 → 2387.18] for some reason,
[2387.34 → 2388.68] maybe I got some links or whatever.
[2388.96 → 2393.70] Now I have a 250 people waiting list also because for the past,
[2393.76 → 2394.06] uh,
[2394.06 → 2394.62] like I said,
[2395.32 → 2396.16] three or four months,
[2396.16 → 2399.54] I was just focused on the book and didn't check that,
[2399.60 → 2399.86] uh,
[2399.86 → 2400.60] waiting list too much.
[2400.60 → 2404.90] So now I have people who have been waiting for like two months to have their account approved.
[2404.90 → 2406.44] My new response back to me was,
[2406.56 → 2406.70] yeah,
[2406.72 → 2408.72] sometimes I wish the site was less popular.
[2409.42 → 2409.82] Yeah.
[2411.76 → 2412.12] Yeah.
[2412.18 → 2413.34] I really do sometimes.
[2413.56 → 2413.66] Well,
[2413.76 → 2415.22] maybe,
[2415.38 → 2415.82] you know,
[2416.22 → 2416.66] that's,
[2416.72 → 2418.12] I guess it's kind of like the
[2418.12 → 2423.40] the fun part of success sometimes is once you get so far and that kind of goes back to what Andrew mentioned is,
[2423.78 → 2425.82] is how do you decide on what to spend your time on?
[2425.86 → 2426.16] Is it,
[2426.76 → 2429.46] this kind of even trickles into the blog post you mentioned too,
[2429.46 → 2429.76] which,
[2429.76 → 2430.20] uh,
[2430.20 → 2431.62] or I mentioned earlier that you wrote,
[2431.62 → 2432.36] uh,
[2432.36 → 2433.32] about the pricing trilogy,
[2433.32 → 2435.58] which was if you're trying to maximize revenue,
[2435.58 → 2436.22] that was a
[2436.22 → 2437.38] a different case here,
[2437.38 → 2438.00] but are you,
[2438.22 → 2440.54] are you motivated by community involvement?
[2440.54 → 2441.80] Are you motivated by,
[2441.80 → 2442.60] uh,
[2442.64 → 2442.94] you know,
[2443.06 → 2444.76] pursuing your interests or is it,
[2445.04 → 2446.66] what is it that kind of drives you?
[2446.68 → 2447.64] Is it monetary?
[2447.98 → 2449.10] Are you monetarily driven?
[2451.36 → 2451.80] Um,
[2451.84 → 2452.82] I'm pretty sure I'm not,
[2452.82 → 2453.22] uh,
[2453.22 → 2455.12] monetarily driven because if I am,
[2455.12 → 2456.66] I'm doing a pretty bad job at it.
[2457.66 → 2458.10] Um,
[2458.26 → 2460.28] but yeah,
[2460.28 → 2461.36] I would say it's my interest.
[2461.78 → 2462.06] Um,
[2462.92 → 2466.90] it's very easy for me to get interested in a new thing and have new ideas.
[2467.10 → 2467.26] So,
[2468.02 → 2468.44] um,
[2468.52 → 2468.70] yeah,
[2468.70 → 2470.14] usually I,
[2470.46 → 2470.96] you know,
[2470.98 → 2475.74] I get this idea, and then I will start working on it and maybe,
[2475.74 → 2476.20] you know,
[2476.20 → 2478.24] do a Photoshop mockup and then say,
[2478.28 → 2478.36] Hey,
[2478.36 → 2479.00] that's pretty cool.
[2479.00 → 2479.26] And,
[2479.74 → 2479.82] you know,
[2479.82 → 2480.38] just do it.
[2480.88 → 2481.82] Or at least like,
[2482.14 → 2482.38] I mean,
[2482.38 → 2482.58] that's,
[2482.64 → 2483.58] I think that's really important.
[2483.66 → 2485.10] It's really important to be able to do that,
[2485.18 → 2486.44] but you also need to limit yourself,
[2486.50 → 2486.94] like I said.
[2487.10 → 2488.44] So yeah,
[2488.44 → 2490.38] it's hard to find the right balance between,
[2490.38 → 2491.96] you know,
[2492.00 → 2492.38] uh,
[2492.50 → 2495.16] never doing anything else besides your,
[2495.16 → 2495.36] uh,
[2495.36 → 2499.88] nine to five and then launching a new thing every week because it's just so
[2499.88 → 2500.14] fun.
[2500.36 → 2500.50] Right.
[2500.90 → 2503.94] So we talk about a topic we like to talk about a lot on the show is,
[2503.94 → 2504.34] uh,
[2504.68 → 2504.92] you know,
[2504.94 → 2506.06] open source sustainability.
[2506.06 → 2506.64] Right.
[2506.94 → 2507.32] And,
[2507.32 → 2508.04] uh,
[2508.04 → 2508.66] with telescope,
[2508.66 → 2509.62] you have it,
[2509.86 → 2510.18] you know,
[2510.18 → 2512.60] it's obviously an open source project that codes on GitHub.
[2512.92 → 2513.40] Uh,
[2513.40 → 2514.52] when you froze,
[2514.52 → 2515.56] to write this book,
[2515.62 → 2516.04] you said you,
[2516.12 → 2518.08] you froze development on telescope.
[2518.20 → 2519.00] Did you actually,
[2519.42 → 2519.74] you know,
[2520.06 → 2523.08] like make an announcement that you were not going to develop on telescope?
[2523.08 → 2527.84] Did you actually freeze development or was the community still working on it behind you?
[2527.84 → 2529.30] No,
[2529.38 → 2529.52] I,
[2529.62 → 2530.68] the community is still working.
[2530.84 → 2532.72] I didn't do any official announcement.
[2533.60 → 2534.00] Uh,
[2534.00 → 2534.72] it's more than,
[2534.86 → 2535.04] you know,
[2535.04 → 2537.46] before I would respond to pull requests or bug,
[2537.46 → 2540.06] bug reports in like a couple of hours.
[2540.06 → 2540.96] And now it's like,
[2540.96 → 2542.28] uh,
[2542.28 → 2542.84] a week or,
[2543.64 → 2544.36] or,
[2544.48 → 2544.68] uh,
[2544.68 → 2544.94] yeah,
[2545.14 → 2545.62] soon.
[2546.02 → 2546.10] Yeah.
[2546.34 → 2546.70] Yeah.
[2546.70 → 2547.72] I did want to mention too,
[2547.80 → 2550.72] that you've been very responsive, and you said,
[2550.78 → 2551.72] so you're in Japan.
[2551.86 → 2553.24] So you're in Japan time right now.
[2553.24 → 2555.46] Is it 739 AM there?
[2555.96 → 2556.12] Yeah,
[2556.20 → 2556.52] it is.
[2556.78 → 2557.60] And it's almost,
[2557.72 → 2559.28] it's 539 PM here.
[2559.40 → 2560.16] It's impressive.
[2560.32 → 2560.44] Has,
[2560.52 → 2561.56] has there been any,
[2562.04 → 2562.46] um,
[2562.76 → 2563.02] you know,
[2563.04 → 2563.30] I don't,
[2563.52 → 2566.56] I don't want to say that most developers are in the U S because I,
[2566.62 → 2568.22] I don't think that's necessarily true,
[2568.22 → 2571.36] but I would think that a lot of the people who are working on,
[2571.36 → 2572.04] um,
[2572.10 → 2572.34] you know,
[2572.40 → 2574.06] telescope and working with you and,
[2574.14 → 2574.78] and want to,
[2574.98 → 2575.30] you know,
[2575.36 → 2577.38] maybe talk to you about the projects you're working on.
[2577.38 → 2578.74] Have you noticed any kind of like,
[2578.82 → 2579.10] uh,
[2579.38 → 2579.70] you know,
[2579.98 → 2582.36] a barrier with time being a problem at all?
[2583.52 → 2584.20] Not really.
[2584.28 → 2585.52] It's usually okay because the
[2585.52 → 2587.28] the time difference is big enough that,
[2587.48 → 2587.70] uh,
[2588.42 → 2589.96] when it's morning for me,
[2590.02 → 2590.82] it's still day,
[2590.94 → 2591.40] uh,
[2591.68 → 2596.36] on the West coast and like early evening on the East coast.
[2596.36 → 2597.82] So I can always find the time.
[2598.76 → 2600.00] And like in,
[2600.02 → 2601.28] in a weird coincidence,
[2601.62 → 2601.84] uh,
[2602.02 → 2603.32] Tom is in Melbourne,
[2603.50 → 2603.80] Australia.
[2603.80 → 2604.64] So we're actually,
[2604.86 → 2605.50] uh,
[2605.50 → 2607.10] we only have one hour of time difference.
[2607.10 → 2608.16] Which is very convenient.
[2608.54 → 2608.74] Yeah.
[2608.98 → 2609.24] Yeah.
[2609.68 → 2610.40] So to,
[2610.62 → 2613.24] to kind of get back to what I wanted to ask before with open source
[2613.24 → 2613.80] sustainability,
[2613.80 → 2614.66] uh,
[2614.66 → 2614.82] to,
[2614.90 → 2616.24] to do a project like telescope,
[2616.24 → 2617.98] which I think is a very,
[2618.48 → 2618.90] um,
[2619.16 → 2619.54] I don't know.
[2619.84 → 2621.16] I don't have the word for it,
[2621.16 → 2621.62] but it's a
[2621.68 → 2622.58] it's a big project,
[2622.58 → 2622.88] right?
[2622.88 → 2623.60] It's something that,
[2623.60 → 2624.14] and it,
[2624.50 → 2625.92] and it's almost limitless,
[2625.98 → 2626.10] right?
[2626.10 → 2627.52] How big this project can get.
[2628.00 → 2628.32] Um,
[2628.80 → 2631.56] have you experienced any kind of like burnout with working on this?
[2631.62 → 2631.94] You said,
[2632.06 → 2632.78] you said that you,
[2632.88 → 2633.92] you'd like to start things,
[2633.92 → 2636.54] but sometimes maybe have a problem finishing them.
[2636.54 → 2637.38] Um,
[2638.14 → 2638.34] no,
[2638.38 → 2639.16] I don't know if you said that.
[2639.18 → 2640.24] I don't want to put words in your mouth,
[2640.24 → 2641.76] but have you noticed with telescope,
[2641.76 → 2642.04] like,
[2642.10 → 2642.90] have you gotten any,
[2643.02 → 2644.68] have you gotten tired of working on it at all?
[2644.76 → 2646.00] Have you decided to like,
[2646.02 → 2646.24] you know,
[2646.24 → 2647.98] take a break from it just because of,
[2647.98 → 2648.30] you know,
[2648.30 → 2648.56] the
[2648.56 → 2651.76] the everyday answering pull requests and stuff has gotten old to you at
[2651.76 → 2651.90] all?
[2651.90 → 2653.82] Well,
[2653.82 → 2655.78] I think that's definitely a risk,
[2655.78 → 2657.50] but it hasn't happened to me.
[2657.74 → 2660.62] And I think that's because I'm using telescope for sidebar.
[2660.86 → 2663.38] So basically every time I want to improve sidebar,
[2663.54 → 2665.60] I have to improve telescope first.
[2666.72 → 2667.42] So I,
[2667.42 → 2668.70] I think that was a pretty,
[2668.90 → 2669.06] like,
[2669.10 → 2671.48] I didn't really plan it out too much that way,
[2671.48 → 2672.44] but,
[2672.50 → 2672.64] uh,
[2672.64 → 2673.14] in retrospect,
[2673.14 → 2676.58] I think that was a good choice because otherwise it's true that I would,
[2676.58 → 2677.30] I would probably,
[2677.30 → 2677.70] um,
[2678.02 → 2682.76] have less motivation to work on telescope and risk burnout a lot more.
[2684.26 → 2684.66] Gotcha.
[2685.32 → 2687.48] I think sidebar is a really neat project.
[2687.48 → 2689.90] And I think just kind of to add to what you're talking about,
[2689.94 → 2690.10] Andrew,
[2690.18 → 2691.30] about sustaining open source.
[2691.38 → 2691.88] I think it's,
[2692.48 → 2693.32] you know,
[2693.32 → 2694.34] I think if it's a trend,
[2694.38 → 2696.88] if you go back and rewind through the past few shows,
[2696.88 → 2697.40] there's,
[2697.50 → 2697.80] um,
[2698.20 → 2699.86] when we talked about this is there's been,
[2699.86 → 2700.22] uh,
[2700.72 → 2701.08] you know,
[2701.08 → 2702.18] some sort of personal gain,
[2702.26 → 2702.94] whether it's,
[2702.94 → 2703.52] you know,
[2703.72 → 2705.20] forwarding interest or forwarding,
[2705.30 → 2706.00] you know,
[2706.08 → 2706.56] income,
[2706.58 → 2706.82] or,
[2706.82 → 2707.78] or whatever it might be.
[2707.78 → 2708.06] But,
[2708.18 → 2708.36] you know,
[2708.36 → 2708.58] in,
[2708.70 → 2709.64] in Sasha's case,
[2709.74 → 2712.08] sidebar is his motivation.
[2712.08 → 2713.98] And you do get some money from that.
[2714.02 → 2715.74] I believe you have sponsors, and you're still growing.
[2715.84 → 2716.54] So I'm sure you have,
[2716.66 → 2717.30] you know,
[2717.30 → 2719.14] some sort of plan in terms of how you'll make money from it,
[2719.16 → 2720.14] but that's,
[2720.20 → 2721.22] it's kind of neat how,
[2722.24 → 2722.86] like you said,
[2722.88 → 2726.88] it was sort of accidental in a case where you didn't really purposely set it up
[2726.88 → 2727.26] like that,
[2727.26 → 2729.76] but how it filters back into open source.
[2729.76 → 2730.74] And I think if we,
[2730.86 → 2733.60] if we look at the community and just kind of be more mindful of that,
[2733.68 → 2734.76] that as,
[2734.78 → 2734.98] uh,
[2734.98 → 2736.18] we see personal projects,
[2736.18 → 2741.54] spruce up like cyborg.io and what that could mean for a micro framework that
[2741.54 → 2742.30] pops out of this,
[2742.38 → 2742.74] you know,
[2742.86 → 2744.16] written in meteor in this case,
[2744.16 → 2744.96] uh,
[2744.96 → 2745.40] telescope.
[2745.52 → 2749.44] And then it's just really neat how open source becomes a bit easier to
[2749.44 → 2749.82] sustain.
[2749.82 → 2750.18] So,
[2750.18 → 2750.96] uh,
[2750.96 → 2753.24] there's a post on the change log ages ago that written,
[2753.24 → 2755.08] that when written about,
[2755.08 → 2755.48] you know,
[2755.48 → 2755.68] the
[2755.68 → 2758.50] the top 10 ways basically to get us to cover open source,
[2758.50 → 2760.46] or I can't remember exactly what the
[2760.74 → 2761.84] what the title was nowadays.
[2762.14 → 2762.56] Why I'm not,
[2762.68 → 2764.70] why I'm not using your open source product.
[2764.70 → 2764.86] Yeah,
[2764.86 → 2765.30] exactly.
[2765.30 → 2767.20] And we get people asking us all the time,
[2767.20 → 2767.46] like,
[2767.46 → 2768.84] you know,
[2768.84 → 2769.44] uh,
[2769.44 → 2771.82] just solving a problem in open source.
[2771.90 → 2772.60] It's the same as,
[2772.72 → 2772.90] you know,
[2772.94 → 2773.32] startups,
[2773.42 → 2773.66] I guess,
[2773.70 → 2774.06] in a sense,
[2774.12 → 2775.08] like if you're just trying to stop,
[2775.26 → 2775.70] uh,
[2776.12 → 2777.78] solve a startup problem,
[2777.84 → 2779.84] not so much solve your own problems,
[2779.84 → 2781.48] it's going to be kind of hard to sustain that,
[2782.02 → 2782.42] you know,
[2782.46 → 2783.48] but in your case,
[2783.48 → 2788.54] you've got a personal gain to it, and you started it and the community has
[2788.54 → 2790.66] adapted to it and has new it as well.
[2790.66 → 2791.80] So they're helping you push it forward.
[2791.90 → 2792.88] But every,
[2793.36 → 2793.98] as you'd mentioned,
[2794.04 → 2795.84] every new thing you want to add to sidebar,
[2795.84 → 2796.90] um,
[2796.96 → 2797.60] goes into,
[2797.60 → 2798.86] into telescope first.
[2800.22 → 2800.58] Yeah.
[2800.66 → 2802.24] And in the beginning I was really,
[2802.24 → 2802.92] you know,
[2802.94 → 2807.28] hoping telescope would get big and people would contribute, and I wouldn't
[2807.28 → 2808.56] have to code anymore on it.
[2808.56 → 2809.56] And nice.
[2810.50 → 2811.08] Has that,
[2811.18 → 2811.38] uh,
[2811.38 → 2812.00] has that happened?
[2812.68 → 2813.06] No,
[2813.12 → 2813.62] not at all.
[2813.68 → 2815.52] And so now I have more of a long-term view,
[2815.74 → 2816.08] you know,
[2816.48 → 2816.78] I mean,
[2816.78 → 2820.48] people say that it takes like three years to build a company to the point
[2820.48 → 2821.20] of profitability,
[2821.20 → 2821.92] I think.
[2822.78 → 2824.94] And I kind of have the same view for telescope.
[2825.30 → 2827.30] So I'm using it.
[2827.48 → 2827.84] Uh,
[2827.84 → 2829.08] if other people are using it,
[2829.10 → 2829.68] it's great.
[2829.78 → 2830.22] If not,
[2830.28 → 2830.98] it's no big deal.
[2831.06 → 2832.24] I'll just keep improving it.
[2832.28 → 2833.26] And hopefully one day,
[2833.34 → 2833.94] you know,
[2833.94 → 2835.12] it will get to the point where,
[2835.12 → 2835.44] uh,
[2835.66 → 2837.22] it doesn't make sense not to use it.
[2838.80 → 2839.88] So let me ask you a question.
[2840.20 → 2840.48] Um,
[2840.94 → 2842.38] when I kind of first,
[2842.66 → 2843.36] I don't know,
[2843.42 → 2843.56] this,
[2843.64 → 2845.24] this question has come up in a lot of different,
[2845.24 → 2845.64] uh,
[2845.64 → 2845.96] areas,
[2846.04 → 2846.82] not just with meteor.
[2847.18 → 2847.62] Um,
[2847.62 → 2849.86] but I think this is one that you've probably had to solve or,
[2850.02 → 2850.38] you know,
[2850.48 → 2851.20] uh,
[2851.66 → 2853.46] that you've had to leverage meteor to solve.
[2853.50 → 2854.60] And that's the idea of,
[2854.64 → 2854.78] you know,
[2854.84 → 2857.16] SEO and indexing your website and stuff like that.
[2857.56 → 2858.04] Um,
[2858.38 → 2859.64] how does meteor handle that?
[2859.68 → 2863.48] And have you actually had to kind of solve that problem for,
[2863.48 → 2863.96] uh,
[2863.96 → 2865.12] telescope and sidebar?
[2866.80 → 2867.24] So,
[2867.24 → 2867.76] um,
[2868.40 → 2872.02] meteor has a package called a spider rebel that does that.
[2872.28 → 2874.34] And it uses a phantom JS.
[2875.00 → 2876.24] So basically when,
[2876.34 → 2876.54] uh,
[2876.74 → 2877.02] you know,
[2877.02 → 2878.88] Googlebot fetches your site,
[2878.88 → 2879.88] um,
[2879.96 → 2882.84] it will run phantom JS and give the result to it.
[2883.50 → 2884.86] So it works pretty well.
[2885.18 → 2885.50] Um,
[2886.18 → 2889.40] I do have to confess that I have not,
[2889.50 → 2889.78] uh,
[2889.82 → 2892.00] actually activated the package on,
[2892.14 → 2892.50] um,
[2893.34 → 2896.38] on sidebar because I think I just moved servers and,
[2896.38 → 2896.70] um,
[2897.80 → 2900.22] installing phantom JS is kind of a pain.
[2900.22 → 2902.00] So,
[2902.00 → 2902.80] yeah,
[2902.80 → 2902.96] I mean,
[2902.96 → 2903.58] that's a downside.
[2903.74 → 2906.66] Obviously I'm looking forward to the day when meteor does real,
[2906.66 → 2907.14] uh,
[2907.14 → 2907.96] server side,
[2907.96 → 2909.02] um,
[2909.38 → 2910.20] content rendering.
[2911.58 → 2912.02] But,
[2912.02 → 2912.50] uh,
[2912.52 → 2913.08] until then,
[2913.12 → 2914.44] I guess it's a good enough,
[2914.44 → 2914.74] uh,
[2914.74 → 2915.12] fix.
[2916.50 → 2920.54] So meteor has kind of their own little hosting platform,
[2920.66 → 2920.74] right?
[2920.76 → 2922.92] You can deploy your apps to meteor servers.
[2923.78 → 2924.26] Um,
[2924.34 → 2928.64] but I imagine you're not doing that with sidebar since you just said you've,
[2928.70 → 2929.40] you've changed them.
[2929.40 → 2930.86] So at least you've moved off of it,
[2930.86 → 2931.08] but,
[2931.12 → 2931.58] uh,
[2931.58 → 2934.84] have you used the meteor servers, and what are you using for yours?
[2936.20 → 2936.94] So yeah,
[2936.98 → 2940.72] the meteor servers are very convenient because you can deploy with just one line
[2940.72 → 2941.92] of one command line,
[2941.92 → 2943.02] but yeah,
[2943.02 → 2943.40] it's,
[2943.40 → 2945.14] it's not meant for production use or,
[2945.36 → 2946.00] you know,
[2946.02 → 2946.98] any serious use.
[2947.14 → 2950.68] It's pretty slow and doesn't hold that well under traffic,
[2950.68 → 2951.88] but you know,
[2951.88 → 2952.12] you know,
[2952.14 → 2952.54] it's free,
[2952.64 → 2954.46] so you can't really complain.
[2955.32 → 2956.30] I guess for me,
[2956.30 → 2958.06] a better alternative is Heroku.
[2958.06 → 2963.84] So I've tested telescope on Heroku a lot and I think it went up to,
[2963.94 → 2964.24] uh,
[2964.76 → 2965.84] about 150,
[2965.84 → 2966.48] uh,
[2966.82 → 2967.92] concurrent connections,
[2967.92 → 2969.44] which,
[2969.62 → 2969.92] I mean,
[2969.94 → 2970.06] that,
[2970.16 → 2971.16] that was like on a free,
[2971.16 → 2971.40] uh,
[2971.40 → 2971.78] Heroku,
[2971.78 → 2972.46] uh,
[2972.46 → 2972.74] Dino.
[2972.94 → 2973.32] So again,
[2973.32 → 2974.04] it's not that bad.
[2974.04 → 2975.86] And for sidebar,
[2975.92 → 2977.14] I'm using a digital ocean,
[2977.14 → 2980.38] which is really cheap and really,
[2980.38 → 2981.14] really fast.
[2981.36 → 2982.92] So I really recommend them.
[2983.66 → 2985.18] And for the
[2985.18 → 2986.46] the meteor books,
[2986.56 → 2986.88] uh,
[2986.88 → 2987.04] I mean,
[2987.10 → 2988.54] discover meteor app,
[2988.66 → 2990.10] we're using,
[2990.10 → 2990.40] uh,
[2990.42 → 2990.86] EC2.
[2990.86 → 2994.46] So the
[2994.46 → 2996.46] the book itself,
[2996.46 → 2997.64] and to go back to your book,
[2997.70 → 2998.34] discover meteor,
[2998.58 → 2999.76] I forgot to ask you earlier,
[2999.76 → 3000.14] the
[3000.28 → 3003.68] the art on the website is a beautiful book.
[3003.72 → 3004.08] It's a
[3004.08 → 3004.84] you know,
[3004.84 → 3005.48] pretty popular,
[3005.48 → 3006.64] uh,
[3006.72 → 3008.44] style for your e-books,
[3008.44 → 3010.78] but that leads me to the question.
[3010.78 → 3013.02] Is there ever going to be a print version of this book available?
[3015.08 → 3015.48] Yeah.
[3015.48 → 3015.60] I,
[3015.76 → 3015.92] you know,
[3015.94 → 3016.62] I really don't know.
[3016.90 → 3017.04] Um,
[3017.70 → 3022.52] what we've been saying is that we'll consider that once a meteor stabilizes at 1.0,
[3022.64 → 3026.28] because until then it doesn't really make sense to come out with a book.
[3026.28 → 3028.30] If the framework itself is going to change,
[3028.30 → 3029.12] you know,
[3029.16 → 3029.92] next week.
[3030.00 → 3030.24] Yeah.
[3031.36 → 3031.80] And,
[3031.90 → 3032.06] uh,
[3032.06 → 3032.82] so obviously we're,
[3032.90 → 3034.64] we're going to keep the online version,
[3034.78 → 3035.08] PDF,
[3035.42 → 3035.74] EPUB,
[3035.80 → 3036.14] all that,
[3036.34 → 3036.62] uh,
[3036.62 → 3037.94] up to date with,
[3037.94 → 3038.30] uh,
[3038.30 → 3038.44] the
[3038.44 → 3039.82] the changes of a meteor.
[3040.58 → 3041.58] But after that,
[3041.64 → 3041.90] maybe,
[3042.22 → 3042.50] uh,
[3042.50 → 3042.96] who knows?
[3043.74 → 3044.82] I will say though,
[3044.82 → 3045.70] that personally,
[3045.70 → 3051.72] I don't think like I wouldn't use a paper version of the book because I think it's,
[3051.72 → 3052.00] uh,
[3052.56 → 3055.02] inferior to the digital version.
[3056.28 → 3056.80] Uh,
[3056.80 → 3057.20] first,
[3057.20 → 3058.36] we were talking like about the
[3058.72 → 3059.00] you know,
[3059.00 → 3059.74] using the
[3059.78 → 3061.32] the app of the book,
[3061.32 → 3061.72] uh,
[3061.72 → 3064.74] in a more interactive way with annotations and stuff.
[3064.92 → 3065.06] So,
[3065.06 → 3066.46] um,
[3066.80 → 3067.28] even,
[3067.58 → 3068.92] even now,
[3068.98 → 3069.36] for example,
[3069.36 → 3071.28] we have links to a code commits.
[3071.70 → 3072.62] So every,
[3073.00 → 3074.80] like maybe two or three times,
[3074.82 → 3075.54] times per chapter,
[3075.54 → 3076.84] we have a code commits,
[3076.84 → 3077.60] uh,
[3077.64 → 3079.00] of the app at that stage.
[3079.00 → 3081.70] And we also link that commit to a live instance,
[3081.70 → 3082.92] uh,
[3082.96 → 3083.60] of the app.
[3084.04 → 3088.42] So those are things that would obviously not be as easy to do with a physical book.
[3088.88 → 3091.66] I don't think meteor handles the physical book part yet.
[3091.82 → 3092.04] Yeah.
[3093.10 → 3093.54] Yeah.
[3094.28 → 3096.02] It wouldn't be a real time and reactive.
[3096.02 → 3097.02] Um,
[3098.24 → 3098.56] so,
[3098.56 → 3099.46] uh,
[3099.46 → 3103.90] I want to give a shout-out to a project that I actually covered on the change like a while
[3103.90 → 3104.24] back.
[3104.24 → 3105.44] And I don't know if you've ever heard of it.
[3105.48 → 3105.62] It's,
[3105.68 → 3105.84] uh,
[3105.84 → 3107.30] just a meteor dot sh.
[3107.30 → 3107.90] Have you,
[3108.00 → 3108.84] have you heard of it?
[3110.12 → 3111.02] Meteor dot sh?
[3111.12 → 3113.72] Is it meteoric dot sh or me?
[3114.00 → 3114.40] No,
[3114.50 → 3115.36] meteor dot sh.
[3115.36 → 3115.72] Yeah.
[3116.00 → 3120.20] So it's a little shell script that you can actually set up a meteor server and deploy
[3120.20 → 3121.18] meteor apps to it.
[3121.26 → 3121.84] And it's,
[3122.02 → 3124.12] it's kind of shocking how easy it is to,
[3124.20 → 3126.84] to set up a meteor server and actually deploy your code to it.
[3127.22 → 3127.54] Um,
[3128.18 → 3129.86] it's a little shell script that you can check out.
[3129.92 → 3130.30] There's a
[3130.38 → 3130.80] we'll put the
[3130.80 → 3131.08] the
[3131.14 → 3131.42] uh,
[3131.42 → 3134.62] link to the repo in the show notes,
[3134.62 → 3134.90] but,
[3135.02 → 3135.18] uh,
[3135.18 → 3136.72] that was one of my first,
[3136.72 → 3137.60] uh,
[3137.60 → 3138.62] kind of,
[3138.98 → 3143.48] I don't know if the exposure or experience is the right word.
[3143.48 → 3143.72] But,
[3144.04 → 3144.20] uh,
[3144.20 → 3145.64] when I saw the meteor dot sh,
[3145.72 → 3146.80] I think that's when I decided,
[3146.94 → 3147.26] you know what,
[3147.26 → 3148.64] this is something that actually,
[3148.64 → 3149.12] uh,
[3149.18 → 3151.30] has a shot to take off and go somewhere because,
[3151.30 → 3152.14] um,
[3152.20 → 3152.78] before that,
[3152.82 → 3153.00] you know,
[3153.04 → 3153.20] you,
[3153.34 → 3153.70] I don't know,
[3153.70 → 3157.14] you hear about a lot of stuff, and it seems like meteor is one of the ones that is just
[3157.14 → 3158.94] blowing up in popularity and growing.
[3159.60 → 3159.84] Um,
[3160.56 → 3162.08] but no matter how much it grows,
[3162.20 → 3164.20] I think one of my biggest pet peeves,
[3164.80 → 3164.96] and,
[3165.10 → 3165.40] uh,
[3165.50 → 3166.00] let me know how,
[3166.10 → 3167.30] what you think about this.
[3167.60 → 3170.54] Why is the mailing list email still so ugly?
[3172.60 → 3173.54] Do you mean the
[3173.54 → 3173.78] um,
[3174.72 → 3174.98] the
[3175.22 → 3177.58] the Google Groups email or the
[3177.74 → 3177.96] no,
[3178.04 → 3178.12] no,
[3178.12 → 3178.80] the actual,
[3178.80 → 3179.32] uh,
[3179.32 → 3181.96] like updates that come out from the team.
[3181.96 → 3184.00] They're just the text, and it's so bad.
[3185.82 → 3186.26] Yeah,
[3186.26 → 3186.74] I don't know.
[3186.92 → 3187.20] Um,
[3187.20 → 3188.46] I don't think they have a
[3189.14 → 3189.38] well,
[3189.60 → 3190.48] I'm not sure.
[3190.52 → 3193.88] I don't think they have a designer like working on their stuff too much.
[3193.88 → 3194.16] So,
[3194.16 → 3194.94] yeah,
[3194.94 → 3196.44] I'm trying to tell you that you should,
[3196.56 → 3196.84] uh,
[3196.84 → 3199.16] you should get involved and help out with that.
[3200.08 → 3200.48] Yeah,
[3200.48 → 3201.46] if I had more time,
[3201.54 → 3202.04] one more time.
[3202.78 → 3204.54] Just another thing to work on.
[3206.34 → 3206.74] So,
[3206.94 → 3208.90] for those of you that have kind of,
[3208.98 → 3209.64] uh,
[3209.64 → 3210.76] listened to the show and,
[3210.76 → 3211.62] and newcomers alike,
[3211.66 → 3212.46] we kind of ask the
[3212.72 → 3214.60] the two questions at the end of every episode.
[3214.60 → 3215.60] Um,
[3215.60 → 3217.78] the first one is for a call to arms.
[3218.16 → 3218.56] So,
[3218.56 → 3220.56] with the book Discover Meteor,
[3220.56 → 3223.78] you might not have necessarily a call to arms as far as,
[3223.90 → 3224.06] I guess,
[3224.10 → 3225.78] you would like for people to just buy the book.
[3225.88 → 3227.16] That could be your call to arms for that.
[3227.72 → 3228.08] Um,
[3228.14 → 3229.22] but what about with telescope?
[3229.46 → 3229.62] Like,
[3229.72 → 3229.90] what,
[3229.90 → 3230.68] what are some,
[3230.68 → 3231.42] uh,
[3231.42 → 3232.58] features or just,
[3232.70 → 3236.60] what would you like to see the community kind of rally around and do for the project telescope?
[3236.60 → 3236.76] Oh,
[3237.76 → 3239.78] that's a great question.
[3241.16 → 3241.60] So,
[3241.70 → 3241.92] um,
[3241.92 → 3245.92] I've actually set up a telescope instance to talk about telescope.
[3246.42 → 3246.90] So,
[3247.14 → 3250.06] meta dot tells dot p.
[3250.46 → 3250.78] Yeah,
[3250.78 → 3252.18] it's a very hard URL to,
[3252.30 → 3254.10] to say.
[3254.32 → 3254.48] Yeah,
[3254.54 → 3255.20] it sure is.
[3255.84 → 3256.42] Using the
[3256.46 → 3256.78] uh,
[3256.78 → 3258.82] a dot in place of the O in telescope.
[3259.80 → 3260.48] But anyway,
[3260.64 → 3261.14] so yeah,
[3261.24 → 3261.64] um,
[3261.78 → 3262.56] we use this,
[3262.56 → 3262.88] uh,
[3263.10 → 3266.38] board to just track new features and what we want to work on.
[3266.38 → 3268.74] So you can head there and take a look.
[3270.22 → 3271.46] And in general,
[3271.46 → 3272.38] I guess it's not even,
[3272.38 → 3272.88] you know,
[3273.34 → 3273.68] uh,
[3273.68 → 3275.68] developing new features as much as the
[3275.78 → 3280.62] just using the project because I believe the only way like people are going to be motivated
[3280.62 → 3284.62] to contribute to telescope is if they're using telescope for their own project,
[3284.62 → 3284.90] right?
[3285.00 → 3285.88] Like I am.
[3286.40 → 3287.66] So yeah,
[3287.66 → 3289.54] I would encourage people to just think of cool,
[3289.54 → 3290.14] uh,
[3290.14 → 3291.58] users that they could,
[3291.66 → 3291.98] uh,
[3291.98 → 3293.36] come up with for telescope.
[3293.94 → 3294.66] For example,
[3294.66 → 3295.16] we have,
[3295.26 → 3295.62] uh,
[3295.62 → 3298.00] one guy doing a telescope for,
[3298.12 → 3298.40] um,
[3299.06 → 3300.70] for the meteor community in Brazil.
[3301.84 → 3302.32] Um,
[3302.84 → 3304.30] another friend did,
[3304.44 → 3304.68] uh,
[3304.96 → 3306.30] use telescope to set up,
[3306.44 → 3306.62] uh,
[3306.62 → 3307.62] uh,
[3307.84 → 3309.04] a board for,
[3309.16 → 3309.52] um,
[3310.14 → 3310.92] Google IO,
[3311.14 → 3311.56] I think,
[3312.10 → 3312.70] just to,
[3312.74 → 3314.22] to centralize info about that.
[3314.70 → 3315.56] So yeah,
[3315.56 → 3316.82] think of a topic that you,
[3316.88 → 3321.98] you like and that you're interested in and see if you can use telescope to just create a community around that.
[3321.98 → 3324.32] And yeah,
[3324.32 → 3326.78] I think that it's something that can definitely,
[3327.32 → 3327.70] um,
[3328.40 → 3329.64] I think that there's no limit,
[3329.64 → 3329.92] right?
[3330.00 → 3332.80] To what communities could benefit from this.
[3332.80 → 3333.60] And we've had,
[3333.66 → 3334.24] it's interesting.
[3334.32 → 3335.46] We've had a few different,
[3336.14 → 3336.46] this is,
[3336.52 → 3336.88] Adam,
[3336.88 → 3339.48] this is almost like an ongoing theme we have of,
[3339.58 → 3341.22] we're bringing on projects that,
[3341.28 → 3341.76] uh,
[3341.76 → 3342.20] you can,
[3342.20 → 3343.60] I don't know what the best way to put it is,
[3343.64 → 3345.36] but you can use these projects,
[3345.68 → 3346.54] uh,
[3346.68 → 3347.06] to,
[3347.34 → 3351.60] to almost build a community around the project itself.
[3351.80 → 3352.28] Uh,
[3352.28 → 3353.22] we did that with,
[3353.22 → 3353.94] um,
[3354.48 → 3354.96] uh,
[3354.96 → 3355.48] discourse.
[3355.94 → 3356.42] Uh,
[3356.42 → 3358.94] we did that last week, and now we're doing that with telescope.
[3359.10 → 3361.30] That's kind of a weird coincidence that,
[3361.30 → 3361.54] uh,
[3361.54 → 3362.98] we're bringing on these,
[3363.18 → 3366.88] these projects that you can use the project to talk about the project itself.
[3367.40 → 3367.70] Inception,
[3368.08 → 3368.76] just like that.
[3368.88 → 3369.02] So,
[3369.42 → 3369.66] yeah,
[3369.70 → 3371.50] it's inception of hacking.
[3371.50 → 3372.50] And so,
[3373.26 → 3373.54] Sasha,
[3373.62 → 3374.20] our last question,
[3374.34 → 3374.44] and,
[3374.50 → 3376.42] and this just gives you kind of chance to,
[3376.42 → 3377.08] uh,
[3377.50 → 3379.22] give a shout-out to anybody you want,
[3379.30 → 3381.30] but who would you say is your programming hero?
[3384.08 → 3384.44] Oh,
[3384.60 → 3384.78] uh,
[3384.78 → 3385.56] that's a hard one.
[3386.76 → 3387.16] Um,
[3387.42 → 3388.38] programming hero.
[3388.82 → 3389.20] Well,
[3389.60 → 3390.90] I guess I could say Tom Coleman,
[3391.06 → 3392.00] but that would be cheating.
[3392.92 → 3393.24] Um,
[3393.76 → 3398.08] yeah,
[3398.10 → 3398.84] that's really hard.
[3399.04 → 3400.96] I guess you could say your design hero too,
[3401.04 → 3401.22] if you,
[3401.22 → 3401.90] because you've kind of,
[3401.90 → 3402.32] uh,
[3402.32 → 3403.76] spread the gamut of both realms.
[3404.48 → 3406.26] So I guess my programming hero,
[3406.48 → 3408.14] or I guess one of them would be John racing.
[3409.48 → 3409.88] Um,
[3410.38 → 3414.26] because like jQuery is what really got me into JavaScript.
[3414.64 → 3416.04] And without that,
[3416.10 → 3419.86] I guess I wouldn't be doing any meat here and design hero.
[3421.94 → 3422.34] Um,
[3422.34 → 3424.52] that's another really hard one.
[3425.34 → 3426.14] There's so many,
[3426.14 → 3427.18] um,
[3427.18 → 3428.18] um,
[3428.60 → 3430.64] well,
[3430.68 → 3432.00] I guess not so much a person,
[3432.12 → 3432.70] but dribble.
[3433.20 → 3433.50] Like,
[3433.78 → 3436.56] I guess dribble is my design hero because that's what pushed me to,
[3436.60 → 3438.42] to really improve my game and,
[3438.54 → 3439.38] and,
[3439.44 → 3439.80] um,
[3439.90 → 3440.66] try and,
[3440.66 → 3440.88] and,
[3440.88 → 3441.32] you know,
[3441.54 → 3444.14] do better than what I was doing.
[3444.22 → 3445.14] We are pretty crappy.
[3445.66 → 3447.34] So I guess not Dan Cedar Holmes,
[3447.46 → 3448.12] not your hero,
[3448.12 → 3450.32] but the community that he's helped develop over there.
[3451.52 → 3452.18] Sorry about that,
[3452.20 → 3452.38] Dan.
[3453.14 → 3453.50] Yeah.
[3453.60 → 3453.84] Sorry,
[3453.92 → 3454.10] Dan.
[3454.14 → 3455.02] That means don't my hero too.
[3455.02 → 3455.42] No cookies.
[3455.42 → 3457.96] That's awesome,
[3458.06 → 3458.14] man.
[3458.26 → 3459.04] Dribbble is a
[3459.04 → 3459.78] is a fun community.
[3459.82 → 3460.80] I can imagine too,
[3460.84 → 3461.58] because you know,
[3461.72 → 3462.84] each shot you put out,
[3462.90 → 3463.14] I mean,
[3463.20 → 3464.92] you're pretty popular on,
[3464.92 → 3465.86] on dribble as well,
[3465.86 → 3466.16] but,
[3466.78 → 3467.20] um,
[3467.36 → 3470.72] it just goes to show that each new shot you put out,
[3470.78 → 3473.52] if you're always trying to improve from the shot beforehand,
[3473.52 → 3476.18] how that plays into how you become a
[3476.24 → 3477.10] a better designer.
[3477.10 → 3478.50] And I know that you use that,
[3478.50 → 3479.36] uh,
[3479.36 → 3480.46] community as a show and tell,
[3480.54 → 3482.90] but also as a way to take that,
[3482.92 → 3483.24] uh,
[3483.24 → 3483.94] that criticism,
[3483.94 → 3485.04] uh,
[3485.04 → 3485.84] so to speak and,
[3485.84 → 3486.98] and improve upon that.
[3488.42 → 3488.82] Yeah.
[3488.82 → 3492.80] I think that's the key to becoming a better designer and a better coder too.
[3492.98 → 3493.38] Absolutely.
[3494.18 → 3494.54] Well,
[3494.58 → 3494.78] Sasha,
[3494.78 → 3496.66] we definitely want to thank you for coming on the show today.
[3496.66 → 3496.86] I mean,
[3496.86 → 3497.16] it's,
[3497.16 → 3497.48] uh,
[3497.70 → 3498.08] it's,
[3498.16 → 3498.66] it's wild,
[3498.76 → 3499.02] uh,
[3499.02 → 3500.40] just having,
[3500.58 → 3500.76] uh,
[3500.76 → 3501.38] I guess,
[3501.44 → 3503.28] knowing you for the last little bit this year,
[3503.28 → 3505.76] just meeting up on the industry and then coming back here on the change law,
[3505.84 → 3506.08] just,
[3506.08 → 3507.22] um,
[3507.32 → 3508.42] getting to know you a bit better.
[3508.42 → 3509.68] As Andrew mentioned,
[3509.80 → 3512.84] I was wrongfully assuming that,
[3512.90 → 3513.04] uh,
[3513.04 → 3513.90] you came from a design,
[3513.90 → 3514.26] background,
[3514.26 → 3514.90] but lo and behold,
[3514.90 → 3515.72] you had this,
[3515.72 → 3515.96] uh,
[3515.96 → 3516.92] the CS background.
[3517.24 → 3517.32] And,
[3517.92 → 3518.26] um,
[3518.32 → 3520.38] even Christian Boyle mentioned in the
[3520.38 → 3520.80] uh,
[3521.20 → 3522.62] the IRC room that that's,
[3522.74 → 3523.72] that's why your,
[3524.28 → 3524.70] um,
[3524.70 → 3527.30] your writing is so informed because,
[3527.42 → 3527.76] you know,
[3528.46 → 3529.10] you're,
[3529.32 → 3529.86] you know,
[3529.86 → 3532.52] you don't just like whimsically write onto your blog.
[3532.60 → 3533.92] You seem to have this,
[3534.06 → 3534.92] um,
[3535.32 → 3535.90] sort of,
[3535.90 → 3537.86] I guess,
[3537.94 → 3538.30] backing.
[3538.38 → 3538.96] I'm not really sure.
[3538.96 → 3539.42] Maybe it's,
[3539.50 → 3540.22] maybe it's just,
[3540.30 → 3540.72] um,
[3541.50 → 3543.28] assurance of what you're writing about,
[3543.38 → 3543.78] uh,
[3543.78 → 3545.72] even if you're not exactly sure what you're writing about,
[3545.80 → 3546.00] but,
[3546.08 → 3546.52] uh,
[3546.52 → 3547.12] you kind of have this,
[3547.24 → 3547.44] this,
[3547.54 → 3547.80] uh,
[3547.80 → 3548.68] this stance about you.
[3548.76 → 3548.88] So,
[3548.88 → 3549.60] but yeah,
[3549.60 → 3552.98] definitely thank you for coming on the show, and thank you for writing the book for,
[3552.98 → 3553.66] for me to hear.
[3553.90 → 3554.22] Um,
[3554.26 → 3555.42] I think that's super awesome.
[3555.46 → 3557.70] And thanks so much for giving us access to it.
[3557.72 → 3558.16] We'll definitely,
[3558.16 → 3558.82] uh,
[3558.82 → 3562.80] share our thoughts on it as well and be sure to plug it on the change log,
[3562.80 → 3563.26] but,
[3563.36 → 3563.68] um,
[3564.58 → 3564.82] cool.
[3564.92 → 3565.72] Thanks for having me.
[3565.72 → 3566.66] It was a lot of fun.
[3566.66 → 3566.80] Yeah,
[3566.84 → 3566.98] man.
[3567.06 → 3567.22] Yeah,
[3567.22 → 3567.40] man.
[3567.78 → 3568.10] Um,
[3568.10 → 3569.00] so we tune into this,
[3569.04 → 3569.26] uh,
[3569.26 → 3571.74] we broadcast the show live every Tuesday at five.
[3571.74 → 3574.76] So if this is your first time listening next week,
[3574.76 → 3575.24] uh,
[3575.24 → 3576.12] set your watch.
[3576.12 → 3578.86] We will broadcast live next week as well.
[3578.86 → 3579.96] We're here on five by five.
[3580.48 → 3581.62] You can go to five by five.
[3581.62 → 3584.82] So if you want to read about,
[3584.82 → 3585.76] um,
[3586.08 → 3586.44] uh,
[3586.44 → 3587.18] different posts,
[3587.18 → 3588.00] as I mentioned,
[3588.00 → 3588.40] uh,
[3588.40 → 3590.38] Sasha guest change logged,
[3590.50 → 3591.06] if that's a
[3591.12 → 3592.84] that's a term on the change log,
[3592.96 → 3595.38] you can go to the change log.com to,
[3595.38 → 3595.82] uh,
[3595.82 → 3596.22] read more.
[3596.30 → 3598.46] We've got tons of writers and cover all the
[3598.58 → 3599.68] all the topics of open source.
[3599.86 → 3601.18] So without further ado,
[3601.22 → 3602.06] that is the show.
[3602.10 → 3602.72] So let's say goodbye.
[3603.56 → 3604.18] See you all later.
[3611.62 → 3612.26] So.
[3614.26 → 3614.74] Yeah.
[3624.08 → 3624.20] Yeah.
[3636.30 → 3636.42] Yeah.
[3636.42 → 3636.58] Yeah.
[3636.58 → 3636.86] Yeah.
