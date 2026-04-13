[0.00 --> 13.92]  Welcome back everyone, this is the Change Log and I'm your host Adam Stachowiak.
[14.06 --> 16.18]  This is episode 136.
[16.82 --> 21.28]  Jared and I had a great conversation with Hong Lee from Fuse and Passenger fame.
[21.58 --> 24.86]  We talked about Ruby Raptor and all sorts of fun stuff.
[25.10 --> 29.60]  Marketing open source, getting the crowd excited about your next version again.
[29.60 --> 31.34]  And much, much more.
[31.52 --> 36.46]  We had some awesome sponsors for this show, Ninefold, TopTile, and DaysWork.
[37.04 --> 40.12]  We'll tell you a bit more about TopTile and DaysWork later in the show.
[40.24 --> 46.42]  But our friends at Ninefold operate a high performance platform for deploying and hosting Ruby on Rails apps.
[46.94 --> 53.26]  The platform is entirely built on Ninefold's own infrastructure with service in the U.S. and Asia Pacific.
[53.74 --> 58.38]  And with Ninefold, you don't need to sacrifice easy app deployment and updates for performance.
[58.38 --> 73.66]  You get quantifiably superior performance compared to the competition with more economical scaling into a great support, zero downtime deployment, SSL, Redis, load balancers, and firewalls all for free straight out of the box.
[74.00 --> 76.00]  Get started today with Ninefold's free tier.
[76.00 --> 84.18]  You get superior performance and easy app deployment on a 1.5 gig app server in the U.S. for free month on month.
[84.54 --> 88.28]  And all you got to do is go to Ninefold.com slash the changelog to learn more.
[88.52 --> 90.04]  And now on to the show.
[90.04 --> 92.78]  What's up, everybody?
[92.92 --> 93.48]  We are back.
[93.60 --> 94.86]  This is Jared with the changelog.
[94.96 --> 96.10]  I'm here with Adam.
[96.64 --> 97.02]  Hey, Adam.
[97.10 --> 97.36]  Say hi.
[97.98 --> 98.62]  Yo, yo, yo.
[98.80 --> 101.76]  And we're here with Hong Lee from Fusion.
[102.78 --> 103.72]  Hong Lee, great to have you.
[104.58 --> 104.96]  Yes.
[105.22 --> 105.80]  Thank you, guys.
[105.96 --> 107.42]  Happy 2015 to everybody.
[108.10 --> 110.46]  Yeah, it's our first show of the new year.
[110.52 --> 111.90]  We took a couple weeks off for Christmas.
[111.90 --> 113.40]  And now we're back.
[113.48 --> 114.48]  We got Hong Lee on.
[114.92 --> 119.58]  Talking about Passenger and specifically Raptor and some other fun stuff.
[120.30 --> 120.52]  Yeah.
[121.02 --> 123.36]  Big Passenger user myself, Hong Lee.
[123.46 --> 126.52]  So thank you very much for your open source throughout the years.
[127.28 --> 130.08]  For those of you who don't know, Passenger is a Ruby app server.
[130.92 --> 133.46]  And first launched, was it back in 2008?
[134.74 --> 135.68]  Yes, it is.
[135.68 --> 142.10]  And set out with the goal to make Ruby and Rails app deployments easier.
[142.30 --> 143.60]  It used to be a huge pain.
[144.76 --> 146.68]  You know, really fun and easy to write apps.
[146.76 --> 150.76]  And then really, really hard and kind of disgusting to deploy them back in the day.
[150.94 --> 156.84]  So Hong Lee, along with his partner Ning, set out to fix that problem.
[156.96 --> 161.24]  And they've been working on and shipping Fusion Passenger ever since.
[161.30 --> 162.42]  You want to give us a bit of a backstory?
[163.74 --> 164.18]  Yes.
[164.18 --> 168.78]  As you said, Passenger was made to solve the Ruby deployment problem.
[168.86 --> 170.22]  Because it just sucked back then.
[170.48 --> 173.44]  If something went wrong, you often didn't know what went wrong.
[173.52 --> 175.12]  It's very hard to diagnose the problem.
[175.66 --> 179.26]  And you had to do, you just had to perform a lot of steps.
[179.74 --> 185.68]  Like what we saw back then was that a lot of people came to Rails with the mindset of PHP.
[186.16 --> 190.44]  In PHP, you can deploy an app just by dropping your PHP file somewhere.
[190.54 --> 191.60]  And then it just works.
[191.60 --> 196.54]  But back then with Ruby, you had to set up these AppSurfer clusters.
[196.54 --> 201.32]  And then you had these Sockets and you had to connect them to the web server and lots of other stuff.
[201.64 --> 205.06]  And then we just thought, yeah, there's something wrong here.
[205.30 --> 208.04]  It should be a lot simpler, maybe like PHP.
[208.34 --> 211.48]  And it is with that vision that we made Passenger.
[211.48 --> 222.12]  So we went for the PHP style upload and go model and tried to implement an Apache module that sort of does something similar, but then for Ruby.
[222.44 --> 224.30]  And that's how Passenger started out.
[224.66 --> 232.52]  The philosophy behind Passenger was to make deployment as easy as possible, to require as least maintenance as possible.
[232.52 --> 237.22]  So if the AppSurfer can do something for you, then it should.
[237.22 --> 244.12]  It should bother the human as less as possible so that the human can focus on the stuff that is really necessary.
[245.52 --> 247.88]  And this is the philosophy behind it.
[247.88 --> 258.72]  And it also tries very hard to solve problems, keeps you out of the dark, to give good diagnosis of the problems instead of just swallowing all the error messages.
[259.18 --> 263.44]  That's why we have that error message base from Passenger.
[263.98 --> 266.62]  And this is kind of where it began.
[266.62 --> 273.86]  We just saw back at the time a lot of people were complaining about how hard Ruby deployment was.
[274.00 --> 279.90]  And then we saw an opportunity there to change things because we saw like Zed Show had its mongrel.
[280.26 --> 285.24]  And then Thin came and then a few others came.
[285.40 --> 290.18]  But they all followed the same model of having a simple AppSurfer that listens to NoSocket.
[290.34 --> 292.60]  And then you had to connect all of them to the web server.
[292.60 --> 296.32]  And lots of people just got confused by that very same model.
[296.62 --> 301.62]  And we were the first one to come up with a completely different usage model.
[302.74 --> 304.64]  And actually, even right now, we still are.
[304.76 --> 307.40]  Because these days, you have Puma and Unicorn.
[307.82 --> 311.92]  But what they fundamentally do is still following that old model.
[312.06 --> 315.32]  And we are the only one that tries to really integrate into the web server.
[315.88 --> 322.00]  And through that way, eliminating a lot of the unnecessary setups, so to say.
[322.00 --> 327.66]  Yeah, just going back to 2008 when you guys first started kicking off.
[327.96 --> 333.02]  I think, didn't you even call it Mod Rails way back in the day before it was called Passenger?
[333.12 --> 333.86]  Am I misremembering?
[334.66 --> 335.48]  Yes, we did.
[335.48 --> 339.00]  So you were really trying to position it as the PHP.
[340.00 --> 345.94]  That same experience of, I can just drop my files into this public folder.
[346.62 --> 349.12]  And Apache is going to process that and serve it.
[349.24 --> 352.54]  And so, because you had ModPHP, you guys decided ModRails.
[353.54 --> 355.28]  Use that really as a launching point.
[355.28 --> 360.14]  At some point, I guess that name didn't scale well.
[360.30 --> 363.52]  We're going to talk a little bit about marketing and positioning and stuff.
[363.92 --> 366.72]  When did you guys decide ModRails was not the best name and why?
[368.32 --> 371.28]  Okay, so back then, the primary...
[372.12 --> 376.80]  Well, let's say the primary way that people see Ruby is through Rails.
[377.26 --> 379.40]  Rails is what made Ruby big back then.
[379.40 --> 382.56]  So we wanted to associate with Rails as much as possible.
[382.88 --> 386.44]  And maybe even completely focus on Rails only.
[386.68 --> 390.60]  Because back then, you had these alternative frameworks, but they weren't really that popular.
[391.34 --> 394.44]  But then, after a short while, Rack came.
[394.86 --> 405.00]  And that's an interface that allows multiple web frameworks to talk the same language, so to say, to the app server.
[405.00 --> 412.82]  So that as an app server author, you only have to implement Rack and then you can support multiple web frameworks, which is a very good thing.
[413.26 --> 417.00]  And we quickly saw that there is a...
[418.00 --> 423.00]  There's a lot of demand from the community to not support only Rails, but also other things.
[423.38 --> 428.30]  We also saw, hey, Rails itself is also going to jump on the Rack bandwagon someday.
[428.78 --> 430.62]  So we should, too.
[430.62 --> 434.34]  And then we came up with ModRails 1.2.
[435.32 --> 438.62]  And then we also decided, hey, we actually need a different name.
[438.80 --> 442.12]  We can call it ModRack, but let's face it.
[442.20 --> 444.58]  Even back then, Rack wasn't that popular.
[444.74 --> 445.82]  It has a lot of promise.
[446.04 --> 449.46]  But calling it ModRack is just a little bit of a lame name.
[449.52 --> 450.96]  It doesn't really sound good.
[451.16 --> 454.38]  And marketing-wise, it's just not a good name.
[454.64 --> 456.56]  And then we needed a new name.
[456.56 --> 461.24]  So then we thought, okay, how about we call it Passenger?
[461.60 --> 466.00]  Because it's in the same category as Rails.
[466.42 --> 471.90]  So imagine that you are a passenger inside a train on top of some Rails.
[472.30 --> 478.42]  All you have to do is to sit back, relax, and everything is taken care of for you.
[478.50 --> 481.52]  You arrive at a destination without having doing much.
[482.04 --> 483.82]  And that's the philosophy behind the name.
[483.82 --> 488.44]  I never connected the whole passenger onto a train rails.
[488.62 --> 491.06]  I never connected that analogy there.
[491.68 --> 497.88]  Yeah, unfortunately, I heard this recently from other people, too, that they didn't connect names.
[498.00 --> 500.40]  So maybe we should make this clearer.
[501.98 --> 503.18]  I like it now that I hear it.
[503.38 --> 504.84]  But with the name, I just didn't.
[504.92 --> 506.26]  I was like, well, Passenger, that sounds cool.
[506.26 --> 512.46]  Well, it definitely scales better because over the years, you guys moved on to add, first of all, you added Nginx support.
[512.76 --> 514.92]  So you could deploy on Apache or Nginx.
[515.24 --> 518.08]  And then later on, you added support for not just Ruby apps, right?
[518.14 --> 520.52]  So now you can deploy Python, Node.js.
[521.18 --> 524.60]  Is it completely polyglot or is it specific ecosystems?
[525.36 --> 526.88]  It is specific ecosystems.
[527.22 --> 530.86]  We didn't want to fragment too much.
[530.86 --> 535.28]  Like, if we support everything, then we just don't have any focus.
[535.72 --> 540.90]  And we want to focus on a few languages that are popular, but to give them really, really good experience.
[541.14 --> 543.10]  And we just can't do that if it supports everything.
[544.72 --> 551.76]  And then you guys took opportunity to build not just an open source project, but you're actually building a business around Passenger.
[551.76 --> 553.70]  Or is it just one of your many products?
[554.88 --> 557.90]  Passenger is right now our primary product.
[558.48 --> 565.14]  Because as Fusion, we started also in 2008 when Passenger was launched.
[565.60 --> 571.10]  We saw Passenger as a way to start a company to gain recognition in the company.
[571.42 --> 573.76]  Back then, our business model was to do consultancy.
[574.56 --> 581.66]  And we saw Passenger as a way to advertise ourselves, to advertise our consulting services.
[581.76 --> 587.76]  People would use Passenger, see that it's good, and then they would come to TrustFusion and come to us for consultancy.
[588.72 --> 590.56]  And this worked for a while.
[591.00 --> 596.34]  But unfortunately, it is not a really good scalable business model.
[597.24 --> 601.14]  So the problem is we could not monetize Passenger directly.
[601.32 --> 605.56]  We spent, even in the first version, months of work into Passenger.
[606.38 --> 610.14]  And we had to earn all that money back through consultancy.
[610.74 --> 613.14]  And luckily, back then, we were still students.
[613.30 --> 618.00]  We were actually in the second year of our computer science study when we started Fusion.
[619.02 --> 621.16]  And then we had to do all this consultancy.
[621.74 --> 625.08]  But the problem with consultancy is we didn't get to study a lot.
[625.14 --> 627.78]  You cannot run a company and study at the same time.
[627.78 --> 632.90]  So as a result of Fusion, we actually had a study delay of about five years.
[632.90 --> 633.50]  Oh, wow.
[633.50 --> 637.52]  So our bachelor is supposed to take three years.
[637.62 --> 642.98]  But then we graduated after about seven years, starting from when we started studying.
[643.54 --> 645.12]  But it was all worth it.
[645.48 --> 647.56]  Having said that, it still didn't scale.
[647.56 --> 656.48]  And so for years, we had to worry about our next client, about getting the next project to generate income.
[656.94 --> 666.44]  So for a long time, we made a lot less money than we should have compared to when we were employed by another company as developers.
[666.44 --> 669.96]  And we lived in our student dorms.
[670.04 --> 672.66]  And we also operated Fusion from home.
[672.82 --> 675.52]  We didn't have an office for a long time.
[676.30 --> 683.88]  Things actually became a lot better after we decided to do away the consultancy business model and started selling Passenger Enterprise.
[683.88 --> 689.10]  So you moved to an open source plus an enterprise, a closed source enterprise?
[689.88 --> 691.72]  Or is it just like a license?
[691.92 --> 693.68]  How do you guys actually manage the upgrade?
[694.96 --> 697.22]  Well, Passenger itself is open source.
[697.36 --> 698.06]  And that is the core.
[698.42 --> 700.90]  Most features are in the open source version.
[701.30 --> 712.64]  And on top of that, we have Passenger Enterprise, which is a paid version with extra features such as rolling restarts, multithreading, live debugging, etc.
[712.64 --> 718.92]  And we just charge a license fee per server per year or per server per month.
[719.92 --> 720.84]  That makes sense.
[721.44 --> 721.96]  Yes.
[722.10 --> 726.22]  And with that model, we were a lot more successful than consultancy or support.
[726.48 --> 730.28]  For a while, we have also tried to sell support Red Hat style.
[730.28 --> 734.74]  A lot of people say, hey, if you are open source and you want to make money, try selling support.
[734.94 --> 738.96]  We tried doing that, but it didn't work at all because Passenger is too good.
[739.72 --> 740.94]  Passenger is too good.
[740.94 --> 742.78]  That is seriously a problem.
[743.12 --> 744.10]  Passenger is too good.
[744.38 --> 745.60]  Two people have problems.
[745.72 --> 746.96]  So nobody needed support.
[747.16 --> 749.14]  We couldn't make any money from that.
[749.48 --> 750.64]  You just need some more bugs.
[750.68 --> 751.26]  That's all you need.
[751.34 --> 753.54]  And then you got built-in support infrastructure.
[753.76 --> 755.90]  Well, be bad coders or something like that.
[756.04 --> 756.30]  Yeah.
[756.44 --> 758.18]  We actually made jokes about that.
[758.26 --> 760.14]  But at the end of the day, we didn't want to do that.
[760.22 --> 761.80]  It hurts our pride as developers.
[761.80 --> 763.68]  And I'm only joking.
[763.78 --> 764.80]  Of course you shouldn't do that.
[765.10 --> 765.14]  Yeah.
[765.24 --> 765.82]  Of course.
[765.96 --> 773.82]  And as a longtime user, I can definitely be a testimonial to not needing support because honestly, you set the thing up and you get it running.
[773.82 --> 780.02]  Unless you have extreme usage or strange things that you're doing, it pretty much just works.
[780.34 --> 784.52]  So good job on writing stable and well-documented software.
[784.78 --> 785.58]  It's rare.
[785.66 --> 786.14]  It's rare.
[786.26 --> 787.34]  It's rare these days.
[787.34 --> 794.66]  This path, though, Jared, that they're on, we've heard this story before where you've got an open-source version.
[794.82 --> 797.56]  You've got an enterprise version of it or a pro version of it.
[798.36 --> 809.44]  And their story, too, Hong Lee, your story for your commitment to Passenger, from a monetary standpoint, as a developer, you could have taken a position at a company and said, well, forget Passenger.
[809.56 --> 812.88]  Or we'll just kind of figure that out along the way and made more money.
[812.88 --> 820.86]  When you guys were making the decisions to kind of make the company and take the long haul, you stretched your education, you stretched your financial dollars to a degree.
[821.34 --> 829.16]  What were the conversations like between you two talking about Passenger and talking about the enterprise edition and talking about the direction the company could take?
[829.46 --> 838.34]  How did you all come up with the decision to sort of stretch your education timeline and even stretch your dollars and not take the quick money path?
[838.50 --> 842.04]  How did you talk about that sacrifice, I guess, for the open-source community?
[842.04 --> 846.62]  It is a very difficult one. It has not been an easy choice.
[847.56 --> 853.22]  The thing is, Ning and I, we have this dream of making our own company and become big with it.
[853.94 --> 859.68]  If you work for someone else, there's not a lot of freedom you have.
[860.30 --> 864.16]  If you don't have your own company, it is a lot safer, but it limits your freedom.
[864.38 --> 868.92]  And it is this freedom that appeals to us. It is also the potential that appeals to us.
[868.92 --> 872.20]  And furthermore, back then, we were still young.
[872.96 --> 879.60]  And we thought, hey, starting this company is something that we can do without a lot of risk when we are young.
[880.02 --> 886.22]  When we are older and we are married, we have children, we have wives, we have responsibility to take care of them.
[886.44 --> 888.16]  And we can't just take all these risks.
[888.40 --> 890.58]  But when we are students, what's the worst that can happen?
[890.58 --> 899.08]  Maybe we go bankrupt and that sucks too, but it wouldn't be as bad as when you go bankrupt while having a family.
[899.42 --> 902.10]  So if we are to do that, we have to do it now.
[904.64 --> 905.34]  That's it.
[906.64 --> 908.20]  That's the most important thing.
[908.46 --> 910.02]  Are you guys married and have kids now?
[910.56 --> 910.80]  No.
[911.06 --> 914.02]  No, I have a girlfriend, but Ning is still single.
[914.02 --> 919.10]  So I suppose for a while, it's not...
[919.10 --> 922.90]  Well, we are doing a lot better now that we have launched Passenger Enterprise.
[924.18 --> 925.12]  Well, that's good to hear.
[925.22 --> 928.96]  So let's talk about Raptor a little bit, because this is pretty interesting.
[929.08 --> 932.54]  In fact, this was the reason why you came back across our radar.
[933.34 --> 938.30]  As I said, long-time user, but you kind of settle in with a tool and you just don't think about it very much.
[938.30 --> 941.16]  But over the years, Passenger has slowly gotten better.
[941.40 --> 942.10]  I say slowly.
[942.36 --> 943.20]  It's probably moved fast.
[944.02 --> 944.96]  But it's gotten better and better.
[945.06 --> 946.26]  You've gotten four versions out.
[946.36 --> 948.22]  As I said, you added support for Nginx.
[948.32 --> 949.50]  You added these different things.
[949.56 --> 952.52]  I'm sure it got faster, better error reporting, and so on.
[953.40 --> 959.58]  But I think it's safe to say that in the community's eyes, it got a little boring, I guess.
[960.06 --> 963.48]  At least in your guys' eyes, the way you thought it was being received.
[964.18 --> 967.08]  Especially in the Ruby community, we're kind of all about the new hotness.
[967.08 --> 968.44]  And developers in general.
[969.04 --> 971.62]  I think it's amplified in the Ruby and JavaScript communities.
[971.62 --> 975.12]  And new app servers were coming out.
[975.76 --> 978.32]  I think it was Puma, perhaps, the most recent.
[979.00 --> 980.08]  Slightly different models.
[980.20 --> 983.66]  So you had multi-processed, then you had some multi-threaded models.
[984.76 --> 986.14]  Benchmarks would be released.
[987.00 --> 988.70]  Passenger may or may not fare very well.
[988.70 --> 998.26]  And then in November of this year, this news starts coming out about a brand new web, Ruby app server named Raptor.
[998.50 --> 1000.86]  Which was just blowing away all benchmarks.
[1001.92 --> 1003.98]  A few prominent bloggers wrote about it.
[1004.06 --> 1006.62]  Ruby Inside and Peter Cooper, friend of the show.
[1006.84 --> 1011.46]  Who I was a bit curious when I saw his post because he kind of has slowed down.
[1011.56 --> 1014.54]  Ruby Inside is not exactly something he's writing on a regular basis.
[1014.66 --> 1015.98]  I think he's doing his newsletters now.
[1015.98 --> 1022.44]  And out came this Ruby Inside post about how he got the inside tip on Raptor and got to use it in beta.
[1023.10 --> 1028.58]  And could confirm these benchmarks where it's outperforming all the usual suspects.
[1028.94 --> 1032.20]  Unicorn Puma, Torquebox, by up to 4x.
[1033.22 --> 1034.88]  Somebody else, I think, blogged about it.
[1034.90 --> 1036.08]  Fabio Akita, perhaps.
[1036.88 --> 1037.76]  Wrote about it.
[1037.82 --> 1041.28]  And all this buzz started happening about this new app server named Raptor.
[1041.90 --> 1043.72]  Everybody wanted to know, where is this thing?
[1043.78 --> 1044.62]  Who's writing it?
[1044.62 --> 1045.80]  When's it coming out?
[1046.58 --> 1053.20]  A little less than a month later, I think it was like mid-November, we find out Raptor is Fusion Passenger 5.
[1053.90 --> 1056.48]  Where did this marketing idea come from?
[1058.88 --> 1064.42]  Okay, so it is, as you said, over the years we have improved Passenger a lot.
[1064.42 --> 1067.92]  But then it got a little bit boring in the community's eyes.
[1068.70 --> 1072.12]  So this is also related to Passenger Enterprise a little.
[1072.24 --> 1080.04]  Because after we launched Passenger Enterprise two years ago, the development of the open source version has increased a lot.
[1080.88 --> 1083.72]  So Passenger Enterprise came right before Passenger 4.
[1084.02 --> 1089.04]  And in Passenger 4, there were just these tremendous improvements in the open source version.
[1089.04 --> 1092.54]  The Enterprise version funds the development of the open source version.
[1093.76 --> 1101.18]  And during consultancy time, we just couldn't spend a lot of time on development of Passenger because we had to do consultancy.
[1101.18 --> 1108.60]  But despite all these improvements, it is, as you say, it got a little bit boring in the community's eyes.
[1108.98 --> 1112.92]  We just saw that, okay, we can come up with improvements.
[1113.46 --> 1114.58]  And these are facts.
[1115.22 --> 1116.08]  And that's okay.
[1116.22 --> 1119.00]  But the perception is also important.
[1119.00 --> 1133.12]  Even if you really become better than Puma and Unicorn and certain features, and which I believe we actually have, then if people don't perceive it that way, it still doesn't help you.
[1133.66 --> 1138.78]  So then we had to come up with an idea to change people's perception.
[1139.58 --> 1143.90]  And if we were to try that, then there are a few options we can choose from.
[1143.90 --> 1153.86]  We can either spend a lot of time blogging about things, trying to talk to people, trying to spread the word, and we can advertise.
[1154.46 --> 1159.62]  But all of that takes a lot of time, a lot of resources, and then you still wouldn't reach a lot of people.
[1159.72 --> 1168.38]  Because after visiting some conferences, it has really sunk into me that a lot of people had kind of closed their mind from Passenger.
[1168.38 --> 1175.94]  No matter what good news we come from, no matter how we improve Passenger, a lot of people just didn't listen to Passenger news anymore.
[1176.04 --> 1179.44]  You can't reach them anymore, no matter the facts.
[1179.96 --> 1183.54]  And that made us a little bit sad.
[1183.82 --> 1187.04]  People were talking about Unicorn, and then we improved upon Unicorn.
[1187.24 --> 1189.04]  We saw, hey, this is the Unicorn feature.
[1189.18 --> 1190.18]  How do we improve it?
[1190.24 --> 1191.18]  Okay, we improved it.
[1191.26 --> 1197.62]  Hey, here's a new release with improved out-of-banned garbage collection or with even better rolling restart.
[1197.62 --> 1199.38]  And then a lot of people just wouldn't listen.
[1199.98 --> 1206.56]  So then we realized, okay, apparently a lot of people in the community would only listen to new things.
[1206.70 --> 1211.44]  And if we used the same Passenger, a lot of people would not listen by default.
[1211.90 --> 1213.58]  And we had to think out of the box.
[1214.22 --> 1216.22]  Like, advertising costs too much money.
[1217.04 --> 1218.64]  And we are a small team.
[1218.74 --> 1220.14]  We are with four people right now.
[1220.94 --> 1223.06]  We also have other projects going on.
[1223.06 --> 1227.86]  So we cannot spend too much time on talking to people and blogging.
[1227.96 --> 1228.84]  It just doesn't scale.
[1229.42 --> 1233.10]  So then we had to use unconventional marketing tactics.
[1234.24 --> 1241.58]  And then we thought, hey, wouldn't it be fun if we were to launch something that appears to be a new project?
[1241.82 --> 1246.08]  And then it kicks everything else out of the water, including ourselves.
[1246.08 --> 1252.30]  And then we'll just pretend like, hey, Fusion is totally defeated by these new guys.
[1252.64 --> 1255.10]  And then at the end of the day, hey, it's actually just us.
[1256.70 --> 1258.96]  So it was kind of...
[1258.96 --> 1259.48]  That's awesome.
[1260.32 --> 1261.36]  That's a good idea.
[1262.06 --> 1265.26]  Yeah, so it kind of started as a joke.
[1265.36 --> 1270.42]  But then we thought, hey, this might actually be a good idea.
[1270.72 --> 1272.10]  It would be a good laugh.
[1272.10 --> 1274.52]  And it would have a lot of effects.
[1274.78 --> 1277.18]  So then we went with this campaign.
[1277.82 --> 1279.20]  Yeah, and you guys went all out.
[1279.56 --> 1284.30]  So, you know, you had your own website, rubyraptor.org, a radically new Ruby web server.
[1284.94 --> 1291.14]  You tapped into your friend network and you got Peter and Fabio to play along, obviously,
[1291.50 --> 1295.30]  and kind of stir up buzz on your behalf.
[1295.44 --> 1297.50]  You had kind of this future announcement.
[1297.92 --> 1300.42]  I think it was like November 10th or whatever the date was.
[1300.42 --> 1300.78]  Yeah.
[1300.92 --> 1306.42]  That the team behind Raptor will be revealed and all this intrigue.
[1306.88 --> 1309.44]  And then you announced that it's Fusion Passenger 5.
[1309.54 --> 1310.48]  Tell us about the reception.
[1310.64 --> 1311.10]  Was it good?
[1311.20 --> 1311.90]  Was it bad?
[1312.26 --> 1313.10]  What were people thinking?
[1314.12 --> 1316.20]  There's a lot of good reception.
[1316.54 --> 1318.70]  There's naturally also some bad reception.
[1319.50 --> 1322.24]  A lot of people were surprised that it's us.
[1322.54 --> 1323.92]  Most of them didn't expect it.
[1324.18 --> 1327.48]  Some of it already figured out by looking up the DNS entry.
[1327.48 --> 1333.82]  But most of the people were just surprised that it is us.
[1334.04 --> 1337.66]  A lot of people were also pleasantly surprised because they were skeptical before.
[1337.94 --> 1339.68]  But then they found out, hey, it's Fusion.
[1340.40 --> 1345.00]  So then they thought, okay, these guys have some reputation.
[1345.38 --> 1346.64]  It's probably good stuff.
[1346.64 --> 1350.50]  And there were also some people who feel deceived.
[1352.18 --> 1355.92]  Some people compared it to switch and bait.
[1356.28 --> 1356.38]  Yeah.
[1357.70 --> 1364.04]  Well, I suppose I can also understand their feelings because we had hidden our identity.
[1364.48 --> 1367.10]  At the same time, we didn't really...
[1367.10 --> 1372.52]  Other than hiding our identity for about a month, we didn't really say anything that isn't true.
[1373.06 --> 1376.70]  Like all the things that we advertise about, they are real.
[1376.82 --> 1378.18]  The performance improvements are real.
[1378.24 --> 1379.32]  And they are even open source.
[1379.46 --> 1384.44]  So everything that we introduced in Raptor is in the open source version.
[1384.56 --> 1385.08]  It is public.
[1385.20 --> 1386.24]  The code is out there.
[1386.24 --> 1391.10]  But there are a lot of beta users for Passenger 5 now.
[1391.72 --> 1393.12]  And we got a lot of feedback.
[1393.34 --> 1395.08]  There are some bugs that need to be ironed out.
[1395.20 --> 1400.32]  And we hope to release Passenger 5 release candidate in about a month.
[1401.54 --> 1405.72]  First of all, I think that's pretty awesome that somebody actually went out and checked the DNS records
[1405.72 --> 1408.08]  and tried to figure out who this is.
[1408.12 --> 1410.96]  That showed how much interest you guys built.
[1410.96 --> 1417.20]  And I think quoting here from your blog post where you kind of do the reveal that it's just Passenger 5,
[1417.72 --> 1422.60]  is that this Raptor approach that you said over the past month has produced more subscribers to our newsletter
[1422.60 --> 1427.58]  than we have been able to accomplish over the past six years through the Fusion Passenger moniker.
[1428.84 --> 1433.54]  He says, you say, we still have a hard time comprehending this, but there's no denying the numbers.
[1434.16 --> 1436.60]  We, the community, seem to like shining new things.
[1437.60 --> 1439.22]  Yes, that is true.
[1439.22 --> 1445.46]  We were just a little bit sad that people would not judge us for our facts, for the things that we really are,
[1445.60 --> 1448.60]  but had to judge us by how shiny we are, so to say.
[1448.98 --> 1450.84]  And I'm not saying this is a bad thing.
[1450.90 --> 1452.68]  This is just how things are.
[1453.40 --> 1455.16]  And I can also understand it a little bit.
[1455.22 --> 1459.10]  As a developer myself, I am also attracted to shiny new things.
[1459.22 --> 1465.08]  But I just want people to treat us fairly and based on our merits.
[1465.08 --> 1473.80]  And as long as the people had this idea of Passenger from three years ago and thought that Passenger had stood still for a few years,
[1474.30 --> 1480.52]  there's no way to win from that except when we introduce something to completely change the perception,
[1480.78 --> 1483.94]  to let them refresh their perception, so to say.
[1483.94 --> 1488.28]  All right, let's pause the show for a minute, give a shout out to a sponsor.
[1488.38 --> 1489.54]  I want to talk to you about TopTile.
[1489.60 --> 1494.06]  We've been working with them for the last year, and it's just been a great time working with them.
[1494.44 --> 1500.12]  We thought it would make some sense to circle back and talk to some of our listeners who have applied with TopTile
[1500.12 --> 1508.30]  and have been accepted because only about 2% to 3% of the engineers who apply make it past their strict elite engineer process.
[1509.16 --> 1513.80]  And that person is Daniel Elzon, a longtime fan and listener of the ChangeLog.
[1514.16 --> 1517.62]  He is now living the dream as an elite engineer at TopTile.
[1517.62 --> 1525.46]  And I say living the dream because he's now able to have 100% control of the types of projects and technologies he's working on,
[1525.66 --> 1527.12]  as well as the rate he wants to charge.
[1527.12 --> 1531.26]  Daniel earns 100% of his income as a TopTile engineer,
[1531.46 --> 1536.72]  and he wanted me to pass on his seal of approval, so to speak, of the TopTile experience.
[1536.82 --> 1540.76]  And for those of you out there who are freelancing or would like to test out freelancing
[1540.76 --> 1545.28]  or even try out a no-risk freelance-like project while you maintain your full-time position,
[1545.62 --> 1546.84]  you've got to check out TopTile.
[1547.02 --> 1550.90]  If you think you have what it takes, head to TopTile.com to get started.
[1551.24 --> 1552.52]  Tell them the ChangeLog sent you.
[1552.98 --> 1553.84]  And now back to the show.
[1554.66 --> 1556.34]  Let's talk about those beta users you mentioned.
[1556.34 --> 1561.96]  How many beta users do you have of Fusion or Passenger 5, a codenamed Raptor?
[1562.76 --> 1564.36]  How many are they exact?
[1564.48 --> 1565.36]  I don't know.
[1565.40 --> 1567.44]  We don't have any statistics for that.
[1568.20 --> 1568.64]  Okay.
[1568.88 --> 1570.40]  Let's maybe talk about then.
[1570.48 --> 1575.94]  What I'm trying to get at here is the perceived change to perception of you, right?
[1575.94 --> 1584.32]  So judging on your merits, this new version out there that's much faster, four times faster than competitors, all that good stuff,
[1584.72 --> 1587.00]  what's the feedback from those people?
[1587.36 --> 1596.96]  These are obviously people who are using your latest, greatest, best version of it that was the shiny new object that turned out to be the same really awesome object,
[1596.96 --> 1598.96]  but just a shiny new cover on it.
[1600.96 --> 1606.58]  Well, it's actually not just a shiny new cover because there actually are a lot of new improvements.
[1606.58 --> 1610.08]  So it's something I can talk about that a little bit later.
[1610.58 --> 1615.00]  It includes this rewritten HTTP engine that makes things faster.
[1615.40 --> 1618.32]  And there's integrated caching support.
[1618.70 --> 1627.34]  And there's also a lot of internal changes in terms of being able to improve the visibility of your application's behavior.
[1627.34 --> 1631.88]  But what we have focused on mostly is the bug reports.
[1632.04 --> 1633.94]  We really value stability.
[1634.54 --> 1638.08]  So there were surprisingly few bug reports, actually.
[1638.20 --> 1646.26]  There were about five bug reports that we deemed critical, like they were called crashes, and we have fixed most of them.
[1647.02 --> 1654.72]  And after this phase is over, we can release a version that is kind of usable for testing in production.
[1654.72 --> 1660.88]  You mentioned that – sorry, what was your question again?
[1661.02 --> 1663.68]  I'm trying to figure out what the – Jared's over there jumping.
[1663.86 --> 1665.36]  This is the first time, by the way, y'all.
[1665.44 --> 1670.48]  We laughed a couple times during this show that may have seemed unusual laughs, but we got our video on on this call.
[1670.56 --> 1673.62]  We don't usually do video during our Skype calls, but we can all see each other.
[1673.78 --> 1677.28]  So I'm seeing Jared kind of antsy over there to ask some sort of question.
[1677.28 --> 1689.18]  But the thing I'm trying to drive here is I'm trying to figure out what you said was that the perception had changed about passenger because you weren't shiny and new, right?
[1689.48 --> 1699.80]  And what I'm trying to figure out is of the new people that began using the latest passenger five, aka Raptor, that's four times faster than X and all that good stuff.
[1699.80 --> 1707.52]  What is their feedback about using this new version that's got the new HTTP server that you just talked about there?
[1707.72 --> 1710.48]  What has been the feedback about their usage of it?
[1711.10 --> 1715.36]  And because we talked about the bait switch for a bit there, but just trying to figure out the perception.
[1715.46 --> 1716.50]  How has the perception changed?
[1717.02 --> 1720.58]  A lot of people, they perceive passenger as faster now.
[1720.58 --> 1728.86]  But we do have to say it is faster in benchmarks, but that does not mean that it is faster in real-world scenarios.
[1729.28 --> 1730.22]  And that's a big disclaimer.
[1730.74 --> 1738.54]  So the number of people who have noticed an increase in actual production performance, they are very limited.
[1738.84 --> 1746.54]  Because in actual production environments, the time spent in the application is a very significant part of the overall time,
[1746.60 --> 1749.20]  and the app server is a very tiny part.
[1749.20 --> 1756.32]  Having said that, one of the major features in Passenger 5 is this turbo caching thing.
[1756.88 --> 1766.06]  And turbo caching is an integrated cache in Passenger that would cache responses and send back a reply on the HTTP level.
[1766.24 --> 1773.30]  And it can completely offload your application to Passenger itself, which is written in C++ and does very fast.
[1773.30 --> 1780.52]  And this is the primary way that we provide to really improve the performance of your application,
[1780.72 --> 1786.32]  even though the application takes up a large amount of time of the entire processing time.
[1786.86 --> 1794.68]  So just to be clear, is this the kind of cache mechanism that a varnish would do or that you would do with Nginx, perhaps?
[1795.32 --> 1796.20]  This turbo caching?
[1796.20 --> 1801.10]  Or is it something that just doesn't exist at all outside of the passenger space?
[1801.84 --> 1803.94]  Well, right now, it is an HTTP cache.
[1804.08 --> 1808.04]  So it is on the same level as Varnish or Nginx.
[1808.74 --> 1812.84]  Having said that, we are working on something new.
[1812.92 --> 1818.04]  We are working on an extension to this mechanism to introduce a new kind of cache.
[1818.04 --> 1825.74]  With this cache that we have right now, we have noticed from feedback from people that it is of limited usefulness.
[1826.18 --> 1832.62]  Like a lot of apps are not cacheable on the HTTP side, on the HTTP level.
[1833.18 --> 1835.58]  Some of them are, but those are mostly static websites.
[1835.84 --> 1840.10]  So if you have an app that, for example, has a login button that displays your username,
[1840.36 --> 1843.10]  then it is already not cacheable on the HTTP level.
[1843.10 --> 1849.48]  So what we are going to introduce in the near future, and we are also going to blog about this,
[1849.70 --> 1857.04]  is to introduce a variation of the HTTP cache that allows you to cache these sorts of apps as well.
[1857.18 --> 1862.80]  Because we have seen, even though a lot of apps are not cacheable technically,
[1863.22 --> 1866.60]  there are a lot of parts in the app that are cacheable.
[1866.60 --> 1872.64]  And which version of the cache you should serve, in a lot of cases,
[1872.76 --> 1877.80]  it depends only on whether the user is logged in or not.
[1878.70 --> 1885.44]  So caches like Varnish, they have problems with caching pages that have cookies,
[1885.86 --> 1890.46]  pages where the content depends on the logged-in user.
[1890.70 --> 1895.72]  But there are large classes of applications that have a lot of anonymous traffic.
[1895.72 --> 1901.72]  For example, think about marketplaces or news sites, maybe even something like Twitter,
[1902.42 --> 1906.14]  where a lot of anonymous people browse the tweets or even YouTube.
[1907.26 --> 1911.82]  And we thought, okay, what if we can come up with a new mechanism
[1911.82 --> 1921.76]  that would allow you to cache the content based on a cookie that specifies which user is logged in?
[1921.76 --> 1929.60]  If we can do that, then you can share the cache response for all the anonymous users.
[1930.04 --> 1935.76]  And that would be able to increase your traffic, I mean, increase your performance tremendously.
[1936.58 --> 1943.36]  For all anonymous traffic, you can completely offload your application and surf directly from passenger.
[1943.36 --> 1951.48]  And I think there's a real use case there that would be really useful for passenger to provide.
[1951.48 --> 1957.10]  So it's like a per-user cache, but one user is the anonymous user,
[1957.26 --> 1961.82]  which actually represents N numbers of people who are not signed in.
[1962.86 --> 1963.46]  Almost.
[1963.88 --> 1967.46]  There's an anonymous user cache, but we can also extend this.
[1967.92 --> 1974.34]  I mean, we can also generalize this concept to a level where you can cache based on user classes.
[1974.34 --> 1981.08]  For example, if you are talking about a user forum like Discourse or PHPPP or something,
[1981.64 --> 1987.14]  then what you actually want to cache, the cached version that you want to send to the client
[1987.14 --> 1992.44]  is based not on who the user is, but on what permission level the user has.
[1992.52 --> 1997.92]  So then you can, for example, define user classes of normal users and moderators.
[1998.22 --> 2002.72]  And then you can send out one version for all normal users and one version for all moderators.
[2002.72 --> 2011.80]  And suppose that you also make some small changes in the application to make it sort of like a single page app.
[2012.08 --> 2014.78]  So then you would load your user details only once.
[2015.08 --> 2018.32]  And for all subsequent page loads, you would use Ajax.
[2018.58 --> 2024.72]  But then that version does not need to query any specific user-specific information.
[2024.84 --> 2028.22]  They only need to know what class the user belongs to, what permission level.
[2028.22 --> 2035.84]  And then if you use that, then you can have these small numbers of cache levels that each one has a very large cardinality.
[2036.04 --> 2042.82]  And that would make things really a lot more cacheable than would be possible with normal HTTP caches.
[2043.38 --> 2049.54]  And I think this would be a real innovation in the HTTP level caching systems.
[2049.76 --> 2049.88]  Yeah.
[2050.36 --> 2051.08]  No, that's exciting.
[2051.20 --> 2054.66]  And definitely keep us in the loop on as you guys develop that out.
[2054.66 --> 2061.36]  Let's talk about what's in Passenger 5 that makes it so fast, even if these are for the synthetic benchmarks.
[2062.12 --> 2064.36]  It seems like you guys have some innovations that have happened here.
[2064.44 --> 2071.12]  One of these is the hybrid I.O. model, where it appears to do multi-process, multi-thread, and a vented in certain cases.
[2071.54 --> 2072.36]  Can you talk to that?
[2074.00 --> 2082.50]  So the hybrid model is not so much for performance as in raw benchmark performance, but it is more for safety and security.
[2082.50 --> 2082.98]  Okay.
[2083.40 --> 2089.06]  The main idea behind that hybrid model is to protect your server from so-called slow clients.
[2089.64 --> 2094.96]  And so slow clients, they can include users who are all on modem, but they don't really exist nowadays.
[2095.40 --> 2098.32]  Users who are on mobile networks, they just have high latency.
[2098.32 --> 2114.14]  So what happens if you have a lot of slow clients, it's like having a lot of people standing in front of your door, and then your normal visitors, they can't enter because of all these people standing there, just standing still and not doing anything.
[2114.14 --> 2126.10]  And the only way to really solve that is by having an evented server on some level that would have a virtually infinitely large door, so to say.
[2127.18 --> 2129.28]  And that is what the passenger core is.
[2129.46 --> 2133.62]  It has a server that is built using the evented style.
[2133.62 --> 2137.80]  Also, that's the same style as Nginx and as Node.js.
[2138.04 --> 2142.76]  It would use operating system level primitives to be able to handle lots of clients.
[2143.22 --> 2146.74]  And it would shield the application from these slow clients.
[2146.88 --> 2153.32]  It would put them in nicely ordered queues where each request and response is very fast.
[2153.44 --> 2155.70]  And so your application doesn't have to worry about that.
[2155.70 --> 2162.48]  You don't have to worry about people using a denial of service attack to block your server.
[2163.02 --> 2169.22]  This doesn't protect you from all denial of service attacks, of course, but it protects you from certain classes.
[2170.62 --> 2176.08]  And the reason why we made it hybrid is to get a little bit of extra performance out of this.
[2176.66 --> 2183.00]  The problem with the normal evented style is that you cannot use multiple cores.
[2183.00 --> 2187.02]  One evented server only runs on a single CPU core.
[2187.32 --> 2195.30]  But then we invented a mechanism to make sure that each CPU core runs its own event loop.
[2195.96 --> 2203.12]  And then we have this load balancer to distribute new clients equally in a round-robin fashion over each core.
[2203.36 --> 2206.62]  And that's how we can leverage multiple CPU cores better.
[2207.38 --> 2212.12]  So some of this work, you know, sometimes is taken off by an Nginx or a HAProxy.
[2212.12 --> 2222.12]  Is it your guys' best practice to, once Fusion Passenger 5 is out of beta, to serve it directly, like have it less than on port ADN443?
[2222.98 --> 2225.56]  Or would you still put it behind some sort of proxy?
[2226.36 --> 2229.84]  You should put it behind some sort of proxy.
[2229.84 --> 2239.70]  So what we did is writing an entirely new HTTP engine that is not only safe, but also very fast.
[2239.90 --> 2245.20]  But the downside of this, of being very fast, is that we had to sacrifice some features.
[2245.92 --> 2251.12]  There are just some features this HTTP engine would never have and that Nginx would have.
[2251.42 --> 2254.18]  And one important thing is, for example, G-step compression.
[2254.18 --> 2258.64]  G-step compression is very important if you have mobile clients.
[2259.58 --> 2263.64]  But we're never going to support that because it would just complicate our code.
[2263.84 --> 2269.58]  It would probably also make things slower by making the architecture more complex.
[2269.82 --> 2271.44]  So we have made an explicit decision.
[2271.72 --> 2274.42]  If you need features, just put an Nginx in front of it.
[2275.24 --> 2277.94]  There's nothing wrong with putting Nginx in front of it.
[2277.94 --> 2284.16]  You would notice that in benchmarks it would probably get slower, but you're not going to notice it in production.
[2286.20 --> 2287.76]  So what else about this is new?
[2287.80 --> 2294.72]  It looks like you have written your own HTTP server for this version, which you say is twice as fast as Nginx.
[2294.78 --> 2296.32]  How did you accomplish that?
[2298.26 --> 2300.44]  Well, mainly by doing less than Nginx.
[2300.44 --> 2308.22]  Nginx is fast, but it's not as fast as it theoretically can be because it has these sorts of features.
[2308.78 --> 2311.76]  So our HTTP server is very bare bones.
[2312.12 --> 2319.72]  We only recommend putting it in your local network for internal communications, but not directly on the internet.
[2319.84 --> 2324.08]  If you want to put it directly on the internet, you should put Nginx in front of it.
[2324.08 --> 2330.52]  And Nginx has these configuration options that makes it internally very flexible.
[2331.22 --> 2338.08]  From a C programmer standpoint, we would say that Nginx internally has a lot of indirect branches,
[2338.28 --> 2341.76]  and that means it has pointers everywhere that points to different functions,
[2341.76 --> 2346.56]  and that doesn't really help with CPU branch target prediction or CPU branch prediction.
[2347.34 --> 2353.56]  There's a lot of safety checks inside Nginx to check for all sorts of stuff.
[2353.56 --> 2361.58]  Nginx has its own IO layer to handle disk IO, and just all sorts of stuff that we don't have.
[2361.70 --> 2368.72]  For our HTTP engine, we just focus on the complete bare minimum that is necessary for a web server,
[2368.92 --> 2371.62]  and that's how we made it fast.
[2372.06 --> 2377.02]  But in real production scenarios, the difference is tiny.
[2377.14 --> 2379.08]  You are probably not going to notice it.
[2380.38 --> 2383.32]  All right, let's pause the show for just a minute, give a shout out to our sponsor.
[2383.32 --> 2384.90]  I want to talk to you about DaysWork.
[2385.46 --> 2390.48]  DaysWork is a new way to track time and sending invoices for freelancers and small companies.
[2390.82 --> 2395.08]  It was designed and built by a small company who was bummed out by other time trackers.
[2395.22 --> 2399.12]  So if you're a freelancer tracking time or you work in a small company,
[2399.18 --> 2401.06]  then you should definitely check this sponsor out.
[2401.48 --> 2405.26]  And as a designer, one of the things I like most about it is they allow you to visualize
[2405.26 --> 2409.52]  the effort that you make every day on a readable and interactive timeline.
[2409.52 --> 2412.70]  This helps make sure you don't forget any of the time you have in a day
[2412.70 --> 2416.08]  and make sure you fill in all the time that you've spent on clients
[2416.08 --> 2420.50]  and also know which clients you're spending the most time on, which is super important.
[2420.90 --> 2425.56]  You can control who can see and manage financials with the admin and non-admin roles.
[2425.92 --> 2428.42]  They allow you to give every member of your team their own account,
[2428.42 --> 2429.98]  so there's no limits whatsoever.
[2430.64 --> 2433.62]  It even has international support, so you can choose your currency,
[2434.24 --> 2437.02]  a 12 or 24-hour clock, and preferred number formatting.
[2437.62 --> 2442.14]  DaysWork is by far the simplest and easiest way to organize your clients
[2442.14 --> 2444.22]  and keep track of your business this time.
[2444.64 --> 2447.84]  And right now, you can sign up for a free trial for 30 days.
[2448.12 --> 2450.26]  No credit cards required, so you've got nothing to lose.
[2450.60 --> 2454.10]  And since a fellow 5x5 hosts help create DaysWork,
[2454.42 --> 2457.30]  they're offering a special discount for 5x5 listeners.
[2457.30 --> 2464.36]  Here's the URL you need to go to, dayswork.co.join.changelog.
[2464.42 --> 2470.38]  Again, that URL is dayswork.co.join.changelog.
[2470.42 --> 2475.56]  Go to that URL, get 20% off both monthly and yearly plans right now.
[2475.92 --> 2481.48]  Once again, that URL is dayswork.co.join.changelog.
[2481.74 --> 2482.66]  And now back to the show.
[2484.20 --> 2486.78]  I'm reading through some of the list of your guys' optimizations.
[2487.30 --> 2489.82]  I'm avoiding dynamic memory allocations.
[2490.10 --> 2493.44]  Looks like you've got some, you're taking advantage of the Node.js HTTP parser.
[2494.10 --> 2496.94]  Anything else in the internals that really stands out that you'd like to talk about?
[2498.22 --> 2502.68]  I think our blog post covers pretty much all the important stuff.
[2503.86 --> 2504.22]  Cool.
[2504.22 --> 2508.28]  So we'll definitely link out to those on the show notes.
[2508.34 --> 2511.88]  It looks like the first one is how we made Raptor up to four times faster than Unicorn.
[2512.60 --> 2517.64]  And then there's a follow-up post about pointer tagging, turbo caching, and other things.
[2518.68 --> 2522.34]  So yeah, we can just link out to those and our listeners can go and read.
[2522.34 --> 2528.44]  Yeah, but the main thing is that we borrowed a lot of things from Node.js, from Nginx.
[2528.88 --> 2530.40]  Their authors are really brilliant.
[2530.50 --> 2535.02]  They have done a fantastic job and we have just borrowed the best parts from them.
[2535.40 --> 2536.80]  We couldn't have done this without them.
[2537.98 --> 2539.32]  That's the beauty of open source, right?
[2539.36 --> 2541.88]  You pull together all the best ideas, the best implementations.
[2541.88 --> 2544.40]  It's not the first time you heard that.
[2544.40 --> 2546.30]  Yeah, it's a winning pattern.
[2546.96 --> 2547.84]  It is a winning pattern.
[2548.38 --> 2550.26]  Look what others are doing and repeat it.
[2550.32 --> 2550.48]  Yeah.
[2550.54 --> 2551.04]  It makes sense.
[2551.26 --> 2554.84]  So let's shift gears a little bit and tell us about your guys' new project,
[2554.98 --> 2556.60]  which you're calling Traveling Ruby.
[2557.18 --> 2557.70]  What's this?
[2558.70 --> 2566.40]  Okay, Traveling Ruby is about being able to distribute your Ruby apps to users.
[2566.40 --> 2572.86]  So if you are a Windows programmer and you have programs in Delphi,
[2573.24 --> 2579.48]  then you would know the beauty of being able to make a single executable that users can just use.
[2580.18 --> 2584.58]  If you have ever used Windows and then you have this .NET app or Java app,
[2584.78 --> 2589.24]  then I'm sure you would have run into ridiculous situations where they say,
[2589.24 --> 2595.84]  hey, you have to install .NET Framework 5.1 first or Java 5 first before you can use the app.
[2595.84 --> 2597.92]  And that just discourages users.
[2598.36 --> 2600.80]  And then in Unix land, it's even worse.
[2601.46 --> 2607.46]  If your app is not packaged by a package manager, and even if it is, then it's probably out of date,
[2607.68 --> 2609.38]  then your users are out of luck.
[2609.44 --> 2613.84]  They have to compile your app from source.
[2614.22 --> 2616.74]  And in case of Ruby, they have to install Ruby.
[2616.84 --> 2619.24]  They have to use RubyGems to install your gems.
[2619.86 --> 2621.82]  And that's just not nice to users.
[2621.82 --> 2624.80]  As a user, you just want to be able to use the app,
[2625.00 --> 2630.64]  and you want it to immediately work without having to take all these sort of sidesteps.
[2630.98 --> 2633.90]  This is also the reason why a lot of people are flocking to Go now,
[2633.98 --> 2637.22]  because Go can just create a single executable that works everywhere.
[2637.88 --> 2641.76]  And it is with this vision that we have created Traveling Ruby.
[2641.76 --> 2648.52]  We have these tools that we want to write in Ruby, because we love Ruby as a language.
[2649.50 --> 2654.84]  But distributing this app to users, it's just a pain if users have to install Ruby
[2654.84 --> 2656.86]  and have to use RubyGems first.
[2657.04 --> 2658.26]  It's going to scare them away.
[2658.70 --> 2660.00]  We want to keep on using Ruby.
[2660.12 --> 2661.24]  We don't want to switch to Go.
[2661.24 --> 2664.82]  And so we came up with this idea of Traveling Ruby,
[2665.32 --> 2670.62]  of just distributing Ruby binaries along with your application.
[2671.40 --> 2675.82]  And the good thing with this approach is that you don't have to set up a fleet of VMs
[2675.82 --> 2680.42]  to cross-compile your application for multiple different operating systems.
[2680.86 --> 2684.74]  If you had to set up these VMs, then as a developer, you would lose a lot of time.
[2684.82 --> 2685.50]  It's just slow.
[2685.60 --> 2687.08]  You just don't want to do this.
[2687.12 --> 2690.58]  It makes the entire experience not enjoyable.
[2690.58 --> 2693.52]  And we want to keep that enjoyable for developers.
[2693.74 --> 2694.56]  That's really important.
[2695.30 --> 2697.32]  So with Traveling Ruby, the idea is really simple.
[2697.42 --> 2699.16]  You take the binaries that we pre-built.
[2699.34 --> 2701.92]  You drop them in a tarpa.
[2702.30 --> 2705.94]  You make three versions of them, each one with platform-specific binaries.
[2706.16 --> 2707.02]  And then you are done.
[2707.08 --> 2713.44]  As a developer, you don't have to learn these complicated steps to make RPM or dApps.
[2713.78 --> 2718.48]  And then each one for all the 20 different Linux distributions, it would just work.
[2718.48 --> 2720.04]  It saves you a lot of time.
[2720.58 --> 2721.14]  Wow.
[2721.32 --> 2723.02]  So what's the status of this project?
[2723.10 --> 2723.78]  Just getting started?
[2724.02 --> 2726.04]  Or is there stuff out there where people can get involved?
[2727.00 --> 2728.98]  It just started, but it's usable.
[2729.14 --> 2730.66]  And it's actually already being used.
[2730.76 --> 2735.50]  For example, the Cloud Foundry project, they have this tool called Bosch.
[2735.94 --> 2740.30]  And Bosch is some kind of release engineering tool.
[2740.30 --> 2743.12]  I'm not entirely sure what it is.
[2743.22 --> 2749.34]  But one of the main problems they've had for a long time is that a lot of their users are not Ruby guys.
[2749.42 --> 2750.66]  They just want to use Bosch.
[2750.74 --> 2752.94]  But then they are told, hey, they have to install Ruby.
[2752.94 --> 2761.92]  And then the developers of this tool just saw that a lot of people struggle with installing Ruby and struggle with installing the dependencies.
[2762.50 --> 2771.86]  So then they have used Traveling Ruby to provide a single package, self-contained, contains everything that they need to run Bosch.
[2772.00 --> 2773.38]  And it's been great.
[2773.38 --> 2777.56]  All their user installation problems have been solved by this.
[2778.28 --> 2793.86]  It sounds a lot like, I guess not a lot like, but to a degree like containerization, Docker, sort of self-contained distributables that make it easy to kind of move these applications or, yeah, I guess in this case, applications too, around.
[2794.14 --> 2797.32]  The build system actually uses Docker and make.
[2797.38 --> 2801.66]  Can you talk a bit about the build system for those that are going to be building Traveling Ruby binaries?
[2801.66 --> 2801.82]  Yes.
[2802.62 --> 2803.06]  Yes.
[2803.14 --> 2811.92]  So the problem with building binaries, especially for Linux, is that there are so many Linux distributions.
[2813.52 --> 2822.22]  So because of all kinds of technical reasons, it's very hard to build a Linux binary that works on all Linux distributions.
[2822.96 --> 2830.04]  So what people traditionally have done is they rebuild the binary once for every distribution.
[2830.04 --> 2836.86]  And this is just nuts if you have to take care of all the 20 different variations plus all the different platforms.
[2837.58 --> 2842.00]  But there is a way to build binaries that works on every Linux.
[2842.14 --> 2845.20]  It just takes a lot of expertise to do it.
[2845.20 --> 2854.56]  And it just so happens that I've had a few years of experience with researching this kind of stuff and building portable binaries.
[2854.90 --> 2862.80]  So then we have a very tightly controlled build environment that we use to build a tightly controlled Ruby binary
[2862.80 --> 2871.02]  that happens to run on all Linux distributions by limiting the number of glibc symbols that they use,
[2871.24 --> 2876.70]  by statically linking certain libraries, and so forth.
[2879.04 --> 2879.60]  Nice.
[2879.72 --> 2885.48]  So do you have a call to action for Traveling Ruby besides use this tool?
[2885.48 --> 2889.30]  Is it highly under development or is it about wrapped up?
[2889.90 --> 2891.76]  Looking for help, looking for bug reports?
[2891.82 --> 2892.54]  What are you looking for here?
[2893.22 --> 2899.50]  Well, it is kind of wrapped up for us because we initially developed Traveling Ruby
[2899.50 --> 2905.56]  because it is a tool that we need for a future tool that we are going to build in Ruby.
[2906.46 --> 2910.38]  So right now, Traveling Ruby already does everything we want it to do.
[2910.38 --> 2913.78]  We have heard from some people in the community, they want Windows support,
[2913.92 --> 2915.92]  but it's not something that we want to bother with.
[2915.92 --> 2916.96]  I was going to ask you about that.
[2918.10 --> 2918.46]  Yeah.
[2918.60 --> 2924.74]  I was going to ask you about that because it's in your readme that you're talking about not supporting it right now for obvious reasons.
[2925.50 --> 2925.86]  Yeah.
[2926.20 --> 2928.30]  For obvious reasons for you because you don't need it.
[2928.66 --> 2928.82]  Yeah.
[2928.92 --> 2930.92]  So I do have a call of action.
[2931.32 --> 2933.50]  Please help us with Windows support.
[2933.66 --> 2934.60]  Please contribute.
[2934.86 --> 2935.38]  There you go.
[2935.38 --> 2937.58]  Yeah, it should be very easy.
[2937.80 --> 2940.64]  Like the Ruby installer project, they already provide Ruby binaries.
[2940.78 --> 2948.94]  So I imagine that it would only be a matter of extracting the binaries they have and repackaging it in a format.
[2949.14 --> 2951.64]  But then you still have native extensions.
[2951.86 --> 2953.38]  You have these gems like MySQL.
[2954.32 --> 2960.42]  And they usually already ship Windows binaries, but some of them are quite out of date
[2960.42 --> 2962.36]  because the maintainer couldn't keep up.
[2962.36 --> 2969.28]  And so I'm asking listeners to please help them, in particular the MySQL 2 gem author.
[2969.62 --> 2972.10]  They need help with keeping their binaries up to date.
[2972.52 --> 2975.54]  They have these GitHub issues open in which they ask for help.
[2975.74 --> 2979.98]  Please go there, read what they say, and just give them a hand if you care about Windows support.
[2980.46 --> 2984.18]  So you mentioned a future tool that you guys are working on.
[2984.38 --> 2985.82]  Anything you want to tease there?
[2986.18 --> 2987.76]  Anything in the pipeline you want to talk about?
[2989.26 --> 2989.70]  Yes.
[2989.82 --> 2991.66]  And this is about the future of Passenger.
[2991.66 --> 2999.04]  So Passenger, for the longest time, has focused a lot on making deployment easy, but only in a limited scope.
[2999.82 --> 3002.66]  So Passenger handles transaction management.
[3003.14 --> 3008.16]  It handles process management, spawning of your processes, and so forth.
[3008.36 --> 3010.54]  But there's a lot of things that it doesn't do.
[3010.62 --> 3012.74]  For example, it doesn't manage the rest of your servers.
[3012.94 --> 3014.18]  It doesn't set up your server.
[3014.18 --> 3020.32]  If you look at something like Heroku, then it's much more of a complete solution.
[3021.72 --> 3028.50]  And we actually have a vision of building something on the order of Heroku.
[3028.50 --> 3036.18]  So the vision is that you can easily deploy your application to any infrastructure.
[3036.18 --> 3043.70]  So not just on AWS, but for example, also on-premise or DigitalOcean or Linode,
[3044.56 --> 3054.70]  with about the same ease of use that Heroku has or something that approaches it.
[3054.70 --> 3059.84]  And this tool is something that we're still working on.
[3059.92 --> 3061.58]  It's currently in prototype phase.
[3061.58 --> 3064.62]  We do not yet know what it is going to be called.
[3064.96 --> 3067.94]  But you would just be able to tell the tool,
[3068.22 --> 3071.06]  hey, I'm on DigitalOcean.
[3071.56 --> 3073.40]  Here are my credentials.
[3073.40 --> 3075.98]  I need Ruby 2.1.
[3076.56 --> 3077.14]  Go nuts.
[3077.62 --> 3080.76]  And then the tool would just spawn the servers for you,
[3081.10 --> 3083.26]  deploy your app, and then you are done.
[3083.38 --> 3087.16]  And then on every app release, you would just use that tool,
[3087.32 --> 3089.66]  and then you are done, and you don't have to do anything else.
[3089.88 --> 3093.32]  And this is much more of a complete solution than Passenger.
[3093.48 --> 3096.78]  But of course, internally, it would use Passenger as the app server.
[3098.14 --> 3098.40]  And I think...
[3099.22 --> 3100.68]  So when can I use this thing?
[3100.68 --> 3101.16]  I think...
[3101.16 --> 3103.76]  You don't have to answer that.
[3104.04 --> 3105.28]  It would take a while.
[3105.52 --> 3107.72]  I don't think I can answer this yet.
[3107.78 --> 3110.20]  It's still very much in a pro type phase.
[3110.56 --> 3111.50]  Well, that's very exciting.
[3111.64 --> 3114.68]  And if you're looking for a name, I hear the name Raptor is available.
[3116.24 --> 3119.00]  No, the name Raptor is not available.
[3119.48 --> 3120.26]  That reminds me.
[3120.28 --> 3123.24]  Did you guys ever consider renaming to Raptor?
[3123.30 --> 3125.28]  I know it's just a code name and you're now discarding it.
[3125.34 --> 3127.76]  But did you ever think, well, what if we just go with Raptor?
[3127.76 --> 3131.40]  We can't do that for trademark reasons.
[3131.84 --> 3131.96]  Oh.
[3133.18 --> 3133.94]  Jurassic Park?
[3134.42 --> 3136.54]  Who's trademarking Raptor?
[3136.98 --> 3137.14]  Do you know?
[3138.86 --> 3140.40]  Or you're saying because you have passengers?
[3140.40 --> 3140.74]  Ford.
[3141.52 --> 3141.84]  Ah.
[3142.04 --> 3143.76]  Ford's got it trademarked.
[3146.00 --> 3147.16]  Screw the truck.
[3147.36 --> 3149.24]  They get the Raptor version of the truck.
[3149.80 --> 3150.44]  There you go.
[3150.44 --> 3156.64]  There are all sorts of parties who have trademarked Raptor.
[3156.90 --> 3161.42]  And also, there's actually already a gem named Raptor, but it's completely unrelated to us.
[3161.66 --> 3164.90]  It's a web framework that happens to be also called Raptor.
[3165.04 --> 3169.32]  So the gem name is already used.
[3169.40 --> 3170.20]  We cannot use that.
[3171.32 --> 3172.84]  Well, never mind then.
[3172.84 --> 3175.18]  I was mostly just kidding.
[3175.42 --> 3175.76]  Anyways.
[3176.72 --> 3178.72]  One last question, then we'll wrap here.
[3179.72 --> 3183.16]  Do you have Passenger 5 is in beta 2.
[3183.86 --> 3189.26]  Is there a schedule for public release of Passenger 5 when you'll be getting out of beta?
[3189.84 --> 3195.32]  The release date depends on the amount of bug reports that come in and how many of them are critical.
[3195.32 --> 3201.68]  But as things are right now, I expect that beta 3 would come out maybe somewhere next week.
[3202.30 --> 3207.36]  And that would solve all the critical bugs and then there would only be minor bugs left.
[3208.22 --> 3214.28]  And so somewhere past next week, we would be able to release a release candidate.
[3215.54 --> 3221.70]  And probably Passenger 5 final would be out at the beginning of February.
[3222.84 --> 3223.48]  Nice.
[3223.48 --> 3227.92]  Well, man, thanks for joining us.
[3228.00 --> 3231.62]  We do have one question we usually wrap with here, which we didn't give you much of a heads up on.
[3231.92 --> 3235.42]  But I'm sure you'll handle it just fine.
[3236.10 --> 3238.66]  And that is, who is your programming hero?
[3240.36 --> 3241.56]  Who's my programming hero?
[3243.06 --> 3245.42]  Feel free to pick a couple if it's hard to narrow it down.
[3246.72 --> 3249.92]  Zed Shaw, author of Mongrel, he's a really brilliant guy.
[3249.92 --> 3255.62]  I think Zed Shaw is underappreciated by the community.
[3256.18 --> 3260.82]  Maybe, I'm sure a lot of people know him from his rants.
[3261.16 --> 3261.28]  Sure.
[3261.56 --> 3263.40]  And a lot of people think he's a jerk.
[3263.52 --> 3265.94]  But in reality, he is really a nice guy.
[3266.02 --> 3268.68]  He's the nicest guy you have ever met if you know him.
[3268.86 --> 3269.14]  Is he?
[3270.00 --> 3270.58]  Yes, yes.
[3270.66 --> 3272.38]  In real life, he's really nice.
[3272.58 --> 3275.12]  Totally not like his internet persona.
[3275.12 --> 3275.24]  Yeah.
[3275.60 --> 3279.10]  So, and he's really experienced in a lot of things.
[3279.24 --> 3280.40]  I have learned a lot from him.
[3280.72 --> 3283.34]  Yeah, it seems like he had, like you said, the Mongrel author.
[3284.80 --> 3286.92]  Mongrel itself fell out of favor years back.
[3286.92 --> 3293.24]  But the parser in there continues in use probably today in many Ruby app servers.
[3294.00 --> 3295.62]  Did Passenger use it or does it still?
[3296.58 --> 3298.12]  No, Passenger does not use it.
[3298.40 --> 3298.68]  Okay.
[3299.34 --> 3301.30]  For all kinds of reasons.
[3301.34 --> 3302.86]  You're using the Node.js parser.
[3302.98 --> 3303.22]  Yes.
[3305.12 --> 3305.76]  Yeah, it's funny.
[3305.82 --> 3308.28]  We had Zed Shaw on episode 34.
[3308.66 --> 3311.42]  So that's like forever ago in our history.
[3311.70 --> 3314.30]  September 8, 2010, we had him on the show.
[3314.74 --> 3314.98]  Cool.
[3315.06 --> 3315.56]  Way back when.
[3315.64 --> 3321.62]  Wynn had a conversation with him about, well, as Wynn says, his non-rockstar alter ego was on the show.
[3322.94 --> 3328.20]  Talking about Mongrel 2, high-performance websites, guitar, and the software community, and Ponzi schemes.
[3329.02 --> 3330.14]  So that was a good show.
[3330.98 --> 3333.60]  Yeah, Zed Shaw, I think you're right, though.
[3333.60 --> 3344.16]  I mean, he's known for his rants, but I think he's, what I've always appreciated most about Zed, aside from his really awesome code, is that he seems like a really real person.
[3344.38 --> 3345.86]  He tells it like it is.
[3345.94 --> 3353.64]  He's, you know, he doesn't fluff it, you know, by any means where some people are a little bit more rounded off the edges.
[3353.64 --> 3356.60]  He's a bit more sharp in that regard.
[3357.62 --> 3361.72]  He's also really good at bringing the troll that's inside of us out.
[3361.86 --> 3362.04]  Out.
[3362.12 --> 3362.78]  Out of the inner troll.
[3362.94 --> 3363.20]  Yes.
[3363.42 --> 3368.44]  You can really extract that inner troll out of the greater programming community on a regular basis.
[3368.44 --> 3368.66]  Yes.
[3369.06 --> 3369.22]  Yeah.
[3369.32 --> 3371.44]  Any other programming heroes you want to give a shout-out to?
[3372.80 --> 3373.70]  It's really hard.
[3373.70 --> 3380.00]  Like, I regularly read hacker news, and I think, wow, those guys are really smart when I read those articles.
[3380.32 --> 3383.02]  But I can't really recall any names.
[3384.28 --> 3394.76]  I just think that if there are heroes, I don't know them personally, but there are a lot of people out there in the world that are a lot smarter than I am, and I just have to keep learning.
[3395.76 --> 3396.00]  Yeah.
[3396.00 --> 3399.10]  Well, if you come up with any names, we'll link them in the show notes for sure.
[3400.36 --> 3401.00]  It's all good, man.
[3401.04 --> 3408.96]  Hong Lee, thanks so much for joining us and sharing both your marketing and technical prowess with Passenger, a.k.a. Raptor.
[3409.00 --> 3409.24]  Yeah.
[3409.44 --> 3410.86]  I got a chuckle out of it myself.
[3410.96 --> 3412.92]  I was excited when it was just Passenger.
[3412.98 --> 3417.78]  I say just Passenger 5 because as a Passenger user, now all I got to do is upgrade, right?
[3418.50 --> 3420.66]  So thanks for—
[3420.66 --> 3421.36]  That made it easier, right?
[3421.40 --> 3421.70]  Exactly.
[3421.78 --> 3423.50]  All I got to do is hit the old upgrade button.
[3424.00 --> 3425.86]  Thanks so much for your open source over the years.
[3426.00 --> 3426.78]  And thanks for joining us.
[3427.44 --> 3427.68]  Yeah.
[3427.68 --> 3432.88]  I think to add to Jared's note there, I think the marketing take was genius in my opinion.
[3433.68 --> 3445.28]  I sure hope any sort of lashback from the community on the bait-and-switch idea that you mentioned doesn't come back to you harshly because I think that you made a bet.
[3445.56 --> 3447.08]  All we can do is test things, right?
[3447.16 --> 3448.92]  Test the waters on how things can be released.
[3449.18 --> 3454.00]  And I think you proved that shiny objects are attractable.
[3454.00 --> 3462.52]  You grew your newsletter list quite well, and you grew better support for it, and you've reopened new eyes to Passenger through this.
[3463.26 --> 3466.40]  And now we just have to fulfill our promise of being better.
[3466.54 --> 3470.70]  We have to keep up with releasing new features and just making it better.
[3471.44 --> 3471.68]  Yeah.
[3471.68 --> 3476.38]  I can imagine that brought some more demand to the Enterprise Edition as well.
[3477.94 --> 3479.90]  But that is it for this show.
[3480.06 --> 3494.62]  Hung Lee, so much gratitude for you to come on the show and you and your team making the sacrifice to stick with it and elongate your studies and then also your financial benefits to come along with working and stuff like that.
[3494.62 --> 3508.46]  I know that it isn't always easy to see that, but on behalf of the Open Source community, I know that Jared and I want to thank you on their behalf because I know that many of us out there use Passenger, and we appreciate your sacrifice and your work in Open Source for sure.
[3509.24 --> 3514.84]  Along with that, we do want to mention a couple sponsors for this show that helped make the changelog possible.
[3514.84 --> 3520.10]  Specifically, an awesome Ruby host out of Australia, Ninefold.
[3520.68 --> 3525.60]  Good friends of ours have been waiting for an awesome Ruby show to come on, the changelog, so we can mention them.
[3525.74 --> 3527.06]  But Ninefold is super awesome.
[3527.38 --> 3531.94]  We'll put a link in the show notes about a particular deal that they're offering, changelog-only listeners.
[3532.68 --> 3534.30]  Also, our good friends over at TopTel.
[3534.42 --> 3536.00]  Love, love, love TopTel.
[3536.56 --> 3539.34]  And also, Dave's work for time tracking.
[3539.90 --> 3541.66]  Brand new tool out there, getting a lot of press.
[3541.80 --> 3543.76]  Sensible time tracking, we'll tell you a bit more about that.
[3544.84 --> 3546.22]  And the show notes as well.
[3546.42 --> 3548.14]  But again, thanks for coming on the show.
[3548.26 --> 3549.72]  And let's everybody say goodbye.
[3550.62 --> 3550.98]  Goodbye.
[3551.66 --> 3552.14]  Goodbye.
[3552.42 --> 3552.82]  Bye.
[3553.02 --> 3553.26]  Thank you.
[3553.26 --> 3553.32]  Thank you.
[3574.84 --> 3580.94]  All right, everybody.
[3580.94 --> 3581.88]  You thought the show was over.
[3581.94 --> 3582.88]  The show is not over.
[3583.06 --> 3584.38]  We have one more thing.
[3584.44 --> 3585.72]  Yes, one more thing to mention.
[3587.22 --> 3588.42]  I just can't believe it.
[3588.42 --> 3590.32]  We've got an admin panel that's being mentioned.
[3591.20 --> 3592.18]  Hanli, why don't you take it over?
[3592.28 --> 3595.16]  Tell us what's happening here with this admin panel for Passenger.
[3595.16 --> 3603.08]  Yes, so this admin panel would be a very useful tool for displaying your requests, displaying your processes.
[3603.78 --> 3610.94]  It would just make it a lot easier to see what's going on on the application and passenger level.
[3611.08 --> 3615.28]  And then you can kind of monitor your CPU and memory usage with that.
[3615.28 --> 3622.44]  And the admin panel could be used to watch your logs, to detect problems, and so forth.
[3622.52 --> 3626.48]  And it would be just a lot nicer compared to using the command line.
[3627.66 --> 3629.46]  I'm sitting here looking at some mock-ups you had here.
[3629.56 --> 3630.60]  So you can see processes.
[3631.00 --> 3633.38]  So for active processes, you can see your logs.
[3633.44 --> 3634.60]  You can see all sorts of different things.
[3635.08 --> 3636.26]  When is this going to be available?
[3636.40 --> 3637.20]  Is this coming in later?
[3637.34 --> 3637.86]  Is this as soon?
[3637.94 --> 3638.98]  Is this in process?
[3638.98 --> 3643.38]  We have not started working on it yet.
[3643.46 --> 3645.68]  It's currently on the concept level.
[3645.92 --> 3647.38]  We have just made mock-ups.
[3648.02 --> 3654.24]  The thing that we are prioritizing right now is to get Passenger 5.0 out to make it stable.
[3654.46 --> 3656.42]  And then we focus on the new features.
[3656.92 --> 3659.56]  Okay, so we're talking about what, mid this year then?
[3660.84 --> 3661.28]  2015?
[3661.58 --> 3662.64]  I believe so.
[3662.74 --> 3666.68]  I think mid this year, you can expect a first version of this.
[3666.68 --> 3667.20]  Gotcha.
[3667.46 --> 3668.92]  And we'll have you back on the change log.
[3669.00 --> 3672.30]  You get to come back and tell the listeners about this new fresh hotness.
[3672.40 --> 3674.56]  People love new fresh hotness as they've heard in this show, right?
[3674.68 --> 3676.24]  So that's what we'll do.
[3676.46 --> 3676.70]  All right.
[3677.10 --> 3679.32]  Thanks for telling us about this awesome admin panel.
[3679.38 --> 3680.28]  We can't wait to hear about it.
[3681.46 --> 3681.94]  Thank you.
[3681.94 --> 3681.98]  Thank you.
