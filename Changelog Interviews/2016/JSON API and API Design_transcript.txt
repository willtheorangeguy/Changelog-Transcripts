[0.00 --> 2.32]  I'm Yehuda Katz, and you're listening to The Change Log.
[11.44 --> 15.12]  Welcome back, everyone. This is The Change Log, and I'm your host, Adam Stachowiak.
[15.22 --> 20.80]  This is episode 189, and what a show it is, the first show of the year.
[21.26 --> 24.16]  Kicking it off with Yehuda Katz, talking about JSON API.
[24.44 --> 29.16]  We talked about Yehuda's past because this is the first time he's been on the show solo.
[30.00 --> 31.22]  So we had to dive deep with him.
[31.22 --> 37.12]  We talked about JSON API, JSON API compliance, resource discovery, supporting extensions,
[37.42 --> 40.48]  future-proofing API design, and so much more.
[40.94 --> 46.00]  We had three awesome sponsors, CodeShip, TopTile, and also DigitalOcean.
[46.54 --> 48.82]  Our first sponsor of the show is CodeShip.
[49.14 --> 51.56]  Head to resources.codeship.com.
[51.88 --> 58.74]  Once again, resources.codeship.com, and there you'll find all sorts of free resources from CodeShip,
[58.74 --> 65.78]  e-books, webinars, email courses, guides, all talking about continuous delivery, Docker, containers,
[66.46 --> 70.10]  getting your code to production in a workflow that makes sense for you and your team.
[70.46 --> 71.76]  We had a couple of guides that are awesome.
[71.90 --> 74.74]  Why Containers and Docker are the Future, Efficiency and Development Workflows.
[75.54 --> 79.76]  They have a couple of webinars coming up here in January this month in 2016,
[79.98 --> 83.62]  Continuous Delivery and Feature Flagging, An Introduction to Web Apps with Docker.
[83.62 --> 87.04]  Those are really awesome free webinars you can join.
[87.14 --> 91.64]  They also have this really awesome five-day email crash course on continuous delivery.
[92.08 --> 95.70]  Once again, head to resources.codeship.com.
[96.18 --> 100.12]  Enjoy all those free resources from CodeShip, and now on to the show.
[100.12 --> 109.50]  Everyone, we're here with YehudaCats.
[109.58 --> 114.18]  It is the first of the year, January 2016, so we're excited about that for one.
[114.52 --> 121.60]  But, Jared, we're here talking to Yehuda today, and we've had this show in particular on the docket for a while,
[121.66 --> 123.26]  but this recent tweet kicked it off.
[123.38 --> 124.80]  What was that tweet about?
[124.80 --> 131.22]  Yeah, that was Yehuda tweeting about JSON API, which is our conversation we'll be about today,
[131.44 --> 135.92]  where he says that you can think of JSONAPI.org as ASM.JSON,
[136.28 --> 141.28]  a low-level, consistent serialization format and protocol you can build on.
[142.14 --> 146.40]  So I'm sure we will tee that one up later in the show as a conversation point,
[146.54 --> 149.34]  but that was kind of a thought that spurred us to say,
[149.42 --> 152.86]  hey, we never had him on to talk about JSON API back when it went.
[152.86 --> 156.16]  But I think 1.0 was earlier this year.
[156.64 --> 157.42]  A few months ago, yeah.
[157.92 --> 159.24]  And so here we are.
[159.44 --> 159.72]  Here we are.
[159.84 --> 161.60]  We've had this, Yehuda, we've had this.
[161.76 --> 163.86]  So everybody, you've heard Yehuda back there in the wings there,
[163.94 --> 170.18]  but we've had this in our podcast Trello board for, I don't know, all year basically,
[170.44 --> 175.78]  all of last year technically, since we're actually recording this in 2015, published in 2016.
[176.20 --> 177.50]  So, you know.
[177.70 --> 179.66]  Hopefully we'll make it over the hump.
[179.88 --> 180.36]  There you go.
[180.36 --> 180.84]  Yeah.
[181.02 --> 188.20]  We had Yehuda and Steve Klabnik on sometime last year talking about Rust, episode 151,
[188.30 --> 189.82]  which was, yeah, April.
[190.64 --> 195.60]  And I know at that time we definitely had right next to that one in the queue was JSON API just waiting.
[195.82 --> 197.30]  So it's definitely been a while.
[198.02 --> 198.14]  Yeah.
[198.16 --> 199.70]  And Steve also works on JSON API.
[200.40 --> 202.14]  So interestingly.
[202.14 --> 206.92]  So obviously that's the main topic of the show.
[207.00 --> 208.46]  I'm sure we'll talk a little bit about Ember.
[208.60 --> 211.28]  We'll talk a little bit how those two things play in.
[211.32 --> 219.88]  And I'm sure you got some, we have a couple of questions in the wings too about JSON API and Rails 5 and playing nice together and stuff like that,
[219.92 --> 222.18]  which I'm sure is what you can talk deeply about.
[222.18 --> 228.60]  But something recently that we've done with our guests, especially someone like you, you've been on the show probably four or five times.
[228.68 --> 230.10]  Jared, I didn't even go back and count, honestly.
[231.16 --> 231.54]  Yeah, four.
[231.66 --> 232.26]  Four times.
[232.74 --> 236.44]  So we'll put all the links in the show notes to those past shows that Yehuda's been on.
[236.56 --> 239.32]  But, you know, Yehuda, we haven't had you on the show by yourself.
[239.40 --> 240.56]  So I don't know how you feel about that.
[240.58 --> 243.46]  You always come with some sort of guest or some sort of wingman, so to speak.
[244.36 --> 245.44]  What do you think about that?
[246.02 --> 253.78]  Yeah, I mean, the reason for that is that I only like to work on open source projects with other people because I don't, honestly, I just don't trust myself that much.
[254.98 --> 261.12]  And so there's always at least one other person who I'm like, well, whatever I say, the other person will have another perspective that will be useful.
[261.12 --> 267.68]  And I think if you listen to me talking with almost any other person, there's usually valuable insights that I would have just missed.
[268.22 --> 269.50]  So that's why I like to do that.
[269.54 --> 270.24]  It's just my style.
[270.24 --> 270.28]  Yeah.
[271.02 --> 274.04]  Josh, we kick off the show with the mention from Brian Liles.
[274.18 --> 279.76]  I know I got a couple of questions as well, but that was an interesting takeaway from Beyond Code up in GopherCon.
[280.32 --> 280.60]  Yeah.
[280.70 --> 284.84]  So I think, you know, we're going to spend a little time with Yehuda getting to know you from a historic perspective.
[284.84 --> 295.18]  I think we all have our own interesting roots and it's fun to find out more about the people behind the awesome open source software that we all use and love.
[295.18 --> 301.62]  We have a video series called Beyond Code, which we shoot at conference after parties.
[302.44 --> 307.72]  And season three was at GopherCon, which is still TBD on a release date on that one.
[307.96 --> 311.20]  But during that, we had Brian Liles on Beyond Code.
[311.20 --> 315.88]  And we do ask everybody in that series who their programming hero was.
[316.60 --> 317.42]  And he mentioned you.
[317.58 --> 321.78]  And so I actually pulled the quote out because I think he gave some interesting reasons as to why.
[322.36 --> 326.14]  And he also seems to be a friend of yours because he kind of takes a couple of cheap shots at the end there.
[326.14 --> 330.66]  So I was going to read this to you and have you kind of just react to it.
[331.16 --> 333.22]  So he said, Yehuda Katz is his programming hero.
[333.34 --> 338.22]  He said, the reason why is because I remember when Yehuda first started writing code and he wasn't good.
[338.52 --> 341.38]  And then he started writing more code and he wasn't good.
[341.58 --> 344.30]  But then he started writing even more code.
[344.54 --> 345.40]  And now look at him.
[345.86 --> 348.80]  Not only has he mastered Ruby, he mastered JavaScript.
[349.18 --> 350.80]  Now he runs his own company.
[351.00 --> 352.44]  And he's like this tall.
[352.66 --> 354.84]  And he kind of puts his hand at it.
[354.92 --> 355.72]  And he's kind of weird looking.
[355.72 --> 356.56]  Yes, I'm very short.
[356.64 --> 358.30]  But he's an amazing person to be around.
[359.16 --> 362.96]  So high praise from Brian along with a couple of cheap shots.
[363.20 --> 365.38]  But could you just react to that?
[365.76 --> 367.26]  Yeah, I think that's all accurate.
[367.94 --> 368.56]  I'm short.
[368.64 --> 369.16]  That is true.
[369.54 --> 371.92]  I think I'm a pretty good programmer these days.
[371.92 --> 375.04]  I also was a very bad programmer at the beginning.
[375.66 --> 378.70]  Like literally every other human being who ever starts programming.
[378.70 --> 388.02]  And I also think that the process of persevering through struggling with code is a thing that made me better.
[388.64 --> 393.18]  And I think that I try to tell that to every new person I meet who's struggling.
[393.18 --> 394.64]  It's like basically everyone.
[394.76 --> 395.48]  That's everyone's story.
[395.56 --> 397.06]  Everybody struggles with code.
[397.06 --> 399.28]  And if you think, oh, that person's cool.
[399.38 --> 400.00]  They must have had.
[400.10 --> 400.84]  It must have been easy.
[401.34 --> 403.20]  That's just like this is like a mythos.
[403.30 --> 404.46]  It's not a real thing.
[405.14 --> 405.34]  Uh-huh.
[405.92 --> 407.74]  I mean, maybe there are some people, but I don't know them.
[408.28 --> 412.02]  That's a good dovetail right into that tweet stream, Jerry, we have mentioned there.
[412.02 --> 421.58]  And Yehud, you probably know this because it was recent, but you'd mentioned the gulp between using programming to automate some repetitive tasks and being able to work on a Linux kernel.
[422.08 --> 425.24]  And you kind of dove a little bit deeper into struggle versus aptitude.
[425.68 --> 427.20]  Can you speak to those tweets?
[427.24 --> 430.50]  We have some links we'll put in the show notes, but I'm sure you can recall that.
[430.60 --> 431.04]  Yeah, I remember.
[431.22 --> 432.44]  I've been doing a few.
[432.44 --> 442.88]  I actually haven't blogged a lot recently because I sort of came to the conclusion that almost anything I have to say could be constructed as like a series of at most 10 tweets.
[443.34 --> 443.36]  So.
[444.28 --> 444.68]  There you go.
[445.12 --> 446.16]  So, yeah, I guess.
[446.40 --> 447.38]  1,400 characters, yeah.
[448.44 --> 449.62]  Yeah, confirm.
[450.40 --> 459.46]  So I guess what I was saying in that in that tweets stream is that there's I've met a lot of people over my career who have tried to program.
[459.46 --> 461.08]  Some people end up being programmers.
[461.24 --> 468.10]  Other people end up, you know, getting to have some aptitude with programming, but not necessarily being quote unquote programmers.
[468.82 --> 477.06]  And I think it's pretty damaging that we get we give off this sense of programming as like a wizardry level thing.
[477.16 --> 479.48]  Like you have to be a wizard to be useful at all.
[479.88 --> 487.04]  And I often like to tell people like so many people are very productive in Excel and Excel is a very simple programming language.
[487.04 --> 495.98]  Obviously, it's very simple, but there are functions and variables and some of the more abstract concepts that you need to do to be a programmer are already present.
[496.62 --> 499.16]  There's like some amount of variables and things like that.
[499.16 --> 505.34]  And I like to think that if you could program in Excel, that's probably not the end of the story.
[505.42 --> 507.30]  You could probably do a little bit of scripting.
[508.70 --> 518.06]  And one of the things I like to think about is when I one of the first jobs that Leah had, who I work with now at Tilda and I am married to.
[518.06 --> 519.94]  And I met her in college.
[521.22 --> 526.62]  But one of the first jobs that she did was a marketing job at a company.
[526.92 --> 532.02]  And she was basically told like every single day you're going to get an email from one automated system.
[532.26 --> 537.86]  And what you're going to do with it is you're going to open it up in Excel, make some changes to it and then email it to another automated system.
[538.36 --> 540.20]  She came home and told me this story.
[540.20 --> 546.90]  And I said, first of all, can you find out like why the person in the first automated system can't just email the second automated system and change the format?
[547.44 --> 555.10]  And so she came back like the next day and she said, I asked them and they told me like they can do it, but it will be like six months to schedule it or whatever.
[555.26 --> 556.72]  And I was like, OK, that seems terrible.
[556.72 --> 575.30]  But then I said, well, why don't we just use Ruby to, you know, pull the mailing in the mailbox, get the CSV file, use like the CSV library to make the translation and then just use the Ruby 132 API to send an email to the second system.
[576.04 --> 577.20]  And we wrote that code.
[577.78 --> 581.10]  And that saved her like some non-trivial amount of time every day.
[581.22 --> 585.30]  Like every day she was supposed to do this very annoying repetitive task and we were able to script it away.
[585.30 --> 589.48]  And I guess I just think that there is a lot more of that.
[589.64 --> 593.86]  I think like Ruby and Perl and Bash are scripting languages.
[594.76 --> 600.52]  And really what that originally meant was like you could use them to write little scripts, like little 20 line scripts.
[600.76 --> 606.48]  Actually, another example of this is every year Tilda sends out like a compensation report that says what your bonus is and things like that.
[606.90 --> 614.46]  And also me and Leia wrote a thing that it's just like a giant, it's like a 50 line file that sets up a bunch of variables.
[614.46 --> 617.38]  And then evals and ERB basically.
[617.54 --> 619.18]  And every year we go in and we make some changes.
[619.34 --> 622.84]  We load a CSV file that she does in Excel, right?
[622.90 --> 626.06]  And these are all tasks that like a lot of people have.
[626.18 --> 630.08]  They have nothing to do with programming per se, but they're very good candidates for automation.
[630.54 --> 637.90]  And there's no real reason why we should tell people like if you can't see yourself being a full-time professional Rails developer, you can't, you shouldn't even think about programming.
[637.90 --> 644.98]  Programming, there's a big slope between not knowing anything, knowing Excel, knowing a little bit of scripting, and then working your way up.
[645.52 --> 650.26]  And I think a lot of people who became programmers actually entered through that path.
[651.16 --> 656.42]  And I think we should be more happy about it, about the existence of it.
[656.42 --> 659.24]  I mean, I think, I just want to give my amen to that.
[659.44 --> 667.00]  I think automation is kind of a gateway drug into, you know, more formal programming things.
[667.24 --> 673.18]  I know when I first started in college, I was studying MIT, MIT Management Information, not MIT.
[673.72 --> 674.56]  I was not at MIT.
[674.72 --> 677.06]  I was studying MIS, Management Information Systems.
[677.06 --> 680.18]  And I never considered myself a programmer or developer.
[680.32 --> 682.58]  I just thought of myself as like someone who likes to automate things.
[682.66 --> 685.28]  And I was using Perl and just scripting little things away.
[686.10 --> 692.86]  And when you see the benefit of that, especially when it saves you five minutes a day and it can save you somebody half an hour a day,
[693.54 --> 699.26]  that's something that you think, hmm, I can take this to the next level and you start having new ideas.
[700.66 --> 702.02]  And before you know you have an app.
[702.66 --> 703.26]  Yeah, exactly.
[703.64 --> 705.20]  Eventually, you have a big thing you need to make.
[705.20 --> 709.76]  As long as you're not, I mean, as long as you're not convinced that the thing you have done is divorced from programming,
[709.94 --> 713.82]  which when we get to my story eventually, I will still explain the connection.
[713.94 --> 718.16]  Yeah, well, let's get to that because you said that you were writing programs when you were eight years old,
[718.16 --> 721.76]  but you were convinced that you didn't have the aptitude for it.
[721.96 --> 722.74]  Can you tell us that story?
[723.18 --> 727.78]  Yeah, so I guess it's pretty connected to this other thing, which is, so I was a kid.
[727.78 --> 733.08]  My father had done submarine simulators for the Air Force like in the 60s.
[733.08 --> 737.12]  So, and I would say that that was not considered like a programming job.
[737.18 --> 739.60]  It was more of like a hardware work with your hands.
[739.98 --> 745.60]  But like, you know, building a computer or anything like that involves a certain amount of technical acumen.
[746.32 --> 750.78]  And so my father in the 80s, which is after I was born.
[751.22 --> 752.32]  I'm very old, I know.
[752.32 --> 759.58]  My father in the 80s was, had his own like hardware shop where he would basically repair people's computers.
[760.40 --> 764.90]  And because of that, when I was born in 82, I already had a computer.
[765.06 --> 767.32]  I had an 8088 and that was the computer.
[767.48 --> 768.48]  We didn't have so much money.
[768.58 --> 774.04]  So that was the computer we had for some number of years, well after its theoretical shelf life.
[774.04 --> 784.16]  And I don't know if people remember this, but DOS, like some middle versions of DOS started coming with QBasic.
[784.56 --> 787.82]  So there was GWBasic, which was like this thing where you had to type the line numbers.
[788.44 --> 792.06]  So you'd be like 10, print whatever, 20, print whatever.
[792.50 --> 799.24]  And then you always would like, the rule was that you would always leave some amount of space between your line numbers in case you want to go back later and add more things.
[799.24 --> 804.74]  So if you're like, oh, I want to put something in between the first line and the second line, you better have enough numbers left so you can go 15.
[805.54 --> 810.92]  And like if you became like a serious business GWBasic programmer, you would do like 100 or 1,000.
[811.10 --> 813.24]  So you always would have enough space to put stuff into.
[814.06 --> 814.38]  That's funny.
[815.06 --> 815.30]  Yep.
[815.96 --> 817.82]  So GWBasic was a thing.
[817.96 --> 821.00]  But I would say because of the line number thing, it was not real.
[821.08 --> 826.06]  It felt, and there was no, you couldn't like really, most GWBasic environments were like a REPL there.
[826.06 --> 829.74]  You couldn't really save it or it was hard to save it and load it back again.
[830.94 --> 839.96]  So GWBasic was more of like a thing people would get a, if you have a Commodore 64, they would like get some magazine and they would type in the game and then they would play the game.
[840.24 --> 840.32]  Right.
[840.54 --> 843.10]  That was, that's sort of like the mythos of GWBasic.
[843.30 --> 849.96]  But QBasic was, stands for Quick Basic, came with DOS and you could like write your file and save your file.
[850.44 --> 854.58]  And you have five and you were now, you know, like a full screen thing that ran your program.
[854.58 --> 861.40]  So you could, and it had like, so it didn't have really a lot of control structures, but it had GoTo, which is actually sufficient to do most things.
[861.88 --> 863.60]  And it also had like a few graphics routines.
[863.72 --> 865.04]  You could make circles and squares.
[865.24 --> 869.62]  And I would say it was probably at a similar level of abstraction as like Canvas, the Canvas tag.
[869.78 --> 871.68]  You could draw some basic shapes.
[871.78 --> 877.50]  And if you want to draw anything complicated, you had to animate by wiping the screen and writing, drawing the next screen.
[877.50 --> 881.64]  But as Canvas shows, that is in fact sufficient to do all the things.
[882.82 --> 888.22]  And I guess when I was eight years old, I found this fascinating and I made like some very basic games.
[888.46 --> 890.48]  The one I remember the most was called Carnival.
[890.60 --> 897.28]  And it was like the most, the thing I was most proud of was I had a game where like something would move back and forth along the bottom.
[897.28 --> 902.84]  And you had to like hit spacebar to get it to go into like a basketball hoop that was painted at the other side of the screen.
[903.24 --> 905.00]  And like my family would play it.
[905.62 --> 917.68]  So in retrospect, the fact that I was using GoTo and like effectively Canvas primitives to draw a animated graphic game when I was eight seems like probably a good indication that I know how to program.
[917.68 --> 922.92]  But at the time I was like, okay, well, QBasic has, first of all, it's interpreted.
[923.18 --> 925.78]  So there, I didn't know that, but I knew you have to hit F5.
[925.98 --> 926.68]  And it was annoying.
[926.82 --> 929.96]  I didn't know how to make the game not require that.
[930.86 --> 937.10]  Although eventually I discovered that there was like a QBasic compiler, but I didn't really know how to reliably have access to it.
[939.74 --> 941.64]  And I was like, oh, I want to learn more things.
[941.72 --> 943.22]  This seems like it's like pretty limited.
[943.22 --> 949.06]  And somebody gave me a book on C, which was like, oh, here's the next step.
[949.12 --> 950.76]  After QBasic, what you should do is learn C.
[950.88 --> 954.08]  And I was like, I literally have no idea anything that's going on here.
[954.38 --> 957.98]  But what I've been told is like QBasic is a toy programming language.
[958.10 --> 959.70]  C is like the real programming language.
[960.10 --> 968.92]  And obviously, since I have no idea what's going on with the C book, which I think the book I was given was the KNRC book, which pretty much is not an appropriate book for a small child.
[968.92 --> 977.22]  I was I basically just came to the conclusion in my head that like, oh, I can I'm good enough to like program toy things.
[977.34 --> 980.36]  But I basically do not have the aptitude to program anything serious.
[980.36 --> 985.88]  There was no like good bridge between the stuff that I already knew how to program and quote unquote real programming.
[985.88 --> 989.82]  So at that point, I gave up programming for like a while.
[990.32 --> 994.76]  And then I went back, I would say like in my teens, I programmed again.
[994.76 --> 995.86]  And this is like embarrassing.
[995.86 --> 999.78]  But the thing I was programming was a stardate calculator for Star Trek.
[1000.46 --> 1000.90]  Nice.
[1001.58 --> 1003.14]  I like found online.
[1003.34 --> 1004.56]  I was online pretty early.
[1004.64 --> 1013.84]  I found online like a fact that like someone had done all the work to reverse engineer all the stardate algorithm for every single era of Star Trek.
[1013.84 --> 1015.08]  And I was like, oh, that seems cool.
[1015.14 --> 1016.32]  Let me like make software out of it.
[1016.58 --> 1020.76]  And I use Visual Basic 6, which a lot of people still have fond memories of.
[1021.92 --> 1027.74]  And Visual Basic 6 is basically like a WYSIWYG programming environment.
[1027.74 --> 1031.84]  But you can like double click on any part of the any UI element.
[1031.96 --> 1039.04]  And then you can say effectively attach an event handler to the to that UI element by just visually.
[1039.22 --> 1039.34]  Right.
[1039.34 --> 1046.60]  So you have to write the code to say what it does, but you don't have to do the work of like wiring up the event handler to the visual element.
[1046.60 --> 1051.78]  And the actual visual work is done is done using a UI.
[1052.14 --> 1052.26]  Right.
[1052.34 --> 1055.02]  So you could sort of think of it as Interface Builder.
[1055.58 --> 1060.84]  But in Interface Builder, you still have to do like write the code in the text part.
[1060.84 --> 1066.84]  And then you have to like drag the arrow or drag the line from the UI element to the text part.
[1067.20 --> 1070.36]  Whereas in Visual Basic, you would write through the UI part.
[1070.44 --> 1074.74]  And then instead of having to like also write the text part, you would just double click on it.
[1074.78 --> 1079.54]  And it would effectively scaffold out the part that Interface Builder makes you do manually.
[1080.04 --> 1083.54]  So it was it was very I would say it was very easy to use.
[1083.54 --> 1088.90]  And I was able to like the algorithm, as you can imagine, it's not very complicated.
[1089.36 --> 1091.86]  So I was able to write it in Visual Basic.
[1092.12 --> 1095.64]  And at that point, it felt pretty similar to my GW to my QBasic time.
[1095.74 --> 1095.86]  Right.
[1095.86 --> 1099.76]  It was like it's pretty clear that it's like a toy environment.
[1100.40 --> 1103.66]  But now the toy environment has gotten better.
[1103.66 --> 1110.90]  So I can do like I can basically get more done with the amount of work that I already with the simple programming that I already know how to do.
[1111.38 --> 1114.44]  But then equivalently, I eventually was like, this seems pretty annoying.
[1114.54 --> 1115.50]  I want to do more things.
[1115.88 --> 1119.44]  And what I was told at the time was like, well, the next step is to learn the Win32 API.
[1120.10 --> 1122.28]  And I went to look at the Win32 API.
[1122.48 --> 1125.64]  And if anybody wants to look at it, it is horrifically terrible.
[1126.42 --> 1127.92]  And well, it's not it's not terrible.
[1127.98 --> 1129.44]  It's just like equivalently very low level.
[1129.72 --> 1129.84]  Right.
[1129.92 --> 1132.10]  So you very dense, hard to understand.
[1132.10 --> 1136.68]  Similar to your C, you know, to the experience you had in your A with C compared to GW.
[1136.68 --> 1136.98]  Exactly.
[1137.40 --> 1141.70]  And the Win32 API is like it's basically like you have this top level switch statement.
[1142.14 --> 1147.30]  And every action that happens is basically running, like telling that switch statement what to do.
[1147.40 --> 1150.12]  And it has to do low level things like drawing boxes.
[1150.12 --> 1159.78]  And it's just it's basically a massive loop between like the nice environment of Visual Basic and the quote unquote serious programming that you do with Win32.
[1159.78 --> 1163.94]  So, again, when in my teens, I was like, well, that's that was fun and all.
[1164.32 --> 1166.80]  But it doesn't really I don't seem to have the aptitude.
[1166.98 --> 1168.10]  I'm no longer eight years old.
[1168.48 --> 1169.68]  Basically, the same thing is happening.
[1169.68 --> 1172.32]  So I'm pretty sure I just should not do this.
[1172.32 --> 1176.80]  So what I guess when did the professional time happen for you then?
[1176.86 --> 1178.52]  Like, was it a struggle for you?
[1178.60 --> 1180.34]  I know you talked about struggle and aptitude there.
[1180.78 --> 1184.86]  And you said that the idea of struggle doesn't mean that you don't have the aptitude.
[1185.06 --> 1188.06]  It's, you know, anybody who's learning to program is going to have some sort of struggle.
[1188.10 --> 1188.80]  That's a good thing.
[1189.18 --> 1189.30]  Yeah.
[1189.30 --> 1194.26]  So what was the how did things progress for you to get into professional, I guess, programming?
[1194.70 --> 1196.30]  So what basically happened is I just gave up.
[1196.34 --> 1201.84]  I was like, OK, I like basically know the equivalent of like very, very light scripting, but I can't really program.
[1201.84 --> 1206.24]  So I and in college, I could have been a CS major, but I was like, it doesn't really seem like it's for me.
[1206.34 --> 1209.72]  And I ended up doing a bunch of other stuff, accounting and journalism.
[1210.56 --> 1213.80]  But journalism in college ended up teaching me design.
[1213.80 --> 1224.52]  So I learned I basically did newspaper design in college and then I got my first job out of college as a web designer from a person who didn't really understand that web design and print design are not the same thing.
[1225.44 --> 1227.74]  And I also didn't know that at the time, as it turns out.
[1228.58 --> 1234.88]  So I was basically given a job to do what I thought was a like pretty straightforward design task that ended up actually being a programming job.
[1235.58 --> 1240.12]  And I was like, oh, shit, if I want to keep my job, I actually need to learn programming.
[1240.52 --> 1241.62]  So I had no choice.
[1241.62 --> 1250.90]  And I was the way the reason I ended up succeeding was because I was given a couple of applications that people have had already written in ColdFusion and PHP.
[1251.62 --> 1254.50]  And I was told, like, please update this application for this year.
[1254.60 --> 1265.46]  So it was a nonprofit and the nonprofit had like these dinners and they were like, OK, we will we basically have an application that lets you pay for your dinner ticket and perhaps ask for additional items.
[1265.46 --> 1267.12]  It was like not not totally trivial.
[1267.54 --> 1270.68]  And they were like, please update it for the changes that we want to make for this year.
[1270.68 --> 1277.68]  So, of course, I was able to go in there and either in ColdFusion or PHP, I was able to make the changes because that kind of thing is not so complicated.
[1278.20 --> 1283.14]  But I often was when I was doing that, I was like, oh, well, it seems annoying that you have this giant form.
[1283.14 --> 1285.50]  And like every time you click next, you have to go back to the server.
[1285.90 --> 1288.16]  So maybe I could find a way to make it more interactive.
[1289.04 --> 1290.82]  Again, I was like thinking about it as a designer.
[1290.82 --> 1294.96]  And I was like this was like right around the time Ajax had become a thing.
[1295.20 --> 1296.66]  I was like, oh, there's this Ajax thing.
[1296.74 --> 1297.80]  I should probably learn that.
[1297.90 --> 1299.20]  Maybe that will help me do it.
[1299.46 --> 1306.74]  I was like very enamored at the time of like the idea of constructing forms that progressively revealed themselves based on the previous information.
[1306.74 --> 1316.96]  And the thing that I really was most angry about that still annoys me is the fact that you would have to put in your city, state and zip code a lot of times.
[1316.96 --> 1320.26]  And I was like, if you put in your zip code, you can derive the city and state.
[1320.34 --> 1322.02]  Why are you making me type all these three things?
[1322.84 --> 1324.36]  And I basically didn't really know how to do it.
[1324.38 --> 1327.20]  But I was like, I'm pretty confident that this is not actually necessary.
[1327.90 --> 1330.00]  Was that the first library you wrote then?
[1330.82 --> 1334.32]  I wouldn't say that it was a library, but I figured out how to like download.
[1334.44 --> 1338.32]  At the time, there was no libraries really for any of the languages I was writing.
[1338.60 --> 1343.60]  But I was able to like download and access database of the city, state and zips.
[1343.60 --> 1349.90]  And I was able to figure out how to get it to reveal its secrets to me and not force me to do the thing.
[1349.96 --> 1352.34]  And then I learned Ajax, so I didn't have to reload the page and things like that.
[1352.68 --> 1354.68]  So that was sort of how I got started with programming.
[1354.68 --> 1360.86]  But then I was like, well, I can't like learning Ajax, quote unquote Ajax all by myself seems very hard.
[1360.98 --> 1363.30]  I'm the internet was not so good at the time.
[1363.44 --> 1367.72]  There was experts exchange was like the most popular thing.
[1367.78 --> 1369.32]  And it was like constantly asking me to pay.
[1369.58 --> 1372.02]  I just didn't feel like I was getting a lot of traction.
[1372.28 --> 1377.12]  So I took this class by Thomas Fuchs, which is like about Ajax.
[1377.80 --> 1382.36]  And I effectively, by the time I took that course, I knew most of the things that was in the course.
[1382.40 --> 1383.40]  It was actually a course on prototype.
[1383.40 --> 1388.00]  But at the very end of the course, he was like, by the way, if you want this to be easier, you could use Rails.
[1388.18 --> 1389.80]  Like Rails will be easier for you.
[1389.86 --> 1394.36]  So you might want I didn't want to force you to use Rails in this course, but probably be a good thing to investigate.
[1394.94 --> 1397.32]  And I don't know how many people actually did in that course.
[1397.32 --> 1399.84]  But I was like, well, if it's easier, sounds better to me.
[1400.34 --> 1401.76]  So I'll investigate that.
[1401.84 --> 1402.60]  And then I did.
[1402.96 --> 1412.06]  And I would say that was basically the beginning of me being an actual program where I was like, oh, well, now I was able to basically build a CMS system for that company without really knowing how to program.
[1412.06 --> 1415.20]  Which I don't know how true that is of Rails today.
[1415.32 --> 1417.80]  I think Rails has become a trickier starting target.
[1418.12 --> 1420.00]  But at the time, there weren't even migrations.
[1420.14 --> 1423.62]  You just like go into a WYSIWYG editor, like change your database schema.
[1424.52 --> 1426.08]  You would like make whatever changes.
[1426.76 --> 1431.04]  And then it was just like you have to know HTML and like a very tiny bit of Ruby to do things.
[1431.04 --> 1433.82]  And I was and I sort of knew access.
[1434.00 --> 1436.14]  So I had like the right proximate mental model for it.
[1436.42 --> 1437.82]  And I was I was able to do that.
[1438.04 --> 1440.82]  And that basically made me feel like massively empowered.
[1440.98 --> 1446.58]  Like in the past, every time I had done this toy thing, it was like basically not a real application.
[1446.64 --> 1447.54]  I wasn't getting paid for it.
[1447.64 --> 1452.42]  And it was like whether or not, you know, the CMS I built was like serious programming or not.
[1452.60 --> 1454.56]  The fact of the matter is somebody is running a real business.
[1454.70 --> 1455.84]  You built something real.
[1455.92 --> 1456.62]  Somebody used it.
[1456.68 --> 1457.56]  They put it in production.
[1457.68 --> 1458.58]  They made money from it.
[1458.58 --> 1459.06]  Yeah.
[1459.06 --> 1459.14]  Yeah.
[1459.38 --> 1460.20]  And so that's awesome.
[1460.70 --> 1469.64]  So that basically made me feel like, well, whether like I didn't it didn't make me have to think a lot about whether or not the programming I was writing was real or not, because it was being used for something real.
[1470.72 --> 1475.96]  Does that tailor into your opening the open source box, so to speak?
[1476.04 --> 1479.16]  I mean, you're pretty prolific in open source now.
[1479.22 --> 1484.12]  It sounds like prototype Thomas and Rails was sort of an entry point to you.
[1484.12 --> 1488.46]  What was the very first thing you did in open source that started to take you down the road you've been going down?
[1488.90 --> 1490.60]  So the first thing actually was not Rails.
[1490.76 --> 1494.76]  The first, I basically learned Rails and jQuery at the same time.
[1495.98 --> 1503.52]  I found jQuery because I was looking, there was some, something that would like have been the equivalent of Hacker News, but I can never remember.
[1503.62 --> 1509.14]  It might have been like, it might have been Slashdot, but I actually don't remember it being Slashdot, so I don't really know.
[1509.14 --> 1512.68]  There was some website that was like, you should check out this UI.
[1512.92 --> 1517.40]  You can like, you can construct a thing that is like the finder that lets you select icons from a grid.
[1517.92 --> 1519.26]  And I was like, wow, that's pretty cool.
[1519.30 --> 1520.48]  I didn't know you could do that on the web.
[1520.56 --> 1524.94]  And I looked at it and it was built using this library called Interface, which was built on top of jQuery at the time.
[1525.16 --> 1526.62]  It's like the precursor to jQuery UI.
[1526.82 --> 1528.66]  And I was like, wow, jQuery can do that.
[1528.70 --> 1529.46]  That seems pretty cool.
[1529.46 --> 1531.36]  So I looked more into jQuery.
[1531.70 --> 1547.80]  And the problem I had at the time was that jQuery, while very cool, was basically documented by John's writing documentation on the wiki at his leisure, which, as you can imagine, is not very likely to be up to date, especially since jQuery itself was pre-1.0.
[1548.60 --> 1550.78]  Not only was it pre-1.0, it just had no versions.
[1551.04 --> 1554.98]  Every so often, John would put a tarball or a zip file on his blog.
[1555.18 --> 1556.40]  Like, here's a new version of jQuery.
[1556.98 --> 1559.26]  And I was like, I really think we could do better than this.
[1560.04 --> 1567.48]  What if instead of you writing things on the wiki, what if you gave me at the time, like this was 2005, so don't laugh.
[1567.64 --> 1569.08]  But what if you gave me an XML dump?
[1569.40 --> 1571.84]  Like, what if you gave me an XML dump of the documentation?
[1572.34 --> 1575.50]  There already were, like, tools that would automatically generate inline docs.
[1575.68 --> 1581.06]  If you give me the XML dump, I will basically do the work to make a, like, automatic website.
[1581.34 --> 1585.40]  And I used XSLT at the time to, like, convert it into something visually appealing.
[1585.40 --> 1593.66]  And so I was basically, I, like, kind of owned the documentation effort for a little while in jQuery just because there was no one else doing it.
[1593.66 --> 1601.88]  And I was feeling like, I guess, I have no idea how I, why I felt like this, but I felt like this should be easier.
[1602.00 --> 1604.10]  There should be, basically everything is in place.
[1604.18 --> 1606.14]  Someone just has to, like, glue it all together.
[1606.14 --> 1613.20]  And then if you glue it all together, then you have automatically up-to-date documentation for every version of jQuery ever just because someone wrote inline docs.
[1613.48 --> 1614.76]  And I felt like that was cool.
[1615.20 --> 1619.30]  So I would say that that was probably the first real open source thing I did.
[1619.42 --> 1624.84]  And the reason, like, the gateway drug for me was just that thing was massively high leverage, right?
[1624.88 --> 1630.72]  Like, before, people would come and they would look at jQuery and they would bounce right off because they couldn't figure out what the rules were.
[1630.72 --> 1635.58]  But then as soon as there was any documentation on the internet, all of a sudden, tons of people stopped bouncing off of it.
[1635.84 --> 1637.40]  Yeah, I can recall those days, actually.
[1637.58 --> 1642.26]  I mean, I remember just, there was a couple other different things happening around then, obviously, product that was around.
[1642.40 --> 1649.84]  But it felt, as someone who came from a front-end perspective, which you could probably lament a little bit about this, with an HTML, CSS background,
[1650.38 --> 1653.92]  Sass wasn't even invented yet, or it might have just been invented, but it wasn't.
[1653.92 --> 1654.54]  Not quite yet.
[1654.54 --> 1656.96]  It was only in Ruby, you know, very different than it is today.
[1656.96 --> 1663.30]  You know, there was no easy path that I could find at the time into this JavaScript world.
[1664.02 --> 1667.86]  But I remember when jQuery had docs, it was actually quite a bit easier to get into it.
[1667.88 --> 1670.50]  I was like, okay, now I feel like I can actually do something with this.
[1670.80 --> 1676.10]  There was this library called Rico at the time, which I actually was like, that Rico actually seems pretty cool.
[1676.16 --> 1676.82]  I want to use it.
[1676.96 --> 1678.04]  Like, the demos are really good.
[1678.32 --> 1681.68]  And every single time I would try to use it, I was like, I literally have no idea how you're supposed to.
[1681.82 --> 1685.74]  It seems cool, and I can look at the source, but I do not know how you're supposed to actually use this.
[1685.74 --> 1687.68]  And I bounced off of it a bunch of times.
[1688.68 --> 1693.36]  And I guess that was sort of the epiphany that I had as a person in the world.
[1693.70 --> 1697.42]  Like, if there are things that are so close, like, think about it.
[1697.42 --> 1699.30]  I basically didn't know how to program at all at this point.
[1699.60 --> 1705.24]  I would say that I effectively had, like, the level of programming that you have when you're writing Excel at this point.
[1705.24 --> 1713.94]  But I was able to figure out how to take documentation that other people had already written and tools that other people had already written to generate the XML version.
[1714.10 --> 1718.52]  And then XSLT, which was pretty declarative and didn't require a lot of programming skill.
[1718.60 --> 1723.52]  And I could take all that and put it together into a thing that enabled a ton of people to use jQuery.
[1723.84 --> 1726.70]  And I felt like, wow, that is massively high leverage.
[1726.76 --> 1730.58]  You can, like, change a lot of people's lives easily, quickly with open source.
[1730.58 --> 1735.30]  And that basically, that's sort of been my guiding worldview ever since.
[1735.46 --> 1742.46]  Like, how do you take people who basically don't necessarily, who are bouncing off of things, and how do you enable them to do more?
[1742.98 --> 1743.20]  Yeah.
[1743.44 --> 1744.28]  It's rough.
[1745.08 --> 1747.26]  It's an interesting thing, too.
[1748.28 --> 1754.54]  Hearing your background on automation, it seems like you have a true passion slash addiction with it.
[1754.56 --> 1755.84]  I'm not really sure how to phrase that.
[1756.22 --> 1758.58]  But it totally makes sense that you wrote Thor.
[1758.58 --> 1758.98]  Yeah.
[1760.18 --> 1767.00]  Yeah, Thor was definitely, I wrote Thor, like, after writing a bunch of CLIs and saying, why is this?
[1767.20 --> 1771.78]  I guess one of my things about open source in general is there's so many things that are, like, so close.
[1772.24 --> 1781.56]  Like, somebody just has to, the difference between where we are now, which is, like, almost nobody can use it, and it being usable by a huge amount of people is often such a tiny gap.
[1781.64 --> 1782.84]  Someone just has to spend the time.
[1782.84 --> 1788.62]  And so many people just, like, there's such a failure of imagination so often about what the gap looks like.
[1788.82 --> 1796.64]  So a lot of times people will try something, and they'll have that experience for some reason or other, and they'll just say, this entire idea is a bad idea.
[1796.86 --> 1798.42]  This entire idea is done.
[1798.42 --> 1805.06]  And really, all that is needed to make it feel better is, like, small things that me 10 years ago could have done.
[1805.90 --> 1806.06]  Right?
[1806.16 --> 1807.18]  Someone has to just do it.
[1807.18 --> 1809.22]  So one more thing we have to mention.
[1809.34 --> 1810.88]  Obviously, we can go on and on.
[1810.94 --> 1817.10]  You have a deep past with programming in open source, and obviously, we'd love to hear all about your past.
[1817.46 --> 1827.68]  One thing I want to talk about before we go into our first break is what I'm calling, I think, might be your brand purpose, your personal brand purpose.
[1827.68 --> 1842.26]  And at November this year, I think it was either this year or last year, I'm not sure which it was, but you said sometime during your talk, and I took this note down, I don't think you made it explicit that this was your brand purpose, but I want to ask you what you think about this before we transition into this break.
[1842.56 --> 1844.64]  But you said build things that empower people.
[1844.64 --> 1858.24]  And it seems like, you know, rewinding back to your beginning through to your initial comfortable feeling of being a programmer and then moving into open source like you've been doing, that that's been your mantra, that's been what you do.
[1858.28 --> 1860.10]  What do you think about building things that empower people?
[1860.64 --> 1861.88]  I think that's, I would agree.
[1861.98 --> 1868.14]  I also agree that I was, it was this year, I also agree it was not so explicit as a, like, me waving the flag around it.
[1868.14 --> 1874.72]  But I think that open source does a lot of things for a lot of people, and I think it's good.
[1874.88 --> 1883.18]  But for me, the main thing to do with open source is to find places where the gap between someone being empowered and not being empowered is small and just closing it.
[1883.18 --> 1893.24]  And unfortunately, for like, at this point in my career, the gaps, the gaps that are, that are, that are still good cost benefit for me are usually much bigger.
[1893.56 --> 1899.92]  But there's still, like, I'm not, I'm never going to be, I mean, maybe someday, but right now I'm never going to, like, invent the Rust programming language.
[1900.52 --> 1903.82]  Because it's like the level of low levelness is too much for me.
[1903.82 --> 1917.46]  But the gap between, like, Rust being a good thing for servo, like a web browser, and being good for Ruby programmers is actually much smaller than the gap between, like, not having Rust in the world and having it at all.
[1917.88 --> 1930.38]  And so I, a lot of what I try to do in my, like, with my open source work is to try to find things where either, like, the fact that something hasn't been invented yet is for a stupid reason, like Thor or Ember.
[1930.38 --> 1938.62]  Or, or there's something that exists in the world, but it's just inaccessible for some reason, like the jQuery doc story or Rust.
[1939.20 --> 1947.18]  Like, thinking about, okay, what can we do to make this a thing that a lot of people, a lot more people can use to do something powerful?
[1948.08 --> 1952.26]  And I just think not enough people think about it.
[1952.32 --> 1957.30]  And more concerningly, and this was also in my Nodevember talk, a lot of people are just pretty cynical about the whole thing.
[1957.30 --> 1960.88]  A lot of people are pretty cynical about the level of complexity in programming.
[1961.02 --> 1967.98]  A lot of people are pretty cynical about how likely you are to find a good solution for these things.
[1968.18 --> 1979.50]  A lot of people are pretty cynical about the power of, like, the power of these things in the first place to change what, to change the nature of what people can do, right?
[1979.50 --> 1985.26]  And I'm very optimistic about being able to change the nature of what a particular person can do at a particular time.
[1985.70 --> 1988.30]  And, but that requires believing in it.
[1988.38 --> 1991.14]  And I think, unfortunately, a lot of people don't always believe in it.
[1991.92 --> 2004.80]  Well, I think on the other side of the break, we want to take these thoughts, the empowering people, and the finding the gaps between empowerment and non-empowerment, and use those to cast a light on your work with JSON API.
[2004.80 --> 2007.30]  So we'll ask you about that on the other side.
[2007.36 --> 2007.88]  We'll be right back.
[2008.56 --> 2010.44]  We know you listen to other podcasts.
[2010.56 --> 2010.94]  Don't worry.
[2011.02 --> 2011.62]  We're not upset.
[2012.06 --> 2015.18]  We know that ChangeLog isn't the only podcast in your list.
[2015.60 --> 2016.08]  And you know what?
[2016.32 --> 2023.92]  You may have heard advertisements on other shows about other hiring platforms and other places like our friends at TopTow.
[2024.06 --> 2030.24]  But let me tell you, there is no match to how invested TopTow is to both sides of the equation.
[2030.24 --> 2039.26]  You have companies out there who need great engineers, great designers, and you have great designers and great engineers out there needing great opportunities.
[2039.56 --> 2048.20]  And TopTow plays both sides of that fence very well, helping make sure the right kind of opportunities are there and the right kind of developers and designers are there.
[2048.20 --> 2060.30]  And if you're a CTO listening to this or someone on a team who knows you need to expand and add more people to help reach your goals, TopTow is the best place to go and find the best designers and the best engineers out there.
[2060.30 --> 2074.44]  And if you're one of those best engineers or best designers looking for great places to do great work and freelance and travel the world and have a lot of freedom, but also have the same kind of support you would want from working somewhere, TopTow is that place.
[2074.52 --> 2075.40]  You can blog with them.
[2075.64 --> 2076.88]  You can travel the world with them.
[2077.10 --> 2078.72]  They have meetups all around the world.
[2079.06 --> 2089.34]  They absolutely love to encourage and to support and help their developers and the designers that are in their network all around the world grow and be better and do better.
[2089.34 --> 2091.72]  Head to TopTow.com to find out more.
[2091.94 --> 2095.24]  That's T-O-P-T-A-L.com.
[2095.52 --> 2098.22]  Once again, T-O-P-T-A-L.com.
[2098.48 --> 2109.86]  But if you want a personal introduction on either side of the fence, whether it's an introduction to find the best designers and developers, or if you're a designer developer looking for great opportunities, get in touch with me.
[2109.98 --> 2111.86]  I'd be glad to give you a personal introduction.
[2112.30 --> 2115.48]  Email me at adam at changelaw.com.
[2115.60 --> 2116.84]  And now back to the show.
[2119.34 --> 2121.08]  All right.
[2121.08 --> 2124.14]  We are back talking with Yehuda Katz about JSON API.
[2124.14 --> 2128.70]  And before the break, we laid out, Yehuda, how you just try to do two things.
[2128.88 --> 2132.40]  The main purpose is to empower people with open source.
[2132.78 --> 2138.14]  And kind of the way you go about that is by finding these gaps between empowerment and non-empowerment.
[2138.20 --> 2140.52]  And hopefully find ones that are easy to bridge.
[2140.52 --> 2144.42]  Probably they're getting harder and harder to bridge as you get more and more advanced.
[2144.68 --> 2153.80]  And we wanted to take those thoughts and apply them to your work behind JSON API because this is something you've been involved in since, I think, May of 2013.
[2153.80 --> 2159.70]  So can you cast that light into JSON API and why it's something that you think needs to exist?
[2159.70 --> 2160.58]  Sure.
[2160.74 --> 2166.60]  So before I do that, I think it's important to understand, like, what does empowerment actually mean?
[2166.60 --> 2176.92]  And one thing that I think it's important to keep in mind is that if somebody already knows how to do something, making it easier for them to do that thing is not empowering.
[2177.48 --> 2179.04]  It might be nice.
[2179.24 --> 2180.92]  It might help them get their job done faster.
[2180.92 --> 2185.86]  But there are some ways in which that kind of thing can be empowering.
[2186.02 --> 2193.24]  But the most empowering things are taking something that somebody does not know how to do at all and then making them be able to do it.
[2193.92 --> 2200.40]  And fundamentally, in order to do that, you have to use abstractions that hide some of the details.
[2201.12 --> 2205.48]  Because pretty much nobody is going to say, like, oh, I would like to build web applications.
[2205.48 --> 2209.86]  So before I do that, let me learn HTTP and Rack and all this stuff, right?
[2209.94 --> 2219.66]  They want to – the shortest path to empowering them to be successful, like I was when I started building that CMS for my company, is to hide a lot of those details.
[2220.68 --> 2232.42]  And this is actually a fundamental conflict in open source and software zeitgeist, is whether abstracting away details is a good idea.
[2232.42 --> 2239.06]  So, for example, Joel Spolsky has this famous blog post from many years ago called The Law of Leaky Abstractions.
[2239.38 --> 2243.38]  And the idea behind this blog post is, like, you can never successfully abstract anything.
[2243.72 --> 2244.74]  It will always leak.
[2244.90 --> 2245.60]  It will always leak.
[2245.90 --> 2246.96]  So don't even bother.
[2247.34 --> 2248.46]  Everybody should just learn everything.
[2249.22 --> 2261.36]  I think this is just a silly worldview, in part because we have so – over the past 30 to 50 years, we have succeeded at abstracting so many details that it just seems, like, self-evidently incorrect.
[2261.36 --> 2268.08]  Like, whether or not, you know, TCP – which was his example in his blog post, one of them was TCP, which I think is a hilarious example.
[2268.78 --> 2274.18]  The fact that TCP might occasionally leak doesn't necessarily mean that TCP is a bad abstraction.
[2274.40 --> 2281.72]  It just means that sometimes if you're doing sufficiently advanced things, you will need to learn TCP to get the sufficiently advanced things done.
[2281.72 --> 2286.96]  But that doesn't mean that we should not have TCP and everyone should just use UDP and build their own thing.
[2287.04 --> 2295.50]  Although there's a good website called notcp.io, which is basically making a joke about this entire phenomenon of people not believing in abstractions.
[2295.50 --> 2309.24]  And I guess for me, if you're looking to empower somebody, you have to figure out what parts of the everyday, the 80-20 job that someone does, what parts of it are about things that are not very important.
[2309.24 --> 2316.96]  And interestingly, what I've also found – what I found is that when you do that analysis, quite often, it's a lot of the thing, right?
[2316.98 --> 2319.74]  It's a lot of the stuff people do, like, on a day-to-day basis.
[2319.74 --> 2328.26]  If you look at, like, what someone does when they write a backbone application, a huge amount – a huge percentage of that is something that you – that Ember doesn't make you think about.
[2328.32 --> 2330.32]  Or even React or Angular doesn't make you think about.
[2330.32 --> 2330.76]  Right?
[2331.14 --> 2343.62]  And I think – so I think when you're first looking at empowering people, what you often discover is that's sort of the natural zeitgeist, the natural worldview of how people think about whatever task it is that they're setting out to do.
[2343.76 --> 2349.84]  And what people think is, like, core and fundamental to the task they're trying to do is really pretty abstractable.
[2349.84 --> 2364.38]  I think if you're going down this path, it's important to remember that when you abstract something, you have to leave escape valves so people can go and break out into the level below if you're an advanced user and you discover things are too limiting.
[2364.98 --> 2373.00]  And I think Rails did a pretty good job at this, and Ember does it with things like didInsertElement, which allows you to basically write jQuery code in the middle of your component, right?
[2373.04 --> 2375.20]  And React has a similar hook.
[2375.64 --> 2377.30]  And I think those kinds of things are very important.
[2377.30 --> 2388.26]  But if you make your escape valves reasonably well-designed and designed to be very, very broad, what ends up happening is that people who are new can get a lot done without having to think about the escape valves.
[2388.56 --> 2393.56]  But people who are a little bit more advanced are able to use the escape valves to get the job done.
[2393.68 --> 2402.46]  So I guess this is how I think about empowerment in general is that your job is to take away a large percentage of the thing that people think is core to the experience of doing it.
[2402.46 --> 2407.50]  And I've been giving talks about what became JSON API for a long time.
[2407.60 --> 2415.84]  I gave a talk just about this in 2012 at RailsConf, which I think was called like Rails the next five years or something like that.
[2415.84 --> 2425.74]  And with JSON APIs, I think there's so many details about it have to do with format and they have to do with protocol.
[2426.58 --> 2431.46]  But somewhat interestingly, the format and the protocol cannot easily be decoupled.
[2431.46 --> 2441.28]  So if you say, well, you know, we're going to make a format, we're going to, the way we're going to make it, we're going to empower people to build JSON APIs more effectively without as much hassle.
[2441.28 --> 2445.36]  And we will allow many, many more people to build JSON APIs than can do it now.
[2445.68 --> 2451.10]  The way, if you think that you're going to do that with a format, the problem is that the format interacts in non-trivial ways with the protocol.
[2451.10 --> 2458.38]  If you do the opposite, if you say, we're going to do the protocol, which usually people are referring to when they talk about REST, they say, we're going to say, we're going to define the protocol.
[2458.62 --> 2463.64]  The problem is the protocol interacts in non-trivial ways with the format, right?
[2463.88 --> 2467.84]  And additionally, a lot of times people will say things like, oh, just use REST.
[2468.44 --> 2471.14]  But they don't actually spend any time describing what it is.
[2471.78 --> 2474.98]  It is assumed that if you're a programmer, you can figure it out.
[2475.54 --> 2480.12]  And number one, a lot of the people we're trying to empower in the first place cannot.
[2480.12 --> 2490.00]  But number two, the actual definition of something like REST is sufficiently ill-defined that it doesn't help even more advanced developers who say use REST.
[2490.10 --> 2491.18]  They have no idea what you're talking about.
[2491.66 --> 2505.26]  And I think a good example of this whole attempt failing was active resource in Rails, where DHH basically thought, and a lot of people thought, like, oh, Rails is pretty conventional.
[2505.66 --> 2508.98]  So what we'll do is we'll say you can connect to a quote-unquote conventional Rails server.
[2508.98 --> 2512.94]  And actually, I made the same mistake in the beginning of Ember Data that led me down this path.
[2513.30 --> 2520.86]  Is that Rails is sufficiently conventional that you should just be able to connect to literally any Rails server and get, like, roughly enough information to do the job.
[2521.08 --> 2527.44]  The problem is that it turns out that the specification of sufficiently similar Rails application is impossible.
[2528.50 --> 2528.62]  Right.
[2528.62 --> 2533.50]  And people do all kinds of random stuff when they're building Rails servers.
[2533.50 --> 2541.44]  So we also, because the same reason that caused DHH to make the mistake about active resource caused us to make a similar mistake in the beginning of Ember Data.
[2541.54 --> 2545.46]  We said, you know, what Ember Data will do is it will hard code to quote-unquote Rails.
[2545.98 --> 2551.82]  And, of course, that doesn't stop you from, I was overly, I made too strong of a statement there.
[2551.82 --> 2554.80]  It doesn't stop you from using the same conventions in any other system.
[2554.80 --> 2559.32]  So, you know, there's, like, the REST framework for Django and Node, of course, lets you do whatever you want.
[2559.60 --> 2565.50]  So it was more like, let's say that the Rails conventions are the Ember Data conventions and we thought that that would get us all the way.
[2566.12 --> 2572.44]  But in practice, what ended up happening is that questions came up, like, should I have a root or not?
[2572.90 --> 2575.28]  Like, should the name of my resource be in the root or not?
[2575.44 --> 2576.30]  That's a simple one.
[2576.50 --> 2578.90]  How do I include associated resources?
[2578.90 --> 2585.34]  What if I want to include just the, like, the links to the associated resources or IDs for them and then lazily load the REST ones?
[2585.38 --> 2589.62]  And these things come up very quickly, like, within a very short amount of time.
[2589.70 --> 2593.04]  It doesn't require you to be an advanced user to encounter some of these questions.
[2593.14 --> 2597.30]  It just involves you trying to do anything even pretty simple with your UI.
[2597.90 --> 2606.64]  So we ended up realizing pretty quickly by 2013 that treating Rails as a spec was not working.
[2606.64 --> 2610.88]  And so at RailsConf that year, I was bemoaning this.
[2611.04 --> 2613.42]  I give it a couple of talks about it.
[2614.12 --> 2628.30]  And Brian Ford from Rubinius, his name is now Brian, I don't know how to pronounce his last name, but it's like something like Sheree, came over to me and he said, like, the world needs to have a better specification.
[2628.42 --> 2629.18]  Could you write one down?
[2629.18 --> 2634.78]  And I said, well, what I'll try to do is I'll try to extract the implicit specification that EmberData had.
[2635.38 --> 2639.22]  Like, basically, even though Rails has no spec, EmberData has to have said something.
[2639.78 --> 2641.78]  So EmberData has implicit spec.
[2641.86 --> 2642.70]  Let me try to write it down.
[2643.28 --> 2649.40]  And so I wrote down the first version of JSON API was just effectively an extracted EmberData spec.
[2649.40 --> 2654.38]  And actually, people were, like, pretty excited about it.
[2654.40 --> 2662.76]  But one thing that we noticed after that was that even EmberData was pretty wishy-washy about a whole bunch of details because of the fact that we were trying to work against a pretty wishy-washy server.
[2663.24 --> 2667.32]  So over time, what we realized was that we needed to get pretty rigorous.
[2667.32 --> 2671.74]  We needed to have opinions about all the details.
[2673.02 --> 2688.88]  And I actually learned something important about JSON APIs and wishy-washiness, which is that a big part of the reason it turns out that people are so wishy-washy in the way they define JSON API is that JSON APIs are maximal bike-shedding opportunity.
[2689.44 --> 2694.60]  So basically, everyone looks at a particular JSON API, and they have a visceral response to the aesthetics of it.
[2694.60 --> 2707.82]  So if you are trying to get a lot of adoption for your JSON API description in some way, you have to – you're trying to figure out, like, okay, how do I make something that a lot of people will not respond negatively to?
[2708.38 --> 2711.10]  And that basically means being pretty wishy-washy.
[2711.24 --> 2712.92]  You say, oh, you could do this or you could do that.
[2713.02 --> 2714.34]  If you don't like this, you can do this other thing.
[2715.28 --> 2721.74]  But the problem with the head is that now the clients have to be willing to accept a lot of different things, which makes it harder to write the right clients.
[2721.74 --> 2736.10]  And what we discovered somewhere in the middle of the JSON API journey is that no matter how much people claim that they're willing to adopt something because it has the right aesthetics, the real value prop of something like JSON API is having good servers and clients.
[2736.10 --> 2743.16]  So we were getting a lot of people to not whine a lot about the exact aesthetics of JSON API by being pretty wishy-washy.
[2743.58 --> 2750.88]  But then every person who was actually trying to write clients would say, you know, this is – the spec seems fine, but I don't know what I'm supposed to do here.
[2751.00 --> 2754.52]  Am I supposed – you know, the server says you're allowed to use whatever status code you want here.
[2754.62 --> 2756.94]  Is that actually – like, what does that mean?
[2757.24 --> 2758.74]  What if the user gives me, like, a 422?
[2758.94 --> 2759.44]  What should I do?
[2759.44 --> 2760.04]  Yeah.
[2760.36 --> 2775.96]  Let me just real quick state something that's perhaps obvious to you and I, but just to be super clear with everybody, that the JSON API – and I'm using the word just to limit its scope, not its usefulness – but it's JSON API, the project that you've been working on that we're talking about.
[2776.34 --> 2781.40]  It is just a specification of how you ought to build JSON APIs, correct?
[2782.08 --> 2782.88]  Yes, confirmed.
[2782.88 --> 2792.24]  It is – so it's a specific – so just to be clear, it's the only specification that I know of that tells you how to build JSON APIs, both the format and the protocol.
[2792.52 --> 2798.24]  In other words, it tells you the HTTP semantics, but it also tells you what the shape of the inputs and outputs are.
[2798.24 --> 2798.76]  Of the data.
[2799.40 --> 2799.80]  Okay.
[2800.02 --> 2802.14]  And as far as I know, I'm probably wrong.
[2802.20 --> 2803.94]  There's probably some other thing that exists in the world.
[2803.94 --> 2815.04]  But as far as I know, the popular alternatives that people say, why you know how or something like that, those things are all either about a protocol or they are about a format and not both.
[2815.80 --> 2816.54]  But yes, I agree.
[2816.72 --> 2823.78]  In retrospect, probably the name JSON API has some confusing ambiguity here, and I apologize in hindsight for that.
[2823.78 --> 2824.84]  It's very Google-able, though.
[2824.92 --> 2827.12]  I mean you can Google it and find it, so that's a good thing.
[2827.34 --> 2827.52]  Yes.
[2827.60 --> 2831.66]  I mean perhaps surprisingly, but it is true that it is very Google-able.
[2831.66 --> 2839.22]  So anyway, so we basically went through this back and forth where at first we were pretty responsive to the aesthetics people.
[2840.02 --> 2849.16]  And eventually we realized that the aesthetics people were not actually adopting JSON API, but the tool builders were important for the adoption of JSON API, and they were telling us about all these issues.
[2849.16 --> 2865.26]  So about a year ago, me and Dan Gebhardt, who is probably the main editor now of the spec, sat down and in a few face-to-face sessions we hashed out what ambiguities people had reported that were making it hard to build tools, and we just made calls about all of them.
[2865.32 --> 2867.66]  We just said the answer is this, the answer is that, the answer is X.
[2867.66 --> 2873.50]  And the consequence of doing that is that now JSON API is very trollable from an aesthetics perspective.
[2873.86 --> 2876.16]  It's very easy for someone to look at it and say, I don't like that.
[2876.28 --> 2878.84]  A very common thing people say is, is this WSDL all over again?
[2879.12 --> 2884.00]  Actually, it is not WSDL because it does not have a big schema type thing and has nothing to do with that.
[2884.14 --> 2893.52]  But it's very easy to look at it and say, you know, I thought the point of JSON was to make this a very like human consumable format, but now you have like this attributes key that has a hash of attributes.
[2893.60 --> 2894.22]  Why do you need that?
[2894.22 --> 2898.32]  Well, it turns out that the reason you need that is that tools need to know the difference between attributes and associations.
[2898.92 --> 2904.80]  And saying that you'll do that by hard coding it in every client is not very good for tools, right?
[2904.82 --> 2908.76]  So there are some things that we did to try to make ambiguities less.
[2908.76 --> 2923.28]  We tried very, very hard when we made the calls to not gratuitously add things for tools that just, you know, that basically would make it a binary format or something like the ugly XML formats that people are used to seeing.
[2923.28 --> 2928.54]  But at the end of the day, there really are some ambiguities that you would like to get out in the spec.
[2928.54 --> 2940.80]  And that's sort of why I tweeted that as in that JSON thing was that JSON API is not really fundamentally about being a, it's not about being a bespoke hand rollable format.
[2941.38 --> 2945.74]  It's about being, which I think is how a lot of people think about JSON APIs, right?
[2945.78 --> 2946.26]  They look at them.
[2946.26 --> 2951.84]  They try to construct the most optimal, most aesthetically pleasing shape of their JSON.
[2952.60 --> 2961.44]  I think that the JSON, the API or the hand rolled artisanal versus, you know, XML and WSDL and these things.
[2961.44 --> 2974.36]  I think it's this, it's this, it's kind of a yin and yang that we go back and forth between a similar to like static versus dynamic type languages where you want the freedom, but then you lose the tooling and the, you know, these conventions.
[2974.36 --> 2983.98]  And I think it's, it's, it's tricky ground because everybody has opinions on it and it seems like there's no like black or white answers either way.
[2984.00 --> 2989.88]  So I think the interesting thing for Rails is that DHH seems to really come down on the artisanal side on JSON.
[2989.88 --> 2998.56]  But I think I, as a programmer, learned the right answer to this question by looking at ActiveRecord, which had a fairly similar question early on.
[2998.74 --> 3009.50]  It basically said, okay, DHH has figured out that the way you could produce the best programming experience is by not allowing you to choose whether or not your primary key is called ID and what the foreign keys are called and all this stuff, right?
[3009.52 --> 3010.86]  We're going to tell you what the answer is.
[3011.16 --> 3014.70]  And maybe, you know, a DBA is going to look at that and say, oh, that's so disgusting.
[3014.80 --> 3016.22]  I can't believe the SQL that's being admitted.
[3016.46 --> 3019.50]  And you're supposed to say in Rails, I just don't care.
[3020.34 --> 3021.86]  I'm not interested in that level of abstraction.
[3022.42 --> 3025.18]  And the story with JSON API is pretty similar, right?
[3025.22 --> 3028.10]  It says, what I want to do is I want to describe my models.
[3028.50 --> 3032.38]  And yes, there's going to be some impedance mismatch, just like there is with SQL.
[3032.82 --> 3035.44]  But I mostly want to think at the model level of abstraction.
[3035.80 --> 3041.82]  I mostly want to think about the model in something like Ember is pretty similar to like the resource concept in Rails.
[3042.28 --> 3043.58]  It's not about database tables.
[3043.98 --> 3045.18]  I want to think about models.
[3045.18 --> 3056.14]  And the fact that there's maybe, you know, maybe an extra attributes hash or extra URLs or maybe the fact that every single thing has to have a type and an ID, right?
[3056.60 --> 3061.82]  All those questions are just not – certainly you want to make sure that the format is debuggable.
[3061.82 --> 3068.52]  I think that's one of the things people don't like about more binary formats is like you look at it and you're like, as a human, I cannot figure out what this is even trying to say.
[3069.30 --> 3070.74]  And I think that's very bad for debugging.
[3071.28 --> 3078.16]  But how many – you know, do I have a type associated with every single one of my records that I have sent over this format?
[3078.16 --> 3085.48]  Those are questions that are legitimate aesthetic questions, but they are analogous to like I would really not – I don't want ID to be my primary key name.
[3086.22 --> 3087.56]  They're just not very important.
[3087.78 --> 3094.26]  And the more you hold on to saying that it's very important that you care about that, the more we push back – we leave open the big gap.
[3095.00 --> 3096.20]  So this is the empowerment thing, right?
[3096.84 --> 3104.24]  There are people who want to build stuff on the web and making them learn about handcrafting their JSON and HTTP status codes and all this stuff.
[3105.24 --> 3108.08]  Even me, when I'm trying to write apps, I don't want to be thinking about this stuff.
[3108.62 --> 3118.12]  And the fact that this is just a part, the normal part of the work of building applications means that there's just a bunch of people who can't do it or can't do it at any particular point.
[3118.22 --> 3119.42]  It's a hard weekend project.
[3119.60 --> 3122.74]  It's a hard side project for a job, right?
[3122.74 --> 3128.34]  And basically the job of JSON API and my philosophy in general is to say how much of that actually matters.
[3128.50 --> 3131.62]  And in fact, that was also the point of Rails, right?
[3131.62 --> 3138.52]  Is to say how much of the stuff that people are spending all their time on actually matters when it comes down to what your application is doing.
[3139.00 --> 3140.62]  Maybe performance really matters.
[3140.74 --> 3143.76]  Maybe you need to handcraft this thing and you can't use JSON API.
[3144.00 --> 3147.10]  But why don't you figure that out after you figure out if the thing you're building even matters?
[3147.80 --> 3147.90]  Yeah.
[3148.40 --> 3151.14]  Yeah, and I think that there are other aspects.
[3151.36 --> 3152.20]  We talk about aesthetics.
[3152.38 --> 3153.58]  You mentioned one, performance.
[3153.58 --> 3168.10]  The other thing is how well your client libraries, whether it's Ember or an iOS library or whatever it happens to be, how well that maps on top of what JSON API is speaking both in protocol and in format.
[3168.40 --> 3178.14]  So has there been a lot of give and take between not just suiting Ember's needs, but suiting an iOS library, suiting React or these types of things?
[3178.14 --> 3179.12]  Yes, absolutely.
[3179.46 --> 3186.42]  So the evolution of JSON API was that it started off being pretty extracted from Ember data.
[3186.56 --> 3187.38]  And I agree with DHH.
[3187.58 --> 3190.66]  Extracting these things is way better than trying to invent them out of your head.
[3191.22 --> 3200.46]  So it started off already being pretty useful, even just to point people at, if you're trying to build an Ember data thing, it is not documented better.
[3201.06 --> 3202.18]  So that's where it started from.
[3202.30 --> 3202.58]  Bonus.
[3202.58 --> 3202.70]  Yes.
[3203.06 --> 3203.20]  Yeah.
[3203.34 --> 3207.26]  I mean, it was like sort of documented, but mostly in the source, mostly in my comments, right?
[3208.36 --> 3209.48]  So that was already helpful.
[3209.48 --> 3215.36]  But we started getting a lot of people who weren't using Ember to say, oh, I'm trying to write an iOS client library.
[3215.48 --> 3217.38]  We already have iOS client libraries.
[3217.58 --> 3222.34]  There's already like a Java server project that lets you build JSON APIs.
[3222.48 --> 3223.24]  There's a node project.
[3223.72 --> 3230.40]  And so increasingly, as people try to use JSON API for things that were not the Rails and Ember combo, people ask for more things.
[3230.40 --> 3239.34]  And really, the philosophy of JSON API at the end of the day, like today, is that JSON API is just describing an arbitrary graph of objects serialized over the wire.
[3239.58 --> 3243.94]  And what that just means is that you have a bunch of objects, and they are linked together in some way.
[3244.10 --> 3248.44]  In order to link them in a serialized form, you need some identifier.
[3248.44 --> 3257.36]  And we chose to use the type and ID identifier as the key, in large part because servers pretty much already have that information readily available.
[3257.86 --> 3264.14]  So a big part of JSON API is making it possible to build a JSON API server with existing infrastructure, like Express or Rails.
[3264.14 --> 3269.94]  It's like not trying to say that you need to start from scratch and build entirely new infrastructure.
[3270.68 --> 3280.24]  But the fact that the type and ID are really just talking about linkage between different objects means that you could have like one type and a UUID as your linkage.
[3280.24 --> 3288.92]  If you're trying to, you know, serialize a completely arbitrary graph of objects, you could just have like the type is always object and the ID is always a UUID that you generated.
[3288.92 --> 3289.96]  That would be just fine.
[3290.34 --> 3293.46]  And so the way I think about JSON API these days is that.
[3293.64 --> 3298.54]  It's a graph of object serialization, which really is the most general.
[3299.18 --> 3306.46]  It's hard to imagine things that you're trying to serialize that you cannot express using that serialization mechanism because it's really quite general.
[3306.46 --> 3325.88]  So who all was involved in this process from, you know, May of 2013 is when you first kind of pulled it out of that RailsConf conversations and Ember data at the time to now where, like we said earlier, it shipped stable 1.0 in May of 2015.
[3326.56 --> 3329.22]  We're wondering, like, where was W3C in all of this?
[3329.30 --> 3330.58]  Who was involved in the specification?
[3330.72 --> 3334.10]  Was it just yourself, Steve, and the other person mentioned?
[3334.10 --> 3337.24]  Or were you able to get kind of a groundswell of support?
[3337.32 --> 3344.54]  Because I was a person who, when I realized you guys were working on this, I was like, yes, this is the kind of thing that needs to exist.
[3344.74 --> 3347.14]  I'm glad that smart people are working on it.
[3347.30 --> 3349.22]  And when it's done, I'm just going to use it.
[3349.40 --> 3351.78]  And that's one last thing I have to think about as I build my application.
[3352.04 --> 3354.30]  So that's where I fell down on it.
[3354.42 --> 3360.64]  But were there other people that thought, ooh, this needs to exist, and we have different needs than Ember, and so we're going to get involved?
[3360.72 --> 3361.60]  Was there a lot of discourse?
[3361.60 --> 3376.46]  Yeah, I mean, I think Dan has some number, but there were threads about seemingly trivial things that went on and on and on for hundreds of comments that occasionally I had to weigh in on as the final arbiter of some of these things.
[3376.46 --> 3382.58]  I would say that basically it had like a sort of on-again, off-again story until pretty recently.
[3383.24 --> 3384.54]  So I put out the thing.
[3385.68 --> 3387.64]  I kind of just said, okay, here's the thing.
[3387.70 --> 3389.90]  I'm going to keep quiet for a while, let people try to implement it.
[3389.90 --> 3400.64]  And we got like probably like around a year later, we got a good enough amount of initial feedback from people who were trying to put it into production, which actually was pretty cool, right?
[3400.66 --> 3411.06]  So we had like, you know, maybe like a dozen people who were legitimately trying to make JSON API the original draft, a production thing, and all of them hit various issues that they reported.
[3411.06 --> 3417.94]  So about a year later, we said, okay, I think we have enough information now to sort of build the second draft.
[3418.14 --> 3425.10]  And the second draft was largely driven by these ambiguity reducing ideas, right?
[3425.10 --> 3429.72]  So we were trying to find places where we unnecessarily said this is a should or a may.
[3430.24 --> 3433.02]  And in fact, there's really no reason for that.
[3433.08 --> 3436.16]  The cost of the ambiguity is much higher than the flexibility benefit.
[3436.26 --> 3437.50]  So let's just make that a must.
[3437.88 --> 3442.86]  Or let's just remove that and say that's potentially a future direction for an associated spec.
[3443.60 --> 3444.58]  So we did that.
[3444.58 --> 3447.86]  I was actually part of the W3C tag for a lot of this process.
[3448.00 --> 3454.80]  And my participation in standards in general gave me a pretty good sense of like what the process of building a standard should look like.
[3455.46 --> 3459.04]  But there was no real standard organization, quote unquote real.
[3459.80 --> 3464.82]  There's a funny thing, which is that the WG is sort of perceived to be a standards organization.
[3465.02 --> 3469.12]  But all the real standards people are like, oh, these kids making standards.
[3469.38 --> 3471.32]  You don't really know what it's like to make a standard.
[3471.98 --> 3474.50]  And the JSON API process was sort of like that.
[3474.50 --> 3478.08]  It was a pretty serious attempt to get pretty rigorous.
[3478.08 --> 3485.46]  It uses the RFC story for how you say things are required, not required.
[3485.68 --> 3488.92]  It tried to get pretty clear about what the requirements were.
[3489.72 --> 3495.64]  It uses the like media type extension mechanism that the other specs we're working with use.
[3495.64 --> 3502.36]  We did a good job of deferring things and leaving open extensibility points.
[3502.64 --> 3508.30]  We've talked about – we've said that it's a living standard, but it's always going to be compatible.
[3508.78 --> 3511.78]  So JSON API 1.1 is only going to be additive.
[3512.02 --> 3513.60]  It's never going to break existing implementation.
[3513.60 --> 3517.00]  So we've done a lot of the things that real standards like to do.
[3517.96 --> 3522.06]  But no, there was no – there were no – I mean, I guess I'm a standards person, right?
[3522.28 --> 3535.60]  Well, you're saying the word real standards there, and I'm kind of piggybacking off on something you said in the talk that seems to be some way for us to weave back into this story, which is it seemed like you had some sort of –
[3535.60 --> 3543.10]  not so much a negative thing against asking for permission from a central authority, which tends to be WC3 or what you're calling real standards.
[3543.10 --> 3551.66]  It seemed like you and Steve and these other people involved in this were, like as Jared said before, like anyone else who had heard you working on this were totally excited because you're smart people.
[3551.80 --> 3552.62]  You're able to do it.
[3552.96 --> 3564.42]  But it seemed like you didn't feel like you had to ask permission to create this JSON API spec that would become the de facto standard should the community bless it and adopt it.
[3564.76 --> 3569.52]  So the first thing we actually did was file an IANA request for the media type.
[3569.52 --> 3580.36]  So I would say that we did go through the minimum viable standards process, which was to express what it is that we're doing and ask for permission to have a centrally registered media type.
[3581.20 --> 3582.56]  And I think that that was good.
[3582.90 --> 3588.42]  I think that – I think we did a few things that people who care about standards being standards would have requested.
[3588.42 --> 3591.44]  And I think that was the right thing.
[3591.86 --> 3605.34]  But I also feel like we're sort of – there's sort of been this pendulum swing where historically people said things should be standardized unless there are two interoperable implementations, which sort of implies that the implementations go first.
[3605.34 --> 3615.08]  But then like somewhere in the – somewhere after 2000, a bunch of standards work happened that was attempting to lead by standards.
[3615.72 --> 3617.24]  And I think there's still some of that left.
[3617.58 --> 3619.06]  But I just don't think that works at all.
[3619.80 --> 3631.84]  And a big part of the pendulum swing that I've been part of in both the TC39 process and to whatever extent I've been involved in the W3C has been an attempt to remind the standards bodies that they should not try to lead.
[3631.84 --> 3634.76]  Because that's not what standards are about, right?
[3634.84 --> 3639.68]  Standards cannot – standards are about acquiring social consensus from implementers.
[3640.44 --> 3644.02]  It's about having a nice space where you can work for W3C.
[3644.12 --> 3647.06]  It's very important that the space is not patent encumbered, right?
[3647.06 --> 3659.60]  So any spec that's approved by the W3C by definition is – it's a promise that all the participants in the W3C, all the members, say that they will not sue anybody for patents because of the technologies that are in the specs.
[3659.82 --> 3661.22]  That's pretty important, right?
[3661.22 --> 3672.66]  So the standards bodies are useful, but they really do need to be facilitators, specifically facilitators of implementers and users, and not try to have standards people do the work.
[3673.36 --> 3674.48]  That's a really good point.
[3674.78 --> 3680.98]  I mean, because that's what you're saying here too is that going back to Rails, it was extracted from Basecamp.
[3681.14 --> 3684.66]  This was extracted from what you were doing in Ember data.
[3684.66 --> 3685.38]  In Ember data.
[3685.58 --> 3704.50]  So it seems like people who are actually doing – not so much that standards aren't doing, but I like your idea of how they're providing this safe environment to come to consensus of what's out there, what's working, why is it working, who trusts it, why do they trust it, and bring it on to one thing that is under some sort of governance that's sort of community-bound in a way.
[3704.50 --> 3707.88]  And I think – so there always are implementers that are participants.
[3708.16 --> 3710.14]  And like TC39 is like a ton of implementers.
[3710.56 --> 3728.26]  And the real thing that you get out of – like the thing that you get out of that process is not that the implementers are sitting around in a room talking to each other about what to implement, but that the implementers understand that they can – that when they implement something or when they propose something, they have acquired the consensus necessary to feel confident that they can move forward with it.
[3728.26 --> 3732.76]  And that process – like some people think of that as being an inherently slow process.
[3733.28 --> 3735.30]  But first of all, I just don't agree.
[3735.44 --> 3743.74]  I think if you look at like the ES6 process or even the HTML5 process, we've made pretty good progress on features despite the need for consensus.
[3743.90 --> 3748.98]  But I think people forget that there's a massive time cost in not acquiring social consensus, right?
[3748.98 --> 3753.10]  If you – you know, Chrome maybe could ship something a little faster or Firefox could ship something a little faster.
[3753.42 --> 3760.10]  But whatever gains you get from shipping something a little faster will be eaten up immediately by the cost of convincing the other browsers to implement it.
[3760.16 --> 3760.34]  True.
[3761.38 --> 3763.00]  And sometimes you have to go first, right?
[3763.32 --> 3764.96]  We always talk about this on TC39.
[3765.34 --> 3766.78]  Sometimes someone has to go first.
[3767.22 --> 3772.48]  And usually what will happen is somebody will propose something and everyone will say, I'm not really sure what the value of that is.
[3772.76 --> 3774.14]  But I'm not necessarily opposed to it.
[3774.18 --> 3775.42]  I will implement it if it turns out.
[3775.58 --> 3776.44]  But why don't you go first?
[3776.44 --> 3779.68]  And then usually the person will go first and quite often it will happen.
[3780.42 --> 3781.66]  They just draw straws or what?
[3782.28 --> 3785.70]  No, it's usually the people who are the most confident that it's a good idea.
[3786.68 --> 3788.78]  Well, that's a good place to take a pause.
[3789.02 --> 3791.98]  We have one more break before the show comes to a close.
[3792.06 --> 3792.92]  However, don't worry.
[3793.06 --> 3794.66]  We have lots more to cover.
[3795.12 --> 3801.98]  Compliance, resource discovery, some experimental things, feature-proofing APIs, just to kind of touch on a couple of topics coming up.
[3802.06 --> 3803.12]  But let's take a break.
[3803.12 --> 3806.38]  We'll come back and we'll dive deeper with you on JSON APIs.
[3806.98 --> 3808.42]  And hopefully you'll love it.
[3808.48 --> 3809.12]  So we'll be right back.
[3809.12 --> 3817.88]  Our friends at DigitalOcean, Simple Cloud Hosting built for developers, launched a new feature recently we absolutely love.
[3818.22 --> 3822.80]  It's called Droplet MultiCreate for easily launching up to 10 servers at once.
[3823.26 --> 3827.90]  You can deploy multiple droplets when you create your droplets with the exact same configuration.
[3828.50 --> 3829.40]  And this is a huge feature.
[3829.46 --> 3830.28]  We absolutely love it.
[3830.28 --> 3832.30]  Head to DigitalOcean.com.
[3832.60 --> 3838.48]  And when you sign up, use our code CHANGELAW to get a $10 hosting credit when you sign up.
[3838.48 --> 3841.20]  All right, everybody.
[3841.28 --> 3843.60]  We're back and we are diving deep on JSON API.
[3843.80 --> 3850.56]  Yehuda, you've mentioned a few features offhand, but I thought we'd take a moment to kind of go through them one by one.
[3850.62 --> 3854.72]  The major principles that have shooken out as useful for a JSON API.
[3854.72 --> 3860.20]  What's in the spec and what does a JSON API compliant server look like?
[3860.76 --> 3860.94]  Cool.
[3861.08 --> 3861.58]  So, yeah.
[3861.80 --> 3869.04]  So I would say the main principle is what I said earlier, which is that what you're doing is you're serializing a graph of objects on your server.
[3869.04 --> 3879.50]  What I mean by graph is just that it's possible for one object to be related to multiple of them, which is like sort of like a has-in-belongs-to-many relationship.
[3880.64 --> 3888.64]  Or you could even have like a, you know, a post has many comments and the comment belongs to a user, but that user might be referenced from other places, right?
[3888.70 --> 3894.08]  So when I say graph, I just mean that people often imagine in their head that the data structure is a tree.
[3894.08 --> 3900.54]  They imagine like, well, there's a post and it has many comments, so that's nested inside of there, and then the comments have users, so you just nest the users inside of there.
[3900.90 --> 3904.80]  But in the real world, those objects are related, could be related to yet other objects.
[3904.98 --> 3907.20]  So you don't necessarily want to continue nesting.
[3907.66 --> 3909.90]  And this is actually a core value of JSON API.
[3910.04 --> 3922.44]  It's something that is sort of counterintuitive to a lot of people, but trying to make it a tree has pretty serious implications on both efficiency and your ability to properly deserialize it.
[3922.44 --> 3925.52]  Like, what if you have the same user in multiple places and they don't match?
[3926.06 --> 3927.18]  What does that actually mean?
[3927.26 --> 3928.02]  Do you have to check that?
[3928.60 --> 3933.02]  So one of the core values of JSON API is that we're talking about a graph of objects, not a tree of objects.
[3933.72 --> 3939.22]  And there's always, there's often, not always, but quite often a primary document.
[3940.82 --> 3946.80]  So if you ask for post number one, you want to know that you might get back a whole bunch of stuff.
[3946.88 --> 3949.98]  You might even get like a summary of how many documents there are in the entire system.
[3949.98 --> 3954.32]  But there's a primary response, which is the post object.
[3954.54 --> 3957.56]  And then it might have links to comments.
[3958.00 --> 3962.78]  And those links to comments could either be referring to other things that are inside the same response.
[3963.36 --> 3964.96]  And that's commonly what people do.
[3965.24 --> 3970.02]  But they could also be URLs that link to other documents that you can use.
[3970.28 --> 3975.48]  So maybe you're downloading a list of posts just because you want to print the front page of your blog.
[3975.48 --> 3977.94]  And you don't need the comments until you actually click on a comment.
[3978.32 --> 3981.74]  You still want to say like, if you ever need the comments, here's the URL for those comments.
[3982.06 --> 3985.70]  So the idea is that what we're talking about is a bunch of linked objects.
[3986.14 --> 3995.36]  But unlike maybe the more pure rest or the pure like linked data philosophy, the assumption is that you will quite often want to include a lot of the linked objects together.
[3995.36 --> 3998.46]  And there should be a very canonical standard way to do that.
[3998.76 --> 4000.40]  And it shouldn't always have to be URLs.
[4000.58 --> 4007.08]  So one thing that's a little problematic about URLs, first of all, is that it implies that there's a way to get individual pieces.
[4007.22 --> 4010.28]  But maybe, for example, there's no way to get comment number 17.
[4010.54 --> 4013.18]  The only way to ever get comment 17 is by going through the post.
[4013.56 --> 4015.78]  And that's a totally reasonable thing to want to be allowed to do.
[4015.78 --> 4020.66]  But if you only link things through URLs, you have to construct a URL for that comment.
[4020.78 --> 4024.20]  And maybe like a very, you know, URL person would say, that's fine.
[4024.24 --> 4025.12]  You can make a fake URL.
[4025.44 --> 4027.44]  But this stuff kind of adds up in complexity.
[4027.68 --> 4035.26]  And what we want to be able to do is just express connected data in ways that are most natural for your implementation.
[4035.68 --> 4037.36]  That doesn't mean that implementation leaks.
[4037.60 --> 4040.52]  It just should mean that it's natural for the implementation that people have.
[4041.16 --> 4043.06]  So we have, you know, we have this post.
[4043.12 --> 4043.74]  It has many comments.
[4043.74 --> 4047.92]  Maybe the comments are directly embedded in the document.
[4048.34 --> 4049.54]  Maybe they're linked through URLs.
[4049.66 --> 4050.92]  Maybe they're not linked through URLs.
[4051.12 --> 4051.94]  They're linked in some way.
[4052.96 --> 4058.40]  But there's very canonical ways of doing all these, all the different ways of describing things.
[4059.02 --> 4059.86]  And they're composable.
[4060.76 --> 4061.44]  And sorry.
[4061.64 --> 4068.16]  And then if you, so all the ways of interacting with that data is done using normal HTTP, the HTTP verbs.
[4068.16 --> 4070.70]  So you get something using the get request.
[4070.70 --> 4076.18]  And when you get something, you just might happen to get back other related things.
[4076.18 --> 4080.82]  If you want to add a new thing, you post to it.
[4080.86 --> 4082.56]  And there's some rules for exactly how that works.
[4083.02 --> 4086.04]  There's also delete to delete something.
[4086.16 --> 4094.26]  And there's patch, which allows you to, there's sort of a historical sad ambiguity about what put exactly means.
[4094.26 --> 4097.20]  But patch very canonically means the right thing.
[4097.60 --> 4101.38]  So you can patch to make some partial changes to an existing document.
[4101.64 --> 4106.26]  Patch is an update to an existing document and puts like a, just supposed to replace the entire thing, right?
[4106.38 --> 4113.34]  So I will just tell you, having now spent many years writing this spec, that people feel a lot more confident about what put means than I think they should.
[4113.34 --> 4116.70]  But people do have religious opinions about what put means.
[4117.08 --> 4124.46]  And because of the fact that you're interacting with infrastructure on the internet, you should probably not run afoul of people's religious opinions about what things mean.
[4125.08 --> 4127.64]  Because you're just avoiding put altogether.
[4127.82 --> 4128.82]  You're just like, we're just going to patch.
[4129.68 --> 4130.12]  Yeah.
[4130.34 --> 4134.96]  And we may, there are use cases for put in JSON API that I think everyone would accept.
[4134.96 --> 4142.22]  But we were, we effectively punted on them for 1.0 because of the fact that what people really usually want is patch.
[4143.60 --> 4145.92]  So, so I would say that that's the main thing.
[4146.00 --> 4150.26]  You, we basically use normal HTTP verbs to describe interactions.
[4150.94 --> 4155.10]  And, and I say that and people probably are nodding their head and saying, okay, I basically know what that means.
[4155.16 --> 4156.78]  I assure you, you basically don't know what it means.
[4157.90 --> 4158.74]  Why is that?
[4159.18 --> 4164.80]  It's just like the exact, like, okay, I'm going to make a, you know, I'm going to make a, patch this document.
[4165.24 --> 4166.20]  First of all, what is the format?
[4166.40 --> 4167.32]  What is the response format?
[4167.46 --> 4169.38]  And then what are like all the status codes?
[4169.60 --> 4170.50]  What are they supposed to mean?
[4170.54 --> 4172.02]  If you have errors, how do you format that?
[4172.06 --> 4178.38]  There's like a billion, like there's so many questions that you have to answer, even to answer like, what is a 204?
[4178.46 --> 4179.10]  What is a 200?
[4179.26 --> 4180.10]  What is a 404?
[4180.56 --> 4181.18]  What is a 500?
[4181.46 --> 4184.64]  Like what kinds of information should come along with each of those things?
[4184.90 --> 4186.66]  Some of them, the specs have something like 204.
[4186.96 --> 4188.72]  You're supposed to not include everything, anything.
[4188.86 --> 4189.02]  Great.
[4189.20 --> 4189.34]  Okay.
[4189.44 --> 4189.92]  Problem solved.
[4190.44 --> 4192.60]  But what about like every other status code?
[4192.70 --> 4193.38]  What about errors?
[4193.38 --> 4198.96]  And you really do want this, all these questions to be not left up to somebody's whims.
[4199.06 --> 4203.74]  You really, if somebody doesn't have a better idea, you would really like to tell them what the answer is.
[4203.74 --> 4208.18]  If someone has a better idea, and it's a really good reason escape valves are a good idea.
[4208.26 --> 4209.14]  And we have this metadata.
[4209.78 --> 4221.76]  And actually, that's another core value is that every place in the document has a metadata key that you can use to put arbitrary information that you think is like the spec doesn't talk about, but is useful information to tell your clients.
[4221.76 --> 4226.70]  And that, first of all, that allows us to reserve the top level.
[4227.22 --> 4232.70]  Like anything, any top level key is reserved so we can add more stuff later without breaking existing clients.
[4232.70 --> 4244.84]  But second of all, it means that people can do pretty aggressive experimentation with things like pagination or filtering, some of which are in the spec, some of which are not, without having to worry about interoperability.
[4245.06 --> 4249.88]  So it's sort of a place where you say, I know for my application I would like to include this extra information.
[4250.64 --> 4253.56]  JSON API is not locking you out of the ability to do that.
[4253.56 --> 4255.70]  Does it have pagination and filters?
[4256.24 --> 4256.42]  Yep.
[4256.42 --> 4256.66]  Yep.
[4256.74 --> 4258.98]  So there's pagination and filtering and sorting.
[4260.80 --> 4268.38]  I would say that the specification for each of these things is not as rigorous.
[4268.56 --> 4269.78]  It's basically clear.
[4270.00 --> 4271.64]  And the word must and should are used.
[4271.64 --> 4276.44]  So it tells you what keys you have to use and, in some cases, what the semantics should be.
[4276.44 --> 4284.24]  But for sure, over time, the specification will get clearer about exactly what you should expect.
[4284.42 --> 4291.46]  So, for example, we tell you that there's the offset and limit pagination and there's the number and size pagination story and there's the cursor story.
[4291.66 --> 4293.50]  And we tell you how each of those things should work.
[4294.00 --> 4297.04]  And we tell you that you, you know, how you should encode the characters and all these things.
[4297.68 --> 4304.58]  But I think we're, like, basically people are using these tools right now to build pagination solutions.
[4304.58 --> 4312.32]  And we're getting a lot of feedback from people about how to, what the best way to rigorously define how to do it.
[4312.50 --> 4315.54]  Filtering and sorting are actually pretty, are easier specs.
[4315.78 --> 4317.36]  And we, and those are already more rigorous.
[4317.88 --> 4325.68]  But we've effectively reserved the pagination space and given you enough tools to work with plus the metadata story so that you can figure out something.
[4325.68 --> 4333.86]  We're waiting for things like EmberData and other clients to figure out, like, what it really looks like to use the metadata solution.
[4333.86 --> 4339.66]  And then the idea is that you take the things that people put in metadata and make them first class once we figure out what it is.
[4340.42 --> 4348.52]  So you mentioned that one of the purposes of the metadata is so you can reserve the top level for future changes because you want to be backwards compatible.
[4348.86 --> 4351.74]  Can you expand on your future-proof API design?
[4351.84 --> 4353.16]  Is that kind of a core value as well?
[4353.58 --> 4353.84]  Yes.
[4353.84 --> 4360.72]  So one thing that I've learned from specifications is that people underestimate the cost of backwards incompatible changes.
[4360.98 --> 4364.10]  And the reason for that is that people underestimate network effects in general.
[4364.36 --> 4373.38]  So if you look at, if you look at something like NPM or RubyGems or like APIs on the web, there's a lot more people involved than you think.
[4373.38 --> 4374.76]  And they all connect to each other.
[4374.88 --> 4376.86]  They don't all just connect to the central thing.
[4376.96 --> 4384.18]  There may be, you know, independent, like intermediate things that you, so there may be libraries or other APIs that work with the other third-party API, right?
[4384.26 --> 4387.30]  And the implementation details can leak across these abstractions.
[4387.30 --> 4404.60]  So one of the things that the web has decided is if you're willing to be creative and you're willing to be pretty careful about what you expose, what you, how much arbitrary scoop you allow people to throw in, then you can pretty much keep adding stuff.
[4404.94 --> 4411.94]  You could deprecate stuff, but you can deprecate stuff without removing it and you can keep adding things over time and mostly have things continue to work.
[4411.94 --> 4420.52]  And I'm just generally a big believer in the idea that it is almost never the case that breaking changes are worth it.
[4421.46 --> 4430.38]  I think in things like Ember, especially when you're talking about the very first version of something, there's probably like one moment in time where breaking changes become important.
[4430.98 --> 4432.86]  I think like Linux had a moment like this.
[4433.56 --> 4434.76]  Ruby had a moment like this.
[4435.62 --> 4438.78]  And even when you do those breaking changes, you have to be extremely careful.
[4438.78 --> 4440.26]  I think you can compare Ruby to Python.
[4440.26 --> 4444.90]  You see Ruby did a much better job of being tasteful and careful about the breaking changes than Python did.
[4445.50 --> 4451.58]  But I think you can do a pretty okay job of keeping things permanently compatible.
[4452.38 --> 4459.96]  And I think that people underestimate the, they overestimate the value and underestimate the cost of being willing to break things.
[4460.54 --> 4464.48]  We just talked, the Rust core team just had a conversation a few times about this.
[4464.48 --> 4468.28]  And there's like, it's not fully, there's not full consensus on this yet.
[4468.28 --> 4471.96]  But I think most people think that Rust 2.0 doesn't really make sense.
[4472.12 --> 4475.64]  That we should continue trying to, you know, maybe we'll have a Rust 1.40.
[4476.28 --> 4481.72]  And we think we could continue to make changes and even add things like garbage collection.
[4481.72 --> 4482.86]  We think we can do compatibly.
[4482.86 --> 4489.60]  And I think people just aren't, they aren't very creative about, it's just much easier to say, oh, the world is changing.
[4489.70 --> 4490.40]  We got to change everything.
[4491.22 --> 4493.08]  And I think it's just not usually true.
[4493.32 --> 4496.46]  So, and I basically have put my money where my mouth is a few times.
[4496.46 --> 4500.40]  And I think, I think people should try.
[4500.46 --> 4501.60]  And I think it will usually work out.
[4501.60 --> 4506.64]  So, one of the ways we kicked up the show was actually kind of deriving where this came from.
[4506.78 --> 4511.18]  It started with a tweet from you, which was comparing JSON API to ASM.js.
[4511.92 --> 4517.86]  You said you can think of JSON API.org, which is obviously JSON API, as ASM.json,
[4518.34 --> 4524.56]  which is a low-level consistent, consistent serialization format and protocol that you could build on.
[4524.94 --> 4529.30]  Can you compare the two, like you said earlier about having a de facto standard.
[4529.30 --> 4532.50]  It seems like, obviously, this is what you're trying to do with it.
[4532.54 --> 4533.40]  But then you also have this.
[4533.46 --> 4534.38]  Are they competing standards?
[4534.94 --> 4535.74]  What is the differences?
[4536.14 --> 4537.30]  And, you know, do they play together?
[4538.30 --> 4544.16]  So, ASM.js is this thing that Mozilla invented, Mozilla Research, which is basically just,
[4544.48 --> 4554.10]  they noticed that there's a subset of JavaScript that if you squint closely enough is a fully typed thing that is sufficient to represent basically all of C.
[4554.70 --> 4558.66]  And so they basically define the subset of JavaScript that they will validate.
[4558.66 --> 4564.12]  You basically tell them that you're using it, then they validate it, and then it will compile into native code.
[4564.22 --> 4568.26]  And it's, like, somewhere between 20% and 50% slower than just, like, straight-up compiled C code.
[4568.96 --> 4574.96]  And the reason I compared it to that is that if you look at ASM.js, what you will see is that no human being wants to write this.
[4575.44 --> 4578.14]  It's actually significantly worse than JSON API.
[4578.32 --> 4580.50]  It's, like, a horrible format to write in.
[4580.88 --> 4583.02]  But the point of ASM.js is that that's not the point.
[4583.42 --> 4584.52]  That's not the goal of ASM.js.
[4584.52 --> 4588.50]  The goal of ASM.js is to be fast and also to be a thing that you could build on.
[4588.66 --> 4594.38]  You could, you know, you could compile gzip to ASM.js, and now you have a fast gzip that you could run in a browser.
[4595.14 --> 4598.32]  And so the idea is you shouldn't be too...
[4598.32 --> 4601.74]  People have said on Hacker News a lot of times, like, ASM.js is so ugly.
[4601.94 --> 4603.04]  It's, like, such a hack.
[4603.36 --> 4604.36]  Why you know bytecode?
[4604.96 --> 4605.16]  Right.
[4605.16 --> 4607.08]  And the point is that that doesn't really...
[4607.08 --> 4609.18]  Like, the exact syntax of ASM.js doesn't actually matter.
[4609.60 --> 4616.58]  The thing that matters is that we have now constructed a thing that you could write that ships on the web that is pretty close to being as fast as C.
[4616.96 --> 4623.10]  And that is pretty important and effectively supersedes any aesthetic considerations that you might have.
[4623.10 --> 4632.08]  And I was sort of trying to get across a similar thing about JSON API, that the goal of JSON API is not to allow you to build artisanal APIs.
[4632.26 --> 4642.02]  The goal of JSON API is to create a nice wire protocol and format for communicating grasp of objects between arbitrary servers and clients.
[4642.50 --> 4645.82]  And obviously, there's some constraints there, like, you should be able to do it on existing servers.
[4645.92 --> 4649.14]  So Rails, Express, Java should all be able to do it.
[4649.18 --> 4652.42]  You shouldn't have to build your own whole new server with whole new server infrastructure.
[4652.42 --> 4654.96]  It shouldn't require things like WebSockets to work, right?
[4655.02 --> 4659.38]  So it should work with regular HTTP infrastructure people have already deployed.
[4659.84 --> 4661.20]  So those things are all very important.
[4662.26 --> 4671.38]  But the exact, you know, whether it's 20% better or worse than the aesthetics that you would have personally designed for a given project is actually just much, much less important than the interoperability.
[4672.00 --> 4676.98]  And so that's sort of what I was getting at was that it's more of a low-level protocol.
[4676.98 --> 4687.42]  It's a way of getting everyone on the same page about something that you can share and build on than it is about being a – and again, it needs to not be a format that's, like, impossible for humans to understand.
[4687.90 --> 4689.82]  It needs to be a format that a human can look at.
[4689.86 --> 4700.16]  But whether or not there's a top-level attributes key or you leave it off and put all the attributes at the top level is really just not something that needs to be a reason for non-interoperability.
[4700.16 --> 4702.90]  That is a bad excuse for non-interoperability.
[4703.58 --> 4718.16]  So one last question before we close up the conversation around JSON API is I think 2015 has kind of been the year of Facebook and Netflix kind of launching out these new API.
[4718.90 --> 4720.88]  I'm going to call them transport patterns or styles.
[4721.00 --> 4722.18]  I'm not sure exactly what you call them.
[4722.18 --> 4731.06]  But we have GraphQL, we have Falcor, and these seem to be taking a little bit different approach than the traditional REST JSON-based APIs.
[4731.24 --> 4738.62]  Can you compare and contrast kind of advantage, disadvantage of the JSON API style versus these new styles?
[4739.08 --> 4742.62]  Yeah, but I think I've been sort of getting at it, but I'll be very explicit.
[4742.62 --> 4759.10]  I think that what GraphQL and Falcor are both getting at is the fact that very purist ideological REST is pretty hostile to bulk transport, and it's pretty hostile to customized transport.
[4759.48 --> 4762.84]  People don't want you to say, give me this resource, but don't include these attributes.
[4763.02 --> 4765.84]  And they don't want you to say, give me this resource and include these other related resources.
[4765.84 --> 4780.86]  In fact, very purist REST people always talk about HTTP2 as allowing you to just like continue down the path of having one URL per resource and just, you know, fire hose them with one HTTP socket, but now multiple requests.
[4780.86 --> 4796.38]  And JSON API and Falcor and GraphQL all share a philosophy that a client should be able to, you should be able to construct payloads that are appropriate for the access patterns that your client actually has.
[4796.76 --> 4803.66]  If you're about to look at a blog and you know that people are likely to click on a comment, you should be allowed to include all the comments at once.
[4804.38 --> 4808.60]  Certainly, you should be allowed to include the count of comments per post so that you can put in the UI.
[4808.60 --> 4822.20]  GraphQL is on a pretty one far end of the spectrum, which is that the idea behind GraphQL is that you derive the exact thing that you need out of the consumption patterns.
[4822.58 --> 4824.54]  So you say, I need a post.
[4824.88 --> 4826.68]  So every component basically says what it wants.
[4827.08 --> 4827.80]  It says, I want a post.
[4827.90 --> 4828.98]  The other guy says, oh, I want a comment.
[4829.06 --> 4830.84]  I need the, you know, I need the comment count.
[4830.84 --> 4840.50]  And the GraphQL library takes all those things, combines it into one request, and it asks for very precisely what the client has asked for.
[4841.54 --> 4851.04]  And Falcor, I would say, is also pretty similar to that, although Falcor is a more flexible, I don't know, people are, whoever's listening to me who works on these projects is going to yell at me no matter what.
[4851.04 --> 4855.20]  But I would say that both Falcor and GraphQL are designed for consumption patterns.
[4855.32 --> 4860.62]  They're designed for building a request for exactly the thing that you need for what the client is asking for.
[4861.04 --> 4869.44]  And I, first of all, one of the reasons JSON API did not go down this path is that it requires a server that's capable of pretty sophisticated querying.
[4869.44 --> 4869.94]  Right.
[4869.94 --> 4875.92]  And I think, again, JSON API has as a goal that you should be able to use existing server infrastructure.
[4876.52 --> 4879.40]  But perhaps more importantly, that kind of stuff is pretty uncashable.
[4880.02 --> 4887.48]  So if you ask for a very specific subset of the data, it's very hard to say, oh, I basically know what you're asking for.
[4887.52 --> 4888.40]  You're asking for all the posts.
[4888.48 --> 4888.80]  No problem.
[4888.86 --> 4889.92]  I already cached the whole payload.
[4890.62 --> 4892.84]  It's very hard to do that when you're asking for very specific pieces.
[4892.84 --> 4904.76]  It's also not really a good fit for what the GraphQL people pejoratively call overfetching and I positively call overfetching.
[4905.24 --> 4913.76]  Sometimes you have to think about when you're building an application, if you're showing a particular page, what are the likely next things the user is going to do?
[4913.76 --> 4921.94]  And if it's very likely that within a few seconds or half a minute, let's say 10 or 15 seconds, they're usually going to click on something.
[4922.34 --> 4928.38]  It's actually a reasonable thing to give them the thing that they're going to click on together with the original payload sometimes.
[4928.46 --> 4929.44]  You have to think about it, obviously.
[4929.80 --> 4939.58]  But it's sometimes worth sending extra data out of the gate so that not the first click will be fast, but then the second, third, and fourth click will be fast.
[4939.58 --> 4952.76]  And so the Ember philosophy is a little bit more, you know, be a little more liberal about what information you download so that when you click on the second or third thing, you didn't tightly scope the data request to exactly what was on the screen the first time.
[4953.10 --> 4959.42]  That a lot of the times the second click will have opportunistically gotten enough information to render it without making new XHRs.
[4959.42 --> 4960.90]  That's the Ember philosophy.
[4961.02 --> 4973.64]  And the JSON API philosophy is sort of agnostic, but it is pretty compatible with the idea of sending extra information out of the gate so that your subsequent navigations are reasonably fast.
[4973.64 --> 4996.02]  So, again, I would say JSON APIs, like the things that I think are powerful and special about JSON API are that it's both pretty good about, it shares the philosophy of wanting to be able to have a payload that's not just talking about one thing, but it's like all the things I need for this particular screen.
[4996.02 --> 5000.24]  But it does not share the philosophy of needing a new infrastructure to make that work.
[5000.32 --> 5004.78]  It wants to be able to piggyback on all the infrastructure that people already have to make it work.
[5005.32 --> 5014.04]  And it also is pretty positive towards the idea of opportunistically including extra information that you think the user might want.
[5014.38 --> 5017.90]  Again, I'm sure that any GraphQL person listening knows how to make that work with GraphQL.
[5017.90 --> 5023.90]  But, again, the GraphQL consumption story is that you don't really think about the query that you're constructing.
[5024.04 --> 5027.72]  The query is constructed automatically based on what your components have said they want.
[5028.10 --> 5031.28]  And I just personally don't buy that.
[5031.92 --> 5036.20]  I think it's bad to tightly scope the data to what happens to be on the screen at a particular time.
[5036.72 --> 5036.84]  Yeah.
[5036.94 --> 5041.06]  You mentioned infrastructure, and I got to thinking about HTTP2 as you were talking.
[5041.06 --> 5053.42]  And it seems like all of these are focusing on optimizing that for the minimum number of requests in order to get the exact data you need for the screen or for the particular widget or what have you.
[5053.94 --> 5063.02]  It seems like the HTTP2 features, the pipelining, the multiplexing, and so on, keeping that one connection open, doesn't that mitigate a lot of the problems that we're trying to solve?
[5063.58 --> 5066.92]  So people have that hunch, and there's a sense in which that hunch is correct.
[5066.92 --> 5069.92]  But I think people have to remember...
[5069.92 --> 5073.60]  No, I think you can construct examples where it helps.
[5074.08 --> 5081.24]  I think people have to remember that there's still a round trip if you use an open HTTP2 socket to make a request.
[5081.64 --> 5093.72]  So if you're basically letting consumption drive your requests, and yes, it is true that when you click on a page, you can fire off the request much faster if there's an open socket just sitting there.
[5093.72 --> 5094.72]  Right.
[5094.72 --> 5100.00]  And if you're also able to do eager pushes, you could try to be clever about what you're doing.
[5100.00 --> 5101.00]  But there's still...
[5101.00 --> 5103.00]  Like, the speed of light is still...
[5103.00 --> 5104.90]  Has only a limited speed.
[5105.28 --> 5113.02]  And people in New Zealand and Australia experience this pretty heavily, where people just assume that your internet connection is fast.
[5113.38 --> 5118.60]  And the New Zealand and Australia problem has not helped a lot by HTTP2.
[5118.60 --> 5125.52]  I mean, it's helped a certain degree, but it doesn't make the connection to the server instantaneous just because it's an open socket.
[5125.84 --> 5133.68]  So I think people are over-optimistic about the ability to take a thing that used to be one document and break it up into a thousand documents.
[5133.68 --> 5139.86]  Because they have in their head the idea that HTTP2 makes the round trips instantaneous, but that is not correct.
[5140.10 --> 5140.64]  So there's...
[5140.64 --> 5142.88]  In other words, there's still a certain amount of serialization that happens.
[5143.02 --> 5143.54]  If you...
[5143.54 --> 5144.88]  Let's imagine that you make...
[5144.88 --> 5149.30]  The idea is you make a request for document A, and it has a dependency on document B, and it has a dependency on document C.
[5149.72 --> 5150.76]  And it's like, oh, no problem.
[5150.84 --> 5157.02]  Now we don't have to include those into one payload because we'll just instantaneously get document A and see that we need B and C and C.
[5158.14 --> 5159.84]  In fact, of course, that is not instantaneous.
[5159.84 --> 5168.52]  There's still some time that it takes to request and download when a smart server could have bundled together A, B, and C into one thing.
[5168.96 --> 5173.30]  And HTTP2 people will say, well, a smart server could also push A, B, and C together.
[5173.66 --> 5178.56]  But that smart server is not really like what GraphQL is talking about or what most people are talking about.
[5178.98 --> 5179.92]  You need to basically...
[5179.92 --> 5186.64]  The server has to figure out the consumption pattern and say, like, oh, I have noticed that a lot of people have asked for B after A, so I will start sending it.
[5186.64 --> 5198.16]  Or you need to have something that is morally equivalent to bundling where you are able to construct manifests that say, whenever you see A, that basically means you need B, using basically the same logic as bundling.
[5198.16 --> 5203.64]  So I guess what I'm saying is bundling still works very effectively.
[5204.04 --> 5204.72]  It's still reliable.
[5204.82 --> 5206.34]  It works on old connections and new connections.
[5207.10 --> 5209.12]  And there is...
[5209.12 --> 5215.64]  The exact story of making things work without bundling ends up getting to be pretty domain-specific, whereas bundling is a pretty...
[5215.64 --> 5216.52]  Like, just works.
[5216.78 --> 5221.46]  Like, if you take all the things that you know you're going to need and put them into one payload and send them at once, you don't have to think anymore.
[5221.54 --> 5222.08]  You're done.
[5222.08 --> 5227.08]  And I think that's why people like it, and I think it's also why HTTP2...
[5227.96 --> 5233.66]  The story about HTTP2 sells better in the realm of the abstract than it does in the real world.
[5233.72 --> 5240.84]  The real world is not magically solving the kinds of issues that cause people to, like, concatenate their JavaScript now that HTTP2 exists.
[5241.50 --> 5243.92]  People are, in fact, noticing that it doesn't work as well as they had hoped.
[5244.96 --> 5249.22]  Well, I guess we'll all just have to wait for HTTP3, which I hear will support quantum computing.
[5249.22 --> 5254.22]  I mean, I think, honestly, the TLDR is that if you...
[5254.98 --> 5257.20]  We just got to get rid of that speed of light problem, right?
[5257.76 --> 5258.12]  Yes.
[5258.94 --> 5262.36]  So, I think the TLDR of all this is that if you...
[5262.36 --> 5264.74]  Are you opening the box to get him to talk about quantum computing?
[5265.26 --> 5266.00]  No, I'm not going to...
[5266.00 --> 5276.84]  I think if you do something that is morally equivalent to bundling, like, you basically construct the bundle, but then you use HTTP2 to push the bundled components, that's probably fine.
[5276.84 --> 5280.84]  Like, that probably will end up being pretty similar to bundling, except that that's...
[5282.20 --> 5285.90]  At that point, you are not really doing the things that people are excited about about HTTP2.
[5286.40 --> 5286.76]  Yeah.
[5286.80 --> 5286.92]  Right?
[5287.00 --> 5288.02]  It didn't really...
[5288.02 --> 5289.14]  It will probably happen, right?
[5289.18 --> 5292.16]  It will probably happen when HTTP2 is very ubiquitously rolled out.
[5292.52 --> 5296.58]  People will have some format that lets you say, like, here is the quote-unquote bundle.
[5296.72 --> 5297.78]  Someone asked for this entry point.
[5297.86 --> 5298.54]  Give them all the things.
[5298.98 --> 5301.14]  But it doesn't really buy you that much.
[5301.14 --> 5307.46]  Well, it's certainly been a fun, deep, long conversation about JSON API's origins.
[5307.72 --> 5316.02]  Obviously, you know, the first beginning of the call was, you know, focus on you personally and your origins in programming and when you became a professional and obviously open source.
[5316.98 --> 5319.20]  But this has been a fantastic call.
[5319.90 --> 5322.00]  Yehuda, you are a man of many hats, though.
[5322.06 --> 5326.28]  So, we couldn't leave this show without at least touching on Ember.
[5326.28 --> 5331.26]  We here at the channel have been tracking isemberfastyet.com all of 2015.
[5331.40 --> 5332.02]  It's not 2016.
[5332.24 --> 5334.40]  So, congrats on that actually being fast.
[5334.50 --> 5340.74]  But is there anything you can share today about the current state of Ember.js, what's going on, and whatnot there?
[5341.24 --> 5341.56]  Sure.
[5341.74 --> 5345.92]  So, I've been working on a project called Glimmer 2 for the past three or so months.
[5346.64 --> 5348.28]  So, isemberfastyet was basically a...
[5349.98 --> 5354.14]  It was about Glimmer 1, the first version of Glimmer, which we actually shipped a while ago now.
[5354.14 --> 5357.90]  Like, maybe May and then spent the next few months, like, making it really polished.
[5358.44 --> 5362.12]  And basically, what Glimmer 1 did was it made re-renders very fast.
[5362.16 --> 5373.40]  So, the idea is if you have a, you know, you have a loop, an each loop in your template and you want to update it with a totally new array in old Ember and Ember 112,
[5373.78 --> 5376.72]  that would be a, like, have to blow away all the DOM and replace it.
[5377.00 --> 5384.08]  And React showed us that we don't need to do that, that there are better strategies that allow you to cleverly update only the parts of the DOM that you really need to update.
[5384.60 --> 5396.22]  And so, what Glimmer 1 was about was about taking those strategies that React pioneered and making them work well in Ember for cases where you have lists of things that maybe the data structure has completely changed,
[5396.30 --> 5397.66]  but the things it's talking about have not.
[5397.76 --> 5403.66]  So, like, maybe you have a list of people and you're constructing a completely new array, but the items inside the array are the same.
[5403.66 --> 5408.36]  Or maybe they're completely new objects, but the properties of all those objects are exactly the same.
[5408.78 --> 5414.28]  And making it so that basically without having to think about it, all those scenarios end up updating fast.
[5414.88 --> 5415.84]  And Glimmer 1 did that.
[5415.94 --> 5425.18]  I think we showed it at Ember Conf a demo that we then repeated when we actually shipped Ember 2.0 that showed a speedup of probably, like, more than 10x for the updating case.
[5425.18 --> 5429.98]  It was to the point where Ember 1.x, the demo basically froze.
[5430.70 --> 5434.96]  And Ember 2.x, it effectively shows fast updates.
[5435.12 --> 5440.58]  It shows everything updating many times per second, basically, instead of being frozen.
[5440.90 --> 5442.62]  So, very big improvement.
[5442.62 --> 5446.62]  However, Glimmer 1.x did not really do much for initial render performance.
[5447.36 --> 5451.76]  And, in fact, for various and sundry reasons, it regressed initial rendering performance.
[5452.32 --> 5459.40]  And, unfortunately, because re-rendering was so slow before Glimmer, almost nobody had applications that were doing a lot of re-rendering,
[5459.72 --> 5463.56]  which meant that all the work we did to improve re-rendering didn't affect existing apps much.
[5463.84 --> 5468.88]  It did let you write new apps better that would take advantage of it, but it didn't affect existing apps.
[5468.88 --> 5471.92]  But all existing apps got slower because the initial render got slower.
[5471.92 --> 5474.00]  So, that made people rightly sad.
[5475.18 --> 5484.64]  And we've done a lot of work since then to close the gap just by, you know, picking away at little paper cuts that we had introduced for various reasons.
[5484.82 --> 5486.80]  A lot of them were compatibility, but not all of them.
[5487.56 --> 5496.18]  And the idea behind Glimmer 2 is to say, okay, now that we have integrated Glimmer into Ember, what have we learned about what the requirements are, right?
[5496.18 --> 5501.04]  So, one of the reasons why things were so slow the first time, I'm being very rough on myself.
[5501.04 --> 5501.32]  Right.
[5501.32 --> 5511.22]  The reason why performance regressed after Glimmer 1 was that we effectively had to learn what the requirements for Ember compatibility were as we were integrating it.
[5511.50 --> 5516.70]  And as you can imagine, like as a programmer, sometimes the way you solve problems like that is you just do whatever.
[5517.16 --> 5519.06]  You do whatever you have to do to get past the problem.
[5519.06 --> 5523.76]  And we did that enough times that things didn't compose very performantly.
[5524.56 --> 5533.52]  But now that we're done, now that we've done all the integration against the more React style of internals model, we kind of know what all the requirements are.
[5533.52 --> 5538.66]  And so, the idea behind Glimmer 2 is to rebuild the primitive layer against the new requirements.
[5539.40 --> 5548.90]  And we have some benchmarks now that we've been running for a while that show many, many X performance improvement on initial render.
[5548.90 --> 5556.10]  And things like beating React on equivalent templates.
[5556.70 --> 5560.24]  So, like beating React by a decent amount on equivalent templates.
[5560.70 --> 5563.18]  So, we're definitely pretty excited about that.
[5563.84 --> 5569.82]  One of the things that is, like one of the things that I've been working towards that we haven't quite done yet, but is going to be pretty awesome.
[5569.82 --> 5576.88]  One of the things that I've been working towards is, so Ember's story about templating the whole time has been that we give you a declarative templating layer.
[5576.96 --> 5580.62]  So, you just write your HTML and you write, you don't write JavaScript in there.
[5580.72 --> 5586.10]  You write basically direct what I guess Angular called directives, but I mean the English form.
[5586.46 --> 5589.26]  You write directives that say this is an if statement, whatever.
[5590.04 --> 5594.06]  And historically, that whole system has been pretty dynamic.
[5594.38 --> 5598.52]  Like we sort of compiled it and then we said we don't really know what this if statement is talking about.
[5598.52 --> 5600.44]  So, just figure it out at runtime.
[5601.04 --> 5604.58]  But we noticed a pattern, which is that a lot of times people will make components.
[5605.26 --> 5607.94]  So, there's this project called Font Awesome, which is pretty cool.
[5609.16 --> 5615.68]  And people write components that wrap Font Awesome so that instead of having to say like I class equals F A space F A bug or whatever,
[5616.10 --> 5619.98]  they'll make an Ember component called F A icon and they'll say like F A icon icon equals bug.
[5620.36 --> 5622.32]  And it will basically emit the correct code.
[5622.92 --> 5627.98]  But if you look at that invocation, icon equals bug, you'll see that there's nothing dynamic about that at all.
[5627.98 --> 5629.96]  They're literally using the string bug.
[5630.34 --> 5637.16]  So, in an ideal world, you'd be able to take the template that is talking about the layout for that component and you would be able to notice,
[5637.32 --> 5642.70]  ah, that is actually not talking about a dynamic thing and compile it into the static thing that it is really talking about.
[5642.70 --> 5652.60]  And one of the goals of Glimmer 2 is to have a sufficiently flexible compilation architecture that we can effectively do these specializations at runtime.
[5652.84 --> 5654.56]  Do them only for hot code.
[5654.70 --> 5659.10]  So, like if you probably don't need to do that if it's only if the F A icon only shows up one time.
[5659.40 --> 5661.64]  But if it's in a loop, probably matters more.
[5661.64 --> 5662.08]  Yeah.
[5662.14 --> 5668.84]  So, basically to have a flexible architecture that lets us say, you know, we notice that this thing is a lot more static than the code would imply.
[5669.32 --> 5672.50]  So, let's actually compile it into the static form.
[5672.50 --> 5681.86]  And this is all owed to the fact that the Glimmer and like Ember templating system is like a pretty nice programming language for optimizations in general.
[5682.00 --> 5685.32]  So, it's like more like a referentially transparent programming language.
[5685.44 --> 5688.92]  It doesn't allow you to do a lot of the dubious things that make it hard to do optimizations.
[5688.92 --> 5698.62]  So, we can apply like the beginner level optimizations that you learn in school against this very simplified programming language and have and be able to do that reliably.
[5699.58 --> 5706.76]  So, that's basically the story behind Glimmer 2 is that we're restructuring the architecture so that it's a flexible compilation architecture.
[5707.08 --> 5714.94]  And then we can make things that are static behave as if they were static instead of behaving as if they were dynamic.
[5714.94 --> 5719.96]  And so far, the work that we've done on this kind of stuff has shown very significant improvements.
[5720.48 --> 5721.56]  So, we're pretty happy about that.
[5721.94 --> 5725.52]  I'm probably one of the people that's putting my hand up saying, I don't know how you do all you do.
[5725.80 --> 5739.64]  But nonetheless, we are definitely still thankful for one, you know, here at this podcast, just thankful for your time to come on today and share your personal story, your story on JSON API and how that plays out for developers.
[5739.64 --> 5748.86]  And a consistent API and a future-proofing in a way for the future, but also the work you're doing at Ember and your company, all that you do there.
[5749.08 --> 5753.18]  And the different products, I guess, you're working on as well would play into that as well.
[5753.56 --> 5759.36]  But Yehuda, we're about 10 minutes past our time, so we're going to close the show today.
[5759.44 --> 5763.12]  We did have a couple of questions we want to ask you, but we'll save those for a different day.
[5763.18 --> 5764.04]  I'm sure you'll be back on.
[5764.10 --> 5765.72]  This is not your last time on the show, I'm sure.
[5766.34 --> 5768.40]  So, let's close there.
[5768.40 --> 5771.78]  We want to thank our listeners for coming and listening to the show religiously.
[5772.48 --> 5773.66]  It is the new year.
[5773.76 --> 5775.52]  We have a great year planned ahead of us.
[5776.20 --> 5777.94]  And if you're not a member yet, go check that out.
[5778.32 --> 5780.08]  ChangeLaw.com slash membership.
[5780.84 --> 5789.36]  For $20 a year, you can support this show and do what we do around here and get an all-access pass back to our members-only Slack channel.
[5789.48 --> 5790.38]  Hang out with us.
[5790.86 --> 5791.78]  Get behind the scenes.
[5792.02 --> 5794.66]  We share lots of stuff with our members before we even share it with the rest of the world.
[5794.66 --> 5799.28]  We also had some awesome sponsors sponsored the show, so thanks to those guys.
[5800.12 --> 5804.94]  And Yehuda, if you have a second, you can throw a note on this if you'd like to.
[5805.42 --> 5812.04]  But our next show is actually about 0DB, an end-to-end encrypted database protocol with McLean Wilkinson and Michael.
[5812.04 --> 5816.26]  I'm not sure how you say his last name, but that was a really interesting find recently.
[5817.56 --> 5819.18]  And that's the next show we're doing.
[5819.82 --> 5820.60]  So, that's it.
[5820.68 --> 5822.52]  Any notes you have on that show particularly?
[5822.94 --> 5824.20]  That seems cool.
[5824.34 --> 5831.72]  I'm generally very pleased about the fact that our community and our ecosystem is pretty encryption-friendly.
[5831.98 --> 5836.00]  And I think the government would like it to not be so.
[5836.12 --> 5836.34]  Right.
[5836.34 --> 5841.74]  And unfortunately, people like encryption, and I'm happy that that's true.
[5841.94 --> 5842.34]  That's cool.
[5843.26 --> 5843.80]  All right.
[5843.86 --> 5845.36]  Well, everybody, thanks for listening.
[5845.48 --> 5846.44]  That is the end of the show.
[5846.56 --> 5848.70]  So, everybody on the show, let's say goodbye.
[5849.38 --> 5849.68]  Goodbye.
[5849.82 --> 5850.20]  Thanks, Yehuda.
[5850.60 --> 5851.08]  No problem.
[5851.08 --> 5851.14]  No problem.
[5851.14 --> 5851.22]  No problem.
[5851.22 --> 5853.26]  No problem.
[5853.26 --> 5855.08]  No problem.
[5855.08 --> 5855.28]  No problem.
[5855.28 --> 5856.08]  No problem.
[5856.08 --> 5857.50]  No problem.
[5857.50 --> 5861.08]  No problem.
[5861.08 --> 5863.58]  No problem.
[5863.58 --> 5864.10]  No problem.
[5864.10 --> 5865.20]  No problem.
[5865.20 --> 5866.00]  No problem.
[5866.08 --> 5866.36]  No problem.
[5866.42 --> 5866.92]  No problem.
[5867.12 --> 5867.86]  No problem.
[5867.86 --> 5867.90]  No problem.
[5871.96 --> 5872.88]  No problem.
[5874.46 --> 5876.44]  No problem.
[5878.94 --> 5879.94]  No problem.
[5879.94 --> 5880.92]  No problem.
[5881.04 --> 5881.12]  No problem.
[5882.06 --> 5882.08]  No problem.
[5882.14 --> 5882.26]  No problem.
[5882.26 --> 5882.54]  No problem.
[5882.54 --> 5883.00]  No problem.
[5883.14 --> 5884.48]  No problem.
[5884.48 --> 5884.70]  No problem.
[5884.70 --> 5885.30]  Okay.
[5885.58 --> 5886.64]  No problem.
[5886.64 --> 5886.90]  No problem.
[5886.90 --> 5887.70]  No problem.
[5887.70 --> 5888.78]  No problem.
[5888.78 --> 5888.84]  No problem.
[5888.86 --> 5889.16]  No problem.
[5889.42 --> 5890.06]  No problem.
[5890.06 --> 5890.66]  No problem.
[5890.66 --> 5891.74]  No problem.
[5891.74 --> 5892.08]  No problem.
[5892.20 --> 5893.16]  No problem.
[5893.16 --> 5893.38]  No problem.
[5893.38 --> 5894.16]  No problem.
[5894.16 --> 5894.70]  No problem.
[5894.70 --> 5895.26]  No problem.
[5895.36 --> 5895.74]  No problem.
[5895.74 --> 5895.86]  No problem.
