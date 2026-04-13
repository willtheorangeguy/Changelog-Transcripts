[0.00 --> 2.58]  Bandwidth for ChangeLog is provided by Fastly.
[2.96 --> 4.86]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at ChangeLog because of Rollbar.
[8.30 --> 9.98]  Check them out at Rollbar.com.
[10.24 --> 12.40]  And we're hosted on Linode cloud servers.
[12.76 --> 14.76]  Head to linode.com slash ChangeLog.
[19.28 --> 21.88]  This episode is brought to you by DigitalOcean.
[22.20 --> 26.96]  DigitalOcean's developer cloud makes it simple to launch in the cloud and scale up as you grow.
[26.96 --> 38.64]  They have an intuitive control panel, predictable pricing, team accounts, worldwide availability with a 99.99 uptime SLA and 24-7, 365 world-class support to back that up.
[38.90 --> 44.36]  DigitalOcean makes it easy to deploy, scale, store, secure, and monitor your cloud environments.
[44.74 --> 48.16]  Head to do.co slash ChangeLog to get started with a $100 credit.
[48.48 --> 50.64]  Again, do.co slash ChangeLog.
[56.96 --> 63.36]  Welcome to JS Party, your weekly celebration of JavaScript and the web.
[63.56 --> 68.46]  If you aren't following JS Party FM on Twitter, you're missing out on notifications for the live show,
[68.70 --> 73.64]  clips and highlights from past episodes, links and repos from around the community, nerdy memes, and more.
[74.06 --> 79.16]  Also, our rivals over at GoTime have been talking smack because they have twice as many Twitter followers as we do.
[79.16 --> 81.82]  Help us show those gophers that JavaScript reigns supreme.
[82.32 --> 83.60]  Follow us. You won't regret it.
[83.76 --> 84.72]  All right. Party time, y'all.
[86.96 --> 89.48]  Welcome to JS Party.
[90.40 --> 99.68]  I am excited to be here this week following the last time I was on was JS Jeopardy where I don't think Chris is going to talk to me ever again.
[99.90 --> 102.54]  That's why we are not joined by him this week.
[102.62 --> 105.04]  But we are joined by the...
[105.04 --> 110.52]  I wanted to use the adjective velvety, but I couldn't put that in a sentence without being creepy.
[110.52 --> 118.36]  We are joined by Jason Langsdorf, who is one of my favorite people to follow on Twitter and in real life.
[118.44 --> 121.12]  But that sounds creepy too when I say I shouldn't record this late at night.
[122.44 --> 123.60]  Welcome to the podcast.
[126.34 --> 133.52]  You want to go ahead and introduce yourself, Jason, and tell us a little bit about you and who you are and what you like to do besides cook meat.
[133.52 --> 140.86]  Yeah. So I cook. I've just learned that I am now trying to avoid Emma following me in real life.
[142.96 --> 144.96]  So I work at Netlify.
[145.18 --> 148.52]  I'm a principal developer experience engineer, which is kind of a...
[148.52 --> 153.30]  It's like some dev rel and some engineering and a lot of other things in between.
[153.74 --> 159.12]  Prior to that, I worked as the head of dev advocacy or developer relations at Gatsby.
[159.78 --> 165.86]  And prior to that, I was a friend and architect at IBM, which is actually where I met Emma back in the day.
[166.06 --> 168.84]  Outside of work stuff, I'm a big fan of cooking.
[169.40 --> 171.40]  I'm also a hobbyist bartender.
[171.56 --> 174.62]  So I collect weird booze and mix it all together.
[174.68 --> 175.78]  And sometimes it tastes good.
[175.78 --> 179.26]  Other times you don't remember if it tastes good.
[183.00 --> 185.98]  Yeah, yeah. That's effectively who I am, I think, in a nutshell.
[186.92 --> 189.94]  That's awesome. And yeah, thanks for that intro.
[190.20 --> 194.68]  And K-Ball, you are also with us. Would you like to say hello to the lovely people?
[195.16 --> 195.84]  Hello, hello.
[196.84 --> 200.28]  I will note, Jason has been on before talking about Gatsby.
[200.28 --> 204.18]  And it was, I believe, one of our top 10 most popular episodes to date.
[204.18 --> 208.48]  So Jason, let's see if you can beat that with this one.
[209.94 --> 213.70]  Yes, I will attempt to be very engaging.
[214.54 --> 218.30]  Awesome. No pressure, but Dustin in the chat says that you are the best.
[218.46 --> 220.32]  And this is just a reminder for everyone listening.
[220.52 --> 224.56]  If you don't follow our live recordings or you aren't in our Slack channel,
[224.60 --> 226.96]  you should definitely join because it's a boatload of fun in there.
[226.96 --> 232.48]  And in any case, today we are here to talk about building courses, technical courses.
[232.48 --> 236.72]  This is something I think a lot of people are interested in, but I haven't seen a lot of content
[236.72 --> 241.86]  on how to be successful at building courses and teaching people and things like that.
[241.92 --> 248.02]  And Jason is exemplary in this area because he does his Learn with Jason show that I would love to talk more about.
[248.02 --> 251.74]  So you've also done some front and master's courses.
[251.96 --> 255.06]  I know that because I've watched them and I've gotten a lot of value out of them.
[255.36 --> 260.50]  Could you give us a little overview of your history teaching courses and all that jazz?
[261.22 --> 261.56]  Yeah.
[262.06 --> 267.62]  I started almost by accident because I was in Montana.
[268.30 --> 270.06]  And in Montana, there weren't a lot of developers.
[270.20 --> 273.00]  This was kind of pre-Stack Overflow.
[273.00 --> 279.50]  So there was really the way that you learned was either by buying books or you would do things like hang out on the W3 schools forum.
[280.16 --> 286.54]  And if any of you are remembering what that was like, you know, hi, you're old just like me.
[291.42 --> 297.14]  But so in Montana, there, you know, I grew up in a place called Whitefish where there was not really a developer community at all.
[297.28 --> 300.00]  And then I relocated to a place called Missoula, Montana.
[300.00 --> 304.90]  And in Missoula, there was this developer group, but there wasn't any specialization.
[305.08 --> 307.78]  People just were like, hey, we work on computers.
[307.78 --> 308.88]  Should we hang out?
[309.22 --> 310.96]  And, you know, one of us did PHP.
[311.38 --> 312.42]  Somebody was front end.
[312.50 --> 313.40]  Somebody was Java.
[313.60 --> 318.64]  And like we didn't know anything about what anybody else was doing, but we wanted to be friends.
[318.64 --> 318.90]  Right.
[318.90 --> 319.96]  So we had to give these talks.
[319.96 --> 327.18]  And I got volunteered to give a talk on PHP at the time and just kind of walked through some of the features.
[327.30 --> 331.64]  This was when PHP six was, I think, in like year two of being about to be released.
[331.64 --> 336.50]  And I was going through like the the changes and what was new.
[336.50 --> 339.40]  And in doing that, I thought I was going to hate it.
[339.44 --> 340.40]  I thought it was going to be terrifying.
[340.50 --> 342.20]  And it ended up being really fun.
[342.40 --> 345.16]  So I started seeking out opportunities to do that.
[345.22 --> 348.44]  I applied to conferences to give talks and teach workshops.
[348.84 --> 354.80]  As I got into companies where it wasn't just me, I would do internal workshops at IBM.
[354.80 --> 358.04]  For example, I did a lot of internal training there.
[358.22 --> 363.66]  We had a couple of groups there where we would do like front end kind of a front end get together where we get breakfast tacos.
[363.66 --> 367.52]  It was this really cool event put on by Kelly Churchill and Jessica Tremblay inside the company.
[367.66 --> 370.60]  We did these other things where it was just kind of like team specific stuff.
[371.26 --> 381.38]  And yeah, I've just I've been doing a lot of workshop stuff at events and in person and then started recently getting more into the online stuff.
[381.38 --> 386.14]  So learn with Jason is an online kind of live coding less so than workshop.
[386.26 --> 388.26]  But then I make egghead courses.
[388.26 --> 393.64]  I make front end master's courses and I do a lot of tutorial writing for, you know, the Netlify blog.
[393.66 --> 401.32]  And the learn with Jason blog, a couple other things like Smashing Magazine, CSS tricks, where I'm trying to help people get familiar with new concepts.
[402.14 --> 408.22]  You're saying all these really great names of companies, which we will link all these in the show notes as well.
[408.38 --> 413.18]  But that's an incredible backlog of companies that you've worked with, like extremely notable people.
[413.18 --> 416.62]  So I'm excited to kind of like dive into that a little bit more.
[416.98 --> 418.68]  I remember we had a conversation at IBM.
[418.82 --> 424.12]  So for those who don't know, we met at IBM back in, I want to say like 2017, 2016.
[424.84 --> 431.32]  And I had just joined a design team and I was really passionate about mentorship and I was trying to start a mentorship program there.
[431.82 --> 437.68]  And Jason was one of the few daring souls who signed on to help me, which was really, really nice.
[437.72 --> 438.40]  And that's how I met him.
[438.96 --> 444.14]  But I remember you and I having a conversation where I asked you, I was like, how do you get to travel so much?
[444.14 --> 445.30]  Like, how do you go to conferences?
[446.20 --> 447.92]  And you were like, well, you know, it's a thing.
[447.98 --> 452.20]  Like you just apply to conferences and like they'll, you know, sometimes they'll help you travel.
[452.34 --> 453.58]  And I remember that moment.
[453.58 --> 455.08]  I was like, I'm going to speak at a conference.
[455.08 --> 457.22]  And you motivated me to speak at a conference.
[457.22 --> 458.34]  So it's really cool.
[458.42 --> 461.78]  I feel like I idolize you in a lot of ways because you are such a good teacher.
[461.94 --> 466.00]  And I remember I also saw your talk in Budapest at CraftConf.
[466.48 --> 467.70]  Not last year, the year before.
[467.90 --> 468.34]  Oh, yeah.
[468.66 --> 470.06]  It was a couple of years ago.
[470.12 --> 470.26]  Yeah.
[470.30 --> 474.04]  I think it was the last time you gave your talk about your beard falling out.
[475.38 --> 479.02]  Which I'm glad to see it is back in business.
[479.28 --> 480.34]  It's back in business.
[480.96 --> 483.46]  But Jason gave a really great talk about work-life balance.
[483.58 --> 483.78]  I forget.
[483.84 --> 484.72]  What was the name of it?
[484.72 --> 488.32]  How you work half as many hours and got more done?
[488.32 --> 488.60]  Yeah.
[488.76 --> 492.20]  How I cut my, I think, how I cut my working hours in half and got more done.
[492.70 --> 493.96]  Or something to that effect.
[494.54 --> 498.62]  That was such a great talk because you are so good at storytelling.
[498.94 --> 502.48]  And I think that definitely translates into your ability to teach people.
[502.88 --> 503.60]  Teaching is hard.
[503.72 --> 505.46]  And I think anyone can teach.
[505.64 --> 508.40]  And I think everyone has something valuable to offer.
[508.50 --> 513.10]  But it takes a certain kind of person to be able to reach everyone, you know?
[513.10 --> 518.80]  And so I'm excited to talk a little more about, like, what makes a great teacher and how do you actually build a course.
[519.54 --> 522.36]  Cable, do you have experience with courses, like building online courses?
[522.86 --> 523.26]  I do.
[523.44 --> 524.76]  I've built a couple, actually.
[525.00 --> 529.32]  I don't have quite the depth of experience that Jason has.
[529.46 --> 538.24]  But I built a small, fully video course for Skillshare on building SVGs and writing SVGs as code.
[538.34 --> 541.18]  And thinking about SVGs and how you animate them and do things with that.
[541.18 --> 546.10]  And I've done a few different, more interactive webinar-based courses.
[546.32 --> 549.80]  I did a bunch on Zurb Foundation when I was working at Zurb.
[549.92 --> 554.44]  And I've done a couple on Vue.js.
[555.16 --> 564.20]  And one of the things I'd be really interested in exploring today is the different modes of creating courses and what courses can look like.
[564.30 --> 566.12]  Jason, you mentioned in-person workshops.
[566.22 --> 568.40]  You've got this live experience with Learn with Jason.
[568.40 --> 572.92]  You've got fully pre-recorded video courses.
[573.38 --> 578.16]  And I've found in my experience, I didn't mention, but I have led some in-person workshops as well.
[578.28 --> 583.18]  So in my experience, each of those mediums has different pros and cons to it.
[583.38 --> 583.78]  Right.
[583.92 --> 585.86]  And both for the teacher and for the students.
[585.86 --> 597.72]  And so I think one really interesting thing we could talk about here, I think a lot of times when people think about building courses, they think, oh, I'm going to build something fully automated for Udemy.
[597.84 --> 599.48]  And it's going to be completely passive income.
[599.48 --> 603.56]  And yay, you know, I won't have to work anymore in five years or something like that.
[603.56 --> 611.12]  And that's only one very small slice of what the world of training and courses looks like.
[611.34 --> 617.14]  And I think it is perhaps not quite what people think it is.
[617.32 --> 625.20]  So I think one thing we could do that would be pretty interesting was like talk about those different modes and what are the pros and cons of each of them.
[625.20 --> 632.16]  Yeah, I mean, the first thing that comes to mind is when you talk about passive income, like passive income is not passive.
[632.54 --> 635.82]  And I think that's a very important thing to learn.
[635.82 --> 642.56]  Like you look at somebody like Wes Boss, who has this collection of courses and he's making his living off of it.
[643.10 --> 652.80]  He's working just as hard, if not harder than most of us to keep that, you know, quote unquote, passive income where people are buying his courses and they're self-directed.
[652.80 --> 659.08]  Like when you hear him talking, he has to go through and update them all to be using the modern things.
[659.08 --> 660.44]  He's got to do the marketing.
[660.58 --> 663.52]  He's got to do the like the support when people get stuck.
[663.52 --> 668.46]  And there's a lot of a lot of things that have to happen to make passive income actually passive.
[669.12 --> 673.98]  And typically speaking, unless you're making bucket loads of money, that's all work that you have to do.
[674.22 --> 682.78]  So it's it's definitely a consideration there that, you know, like if if your goal for making a course is to make passive income, you may want to reconsider that because it is actually a lot of money.
[682.80 --> 684.60]  A lot of work to make passive income.
[685.58 --> 689.14]  And many courses aren't going to be big hits.
[689.24 --> 689.58]  That's true.
[689.92 --> 694.60]  I think, you know, if I look at and they take a lot of time to put together.
[694.72 --> 700.78]  So if I look at the money I've made from courses now, I have not gone fully on courses and I have not.
[700.92 --> 703.02]  There's a lot of things I've done that are probably suboptimal.
[703.12 --> 708.38]  But if you take that and divide it by the number of hours that I've put there, it's way less than my freelancing rate.
[708.38 --> 710.24]  Yeah, for sure.
[710.52 --> 722.60]  I just gave my first course back in February, maybe January with LinkedIn Learning, which was formerly Linda dot com, which for my first course was like super.
[722.88 --> 724.20]  That's at the bar so high.
[724.56 --> 729.64]  And it's really interesting to see because I have I'm actually doing my first run in master's course in one week.
[729.72 --> 730.48]  Oh, cool.
[731.04 --> 731.90]  Yeah, it's exciting.
[731.98 --> 732.90]  But I'm also terrified.
[732.90 --> 735.86]  But it's interesting to see how different companies operate.
[736.10 --> 738.58]  So like Linda was very, very structured.
[738.78 --> 740.40]  You had weekly meetings with your producers.
[740.96 --> 745.54]  I'm sure you can attest to this to Jason that like front and masters is very much like on you, which is great.
[745.54 --> 747.34]  But it's also like, oh, there's no accountability.
[747.62 --> 748.56]  But then you have Egghead.
[748.98 --> 750.92]  Egghead is very much also self-directed.
[750.98 --> 753.40]  But each of these have different payment like plans.
[753.50 --> 754.40]  I don't like payment plans.
[754.44 --> 757.12]  That's not the right phrase, but different payment structures, I guess.
[757.12 --> 762.78]  And so, yeah, to the point of like passive income, some companies will actually pay you up front to work.
[763.02 --> 764.86]  And then you'll also make royalties off that.
[765.18 --> 767.88]  But some companies, you're solely on royalty based income.
[768.00 --> 769.34]  And so it really just kind of varies.
[769.46 --> 773.38]  But agreed, the amount of work you put into a course is absurd.
[773.50 --> 774.78]  And then you also have to update it.
[774.88 --> 777.62]  So I wanted to just mention a few of my favorite course makers.
[778.32 --> 781.96]  So to the West boss, like tangentially is Scott Talinsky.
[782.18 --> 782.92]  He's incredible.
[783.16 --> 784.64]  His level up tutorial site.
[784.74 --> 786.58]  I have taken so many courses on there.
[786.58 --> 789.16]  He's a great teacher, but he's always updating it.
[789.40 --> 790.42]  Tyler McGinnis as well.
[790.54 --> 792.56]  Loved all his React and JavaScript stuff.
[792.90 --> 794.32]  Dave Cetia works really hard.
[794.72 --> 796.12]  And Bianca Gandolfo.
[796.24 --> 799.86]  I liked her courses over on Frontend Masters as well.
[800.00 --> 805.92]  So, you know, you can tell great teachers that they make it seem so easy.
[806.10 --> 811.02]  But when you look at the amount of work they've put into it, it's like, oh, that's why you're so good at this, right?
[811.60 --> 811.84]  Right.
[812.46 --> 812.70]  Yeah.
[812.74 --> 814.38]  I mean, it's a performance art, really.
[814.38 --> 819.04]  If you think about what a workshop is, you're not just sharing information.
[819.16 --> 821.66]  If you were just sharing information, you'd be writing an article or a book.
[821.66 --> 834.76]  And so when you take that to the next step, what you're trying to do is you're trying to get someone not only to expose themselves to new information, but to engage with it and have kind of a guided experience, which takes it that next step.
[834.84 --> 835.82]  Now it's performance art.
[835.82 --> 844.48]  What you're trying to do is try to get somebody emotionally invested enough, intellectually invested enough in whatever the subject matter is that they want to do that work now.
[844.68 --> 845.66]  They're in with the group.
[845.76 --> 846.80]  They want to get something done.
[846.90 --> 849.24]  You're all pulling together to get to an outcome.
[849.24 --> 852.04]  And I think that's where it starts to really land.
[852.16 --> 856.46]  And that's where you get the benefit of a workshop versus just reading an article by yourself.
[856.74 --> 858.34]  You can see when people practice that.
[858.34 --> 869.00]  Well, and that actually comes to a pretty interesting point about courses, which is how do you as a teacher think about keeping your students motivated and going through the course?
[869.00 --> 876.20]  Now, in a workshop setting, they'll tune out, but they probably won't leave if it's a single workshop for a couple hours.
[876.60 --> 888.88]  But if you're putting together an online course or a series of webinars or some other type of thing that requires ongoing commitment, I mean, one thing that I have seen in the courses that I've done is that a large percentage of people drop out.
[888.88 --> 906.96]  And that was even after for those courses, particularly for the webinar-based ones, I thought a lot about how do I motivate and try to cut that off and kind of get people past the feeling of, oh, I'm not getting this, so maybe I can't get this, so I'm going to stop or what have you.
[907.34 --> 909.40]  But it wasn't fully successful.
[909.86 --> 912.54]  I'm curious how the two of you think about that.
[912.54 --> 923.58]  How do you think about the kind of human, not just the skill transfer that you're doing, but the motivational and the sequencing such that people feel engaged and continue to be motivated throughout the course?
[924.14 --> 925.22]  You want to take the first shot at that?
[926.18 --> 926.38]  Yeah.
[926.56 --> 932.46]  So we talked with Angie Jones, who is an incredible person, but also an amazing teacher.
[932.56 --> 933.60]  She does a lot of testing.
[933.76 --> 935.02]  I think testing JavaScript.
[935.68 --> 937.80]  She has a, we'll link it in the show notes as well, but she's a great teacher.
[937.80 --> 938.70]  Testing Automation University.
[938.94 --> 940.38]  Testing Automation University.
[940.38 --> 940.82]  Thank you.
[940.82 --> 943.06]  And we talked about how people learn.
[943.30 --> 946.62]  And I think knowing how people learn and digest information is very important.
[947.14 --> 956.54]  And one of the things that we discussed with her and Allie, Allie Spittles, also an educator at General Assembly, is this idea of having I do, we do, you do activities.
[956.54 --> 958.42]  So I'm going to show you something.
[958.60 --> 959.76]  We'll do something together.
[959.76 --> 964.70]  And then you do this based on the skills I've just, we've just done together and that I've just shown you.
[964.70 --> 976.48]  And I think having this reinforcement, having small doable chunks of information, but also letting them abstract out some of these skills and try it on their own is one way to really kind of like drive home certain points.
[977.18 --> 977.64]  I love that.
[977.92 --> 985.06]  I feel like that takes something very big and academic and turns it into something, you know, repeatable.
[985.14 --> 985.50]  I do.
[985.62 --> 985.96]  We do.
[986.06 --> 986.34]  You do.
[986.44 --> 988.28]  That's like, I'm going to take that one to the bank.
[988.36 --> 989.48]  Thank you for that.
[989.48 --> 994.02]  That's a great show note or a title of this episode.
[994.14 --> 997.00]  I think that's a, you know, it's a memorable phrase.
[997.10 --> 999.54]  And that's what I like when I was writing down my courses.
[999.54 --> 1000.82]  I'm like, this is what I need to do.
[1000.86 --> 1001.30]  This is great.
[1001.90 --> 1003.38]  Yeah, it's a really great idea.
[1004.06 --> 1011.54]  And what I was going to say is, I think, just to echo what you just said, that like understanding the different ways that people learn.
[1011.54 --> 1019.26]  And I think there are a lot of different axes just inside that sentence because you have like the actual media.
[1019.26 --> 1027.10]  Are they learning through written word, through, you know, person to person interaction, through video, through, you know, seeing example.
[1027.30 --> 1029.14]  Everybody's got their preferred learning modes.
[1029.14 --> 1033.58]  And then you've got like what they're doing in that media.
[1034.22 --> 1044.74]  So if it's a video and all they do the whole time is watch, then that can get really kind of monotonous and you can you can find yourself tuning out and it's hard to stay with it.
[1045.10 --> 1047.50]  But if the whole thing is doing, then you can get frustrated.
[1047.50 --> 1050.18]  Like, well, why am I not just doing this by myself?
[1050.22 --> 1053.10]  Why am I paying somebody to, you know, to watch me work?
[1053.10 --> 1067.34]  So finding a good blend and going through the point where you're, you know, you're providing engaging information and almost like entertainment on the how to learn this thing and then making sure that that you break up that flow.
[1067.34 --> 1076.48]  Like I talked to Sarah Jasner about this, who has done like hundreds of workshops and is just like a truly fantastic educator.
[1076.48 --> 1094.06]  And she always talks about that like this, you know, the idea is that you're you're trying to move people into different modes of thinking to let them, you know, experience the thing, take it in visually, take it in auditorily, but then actually try it and then get feedback.
[1094.68 --> 1098.82]  And so there's all of these different modes that you're trying to move people in and out of as they as they go.
[1098.98 --> 1102.48]  And that is like that's a really powerful approach in this.
[1102.48 --> 1108.42]  We haven't read this yet, but our book club we're doing we're reading Make It Stick, which was picked by Allie.
[1108.66 --> 1112.14]  And it's about how people actually learn the science behind learning, I believe.
[1112.28 --> 1113.64]  And so I'm excited to read it.
[1113.66 --> 1120.94]  But if you're thinking about getting into teaching or you are a teacher, I would highly recommend checking it out because I skimmed it and it looks really, really interesting.
[1121.24 --> 1123.22]  With that, I think let's take a break.
[1123.26 --> 1126.50]  And when we come back, we'll talk about how you can actually get started building a course.
[1132.48 --> 1139.52]  We deserve a better Internet.
[1139.52 --> 1142.82]  And the brave team has the recipe for bringing it to us.
[1142.94 --> 1143.94]  Start with Google Chrome.
[1144.16 --> 1147.90]  Keep the extensions, the dev tools and the rendering engine that make Chrome great.
[1148.08 --> 1148.96]  Rip out the Google bits.
[1149.12 --> 1149.76]  We don't need them.
[1150.10 --> 1152.60]  Mix in ad and tracker blocking by default.
[1152.86 --> 1157.48]  Quick access to the Tor network for true private browsing and an opt in reward system.
[1157.48 --> 1160.30]  So you can get paid to view privacy respecting ads.
[1160.52 --> 1164.26]  Then turn around and use those rewards to support your favorite web creators like us.
[1164.60 --> 1169.16]  Download Brave today using the link in the show notes and give tipping a try on changelog.com.
[1179.80 --> 1186.66]  So we talked a little bit about our backgrounds of teaching and how people learn at a high level and why that's important.
[1186.66 --> 1191.94]  But I want to shift gears and talk about how do you actually go about building an online course.
[1192.10 --> 1199.44]  So I think and I know, Jason, you added some of your thoughts, but let's talk a little bit about formats for creating courses and the different types those can take.
[1199.52 --> 1201.14]  I'm going to let you start in on that.
[1201.62 --> 1201.74]  Yeah.
[1201.84 --> 1206.92]  So formats, I think like the formats that I have seen.
[1206.92 --> 1212.48]  You've got like short form workshops, which is more of like a code along, right?
[1212.48 --> 1217.90]  You're going to do one small concept and you can typically do that in the span of a like a meetup, right?
[1217.92 --> 1220.00]  Like a 30 or 60 minute slot.
[1220.00 --> 1224.36]  And then you've got the half day and full day workshops, which are way more in depth.
[1224.44 --> 1229.86]  You're going to probably build something or a series of projects and those can be a little more in depth.
[1230.00 --> 1237.70]  They're typically more classroom style, but then you can take that whole thing and you can move it online and you can find yourself doing like.
[1237.70 --> 1246.20]  Well, like if you look at Getsky does like the games like CSS grid zombies, I think it is.
[1246.20 --> 1249.06]  They're like Frogger where you flex box froggy.
[1249.72 --> 1252.98]  Those those types of games were like those are effectively workshops, right?
[1253.00 --> 1253.72]  They're just fun.
[1253.86 --> 1254.06]  Yeah.
[1254.52 --> 1256.38]  And they're they're completely self-guided.
[1256.50 --> 1257.54]  It's a way to learn.
[1257.54 --> 1267.54]  So I think you kind of move on the spectrum in length and then you move on the spectrum in terms of level of human involvement, because I think there's, you know, the just straight up.
[1267.70 --> 1270.24]  Pair programming is kind of a workshop.
[1270.24 --> 1277.16]  If you think about it, like a senior dev sitting with a earlier career dev and and working through a problem, that's a workshop.
[1277.68 --> 1280.40]  And so all of those are things that are those skills transfer over.
[1280.50 --> 1287.42]  So even if you've never taught a workshop, but you've done a lot of pair programming, you actually have valuable experience that will help you make that kind of content.
[1288.24 --> 1289.52]  That's really interesting, actually.
[1289.66 --> 1296.16]  So like when you're saying that I'm thinking about there's sort of like there's a few different dimensions that this varies along.
[1296.16 --> 1301.08]  There's length, there's number or amount of personalization.
[1301.50 --> 1304.26]  You know, is this one-on-one you're reacting to that one person?
[1304.52 --> 1309.52]  Is this in a small group where you're maybe reacting to those three, but you have more of an agenda or what have you?
[1310.52 --> 1312.40]  There's delivery medium.
[1312.70 --> 1313.56]  You know, is this live?
[1313.66 --> 1315.36]  Is this by video?
[1315.52 --> 1316.30]  Is this written?
[1316.46 --> 1317.54]  Is this something like that?
[1318.02 --> 1320.06]  Are there any other dimensions that we're talking about?
[1320.06 --> 1326.56]  I guess the extent of how much doing is on which side of the person?
[1326.76 --> 1331.54]  Like, is it how much is it watching the teacher or learning from the teacher versus acting and doing?
[1332.00 --> 1336.72]  Yeah, it's I wanted to call out two people again who have very opposite formats.
[1336.90 --> 1340.18]  So what I've seen be very successful are two different approaches.
[1340.40 --> 1344.28]  One is you build a project from scratch from start to finish.
[1344.42 --> 1346.08]  And Brian Holt is an amazing teacher.
[1346.08 --> 1347.46]  And he does that very, very well.
[1347.94 --> 1356.68]  Wes Boss, I've seen him take another approach, which is doing very small, sizable examples in, you know, one video or two videos.
[1356.74 --> 1359.66]  And like he has very encapsulated different examples.
[1359.66 --> 1362.48]  So those are both very successful ways to go about it.
[1362.48 --> 1369.10]  And I would say, like, if you look at Egghead, Egghead's mantra is basically very short, consumable videos that can kind of also stand alone.
[1369.44 --> 1372.38]  Versus Front End Masters, I would say, it's more like a college lecture style.
[1372.38 --> 1377.28]  So it's really up to you in terms of the way that you want to go about it.
[1377.80 --> 1382.10]  I think what's interesting is also if you think about, like, how do you want to leverage this content?
[1382.22 --> 1382.36]  Right.
[1382.36 --> 1385.36]  So I'm going to take a little bit of a tangent, but I swear I'm bringing it back.
[1385.82 --> 1392.54]  So one of the things that you mentioned earlier, Kevin, was that, like, when we start these courses, they are a huge amount of work.
[1392.68 --> 1392.90]  Right.
[1392.94 --> 1394.92]  Like it's it's so much work to make this happen.
[1394.92 --> 1403.04]  And so if you're going to do that amount of work to really get full value out of it, how are you going to use that content in different ways?
[1403.18 --> 1409.16]  And so one of the things that that I've started looking at is this idea of multi leveraging time.
[1409.16 --> 1414.28]  I'm kind of organizing under this banner of like, you know, get five hours output for every one hour of work.
[1414.28 --> 1421.10]  And in doing that, what I'm looking at is like, OK, if I'm going to write a workshop on something, I'm not just going to say I have an idea.
[1421.24 --> 1423.76]  I'm going to spend six weeks writing a workshop.
[1423.90 --> 1424.88]  It's I have an idea.
[1425.00 --> 1426.64]  I'm going to tweet about this.
[1426.92 --> 1427.72]  Did people engage?
[1427.78 --> 1430.34]  Like, was this something that was everybody like, this is a terrible idea.
[1430.34 --> 1430.84]  Don't do it.
[1430.84 --> 1438.28]  And then if that gets or avoids blowback or it feels like it's something good, then, you know, maybe I'll I'll write an article about it.
[1438.34 --> 1442.04]  Or maybe I'll make an egghead video, which is, you know, two and a half, three minutes.
[1442.04 --> 1456.60]  And if those are all getting good feedback, then maybe I want to do an online workshop like egghead has a really cool online workshop format that I love where I can teach a short workshop, maybe two hours on a condensed version of this topic.
[1456.60 --> 1463.64]  And then if it's if all of these things are working, first of all, it's one idea that I've now used just in that format four different ways.
[1464.40 --> 1469.64]  And from that, then I know that I've got something good that that is helping people.
[1469.64 --> 1474.74]  It's getting like positive responses and people are learning the thing that I want them to learn.
[1475.16 --> 1479.62]  So I can then then I go and I look at like the huge, you know, the big thing.
[1479.68 --> 1486.24]  Do I want to try to turn this into a full on course on egghead, which is like the hour long collections of of more in-depth material?
[1486.34 --> 1489.96]  Do I want to go pitch a version of this to front end masters and do the full day thing?
[1490.28 --> 1494.10]  Do I want to pitch it to conferences as an actual like sit down in person workshop?
[1494.10 --> 1496.64]  But by that point, I've already done a lot of the work.
[1496.74 --> 1497.92]  I've already validated the idea.
[1498.10 --> 1499.80]  I've got most of the content put together.
[1500.36 --> 1506.52]  Now it's just extending it and expanding it with more information as opposed to saying, like, maybe I can make this work.
[1506.76 --> 1509.76]  Let's do tons and tons of work so I can go try this out.
[1509.96 --> 1511.26]  I love that.
[1511.52 --> 1512.28]  That's so funny.
[1512.66 --> 1519.66]  That's what I did this year, because last year was my first year speaking at conferences and I burned out because I did three different talks.
[1519.78 --> 1522.32]  I mean, that's insane, especially as a first time conference speaker.
[1522.32 --> 1525.30]  So this year I'm like, I'm going to do one conference talk.
[1525.56 --> 1527.20]  And I wrote it and it was about React Spring.
[1527.40 --> 1530.04]  And I took that and I wrote it as a Stack Overflow blog.
[1530.30 --> 1533.28]  And then I took that and I am turning it into an egghead course.
[1533.42 --> 1536.42]  And then I'm taking pieces of it and putting it into my front end masters course.
[1536.74 --> 1539.00]  So it's like, do the work once, do it well.
[1539.24 --> 1541.90]  And generally what I find is I'm writing outlines for these anyway.
[1542.24 --> 1543.74]  So outlines can turn into blog posts.
[1543.88 --> 1547.72]  Blog posts can be turned into short form courses and conference talk.
[1547.86 --> 1550.98]  You know, those can then go into larger courses and potentially even an e-book.
[1550.98 --> 1556.36]  Like, find ways to, like, multi-purpose your hard work.
[1556.46 --> 1560.26]  That is like, it's so funny that you brought that up because I was like, has anyone else been doing this?
[1560.30 --> 1561.00]  Like, is this cheating?
[1561.20 --> 1564.40]  Like, and no, it's like, that's actually a really good business model.
[1564.74 --> 1564.90]  Yeah.
[1564.98 --> 1569.18]  People ask me all the time, like, because I have this appearance of being very productive.
[1569.32 --> 1569.68]  Yeah.
[1569.68 --> 1571.92]  And it's because I put out a lot of content, right?
[1572.62 --> 1578.66]  And there are others in the industry who are the same way, like Sarah Drasner, Kent C. Dodds, Wes Boss, Chris Biscardi.
[1578.96 --> 1581.24]  It's like, wow, these people are fountains of content.
[1581.32 --> 1582.46]  How did they get so much done?
[1582.92 --> 1585.94]  But if you look at what they're doing, like, Kent is a good example.
[1586.12 --> 1589.42]  Every time that Kent does something, he writes a newsletter about it.
[1589.80 --> 1591.12]  He writes an article about it.
[1591.32 --> 1593.48]  He creates a video about that article.
[1593.48 --> 1599.48]  He then puts that article into a workshop and then he rolls up the workshops into a course.
[1599.64 --> 1603.76]  So he's not creating dozens of independent pieces of content.
[1603.76 --> 1611.86]  He's creating lots of interrelated, overlapping bits of content that repackage and repurpose that content to help people use it.
[1611.96 --> 1614.24]  And they can consume it through whatever media they prefer.
[1614.24 --> 1623.48]  But it also allows him to validate individual pieces of the curriculum and get those into the right place before they roll up into the full workshop.
[1623.48 --> 1640.20]  It's a way of, like, doing the work and getting feedback and potentially payment for pieces of the work before you, you know, spend the weeks of effort to do the thing that in a lot of cases, I mean, I can't tell you how many people I know who do a workshop one time.
[1640.20 --> 1645.60]  And it's like, how could you do that much work and give that workshop once?
[1645.94 --> 1647.30]  That's not a good return on investment.
[1647.70 --> 1656.66]  Well, yeah, I mean, it's there's no way it's going to I mean, you could I guess if you sell it out and you've got a really good deal with whatever venues holding the workshop, you might make a decent hourly rate.
[1656.72 --> 1659.92]  But typically speaking, the first time you give that workshop, you're going to take a loss.
[1660.64 --> 1664.74]  So giving it multiple times is how it turns into something that that actually makes money.
[1664.84 --> 1669.42]  You're just kind of amortizing the cost like you're going to do the work, but like spread it out and find ways to make that.
[1670.20 --> 1675.74]  Like feed multiple income streams for you as opposed to putting all of your eggs in the workshop basket.
[1677.26 --> 1686.56]  That's like if you take anything away from this, take that away, because that's it's honestly it's a brilliant thing because people always like like they tell you they'll ask me, how are you so productive?
[1686.64 --> 1690.24]  I'm like, I'm really not like I reuse my own material in different ways.
[1690.46 --> 1694.36]  I mean, obviously, I'll change like certain activities, but the premise will be the same.
[1694.36 --> 1694.92]  Mm hmm.
[1695.84 --> 1697.94]  Yeah, I get some of that as well.
[1697.94 --> 1700.20]  Less now that I actually have a real job.
[1700.50 --> 1705.68]  And I'm not just working on consulting plus content.
[1706.06 --> 1708.76]  But yeah, that said, I felt like I knew that lesson.
[1708.88 --> 1714.00]  But hearing Jason go through it step by step by step there, like you could take that package it.
[1714.06 --> 1714.62]  That's gold.
[1714.96 --> 1715.44]  Do that.
[1715.58 --> 1719.50]  Do exactly what Jason described or what he described Kent doing.
[1719.50 --> 1721.28]  Like it's pure gold.
[1721.28 --> 1726.58]  And even if you think you know it, like I was thinking as you're going through that, yeah, I reuse and I do this.
[1726.72 --> 1732.16]  But holy smokes, that is a tuned process you just described that is better than what I've been doing.
[1732.48 --> 1737.30]  Well, think about how we validate our assumptions in the professional workplace.
[1737.30 --> 1746.34]  Generally, if you're a larger company with a fleshed out design organization, you will validate your assumptions with user testing.
[1747.32 --> 1750.56]  And the same is, I mean, you are a valuable resource.
[1750.66 --> 1753.78]  Your time is a resource and it's a non-refundable resource.
[1754.50 --> 1755.92]  So you need to validate your assumptions.
[1756.14 --> 1757.98]  And what Jason said is, yeah, posting on Twitter.
[1758.10 --> 1762.74]  See if you get any feedback on that or post like a very short blog and validate your assumptions.
[1762.74 --> 1770.80]  But also one thing that I did for this upcoming course, because I'm kind of anxious that, like, I don't know.
[1770.86 --> 1779.76]  The first time you do a workshop is very anxiety inducing because you want to make sure that if people are paying for something that they are really, you're respecting their time and their money.
[1780.00 --> 1782.90]  So I had people in the industry, I just posted on Twitter.
[1783.00 --> 1784.98]  I was like, hey, would anyone be willing to vet my course?
[1785.38 --> 1786.96]  And I had them go through it.
[1787.06 --> 1788.30]  They opened pull requests.
[1788.30 --> 1799.30]  I had people who had actually built the technologies that I was using in my workshop, which was terrifying to have Max, one of the creators of style components, review my style components course.
[1800.60 --> 1804.54]  But then I also had complete beginners because it's important to get both sides.
[1804.68 --> 1812.20]  And I understand that everyone has the time and or the resources to get, you know, the creator of the technology to review your course.
[1812.30 --> 1817.22]  But vet it with people, vet it with people who have experience and with people who are beginners and see what they say.
[1817.22 --> 1821.60]  Because often you have tunnel vision and you're going to miss a lot of the things that they're bringing up.
[1822.08 --> 1822.24]  Totally.
[1822.98 --> 1825.80]  Yeah, I think that feedback is so valuable.
[1826.48 --> 1829.26]  I'm curious what the two of you have seen on that vetting front.
[1829.58 --> 1833.78]  So you try it first as a Twitter post and then you try it as a short article.
[1834.26 --> 1835.54]  Like, what's your funnel look like?
[1835.60 --> 1837.76]  How many of those Twitter posts don't hit?
[1837.96 --> 1844.60]  And then if it gets to the article stage, how many of those end up not moving forward to the next level?
[1844.60 --> 1848.10]  I think like you you'll get a sense of something that's really working.
[1848.32 --> 1848.76]  Right.
[1848.84 --> 1856.02]  So I would say I have a bunch of things that I write an article or I like build a little demo or something.
[1856.34 --> 1866.94]  You know, learn with Jason has been a great source of instant feedback because when we do those shows, like the format of the show is I intentionally I show up completely unprepared.
[1867.08 --> 1868.62]  I want to ask all the beginner questions.
[1868.62 --> 1870.18]  We start with an empty folder.
[1870.30 --> 1875.64]  The idea is to build something together in 90 minutes that has zero assumptions, no boilerplate or anything.
[1875.78 --> 1878.62]  We just were like, all right, how does this work?
[1878.66 --> 1882.02]  And I'm going to ask you all the dumb questions because I've never used this before.
[1882.14 --> 1883.54]  Like, what is a beginner seeing?
[1883.64 --> 1884.88]  That's what I'm trying to do.
[1884.88 --> 1896.86]  And what I'll notice is that depending on what I'm covering, there will be really, really high levels of interest and engagement and long tail views where people are really like digging into this content.
[1896.98 --> 1901.18]  Or it'll be something that like I think is really interesting and it was really fun.
[1901.24 --> 1902.62]  And the people who showed up had a good time.
[1902.62 --> 1904.44]  But like there's just not that demand.
[1904.44 --> 1906.06]  Like it doesn't get the long tail views.
[1906.06 --> 1908.44]  It's not getting shared around by people.
[1908.44 --> 1916.00]  So in creating those pieces of content, I get to see pretty quickly like, oh, a lot of people are interested in Svelte.
[1916.28 --> 1918.08]  A lot of people are interested in Eleventy.
[1918.48 --> 1922.18]  You know, those are two posts that I did recently that really caught a lot of steam.
[1922.78 --> 1926.82]  So that shows me, all right, I should probably dig into this a little bit more.
[1926.82 --> 1931.18]  Maybe I should write an article about Eleventy or about Svelte.
[1931.98 --> 1933.26]  And then we'll see how that goes.
[1933.40 --> 1934.56]  Like, does that get a lot of traction?
[1934.64 --> 1935.88]  Because then I'll take it a step further.
[1936.26 --> 1937.76]  Maybe I'll make an egghead course about it.
[1937.76 --> 1949.00]  But a lot of the things that I do, you know, you see it happen and you put it out into the world and you see that it was like not a bad response, but not a it's not like people aren't like, oh, this is amazing.
[1949.04 --> 1949.96]  We got to share this everywhere.
[1949.96 --> 1952.32]  And you're like, OK, so that would probably be harder to market.
[1952.32 --> 1960.26]  Like if I made that, I'd have to be creating a market for that as opposed to these other ones where there's obviously already interest and people looking for it.
[1961.44 --> 1961.56]  Yeah.
[1961.56 --> 1970.90]  And I think for me, if I post and I'm immediately getting a lot of people, sometimes I'll do like a Twitter poll where I'm like, would you be interested in this?
[1970.96 --> 1977.40]  And if it's even remotely like split down the middle, I also like I won't do it or I'll get a lot of comments.
[1977.40 --> 1979.36]  Sometimes it's like this has been done a thousand times.
[1979.44 --> 1980.96]  It's oversaturated at that point.
[1981.04 --> 1981.28]  Yeah.
[1981.28 --> 1989.74]  Like look where there's a need, like you want to find the sweet spot where you're interested in and where there's not enough content.
[1989.90 --> 2001.24]  For me, that was React Spring and animation libraries because Scott Tolinsky's course on React Spring was the best I've seen on the library, but it was the only one that I'd truly seen on the library.
[2001.24 --> 2011.36]  And I'm like, this seems like an area I could add something new to, like talk about the psychology of micro interactions on our users, blend that in with the library and how we can mesh those together.
[2011.50 --> 2016.30]  But so I would say find what you're interested in and see if there's already a market for it.
[2016.30 --> 2019.30]  If there is, maybe pick something with a little bit less saturation.
[2019.86 --> 2021.34]  And generally that's where I go.
[2021.34 --> 2032.46]  I have mixed feelings about the saturation thing because I personally think that people are, they're consuming content for like what they're trying to learn.
[2032.58 --> 2037.36]  But oftentimes, like how many courses are there on React?
[2037.72 --> 2038.08]  Right.
[2038.32 --> 2042.50]  And there's still an enormous market for making content about React.
[2043.16 --> 2046.20]  You know, I think Kent just released a new one today.
[2046.68 --> 2048.58]  That's like how to write React.
[2048.58 --> 2052.88]  And so I don't think saturation should necessarily discourage you from writing.
[2053.34 --> 2060.04]  I think what I use as a guide and what I always encourage people to do, I've been like repeating this phrase of just like play until it pays.
[2060.04 --> 2065.96]  Because what I've found is that if you're doing things that you're engaged in and I mean, I'm I don't take myself very seriously.
[2065.96 --> 2071.80]  So a lot of the stuff that I do is more intended to make me laugh than it is to be like productive work.
[2072.04 --> 2077.90]  But I chase that if I'm playing with something and I'm doing something silly, I will find that I'm having more fun doing it.
[2077.90 --> 2081.80]  And I'm getting these reps in and I'll start to see like where my interest is going.
[2081.80 --> 2084.32]  I am clearly gravitating toward this thing.
[2084.44 --> 2087.66]  So I'm not going to have to grind to create content.
[2088.14 --> 2097.64]  And so even if it's an area that's kind of saturated, I don't worry too much about putting something out in that space because it's like maybe my course is the one that finally makes it click for somebody.
[2097.64 --> 2105.90]  Even if there's a whole bunch of content there, like you always get that email that somebody is like, I've watched so many of these and yours was the first one that really made it land.
[2105.90 --> 2109.28]  And I'm sure that a lot of people watch mine and mine's the one that doesn't make it land.
[2109.40 --> 2111.90]  And they're looking for who's going to do the next one that does.
[2112.30 --> 2112.50]  Right.
[2112.50 --> 2121.00]  So I guess I would just say it's so easy to say that that an area is saturated because we see it on Twitter or there's like five courses about it on front end masters or whatever.
[2121.00 --> 2125.08]  But like if you're interested and you would have fun doing it, I so highly encourage you to do it.
[2125.14 --> 2129.60]  A lot of times like Chris Biscardi and I were working on identical courses at the same time.
[2129.60 --> 2132.56]  We're going to release them and they're going to be like more or less the same course.
[2132.66 --> 2139.24]  But he is a very like deep divey, thinks about things in a very like systems, computer science way.
[2139.50 --> 2142.78]  And I'm a doofus who likes to play and make boop jokes.
[2143.18 --> 2146.90]  And he like, you know, it's going to be different courses for different people.
[2146.90 --> 2152.42]  And watching both of them is still going to be useful, even if it's technically the same content.
[2153.26 --> 2153.42]  Awesome.
[2154.06 --> 2155.22]  Yeah, no, that's good advice.
[2155.48 --> 2159.00]  I think my only stipulation is like, don't build something.
[2159.00 --> 2160.30]  This goes for anything in life, really.
[2160.42 --> 2165.38]  But I wouldn't recommend blogging or creating a course on something that you passionately dislike.
[2166.64 --> 2167.94]  To Jason's point.
[2169.04 --> 2171.40]  Well, I see people all the time that's like, oh, React's hot.
[2171.48 --> 2172.66]  I'm going to make a course on React.
[2172.76 --> 2173.88]  But you don't like React.
[2173.96 --> 2174.62]  So don't make it.
[2174.66 --> 2178.02]  Because if you don't like something, people are going to be able to tell.
[2178.24 --> 2180.48]  And they're not going to want to take your course or your blog.
[2181.16 --> 2187.14]  So when we come back, we're going to talk about some tips for building a great and memorable course.
[2187.14 --> 2190.84]  And maybe share some of our most memorable courses that we've taken.
[2190.84 --> 2204.18]  If you like this show, I bet you'd enjoy listening to Brain Science.
[2204.56 --> 2214.76]  Join clinical psychologists Muriel Reese and Adam Sokoviak as they explore the inner workings of the human brain to understand behavior change, habit formation, mental health, and being human.
[2214.76 --> 2216.78]  Here's a quick taste of what you can expect.
[2216.90 --> 2220.10]  It's from episode four about coping skills and strategies.
[2220.30 --> 2220.84]  Take a listen.
[2221.68 --> 2226.50]  I often use this acronym with people when they're trying to cope.
[2226.72 --> 2227.64]  And it's HALT.
[2227.92 --> 2229.10]  H-A-L-T.
[2229.24 --> 2229.58]  HALT.
[2230.16 --> 2239.30]  Because if we are hungry, angry, lonely, or tired, your coping will invariably look different.
[2239.44 --> 2241.66]  I don't care if you're 3, 33, 73.
[2242.38 --> 2242.74]  Right.
[2242.74 --> 2252.14]  If you are hungry or hangry, angry, lonely, or tired, you just have less to be able to navigate it.
[2252.90 --> 2254.88]  Brain Science is a great podcast.
[2255.34 --> 2258.10]  Check it out at changelog.com slash brain science.
[2258.26 --> 2263.18]  Or just search Brain Science in Apple Podcasts, Spotify, or your favorite podcast directory.
[2263.30 --> 2263.84]  You'll find it.
[2264.10 --> 2267.64]  While you're at it, upgrade to our master feed at changelog.com slash master.
[2267.80 --> 2270.30]  And let your podcast app download all the shows we produce.
[2270.30 --> 2273.72]  Then you can pick and choose the ones you're interested in the most and skip the rest.
[2273.96 --> 2274.70]  What have you got to lose?
[2275.10 --> 2275.42]  All right.
[2275.50 --> 2276.08]  Back to the show.
[2281.38 --> 2284.78]  So we've talked a little bit about courses.
[2285.66 --> 2288.76]  I was just saying on the break that I don't know how to English anymore.
[2289.00 --> 2290.40]  And I totally am losing it.
[2290.98 --> 2293.28]  We're going to talk more about courses.
[2293.28 --> 2298.90]  Let's talk about what makes a good course and kind of what differentiates it from the back.
[2299.16 --> 2301.38]  Are we going to finish this up as Sean Connery?
[2302.02 --> 2302.30]  Differentiate.
[2303.18 --> 2305.10]  That was just how I speak, apparently.
[2306.16 --> 2309.80]  Past 7 p.m., my motor functions decline.
[2311.80 --> 2313.86]  Well, let's talk about this.
[2314.14 --> 2314.86]  Oh, my gosh.
[2315.00 --> 2318.70]  You know, when I was in high school, the only accent I could accurately pull off was a redneck.
[2318.70 --> 2324.56]  Like, I remember I was one of those news anchors on our news channels, and it was Irish Day.
[2324.70 --> 2325.34]  Oh, my gosh.
[2325.42 --> 2327.08]  St. Patrick's Day, not Irish Day.
[2327.66 --> 2330.38]  And all I could get out was a redneck accent.
[2330.94 --> 2333.34]  So, anyway, that was a tangent.
[2333.62 --> 2335.06]  Let's talk about courses.
[2337.14 --> 2339.32]  Y'all don't want to hear my redneck.
[2339.88 --> 2340.52]  Oh, goodness.
[2340.84 --> 2346.94]  Okay, well, since you started in with that accent, what's one tip that you would give someone looking to make a great course?
[2346.94 --> 2348.64]  Well, Emma.
[2350.32 --> 2352.82]  I don't know that I could hold this the whole way.
[2354.24 --> 2358.68]  The number one thing to make a good course, let's say.
[2360.88 --> 2373.10]  I think, actually, the first thing to start with for making a great course is to spend a little bit thinking about where people are and where you're trying to take them.
[2373.10 --> 2376.60]  So, it's really easy to say, I want to teach about this subject.
[2376.72 --> 2382.76]  And you start sort of like, you know, just throwing out content about that subject or the stuff that's the most interesting to you.
[2383.40 --> 2389.08]  But, you know, very commonly, people don't have the context that you have.
[2389.08 --> 2392.88]  And so, you need to think about, like, what is the necessary context for this course?
[2394.32 --> 2396.56]  Do you expect people to have it before they get in?
[2397.10 --> 2401.06]  What context do they need to get some of the later pieces that you need to teach them in the beginning?
[2401.18 --> 2406.08]  And be very upfront about that planning step of, you know, here's what you should know already.
[2406.08 --> 2409.42]  And ideally, you know, give people that information.
[2409.58 --> 2410.86]  You should know X, Y, and Z.
[2410.98 --> 2413.78]  And here are some resources that I recommend for you to learn those things.
[2414.32 --> 2421.36]  And then, what sequence of things do you need to build on to get to the place you're trying to go?
[2421.48 --> 2424.98]  Because, yeah, I think it's a lot of really bad courses that I've seen.
[2425.04 --> 2427.00]  And this is true for articles and stuff like that, too.
[2427.00 --> 2431.86]  They jump right in from a point that is the mental state of the author.
[2432.78 --> 2441.04]  And they fail to do that thinking of what are the layers of context that you need to build up to get somebody to the place you're trying to take them.
[2441.68 --> 2446.84]  That's super funny because I just gave an internal talk at LogMean today about blogging.
[2446.90 --> 2449.50]  And one of my tips is don't make assumptions about your readers.
[2450.06 --> 2452.42]  So, that means, like, spell out acronyms.
[2452.42 --> 2462.26]  Like, if you're going to reference tangential technologies, like, if you're doing a course on React and you mention Redux, at a high level, define what Redux is and maybe link to the docs.
[2462.46 --> 2465.42]  But I would say, like, playing off that, my biggest tip is why.
[2466.38 --> 2467.86]  Why should your users care?
[2468.04 --> 2469.38]  Why are you teaching them this?
[2469.64 --> 2473.98]  And I have a book recommendation because it wouldn't be a podcast episode if I didn't recommend a book.
[2474.46 --> 2477.20]  Start with Why by Simon Sinek.
[2477.34 --> 2478.48]  It's one of my all-time favorites.
[2478.70 --> 2481.86]  And it explains, like, what is, literally, why do I care?
[2481.86 --> 2482.90]  Why should I care?
[2483.38 --> 2491.54]  And, like, I wrote a post on specificity, CSS specificity, and it's like, yeah, I can tell you the mathematical equation for how styles are applied in the DOM.
[2491.86 --> 2492.44]  But why?
[2492.68 --> 2493.72]  Like, why do you care?
[2493.82 --> 2496.70]  And you should care because it leads to maintainable code.
[2496.82 --> 2498.46]  It's actually more accessible this way.
[2498.80 --> 2502.48]  When you delete legacy code, you can delete the CSS and not have to worry about it.
[2502.64 --> 2505.24]  So, that's what I would suggest is explain the why.
[2505.58 --> 2509.88]  And if you're a video person, his TED Talk also on the same subject is amazing.
[2509.88 --> 2520.72]  I have not read that book, but there's an old, I think it was Toyota in Japan, had a technique that they used to diagnose root cause, which was the five whys.
[2520.72 --> 2531.22]  And in studying that, which is not quite related to what we're talking about now, but as I was thinking more about that, I ended up coming up with this mantra that I repeat to myself, which is always find the why.
[2531.74 --> 2533.98]  Because of all the reasons you just listed, right?
[2533.98 --> 2540.76]  And so, I've written articles about that and I talk about it all the time because understanding, like, why does any of it matter?
[2541.28 --> 2545.90]  Like, if I'm going to teach you something, it needs to make a measurable improvement on your life.
[2546.24 --> 2551.62]  And if I can't articulate what that is, like, why is the thing that I'm about to teach you better than what you're doing now?
[2551.66 --> 2554.80]  And if I can't articulate that, I don't have a course.
[2554.80 --> 2556.74]  I just have, like, a thought.
[2557.36 --> 2563.80]  And that helps inform a lot of my decision making on whether or not I want to pursue something.
[2563.80 --> 2573.28]  Because if I don't have a benefit, if I can't articulate a clear, like, a clear measurable improvement to your life, I don't think it's worth me taking up your time to teach it to you.
[2573.58 --> 2574.44]  I like that.
[2574.76 --> 2575.44]  No, it's true.
[2575.44 --> 2583.94]  And, like, especially if people are paying money, like, I hate when I pay money for a course and I feel like I walk away and I've forgotten everything.
[2585.00 --> 2591.62]  But corollary to that is think about who your course is for and possibly even more importantly, who is it not for?
[2592.18 --> 2593.62]  And make that explicit, right?
[2593.64 --> 2599.10]  Like, you will get value from this if you are in this situation trying to do this type of thing.
[2599.32 --> 2602.60]  And if you are not in that, you will not get value out of this.
[2602.60 --> 2609.28]  I apologize because I'm about to say the S word, but, like, learning how to sell things is such a critical part.
[2609.40 --> 2610.94]  I was just going to say that.
[2611.02 --> 2612.98]  I feel like we're of one mindset.
[2613.54 --> 2614.14]  Which is odd.
[2614.14 --> 2615.06]  We're so far away.
[2615.06 --> 2615.64]  I think so.
[2616.08 --> 2618.32]  You know, I'm going to go with great minds.
[2620.20 --> 2626.08]  But, yeah, I think, like, one of the things that I've noticed is that when I used to work in an agency, I worked a lot on sales copy.
[2626.08 --> 2632.48]  And we were always trying to figure out, like, how do we make sure not just that people will buy a thing?
[2632.52 --> 2634.28]  Because it's easy to get somebody to buy a thing.
[2634.28 --> 2637.20]  But how do we get people to buy a thing and not regret it?
[2637.60 --> 2637.94]  Right?
[2638.30 --> 2644.28]  How do we make sure that when somebody buys this thing, they're walking away feeling like they made a great decision and their life is improved?
[2644.28 --> 2650.36]  And pre-qualification and pre-disqualification were two of the biggest things that we found.
[2650.56 --> 2652.06]  I don't want to waste your time.
[2652.34 --> 2654.72]  And I don't want you to feel like your time has been wasted.
[2654.86 --> 2662.70]  So I'm going to tell you, like, you should not read this or you should not take this course if these conditions are true.
[2662.76 --> 2664.46]  Because it's not going to be useful for you.
[2664.82 --> 2670.78]  And if you lay those things out, it also helps you as a course creator articulate better, like, what are you trying to do?
[2670.82 --> 2672.70]  You know, like you said, what is this for?
[2672.80 --> 2673.92]  You know, who is this for?
[2673.92 --> 2675.26]  Why am I making this course?
[2675.34 --> 2677.04]  And it helps with the conversation.
[2677.04 --> 2690.68]  You can target your messaging a little more clearly to people in the situation you're actually writing for instead of doing this thing that I catch myself doing sometimes where I'm trying to back out to a generic to the point that it almost becomes meaningless.
[2690.92 --> 2693.32]  Like I'm giving you, it's like the foobar example.
[2693.56 --> 2697.76]  Like it sort of demonstrates the concept, but it's so academic that it's hard to land.
[2697.76 --> 2704.76]  And it usually just a beginner or somebody who's not familiar with the philosophy around that language, they'll be completely lost.
[2704.76 --> 2706.70]  Yeah, that's a good point.
[2706.70 --> 2714.84]  Because I do feel like a lot of, like, I remember being pointed to Coursera courses and the Harvard education courses when I was trying to learn development.
[2715.22 --> 2719.68]  Because, like, I have a computer science degree, which I learned Java in, okay?
[2719.94 --> 2721.20]  In MIPS, assembly language.
[2721.20 --> 2723.78]  And then I got to IBM and they were like, JavaScript in the web.
[2723.82 --> 2725.18]  And I'm like, it's easy.
[2725.42 --> 2729.16]  And then I went on W3 Schools and I was like, this is easy.
[2729.16 --> 2734.14]  And then I got into the dojo code base and I was like, what the actual?
[2736.06 --> 2749.32]  So I think being able to translate academic, typically academic content in the past that was taught, like algorithms and data structures into something that is consumable by the everyday human.
[2750.28 --> 2756.74]  Actually, I remember this is one of my most memorable courses was Kyle Shevlin's Data Structures and Algorithms course with JavaScript on Egghead.
[2756.74 --> 2762.60]  And it was the first time I had seen someone create a data structures and algorithms course using JavaScript.
[2762.82 --> 2764.78]  They're typically taught with back-end languages.
[2765.00 --> 2777.64]  And when you are new and you're trying to study for a technical interview and you're reading Cracking the Coding interview and it's all in C, C++ and Java, how do you, like, you can't conceptually translate that into different languages yourself.
[2777.76 --> 2778.62]  Like, that's really hard.
[2778.62 --> 2789.34]  And so he was the first person I saw that was, like, taking something so traditionally abstract and so academic and breaking it down for the average person.
[2789.68 --> 2791.62]  And that is something really covetable.
[2792.72 --> 2792.88]  Yeah.
[2793.04 --> 2795.04]  I love the way Kyle's brain works on that stuff.
[2795.24 --> 2798.28]  He's done another one on functional programming that I really like.
[2798.28 --> 2798.94]  Mm-hmm.
[2799.30 --> 2799.98]  It's funny.
[2800.54 --> 2808.12]  The way he and I met is he sent me a message and he was like, I think you and I made exactly the same course without ever meeting each other.
[2808.34 --> 2824.16]  Because we'd both made this, like, functional programming for people who don't care about functional programming style course that was more like, here are all the things you're already doing that are functional programming and why they're valuable and why you should consider doing more of them.
[2824.16 --> 2828.54]  And mine was way more, you know, irreverent and silly.
[2828.70 --> 2837.72]  And his was, like, very thoughtful and, like, here are real world examples of what you're doing using JavaScript and ways that you can make your life easier with functional programming.
[2837.72 --> 2841.12]  And I've always liked that because he's a very, like, philosophical thinker.
[2841.12 --> 2849.62]  But he brings that down to a very, like, practical level, which I think is extremely challenging.
[2849.76 --> 2850.88]  And I've seen him pull his hair.
[2850.94 --> 2854.38]  Well, if he had any hair, he'd pull it out over how he writes these.
[2858.04 --> 2859.86]  Kyle, we're so sorry if you're listening.
[2862.36 --> 2863.16]  I'm joking.
[2863.90 --> 2866.06]  Kyle and I were both, like, bald bearded guys.
[2866.32 --> 2870.28]  Well, was he the one that you did the Guess Whose Beard This Is challenge?
[2870.28 --> 2875.32]  Yeah, I had to build a machine learning tool because people kept thinking that we were each other.
[2875.92 --> 2877.52]  So I built a machine learning.
[2877.62 --> 2881.42]  It's at whosebeardisthis.com or whichbeardisthis.com.
[2881.96 --> 2883.10]  Oh, no, I need to look this.
[2883.14 --> 2884.42]  I think it's whichbeardisthis.com.
[2884.58 --> 2889.76]  And you drag a picture of one of us on there and it'll tell you which of us it is because it was a legit problem.
[2889.88 --> 2895.36]  Like, people would think we were the other person because we're both, like, bald bearded white guys from Portland, Oregon.
[2895.46 --> 2897.62]  It's, like, very easy to cross us up.
[2897.62 --> 2901.88]  This is the most absurd thing that I've ever seen, but also I love it.
[2903.16 --> 2904.78]  That is pretty funny.
[2905.72 --> 2906.16]  Amazing.
[2906.78 --> 2911.18]  One other tip that I have is about medium rotation, which sounds really cool.
[2911.62 --> 2914.60]  And then I explain it and you're like, oh, it sounds cooler than it is.
[2914.70 --> 2918.14]  It's basically the fact that people learn through different mediums.
[2918.14 --> 2926.72]  And I think, A, if you're going to take a course and invest money and time into it, like, I think it's worth it to understand the best way that you learn before you go into it.
[2926.78 --> 2930.14]  So, like, I love reading, but I can't just read.
[2930.28 --> 2932.78]  I have to also practice by coding and I have to watch videos.
[2932.84 --> 2934.66]  So, like, I like all three mediums of learning.
[2934.66 --> 2943.54]  And when you're creating a course, I think having multiple mediums that you rotate through to reinforce the skills is really important.
[2943.94 --> 2947.24]  And Tyler McGinnis does as well where he'll have a 20-minute video on a topic.
[2947.42 --> 2950.50]  And then he'll have an associated blog post with it and then an activity.
[2951.08 --> 2959.14]  And this is great, especially for people who maybe can't watch the video right now because they're, like, commuting on a train or something and they just want to read it.
[2959.48 --> 2961.52]  But having that reinforcement is so important.
[2962.26 --> 2962.46]  Yeah.
[2962.88 --> 2963.50]  I love that.
[2963.50 --> 2970.74]  I mean, I think that's something that I want to get better at is creating written companions to the video content that I produce.
[2970.80 --> 2974.76]  Because I create a lot of video content, but I don't create a ton of written content.
[2974.92 --> 2980.94]  And that's been something that kind of bums me out because I know that not everybody has time to watch a 90-minute video.
[2981.14 --> 2984.54]  And having a tutorial that condenses that down is very valuable.
[2984.72 --> 2989.96]  Like, also just for me, like, condensing what I learned into a written post helps me cement what I'm learning.
[2989.96 --> 2993.70]  Because, you know, I'm learning something new a couple times a week and a lot of times it doesn't stick.
[2994.04 --> 3003.04]  Like, if you ask me, like, how to do what Angie Jones taught me when she came on a few weeks ago, I would have to go watch the video to remember how to do it.
[3003.10 --> 3004.38]  And that's kind of a bummer, right?
[3004.42 --> 3006.92]  I'd love to have more of that information stick in my brain.
[3006.92 --> 3010.68]  And so, I think they say one of the best ways to learn things is to teach them.
[3010.88 --> 3015.62]  And I'm finding that to be more and more true, especially as I go broader with the subject matter.
[3016.24 --> 3018.54]  Because, you know, otherwise it just goes in one ear and out the other.
[3019.38 --> 3033.56]  One thing that I think is worth highlighting that's come out in what both of you are saying is that there are a set of skills beyond the expertise in the topic area that are important for building a good course.
[3033.56 --> 3038.58]  And this is not to say that you should feel like you have to get all those skills before you start building a course.
[3038.64 --> 3039.02]  Not at all.
[3039.10 --> 3045.90]  But don't be surprised if the fact that you are an expert in a topic area doesn't immediately translate into a great course.
[3046.34 --> 3049.44]  You need to learn about how to structure content.
[3049.56 --> 3051.92]  You need to learn about how to record video.
[3052.08 --> 3054.30]  You need to learn about how to write all these different things.
[3054.66 --> 3055.52]  You know, there's sales skills.
[3055.62 --> 3056.56]  There's marketing skills.
[3056.56 --> 3063.46]  A lot of the stuff you were talking about in terms of gathering information about where people are and how they're doing, that's marketing.
[3064.38 --> 3066.32]  These are all distinct skill areas.
[3066.94 --> 3072.12]  And as you get started working on courses, you'll discover that, hey, a lot of these have a lot to learn themselves.
[3072.12 --> 3074.44]  And you maybe want to go and take a course on marketing.
[3074.54 --> 3078.02]  You maybe want to go take a course on how do I write a course.
[3078.08 --> 3078.76]  They exist.
[3079.34 --> 3083.44]  So, you know, I think, once again, not saying this to try to discourage people.
[3083.44 --> 3095.62]  I think if you have an area you're excited to teach, go and start learning about how to teach and start trying to teach and giving workshops and all these different things because you learn best probably by doing and by trying.
[3095.62 --> 3099.20]  But don't be shocked if it's hard.
[3099.20 --> 3102.92]  Because these are new skills for most of us.
[3103.66 --> 3108.14]  And it will take you some time to feel like you've got it and you're getting it to work.
[3108.98 --> 3109.14]  Yeah.
[3109.62 --> 3110.06]  Absolutely.
[3110.84 --> 3114.50]  I think that was a very, like, sentimental moment right there.
[3115.08 --> 3121.38]  So, with that, and I want to reiterate, like, what Cable just said because I do think it's really important.
[3121.66 --> 3124.92]  Like, you know, if you want to do something, just do it.
[3125.14 --> 3125.44]  Right?
[3125.44 --> 3127.98]  Like, what is the worst thing that could possibly happen?
[3128.06 --> 3131.40]  This is kind of the mantra that I adopted in my life the last couple of years.
[3131.48 --> 3132.74]  But, like, what's the worst that can happen?
[3132.84 --> 3133.66]  What do you have to lose?
[3134.08 --> 3135.18]  What do you have to gain?
[3135.42 --> 3138.16]  Honestly, like, if it works out, like, you have everything to gain.
[3138.62 --> 3144.10]  So, I want to ask both of you, what is one of your most memorable courses that you have ever taken?
[3144.84 --> 3145.60]  I'll go first.
[3145.96 --> 3151.44]  Jason's Gatsby course on front and masters was one of my all-time favorites because a Gatsby fangirl.
[3151.44 --> 3158.40]  And I think it's honestly for the fact that Jason was teaching it because it was so easy for me to learn from him.
[3158.56 --> 3160.54]  So, that was one of my most memorable.
[3160.88 --> 3162.26]  Well, that makes me feel great.
[3162.70 --> 3165.60]  This isn't a video podcast yet because I'd be blushing.
[3165.94 --> 3167.54]  He paid me to say that.
[3168.58 --> 3169.42]  Checks in the mail.
[3170.44 --> 3172.60]  You do look visibly more red, I think.
[3172.60 --> 3183.36]  This is hard because I've been in a lot of really good courses and I've seen a lot of stuff.
[3183.50 --> 3193.50]  I would say probably the course that was the most impactful for me because it was right place, right time, was You Don't Know JavaScript by Kyle Simpson.
[3193.50 --> 3199.68]  I had been doing web development for a long time, but I had always been doing kind of framework-driven design.
[3200.42 --> 3205.86]  And I was just about to take a contract where I was going to be building new stuff.
[3206.38 --> 3213.76]  So, it was like, okay, I'm not going to be doing what I'm used to, which is taking a theme and making that theme do cool things.
[3213.86 --> 3218.74]  It was like, I need to be thinking about architecture and I need to be thinking about how this actually works.
[3218.74 --> 3243.54]  So, when I read that book, it was at the right time and the right experience level where the things he was teaching helped drop a lot of knowledge that I had into a slot that was actually useful and applicable while introducing new concepts that helped me think better about architecture and about writing more extendable and maintainable code.
[3243.54 --> 3244.96]  It's such an experiential thing, right?
[3244.96 --> 3247.36]  Because I've seen all these other amazing courses.
[3247.56 --> 3256.58]  I've learned animation or I had Anjana Vakil did a course on lambda calculus that is so fantastically well put together.
[3257.46 --> 3261.50]  And she's such an amazing teacher, but I don't use lambda calculus every day.
[3261.68 --> 3265.78]  So, in terms of the impact that it had on me, professionally, the impact was low.
[3265.86 --> 3273.96]  As an educator, the impact was super high because I was like, man, I want to be as good as Anjana at teaching because she's so fantastic.
[3273.96 --> 3278.48]  But yeah, I would say in terms of professional impact that you don't know, JavaScript was probably the most impactful.
[3279.12 --> 3287.82]  I think the course that has been most impactful for me was not a technical course, but it was a course on online business and marketing called Product Launch Formula.
[3287.82 --> 3294.56]  That, I mean, the content of the course, I've come to realize it's not super unique in a lot of ways.
[3294.64 --> 3296.46]  Some of it is, but a lot of it is widespread.
[3296.68 --> 3311.58]  But why it was super impactful for me is it completely opened my eyes to this whole area around how online business and marketing can and does work and how people do it successfully and what a bunch of the different core concepts were.
[3311.58 --> 3318.38]  And so, it was not around the actual details of the execution pieces that I picked up in that course.
[3318.48 --> 3319.40]  Some of them were valuable.
[3319.52 --> 3320.22]  Some of them weren't.
[3320.54 --> 3328.28]  But it was more around, here is this entree into this whole different world from where I had been, which was purely technical.
[3328.28 --> 3340.56]  And now I have a different perspective anytime I'm looking at and working at a business, whether I'm working on the business side of it, which I was at the time that I took this course.
[3340.56 --> 3342.24]  I had my own business doing different things.
[3342.24 --> 3349.88]  Or when I'm working in the engineering department, but thinking about how are we marketing and selling our product and how does that tie into the work we're doing in engineering?
[3350.06 --> 3353.72]  And are there different ways that we can design things that are going to make a big difference there?
[3353.72 --> 3360.20]  And I think the sort of meta lesson on that is take courses that are outside of your area of expertise.
[3360.56 --> 3372.62]  Because even if the actual detailed content of that course doesn't end up being something you use very often, the broadening of perspective is sometimes transformational.
[3373.04 --> 3373.56]  Absolutely.
[3374.02 --> 3375.04]  I love that.
[3375.16 --> 3376.38]  That is solid advice.
[3377.06 --> 3378.84]  This episode is full of solid advice.
[3378.98 --> 3382.86]  Just honestly, I learned a lot this episode.
[3382.86 --> 3390.14]  I feel like it's nice to speak to other content creators about this because I don't think I've ever talked about making a course with anyone.
[3390.50 --> 3393.36]  But it's an intimidating thing.
[3393.96 --> 3397.02]  But I think what I've taken away from this is anyone can do it.
[3398.56 --> 3399.78]  It's going to be hard.
[3400.08 --> 3401.12]  You have to put in the time.
[3401.34 --> 3406.16]  And if you're willing to put in the time, be detail-oriented, you can do really well.
[3407.02 --> 3407.42]  Absolutely.
[3408.60 --> 3409.00]  100%.
[3409.00 --> 3410.14]  Know that it will be hard.
[3410.14 --> 3416.30]  Come into it knowing that it will be hard and just power through like you did with whatever else you've done that's hard in your life.
[3417.22 --> 3428.04]  And one thing that I would like to call out is if you can find people who are doing the same things, it is so helpful to have like accountability buddies.
[3429.16 --> 3430.36]  Oh, I love that word.
[3430.36 --> 3434.26]  I am part of a Discord group.
[3434.52 --> 3435.44]  Chris Biscardi and I.
[3435.70 --> 3438.58]  It's like Chris Biscardi started this thing called the Party Corgi Discord.
[3439.32 --> 3444.12]  And then it's evolved over time into this community of people who are creating content.
[3444.36 --> 3448.34]  And so I'll put a link here to join that.
[3448.34 --> 3454.72]  But it's like if you go here, it's a bunch of people who are trying to create things.
[3454.80 --> 3455.74]  They're sharing ideas.
[3455.86 --> 3456.98]  They're iterating.
[3457.16 --> 3462.74]  They're like putting stuff out from live streams to articles to courses and everything in between.
[3463.22 --> 3469.18]  And seeing people create is always such a good impetus to continue creating.
[3469.18 --> 3476.48]  So I get super inspired because I'm watching all of these really brilliant people just put stuff out there.
[3476.52 --> 3477.98]  And I'm like, oh, I want to put stuff out there.
[3478.00 --> 3479.10]  And then they'll do something.
[3479.22 --> 3480.76]  And I'm like, I have thoughts on that.
[3480.76 --> 3482.84]  So I can like remix their thought.
[3482.92 --> 3486.50]  You know, I'll reference their post and then I'll call out something they said that make me think.
[3486.52 --> 3487.84]  And then I'll write a post about that.
[3488.06 --> 3498.78]  And it's this amazing way to create good, like lots of content and have a network of people who are it's you get that like positive feedback loop where it's lots of people.
[3499.18 --> 3507.56]  Working together and encouraging each other as opposed to you in a vacuum trying to work up the will to create this course and hoping people will like it.
[3508.08 --> 3512.34]  Yeah, we're going to link that in the show notes because I just went and joined and it is popping in there.
[3513.48 --> 3514.68]  I need to go to sleep.
[3514.78 --> 3516.98]  I have never said that before in my life.
[3517.90 --> 3519.42]  I need to stop.
[3519.70 --> 3522.86]  So with that, I just want to say a huge thank you to you, Jason.
[3522.96 --> 3524.60]  I know your time is extremely valuable.
[3524.60 --> 3534.76]  And if y'all listening are not subscribed to Jason's Learn With Jason and or on Twitter, like you should, because there's a boatload of meat that he posts.
[3535.02 --> 3538.50]  Not in his Learn With Jason, although I would like to see a meat smoking tutorial.
[3539.06 --> 3540.00]  So I'm working on it.
[3540.24 --> 3544.04]  Joel and I are working on ways to create video content about cooking.
[3544.80 --> 3548.88]  OK, and then I expect some in the mail, preferably expedited.
[3549.04 --> 3550.12]  You got to come visit Portland.
[3550.12 --> 3552.42]  I do want to go to Portland.
[3552.56 --> 3554.32]  So next time I'm there, I'll hit you up.
[3554.66 --> 3556.96]  But thank you so much for joining us.
[3557.18 --> 3560.20]  And if you are listening and you want to make a course, go for it.
[3560.22 --> 3562.94]  You have nothing to lose and everything to gain.
[3566.22 --> 3568.68]  Thank you for listening to this episode of JS Party.
[3568.92 --> 3570.94]  We appreciate your time and your attention.
[3571.44 --> 3577.12]  If this show has helped you, entertained you or brought you joy in any way, we would love a five star review on Apple Podcasts.
[3577.12 --> 3586.32]  In fact, I will donate 100 Internet points to the first person who gives us five stars and mentions Emma and Cable's terrible, awful redneck accents in the review.
[3586.70 --> 3589.42]  Special thanks to Jason Langstor for joining us once again.
[3589.54 --> 3591.12]  Check him out at learnwithjason.dev.
[3592.02 --> 3594.84]  This episode was hosted by Emma Bosh and with help by Cable.
[3595.12 --> 3596.78]  It was produced by me, Jared Santo.
[3597.16 --> 3599.84]  And our beats are by the one and only Breakmaster Cylinder.
[3600.28 --> 3601.58]  We have awesome sponsors.
[3601.72 --> 3602.18]  Support them.
[3602.26 --> 3602.90]  They support us.
[3603.32 --> 3606.78]  Thanks again to Fastly, Linode, and Rollbar for helping us do what we do.
[3606.78 --> 3608.16]  So that's all for now.
[3608.36 --> 3609.58]  We'll talk to you next time.
[3616.98 --> 3618.76]  Clap your hands, everybody.
[3619.12 --> 3620.88]  If you got what it takes.
[3621.12 --> 3625.32]  Because I'm Curtis Blow and I want you to know that these are the boys.
[3625.94 --> 3626.32]  Nice.
[3626.76 --> 3630.78]  Do you need to go microwave more coffee or are you oversaturated?
[3631.58 --> 3634.62]  No, I will take the excuse to go microwave more coffee.
[3634.62 --> 3636.92]  Wah- işte-
[3637.42 --> 3637.74]  See you.
[3638.44 --> 3638.84]  Excellent.
[3638.84 --> 3639.24]  myth
[3639.24 --> 3641.68]  and ظ
[3641.68 --> 3642.72]  mind
[3642.72 --> 3643.36]  ropes
[3643.36 --> 3644.28]  That's crazy.
[3644.28 --> 3644.50]  There we go.
[3644.66 --> 3645.82]  There we go Office quer
[3645.82 --> 3647.46]  game
[3647.46 --> 3647.60]  game
[3647.60 --> 3648.12]  game
[3648.78 --> 3650.10]  game
[3650.10 --> 3650.92]  game
[3650.92 --> 3651.12]  game
[3651.12 --> 3651.18]  game
[3651.18 --> 3652.88]  game
[3652.88 --> 3654.74]  game
[3654.74 --> 3655.96]  game
[3655.96 --> 3656.82]  game
[3656.82 --> 3657.94]  game
[3657.94 --> 3658.52]  game
[3658.52 --> 3659.96]  game
[3659.96 --> 3660.74]  game
[3660.74 --> 3660.76]  game
[3660.76 --> 3660.82]  game
[3660.82 --> 3660.84]  game
[3660.84 --> 3660.92]  game
[3660.92 --> 3661.78]  game
[3661.78 --> 3662.74]  game
[3662.74 --> 3662.86]  game
[3662.86 --> 3664.06]  game
