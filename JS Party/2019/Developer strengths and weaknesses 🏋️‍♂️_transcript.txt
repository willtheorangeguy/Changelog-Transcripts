[0.00 --> 2.58]  Bandwidth for Changelog is provided by Fastly.
[2.96 --> 4.84]  Learn more at Fastly.com.
[5.08 --> 8.16]  We move fast and fix things here at Changelog because of Rollbar.
[8.30 --> 9.96]  Check them out at Rollbar.com.
[10.18 --> 12.40]  And we're hosted on Linode cloud servers.
[12.74 --> 14.74]  Head to Linode.com slash Changelog.
[15.48 --> 18.54]  This episode is brought to you by our friends at Rollbar.
[18.66 --> 21.62]  Move fast and fix things like we do here at Changelog.
[21.62 --> 24.38]  Check them out at Rollbar.com slash Changelog.
[24.60 --> 26.96]  Resolve your errors in minutes and deploy with confidence.
[26.96 --> 30.14]  Catch your errors in your software before your users do.
[30.52 --> 33.16]  And if you're not using Rollbar yet or you haven't tried it yet,
[33.30 --> 36.78]  they want to give you $100 to donate to open source via Open Collective.
[36.88 --> 40.22]  And all you got to do is go to Rollbar.com slash Changelog, sign up,
[40.60 --> 41.84]  integrate Rollbar into your app.
[41.92 --> 45.92]  And once you do that, they'll give you $100 to donate to open source.
[46.30 --> 49.14]  Once again, Rollbar.com slash Changelog.
[56.96 --> 63.12]  Welcome to JS Party, a weekly celebration of JavaScript and the web.
[63.28 --> 69.72]  Tune in live on Thursdays at 1 p.m. Eastern, 10 a.m. Pacific at Changelog.com slash live.
[69.72 --> 74.84]  Join the community and Slack with us in real time during the show at Changelog.com slash community.
[75.30 --> 76.04]  Follow us on Twitter.
[76.14 --> 77.66]  We're at JSPartyFM.
[77.78 --> 79.12]  And now on to the show.
[79.12 --> 85.52]  We are back, everyone, for another JS Party.
[85.74 --> 86.94]  And guess who is back?
[87.04 --> 87.76]  It's Suze.
[87.86 --> 89.14]  Suze, welcome back to the party.
[89.62 --> 90.86]  Thank you for having me back.
[90.98 --> 92.64]  I missed everyone so much.
[92.68 --> 94.70]  It was so weird to be away for so long.
[94.82 --> 98.80]  We have two new panelists that have joined the circuit and everything.
[99.10 --> 100.34]  So, yeah, I've been under a rock.
[100.44 --> 101.38]  Thanks for having me back.
[101.58 --> 102.04]  You bet.
[102.14 --> 104.64]  Speaking of new panelists, Divya is back as well.
[104.72 --> 105.20]  Welcome, Divya.
[105.76 --> 106.16]  Yay.
[106.32 --> 106.62]  Hello.
[107.22 --> 107.78]  Good to have you.
[107.78 --> 110.36]  And it wouldn't be a party without K-Ball over there dancing to the music.
[110.46 --> 110.94]  What's up, K-Ball?
[111.36 --> 114.34]  Yeah, I probably have the most ridiculous rock out every day.
[114.42 --> 116.62]  And now you see it now that we do video while you're talking.
[116.76 --> 118.22]  I'm just like rocking out over here.
[118.46 --> 119.02]  I'm a fan.
[119.38 --> 120.00]  I'm a huge fan.
[120.52 --> 120.88]  Absolutely.
[121.12 --> 122.72]  You have three huge fans over here.
[123.66 --> 125.12]  Today's show is going to be lots of fun.
[125.18 --> 126.76]  Let's hop right into it.
[126.84 --> 130.58]  We're going to focus on something that hopefully is helpful for everyone.
[130.58 --> 136.90]  And if not, at least maybe therapeutic for us as we go inside our ids and egos and discuss
[136.90 --> 140.76]  some introspection about strengths and weaknesses.
[141.14 --> 143.08]  So we all have them, both.
[143.46 --> 145.84]  And some things lend themselves well to software development.
[145.96 --> 147.22]  Some things harm us.
[147.56 --> 149.74]  Kind of tease it apart and talk about strengths and weaknesses.
[149.74 --> 155.00]  The idea for this actually came during an episode of Backstage I did with Nick Janatakis,
[155.24 --> 159.04]  who is a ChangeLog community member, where we were just talking about development.
[159.20 --> 163.80]  And I happened to just by happenstance state one of what I think is a strength I have.
[164.02 --> 166.30]  And then I followed it up with a weakness kind of off the cuff.
[166.38 --> 168.22]  And I thought, wow, let's expand this idea.
[168.38 --> 173.04]  And let's talk about ourselves with the panelists here, as well as people out there in the community
[173.04 --> 177.10]  that we admire or that we think are great developers and talk about their strengths
[177.10 --> 179.10]  and weaknesses, maybe give some props as well.
[179.10 --> 184.62]  So as we like to stay positive, let's start on the plus side, which is the strengths side
[184.62 --> 186.02]  of the conversation.
[186.02 --> 192.18]  And let's talk about what we think are characteristics or traits or skill sets, whatever it happens
[192.18 --> 194.84]  to be that makes people great at software development.
[195.30 --> 198.18]  And specifically, let's not get too selfish.
[198.28 --> 203.26]  Let's start with others before we talk about ourselves and talk about the most amazing or
[203.26 --> 207.00]  admirable developers out there and what you think makes them great.
[207.52 --> 208.56]  So that's the conversation.
[208.56 --> 212.90]  I'll open it up to call dibs or grab who wants to go first here and kick off the combo.
[213.86 --> 214.38]  Fair enough.
[214.48 --> 216.28]  I guess I'll just have to like a school teacher.
[216.36 --> 217.28]  I'll have to just call names.
[217.36 --> 218.90]  Either raise your hand or I'm going to call your name.
[219.72 --> 221.50]  So Suze, you didn't raise your hand.
[221.54 --> 222.22]  So I'm going to call your name.
[222.30 --> 224.58]  Why don't you kick us off and talk about developer strengths?
[225.12 --> 225.26]  Sure.
[225.26 --> 230.40]  One thing that I really admired in other developers and tried to emulate this is somebody who's
[230.40 --> 233.12]  really good at compromise and pragmatism.
[233.60 --> 236.06]  I think that they're really important things to have.
[236.18 --> 240.70]  I think that once you build up a certain amount of technical skill and you sort of have this
[240.70 --> 244.32]  broad, at least like broad understanding of lots of different topics and maybe you specialize
[244.32 --> 249.80]  in a few, you should be able to take that knowledge, ask the right questions of people who have
[249.80 --> 255.50]  better knowledge than you and then be able to arrive at a solution where knowing that
[255.50 --> 258.52]  there's really hardly ever a perfect solution to something.
[258.66 --> 260.02]  There's always trade-offs and things like that.
[260.02 --> 265.58]  But someone who can very swiftly make the right trade-offs, make the whole team comfortable
[265.58 --> 269.20]  with that decision if they're working on a team as well, but also have enough sort of
[269.20 --> 273.08]  technical chops to be able to explain the reasoning behind things so that everyone's on the same
[273.08 --> 273.42]  page.
[273.66 --> 278.82]  I think that that just has like a huge productivity multiplier and a psychological safety multiplier
[278.82 --> 279.80]  on everybody.
[280.16 --> 286.78]  And it's really using your skills as, I guess, like as an experienced developer in order to
[286.78 --> 291.34]  really just get rid of roadblocks and start making something that's very good quality.
[292.10 --> 295.58]  Is there anybody in particular that you think embodies that or that you think of as you're
[295.58 --> 300.50]  talking about this generic skill of compromise that you would point to and say, here's somebody
[300.50 --> 301.38]  that's really good at it?
[301.64 --> 303.80]  I do, but they're not well known in the industry.
[303.92 --> 304.60]  Does that make sense?
[304.92 --> 305.14]  Sure.
[305.50 --> 306.58]  You can still shout them out.
[306.58 --> 308.72]  If you don't think they'd be really embarrassed by it.
[308.96 --> 310.16]  Yeah, I don't want to put them on blast.
[310.46 --> 311.78]  I will say first name basis.
[312.00 --> 316.76]  So the first job that I had in the US, I worked with a really extraordinary team.
[317.20 --> 322.08]  And one person in particular, whose name was Nick, was just an exceptionally talented
[322.08 --> 322.58]  engineer.
[322.98 --> 327.94]  But he would be brought into so many different conversations outside of his team every day
[327.94 --> 334.50]  because he was so smart, but also just incredibly good at listening and incredibly good at being
[334.50 --> 337.80]  able to kind of provide any gotchas to think about.
[338.14 --> 343.16]  And also he was happy to explain certain concepts by like drawing diagrams and things like that.
[343.16 --> 348.70]  And you could tell that that was something that he was just really admired for at work
[348.70 --> 354.78]  because there was a system that we had where you could basically donate, like you could
[354.78 --> 356.46]  give someone a bonus every single month.
[356.64 --> 359.06]  So you could choose one person to give that to.
[359.54 --> 364.46]  And they got like a certificate and you wrote the reasoning down for why they should get this
[364.46 --> 364.82]  bonus.
[365.20 --> 369.24]  And then basically you would, the ceremony was you would print it out and bring it to their
[369.24 --> 370.20]  desk and give it to them.
[370.20 --> 372.88]  And then they would enter the code and then that would go into their paycheck.
[373.30 --> 377.68]  And this person, by the time I gave them one, because they'd been at the company a while,
[377.74 --> 382.54]  by the time I came over and gave him one, Nick would basically take the little, the cork
[382.54 --> 382.80]  board.
[383.38 --> 384.48]  What do you call it in America?
[384.76 --> 388.50]  I'm like, I want to call it a thumbtack or a push pin, but I don't know what you call
[388.50 --> 388.72]  them.
[388.98 --> 389.14]  Yeah.
[389.34 --> 389.86]  Both of those.
[389.86 --> 395.60]  So he took that out and he had so many of them that he couldn't get the push pin all
[395.60 --> 398.78]  the way through, like all of them without it falling off the wall.
[398.88 --> 400.50]  So he had to like start another pile.
[400.92 --> 404.76]  And I think that that sort of shows how much everybody really valued those skills that he
[404.76 --> 405.14]  had.
[405.18 --> 407.96]  And it made me want to become that sort of person.
[408.46 --> 408.72]  Love it.
[408.96 --> 409.28]  Love it.
[409.30 --> 410.24]  Let's kick it over to K-ball.
[410.30 --> 410.68]  What you got?
[411.14 --> 411.40]  Yeah.
[411.54 --> 412.72]  I've been thinking about this.
[413.02 --> 416.08]  So I want to highlight a couple of skills and I'm going to highlight particular people.
[416.08 --> 421.12]  And these are skills that I, there are strengths that I don't have really, or that are, you
[421.12 --> 422.40]  know, I might be okay on them, but not.
[422.50 --> 423.68]  So it really stands out to me.
[424.20 --> 430.26]  So the first one that I want to highlight is there's a set of people out there that really
[430.26 --> 431.96]  master their tools.
[432.26 --> 436.14]  Like they have their editor tuned to the finest thing and they know how to do everything.
[436.28 --> 440.02]  So a couple of people that strike me at this one is our own Nick Neesey.
[440.16 --> 444.00]  Like if you've ever seen his Vim config, it is cray cray.
[444.00 --> 449.64]  I was updating my, I got a new laptop and I was like, okay, I'm going to just steal his
[449.64 --> 450.74]  config, which I did.
[450.84 --> 453.20]  And I have no idea what like 90% of it does.
[453.30 --> 456.20]  Like there's so much in there and he knows every piece of it.
[456.36 --> 457.58]  He's just like a master.
[458.20 --> 462.72]  The other someone I worked with years ago, a gentleman by the name of Brad Fultz, who also
[462.72 --> 465.72]  just like, he knew his tools inside and out.
[465.78 --> 468.68]  And it was just this incredible feel of like, this is a craftsperson.
[468.88 --> 473.28]  They know what they're working with and they have it tuned to the nth degree.
[473.28 --> 474.84]  So that's something I admire.
[474.92 --> 479.02]  It's something I'm not good at, but really when you watch a master at work, it's incredible.
[479.54 --> 485.64]  The other thing that I want to highlight is the capability of really like diving deep
[485.64 --> 490.16]  on a problem and researching all of the ways that people have done it in the past and kind
[490.16 --> 494.22]  of drawing out and synthesizing the best pieces of each of those things.
[494.64 --> 498.82]  And there's a person I'm thinking of in particular that I worked with on an open source project
[498.82 --> 500.12]  on Zurb Foundation.
[500.66 --> 504.66]  Engineer, running guy by the name of Brett Mason, who I think listens to this podcast.
[505.00 --> 506.10]  So Brett, props to you.
[506.44 --> 514.36]  He is incredible at researching a topic area, looking at 10 or 30 different ways that people
[514.36 --> 519.22]  have solved a problem and drawing out the best pieces of each one.
[519.66 --> 522.46]  And I really admired that when that happened.
[522.54 --> 527.42]  So those are a couple of both shout outs and strengths that I kind of wish I had, but I
[527.42 --> 528.42]  definitely don't.
[528.48 --> 529.60]  There's some really good ones.
[529.70 --> 530.54]  Thanks for sharing those.
[531.34 --> 531.74]  Absolutely.
[532.30 --> 532.90]  Divya, how about you?
[532.94 --> 534.32]  You put some thought into this?
[534.72 --> 534.98]  Yeah.
[535.24 --> 540.04]  So I think I'll speak generally and then maybe I can pull it down to like actual specific
[540.04 --> 540.46]  people.
[541.00 --> 544.44]  I think what Suze is talking about with like communication like really resonates.
[545.06 --> 549.82]  And it's actually something I've been thinking about this week because I find that communication
[549.82 --> 555.88]  is a little underrated in tech because I feel like people consider it a soft skill and
[555.88 --> 556.78]  it's not as important.
[557.24 --> 563.76]  But I think it's so important because you need to be able to talk to people at their
[563.76 --> 564.28]  level.
[564.80 --> 569.88]  Talking to someone is one thing, but being able to understand process and then like speak
[569.88 --> 575.04]  to someone where they're at with the proper words is a lot of work.
[575.70 --> 580.50]  And every time I communicate, I try to be better because I'm obviously not the best at it.
[580.50 --> 584.12]  And because sometimes I'll say something and I'll be like, wait, I didn't intend for it
[584.12 --> 585.28]  to come across as that way.
[585.48 --> 586.92]  Like, but this person was offended.
[587.22 --> 588.72]  Like, what can I do in the future?
[589.48 --> 594.88]  I think a successful developer is also someone who's able to communicate both to like people,
[595.18 --> 599.82]  like any other developers or just people in general and also upper management as well.
[599.90 --> 603.22]  Just like being able to talk like to different levels.
[603.22 --> 608.76]  So like across your skill set, below your skill set and above as well, because I think
[608.76 --> 613.28]  that is a huge thing that is completely underrated.
[613.68 --> 619.68]  Like something that I definitely am like learning a lot about from liaising with developers that
[619.68 --> 620.72]  I admire and so on.
[621.02 --> 624.96]  One example of a person I think is great is like Sarah Dresner.
[625.50 --> 628.02]  She's my manager now, which I think is wonderful.
[628.22 --> 629.28]  That's awesome, right?
[629.28 --> 633.56]  Yeah, because she moved over from Microsoft.
[635.38 --> 636.42]  I forgive you.
[636.48 --> 637.18]  I forgive you.
[637.46 --> 639.18]  We got to share her around, you know.
[639.40 --> 640.60]  I know she's wonderful.
[640.60 --> 645.50]  And she's just able to communicate on a level that I find admirable.
[645.80 --> 650.14]  I basically report to her and she speaks to me on like a level where she's like, how can
[650.14 --> 651.78]  I get you to where you want to be?
[652.02 --> 653.12]  So I can have that.
[653.18 --> 655.96]  And I feel like honest, like I can have an honest conversation with her.
[655.96 --> 660.86]  And she's also able to take concerns that I have, translate them into actionable steps
[660.86 --> 664.72]  that she can take to like upper management if need be.
[665.26 --> 670.66]  And so it's really great for someone who's being managed by such a great manager, someone
[670.66 --> 674.52]  who has such communication skills because you feel like one, someone is vouching for
[674.52 --> 677.58]  you and two, that your concerns will always be addressed.
[678.10 --> 681.42]  Sometimes it's just lip service where you're like, yeah, of course, like I hear you.
[681.42 --> 686.04]  And someone who might speak to you on your level trying to make you feel heard, but then
[686.04 --> 690.32]  you're not heard because when they're talking to someone else who is actually making decisions,
[690.42 --> 691.22]  they'll be like, oh, whatever.
[691.36 --> 691.92]  We don't care.
[692.02 --> 693.40]  Like we're going to do this thing instead.
[694.00 --> 697.68]  And so I think that is really key and really cool.
[697.98 --> 702.22]  The other thing that I think is really important is also this idea of sponsorship.
[702.22 --> 708.98]  So Lara Hogan wrote a post about mentorship versus sponsorship, which is something that
[708.98 --> 715.38]  resonates with me a lot because for me, I've always tried to mentor people.
[715.76 --> 720.56]  And I think this is something that happens a lot with like women and minorities in general.
[720.56 --> 723.88]  They tend to get a lot of mentorship, but not sponsorship.
[724.00 --> 729.10]  So the difference is that mentorship is like, oh, let me help you like with skills, development,
[729.10 --> 731.32]  like I'll spend time with you one on one.
[731.64 --> 736.44]  But sponsorship is when you kind of elevate the person and give them opportunities, make
[736.44 --> 738.78]  connections like both are valuable.
[738.86 --> 745.16]  But sponsorship has this ability to take someone's career and then like rocket them much further
[745.16 --> 747.18]  than mentorship could ever do.
[747.32 --> 750.24]  And I think there's so many people in the industry who do that.
[750.34 --> 751.22]  I can't even name.
[751.30 --> 753.12]  I don't name names because there's so many.
[753.82 --> 755.22]  Sarah obviously is one of them.
[755.30 --> 756.22]  She's great at this.
[756.40 --> 758.12]  Lara Hogan is great at this.
[758.12 --> 763.66]  And like there's lots of like Sarah Stouidan, who's in CSS and SPG World does this a lot
[763.66 --> 765.38]  and a lot of names I can drop.
[766.06 --> 770.78]  And yeah, I think it's so valuable and something that I want to do more of because there are
[770.78 --> 772.88]  lots of times where I'll be like, oh, yeah, I can mentor you.
[773.04 --> 775.10]  But mentorship is one thing and it's really important.
[775.10 --> 780.48]  But it's also like, how can I use my connections to help someone else?
[780.52 --> 785.00]  Because I've benefited from that where someone else has been like, hey, you should talk to
[785.00 --> 789.38]  this person and then that has led to either an opportunity to speak at a conference, a
[789.38 --> 792.40]  job opportunity, like something that would help me move upwards.
[793.06 --> 796.76]  And so like just being able to pay that forward is huge.
[796.80 --> 800.18]  And it's something that I really aspire to do more.
[800.56 --> 801.16]  That's awesome.
[801.22 --> 804.14]  I'd like to point out the things that we're discussing here.
[804.14 --> 809.22]  As I kicked it off, I talked about inherent strengths or maybe, you know, God given talent
[809.22 --> 815.42]  or whatever that's called versus learned skills or things that you can acquire based on effort.
[815.42 --> 820.62]  And so far, we've talked about compromise, communication, tool mastery, deep dives into
[820.62 --> 822.42]  history, more communication.
[823.22 --> 824.24]  And it's worth pointing out.
[824.36 --> 828.02]  And especially in our industry, we have different forms of communication that all can be mastered,
[828.08 --> 828.22]  right?
[828.24 --> 831.10]  You have audible text based conversation communication.
[831.10 --> 836.78]  You have written communication, which is a completely other related but different medium
[836.78 --> 838.84]  skill sponsorship.
[838.84 --> 844.78]  These are all things that with effort and application, everybody can be great at these
[844.78 --> 845.06]  things.
[845.46 --> 847.72]  And these are things that make great developers.
[848.32 --> 854.42]  And so I think it's just really cool how many aspects of what we do are things that are
[854.42 --> 859.62]  available to anybody with effort in terms of like, what does it take to, you know, cable
[859.62 --> 862.26]  really admires when people do dives into history?
[862.36 --> 863.96]  Well, that's, I mean, anybody can do that.
[864.02 --> 867.52]  You just got to actually do the deep dive into the history and you have to advance your
[867.52 --> 869.92]  skills at reading and those kinds of things.
[870.12 --> 873.04]  But I just love how approachable all these strengths are.
[873.14 --> 878.60]  So if they are weaknesses of yours, you can turn them into strengths by way of effort.
[878.74 --> 883.68]  One thing that I would like to point out, which teeter totters a little bit into the realm
[883.68 --> 888.70]  of, I don't know if it's personality traits, but there are aspects of what we do where
[888.70 --> 892.44]  some people are naturally given to them over others.
[892.44 --> 894.50]  And yet you can still level up your game.
[894.60 --> 899.28]  And one thing that I think really makes for me an admirable developer, which are these
[899.28 --> 900.68]  are people that we talk to a lot.
[900.78 --> 907.40]  I mean, I'm talking to a few of them right here, but on our shows is an ability to think
[907.40 --> 915.08]  systematically and to hold a system in your head and the larger the systems or the system
[915.08 --> 920.64]  that you can hold in your head at once and comprehend and retain the context of the system.
[920.76 --> 926.30]  The larger that system is to me, the more admirable and the more skilled or strong that
[926.30 --> 927.16]  strength is.
[927.30 --> 930.76]  A couple of people that come to mind, which aren't, these are just people I've met over
[930.76 --> 931.22]  the years.
[931.34 --> 932.94]  A lot of them are language designers.
[933.22 --> 935.94]  I can't pronounce his last name, Anders Halsberg.
[935.94 --> 940.12]  I can't remember his last name, but he's the inventor of TypeScript at Microsoft, as well
[940.12 --> 941.54]  as I think the Delphi programming language.
[941.66 --> 946.40]  This is a man who can hold, like he understands TypeScript all at once, which is incredibly
[946.40 --> 947.58]  difficult to do, right?
[947.62 --> 953.24]  Like these are complex things, maths with a reprogramming language, people who can take
[953.24 --> 960.80]  the entire domain of an area and they can filter all of the questions and all the ideas
[960.80 --> 965.84]  and the features and the bugs through an understanding, especially when you get to application systems.
[965.94 --> 973.10]  It is an incredibly important skill and one where people who have that strength will
[973.10 --> 973.68]  do very well.
[974.24 --> 979.38]  So speaking of this panel, let's now turn a little bit inward and let's share some of
[979.38 --> 980.36]  our own personal strengths.
[980.46 --> 984.92]  Now, I don't, I know none of us want to be up here boasting and bragging, but I would ask
[984.92 --> 989.08]  you, you know, don't be too shy because we all have our own strengths and we're going to
[989.08 --> 991.52]  get to our weaknesses, which I think will be a fun segment for sure.
[991.52 --> 996.98]  But if you had to be honest and talk about yourself just a little bit, what would be
[996.98 --> 1002.66]  your personal greatest strength or strengths or things that you really see as assets in
[1002.66 --> 1005.18]  your developer career that you can share with us?
[1006.06 --> 1008.34]  Selflessness, I guess, is the first one that we all have.
[1009.12 --> 1010.46]  Nobody wants to take the spotlight.
[1011.00 --> 1012.42]  Okay, I'm going to be that school teacher.
[1012.54 --> 1013.44]  I'm going to start calling on people.
[1013.56 --> 1015.22]  Let's start with K-Ball this time.
[1015.76 --> 1016.84]  Okay, let's see.
[1016.94 --> 1018.42]  So greatest strengths as developer.
[1018.42 --> 1022.42]  There are two things that come to mind.
[1023.38 --> 1027.22]  One of those is kind of in this communication domain.
[1027.84 --> 1033.04]  One of the best definitions I heard for the responsibilities of a tech lead or somebody
[1033.04 --> 1036.96]  who's really like more advanced as a developer and something that resonates strongly because
[1036.96 --> 1041.06]  it's an area that I've invested a lot in and I feel like I have a strength in is being
[1041.06 --> 1049.00]  able to translate business and product requirements and desires into technical requirements and
[1049.00 --> 1049.54]  architecture.
[1050.34 --> 1055.42]  So performing the translation step between we have this problem or we have this thing we're
[1055.42 --> 1062.48]  trying to accomplish or even just like here's the product or business outcome we want and
[1062.48 --> 1066.08]  say, okay, here's an architecture that we could build that would accomplish that.
[1066.08 --> 1071.82]  Here's how we can break that down into steps and actually task that out into software things that
[1071.82 --> 1072.48]  we can do.
[1073.00 --> 1078.88]  That's something that I've come to realize is actually quite hard, but it's something that
[1078.88 --> 1081.22]  for whatever reason I've always been pretty good at.
[1081.48 --> 1085.52]  The other one that I think comes up is just I'm stubborn.
[1086.22 --> 1087.38]  You stole mine.
[1087.94 --> 1088.52]  I know, right?
[1088.64 --> 1093.62]  Well, it's a thing because I used to always be the one who like if there was a bug you
[1093.62 --> 1099.06]  couldn't solve like, okay, eventually if I would come to me and if it took me two weeks
[1099.06 --> 1103.08]  of banging my head against it to like, I'd try this and try that and try that and go.
[1103.20 --> 1108.32]  But eventually I would get that damn bug, you know, and that has served me very well because
[1108.32 --> 1110.20]  that process also teaches you a lot.
[1110.34 --> 1114.54]  And so having this strength of stubbornness of like, I'm just going to keep going until
[1114.54 --> 1119.52]  I figure this darn thing out then helps with many other areas of learning.
[1120.70 --> 1121.14]  100%.
[1121.14 --> 1123.02]  All right, Divya, let's kick it back to you.
[1123.02 --> 1125.34]  Ooh, this is a hard one.
[1125.78 --> 1131.34]  I think I have a sense of like, I really care about who's using the thing that I'm building,
[1131.84 --> 1137.08]  which is why I'm really drawn to like the front end of things in the first place, because
[1137.08 --> 1142.08]  that's where I think a lot of people interface with like an application you're working on.
[1142.42 --> 1147.02]  And it's something that I care a lot about just to be like, is it clear?
[1147.24 --> 1148.32]  What's the user flow?
[1148.32 --> 1152.42]  I don't know much about UX besides just like things I teach myself.
[1153.02 --> 1157.20]  But I think it's really fascinating and super fun to just like work on that problem space
[1157.20 --> 1159.46]  because there's so many different roads you can take.
[1159.54 --> 1160.66]  There's no like right answer.
[1161.10 --> 1162.18]  And there's a lot of testing.
[1162.34 --> 1166.82]  There's a lot of people you can talk to to ask them how they're using stuff and then try
[1166.82 --> 1169.62]  to figure out how to solve for specific use cases.
[1169.62 --> 1175.46]  And then alongside that also is that I really like taking something like very technical
[1175.46 --> 1177.32]  and then making it understandable.
[1178.78 --> 1181.42]  It's something that I never noticed I was good at.
[1181.50 --> 1186.92]  Someone actually told me that because I like, for example, recently I gave a talk about authentication
[1186.92 --> 1191.08]  and I was actually surprised because to me, because I've worked on it so much.
[1191.08 --> 1192.80]  I was like, I'm sure everyone knows this.
[1192.88 --> 1196.74]  And I'm the noob who like is like, JSON web tokens.
[1196.86 --> 1197.58]  How do they work?
[1197.58 --> 1201.66]  And I only just figured out like the different pieces and how to build one and whatever.
[1202.06 --> 1205.68]  And I gave a talk about it, expecting people to be like, yeah, I knew everything.
[1205.86 --> 1209.30]  And most people who came up to me afterwards, it's like, actually, I never thought about
[1209.30 --> 1213.20]  a JSON web token deeply besides just needing it to like exchange information.
[1213.20 --> 1219.34]  And so, yeah, I just like, I think I underestimate this, but I have so far been able to take something
[1219.34 --> 1223.74]  that is technical and then break it down to like understandable chunks.
[1224.02 --> 1230.34]  I think I attribute that to having taught classes before to like programmers and non-programmers
[1230.34 --> 1233.92]  alike and failing and maybe being successful at some point.
[1234.08 --> 1239.10]  And just like the ebb and flow of that, I think, has influenced the way I approach just
[1239.10 --> 1240.32]  learning materials.
[1240.32 --> 1247.62]  To me, it's really valuable and I find a lot of joy in helping someone learn a thing because
[1247.62 --> 1252.62]  a lot of the times when I'm learning something, sometimes resources might not exist or resources
[1252.62 --> 1256.24]  would exist, but it's very confusing and like not very clear.
[1256.94 --> 1259.22]  And then I would go through the trouble of understanding it.
[1259.30 --> 1262.84]  And then I'm like, let me make it better for like someone else so they don't have to read
[1262.84 --> 1265.94]  this like crazy white paper to understand how something works.
[1266.34 --> 1267.04]  Very good.
[1267.14 --> 1267.38]  Suze?
[1267.38 --> 1270.70]  I think what's already been said, I've resonated a lot with.
[1270.78 --> 1273.30]  I think that I have the stubbornness that people talk about.
[1273.48 --> 1274.72]  I usually just call it grit.
[1275.64 --> 1280.78]  Grit has had a lot of studies on it and it's been shown to kind of like predict someone's
[1280.78 --> 1283.60]  success at general things in life, which is kind of cool.
[1284.18 --> 1287.32]  And then everything that Divya said just resonated with me.
[1287.84 --> 1292.06]  The disadvantage to going third is that sometimes people say the things that you were going to
[1292.06 --> 1296.36]  say, but in a nice way, it reminds you that you do have different skills that you might,
[1296.64 --> 1299.78]  you know, when somebody says a skill and it resonates with you, you probably realize you
[1299.78 --> 1300.34]  have that skill.
[1300.46 --> 1304.52]  So that's kind of very humbling and nice to think about is that we all have lots of different
[1304.52 --> 1304.84]  skills.
[1305.02 --> 1309.14]  But if I was going to pick one that hasn't been mentioned yet, over the last two years,
[1309.14 --> 1313.10]  I've gotten really good at ramping up on new technical topics very quickly.
[1313.10 --> 1316.54]  And part of that for me has been a necessity of the job.
[1316.90 --> 1321.52]  I mean, when I took on a role in developer relations for Azure, when you think about Azure,
[1321.72 --> 1326.24]  it's, you know, a whole collection of cloud services and there's a lot of them, right?
[1326.34 --> 1330.34]  I've been, you know, thrown into situations where I've had to ramp up on a specific Azure
[1330.34 --> 1334.82]  technology or a technical concept that I wasn't, you know, well-versed in very, very quickly.
[1335.34 --> 1341.08]  And so over the last, I think, two years, because of that and because of how I sometimes
[1341.08 --> 1345.78]  stumble into things when I'm live streaming my code where I don't know what I'm doing
[1345.78 --> 1349.80]  and I have to take a breath and read some documents and do that under pressure while,
[1349.92 --> 1351.46]  you know, 200 people are watching me.
[1351.58 --> 1356.22]  Like, I've definitely seen those two things, like being thrown in the deep end of my job
[1356.22 --> 1360.08]  and also having to, like, make mistakes and stumble in front of people on my live stream.
[1360.08 --> 1365.10]  They've made me very good at just being able to stay focused and learn something new, learn
[1365.10 --> 1370.86]  the most important parts, but then also try to get as deeply into that topic as possible.
[1371.08 --> 1373.68]  For, you know, actually being able to understand it.
[1373.82 --> 1379.36]  And then that dovetails nicely into me being able to teach that to somebody else as well.
[1379.92 --> 1381.70]  So I think that's a really nice skill to have.
[1381.94 --> 1386.76]  You just feel so much less anxious in this industry when you're trying to keep up on top
[1386.76 --> 1387.26]  of everything.
[1387.44 --> 1390.76]  If you've sort of gotten to a point where you can ramp up very quickly.
[1391.52 --> 1394.04]  Well, if you think going third is hard, try going fourth sometime.
[1394.14 --> 1394.64]  No, just kidding.
[1394.98 --> 1397.46]  Because basically, K-Ball stole mine, as I said.
[1397.46 --> 1402.80]  And I think we're seeing a theme here with regard to one particular strength, which is
[1402.80 --> 1404.16]  maybe you can call it grit.
[1404.34 --> 1406.34]  Maybe you can call it stubbornness.
[1406.44 --> 1409.16]  The word that I tend to think of, which I think grit's actually a better one.
[1409.24 --> 1410.12]  So I'm going to switch to that.
[1410.18 --> 1415.22]  But I've used the word intrepid, which is fearlessness or adventurousness.
[1415.30 --> 1419.32]  It's kind of the idea that you don't actually know what you're getting yourself into.
[1419.42 --> 1422.12]  And that it's kind of the ignorance is bliss, certain situation.
[1422.12 --> 1427.02]  But this is actually the skill I was referring to on that episode of Backstage, which is
[1427.02 --> 1433.94]  if there's a challenge that's been placed on my desk, I'm just going to figure it out
[1433.94 --> 1434.16]  somehow.
[1434.54 --> 1436.92]  I know that the confidence to do that.
[1437.36 --> 1439.94]  Maybe it's going to take 10 minutes and I'll feel good.
[1440.00 --> 1442.74]  Maybe it's going to take three days and I'll hate myself.
[1443.08 --> 1444.64]  But eventually I'm going to get there.
[1445.00 --> 1446.94]  And I have confidence that that's the case.
[1446.94 --> 1452.54]  So that allows me to take on tasks that might otherwise scare me off has been a huge strength
[1452.54 --> 1453.12]  for me.
[1453.48 --> 1456.24]  So that one, I'll just iterate it for the third time, I suppose.
[1456.80 --> 1460.12]  The other thing that I used to say, which is kind of a joke, but it's true.
[1460.28 --> 1463.90]  I tell people that my greatest strength as a developer is fear of irrelevance.
[1464.80 --> 1469.40]  And the reason I say that is because industry moves so fast.
[1469.54 --> 1473.36]  And I've always had like this feeling of in six months, I'm going to be useless.
[1474.10 --> 1476.00]  And maybe that wasn't always true.
[1476.00 --> 1478.14]  And so far it hasn't proven not to be true.
[1478.22 --> 1482.44]  Maybe it's a self-fulfilling prophecy because that fear of becoming irrelevant very quickly
[1482.44 --> 1489.06]  has led me to always stay up to date and even ahead of a lot of people in terms of techniques
[1489.06 --> 1489.84]  and trends.
[1489.98 --> 1494.72]  And I think it's probably, you know, at a meta level led me to be, you know, where I am
[1494.72 --> 1497.16]  with changelog because of that fear.
[1497.34 --> 1500.54]  And so it's kind of turning a weakness into a strength in that regard.
[1500.78 --> 1505.34]  I'll say one more real quick before we wrap up, which is going to sound super simple.
[1505.34 --> 1506.18]  And it really is.
[1506.26 --> 1507.84]  It's just easy to say and hard to do.
[1507.90 --> 1512.08]  And it's not just for developers, but it's for career and industry in general.
[1512.76 --> 1513.44]  Here's it is.
[1513.88 --> 1516.74]  When I say I'm going to do something, I do it.
[1517.44 --> 1519.92]  And that should be in the chat.
[1519.98 --> 1522.10]  They're talking about soft skills as table stakes.
[1522.48 --> 1526.88]  I think table stakes is when you say you're going to do something, you should do it.
[1527.32 --> 1528.70]  And so I hold myself to that standard.
[1528.80 --> 1530.14]  Now, do I always achieve that standard?
[1530.20 --> 1530.88]  No, of course not.
[1530.88 --> 1532.06]  I fail all the time.
[1532.30 --> 1536.26]  But my goal is when my word goes out, then I follow up on my word.
[1536.82 --> 1543.50]  And that has been a huge asset to me over time because unfortunately, there's a lot of
[1543.50 --> 1546.24]  people that say they're going to do things and then they don't do them.
[1547.02 --> 1550.08]  And if you can be the person who says you're going to do something and then you follow up
[1550.08 --> 1558.40]  and you do it on a reliable, consistent basis, well, that's a very, very valuable thing in
[1558.40 --> 1559.10]  industry.
[1559.32 --> 1564.14]  And it's proven to be one of the reasons I think I've had success that I have in both
[1564.14 --> 1569.08]  as a developer and just as a business person in general is because if I say I'm going to
[1569.08 --> 1570.08]  do something, then I do it.
[1570.52 --> 1573.40]  And it's a simple equation, but it pays dividends.
[1574.14 --> 1574.58]  I like that.
[1574.66 --> 1576.12]  That's really simple, but very powerful.
[1576.74 --> 1578.14]  And again, it's something that we all can do.
[1578.14 --> 1583.02]  There are times where, of course, like extenuating circumstances, you totally forgot, you feel
[1583.02 --> 1583.40]  terrible.
[1584.24 --> 1589.60]  But nine times out of 10, if you can just stick to that word and do that over a course of
[1589.60 --> 1594.48]  years, I believe that you will be successful in business because it's an incredibly, incredibly
[1594.48 --> 1595.42]  valuable thing.
[1595.84 --> 1597.84]  And like you said, it's pretty simple.
[1598.38 --> 1599.56]  You just got to actually go do it.
[1608.14 --> 1610.14]  This episode is brought to you by Manifold.
[1610.44 --> 1615.12]  Manifold is the easiest way for you to discover, buy, and manage the best developer services
[1615.12 --> 1617.22]  for your application, regardless of your cloud.
[1617.62 --> 1622.06]  Manifold is changing the way developers and cloud services work together, easily find,
[1622.32 --> 1624.16]  integrate, and share the best cloud services.
[1624.60 --> 1628.68]  And what's interesting is as you assemble your stack, you can organize your services and
[1628.68 --> 1633.08]  their projects, then create and invite team members to collaborate via role-based access
[1633.08 --> 1633.58]  controls.
[1633.58 --> 1635.88]  And I love their hacker-friendly sign-up experience too.
[1636.12 --> 1640.70]  For example, if you're on a Mac, you can install the Manifold CL Avia Homebrew, then run Manifold
[1640.70 --> 1641.62]  Sign-Up to get started.
[1641.86 --> 1642.64]  It's so easy.
[1643.02 --> 1646.18]  Learn more and discover the best cloud services for your projects at Manifold.co.
[1646.64 --> 1648.56]  Again, Manifold.co.
[1648.56 --> 1657.68]  Manifold.co.co.
[1661.68 --> 1664.78]  Well, enough boasting about ourselves.
[1664.90 --> 1665.80]  Let's get real.
[1666.68 --> 1668.76]  And let's talk about things that are holding us back.
[1669.08 --> 1669.88]  Our greatest weaknesses.
[1670.62 --> 1671.56]  We all have them.
[1671.62 --> 1673.50]  We all know them very well, I'm sure.
[1674.08 --> 1678.18]  And we're now going to focus on them for a while and share that.
[1678.18 --> 1678.96]  So I'll go first.
[1679.68 --> 1684.92]  And I will say that one great weakness that I have and that is a thing I admire in other
[1684.92 --> 1688.56]  people, and I haven't been able to change it, unfortunately, over the years, is that
[1688.56 --> 1692.60]  I do not think in libraries very well.
[1692.68 --> 1696.30]  I don't think in general use software.
[1696.62 --> 1698.02]  I think in very specific software.
[1698.02 --> 1701.42]  And I do think in abstractions.
[1701.62 --> 1704.64]  But there are always tiny little abstractions that I can reuse.
[1704.84 --> 1709.84]  And they're never general purpose abstractions that everybody can use, which is more useful
[1709.84 --> 1710.50]  software, right?
[1710.54 --> 1716.00]  If I write a thing for my thing and I can pull it out and it can be used by 100,000 other
[1716.00 --> 1718.40]  people, that was very valuable software.
[1718.40 --> 1721.26]  And I'm sure there's times that I can do that.
[1721.76 --> 1725.78]  But either it just never crosses my mind or I think, oh, it's just too much work.
[1725.84 --> 1726.70]  I'm not going to do it.
[1726.84 --> 1731.94]  Or I feel like I'm not very good at API design for anybody but myself, which is probably true
[1731.94 --> 1732.30]  as well.
[1732.36 --> 1732.78]  Another weakness.
[1733.16 --> 1736.30]  I'm very good at designing things for me, but not for other people.
[1736.80 --> 1738.50]  Whatever it is, I stop short.
[1738.78 --> 1744.12]  And I see so many people in companies have like a product and then they pull portions out
[1744.12 --> 1747.76]  of the product and they give them to the world and the world benefits.
[1748.44 --> 1749.32]  And I love that.
[1749.82 --> 1751.10]  And it's the beauty of open source.
[1751.88 --> 1753.56]  And yet I'm not good at doing it.
[1753.96 --> 1755.84]  And I haven't been able to get good at doing it so far.
[1756.24 --> 1759.04]  But sometimes with a weakness, just recognizing it's the first step.
[1759.14 --> 1760.92]  So maybe I can start to get better at that.
[1760.98 --> 1762.02]  But it's definitely a weakness of mine.
[1762.44 --> 1766.42]  I don't think in generic library abstractions.
[1766.86 --> 1769.16]  And so I think my software suffers as a result.
[1769.76 --> 1770.12]  All right.
[1770.14 --> 1771.72]  Let's go over to KBall.
[1772.22 --> 1772.62]  Weaknesses.
[1772.62 --> 1773.56]  All right.
[1773.56 --> 1782.16]  So my one weakness that stands out to me is I'm actually pretty darn bad at getting
[1782.16 --> 1785.12]  way down in the nitty gritty on stuff.
[1785.44 --> 1788.44]  Like I'm really good at getting software from zero to 80%.
[1788.44 --> 1792.54]  And there are some developers who are really good at polishing everything and getting everything
[1792.54 --> 1796.76]  fully tested and giving like they know all the latest language techniques and whatever.
[1797.46 --> 1799.14]  I'm bad at that.
[1799.24 --> 1800.02]  I'm bad.
[1800.02 --> 1804.00]  I extremely common that I'll work with somebody and they'll be way more junior.
[1804.10 --> 1805.58]  And they're like, you know, there's a better way to do this.
[1805.70 --> 1808.42]  Or like, they'll be picking up the pieces down there.
[1808.86 --> 1813.72]  And, you know, it goes to something we'll talk about later in terms of partnering with
[1813.72 --> 1813.96]  people.
[1813.96 --> 1816.60]  Because I think, you know, there are people who are really good at that.
[1816.64 --> 1818.04]  And I like to work with them.
[1818.04 --> 1825.34]  Because I don't have the level of deep dive detail orientation that some amazing developers
[1825.34 --> 1825.64]  do.
[1825.92 --> 1828.74]  That's a good that's a good segue for mine, actually.
[1828.92 --> 1830.98]  So I'm a very detail oriented person.
[1831.30 --> 1832.50]  We should work together.
[1832.98 --> 1833.86]  We should.
[1834.10 --> 1834.62]  We should.
[1834.62 --> 1839.60]  But I have these two weaknesses that really let me down in order to take advantage of
[1839.60 --> 1839.84]  that.
[1840.26 --> 1843.44]  The first one is that I type slower than I think.
[1843.76 --> 1849.48]  And so I've been really trying to improve my typing speed over the last, I would say I
[1849.48 --> 1852.08]  started seriously about six weeks ago.
[1852.18 --> 1853.40]  And I've been practicing every day.
[1853.44 --> 1855.76]  And I'm trying to change my typing style and things like that.
[1856.16 --> 1859.88]  And it's because I actually have a very bad short term memory.
[1860.14 --> 1862.00]  And so I'm super excited about details.
[1862.00 --> 1866.12]  My brain is already sort of collecting all of them, but it cannot retain them.
[1866.46 --> 1872.94]  And if I can't type fast enough to get them out onto, you know, into Vim or onto the, you
[1872.94 --> 1875.72]  know, the documentation that I'm writing, I lose it.
[1875.82 --> 1879.72]  And so if you watch my stream, I mean, part of this is because I'm on the spot in front
[1879.72 --> 1881.78]  of a bunch of people and I'm talking aloud, right?
[1881.80 --> 1883.44]  So my concentration is a little off.
[1883.72 --> 1885.08]  But even off stream, I do this.
[1885.40 --> 1890.82]  You'll see that if I have several Vim buffers open and I have several files open in my IDE,
[1890.82 --> 1895.84]  that's the equivalent, I'll basically be in one file and I'll, you know, write a new
[1895.84 --> 1897.18]  variable or a new function name.
[1897.28 --> 1899.74]  And then I'll jump over to the other file to use that function.
[1899.74 --> 1903.14]  And I will totally forget what I just called that variable name.
[1903.64 --> 1905.86]  And so that's how bad my short term memory is.
[1905.90 --> 1910.00]  I have a very good long term memory where again, like I tweeted this week that I remembered
[1910.00 --> 1912.66]  something from the Dewey decimal system like 14 years later.
[1913.12 --> 1916.88]  You know, I have a really great detail oriented long term memory.
[1916.88 --> 1921.50]  But when I know that I only need something for, you know, 30 seconds to a minute, I really,
[1921.66 --> 1923.32]  really struggle in that short term space.
[1923.44 --> 1926.44]  And so I've been working on my typing to get faster.
[1926.64 --> 1930.56]  And then I've also been looking into how I can actually improve my memory because it is
[1930.56 --> 1934.42]  something you can work on even if you are predispositioned to be bad at it.
[1934.84 --> 1935.86]  That's a very interesting one.
[1935.94 --> 1936.88]  Okay, Divya, how about yourself?
[1937.40 --> 1937.70]  Cool.
[1937.90 --> 1940.00]  I can go off of the same topic as well.
[1940.00 --> 1945.26]  For me, I'm like similar to Sue's, very detail oriented.
[1945.66 --> 1948.96]  But then I also like get into rabbit holes very fast.
[1950.58 --> 1954.44]  Because it's like the yak shaving thing where you're like, oh, I need to fix this thing.
[1954.54 --> 1957.08]  And then you're like, oh, wait, that depends on this other thing.
[1957.12 --> 1958.90]  And then you're like, oh, that depends on this other thing.
[1958.96 --> 1960.90]  And then you go down into like the source code.
[1960.90 --> 1963.30]  And then you go through like node modules folders.
[1963.30 --> 1964.92]  And then you're like right in.
[1965.08 --> 1966.10]  What am I working on again?
[1966.22 --> 1968.58]  And that actually happened like, was it yesterday?
[1968.58 --> 1969.86]  It might have been yesterday.
[1970.18 --> 1976.28]  I was trying to figure out like an issue that I was having with like a specific tool.
[1976.46 --> 1982.26]  And then I ended up not being sure how to like, I didn't want to pull down like the GitHub
[1982.26 --> 1985.72]  like repo for that specific module and then work on it.
[1985.72 --> 1989.38]  And then try to like link it to the local one to see if it worked.
[1989.50 --> 1994.52]  So I pretty much like went into the node modules, into the folder, into like the actual thing
[1994.52 --> 1996.02]  and then tried to make changes.
[1996.02 --> 1999.64]  And then I was like, wait, what was I even working on?
[2000.38 --> 2004.46]  And then I have to remind myself like, wait, I think I like went too deep.
[2004.66 --> 2007.30]  And what I'm working on is not worth my time.
[2007.30 --> 2012.76]  I'm just wasting time trying to fix a thing that could have been fixed in an easier way.
[2012.90 --> 2015.16]  So like I get so caught up with that.
[2015.22 --> 2019.76]  But then at the same time, I also lose track of time when I'm like, I really need to fix this.
[2019.76 --> 2022.00]  And then I just keep hitting at it.
[2022.04 --> 2025.06]  And then I keep thinking like, oh, I need five more minutes.
[2025.06 --> 2026.28]  And then five minutes passes.
[2026.28 --> 2027.84]  And then I'm like, I need five more minutes.
[2028.02 --> 2029.82]  And then the whole day goes by.
[2029.98 --> 2030.54]  It's gone.
[2030.70 --> 2031.24]  The day's gone.
[2031.42 --> 2031.64]  Yeah.
[2031.72 --> 2033.00]  And I was like, what did I do?
[2033.08 --> 2035.40]  I just like, oh, it's so irritating.
[2035.64 --> 2039.12]  And I need this ability to just be like, no, you have 20 minutes.
[2039.12 --> 2040.98]  If you don't solve it, that's it.
[2041.12 --> 2043.10]  And then continue on to the next thing.
[2043.10 --> 2047.48]  Because otherwise, you're just going to be like going in circles and not solving any.
[2047.56 --> 2052.18]  You might learn something like in a couple of days, maybe weeks or months or whatever.
[2052.42 --> 2055.36]  Eventually, you'll learn something and there will be like some outcome.
[2055.82 --> 2057.72]  But I don't know if that's worth the time.
[2058.20 --> 2058.70]  I love this.
[2058.80 --> 2061.72]  I'm thinking of all these other weaknesses I have as everyone's talking.
[2061.82 --> 2062.76]  I feel like I go on forever.
[2063.00 --> 2070.32]  I'll add one more and then we'll move on because we have some good stuff coming up on ways of working around, teaming up, etc.
[2070.72 --> 2071.40]  Improving yourself.
[2071.40 --> 2074.34]  But I don't ever take notes.
[2074.70 --> 2075.96]  It's just like the dumbest thing ever.
[2076.34 --> 2082.86]  Even when I find answers to solutions, I'll just remember what I googled to find it and I'll just google it again the next time.
[2083.38 --> 2086.06]  And I mean, I'm 36 years old at this point.
[2086.16 --> 2091.60]  You think by now I would have learned that you should write down things once in a while.
[2092.50 --> 2094.76]  And it's a weakness of mine.
[2094.98 --> 2095.92]  I just don't take notes.
[2096.64 --> 2099.42]  And it bites me like daily, daily basis.
[2099.84 --> 2100.28]  Is that just me?
[2100.28 --> 2102.76]  I don't even know how you would organize your notes.
[2102.96 --> 2105.74]  Like a lot of the times I'll be like, oh, it's a git thing that I learned.
[2105.86 --> 2107.36]  And then it's like a JavaScript thing.
[2107.44 --> 2109.42]  And then it's this random other like dependency.
[2109.78 --> 2115.10]  So it's just like, I think I tried at one point four or five years ago to like take notes.
[2115.10 --> 2116.84]  And it was just so haphazard.
[2117.30 --> 2119.06]  It was called like TIL.
[2119.42 --> 2120.28]  Today I learned.
[2120.66 --> 2122.68]  I was like, this is such a random dog.
[2123.12 --> 2123.94]  Blog posts.
[2124.10 --> 2124.98]  Yeah, blog posts.
[2124.98 --> 2125.70]  Writing a blog.
[2126.16 --> 2131.16]  Because like, I mean, I still find myself, I'll google stuff that I'm like, I know I solved this at some point.
[2131.24 --> 2132.32]  And I'll google for it.
[2132.44 --> 2135.40]  And like, it's on my blog from a year ago or two years ago or whatever.
[2136.10 --> 2137.18]  But talk about a yak shave.
[2137.38 --> 2139.62]  You know, you set out to solve a problem.
[2139.74 --> 2140.86]  Now you're writing a blog post.
[2141.00 --> 2143.72]  You know, that's where I'm always like, ain't nobody got time for that.
[2143.72 --> 2147.96]  But yeah, I find like whenever I write a blog post, it takes me a lot longer.
[2148.36 --> 2150.92]  Like I can't just like write one and then publish.
[2151.06 --> 2153.52]  I have to, I go through the editing process a lot.
[2153.78 --> 2154.32]  Yeah, yeah, yeah.
[2154.32 --> 2160.28]  But when you, when you do that thing, like that's, I do my notes in my drafts folder for my, because I'm, my blog is a Jekyll site.
[2160.42 --> 2161.82]  So I've got a drafts folder, right?
[2161.88 --> 2164.16]  And it's, it's in my, I'm already in my terminal.
[2164.36 --> 2165.58]  I figured this thing out.
[2166.04 --> 2167.82]  Copy, paste, dump it in my drafts folder.
[2168.20 --> 2170.30]  Most of them, many of them I probably won't get to.
[2170.30 --> 2172.20]  I have a very large drafts folder.
[2172.20 --> 2176.12]  Sounds like a strength of yours and definitely a weakness of mine because I'm with Divya.
[2176.24 --> 2180.72]  I would take 20 minutes to figure out the answer and four hours blogging about it.
[2181.06 --> 2182.76]  And so that's a good idea.
[2182.86 --> 2186.20]  Just take notes as blog post drafts.
[2187.00 --> 2188.18]  There's a life hack for you.
[2196.10 --> 2198.24]  This episode is brought to you by Gage.
[2198.46 --> 2202.08]  Gage is a free and open source test automation tool by ThoughtWorks.
[2202.20 --> 2205.00]  The goal of the tool is to take the pain out of test automation.
[2205.42 --> 2210.40]  And to help with this, Gage supports specifications and markdown, which are easy to read and easy to write.
[2210.82 --> 2214.74]  Reusable specifications to simplify your code, which makes refactoring easier.
[2215.06 --> 2217.74]  And less code means less time maintaining code.
[2217.74 --> 2219.32]  And finally, integrations.
[2219.46 --> 2222.96]  Use Gage with your favorite tools and your IDEs and the ecosystem of your choice.
[2223.46 --> 2231.78]  Selenium, SciHeap Pro, CIC and CD tools like GoCD, Jenkins, Travis, and IDE support for Visual Studio, VS Code, IntelliJ and more.
[2232.02 --> 2234.90]  Head to gauge.org slash jsparty to learn more and give it a try.
[2235.12 --> 2237.56]  Again, gauge.org slash jsparty.
[2237.56 --> 2248.04]  So we've talked about some strengths and weaknesses.
[2248.70 --> 2249.60]  Strengths are strengths.
[2249.78 --> 2250.28]  You got them.
[2250.68 --> 2251.40]  You hold on to them.
[2251.46 --> 2251.98]  Don't lose them.
[2252.52 --> 2254.84]  But weaknesses is where we can really improve, right?
[2255.34 --> 2258.84]  So if we focus in on weaknesses and ask about how we can actually get better.
[2259.14 --> 2264.46]  I like to cable has some good advice for one particular weakness that I guess Divya and I have in the last segment.
[2264.46 --> 2273.32]  But what are some strategies and techniques that we and the listeners and the community can use to improve the weaknesses that we have?
[2273.92 --> 2279.06]  And what are some ways that we can suggest or maybe you've improved yourself in the past somehow?
[2279.48 --> 2280.60]  Open that up for conversation.
[2281.22 --> 2284.42]  Before I do, I actually want to challenge the premise for a second.
[2284.42 --> 2288.42]  And say that contained the assumption that really we should work on our weaknesses.
[2288.88 --> 2290.50]  I'm not 100% sure that's true.
[2291.12 --> 2297.52]  It may actually be more valuable to double down on improving our strengths and then find ways to compensate for our weaknesses.
[2297.82 --> 2301.86]  Like, for example, it's really easy to find developers to work with who are detail-oriented.
[2302.20 --> 2305.56]  One of my big weaknesses is that lowered level of detail orientation.
[2306.22 --> 2312.04]  But it comes with, like, some of my strengths are things that other developers may have challenges with.
[2312.04 --> 2319.26]  So, like, I've actually found it more productive for me to find folks to partner with than to work on that weakness.
[2319.76 --> 2321.68]  Plus, working on your weaknesses sucks.
[2322.36 --> 2324.88]  So that is a good way to...
[2324.88 --> 2329.24]  That, I guess, you could call it a strategy in terms of finding people who are good at the things that you're bad at.
[2329.34 --> 2329.66]  Absolutely.
[2329.66 --> 2332.62]  And it goes back to what I didn't say out loud, but I did write down.
[2332.72 --> 2335.88]  How do you route around your weaknesses or improve them over time?
[2335.96 --> 2337.46]  So I guess it opens up both questions.
[2337.66 --> 2339.62]  And routing around is a great strategy.
[2339.76 --> 2344.98]  There are things that I think if you are bad at them, whether it feels shitty or not, you should get better at them.
[2345.00 --> 2346.74]  And you'll be overall better at what you do.
[2347.12 --> 2349.10]  And so, assuming that we do want to improve our weaknesses.
[2349.70 --> 2355.26]  Or maybe just find that detail-oriented person and hope they want to work with you.
[2355.58 --> 2355.88]  I don't know.
[2355.92 --> 2356.96]  Suze, you're going to go first here.
[2356.96 --> 2360.56]  K-Ball rudely cut you off after 30 seconds of silence.
[2360.80 --> 2362.66]  So hop in there, Suze.
[2362.74 --> 2364.38]  Poor K-Ball takes the stage again.
[2364.78 --> 2366.56]  No, I'm so glad that K-Ball said all that.
[2366.64 --> 2369.20]  Because that actually is very relevant to what I was going to say.
[2369.30 --> 2373.84]  I think that using your strengths to help attack your weaknesses is a really good thing.
[2373.98 --> 2377.20]  So, for example, I'm really good at learning new things and ramping up on them.
[2377.70 --> 2380.38]  And that usually makes me excited, right?
[2380.44 --> 2383.46]  Like, I'm very excited and don't feel threatened about learning new things.
[2383.60 --> 2386.66]  Which is not something that I've always had in my career, but I do now.
[2386.96 --> 2390.18]  And so, if it's something such as the drudgery of learning how to type faster,
[2390.74 --> 2395.58]  you know, I'm going to essentially create a framework for myself to succeed first, right?
[2395.58 --> 2399.30]  I'm going to set goals and say, I'm going to practice for half an hour a day.
[2399.42 --> 2402.00]  And then I'm going to observe, you know, how I improve.
[2402.06 --> 2407.12]  And then if I hit this certain goal, then I'm also going to do this nice thing to reward myself,
[2407.20 --> 2407.38]  right?
[2407.38 --> 2409.40]  So, I usually set myself up with a framework.
[2409.82 --> 2411.04]  That's what makes you excited.
[2411.52 --> 2415.60]  You know, if something's drudgery, then you have to introduce other things to make it exciting.
[2416.32 --> 2420.44]  And then knowing that I'm pretty good at picking new stuff up, I'm pretty good at being disciplined
[2420.44 --> 2421.90]  to do it as well.
[2422.00 --> 2426.20]  Like, I try to take advantage of those strengths in order to work on my weaknesses, if that makes
[2426.20 --> 2426.48]  sense.
[2426.96 --> 2432.12]  You know, so for me, like, I have been dedicating X amount of time a day to practicing my typing.
[2432.12 --> 2438.42]  And then I've been dedicating half an hour a day to reading about a new topic, you know,
[2438.44 --> 2440.66]  that I think would be good for me to know.
[2440.88 --> 2444.90]  And then that way, I'm also improving things like, oh, I have this weakness about this one
[2444.90 --> 2447.00]  topic, so I'm going to learn about it.
[2447.34 --> 2451.82]  And if you could just find something that is exciting about the weakness that you're trying
[2451.82 --> 2455.76]  to work on, you know, even if you're just like giving yourself, you know, a cheap reward,
[2455.86 --> 2461.26]  like I'm going to go buy a donut if I achieve this, then that's usually a recipe for success,
[2461.26 --> 2462.74]  at least as far as I'm concerned.
[2463.00 --> 2466.86]  So yeah, that's what I'm working on right now is just like creating a disciplined environment
[2466.86 --> 2472.42]  where I'm excited about the idea of actually improving as a person and improving as a developer.
[2472.58 --> 2473.44]  And that's enough for me.
[2473.98 --> 2474.20]  Love that.
[2474.28 --> 2474.62]  Love that.
[2474.74 --> 2477.46]  Use your strengths to improve weaknesses.
[2477.80 --> 2479.30]  That's a great tip.
[2479.94 --> 2483.76]  So let's talk about some of these are subject, not subjective, but case by case.
[2483.76 --> 2487.80]  So depending on the weakness, the strategy in order to improve it would be different.
[2488.36 --> 2490.80]  And so one of the things that we talked about that we all admire is,
[2491.26 --> 2494.44]  in a great developer is communication skills.
[2494.54 --> 2496.88]  I'm going to talk about there's different kinds of communication skills.
[2497.56 --> 2498.74]  Well, there's a lot of people.
[2498.98 --> 2502.92]  And I mean, hey, there are people who are naturally gifted communicators.
[2503.06 --> 2504.04]  Most of us aren't right.
[2504.42 --> 2506.94]  And so a lot of this is learned very much so.
[2507.52 --> 2510.26]  And so how what are some tips that you all have?
[2510.70 --> 2511.84]  You guys are great communicators.
[2511.84 --> 2515.28]  I'll just go ahead and say it that got you where you are today.
[2515.42 --> 2518.88]  Like, what are some ways that people who aren't great communicators can go about improving
[2518.88 --> 2521.10]  that skill because it crosses the chasm?
[2521.66 --> 2523.60]  Industry, personal life, right?
[2523.68 --> 2527.68]  Software development, especially have to be able to communicate well to be effective.
[2527.94 --> 2530.98]  So if you aren't a great communicator, what are some things you can do?
[2531.70 --> 2533.64]  I'm a huge advocate of Toastmasters.
[2533.90 --> 2538.96]  For those who are not familiar, Toastmasters is a chapter based nonprofit organization that
[2538.96 --> 2542.10]  is focused on helping people develop communication and leadership skills.
[2542.10 --> 2546.20]  And basically, you know, it's a set of small clubs.
[2546.80 --> 2550.46]  And, you know, if you Google for Toastmasters in your neighborhood or your location, if you're
[2550.46 --> 2552.44]  in a city, you'll probably see dozens nearby.
[2553.92 --> 2556.84]  And it's literally practice.
[2556.96 --> 2560.44]  It's just a controlled, safe environment for practicing speaking.
[2560.44 --> 2566.62]  And they have both a set of curriculum to practice prepared talks and prepared speeches.
[2567.18 --> 2570.32]  But they've also got stuff for working on your impromptu speaking skills.
[2570.32 --> 2572.34]  They have stuff for working on your feedback skills.
[2572.86 --> 2575.04]  There's a whole slew of things around it.
[2575.24 --> 2578.30]  And I was a member of a Toastmasters club for about six years.
[2578.56 --> 2582.22]  I saw people coming in where like the first time they had to stand up in front of people
[2582.22 --> 2584.38]  and try to speak, they couldn't.
[2584.68 --> 2589.94]  They turned red and they just could not get a single word out going through to the point
[2589.94 --> 2595.00]  where they could get up in front of people and give a prepared speech for five to seven
[2595.00 --> 2596.66]  minutes and just do it.
[2596.92 --> 2599.76]  And, you know, it's got a bunch of different stuff in it.
[2599.76 --> 2602.72]  Um, there's lots of different ways you're because it's chapter based.
[2602.82 --> 2604.52]  Your experience is going to vary a lot by club.
[2604.60 --> 2607.84]  So if you go out and check out, you know, if you, if you're interested in doing it, check
[2607.84 --> 2611.66]  out several clubs in your neighborhood to see which one feels good to you and feels supportive
[2611.66 --> 2613.46]  and feels like an environment that you want to be in.
[2613.72 --> 2620.12]  But if you want to work on your spoken communication skills, like it is an incredible resource and
[2620.12 --> 2622.98]  it's like super, you can go as a guest as many times as you want.
[2623.04 --> 2625.04]  And a membership is like 40 bucks a year or something.
[2625.04 --> 2626.06]  So it's super affordable.
[2626.06 --> 2630.66]  And if you, if that's a hardship, like a lot of times they'll have sponsorships available.
[2630.66 --> 2634.40]  Like we had a, we had a guy come in who was literally homeless and it was attending our
[2634.40 --> 2635.08]  club.
[2635.08 --> 2637.02]  And it was amazing because he was, he was homeless.
[2637.22 --> 2639.40]  He would, uh, product of the foster system.
[2639.50 --> 2641.04]  He had all sorts of challenges.
[2641.04 --> 2645.56]  And like over the course of working with his Toastmasters club for about a year and a half,
[2645.66 --> 2648.54]  like he, his communication skills improved dramatically.
[2648.82 --> 2649.92]  He got a job.
[2650.02 --> 2653.86]  He got all sorts of other stuff out of like being able to be in an environment where he
[2653.86 --> 2654.72]  could just practice.
[2654.84 --> 2657.46]  How do I interact with other people on a regular basis?
[2658.04 --> 2660.80]  It was, yeah, highly, highly, highly recommend.
[2661.22 --> 2662.14]  That's great advice.
[2662.22 --> 2663.74]  I had never even considered that.
[2663.86 --> 2666.52]  And I have other people who've had success in Toastmasters.
[2666.66 --> 2670.16]  So I didn't even think of it, but that's, that's a great, especially just a way of getting
[2670.16 --> 2675.56]  ramped up, you know, without all the pressure live on stage with hundreds of people staring
[2675.56 --> 2675.94]  at you.
[2676.44 --> 2679.20]  Divya, do you have any advice on, on communication skills?
[2679.64 --> 2679.90]  Yeah.
[2680.12 --> 2683.20]  I think it's interesting because there's different forms of communication.
[2683.20 --> 2688.40]  So like speaking and like public speaking is one aspect of communication, which is really
[2688.40 --> 2690.02]  valuable in tech.
[2690.50 --> 2694.94]  Um, and then there's also the other aspect, which is more just in general when you're on
[2694.94 --> 2700.14]  a team, which is oftentimes you have to deal with conflict and conflict resolution.
[2700.16 --> 2702.22]  And that's something that is really hard.
[2702.22 --> 2707.48]  And I don't think is talked about a lot because it's just assumed that you'll figure it out.
[2707.48 --> 2709.52]  Like, oh, your manager will figure it out.
[2709.52 --> 2714.52]  And, um, there's a lot of, like, I've been interested in this because I've been in, in,
[2714.72 --> 2716.62]  on teams where sometimes there's a disagreement.
[2716.88 --> 2720.96]  And usually there's oftentimes on a team, there's someone with a very strong voice.
[2720.96 --> 2724.16]  And then that person overpowers the conversation.
[2725.06 --> 2729.94]  And so in general, I've, there's a lot of books on like conflict resolution and just being
[2729.94 --> 2730.84]  able to diffuse.
[2731.22 --> 2736.40]  So I think, I think it's called like difficult conversations or something, which is, it's,
[2736.40 --> 2741.02]  it's kind of broad because it goes into not just professional communication, but also
[2741.02 --> 2746.80]  just like personal relationships, friendships, like partners and whatever significant others,
[2746.80 --> 2751.62]  which is useful because I mean, you obviously have to have those conversations outside of
[2751.62 --> 2752.60]  your professional life.
[2753.16 --> 2758.92]  I think being able to have those skills to understand how to communicate is really effective.
[2759.70 --> 2764.46]  And of course, like specifically that happens a lot, like within a team, but sometimes you
[2764.46 --> 2766.94]  would have to do conflict management and resolution.
[2766.94 --> 2772.82]  If you've ever been on support or been on call, you sometimes have to deal with issues where
[2772.82 --> 2778.68]  customers are angry and that's really hard because like your knee jerk reaction is to be like,
[2778.78 --> 2780.24]  no, you didn't read the docs.
[2780.42 --> 2786.40]  We were so clear, like you're an idiot kind of thing, which like, which is not the best
[2786.40 --> 2788.34]  way to represent your product.
[2789.42 --> 2793.34]  And so just being able to have the tools and techniques to do that.
[2793.44 --> 2799.56]  And generally like my rule of thumb in whenever I have to deal with like a support thing or someone
[2799.56 --> 2805.66]  who's really angry is to not respond immediately, which is like something I want to do and is
[2805.66 --> 2806.58]  probably expected.
[2806.82 --> 2812.30]  But I take a moment to just be like, OK, deal with my own emotions and knee jerk reaction
[2812.30 --> 2817.78]  and then and then get back to it and be like, OK, let me try to figure out how to approach
[2817.78 --> 2818.34]  this.
[2818.52 --> 2822.66]  And sometimes I'll even have my responses vetted by someone else.
[2822.88 --> 2826.16]  So I'll be like, hey, I wrote this post, this thing response.
[2826.16 --> 2828.62]  Can you read it over and see if it makes sense?
[2828.78 --> 2835.44]  Because like, I don't know, because sometimes your ego can come through like, hey, this is
[2835.44 --> 2836.22]  hard for you.
[2836.34 --> 2837.04]  But guess what?
[2837.06 --> 2838.20]  It's hard for me, too.
[2839.26 --> 2841.30]  Which like I've actually written before.
[2842.32 --> 2847.00]  Yeah, like I took a lot of time on this specific thing and I was just like, I'm annoyed because
[2847.00 --> 2847.74]  it's not just you.
[2847.80 --> 2848.42]  It's also me.
[2848.90 --> 2853.28]  But yeah, like taking a step back, taking a breather and then responding and also knowing
[2853.28 --> 2857.24]  that oftentimes in conflict, it's like not about you.
[2857.46 --> 2861.04]  Try to focus on the issue at hand, which is very hard.
[2861.14 --> 2861.92]  That separation.
[2862.28 --> 2864.26]  Yeah, that takes practice for sure.
[2864.86 --> 2866.16]  Yeah, that's very insightful.
[2866.74 --> 2867.28]  Thank you.
[2867.78 --> 2869.56]  I'll say one more tip while we're talking about communication.
[2869.56 --> 2878.08]  This is specifically around written communication is there's nothing wrong with emulation until
[2878.08 --> 2879.22]  you can find your own voice.
[2879.22 --> 2884.30]  And so if you feel like you are bad or maybe you are bad and so you appropriately feel like
[2884.30 --> 2889.68]  you are bad at writing down your thoughts and having somebody else read them and interpret
[2889.68 --> 2892.84]  them the way that you wanted them to and have the desired output.
[2893.06 --> 2893.24]  Right.
[2893.42 --> 2897.30]  If you are bad at that or you wish you could be better, there's nothing wrong with just
[2897.30 --> 2898.86]  finding people who are good at that.
[2899.52 --> 2900.58]  And it's very easy.
[2900.58 --> 2904.34]  Like if you read, you will find people who you read and you're like, I like their writing.
[2904.46 --> 2905.72]  I like to read this writing.
[2905.72 --> 2907.92]  And you just emulate them.
[2908.42 --> 2909.62]  You know, don't plagiarize, obviously.
[2910.30 --> 2915.22]  But think about what it is about the way that this person writes that is compelling or
[2915.22 --> 2916.58]  effective in your eyes.
[2917.04 --> 2921.74]  And then you just start to adopt those patterns and principles in your own writing.
[2922.22 --> 2925.16]  And eventually you will find your own voice through that.
[2925.26 --> 2930.14]  Like you can work your way until you get the skills up that you will then shed those and
[2930.14 --> 2931.06]  find your own voice.
[2931.06 --> 2936.68]  But in the meantime, there's nothing wrong with finding good examples and emulating them.
[2936.84 --> 2941.80]  So that's one tactic for improving your communication pretty quickly through simple
[2941.80 --> 2942.22]  emulation.
[2942.42 --> 2943.80]  I totally agree with that.
[2944.22 --> 2945.24]  Yeah, that's pretty cool.
[2945.68 --> 2947.10]  I had one more recommendation.
[2947.80 --> 2951.92]  So I was blanking on the topic, but there's a book that I've been like kind of referencing
[2951.92 --> 2954.60]  from time to time called Thank You for Arguing.
[2955.00 --> 2957.44]  And it's about the art of persuasion.
[2957.44 --> 2959.78]  So it's not about like winning an argument.
[2960.08 --> 2965.44]  It's just how to navigate an argument, because a lot of the times that's hard.
[2966.02 --> 2971.20]  And a lot of the times it's just like anger versus anger rather than like the actual point
[2971.20 --> 2972.24]  that you're trying to make.
[2972.60 --> 2978.32]  And I think it's a really cool book just to analyze like how exactly arguments are like
[2978.32 --> 2980.28]  effective arguments can be had.
[2980.28 --> 2985.68]  And I reference it again, because I'm just like, oh, sometimes when I have an argument
[2985.68 --> 2989.58]  and it did not end well, I'll be like, what did I do?
[2990.24 --> 2993.58]  And then I'll look at this book and I'll be like, oh, OK, maybe I could have done this
[2993.58 --> 2994.32]  better or that.
[2994.40 --> 2996.04]  It's kind of just a reference point.
[2996.10 --> 2997.50]  You don't have to read it cover to cover.
[2997.50 --> 3003.90]  It's kind of like every chapter has morsels of information, but it's really useful to
[3003.90 --> 3011.08]  understand the art of a good argument, which also bleeds into like general outside of programming,
[3011.34 --> 3013.68]  because I think this is just a general criticism.
[3013.68 --> 3020.54]  But I think as a society, we just have the have have basically gone backwards in terms of
[3020.54 --> 3021.50]  the ability to argue.
[3021.50 --> 3023.46]  We just are unable to do that.
[3023.46 --> 3025.54]  We automatically shut down.
[3025.66 --> 3030.14]  And I think that is horrible because like then there's no discourse.
[3030.30 --> 3033.88]  We can't like the moment someone disagrees with you, the conversation is over.
[3034.06 --> 3038.70]  And the fact is that we can disagree and be OK with each other.
[3038.82 --> 3042.12]  If you disagree, you're on this other side of this, whatever the topic is.
[3042.12 --> 3044.18]  And we're very divided because of that.
[3044.20 --> 3046.14]  And it's like we can disagree and still get along.
[3046.22 --> 3047.58]  And that's part of life.
[3047.58 --> 3051.16]  And a valuable part of life is engaged disagreement.
[3051.16 --> 3055.78]  I do have one more topic I want to get into in terms of the advice, specifically around
[3055.78 --> 3056.68]  the empathy side.
[3057.04 --> 3063.18]  Speaking of empathy, Suze, Divya talked about a great skill is empathy, aka caring about others
[3063.18 --> 3065.86]  and the user experience and like the person who's using your software.
[3066.24 --> 3067.50]  So what if you're really bad at that?
[3068.02 --> 3069.76]  Do you have any advice on ways that you can get?
[3069.80 --> 3072.12]  Because that's hard to improve, I think.
[3072.52 --> 3073.88]  But do you have any advice on that?
[3074.36 --> 3074.56]  Yeah.
[3074.74 --> 3078.64]  For me, the most powerful thing that helps people who are really struggling with it is you're
[3078.64 --> 3082.46]  never going to be able to get outside of your own experience or your head unless you actually
[3082.46 --> 3087.42]  go out and either observe people having the problems that you're having trouble empathizing
[3087.42 --> 3090.08]  with or just asking people questions about it.
[3090.20 --> 3090.40]  Right.
[3090.84 --> 3095.78]  And I've seen this a lot where, you know, I led an accessibility effort at a job once
[3095.78 --> 3100.04]  and I just couldn't get people to consider experiences outside of their own.
[3100.70 --> 3104.68]  Obviously, there's like a lot of work that is required in order to learn accessibility topics
[3104.68 --> 3105.42]  if you don't know them.
[3105.42 --> 3108.00]  So obviously, there's like pushback because of that reason, too.
[3108.36 --> 3112.72]  And what we ended up doing was we brought someone in to the company and they used our
[3112.72 --> 3116.16]  website and they used the tools that they need to use the website.
[3116.60 --> 3119.52]  And that was the fundamental turning point for people.
[3119.82 --> 3121.04]  They just needed to see it.
[3121.18 --> 3124.82]  They needed to feel someone using something that they made personally.
[3124.96 --> 3130.24]  So if your code is the piece of code that's responsible for a bad experience or something
[3130.24 --> 3136.64]  and you visually, viscerally, cringeworthy, you know, feel it, having people cringe like
[3136.64 --> 3141.68]  that, that's when you realize, you know, unfortunately, sometimes people only empathize once they've
[3141.68 --> 3144.88]  been through it or once they've had a relative or someone they care about that goes through
[3144.88 --> 3145.04]  it.
[3145.30 --> 3146.74]  That's just not good enough.
[3146.88 --> 3148.34]  It's not something you can rely on.
[3148.34 --> 3151.48]  And it's kind of not really that nice.
[3151.60 --> 3152.10]  You know what I mean?
[3152.14 --> 3154.80]  To like wait until it actually affects you.
[3155.18 --> 3159.46]  You really have to make that effort to go out there and watch people struggle to use the
[3159.46 --> 3165.42]  things or watch a junior or like be thrown in the deep end and have someone explain something
[3165.42 --> 3166.52]  really badly to you.
[3166.62 --> 3170.44]  And you feel that frustration, which makes you want to be better at explaining things to
[3170.44 --> 3173.60]  junior developers or people who are new to a topic that you're really good at.
[3173.60 --> 3178.90]  You really should try and at least try to be a little bit uncomfortable at times in order
[3178.90 --> 3182.10]  to really be able to bridge that gap that you're struggling with.
[3182.72 --> 3183.36]  I love that.
[3183.72 --> 3184.22]  Yeah.
[3184.26 --> 3189.02]  Within the context of developers, I cannot recommend highly enough watching somebody who
[3189.02 --> 3192.44]  has never used your code, use your code, especially on the web.
[3192.52 --> 3193.50]  It's really easy, right?
[3193.56 --> 3201.34]  Like go to a freaking store or like cafe or something and your laptop, have your website open and say,
[3201.34 --> 3204.90]  hey, you know, can I ask you just go to a random person?
[3205.02 --> 3207.06]  Can I ask you to play around with this a little bit?
[3207.66 --> 3212.48]  Like it is striking how many people will say yes and you watch them and your mind will be
[3212.48 --> 3216.44]  blown because people do not use your tools the way that you use your tools.
[3216.56 --> 3220.02]  And it may be more difficult if you're using something that's less consumer focused or
[3220.02 --> 3222.98]  whatever, but sit in on a design user study or whatever.
[3223.18 --> 3226.04]  People do not see your software the same way you do.
[3226.04 --> 3231.36]  And it will just it's incredibly humbling because no matter how good of a job you've
[3231.36 --> 3234.74]  done, they will get confused about something, especially if you haven't been already doing
[3234.74 --> 3235.66]  this a lot.
[3236.16 --> 3240.84]  And a lot of times they'll get confused about everything and they will have no idea what's
[3240.84 --> 3241.96]  going on with your software.
[3242.32 --> 3247.50]  And it's a mind opening and stretching experience and very painful, but worth doing.
[3248.18 --> 3248.76]  Love that advice.
[3248.84 --> 3252.26]  Well, let's turn that advice inward a little bit as we wrap up.
[3252.26 --> 3258.70]  We have no idea what you all think of our podcasts unless we listen to you, listen to
[3258.70 --> 3258.88]  them.
[3258.96 --> 3259.66]  No, we can't do that.
[3259.76 --> 3262.12]  But we can do is solicit your feedback.
[3262.76 --> 3266.68]  Let us know what you think of our shows, specifically the show.
[3266.82 --> 3272.10]  Every show now on channel.com does have its own discussion page where you can talk to the
[3272.10 --> 3272.56]  panelists.
[3272.90 --> 3274.42]  You can share your strengths and weaknesses.
[3274.88 --> 3276.64]  You can share the show's strengths and weaknesses.
[3276.78 --> 3277.54]  Tell us what we're doing well.
[3277.90 --> 3279.42]  Tell us what we really could improve at.
[3279.48 --> 3280.34]  We'd love to hear from you.
[3280.34 --> 3284.88]  We want this to be a show for and by the community of JavaScript and web people.
[3285.42 --> 3286.60]  And so that's what we're striving for.
[3286.70 --> 3289.08]  And you can help us by letting us know what you think.
[3289.58 --> 3291.14]  So that's our show today.
[3291.70 --> 3294.70]  Divya, KBall, any final words before we call it a show?
[3295.34 --> 3299.42]  Know yourself because, you know, we've spent a bunch of introspection here, but I think
[3299.42 --> 3302.56]  it is really important to pay attention to this in yourself.
[3303.02 --> 3306.78]  And I think one thing we didn't really talk about here, but it kind of came up tangentially
[3306.78 --> 3312.02]  is know what gets you excited because whether or not something is your strength or your weakness,
[3312.02 --> 3316.94]  like you're going to be able to learn and power through and do whatever by getting excited
[3316.94 --> 3317.44]  about it.
[3317.58 --> 3320.20]  You know, Sue's talked about, you know, being really excited about learning.
[3320.28 --> 3321.02]  I have the same thing.
[3321.08 --> 3326.78]  Like I can do something that is the most boring, detail oriented, right in my weaknesses, all
[3326.78 --> 3327.40]  these other things.
[3327.52 --> 3332.00]  If it's new to me and I'm learning something to it, it'll be fun because that's what gets
[3332.00 --> 3332.58]  me excited.
[3333.02 --> 3334.20]  That's not what gets everybody excited.
[3334.36 --> 3340.32]  Know yourself, know how you react to these things and use that to help guide your investment
[3340.32 --> 3341.36]  in your strengths and weaknesses.
[3342.04 --> 3342.70]  Yeah, definitely.
[3343.16 --> 3345.72]  I completely agree 100%.
[3345.72 --> 3350.00]  Just like I think enthusiasm goes a long way.
[3350.00 --> 3354.74]  And so something that started as your weakness, if you're very enthusiastic, it can turn into
[3354.74 --> 3355.24]  a strength.
[3355.50 --> 3356.84]  Like if you power through.
[3357.54 --> 3357.72]  Love it.
[3357.80 --> 3358.16]  Love it.
[3358.24 --> 3358.82]  Know yourself.
[3358.98 --> 3359.56]  Very good.
[3359.68 --> 3360.68]  Well, thanks you too.
[3360.86 --> 3363.48]  Thanks to Sue's who is now on her way to the airport.
[3364.08 --> 3365.56]  Thanks for you for listening.
[3365.76 --> 3366.68]  That's our show this week.
[3366.74 --> 3367.76]  We'll see y'all next time.
[3369.54 --> 3370.10]  All right.
[3370.12 --> 3371.98]  Thank you for tuning in to JS Party this week.
[3371.98 --> 3375.06]  Tune in live on Thursdays at 1 p.m.
[3375.10 --> 3378.14]  U.S. Eastern at changelaw.com slash live.
[3378.14 --> 3381.14]  Join the community and Slack with us in real time during the shows.
[3381.42 --> 3382.90]  Head to changelaw.com slash community.
[3383.56 --> 3384.24]  And do us a favor.
[3384.38 --> 3386.76]  Share this show with a friend or just have a podcast.
[3387.26 --> 3388.82]  Go into Overcast and favorite it.
[3389.24 --> 3391.56]  And thank you to Fastly, our bandwidth partner.
[3391.94 --> 3393.42]  Head to fastly.com to learn more.
[3393.82 --> 3396.44]  And we move fast to fix things around here at changelaw because of Rollbar.
[3396.80 --> 3398.38]  Check them out at rollbar.com.
[3398.70 --> 3400.64]  We're hosted on Leno cloud servers.
[3401.04 --> 3402.64]  Head to leno.com slash changelaw.
[3402.70 --> 3404.10]  Check them out and support this show.
[3404.52 --> 3406.54]  Our music is produced by Breakmaster Cylinder.
[3406.54 --> 3410.00]  And you can find more shows just like this at changelaw.com.
[3410.16 --> 3411.10]  Thanks for tuning in.
[3411.36 --> 3412.14]  We'll see you next week.
