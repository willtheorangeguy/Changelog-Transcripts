[0.00 --> 6.94]  The Change Log is brought to you by Pusher, and they're looking for a system engineer who specializes in evented systems.
[7.52 --> 15.06]  If that's you, send your GitHub profile, a cover letter, and your CV to jobs at pusher.com.
[15.56 --> 22.32]  And also use the coupon code THECHANGELOG to save 15% off your first month billing.
[22.32 --> 25.98]  Join the real-time web today at pusher.com.
[30.00 --> 44.72]  Welcome to The Change Log, episode 0.7.9.
[44.82 --> 45.88]  I'm Adam Stachowiak.
[46.24 --> 47.10]  And I'm Wynne Netherland.
[47.22 --> 48.14]  This is The Change Log.
[48.22 --> 49.68]  We cover what's fresh and new in open source.
[49.88 --> 52.74]  If you found us on iTunes, we're also up on the web at thechangelog.com.
[52.86 --> 53.68]  We're also up on GitHub.
[53.96 --> 58.72]  At thegithub.com slash explore, you'll find some trending repos, some feature repos from our blog,
[58.72 --> 60.20]  as well as the audio podcast.
[60.46 --> 62.46]  And if you're on Twitter, follow The Change Log.
[62.56 --> 63.72]  And me, Adam Stach.
[64.04 --> 66.16]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[66.66 --> 67.40]  Fun episode this week.
[67.46 --> 72.08]  Talked to the guys over at Adhesion, Ben and Ben, who on the episode you'll hear me call Ben Zero and Ben One.
[73.38 --> 73.78]  Nice.
[73.78 --> 78.46]  Just to talk through what's going on with Adhesion version 2.0
[78.46 --> 82.06]  and what they're doing with the plug-in architecture over there.
[82.46 --> 89.18]  And just a nice telephony conversation, kind of a follow-up to what we did with Chris Matthew back in the day.
[89.32 --> 90.06]  Yeah, back in the day.
[90.08 --> 91.04]  That was a good show, too.
[91.10 --> 91.64]  I know Chris.
[91.68 --> 92.16]  He's awesome.
[92.74 --> 93.14]  Yes.
[93.78 --> 98.60]  So it's just, I guess telephony is one of those things that's such a cool tool.
[98.68 --> 99.98]  I wish I had a problem to solve with it.
[100.40 --> 104.84]  Other than some Uber prank call system, I'm not sure what I would build with it, but it is super cool.
[104.84 --> 105.64]  Yeah, definitely.
[105.72 --> 111.42]  I could see small businesses tying into some of this stuff and building their own, I guess, call system.
[111.50 --> 112.02]  That's pretty neat.
[112.56 --> 119.84]  You know, if you're a 12-year-old, I think it would be the coolest thing ever to be able to build a very sophisticated, you know,
[119.98 --> 121.34]  your cow's in my garden type of ad.
[122.42 --> 122.78]  Yeah.
[123.76 --> 124.62]  Fun episode this week.
[124.66 --> 125.16]  Should we get to it?
[125.32 --> 125.92]  Let's do it.
[134.84 --> 136.48]  We're chatting today with Ben and Ben.
[136.48 --> 139.24]  Ben Langfeld and Ben Klang from Adhesion.
[139.60 --> 144.16]  So Ben Klang, why don't you introduce yourself and then we'll jump over to Ben number two.
[144.92 --> 145.12]  Sure thing.
[145.38 --> 146.44]  So my name is Ben Klang.
[146.60 --> 151.26]  I'm the founder of a company called Mojo Lingo based out of Atlanta and parts throughout the world.
[151.58 --> 157.92]  I'm actually here today in my capacity also as the Adhesion project leader, and I've been in that role for about two years now.
[158.54 --> 159.24]  And Ben?
[159.24 --> 159.32]  Ben?
[160.60 --> 161.82]  I'm Ben Langfeld.
[162.04 --> 166.78]  I'm based in the UK, and I'm an application architect for Mojo Lingo.
[167.66 --> 169.86]  As Ben said, we're distributed all over the world.
[171.04 --> 179.76]  I'm also on the core team for the Adhesion project, and I have a background in the sciences.
[181.34 --> 181.94]  Awesome.
[182.44 --> 184.66]  We did a lot of that on the previous episode.
[184.92 --> 186.96]  It's quite well received.
[186.96 --> 190.28]  And so, Ben, one, I guess I should say.
[190.80 --> 193.60]  For those that don't know Adhesion, what is it?
[193.84 --> 194.70]  What can it do for me?
[195.72 --> 196.00]  All right.
[196.10 --> 200.42]  So Adhesion is an open source framework for the creation of voice applications.
[200.96 --> 209.58]  And what I mean by that is I think we're all familiar, at least in concept, with things like Ruby on Rails or Django or other web-based development frameworks.
[209.58 --> 216.12]  And those frameworks make it possible for you to relatively quickly and painlessly develop a web application.
[216.68 --> 219.80]  And Adhesion is much the same thing except applied to the telephony domain.
[220.20 --> 227.66]  As any good framework does, it gets rid of a lot of the minutiae, the painful parts of dealing with the telephony world.
[227.66 --> 238.84]  So the framework provides things like a plug-in management system, configuration management, the ability to – sorry.
[239.84 --> 250.68]  It provides a nice clean API for developing voice applications in a way that's familiar for Ruby developers,
[250.68 --> 258.62]  and particularly those coming from Rails, and provides a whole host of integration points with various other bits and pieces of software,
[258.78 --> 265.90]  such as Rails, for example, integrating your voice prompts with a database or some web API.
[266.64 --> 275.68]  Things that are very trivial to do in Ruby can be applied to a voice application very easily.
[275.68 --> 278.92]  So we've got a bit of Ruby here on the homepage.
[280.06 --> 282.76]  So let's talk about the architecture for a moment.
[282.86 --> 285.80]  Is it just a Ruby API wrapper around some other tools?
[285.92 --> 287.28]  What's the stack look like?
[287.76 --> 289.46]  So I think that's an important distinction.
[289.66 --> 291.08]  It's not just an API.
[291.28 --> 292.92]  It is a fully featured framework.
[293.36 --> 300.08]  It provides much more than a simple library into dealing with Asterisk or Rayo or Prism or anything else.
[300.08 --> 304.78]  It's a whole environment and a way of thinking about approaching telephony problems.
[304.78 --> 310.08]  We did select Ruby as the language of choice, I think both because we like it as a language
[310.08 --> 315.60]  and also because it's very expressive and makes it relatively painless to solve these problems.
[316.16 --> 324.42]  The ability to provide a DSL that closely maps to the needs of a telephone application just enhances that experience.
[325.32 --> 326.60]  What's new in Adhesion 2.0?
[328.54 --> 330.02]  Just about everything.
[330.02 --> 336.84]  I'll go high level kind of what the bullet points for Adhesion 2 and I'll let Ben go into some of the details.
[337.84 --> 346.04]  I think the biggest, most exciting thing in Adhesion 2.0 is the fact that we've added support for not only a new telephony backend,
[346.32 --> 351.22]  but we've also made it modular so that in the future we can continue to add support for telephony backends.
[351.22 --> 358.34]  So just very briefly, the history of Adhesion was a framework for building Asterisk applications,
[358.80 --> 361.18]  Asterisk being the open source to PBX.
[362.02 --> 364.04]  And that was very powerful and went a long way.
[364.60 --> 372.66]  But obviously there are more than one way to skin a cat, and Asterisk had a lot of strengths, it also had a few weaknesses.
[372.66 --> 379.98]  So we wanted the ability to support other backends, such as cloud-based backends like Tropo,
[380.10 --> 383.82]  and also very large-scale enterprise backends with something like Prism.
[384.38 --> 392.66]  So the big thing that prompted a lot of the rework in Adhesion 2 was the ability to abstract the telephony APIs,
[393.76 --> 396.92]  the lower-level interfaces from the DSL.
[396.92 --> 401.36]  And so with Adhesion 2.0, out of the box we support Asterisk, as we always have,
[401.74 --> 408.86]  and we also support Prism, which is an enterprise-grade commercial telephony engine provided by Boxeo,
[408.94 --> 413.94]  using a new open-standard RAIO protocol, which I'm sure we'll be talking about later in this podcast.
[415.26 --> 417.34]  How portable is the DSL across those backends?
[417.42 --> 421.18]  Are you investing in a backend if you choose a particular solution?
[421.78 --> 425.60]  We really do aim to be completely portable.
[425.60 --> 430.16]  And the idea is that if you stay within sort of the sandbox, maybe not the best word,
[430.20 --> 436.64]  but if you stay within the confines of our DSL, you're guaranteed to be portable across the supported backends.
[436.96 --> 439.86]  There always will be things that each backend can do that others cannot.
[440.48 --> 445.28]  And we expose those to you, but you have to do those things consciously.
[445.74 --> 448.70]  And where there are differences in platforms, we document those.
[449.06 --> 451.36]  So really the goal is to make applications portable.
[451.46 --> 455.22]  We don't want to have you invest all that time and energy just to be locked to one backend.
[455.22 --> 456.86]  There are too many ways to do that already.
[457.24 --> 459.74]  Really the promise of Adhesion should be that you can write your application
[459.74 --> 462.44]  and then have it portable across any of our supported backends.
[464.02 --> 465.12]  So you mentioned cloud providers.
[466.14 --> 469.28]  Has that been a long time in the works or how did that come about?
[470.38 --> 477.88]  Well, our project is sponsored by Tropo, which is a leading provider of cloud-based telephony services.
[477.88 --> 480.06]  And we've worked closely with them.
[480.42 --> 489.16]  They have, in addition to Tropo, the cloud product and service, they actually sell premise versions of Tropo.
[489.24 --> 492.88]  So you can actually install this into your own data center if it's something that you wish to do.
[493.62 --> 501.68]  So we've worked closely with them to ensure that we are very compatible with the services they provide.
[501.68 --> 508.72]  One of the things that Tropo does out of the box that Asterisk can't do, for example, is very high quality text-to-speech and speech recognition.
[509.58 --> 513.34]  And Adhesion was designed to support those things if they're available.
[513.48 --> 515.52]  And certainly you can make those things available on Asterisk.
[515.60 --> 517.06]  It's just they don't come out of the box.
[517.06 --> 525.04]  So Tropo support is something, or cloud, I should say cloud support is something that we've really looked at closely with Adhesion 2,
[525.20 --> 529.06]  both the ability to run Adhesion applications in the cloud on the likes of Heroku,
[529.30 --> 532.16]  but also to be able to use cloud providers such as Tropo,
[532.70 --> 539.72]  which although I have to admit there are technical limitations today that make it not possible to run a Tropo app,
[539.72 --> 542.74]  those things will be resolved in the near future,
[543.06 --> 547.60]  and a fully cloud-deployed Adhesion telephony application will be a reality.
[548.52 --> 552.58]  Let's talk about some of the solutions, I guess, practical applications people are building with the platform.
[552.70 --> 556.34]  So I think Call Center is the one that comes to mind.
[556.44 --> 559.22]  What other solutions are you seeing people building with Adhesion?
[560.38 --> 563.98]  Well, the go-to answer would be things like IVR and Call Center.
[564.10 --> 566.38]  Those are kind of the classic telephony applications.
[566.38 --> 570.38]  And certainly there is plenty of room in that space to innovate,
[571.22 --> 575.18]  to improve the processes that those kind of users have.
[575.56 --> 581.62]  With Call Centers, for example, what we're seeing is a lot of call centers are becoming more and more distributed,
[582.06 --> 588.52]  whether they're classic call centers or just sort of applying call center techniques to the modern cloud world.
[588.64 --> 591.94]  For example, we have a client that has a dictation service,
[591.94 --> 600.76]  and the dictation service employs transcribers around the country to take recordings
[600.76 --> 603.14]  and then turn them into written documents.
[603.68 --> 609.60]  And so the application we help them build is one that collects those recordings
[609.60 --> 612.48]  and routes them to the queue to be processed.
[613.28 --> 617.94]  So theoretically, you could have a, let's say, podcast, upload an audio file,
[618.02 --> 620.98]  have it transcribed and have an ASCII version of that.
[620.98 --> 623.66]  Yes, and that is exactly what their service does.
[624.40 --> 625.78]  Might need to check into that.
[627.94 --> 628.94]  Yeah, yeah.
[629.08 --> 636.58]  It opens a lot of possibilities when you have the ability to apply a programming language that's modern
[636.58 --> 639.68]  and has libraries for everything already available.
[639.78 --> 641.06]  You're not having to reinvent the wheel.
[641.56 --> 645.18]  In fact, part of their story was they were locked into an old proprietary platform,
[645.18 --> 648.06]  and it was prohibitively expensive to make changes.
[648.06 --> 655.58]  And basically, if they didn't replace it, they were looking at not being able to continue to run the service,
[656.02 --> 657.46]  I think, in the way they had it.
[657.50 --> 660.36]  It just was not a workable solution.
[661.30 --> 667.98]  So certainly there's a huge opportunity to continue to replace legacy telephone systems
[667.98 --> 674.38]  that are not programmable, not maintainable, just not modern by every definition.
[674.94 --> 677.06]  And those are great stories to tell.
[677.66 --> 684.24]  But I have to admit, I have sort of an affinity for some of the really cool innovative stuff that this also enables.
[684.24 --> 691.38]  I think that one message we would like to get out to the world is that for a long time, telephony was kind of forgotten.
[691.58 --> 694.94]  It was sort of a painful technology to use.
[695.06 --> 698.24]  The audio quality wasn't great, and you had to memorize telephone numbers.
[698.80 --> 702.12]  There was a very limited interface between you and whoever you were calling.
[702.82 --> 704.90]  But a lot of that is changing, and it's changing very quickly.
[705.08 --> 711.48]  The likes of Skype, the likes of the WebRTC initiative to put audio into the web browsers.
[711.48 --> 716.88]  Suddenly the voice channel is just one more channel with which to communicate,
[717.14 --> 724.34]  and you can embed this into an existing web application or into an existing desktop application or whatever it may be,
[724.46 --> 730.72]  and really bring an additional rich communications channel to whatever it is you're doing.
[730.82 --> 732.50]  That's a powerful idea.
[733.18 --> 738.70]  And I do believe that we are still on the leading edge of seeing some of the really cool ideas come to market,
[738.70 --> 746.10]  that this adhesion, among many other technologies, will enable a new generation of really cool applications.
[746.10 --> 748.18]  Hey, Adam here.
[748.26 --> 752.50]  Just wanted to take a moment and thank our sponsor, Hover.com, for supporting the show.
[753.04 --> 754.98]  We certainly appreciate their support.
[755.42 --> 758.52]  Hover is by far the best place to register your domains.
[759.10 --> 764.34]  We recently took advantage of their domain concierge service, which is completely free, by the way.
[764.74 --> 768.42]  We had over 30 domains that needed to move over from GoDaddy because, you know,
[768.50 --> 771.28]  for obvious reasons why we didn't want to use them anymore.
[771.28 --> 773.84]  And Hover took care of everything.
[773.98 --> 775.34]  They took care of all the heavy lifting.
[775.48 --> 776.88]  It's this special service they have.
[777.46 --> 782.24]  It's called their domain concierge service, which basically means you don't worry.
[782.42 --> 783.54]  They do all the work.
[783.64 --> 785.06]  They move over all your domains.
[785.48 --> 792.12]  They take care of recreating your C name, your A records, your MX records for your email, everything.
[792.42 --> 794.96]  All you do is sit back and relax, and it's completely free.
[795.48 --> 797.64]  You actually talk to a human being to set it all up.
[797.70 --> 799.20]  It takes about five or ten minutes.
[799.20 --> 804.54]  You call this 800 number, 866-731-6556.
[805.42 --> 806.94]  And like I said, you talk to a human.
[807.04 --> 807.76]  They take care of you.
[807.84 --> 810.76]  They make sure that you're good to go.
[810.94 --> 812.92]  And just tell them the changelog sent you.
[813.00 --> 819.14]  Use the coupon code THECHANGELOG to save 10% on all the services that apply us to.
[819.34 --> 822.28]  We certainly appreciate their support, and thank you for trying them out.
[822.34 --> 823.36]  Hover.com.
[824.22 --> 827.02]  Well, let's talk plug-ins for a moment with Adhesion 2.0.
[827.02 --> 829.20]  What's the anatomy of an Adhesion plugin?
[831.20 --> 837.92]  So in the last release before 2.0, we had a concept called Components.
[837.92 --> 844.52]  They allowed you to do a limited set of things with regards to code reuse.
[844.84 --> 849.72]  The new plugin system is much more similar to Railties.
[850.52 --> 852.12]  A lot of people will be familiar with that.
[852.90 --> 853.02]  Sure.
[853.02 --> 859.64]  It allows you to extend the functionality of the application from within a gem dependency
[859.64 --> 866.50]  by doing such things as providing extra call controller DSR methods.
[866.80 --> 871.40]  We'll talk more about what a call controller is a little bit later.
[871.40 --> 879.58]  It allows you to do things like add rate tasks to the application, add extra configuration options
[879.58 --> 883.54]  to the central configuration system in your Adhesion application,
[884.22 --> 890.14]  and allows you to extend Adhesion to connect to various different services.
[890.14 --> 897.36]  For example, one of the plugins that we have that started off as a core feature of previous versions of Adhesion
[897.36 --> 903.50]  and is now extracted out into a plugin because we can do that now is XMPP functionality.
[904.14 --> 908.84]  So if you want to integrate your voice application with either instant messaging
[908.84 --> 919.56]  or some other more technical use case for XMPP or Java, you can do that very easily by including Adhesion XMPP
[919.56 --> 928.14]  in your application's gem file and make use of the excellent Blather XMPP gem,
[929.02 --> 936.56]  which allows you to send and receive XMPP messages and do all kinds of interesting things.
[936.56 --> 941.28]  So let's take, I guess, a step back and talk about the architecture of an application then.
[941.46 --> 946.24]  So the example on the homepage is a class of my controller,
[946.62 --> 951.84]  and people with a Rails background might think MVC when they see that.
[952.04 --> 955.46]  What are some of the similarities or differences between how you would construct
[955.46 --> 958.68]  maybe a Ruby-based web app and a Ruby-based voice app?
[959.70 --> 963.10]  So with Adhesion 2, we've introduced this concept of call controllers,
[963.10 --> 968.06]  which brings an MVC-like approach to a voice application.
[969.88 --> 975.84]  It seems strange that you would consider a telephone call to fit into MVC,
[976.34 --> 979.34]  but if you break it down in a particular way, it really does.
[980.72 --> 986.30]  If you can consider the actual phone call itself to be the view,
[986.30 --> 991.96]  you can render audible input and output to that view.
[993.08 --> 997.52]  You can capture audio from it.
[997.60 --> 1000.44]  You can manipulate it in several different ways.
[1000.58 --> 1006.58]  You can transform that view by applying combinations of other views.
[1007.64 --> 1009.20]  You can, for example, join calls together.
[1009.20 --> 1015.38]  Those actions are generally instigated by a controller,
[1015.66 --> 1020.42]  which is the call controller that you're seeing a sample of on the website.
[1021.12 --> 1027.36]  That provides you with several methods by which you can manipulate the call view.
[1028.62 --> 1031.34]  And then the vast majority of interesting Adhesion applications
[1031.34 --> 1039.96]  that we build and other people build don't stop at providing output and recording input.
[1040.16 --> 1042.80]  They integrate with some kind of data source or some kind of model
[1042.80 --> 1048.26]  that provides, for example, a dynamic menu or, for example,
[1049.02 --> 1052.48]  captures a response from a user and stores it in a database and so on.
[1052.48 --> 1060.88]  So the classic MVC pattern does approximately apply to a voice application scenario.
[1060.88 --> 1067.18]  It's not identical to the Rails-style MVC, which is not true MVC anyway.
[1068.22 --> 1068.40]  Sure.
[1069.54 --> 1072.82]  But it's that kind of approach,
[1072.90 --> 1075.96]  and it's a very useful way of thinking about it when you're building your application.
[1076.44 --> 1078.40]  There's also a concept of a router that routes.
[1078.78 --> 1079.50]  There is indeed.
[1079.50 --> 1086.00]  We have a routing DSL, which allows you to match an incoming calls, variables.
[1086.78 --> 1093.06]  Any call coming into the system will have a certain set of variables provided with it
[1093.06 --> 1100.14]  when it comes in that tell you things about, for example, the caller ID of the person
[1100.14 --> 1104.90]  who initialized the call, the method by which it got to your system,
[1104.90 --> 1110.88]  various metadata that the call is tagged with along the way across the telephone network to your system.
[1111.54 --> 1116.96]  And you can use that information combined with any information from the environment of the application
[1116.96 --> 1119.18]  at the time of the call, for example, the current time,
[1119.56 --> 1125.14]  to match against incoming calls and route them to different controllers.
[1125.14 --> 1129.76]  So, for example, it's very easy to have a route in the DSL,
[1129.82 --> 1135.86]  which says any calls coming from such-and-such call or ID can be routed in one direction.
[1136.00 --> 1141.46]  Any calls, for example, coming in outside of office hours can be routed to a voicemail system.
[1142.86 --> 1143.94]  It's very flexible.
[1144.80 --> 1149.58]  What sort of challenges are involved, I guess, in creating global applications with something like this?
[1149.58 --> 1153.70]  Any differences in telephone networks across international boundaries?
[1154.44 --> 1160.36]  As far as the details of actually connecting between networks goes,
[1160.50 --> 1163.22]  adhesion doesn't really worry about that a great deal.
[1164.74 --> 1170.52]  The issues faced in adhesion applications are normally ones of addressing.
[1170.52 --> 1180.34]  It's quite often you need to store or manipulate phone numbers in a particular way,
[1180.48 --> 1185.36]  and there are inconsistencies across the world in the way phone numbers are structured.
[1186.36 --> 1190.14]  That's a minor problem that you often come across in these kinds of applications.
[1191.58 --> 1194.06]  So if you were to localize one of these applications, I guess,
[1194.14 --> 1197.62]  to offer different language prompts based on where the call was coming from,
[1197.68 --> 1198.98]  does it offer any hooks for any of that?
[1198.98 --> 1204.46]  Currently, there is no internationalization support built into adhesion.
[1205.08 --> 1208.90]  It's a fairly simple thing to do custom in your application.
[1209.06 --> 1215.52]  That is something we have on the roadmap going forward with the two series of adhesion.
[1216.32 --> 1221.52]  The other interesting issue when you're talking about real-time interaction with the user,
[1221.66 --> 1224.90]  more so when you're making outbound calls, is time zones.
[1225.36 --> 1227.94]  We all know time zones suck in a very big way.
[1228.98 --> 1233.74]  But they suck even more when you're talking about calling people at 3 o'clock in the morning.
[1234.80 --> 1240.26]  So that is another challenge that is present in this kind of software development.
[1240.64 --> 1241.90]  But it's one that can be...
[1243.50 --> 1247.32]  You can get around it if you think about it.
[1247.32 --> 1250.70]  So you guys had adhesion conf back in October.
[1250.70 --> 1252.56]  Any plans for a follow-up?
[1253.70 --> 1254.10]  Definitely.
[1254.42 --> 1256.14]  In fact, that was the second adhesion conf.
[1256.34 --> 1257.82]  We had the first one in 2010.
[1258.30 --> 1260.24]  And 2011 was even better.
[1260.50 --> 1263.90]  It was, I would say, half again larger than the original.
[1264.08 --> 1266.20]  And we had more speakers coming from the community.
[1266.20 --> 1269.78]  I was very, very excited by the growth we had last year.
[1269.92 --> 1272.56]  And I'm hopeful that we'll get that again this year.
[1272.86 --> 1274.98]  We haven't actually really started planning.
[1275.12 --> 1278.40]  It usually happens late in the summer or possibly early in the fall.
[1278.48 --> 1281.70]  So we've been thinking about when and how that will be.
[1282.32 --> 1284.14]  But yes, definitely we'll have it again this year.
[1284.22 --> 1285.44]  And I'm looking forward to it.
[1285.44 --> 1291.98]  It actually might be interesting in that the Adhesion 2 framework, or I shouldn't say that,
[1292.04 --> 1296.90]  the Adhesion 2 roadmap was actually first revealed publicly at Adhesion Conf.
[1296.98 --> 1301.78]  There's video of Ben and myself talking about kind of the goals we wanted to achieve.
[1302.42 --> 1304.26]  And I'm pretty happy that we've...
[1304.26 --> 1307.92]  I feel like we've hit most of the goals we put into that presentation.
[1307.92 --> 1312.76]  And of course, just have that many more exciting things coming up for some of the next releases.
[1312.76 --> 1315.52]  How many people are hacking on the framework?
[1316.56 --> 1317.74]  On core itself?
[1318.60 --> 1322.68]  If you're talking about the core of the framework itself, it's not many.
[1323.68 --> 1327.72]  We have approximately 35 past contributors.
[1329.08 --> 1334.36]  As far as people using Adhesion to write applications, it's quite a lot.
[1334.36 --> 1337.68]  And it's people you wouldn't necessarily expect to be using it.
[1338.32 --> 1341.36]  For example, at the last Adhesion Conf, we had...
[1342.76 --> 1347.70]  A presentation from a gentleman who works for the security services in the United States.
[1348.60 --> 1351.50]  So the Department of Defense are using Adhesion.
[1351.76 --> 1357.74]  If it's good enough for them, then I'm sure there's a great many things that the rest of us can do with it.
[1358.36 --> 1359.34]  I'm sure they're war dialing.
[1360.04 --> 1363.34]  Actually, that was exactly his presentation was war dialing.
[1363.56 --> 1364.36]  It's funny you mention that.
[1364.36 --> 1371.46]  But actually, we also have reports that the Army was using Adhesion in the Green Zone in Iraq as part of a voice biometric system.
[1371.74 --> 1373.90]  So there are some pretty cool applications out there.
[1374.24 --> 1374.60]  Interesting.
[1374.84 --> 1380.52]  You know, it just occurs to me that we used to spend so many brain cycles trying to do prank calls back in the day.
[1380.58 --> 1385.30]  And this is like a perfect cloud-based prank calling system if you were so inclined.
[1385.62 --> 1389.16]  The average 13-year-old that knows Ruby could have a lot of fun.
[1389.16 --> 1389.82]  We try this at home.
[1390.00 --> 1391.60]  We don't condone that kind of behavior.
[1391.74 --> 1399.56]  But if you were interested in learning more about how to do that, there's a really good video actually by Nathaniel Barnes, who was the gentleman Ben was referring to.
[1399.94 --> 1401.82]  His video from Adhesion Conf is up on the web.
[1401.82 --> 1411.14]  They actually compared what they created to Metasploit, which if you're familiar with that, it's a Ruby framework for penetration testing and exploiting.
[1411.60 --> 1413.90]  And it's an interesting comparison.
[1414.28 --> 1423.12]  But yeah, his presentation had all kinds of really, really interesting details from the field, hypothetically, theoretically, on how you might do that.
[1423.50 --> 1424.94]  If one was not constrained by law.
[1424.94 --> 1432.36]  I first came across Adhesion Astrix, I guess about three, maybe four years ago.
[1432.44 --> 1433.10]  I'm trying to remember.
[1433.22 --> 1436.66]  It's been a while at a local regional Ruby conference.
[1436.84 --> 1447.86]  And it seems like back then, to kick the tires on this thing, the first thing people did was had a home install, you know, where they had their own menu-based phone answering program at the house.
[1448.16 --> 1450.96]  Have you guys so deployed one at home?
[1451.74 --> 1452.74]  I have in the past.
[1452.74 --> 1453.78]  I don't still have one.
[1453.78 --> 1456.40]  It's a nice introduction.
[1458.70 --> 1462.88]  We do similar things with corporate voice networks these days.
[1464.90 --> 1469.96]  And for example, our entire internal phone system is powered by Adhesion.
[1472.66 --> 1474.72]  So it's something that we do.
[1476.34 --> 1483.24]  And I certainly, I'm sure Ben has done something similar, have gone down the home voice system route.
[1483.24 --> 1485.12]  But it's something that wears off a little bit quickly.
[1486.78 --> 1494.96]  Yeah, I definitely have had over the years many different deployments of Astrix or other telephone things in my house.
[1494.96 --> 1500.44]  And pretty much it got to the point where I needed to maintain the PBX for the business.
[1500.76 --> 1502.56]  And so that's where all my effort goes.
[1502.74 --> 1509.20]  And my home phone line is actually, it's just a special phone hanging off the business PBX.
[1509.20 --> 1516.48]  But there's really, with the quality of bandwidth today, there's really no need for me to run my own AstroSense at home.
[1516.58 --> 1520.46]  It's really easy just to hang it off the work PBX.
[1520.46 --> 1535.84]  Even if you weren't someone who had their own work PBX that was available, the rise in the hosted PBX market has really, I think, shown the flexibility, the relative inexpensive.
[1535.84 --> 1540.26]  It's just not hard to manage phone systems that way.
[1540.40 --> 1542.92]  That's really, to me, it's the obvious choice.
[1543.00 --> 1548.84]  I mean, who wants to pay for the initial hardware and also the cost of maintaining a phone system anymore?
[1549.20 --> 1552.74]  Unless it's something you specialize in doing, it's just not something you want to take on yourself.
[1552.74 --> 1558.14]  In just a short time, we've seen it go from voice to XMPP and SMS.
[1559.18 --> 1564.30]  Any plans for video or other adapters that you could see coming into this sort of architecture?
[1565.00 --> 1565.38]  Definitely.
[1565.72 --> 1567.78]  I mean, video is something that everybody's excited about.
[1568.32 --> 1570.70]  But it's also one of those things that's sort of easier said than done.
[1572.08 --> 1578.74]  Adhesion as a project, theoretically today, could do much of...
[1578.74 --> 1583.82]  Really, from Adhesion's perspective, a video call is not that different from a voice call.
[1584.56 --> 1586.84]  The limitation is the underlying platform.
[1587.82 --> 1590.24]  Today, Asterisk does have video support.
[1590.70 --> 1595.48]  It has relatively good video support when you're talking about placing a direct call from party to party.
[1595.86 --> 1599.38]  It has a very limited video bridge.
[1599.38 --> 1603.24]  And I say limited in the sense that you can have multiple people in a conference.
[1603.82 --> 1609.48]  And you can either have it so the video is fixed so that one person is always on video broadcasting to other participants.
[1609.74 --> 1611.08]  You can think of that like a lecture mode.
[1611.38 --> 1613.38]  It also has a mode where you can...
[1613.38 --> 1614.42]  It'll follow the active speaker.
[1614.58 --> 1618.02]  So based on who's talking, that video stream will be fed to all the participants.
[1618.02 --> 1628.78]  What it doesn't do, and mostly for reasons of both complexity of code as well as complexity of CPU complexity and load on the server,
[1629.58 --> 1632.76]  it does not make any attempt to mix the video.
[1632.92 --> 1634.06]  So it doesn't try to transcode.
[1634.20 --> 1638.94]  It doesn't try to do what's called the Brady Bunch effect where you have...
[1638.94 --> 1641.40]  If you have nine people in a conference, you have nine faces tiled.
[1642.16 --> 1643.66]  Those things don't happen.
[1644.64 --> 1646.86]  So that is a limiting factor for video.
[1646.86 --> 1651.12]  So other platforms, in fact, such as Prism, have no video support at all.
[1652.10 --> 1654.10]  So definitely we would like to approach it.
[1654.18 --> 1659.26]  But I think that the technology there needs to evolve a bit more before it's actually useful.
[1659.70 --> 1667.78]  As far as adhesion is concerned, a lot of these challenges, as Ben says, are pushed down to the layer of the platform that adhesion is driving.
[1668.18 --> 1672.16]  It's important to note that adhesion does not, for example, process any audio.
[1672.16 --> 1680.32]  Adhesion is a third-party control layer on top of the VoIP platform of your choice.
[1680.32 --> 1686.14]  So we don't need to worry about any of the heavy lifting of transcoding video, etc.
[1686.38 --> 1688.54]  That is all done for us.
[1688.90 --> 1696.76]  And once the platform does those things appropriately, it will not be too difficult for us to drive it.
[1696.76 --> 1701.66]  In a way, very similar to how we do voice right now.
[1703.20 --> 1709.54]  So in some of the installations that you guys have been a part of in the PBX systems, what are some of the menu options?
[1709.74 --> 1712.44]  Are you doing purely audio and touchstone-based menu options?
[1712.56 --> 1718.30]  Or are you pulling the information back into dedicated displays on phones and things of that sort?
[1718.30 --> 1721.84]  Or the visual voicemail style of app?
[1722.32 --> 1725.96]  You know, there are so many uses for telephone systems.
[1726.08 --> 1727.08]  We have done IVR.
[1727.24 --> 1729.58]  It's really not something that we do a lot of.
[1730.70 --> 1732.66]  There are companies that specialize in IVR.
[1732.88 --> 1735.54]  I mean, it's that big of a field, I suppose.
[1737.16 --> 1742.12]  A lot of our work has been on kind of non-traditional applications.
[1742.12 --> 1746.34]  So, for example, we have a client, Palmling, that's on the Tropo platform.
[1746.96 --> 1748.84]  And their service is about connecting.
[1750.32 --> 1758.24]  If you're traveling in a foreign country and you need help translating in that language, you can call into their platform.
[1758.54 --> 1764.80]  And it will find someone in their network who speaks the right language and connect you so that they can help you translate the call.
[1765.08 --> 1765.34]  Oh, nice.
[1765.78 --> 1767.00]  Yeah, it's a really cool idea.
[1767.10 --> 1768.42]  And it's a great service.
[1769.92 --> 1770.98]  And congrats to them.
[1770.98 --> 1772.38]  They launched not too long ago.
[1773.72 --> 1778.80]  But my point in telling that story, as far as your question goes, there is an IVR there.
[1779.00 --> 1780.28]  But it's relatively basic.
[1780.58 --> 1787.28]  The main function of the IVR is to authenticate the caller to make sure that they're a registered subscriber with an active account.
[1788.04 --> 1791.68]  And to as quickly as possible get them out of the IVR and get them talking to a translator.
[1791.82 --> 1793.80]  Because that's really the problem they want solved.
[1794.46 --> 1796.06]  And it's sort of a Zen-like thing.
[1796.20 --> 1797.70]  The less IVR you need, the better.
[1797.70 --> 1808.38]  I think the broader question was looking at multiple interface modes around a call.
[1808.38 --> 1811.08]  We have developed applications.
[1811.92 --> 1815.12]  Most of them are still in development.
[1815.60 --> 1817.80]  And we can't talk in too much detail about them.
[1818.26 --> 1828.04]  But we have applications which combine a web browser, a mobile app, a voice call, instant messaging, etc.
[1828.04 --> 1836.66]  Where you have multiple modes of communication with the application simultaneously.
[1837.66 --> 1843.60]  So you may have a conference call and a text conference.
[1844.38 --> 1847.58]  Similar to how you may do a Skype conference call.
[1847.58 --> 1853.32]  But in ways that are very flexible across devices.
[1855.18 --> 1859.64]  So imagine if one of those participants could be a cell phone and another one is a desktop application.
[1860.22 --> 1863.14]  And that you don't have to worry too much about the capabilities of each channel.
[1863.70 --> 1867.38]  Sort of like the idea of progressive enhancement with the web or graceful degradation.
[1867.74 --> 1872.58]  You present to each channel the best of its capabilities and everybody participates at their own level.
[1872.58 --> 1878.18]  So when you guys aren't hacking on Adhesion, what's in your open source radar?
[1878.34 --> 1880.70]  What is out there that you just can't wait to play with?
[1882.20 --> 1883.78]  So I'll go for that first.
[1885.08 --> 1888.00]  I'm very invested in XMPP.
[1888.66 --> 1893.56]  In fact, the RIO protocol that we've been talking about is an XMPP extension.
[1893.56 --> 1910.16]  It allows Adhesion to connect as an XMPP resource and communicate with the voice backend over a protocol that is fit for the web.
[1911.44 --> 1913.00]  That's a major enhancement.
[1913.00 --> 1928.88]  I maintain, along with its original author, Jeff Smick, the Blather XMPP library, which allows you to build quite advanced software that makes use of XMPP.
[1929.08 --> 1931.28]  For example, a bot.
[1933.84 --> 1936.08]  Everybody when he's 17 builds an IRC bot.
[1937.20 --> 1938.70]  You can do the same thing with XMPP.
[1938.70 --> 1943.60]  You can integrate with Google Talk, for example, which is XMPP-based.
[1945.28 --> 1947.12]  I do a lot of work in that arena.
[1947.58 --> 1948.84]  That interests me.
[1949.52 --> 1950.92]  XMPP seems to be everywhere.
[1951.32 --> 1958.70]  We at work use HipChat for our group chat, and I think that's one of the biggest selling points is that you can bring any XMPP client along and connect.
[1958.70 --> 1958.98]  Exactly.
[1959.64 --> 1960.50]  It's open.
[1960.70 --> 1961.46]  It's federated.
[1962.12 --> 1963.14]  It's very flexible.
[1963.54 --> 1967.96]  And it can be used not only for user-facing things, but it can be used for internal infrastructure as well.
[1968.70 --> 1972.78]  XMPP PubSub is a fantastic queuing mechanism, for example.
[1974.12 --> 1975.16]  And it's a proven technology.
[1975.48 --> 1977.52]  Ben kind of mentioned the federated nature of it.
[1977.60 --> 1983.02]  I mean, it's an awesome way to not reinvent the wheel, is a good way to say it.
[1983.04 --> 1986.40]  But a lot of services that you might not even realize are being built on XMPP.
[1986.40 --> 1993.88]  To my understanding, Apple's iMessage, which is the new sort of SMS replacement they have that's XMPP-based, as is Facebook chat.
[1994.44 --> 2001.36]  Now, the degree to which you can access it with external clients kind of varies, but just the fact that those things are running on XMPP is good for the entire community.
[2001.36 --> 2007.44]  A great deal of messaging systems are built on XMPP without you knowing it.
[2007.64 --> 2008.66]  As Ben said, iMessage.
[2010.18 --> 2011.78]  And WhatsApp is another one.
[2012.18 --> 2014.46]  That's an entirely XMPP-based network.
[2015.22 --> 2019.32]  A lot of people are using it who you might not necessarily know about using it.
[2019.50 --> 2025.18]  But it's a fantastic protocol that, quite frankly, more people should know about.
[2025.18 --> 2029.02]  What's the most interesting project that you've built with Blather?
[2031.38 --> 2034.62]  I think the most interesting one is probably one that I can't really talk about.
[2037.00 --> 2046.28]  I guess the most interesting topical one would be the library that Adhesion now uses to communicate with the VoIP backend.
[2047.82 --> 2049.58]  As Ben said, we've made everything modular.
[2049.58 --> 2061.44]  We now have a middleware library called Punchblock, which sits in between Adhesion and the voice platform and makes them all appear under a consistent API.
[2063.14 --> 2070.10]  That uses Blather and XMPP to drive a RIO server, for example, VoxAerPRISM.
[2070.96 --> 2077.20]  That's had some unique challenges and was very interesting to put together.
[2077.20 --> 2081.30]  There's some things we've done there that we might not do again.
[2081.42 --> 2083.48]  Some things we've done there that are quite fantastic.
[2085.06 --> 2089.84]  Altogether, a very interesting use case for XMPP that has absolutely nothing to do with instant messaging.
[2090.92 --> 2095.40]  So since you can't talk about your day job at MI6, let's talk about your background in the sciences.
[2095.58 --> 2099.42]  So let someone think that it's just a broad da Vinci stroke there.
[2099.70 --> 2101.78]  What sort of sciences have you dabbled in?
[2101.78 --> 2107.14]  So I did a physics degree as an undergrad.
[2108.40 --> 2110.42]  That was actually only a few years ago.
[2112.64 --> 2121.46]  I do some work casually with a friend of mine who does a PhD in astro seismology.
[2121.46 --> 2134.30]  And I use or have encouraged him to and helped him to use Ruby to infiltrate a world that is full of Fortran and IDL and other nonsense.
[2135.60 --> 2148.54]  So I've been playing my limited part in expanding the horizons of the British scientific community to include such a fantastic language as Ruby.
[2148.54 --> 2156.30]  So did you come into computing as just a love for computing or just out of necessity to do something more valuable and this was a means to an end?
[2156.74 --> 2160.30]  I've always been interested in communications problems.
[2160.30 --> 2174.46]  And I came to the work that I'm doing now with Ruby and more or less all of my software engineering work that I've done from that angle.
[2175.46 --> 2180.74]  I did a lot of work while I was doing my degree with the university radio station.
[2180.74 --> 2188.14]  And there were some interesting problems to solve there with regards to communication when you don't have a multimillion pound budget to buy commercial systems.
[2188.88 --> 2199.16]  And so that's actually what brought me to Adhesion, building a flexible phone system for a very specialized use case, a radio studio.
[2200.46 --> 2202.76]  And actually Adhesion fit that very well.
[2204.04 --> 2205.18]  Ben Zero, what's your background?
[2205.18 --> 2207.92]  My background is systems.
[2208.28 --> 2210.62]  So I started actually in high school.
[2210.78 --> 2215.64]  I took sort of random jobs as a systems administrator.
[2215.98 --> 2218.86]  And I spent the next 10 years doing all things system.
[2219.66 --> 2228.56]  I did a lot of work consulting on, believe it or not, PeopleSoft as an architect, figuring out how many networks and how many servers and how much storage you would need.
[2229.12 --> 2232.58]  So I still have a love for the operational side of things.
[2232.58 --> 2235.96]  And actually, I came to telephony almost by accident.
[2236.12 --> 2237.56]  My father-in-law had a startup.
[2237.82 --> 2246.08]  He got royally upset at AT&T one day for canceling a service that he liked, which today is fairly commonplace, but then was really not.
[2246.20 --> 2248.90]  It's the classic follow me where you have a phone number.
[2249.04 --> 2249.42]  You call in.
[2249.66 --> 2250.68]  Google Voice does this.
[2250.76 --> 2254.74]  You call into it and it calls your cell phone, your home phone, and you can take the call wherever.
[2255.28 --> 2256.64]  This was back in 2002.
[2257.76 --> 2260.16]  Asterisk had not actually reached version 1.0.
[2260.16 --> 2264.48]  Everyone who was running Asterisk had to check it out from CVS and compile it and run it.
[2265.34 --> 2266.14]  And so, yeah.
[2266.28 --> 2270.46]  So we kind of tried to start a business offering follow me services.
[2271.38 --> 2276.86]  That part didn't go so well, but definitely got me hooked on telephony and the possibilities there.
[2276.86 --> 2287.30]  And so as I exited the systems admin world, I was looking for something to do, you know, because I wanted to start a company.
[2287.76 --> 2288.80]  And telephony was really interesting.
[2288.92 --> 2297.98]  And it was kind of the case of right place, right time, especially as far as the Adhesion project was concerned, as the former maintainer was sort of on his way out.
[2297.98 --> 2303.22]  And so I stepped into that role and it's just been a fantastic, fantastic ride since then.
[2304.30 --> 2305.58]  So I'll put you on the spot.
[2305.78 --> 2307.16]  Either one of you have a programming hero?
[2308.74 --> 2309.84]  I think Ben's my hero.
[2311.54 --> 2313.34]  Yeah, I have.
[2314.10 --> 2314.88]  Well, thank you, Ben.
[2314.88 --> 2326.44]  I have several people whose work that has benefited me, some of those that I've taken over projects from.
[2327.88 --> 2335.58]  Jeff Smick, who was the original author of Blather, has done some pretty cool stuff.
[2335.58 --> 2347.84]  There's a few people doing very interesting stuff around concurrency in Ruby, which is not a pretty subject in some cases.
[2348.74 --> 2353.70]  I've been wanting to get the celluloid project on the audio.
[2353.96 --> 2356.26]  I can talk to you a little bit about celluloid.
[2357.54 --> 2358.60]  Adhesion uses it.
[2359.40 --> 2359.92]  Oh, yeah.
[2360.72 --> 2361.00]  Yeah.
[2361.14 --> 2361.94]  I've never seen that now.
[2361.94 --> 2369.90]  Tony has put together a fantastic framework that looks and smells a lot like Erlang, but without the yuckiness.
[2372.10 --> 2373.42]  That's so good in the show notes.
[2375.14 --> 2377.72]  Mike Perham has done a lot of interesting stuff.
[2379.88 --> 2384.76]  Yeah, there's some pretty cool guys out there doing interesting things with concurrency on Ruby.
[2384.76 --> 2398.38]  I'd also like to point out Charles Nutter and the guys working on JRuby for really doing, I think, some important work to bring Ruby to an entirely different audience and to an entirely different scale.
[2399.22 --> 2400.58]  That's a really cool project.
[2401.36 --> 2401.72]  Absolutely.
[2402.62 --> 2407.04]  Well, thanks, guys, for joining us and talking to us a bit more about Adhesion 2.0.
[2407.10 --> 2410.66]  It's a fun project, and I think I'll be dabbling in this myself.
[2411.66 --> 2412.04]  Fantastic.
[2412.04 --> 2412.84]  Glad to hear it.
[2414.76 --> 2415.76]  Thank you.
