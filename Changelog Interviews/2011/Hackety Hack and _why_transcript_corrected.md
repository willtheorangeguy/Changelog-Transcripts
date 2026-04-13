[0.00 → 18.20] Welcome to the Changelog episode 0.4.3.
[18.48 → 19.50] I'm Adam Stachowiak.
[19.70 → 20.56] And I'm Wynne Netherlands.
[20.68 → 21.62] This is the Changelog.
[21.66 → 23.66] We cover what's fresh and new in the world of open source.
[24.06 → 26.92] If you found us on iTunes, we're also on the web at thechangelog.com.
[27.00 → 27.86] We're also up on GitHub.
[27.86 → 29.52] Head to GitHub.com slash explore.
[29.60 → 33.32] You'll find some trend repos, some feature repos from our blog, as well as the audio podcast.
[33.66 → 36.06] And if you're on Twitter, follow ChangeLog Show.
[36.54 → 37.46] I'm me, Adam Stack.
[37.72 → 39.92] And I'm Penguin, P-E-N-G-W-Y-N-N.
[40.24 → 41.06] Fun episode this week.
[41.12 → 42.20] Got a new contributor on board.
[42.60 → 43.20] Yeah, Steve.
[43.42 → 44.02] Welcome aboard.
[44.52 → 49.38] Welcome, Steve Planck, the I guess, maintainer now of Hacking Hack from Hawaii.
[49.52 → 51.38] We talked about Hacking Hack in this episode.
[51.86 → 53.28] A lot of fun stuff with this project, too.
[53.28 → 62.74] I love seeing what it's going to do for, you know, programming in general, but specifically that bigger application, Shoes, and then, you know, Hacking Hack itself and being a Ruby app.
[63.10 → 65.90] Yeah, definitely a fun way to learn programming and Ruby to boot.
[66.28 → 68.04] So we also have some jobs to promote, too.
[68.12 → 69.68] We've got some fun GitHub jobs.
[69.80 → 76.78] If you're looking for posting a job, head to thechangelog.com slash jobs to use our affiliate link and post a job to GitHub.
[76.88 → 77.64] And we appreciate it.
[77.70 → 79.10] But, Wynn, why don't you take the first one?
[79.10 → 83.22] First up this week is a Ruby engineer slash data wrangler over at PostRank.
[83.58 → 87.22] I guess a data wrangler means you have to be in Texas for this gig.
[87.60 → 90.14] Need to be fluent in Ruby Rails, Vent Machine, RabbitMQ.
[90.78 → 97.20] The usual suspects when, if you work on an Ilya project, we know that Ilya Gregorio works over at PostRank.
[97.30 → 99.70] This should be a fun gig for anybody that wants to sling the Ruby.
[100.18 → 107.44] And if you want to change the world, Causes.com is looking for the most world-changing Ruby Rails developer in history.
[107.44 → 107.96] Seriously.
[108.44 → 111.74] Go to Causes.com to check out more details about that company.
[111.84 → 121.80] But they're approaching 25 million active users on a series of Rails applications that's backed by MySQL and Teacake, D, Regis, and a few other fun things.
[121.98 → 125.70] But plenty of things to do there, scaling, product challenges.
[126.16 → 129.82] So if that's your world, check them out and check out the show notes for details.
[129.82 → 135.92] If your LinkedIn profile mentions Rockstar or Ninja, you need not apply at Centro.
[136.12 → 142.60] They're looking for talented developers of JavaScript, CoffeeScript, Sprout Core, jQuery, Ruby, Sinatra, Rails, and MongoDB.
[142.84 → 143.78] That's quite the stack.
[144.40 → 144.66] Wow.
[145.34 → 146.80] I understand they use all those over there.
[147.12 → 148.34] That's pretty intense.
[149.62 → 150.18] Hacking hack.
[150.72 → 151.74] Don't talk back.
[151.74 → 181.72] Thank you.
[181.74 → 183.68] I've been programming since I was about seven years old.
[184.12 → 191.98] And by now, I'm much more interested in how to make good software and the surrounding things than the actual code itself.
[192.26 → 201.56] So I've been focusing a lot on best practices and refactoring and all sorts of things like that, which is one of the reasons why I really love Ruby and why I now call myself a Rubbish for the last couple of years.
[201.56 → 203.66] It's because the Ruby community is into all this kind of things.
[203.66 → 210.66] So my main open source project is Hacking Hack, which I inherited from Y, which we'll talk more about in a little bit, I guess.
[210.98 → 214.66] And I do various startup-related things.
[215.22 → 217.16] So that's sort of what I'm into, I guess.
[217.24 → 219.78] Startups, Ruby, software, all that kind of stuff.
[220.54 → 221.22] So let's jump into it.
[221.26 → 221.88] Hacking Hack.
[222.00 → 225.02] This is a project I guess you inherited from Y the Lucky Stiff?
[225.76 → 226.02] Yep.
[227.10 → 236.36] Basically, it was whenever Y disappeared and everybody realized that he was gone for good, people started stepping up for his projects because, you know, they were all really awesome.
[236.44 → 237.28] We wanted to keep them going.
[237.28 → 239.76] And I had actually just missed Y.
[239.84 → 240.64] I never met him.
[241.50 → 249.42] He came to Pittsburgh a couple of months in March before he disappeared in August and gave a talk at Art & Code about Hacking Hack.
[249.62 → 251.56] And I didn't realize he was going to be there.
[251.76 → 257.86] I wanted to go to Art & Code, but I heard about it, and I was out of town that weekend and I said, OK, well, I'll just hit the next Art & Code up.
[258.04 → 261.90] And then when I came back, I realized Y was there, and I was really upset that I had missed it.
[261.90 → 271.18] But basically, when Y disappeared, nobody stood up to take care of Hacking Hack, and I wasn't really sure that I could do it or not, but I didn't want to let the project die.
[271.42 → 277.18] So, you know, I sort of stepped up and that led to now a year and a half later.
[277.70 → 288.08] So for the folks outside the Ruby community that think we may be talking in terms of Albert and Costello skit here, explain who Y is and Y is important, no pun intended.
[288.08 → 293.58] So Y the Lucky Stiff was an artist whose medium was software.
[294.72 → 305.84] Basically, he was a very well-known figure in the Ruby community who really did the whole – the reason that conference was called Art & Code and the reason why I was talking there was because that's what he was about.
[305.84 → 317.64] So he made very creative, interesting projects in software, but they're very much from that sort of angle rather than from the computer science kind of side of things.
[318.08 → 324.60] He went by the name Y as a pseudonym because he wanted his privacy.
[324.92 → 331.16] Actually, most of the time his name was written with an underscore in the front, which is sort of that convention about private variables.
[332.34 → 338.82] So he went by that name for all the different various things that he did, and so he was a great guy.
[339.56 → 341.50] So what was this Art & Code? What is that?
[341.50 → 348.80] Art & Code is something that there's been two or three of now, but there's a guy named Golan at Carnegie Mellon University here in Pittsburgh.
[349.30 → 356.62] And he's sort of interested in the same kind of space where processing is and a bunch of other – this kind of projects that are connecting those two things together.
[356.62 → 365.38] And so every couple months or so – I guess there's been three of them now – he has this event where he invites people to come and talk.
[365.76 → 368.00] He usually has five or six of them, and it takes a day or two.
[368.68 → 375.22] At the same one that Y was at, they had the guy who wrote processing whose name I'm totally drawing a blank on and a couple other people.
[375.82 → 379.98] They did a mobile-themed one later where it was all about building interesting mobile applications.
[380.22 → 382.90] It's just kind of a general little conference in Pittsburgh.
[382.90 → 386.40] Is that the same thing as the open source gaming coding competition?
[387.48 → 391.88] No, that's actually run by my friends and me, actually.
[392.60 → 401.74] So OS GCC was something where my friends and I have traditionally in college, we all realized that we're giant nerds, and we want to program 24-7.
[402.02 → 410.46] So every Saturday, we set aside Saturday to sleep until noon, go get a burrito and then go to the computer lab and code away.
[410.46 → 416.96] And so because a lot of people were interested in games, we decided to have an annual game coding competition.
[417.62 → 422.52] And so we sort of invited people outside our friends group to get together and do the same sort of thing.
[422.60 → 426.08] So we have this like 24-hour sit down, start making a game.
[426.40 → 428.66] 24 hours later, it gets judged thing.
[428.72 → 431.36] And this past year was a really, really huge year for us.
[431.46 → 435.48] We had more contributors than the rest of the previous three years combined actually I think.
[435.94 → 436.96] So it was perfect.
[436.96 → 442.40] So Hacking Hack is not a singles from the coasters in the late 50s.
[442.48 → 446.04] It's actually a program to help you learn programming using shoes.
[446.16 → 446.60] What's shoes?
[447.14 → 447.30] Yeah.
[447.56 → 450.58] So shoes actually was born out of Hacking Hack.
[450.72 → 451.82] It's another why project.
[451.96 → 459.14] But basically why wanted Hacking to be available on all three platforms because everybody deserves to learn programming.
[459.14 → 470.42] So as he developed it, he decided that basically he should release all of that GUI platform toolkit stuff as a separate project.
[470.64 → 474.30] And so he pulled shoes out of Hacking and released it on its own.
[474.52 → 477.78] And so other people can write apps using the same kind of interface.
[478.34 → 482.38] Shoes is the only GUI toolkit I've ever used that I actually enjoy using.
[482.38 → 487.40] So it seems like every other toolkit is really complicated and takes forever to use.
[487.50 → 498.02] And they're all sort of based on when we started writing toolkits in C in like the 80s or whenever Gnome and KDE date to I guess early 90s, late 80s if I'm remembering my dates correct.
[498.20 → 501.94] But shoes really embraces Ruby in particular and uses blocks.
[502.34 → 505.34] And it's just – it's super easy to actually code in.
[505.34 → 508.26] And so Hacking is the largest shoes application.
[509.06 → 513.24] So I'm sort of – I'm on the core shoes team as well.
[513.34 → 518.80] We have five or six people that work on shoes because I am the largest user of shoes at the same time.
[518.86 → 523.70] But there are tons of other applications that are like little tiny gaming things essentially.
[524.06 → 526.34] So what shoes use under the hood to do the rendering?
[526.60 → 528.94] And face value looks a lot like Tickle TK.
[529.68 → 529.86] Yeah.
[529.94 → 532.22] So right now it depends on what platform you're running.
[532.22 → 535.74] So if you're – shoes 3 is the latest release.
[536.16 → 544.70] If you're using that, then you've got actually native OSX widgets for Mac OS X, I guess I should say.
[544.82 → 546.84] I have a bad habit of saying OS X instead of OS X.
[547.86 → 553.86] It uses GTK on Linux, and it uses the native Windows stuff.
[554.06 → 557.28] And I think it might even use a little bit of GTK stuff on Windows too.
[557.34 → 559.74] I'm not 100% sure because I don't do the Windows stuff.
[559.82 → 561.12] I handle the Mac things mostly.
[562.22 → 564.08] So it's mostly native right now.
[564.46 → 566.56] But it does use Cairo and Mango.
[567.28 → 570.50] And so it has its own sort of widgets drawn as well.
[570.58 → 571.98] It doesn't always use the native ones.
[572.20 → 574.98] But we're looking at shoes 4 to be all in Ruby.
[575.36 → 581.46] And so what it's looking like, it's shaping up to be – we sort of all got together and tried a couple of different approaches.
[581.46 → 589.66] And it looks like shoes 4 is going to be GTK with the native Ruby bindings on Windows and Linux.
[589.74 → 599.62] And either I'm going to get GTK to work properly on the Mac without needing X11, or I'm just going to do a Mac Ruby port for the Ruby side, and it will be in Mac Ruby.
[599.62 → 601.92] So it will be one of those two things.
[602.02 → 603.42] But it will be an all Ruby in the future.
[604.98 → 606.14] Well, you're feeling my segue.
[606.40 → 607.66] That was going to be my next question.
[607.72 → 608.88] How does this fit in with Mac Ruby?
[609.78 → 610.04] Yeah.
[610.04 → 618.38] So the other nice thing about Mac Ruby is that shoes built a packager system that sort of kind of works most of the time.
[619.16 → 621.82] It's sort of this ultimate black magic.
[622.36 → 628.58] One time Y said that he really truly only learned about Ruby once he started working on shoes and digging down into the C code.
[629.70 → 635.46] So basically the shoes has the ability to package up your application to be able to run.
[635.46 → 641.62] You can package up an EXE or a .app or on Linux it uses this weird .run file sort of format.
[641.98 → 644.46] But Mac Ruby has that built in for the Mac already.
[644.66 → 646.60] So it will be nice not to have to replicate that.
[647.22 → 651.42] We're not really 100% sure what we're going to do with the pure Ruby shoes to make that happen.
[651.58 → 653.00] But, you know, I'm working on it.
[653.28 → 658.08] There's been some interesting bundler developments actually to sort of make gems be self-contained.
[658.22 → 662.86] And so I'm looking into possibly, you know, seeing if that can help with some other things.
[662.86 → 665.24] But it's pretty crazy C code at the moment.
[665.46 → 665.98] So, you know.
[666.72 → 668.96] So Hackney Hack uses shoes, but what else uses shoes?
[669.86 → 676.26] I don't think that there's any other big giant applications that you would necessarily be directly familiar with that use shoes.
[676.84 → 686.34] If you go to the shoebox actually, which is the-shoebox.org, that's a little website that is sort of almost like a mini GitHub for shoes.
[686.34 → 691.28] It's actually still, you know, it's up and running.
[691.52 → 697.06] It's the guy who wrote CoffeeScript actually is currently hosting this.
[697.20 → 701.78] But he and I have been talking, and we're trying to work it back into the main project in general.
[701.78 → 706.14] But it's got a ton of little tiny apps that people have written that are really cool.
[706.26 → 711.28] You see like a Go implementation there and somebody made an IM client and all sorts of other things.
[711.58 → 718.68] I really liked Number Crunchers is this Number Munchers clone that I used to play on the Mac when I was in eighth grade or something.
[719.72 → 720.70] And so that was tons of fun.
[720.84 → 723.60] But there's, you know, all sorts of little stuff like that.
[723.68 → 726.52] There aren't any like big, giant, well-known applications.
[726.52 → 728.64] Hacking is definitely the largest.
[729.18 → 740.92] So with Hacking Hack becoming 1.0 officially, I guess, last week, and also getting posted to Life hacker, the unofficial Apple weblog, and a bunch of other things,
[740.98 → 743.38] it's got to certainly raise the profile for shoes at this point, doesn't it?
[743.74 → 744.38] Yeah, definitely.
[744.94 → 746.22] That's my goal.
[746.56 → 751.56] Although I apparently have a lot of work to do because apparently most of the Windows development was done on XP.
[751.56 → 757.94] And so there are some things with Windows Vista and Windows 7 that I'm fixing some bugs that people uncovered.
[758.48 → 759.82] It's the classic software.
[760.02 → 761.60] It works for me perfectly fine.
[761.70 → 767.40] And then you hand it out to – I actually had 12,000 people download Hacking Hack in the last four days.
[767.92 → 770.66] And so I got a lot of good feedback.
[771.50 → 772.96] Everybody seems to really like it.
[773.52 → 781.24] But there's been some crashes that I'm going to be taking care of now that I have a little bit of a broader installed base of people.
[781.56 → 783.78] So how did Heroku handle that traffic?
[784.18 → 786.14] It was a champ.
[786.56 → 792.78] Basically, I'm only ever on the free plan for it using Sinatra and Monographer.
[793.52 → 799.66] And so we got 50,000 uniques and 100,000 hits roughly.
[800.08 → 802.36] Last time I checked the numbers, it's a little bit earlier today.
[803.00 → 807.16] And whenever I got on Life hacker, I added an extra Dino, but it didn't even need it.
[807.46 → 809.82] It totally was awesome.
[809.82 → 812.70] Part of this is because the homepage is mostly static.
[813.30 → 818.60] So the Varnish caching that they have set up on Heroku was super awesome.
[818.84 → 824.78] But, yeah, I never expected to be able to sustain a Life hacker front page and the unofficial Apple weblog too.
[824.96 → 830.82] So both of them basically at the same time, I paid like 15 cents or something because I turned on a Dino for a little while.
[831.30 → 831.66] That's awesome.
[831.70 → 832.60] We're big fans of Varnish.
[832.60 → 836.92] Yeah, it's amazing what a little upfront HTTP caching can do for your application.
[837.04 → 838.26] We need to get those guys on the show.
[838.70 → 839.10] Yeah, yeah.
[839.38 → 840.46] They're super great.
[840.64 → 844.88] The main guy who wrote it, I know, writes all these crazy papers about the system stuff that he does.
[845.94 → 850.26] Two of my better friends are operating system PhD candidates.
[850.26 → 852.50] And so we talk about that stuff all the time.
[852.56 → 854.46] And that guy is a perfect systems guy.
[854.86 → 858.38] So the point of Hacking Hack is to learn programming.
[858.64 → 861.00] What makes Ruby such a great tool for that?
[861.50 → 866.82] Well, so I wrote up something about this actually on the blog a couple of weeks ago.
[866.82 → 872.42] And basically what it boils down to is that Ruby is ultimately very forgiving.
[873.38 → 877.56] It's very well-supported by the community in general.
[878.98 → 880.66] So I guess I should back up slightly.
[880.86 → 885.74] So in the intro to programming class at my university, we use Java.
[885.74 → 892.32] And while Java has its strengths in certain areas, as far as the beginning programming goes,
[892.72 → 899.44] everybody knows the class, main class, public static, void, main, string, array, arms,
[899.54 → 902.48] stuff that gets involved with writing your first program.
[902.74 → 906.88] And so if you're teaching somebody intro to program with something that's a little more static,
[907.10 → 911.42] like Java is, you have to sort of present it as all of these things are magic.
[911.72 → 913.26] Don't worry about the details.
[913.58 → 914.84] This is just hello world.
[914.84 → 919.72] And so you really have to like gloss over this large body of information before.
[920.04 → 922.96] And you sort of are presenting it in that way that like software is something magical
[922.96 → 924.56] and the computer does these crazy things.
[924.72 → 927.86] And you're sort of playing with it, but you're not really like,
[928.36 → 931.50] and it's encouraging that sort of mindset from the get-go.
[931.94 → 935.68] So with Ruby or with Python or Perl or any of the other scripting languages,
[936.06 → 938.22] hello world is just puts hello world.
[938.72 → 942.58] And so you start off with, you know, it executes stuff in order.
[942.58 → 945.12] And, you know, everything is very simple.
[945.38 → 950.24] And so while there is some stuff going on under the hood, you don't have to explain it right away.
[950.32 → 955.72] And I think that's really valuable for beginners because a lot of people get sort of hung up on that early syntax.
[956.16 → 960.66] And once you start getting in that mindset that you don't actually, you're not in control of the machine,
[960.74 → 964.30] the machine is controlling you, and you're sort of playing around with it, you're on the wrong footing.
[964.30 → 966.64] You know, like software is all about us building things.
[967.90 → 970.96] So, you know, that's one of the reasons I feel really strongly about Ruby.
[971.54 → 975.44] The other reason is that the syntax is really nice and expressive.
[976.14 → 981.60] So I just think that in general dynamic languages are much better for learning than static languages are.
[981.60 → 986.38] Because even if they have, you know, some small runtime issues as opposed to compile time issues,
[986.48 → 991.80] I find that beginners are confused by C compilers' error messages anyway.
[992.00 → 994.58] So it doesn't really help as much as you would think it was.
[994.62 → 997.50] Even though it says there's an error, they're, you know, they don't know what it means.
[998.20 → 1002.44] I guess this is a why project previous to being a Steve project.
[1002.66 → 1005.02] But why I wrote this book called Why?
[1005.62 → 1007.02] The Pointing Guide to Ruby.
[1007.02 → 1012.76] So I wonder if there's anything that actually stems from that book that has fallen into the learning patterns of Hacking Hack.
[1013.26 → 1015.36] Yeah, I mean, not necessarily directly.
[1016.20 → 1017.44] It's true.
[1017.62 → 1023.72] So one of the things that took me this long to come out with a 1.0 was because for the first couple of months,
[1024.10 → 1027.66] I was Uber sensitive about the fact that I am not Why.
[1028.24 → 1030.12] You know, like it's really, really hard.
[1030.40 → 1032.88] It's sort of like, I don't know whoever it was,
[1032.88 → 1036.68] but whoever was the point guard of the Chicago Bulls right after Jordan retired,
[1037.02 → 1041.76] you know, there's like huge shoes to fill and people have huge expectations of you.
[1042.28 → 1048.10] And so it's also difficult because I really loved Why's style and I thought that it was great,
[1048.42 → 1049.78] but it's also not my style.
[1049.98 → 1055.28] So I need to keep the project respecting sort of his original way of doing things,
[1055.30 → 1056.96] but make it my own at the same time.
[1056.96 → 1064.22] So I really had lots of problems initially sort of grappling with those kinds of awkward identity issues where,
[1064.32 → 1067.94] you know, am I just going to totally screw up Why's greatest, you know, masterpiece?
[1069.24 → 1073.68] And, you know, so once I finally got over myself and just started actually writing code, everything worked out.
[1074.12 → 1075.96] But, you know, that's –
[1075.96 → 1081.30] there's not anything necessarily directly from the point and guide because I'm trying to sort of –
[1081.30 → 1083.58] I don't want Why to go away.
[1084.06 → 1085.88] I obviously wish that he was still here.
[1086.36 → 1092.50] But running around saying why, why, why, why, why, and crying about it is not going to let the community move forward.
[1092.80 → 1094.70] And so I'd like to –
[1094.70 → 1098.00] rather than try to use more and more of what Why's earlier works did,
[1098.04 → 1101.52] I would rather be inspired by them and make new stuff that's equally awesome.
[1101.52 → 1102.92] So no Chunky Bacon?
[1103.32 → 1103.58] Yeah.
[1103.74 → 1111.48] I try to leave some of that stuff in there, you know, but I'm trying to gradually sort of –
[1111.48 → 1115.44] as the grieving process moves along, you know, it's been a while.
[1115.56 → 1119.24] So it gets easier and easier as time goes on to sort of take those things out.
[1119.68 → 1121.86] I noticed the Chunk 5 font on the website.
[1121.98 → 1123.68] Is that a tribute to Chunky Bacon?
[1124.36 → 1125.06] Yeah, I know.
[1125.14 → 1129.08] It's just that it just happened to be a nice one that I like the look of.
[1129.08 → 1132.94] If you're not sure what we're talking about, go check out Why's Poignant Guide to Ruby.
[1133.68 → 1137.62] So up on GitHub, Hacking Hack is touting around 200 watchers now.
[1137.76 → 1139.84] So when you posted it last week to the changelog,
[1139.88 → 1143.72] what kind of effect did it have to the watch status and fork status of Hacking Hack?
[1144.76 → 1145.86] You know, it's funny.
[1145.98 → 1149.26] Every time I post something to the changelog, I always tell myself, like,
[1149.78 → 1154.84] I want to look and see how many things that changes, but I never do.
[1154.84 → 1159.28] I'm a huge sucker for game mechanics, and this kind of numbers are something that I, like,
[1159.34 → 1160.74] intensely am all into.
[1160.96 → 1168.34] But I think that I added about 70 or 80 watchers and probably 10 or 15 forks.
[1168.64 → 1174.12] I definitely got some contributions from people that I'd never gotten before after it was posted.
[1174.36 → 1180.46] So thanks to everybody who's now watching and, you know, the people who are contributing to it.
[1180.46 → 1184.16] Although I still am doing the vast majority of the work on Hacking itself.
[1184.90 → 1189.00] But, you know, we've gotten some good patches in from people.
[1189.24 → 1190.72] So it's been nice.
[1191.32 → 1192.70] I've sort of got to raise the bar for it a little bit.
[1192.78 → 1197.14] You've got 27 issues there now that are mentioned there.
[1197.24 → 1201.34] But what kind of support are you getting from the community now in terms of actual pull requests
[1201.34 → 1204.26] and what kind of changes that come from not just you but others?
[1204.26 → 1210.62] So I'm still not getting a lot of actual software support.
[1210.82 → 1215.04] So those 27 issues, a lot of them are actually shoes bugs that Hacking exposed.
[1215.58 → 1216.90] So they're sort of merged in.
[1217.34 → 1220.48] And one of the things I want to do with the shoes issue tracker was we were keeping track
[1220.48 → 1222.08] of feature requests in the issues' tracker.
[1222.24 → 1226.52] But now it looks like there's a million, there's like 45 issues now because we have, you know,
[1226.52 → 1229.54] 15 or 20 of them are feature requests that people ask for.
[1230.24 → 1231.88] So I want to sort of move those around.
[1231.88 → 1235.80] So sometimes those issues get a little conflated a little bit where, you know,
[1235.82 → 1238.74] it's not really my fault so much as something that I'm doing that messes up shoes.
[1238.96 → 1243.58] But one of the things that I'm continually trying to do is lower the bar for contribution
[1243.58 → 1248.00] because I want Hacking to be the ideal open source project.
[1248.26 → 1251.90] You know if I'm going to be teaching people programming, I sort of have this, you know,
[1251.94 → 1255.90] subtle goal of getting them to contribute to open source as well.
[1256.06 → 1261.36] So you'll see the website and the project in general will merge more and more towards trying
[1261.36 → 1266.66] to get people to share their code with each other and improve on each other's things.
[1267.02 → 1270.72] I definitely want to add the ability to fork people's projects on Hacking Act and those
[1270.72 → 1271.30] kind of things.
[1271.72 → 1274.96] It's already happened one or two times on its own and that made me really, really super
[1274.96 → 1278.70] happy where someone posted their program and then somebody else said, hey, check this
[1278.70 → 1278.90] out.
[1278.98 → 1282.14] Like I made your thing, but I added, you know, another screen to it or whatever.
[1282.74 → 1283.58] So that was really exciting.
[1283.58 → 1288.76] But one of the big things that we're trying to address with the next version of shoes is
[1288.76 → 1291.34] that shoes is incredibly difficult to compile.
[1292.86 → 1297.72] It actually, because Y was not necessarily known for commenting his code and he was also
[1297.72 → 1303.96] known for lots of metaprogramming and the fact that shoes is a C and C++ and Objective-C
[1303.96 → 1305.54] and Ruby project.
[1306.42 → 1310.30] It's a bit intimidating sometimes if something goes wrong during the compilation step.
[1310.30 → 1313.54] So you don't actually need to compile shoes to work on Hacking Hack.
[1313.66 → 1317.12] You can just download shoes itself and open the RB files and make it work.
[1317.46 → 1321.00] But I think that I'm not doing a good job yet of letting people know that.
[1321.18 → 1325.98] And so I think that it's slightly intimidating to some people because of that factor.
[1326.20 → 1332.04] So I'm continually trying to make it more and more easy to contribute because, you know,
[1332.12 → 1333.46] I would love to have people help me out.
[1333.46 → 1339.80] But, you know, that's kind of the thing is this dual nature of the project being two projects
[1339.80 → 1343.18] but one project kind of is, you know, a little intimidating for people that don't know what's
[1343.18 → 1343.62] going on.
[1343.86 → 1348.86] It certainly has to expose some of those dependency issues that we see in Ruby apps and whatnot.
[1349.44 → 1349.66] Yeah.
[1349.92 → 1353.82] And because we also, I don't want to make people install extra things.
[1354.02 → 1358.04] So what shoes actually does is it compiles all of its dependencies and then wraps them all
[1358.04 → 1359.00] up inside itself.
[1359.00 → 1361.06] So it's completely self-contained.
[1361.52 → 1365.12] And so there's been some issues sometimes with those kinds of dependency issues too where
[1365.12 → 1368.94] I've included the wrong versions of something, or I've accidentally left one out, you know,
[1368.98 → 1369.98] and then it happens.
[1370.34 → 1374.20] So for those listening out there that are on different platforms other than what you develop
[1374.20 → 1376.52] on, what do you need most help on?
[1377.00 → 1383.50] What would be great is somebody who really knows about Windows 7 and Vista and the ways that
[1383.50 → 1384.68] they were different from Windows XP.
[1384.68 → 1390.42] So we pretty much have Team Shoes essentially has three people, one on each platform that
[1390.42 → 1394.80] sort of manages and does most of the development on that particular platform.
[1395.08 → 1403.34] So the guy who does Windows development, his name is Ash, Ashby on Twitter, and he uses
[1403.34 → 1404.60] Windows XP primarily.
[1405.04 → 1408.46] And so a lot of the development was sort of done in that era too, I think, that Y was developing
[1408.46 → 1408.86] on XP.
[1408.86 → 1413.12] So for instance, somebody let me know that I was installing certain things to a protected
[1413.12 → 1416.10] folder and that was causing crashes on some people's systems and not others.
[1416.30 → 1421.10] So I would really love somebody who knows more about Windows development to, you know, to
[1421.10 → 1421.64] give me a hand.
[1421.72 → 1426.66] That would be really great because I come from the Linux and Mac world and so all those tools
[1426.66 → 1427.56] are sort of foreign to me.
[1427.68 → 1431.50] And I got my VM set up last night and I got everything to compile and working out.
[1431.62 → 1432.92] So, you know, I'm working on learning it.
[1433.06 → 1436.30] But, you know, it's always good to have people who know what they're talking about.
[1436.30 → 1439.44] So that would be the largest need for sure as somebody who knows Windows stuff.
[1439.44 → 1444.72] I know most of our contributors are way younger than Adam or me, but if you've started when
[1444.72 → 1447.38] you were seven, I'm guessing Ruby wasn't your first programming language?
[1448.08 → 1449.00] No, not at all.
[1449.16 → 1450.94] So how many languages do you speak?
[1452.00 → 1457.28] I've done serious projects in, I guess it's probably just easier rather than counting the
[1457.28 → 1458.96] numbers to go back through and think about it.
[1458.96 → 1466.76] So I started off using GW Basic, and then I moved to C and then C++ and then Perl and Java.
[1467.48 → 1471.18] And then I did a little bit of Python, but I found Ruby and I liked it better.
[1471.38 → 1475.16] So I've done more in Ruby, but I have done one or two projects in Python, including some
[1475.16 → 1476.04] robotics stuff.
[1476.86 → 1481.72] I have a love affair with Haskell, which I'm always trying to find more excuses to use,
[1481.80 → 1483.20] but I haven't really gotten around to yet.
[1483.62 → 1485.72] I've played around with various Lisps and Scheme.
[1485.72 → 1491.10] Um, I, I enjoy doing JavaScript stuff sometimes in the browser when it's not too tricky.
[1491.38 → 1494.28] Uh, sometimes it gets frustrating, but that's, uh, you know, a lot of fun.
[1494.86 → 1500.24] Um, I have several friends who are heavily involved in the D language programming community.
[1500.70 → 1504.84] Uh, and so I've used D for a couple of things, although nothing super major, but, um, that
[1504.84 → 1508.12] operating system project that I was talking about earlier, my friends are doing PhD candidates
[1508.12 → 1510.46] are actually writing it in D, which is kind of cool.
[1510.46 → 1515.22] Um, and, uh, you know, a couple assembly languages every once in a while.
[1515.28 → 1516.34] And that's, I think that's it.
[1516.46 → 1516.88] I don't know.
[1516.92 → 1517.42] A lot of stuff.
[1517.52 → 1518.14] I love languages.
[1518.80 → 1522.86] So you find it easier to pick up new languages after you get more under your belt.
[1523.40 → 1523.76] Yeah.
[1523.78 → 1527.84] I think that what it really takes is once, once you get a dynamic language, like a scripting
[1527.84 → 1531.42] language, uh, Ruby, Python, Pearl, you know, any of the three of those are something
[1531.42 → 1531.84] similar.
[1531.84 → 1536.08] And once you get a functional language, and you get a more normal, like static imperative
[1536.08 → 1539.58] language, once you have those three under your belt, it becomes really easy to pick
[1539.58 → 1545.76] up almost anything else because most languages are pretty closely tied to those three different
[1545.76 → 1546.20] ideas.
[1546.32 → 1549.44] There are not a lot of ones outside those kinds of categorizations.
[1550.20 → 1555.80] So, uh, you know, but definitely, um, learning Haskell and functional programming was one part
[1555.80 → 1560.90] where I really felt like I got much better as a programmer, and it continues to improve my Ruby
[1560.90 → 1562.06] code to this day.
[1562.36 → 1566.04] Uh, whenever I do, you know, functional sort of things that Ruby supports.
[1566.28 → 1571.30] So before we get to the, the infamous radar question, I have a kind of off the wall
[1571.30 → 1572.18] question for you.
[1572.50 → 1572.90] Okay.
[1573.46 → 1578.16] In, uh, in your, your bio and what we posted here to the change log to kind of introduce
[1578.16 → 1579.00] you to the audience.
[1579.36 → 1579.72] Yes.
[1579.72 → 1582.94] Um, there's, there's one piece that stands out a little bit, and it says that you're an
[1582.94 → 1588.68] anarchist and at the same time, you're also involved in open source and kind of creating
[1588.68 → 1589.42] this community.
[1589.42 → 1591.68] Does that kind of become an oxymoron for you?
[1591.78 → 1594.58] And why, uh, why would you say that and be in open source?
[1595.26 → 1596.80] I think it's actually the exact opposite.
[1597.12 → 1603.44] So I, first, I call myself an anarchist because I've been, I've been reading about
[1603.44 → 1605.24] anarchism for the last year or two.
[1605.36 → 1610.16] And so it took me a really long time to, uh, to identify that way, but I'm pretty sure
[1610.16 → 1612.84] that I agree with most of that, um, political theory now.
[1612.84 → 1615.16] So it feels the most, the most correct to me.
[1615.16 → 1622.50] But basically anarchism is fundamentally about empowering people to do the things they want
[1622.50 → 1622.80] to do.
[1622.92 → 1628.00] It's about not being controlled by others and, and doing, uh, like empowering people that
[1628.00 → 1628.16] way.
[1628.18 → 1628.96] And it's about community.
[1628.96 → 1635.54] Like you can't, you can't have, uh, a, a group of people, um, work together effectively
[1635.54 → 1637.18] unless they know each other, and they become friends.
[1637.18 → 1642.38] So anarchism gets a terrible rap because, uh, you know, it's, uh, been sort of slandered
[1642.38 → 1643.34] by people over the years.
[1643.34 → 1648.04] But, um, really I think that, I think that open source and specifically the internet actually
[1648.04 → 1656.10] is a great example of how anarchism could theoretically work as, as a way of governing people, um, because
[1656.10 → 1657.94] of that they're exactly that they're distributed.
[1658.24 → 1660.40] No one's necessarily directly in charge.
[1660.74 → 1665.52] Um, and you know, so that sort of relates into those things, but, uh, that's why I identify
[1665.52 → 1670.40] that way, um, anarchism is not, there's a sort of saying like anarchism is not no rules.
[1670.46 → 1671.52] It's no rulers.
[1672.42 → 1674.18] Um, it's about direct democracy.
[1674.36 → 1680.36] And so you can sort of think of it as libertarianism to a slightly even more, um, extreme to the
[1680.36 → 1682.52] point where they don't like capitalism essentially.
[1683.06 → 1685.90] So for the folks who don't really know Steve yet, and then when they read that, it's
[1685.90 → 1689.78] like, could have been a, uh, a negative thing, I guess, but you just definitely clarified
[1689.78 → 1695.12] the air that you're not a an evil co-conspirator of some sort of, um, I don't know,
[1695.12 → 1697.50] like, uh, conspiracy theories and stuff.
[1698.40 → 1698.46] Yeah.
[1698.60 → 1698.80] Yeah.
[1698.86 → 1702.58] It's, it's one of those things where, uh, I wish there was a better word because people
[1702.58 → 1708.44] have sort of, uh, taken it down, uh, a notch by associating it with all sorts of, you know,
[1708.44 → 1709.92] other things, uh, necessarily.
[1710.14 → 1712.84] And, you know, this is a very complicated topic.
[1712.84 → 1717.16] I guess I'll just leave it at that, but it's not as simple as like, I'm a teenager and I
[1717.16 → 1720.42] hate my parents, so I don't want there to be any rules in the world would be awesome.
[1721.38 → 1722.62] That's, that's really all I have to say.
[1722.62 → 1726.00] And if anybody has questions, you can email me about it, and I'd be more than happy to,
[1726.00 → 1727.30] you know, talk about it in more depth.
[1727.64 → 1728.56] Nah, I'm sure you're a good guy.
[1728.64 → 1732.62] I mean, I was just, I was just, uh, just kind of curious about how that played into your
[1732.62 → 1732.92] role.
[1733.00 → 1738.00] And then, um, just in, in general, I just thought I'd ask, but, um, I guess
[1738.00 → 1741.88] it's about time that we asked of what's on your open source radar.
[1741.88 → 1744.58] So that's, uh, there's lots of stuff out there in the open source world.
[1744.66 → 1745.36] It moves fast.
[1745.46 → 1748.68] We try our best to keep up, but what's out there in open source.
[1748.76 → 1750.90] It's on your radar that you just have to go out and play with right now.
[1750.90 → 1755.38] So the biggest things, the two, the two largest things that I want to play with more, um,
[1755.84 → 1757.32] are vented programming.
[1757.48 → 1760.08] So that's why I posted that Coolio project a couple of days ago.
[1760.72 → 1767.10] Um, I would love to do something with Node.js and, or event machine or Coolio, but vented
[1767.10 → 1771.34] style web programming is something where I have very little experience, but it seems like it
[1771.34 → 1774.18] has a perfect use case, um, in certain times.
[1774.18 → 1777.72] And so that would be, uh, definitely something that I would like to expand some more knowledge
[1777.72 → 1779.06] about, and it's getting kind of hot lately.
[1779.60 → 1783.78] Um, the other thing is that I've been using MongoDB a lot and I really, really enjoy it.
[1784.10 → 1788.04] Um, and I would like to get familiar with some of the other NoSQL stores since they're not
[1788.04 → 1789.38] really similar to each other.
[1789.38 → 1792.30] It's sort of like learning different ones every time, you know?
[1792.30 → 1799.58] So I think that, uh, I think that learning more about the, the details of Cassandra and,
[1799.58 → 1807.04] um, like Ryan, uh, I've used Regis a teeny little bit and, um, uh, Couch DB are the other
[1807.04 → 1810.60] ones that I really want to try to, uh, you know, learn how to use those tools effectively
[1810.60 → 1813.22] because it's all about using the right tool for the job, right?
[1813.24 → 1816.20] So the more things you learn, the more equipped you are to solve problems.
[1816.20 → 1821.84] So, um, I guess those are the next big things that I'm sort of interested in, uh, in learning
[1821.84 → 1825.42] about in the open source projects that are sort of popping up now that those things are
[1825.42 → 1826.02] getting popular.
[1826.20 → 1831.16] We've done a couple of shows now on, uh, Ryan and we've covered, uh, MongoDB on the show.
[1831.24 → 1834.30] I'd love to get, uh, Regis on the changelog.
[1834.38 → 1839.12] We'll have to keep trying to nail down Antares to get, get him on the show, but, uh, Cassandra
[1839.12 → 1840.88] would be another, another great episode.
[1841.14 → 1841.54] Yeah.
[1841.60 → 1845.80] They're all cool projects, and it's, it's interesting how similar and different they all are at the same
[1845.80 → 1846.14] time.
[1846.46 → 1851.00] We've also been asked to, to kind of rehash the whole no SQL Smackdown too.
[1851.56 → 1853.12] You know, I have to host another one of those.
[1854.52 → 1855.80] Well, thanks for taking the time.
[1855.96 → 1860.90] Thanks for contributing to the changelog, Steve, and, uh, looking forward to the posts that you
[1860.90 → 1864.36] have forthcoming and, uh, more about Hacking Hack.
[1864.60 → 1864.76] Yeah.
[1864.76 → 1865.42] Thanks for having me.
[1865.44 → 1866.72] It's been a lot of fun so far.
[1866.84 → 1872.16] And, uh, you know, you guys, I'm glad to, to be a part of this cool stuff that you guys
[1872.16 → 1872.50] are doing.
[1872.50 → 1875.42] I think that it's, it's, uh, great to be able to find out about new projects.
[1875.42 → 1876.38] I'm always on the lookout.
[1876.38 → 1877.32] So it's good.
[1877.32 → 1907.30] We'll be right back.
[1907.32 → 1937.30] We'll be right back.
