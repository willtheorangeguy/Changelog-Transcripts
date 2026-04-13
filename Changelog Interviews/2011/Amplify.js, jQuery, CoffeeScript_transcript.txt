[0.00 --> 18.14]  Welcome to the ChangeLog episode 0.5.7.
[18.48 --> 19.42]  I'm Adam Stachowiak.
[19.68 --> 20.60]  And I'm Wynne Netherland.
[20.78 --> 21.78]  This is the ChangeLog.
[21.84 --> 23.52]  We cover what's fresh and new in open source.
[24.02 --> 27.02]  If you found us on iTunes, we're also on the web at thechangelog.com.
[27.12 --> 28.08]  We're also up on GitHub.
[28.08 --> 30.04]  Head to github.com slash explore.
[30.14 --> 34.34]  You'll find some trending repos, some feature repos from the blog, as well as our audio podcasts.
[34.72 --> 37.22]  If you're on Twitter, follow ChangeLog Show and me, Adam Stach.
[37.92 --> 40.42]  And I'm Penguin, P-E-N-G-W-Y-N-N.
[40.90 --> 42.60]  This episode is sponsored by GitHub Jobs.
[42.68 --> 45.12]  Head to the changelog.com slash jobs to get started.
[45.44 --> 50.58]  If you like us to feature your job on this show, select advertise on the ChangeLog when posting your job, and we'll take care of the rest.
[51.56 --> 56.26]  Big Bang Technologies looking for a desktop class web application design engineer.
[56.26 --> 61.08]  And for those that don't know, desktop class web applications are web apps that feel like they belong on the iPad.
[61.84 --> 65.46]  If you know how to write a fairly large, complex SQL query, check your code into Git.
[65.90 --> 69.62]  Have a few open source projects and understand the value of social coding on GitHub.
[69.78 --> 71.58]  You're a perfect fit for Big Bang technology.
[71.82 --> 73.36]  You have an awesome compensation package.
[73.86 --> 79.82]  And if you're in Toronto, Ontario looking for a full-time gig, check out lg.gd slash AA.
[80.28 --> 83.10]  Because they're probably looking for you, and you're probably looking for them.
[83.10 --> 85.62]  Next up is ELC Technologies.
[85.76 --> 87.56]  They have a full-time position in Portland, Oregon.
[88.26 --> 90.00]  Telecommuting is also an available option.
[90.16 --> 94.00]  They're looking for Ruby and Ruby on Rails devs with strong problem-solving skills.
[94.54 --> 96.74]  At least one year experience in building web apps.
[97.06 --> 101.62]  So if you're proficient with Ruby, Rails, or mobile development, and you know what the cloud is,
[102.06 --> 105.02]  maybe even have an understanding of what something should be put into an API,
[105.78 --> 107.82]  and how to leverage existing ones to make your life easier,
[107.82 --> 111.02]  check out lg.gd slash AB for more details.
[111.02 --> 112.80]  Fun episode this week.
[112.88 --> 117.62]  Talk to the guys over at Appin2 about Amplify.js, their new JavaScript framework.
[118.06 --> 119.58]  That kind of complements jQuery.
[120.06 --> 122.44]  Has no hard and fast jQuery requirements anymore,
[122.60 --> 127.36]  but kind of a slimmed-down version of Backbone, perhaps in certain respects.
[127.46 --> 128.68]  But it does look pretty cool.
[128.74 --> 129.44]  I'm going to check it out.
[130.40 --> 131.14]  That sounds exciting.
[132.02 --> 135.16]  Speaking of exciting, we just got back from RedDirt RubyConf.
[135.62 --> 137.68]  Great week up there in Oklahoma City.
[137.68 --> 143.64]  I did it live on, I guess, Thursday over the interwebs, if a few of you caught that.
[143.72 --> 149.72]  We'll be posting that audio in a couple of future episodes with Nick Caranto from Jump Cutter
[149.72 --> 151.66]  and Wesley Berry from Thought.
[152.62 --> 155.04]  I missed that show, but I heard it was really awesome.
[155.72 --> 156.42]  It is cool.
[156.60 --> 158.22]  It was such a cool venue up there.
[158.28 --> 163.64]  If you ever have a chance to get up to Oklahoma City to go to anything that Derek Parkhurst and those guys put together,
[163.64 --> 168.12]  it was really good, James Edward Gray II was a great host.
[168.30 --> 173.58]  We just had fun talking with Dr. Nick and Aaron Patterson and a lot of Ruby folk up there.
[173.72 --> 176.16]  But a lot of JavaScript at this conference, too.
[176.34 --> 178.84]  So kind of right up our alley for the changelog.
[179.08 --> 180.28]  I thought it was the Ruby conference.
[180.94 --> 181.30]  I know.
[181.42 --> 189.42]  Dr. Nick pretty much lambasted us there in his keynote talking about why we're having so much JavaScript at a Ruby conference.
[189.72 --> 192.20]  But it was fun times to be had, for sure.
[192.72 --> 193.28]  Good stuff.
[193.64 --> 194.80]  Speaking of, should we get to it?
[195.30 --> 195.88]  Let's do it.
[204.94 --> 210.94]  We're chatting today with Mike Hostetler and Scott Gonzalez from Append2 to talk about Amplify.js.
[211.22 --> 217.54]  But before we begin, Mike, why don't you introduce yourself, your role at Append2, and then we'll let you introduce yourself, Scott.
[218.84 --> 220.48]  My name is Mike Hostetler.
[220.48 --> 223.52]  I'm the founder and CEO of Append2.
[223.52 --> 230.90]  We're the company dedicated to jQuery and supporting the jQuery community through a variety of business services.
[231.22 --> 235.46]  We currently focus on training, development, and support.
[235.46 --> 245.16]  So we offer on-site and remote training to companies that are interested in sort of improving their skills with jQuery.
[245.84 --> 251.70]  With our development, we do a number of architecture reviews and performance reviews and Kickstarter projects.
[251.70 --> 264.60]  So we'll participate on a team and help get that team up to speed with either putting together the architecture of a project through a prototype and then handing it over to the team to finish out.
[264.60 --> 272.14]  But we really focus on some cutting edge and pushing the boundaries of what you can do with jQuery.
[272.64 --> 282.94]  And then we also offer corporate support contracts to those who are interested in just getting that extra – they know who they can call.
[283.32 --> 284.24]  So that's what we do.
[285.12 --> 285.42]  Scott?
[285.42 --> 285.50]  Scott?
[286.94 --> 288.00]  I'm Scott Gonzalez.
[288.22 --> 293.44]  I am an architect at Append2, and I'm one of the development leads for jQuery UI.
[294.10 --> 301.50]  And I spend almost all of my time at Append2 working on open source projects, so working on jQuery UI and working on Amplify,
[302.34 --> 309.16]  working on some smaller projects that we have, and occasionally working on client projects.
[309.80 --> 312.40]  We'll jump into jQuery and jQuery UI, I'm sure, in a moment.
[312.40 --> 314.50]  But what's the elevator pitch for Amplify?
[315.28 --> 320.30]  So Amplify is a set of components for solving common web application problems.
[320.94 --> 331.78]  So basically, as we work on client projects at Append2, if we run into a problem over and over, we recognize that there is something consistent here,
[331.92 --> 336.88]  and we try and find a solution that works elegantly across all of our projects.
[336.88 --> 342.92]  So that's the goal for Amplify is to just solve the problems that we're commonly hitting.
[343.74 --> 352.20]  So it's nothing like solving some niche problem or trying to be really, really clever about a solution.
[352.44 --> 358.80]  We try and make something as simple as we can to solve some kind of common problem that we're facing
[358.80 --> 360.62]  and probably many other people are facing.
[360.62 --> 362.98]  So let's talk specifics for a moment.
[363.06 --> 364.22]  I'm looking at the documentation site.
[364.32 --> 365.90]  See, request, store, and PubSub.
[366.00 --> 367.20]  What's this all about?
[367.68 --> 376.00]  So request separates out making a request and actually – so asking for data from a request
[376.00 --> 379.14]  and actually making that request, like actually going and getting the data.
[379.14 --> 385.84]  And the reason that's important to us is because we're frequently working with companies
[385.84 --> 390.00]  where we're writing all the client-side code and they're writing all the server-side code.
[390.94 --> 396.30]  So when we have to integrate with the server-side code, you know, if we're calling into a service,
[397.06 --> 400.02]  that service may or may not be built yet, right?
[400.02 --> 407.16]  And so we want to separate out the fact that we want to call into the service
[407.16 --> 409.44]  and how we actually call into the service.
[409.80 --> 413.68]  So, you know, if we say, you know, we need to get a list of movies,
[414.36 --> 419.96]  we don't really care, as the person asking for the movies, how we got that list of movies.
[421.38 --> 429.26]  So we separate out the actual request from the actual implementation of the request.
[430.02 --> 436.36]  And that way, if the server-side implementation changes or if we want to mock out the implementation
[436.36 --> 442.08]  because the server-side code's not written yet, the front-end code doesn't actually change, right?
[442.08 --> 446.76]  Like the code that says, go give me a list of movies and I'll handle that list when it comes back to me
[446.76 --> 453.44]  stays the same regardless of how many times we change the implementation of how do we actually get those movies.
[454.62 --> 457.62]  So that's the main thing that request does.
[457.62 --> 464.98]  It also handles things like if the services return data wrapped in some kind of envelope, you know,
[465.02 --> 475.40]  so it says the status was successful or error, the request object can decode that and return just the actual data.
[475.86 --> 481.92]  And it can also determine that even though it was, you know, an HTTP 200, that it was actually an error,
[481.92 --> 488.40]  which lots of services do, pretty much all the popular services always return a status code of 200.
[488.66 --> 491.60]  And then they tell you some other way that there was an error.
[492.14 --> 498.92]  So with amplify.request, you can actually say, you know, here's my success callback, here's my error callback,
[498.92 --> 501.64]  and then here's a function that decodes it.
[501.84 --> 506.56]  But as the person asking for the data, you're not specifying how it gets decoded.
[506.66 --> 512.38]  As the person implementing how that request works, you define the way that it gets decoded.
[512.60 --> 516.52]  So again, like it's abstracting away all the details for you.
[516.52 --> 526.50]  So I see on the options that you can pass into this thing so that XHR, the XHR object, the XMLHTB request object can be specified.
[526.66 --> 531.60]  So does this mean that you're decoupled from jQuery's transport and can use any transport you want?
[532.32 --> 532.76]  Yeah.
[532.88 --> 538.28]  So when you define a request, you define the type of request.
[538.42 --> 541.40]  So AJAX requests are just one type of request that we support.
[542.12 --> 545.54]  We don't have built-in support for anything else yet.
[545.54 --> 551.42]  We do want to have AJAX polling and something to normalize across different types of streaming data.
[551.66 --> 557.20]  So like WebSockets, you know, and then if WebSockets are not available, maybe you fall back to AJAX polling.
[557.44 --> 564.24]  But the API that's exposed to you as the user of that request looks exactly the same.
[565.78 --> 572.50]  You can also do requests that are just functions, but the API is exactly the same for the person making the request,
[572.50 --> 577.58]  regardless of, you know, the fact that the request is just a function or it's an AJAX request.
[579.22 --> 587.08]  So, you know, we're really trying to just completely separate the fact from I'm making a request for data,
[587.08 --> 596.54]  and this request for data is handled in a specific way because we want to have the flexibility to change how that part's implemented
[596.54 --> 601.30]  and not have to ever worry about going back and changing something else.
[602.80 --> 607.64]  So in the same way that requests, abstracts, transport and decoding, network requests,
[607.82 --> 614.14]  I assume store abstracts the same thing for local storage and different mechanisms for persisting data?
[614.14 --> 622.08]  Yeah, so store is a layer on top of any synchronous web storage system,
[622.32 --> 624.48]  any synchronous persistent web storage system.
[624.82 --> 630.44]  So that's basically what local storage is, but older browsers don't have local storage.
[631.36 --> 634.58]  So, you know, in older versions of Firefox, you have global storage.
[634.70 --> 636.74]  In older versions of IE, you have user data.
[636.74 --> 641.26]  So it handles all of that.
[641.36 --> 644.90]  It figures out what's actually available, and it just uses that.
[645.60 --> 650.20]  And it also adds in expiration, which none of these systems have.
[650.86 --> 655.72]  So you can store something in local storage and say this is only valid for, you know, 10 seconds.
[656.28 --> 659.92]  And then if you try and get that data, it'll be there for 10 seconds.
[659.92 --> 663.26]  But if you try it, you know, 11 seconds later, it'll be gone.
[664.12 --> 666.84]  So that's a nice feature that it adds.
[667.24 --> 672.88]  And then the main thing it does is just abstracts away the fact that, you know,
[672.98 --> 676.34]  there are differences in how browsers implement persistent storage.
[676.74 --> 680.34]  There's also support for session storage, though it never defaults to that.
[680.90 --> 684.96]  So you can specify which storage system you want to use.
[684.96 --> 689.32]  Generally, that's really only useful right now for session storage.
[690.00 --> 693.70]  You know, if you explicitly want to use global storage, you can do that.
[693.92 --> 698.84]  But that would be a strange thing to do since it only works in, you know, specific browsers.
[699.24 --> 704.52]  And if you needed to use that because local storage didn't exist, it would already default to that anyway.
[705.68 --> 708.92]  But you do have the ability to specify which storage you want.
[708.92 --> 712.74]  And you can also change the default storage system.
[712.74 --> 717.50]  So by default, it figures out, you know, what's the best available system.
[717.68 --> 718.82]  I'm going to use that.
[719.30 --> 723.62]  But you can change which one it defaults to if you just go through Amplify.store.
[724.14 --> 728.12]  And then you can also add additional storage systems if you want.
[728.12 --> 732.80]  So the latest big piece or the last big piece is PubSub.
[733.04 --> 742.08]  So for the developer that maybe their eyes gloss over when they see live and delegate and ad event listener and now PubSub with subscriptions,
[742.54 --> 747.98]  what's the use case and benefit of a PubSub architecture, especially on the client end?
[747.98 --> 756.38]  The thing that you normally hear people talk about is performance and how PubSub is more performant than events.
[757.34 --> 760.16]  That's not the reason that we built a PubSub system.
[760.38 --> 763.16]  We haven't actually run into performance issues.
[763.16 --> 769.96]  We generally end up using custom events in jQuery to do our communication.
[770.34 --> 777.52]  But with the request module, we wanted to publish messages similar to jQuery's AJAX events.
[777.64 --> 780.50]  It's like before and after events.
[780.76 --> 785.48]  So you can hook into that and do things like, you know, a loading indicator during a request.
[785.48 --> 790.88]  But in order to do that, we were going to publish custom events.
[792.00 --> 796.34]  But then we got into a debate about should we publish custom events on the document?
[796.48 --> 798.86]  Should we publish custom events on an object?
[799.12 --> 802.26]  If we're going to do it on an object, should we publish them directly on the Amplify object?
[803.22 --> 812.48]  And we knew from experience that a lot of users get confused when you use jQuery to wrap objects instead of DOM elements.
[812.48 --> 816.50]  And then they get even more confused when you're triggering events on objects.
[816.90 --> 823.60]  So we decided that building a PubSub system would be easier for most people to understand exactly what's happening.
[824.44 --> 827.70]  And so that's the main reason that we decided to build a PubSub system.
[828.68 --> 832.38]  Then the reason we decided to build one, sort of just take an existing one,
[832.96 --> 840.80]  is because we wanted to keep it as small as possible while adding features that we would like to have in events,
[840.80 --> 845.98]  like the ability to specify an order when you're binding an event.
[846.26 --> 849.96]  So it's not too uncommon that you bind an event and you say,
[850.06 --> 854.50]  I really wish I could get this to be the first event handler that runs.
[855.08 --> 857.74]  But there's no clean way to do that with events.
[858.92 --> 865.06]  So with the PubSub system and Amplify, we added a priority option when you had a subscription.
[865.06 --> 871.44]  So when you subscribe to a message, you can say, you know, I want to have a priority of 1.
[872.32 --> 876.70]  And the lower your priority, the higher in the run order you are.
[877.22 --> 881.12]  So the subscriptions default to a priority of 10.
[881.24 --> 887.10]  So if you go to a priority of 11, you'll run after anything that's bound without specifying a priority.
[887.10 --> 894.48]  And if you specify a priority of 9, you'll run before any other handler that runs without a priority.
[895.46 --> 900.92]  So we did that so we could build the caching layers for Amplify requests
[900.92 --> 903.42]  and make sure that they run at the very beginning.
[904.76 --> 908.36]  So up front it says Amplify is a jQuery component library.
[908.54 --> 911.92]  What actual dependencies are on jQuery?
[911.92 --> 918.02]  When we started building it, we said, you know, we use jQuery on every project.
[918.64 --> 920.80]  A lot of people use jQuery on their projects.
[921.52 --> 926.36]  We'll just have jQuery as a dependency since we always have it available anyway.
[927.16 --> 930.92]  That lets us do things like not have to worry about, you know,
[931.58 --> 935.96]  utility methods like .each or .extend or, you know, is function.
[936.80 --> 938.30]  So we started with that.
[938.30 --> 944.56]  And for the most part, outside of AJAX requests in the request module,
[944.98 --> 947.08]  that's really all we used it for.
[947.22 --> 951.10]  And the decision, again, was only because it's always available to us.
[951.44 --> 954.34]  Why write small utilities like that again?
[957.16 --> 962.52]  After we released the alpha, we got some feedback from a bunch of people saying,
[962.62 --> 966.40]  you know, this stuff looks really cool, but I don't like the fact that there's a jQuery dependency.
[966.40 --> 971.66]  So because we were only using it for simple things, we decided to take, you know,
[971.72 --> 978.42]  the tiny file size hit and remove the jQuery dependency for everything except AJAX requests.
[978.98 --> 985.40]  So the PubSub system and Amplify store both have no dependencies now.
[985.92 --> 990.34]  So store doesn't even depend on Amplify core, which only contains PubSub.
[990.34 --> 994.40]  And then request depends on Amplify core for the PubSub.
[995.10 --> 998.34]  And then if you want to use the AJAX request, it depends on jQuery as well.
[998.80 --> 1001.12]  And we support jQuery 1.4 and higher.
[1002.86 --> 1006.90]  The reason I ask is, you know, Append2 is kind of positioning itself as, you know,
[1007.50 --> 1010.78]  a company that supports the jQuery community.
[1010.78 --> 1018.14]  So, Mike, what's it mean to develop in shops that have such a heavy jQuery dependency?
[1018.32 --> 1023.80]  Are you finding that you're educating people on jQuery or just as much educating them in JavaScript?
[1024.70 --> 1027.50]  We found ourselves doing a little bit of both.
[1028.00 --> 1032.70]  Oftentimes when we get invited into a company to train their staff on jQuery
[1032.70 --> 1036.70]  or to do a jQuery-based architecture review,
[1037.24 --> 1044.40]  they will have adopted jQuery and know that they want to kind of go down this path
[1044.40 --> 1046.68]  of building something with the front end.
[1047.16 --> 1051.02]  But they often confuse JavaScript with jQuery.
[1051.32 --> 1055.92]  So we start by trying to give them a firm foundation in the JavaScript language.
[1056.98 --> 1058.94]  A lot of our training is geared that way.
[1058.94 --> 1064.94]  I mean, we even have training courses that just talk over the basic HTTP interaction.
[1065.40 --> 1067.40]  You know, what happens in a browser?
[1067.58 --> 1068.54]  What is strict mode?
[1068.66 --> 1069.48]  What is ES?
[1070.14 --> 1071.06]  What is ECMAScript?
[1071.42 --> 1074.90]  You know, they aren't aware of all that.
[1074.98 --> 1079.50]  So we build off of that and then get them up to the place where they can be productive
[1079.50 --> 1084.22]  because it's the thing that they're most interested in, us helping them with,
[1084.64 --> 1087.54]  is the ability to become productive as fast as possible.
[1087.54 --> 1101.38]  So we do focus on jQuery, but when we get those opportunities,
[1101.82 --> 1107.74]  we do as much as we can to help them round out their entire front end knowledge,
[1108.30 --> 1112.46]  including JavaScript, HTML5, you know, all the latest stuff,
[1112.46 --> 1119.88]  while getting them productive and helping their team develop really good quality code
[1119.88 --> 1122.16]  in a short amount of time.
[1124.06 --> 1127.74]  So I'm looking at Amplify, and it's a really lightweight framework
[1127.74 --> 1132.10]  meant to complement jQuery, which is a much larger framework.
[1132.20 --> 1135.88]  But I'm not sure if you guys have seen the, I guess, the debate in the last couple of days
[1135.88 --> 1144.68]  between Yehuda Katz and Thomas Fuchs from Sproutcore and Prototype and now Zeptofame, respectively.
[1145.08 --> 1150.42]  Talking about these big monolithic frameworks, which I guess Sprout would be more in that category,
[1150.58 --> 1152.36]  Sproutcore, Cappuccino, things of that sort,
[1152.36 --> 1157.96]  and these smaller frameworks like Zeptofame, and then now Ender,
[1158.20 --> 1160.68]  that kind of stitches together smaller frameworks.
[1162.12 --> 1168.10]  What's your take on the, I guess, that spectrum of monolithic versus surgical?
[1170.66 --> 1173.84]  So I had this debate with a few people.
[1174.96 --> 1179.08]  I think it's really just, you know, do you buy into the Linux model or not?
[1179.08 --> 1184.34]  Right. You've got these people following the Linux model where you've got a tool
[1184.34 --> 1186.28]  that solves a problem and it solves it well.
[1187.00 --> 1190.00]  And if you need to solve larger problems that contain many small problems,
[1190.08 --> 1194.06]  you get many small programs together and you glue them together however you need to.
[1195.88 --> 1200.18]  There's definitely a place for that, and there's a place for, you know,
[1200.28 --> 1203.52]  I've got a framework that tells me exactly how to glue those things together,
[1203.52 --> 1205.20]  and it's already glued them together for me.
[1205.20 --> 1208.96]  I don't think one is right or wrong.
[1210.02 --> 1213.64]  You know, it really depends on what you're trying to do, who's on your team.
[1214.82 --> 1219.08]  So we tend to take the approach of, you know,
[1219.12 --> 1223.54]  take the little tools that solve specific problems
[1223.54 --> 1226.48]  and use them however you see fit.
[1226.48 --> 1232.52]  But, you know, that doesn't mean that that's better or worse for any specific,
[1233.16 --> 1234.16]  well, just in general.
[1234.30 --> 1238.20]  For a specific project, it may be the right or wrong choice.
[1239.32 --> 1243.18]  But that's generally how we solve problems.
[1243.18 --> 1249.98]  So how much of Amplify has been extracted out of real-world working code?
[1251.90 --> 1255.38]  Well, it's all based on real-world working code,
[1255.72 --> 1259.10]  and, you know, then we go and use it in our project.
[1259.26 --> 1262.10]  So, like I said, we encounter a problem in a project,
[1262.34 --> 1264.58]  and we solve the problem in that project.
[1264.58 --> 1267.60]  If we encounter the problem in another project,
[1268.30 --> 1274.86]  we may or may not take the existing solution from the other project, right?
[1274.90 --> 1279.28]  So there's one thing we don't want to do is solve a problem once
[1279.28 --> 1281.50]  and decide that that's how we're always going to solve it.
[1282.24 --> 1288.84]  And so the idea behind Amplify has existed for a long time.
[1288.84 --> 1295.06]  The actual code that we're shipping has not existed for as long as, you know,
[1295.16 --> 1296.70]  we've been solving these problems.
[1297.16 --> 1299.64]  We've solved the problems over and over,
[1299.84 --> 1302.84]  and we go back and we look and we say, you know,
[1302.94 --> 1304.66]  this is how we solved it in this application.
[1305.34 --> 1307.50]  Why did we solve it differently in a different application?
[1308.28 --> 1315.18]  And we want to find something that works cleanly in both applications, right?
[1315.18 --> 1319.60]  So if you're designing something for a specific application,
[1320.02 --> 1325.00]  you may not build the most useful general purpose tool.
[1325.58 --> 1329.94]  So if you build something that's just the most useful general purpose tool,
[1330.06 --> 1333.80]  it may not solve specific problems the best way.
[1334.90 --> 1338.32]  So, you know, we've been trying to take a careful balance about that,
[1338.36 --> 1340.50]  and that's why we're not solving large problems.
[1340.50 --> 1346.52]  We're finding specific problems that occur everywhere and trying to solve those as best we can.
[1346.62 --> 1349.94]  So that way we can drop them into the applications, right?
[1349.98 --> 1354.88]  And so that's why we're not in that build one monolithic framework mindset,
[1355.12 --> 1358.70]  because once you do that, we feel that you generally end up,
[1359.84 --> 1361.42]  you may solve all your problems,
[1361.64 --> 1366.16]  but you may not solve them the way that you like to solve them the best.
[1366.16 --> 1368.86]  I would completely agree with that,
[1368.98 --> 1374.94]  and that really underscores the approach we've taken.
[1376.12 --> 1378.46]  We've, in building our own projects,
[1378.72 --> 1383.80]  have seen that there's really a lot out there to solve the problems we need to solve,
[1384.34 --> 1389.30]  but it's a matter of kind of piecing it together
[1389.30 --> 1394.02]  and focusing in on how to solve it the best
[1394.02 --> 1399.30]  and amplify as an attempt to fill in a few holes a little bit.
[1399.86 --> 1401.72]  There's, you know, there's a lot of other problems,
[1401.86 --> 1404.52]  but we wanted to focus and do something really, really well.
[1405.54 --> 1409.02]  And from the other side, I, and kind of this debate going on,
[1409.16 --> 1413.30]  I completely understand the argument for a large monolithic framework,
[1414.30 --> 1416.98]  really kind of from a marketing and branding perspective.
[1416.98 --> 1424.18]  In my discussions, and we've gone in and talked with clients,
[1424.62 --> 1430.30]  there's a comfort level in adopting just one name with one version number.
[1431.20 --> 1434.74]  And we completely understand that,
[1434.92 --> 1437.50]  but we kind of hold to our technical approach.
[1438.16 --> 1444.78]  So we're currently talking internally about ways that we could help companies solve that
[1444.78 --> 1450.92]  because they're starting to realize that there's more to the JavaScript world than just jQuery itself.
[1451.92 --> 1460.22]  And they're looking for solutions for, you know, packaging and pulling in other things besides jQuery.
[1460.78 --> 1467.52]  So it's something we're very interested in and working on.
[1467.52 --> 1475.68]  So what's the breakdown of companies that you support or that you consult with as far as their backend stacks?
[1475.80 --> 1481.82]  How much of them are Microsoft versus Python or Ruby or other frameworks?
[1482.36 --> 1486.58]  You know, the majority of it has been more of the enterprise, Java and Microsoft.
[1486.58 --> 1493.40]  A lot of the open source hackers run on either Ruby or Python, PHP.
[1494.44 --> 1496.92]  There's a little bit of that, but not as much.
[1498.20 --> 1502.74]  Part of that, I think, is due to just the way they approach development.
[1503.74 --> 1512.68]  And in our kind of work, we've noticed that a lot of backend developers approach the frontend from a backend perspective.
[1512.68 --> 1520.16]  And we've, as a company, made the decision when we founded to approach it from a frontend perspective
[1520.16 --> 1527.56]  and to really try to shed new light on the way that we were solving these problems and building these applications.
[1529.04 --> 1535.30]  And the place we've gotten the most traction with that has been in kind of the big enterprise world
[1535.30 --> 1540.98]  where they are trying to build big, exciting things.
[1541.38 --> 1547.22]  And they kind of see where it's broken down.
[1547.48 --> 1555.08]  We often come in and we'll do a review and kind of expose and have a conversation about, you know,
[1555.66 --> 1558.46]  you should have done this differently.
[1558.78 --> 1560.42]  You know, we can help with that sort of thing.
[1560.42 --> 1565.20]  And then we just start there and help them not only learn how to do it better,
[1565.32 --> 1568.00]  but show them, write some code, guide them.
[1568.72 --> 1572.42]  So I would say it's mostly on the enterprise side.
[1572.92 --> 1575.48]  So in my former life, I was actually a .NET developer.
[1575.60 --> 1582.04]  So I think I can speak with a little experience around what you're saying there around approaching it from a backend perspective.
[1582.04 --> 1589.40]  The page state and the view state and they tried to turn the web in the early days of ASP.NET,
[1589.48 --> 1593.22]  turn it into more visual basic form load programming model,
[1593.34 --> 1599.90]  which kind of is just against, I guess, the architecture and the nature of the web.
[1601.48 --> 1604.34]  Even going as far as the early Atlas project,
[1604.44 --> 1608.62]  kind of ported the CLR light all the way down to JavaScript, right?
[1608.62 --> 1613.72]  What have you seen now that they've kind of shifted course and adopted jQuery?
[1613.98 --> 1620.68]  Has Microsoft done to really embrace the nature of the web with their backend technologies?
[1621.32 --> 1623.80]  So I've seen a couple of things.
[1625.16 --> 1630.90]  The first thing is I really am personally impressed.
[1631.06 --> 1637.24]  I don't come from a Microsoft background of how much they're participating in the conversation.
[1637.24 --> 1645.64]  That, to me, that conversation is as important as the technology itself
[1645.64 --> 1650.44]  because the community of web developers,
[1650.78 --> 1652.96]  and maybe just throw out all the backends,
[1653.26 --> 1657.54]  there's really a tight community where we all push each other forward
[1657.54 --> 1660.50]  and it's a conversation to make the web better
[1660.50 --> 1662.64]  because that's what we're passionate about.
[1662.64 --> 1667.56]  And that makes a huge difference.
[1669.00 --> 1673.98]  Secondly, we've seen a lot of really interesting stuff coming out of Redmond
[1673.98 --> 1677.74]  and just their guidance, their participation in that question
[1677.74 --> 1684.26]  and what they're trying to do to, number one, provide the tooling support,
[1684.26 --> 1692.16]  but provide the guidance for all of the people that follow kind of the .NET backend,
[1692.42 --> 1695.32]  the Microsoft way for how to do it right.
[1696.12 --> 1699.68]  And, you know, they, again, going back to the conversation,
[1699.86 --> 1704.82]  they acknowledge that, you know, it's a process to find that right solution,
[1704.82 --> 1710.52]  but just it's important to have the conversation, to take feedback, to continue working on it.
[1710.58 --> 1716.38]  And we've seen a lot of really cool advances with the Visual Studio platform
[1716.38 --> 1721.50]  through, like, just VS Doc support for IntelliSense.
[1721.68 --> 1725.66]  I mean, little things, but they're putting effort behind it.
[1725.66 --> 1736.54]  The Nuget packaging system where you can now pull down different pieces of jQuery UI.
[1736.54 --> 1738.84]  And, again, it's a funny fundamental little thing,
[1738.98 --> 1746.96]  but we kind of take for granted the fact that jQuery UI is several different pieces
[1746.96 --> 1753.54]  that build up that kind of toolkit where so often people pull it down wholesale
[1753.54 --> 1757.50]  or a backend project will pull it in.
[1757.90 --> 1759.38]  It is just jQuery UI.
[1759.62 --> 1761.28]  Well, why would you want to do anything else?
[1761.38 --> 1764.00]  Well, they end up using just an accordion
[1764.00 --> 1769.68]  and pushing a lot of extra code to the browser,
[1769.92 --> 1771.12]  and that just doesn't work.
[1771.40 --> 1776.36]  So Damian Edwards on the MVC team
[1776.36 --> 1780.52]  recently packaged up all of the different jQuery UI components
[1780.52 --> 1783.28]  separately into their Nuget packaging system.
[1783.28 --> 1787.42]  So if you want to use an accordion, you just pull down an accordion,
[1787.54 --> 1789.28]  and it'll pull down the dependencies correctly
[1789.28 --> 1791.32]  and make your page more efficient.
[1791.76 --> 1797.24]  You know, little things like that show a real commitment to get the details right,
[1797.64 --> 1802.88]  and we've been happy to kind of participate with them in that conversation
[1802.88 --> 1804.12]  and help out where we can.
[1804.12 --> 1808.18]  So you guys are friends also with Nathan Smith,
[1808.32 --> 1810.38]  who I affectionately call the 960 guy,
[1810.50 --> 1812.42]  but I think he bristles at that now.
[1812.64 --> 1814.44]  I'll call him JavaScript extraordinaire.
[1815.46 --> 1818.88]  He's got just as much JavaScript as he does CSS.
[1819.12 --> 1821.26]  Once, he's kind of asking a baited question.
[1821.34 --> 1825.56]  He wants me to ask your take on Rails now,
[1825.68 --> 1828.12]  including CoffeeScript by default, M3.1.
[1828.12 --> 1833.74]  So that, I think, is very interesting.
[1835.08 --> 1836.42]  Actually, it's funny.
[1836.80 --> 1839.78]  We're at a conference,
[1840.04 --> 1844.04]  and yesterday I actually asked Douglas Crockford
[1844.04 --> 1845.38]  what he thought of CoffeeScript,
[1845.54 --> 1850.62]  and there was a panel with a couple of the other people
[1850.62 --> 1852.52]  who worked on the ES5 spec,
[1853.58 --> 1857.90]  and just talking through their process of language design
[1857.90 --> 1861.46]  and what place something like CoffeeScript has
[1861.46 --> 1863.06]  in the JavaScript ecosystem.
[1864.08 --> 1867.10]  And it was really a fascinating conversation,
[1867.56 --> 1870.70]  and I was actually surprised
[1870.70 --> 1873.56]  that they all loved the idea of CoffeeScript
[1873.56 --> 1876.26]  and different dialects of JavaScript
[1876.26 --> 1878.56]  being built on top of JavaScript.
[1878.56 --> 1881.62]  There's obviously a downside of a compile step
[1881.62 --> 1884.32]  when it comes to tooling and debugging,
[1885.12 --> 1892.56]  but the real win is making that barrier to entry lower
[1892.56 --> 1898.02]  and just making a very tight, robust, obvious way
[1898.02 --> 1900.98]  to get in and develop with JavaScript
[1900.98 --> 1904.20]  that is sort of a gateway drug.
[1904.34 --> 1907.96]  I mean, JavaScript, everybody's consensus has been
[1907.96 --> 1909.62]  and it's going to become
[1909.62 --> 1912.64]  or has become the most ubiquitous programming language out there.
[1913.10 --> 1915.58]  And it's now our job as developers
[1915.58 --> 1922.06]  to make it easy for people to kind of dip their toes in,
[1922.16 --> 1924.24]  but to understand the power of the language
[1924.24 --> 1927.18]  because it's no longer a scripting language.
[1927.18 --> 1934.10]  And JavaScript, we've really experienced it,
[1934.16 --> 1938.80]  and part of our goal and mission is to just help people ease into it,
[1938.96 --> 1940.70]  but to give it the respect it deserves
[1940.70 --> 1945.56]  to help clients and customers understand
[1945.56 --> 1949.10]  that this really is an important language.
[1949.10 --> 1950.48]  You can do a lot with it,
[1950.48 --> 1958.34]  and you can really just build amazing applications with it.
[1958.78 --> 1961.82]  So, you know, I think,
[1962.32 --> 1966.08]  well, CoffeeScript's an acquired taste, definitely.
[1966.78 --> 1968.78]  And I wouldn't set out writing CoffeeScript
[1968.78 --> 1971.20]  if you don't really understand JavaScript going in the same way
[1971.20 --> 1973.12]  that I wouldn't want to write SAS
[1973.12 --> 1975.52]  without firmly grasping CSS.
[1975.52 --> 1978.32]  But once you do, there's incredible power
[1978.32 --> 1979.64]  in just some of the language features
[1979.64 --> 1981.78]  that you can do with CoffeeScript.
[1981.86 --> 1984.88]  But one of the things that I love about using CoffeeScript
[1984.88 --> 1986.82]  is the Cake compiler.
[1987.06 --> 1988.08]  I come from a Ruby background,
[1988.48 --> 1991.26]  and so, you know, it's like Rake or Make,
[1991.74 --> 1992.76]  except in CoffeeScript.
[1992.86 --> 1995.30]  So now I can compile a lot of scripts,
[1995.50 --> 1998.16]  even surgically, from a lot of different namespaces
[1998.16 --> 2000.10]  across, you know, 10 or 12 different files
[2000.10 --> 2004.56]  to really keep my concerns separated as I'm coding,
[2004.56 --> 2006.30]  but they get compiled down to one JavaScript
[2006.30 --> 2009.28]  that I can send down to the mobile device
[2009.28 --> 2011.98]  or into the browser, which is really cool.
[2013.66 --> 2016.40]  So what are you guys doing as far as package management?
[2016.64 --> 2020.52]  If you're dealing just with the front-end layer
[2020.52 --> 2022.76]  as you consult in these projects,
[2022.84 --> 2024.28]  and every back-end tends to be different,
[2024.36 --> 2026.62]  what are folks using maybe in the .NET world
[2026.62 --> 2028.78]  or some of the other stacks that you see
[2028.78 --> 2030.38]  to package up and compile
[2030.38 --> 2033.38]  and serve up the JavaScript in their projects?
[2033.38 --> 2035.64]  We haven't done a lot with that,
[2036.04 --> 2037.12]  with package management.
[2037.80 --> 2039.40]  There's a lot of different aspects
[2039.40 --> 2040.54]  to package management.
[2042.30 --> 2044.98]  We've, on the front end,
[2047.34 --> 2049.38]  a lot of what we end up doing
[2049.38 --> 2051.16]  is just including what we need to
[2051.16 --> 2056.52]  and using a script loader of some sort.
[2062.20 --> 2065.28]  We've seen kind of the .NET world embrace Nuget,
[2065.62 --> 2067.88]  which is, we really think is a great thing,
[2068.00 --> 2070.00]  but again, that's more of a back-end thing.
[2070.40 --> 2074.80]  We're very familiar with the CommonJS package spec,
[2074.80 --> 2078.96]  and we've embraced that as much as it makes sense.
[2079.50 --> 2081.74]  But that's, again, it's not so much front-end.
[2083.08 --> 2086.84]  So, yeah, there's just,
[2088.32 --> 2090.80]  in what we do in focusing on the front-end,
[2090.96 --> 2093.78]  we don't end up running into that problem.
[2094.34 --> 2097.00]  That problem does exist with our projects,
[2097.04 --> 2098.36]  but we let others solve it
[2098.36 --> 2101.00]  because it's very particular to their environment.
[2101.00 --> 2102.36]  That's definitely the way to do it.
[2102.44 --> 2105.08]  So we've got two long-running drinking games
[2105.08 --> 2105.56]  on this show.
[2105.62 --> 2107.36]  I'm not sure if you've caught any of the episodes,
[2107.54 --> 2110.08]  but every time that we say Hamlin Sass or Node.js,
[2110.20 --> 2111.02]  people have to take a drink.
[2111.26 --> 2112.62]  So cheers, audience.
[2113.36 --> 2114.96]  So I can't talk about JavaScript
[2114.96 --> 2115.92]  and not talk about Node.
[2116.02 --> 2118.96]  It's one of those things that is just taking fire.
[2119.22 --> 2121.92]  So given that you guys love JavaScript
[2121.92 --> 2124.38]  and you code JavaScript as your primary focus,
[2125.04 --> 2127.06]  have you done anything with Node on the back-end?
[2127.06 --> 2132.02]  So we, as yet, have not had a client project
[2132.02 --> 2133.76]  where we've worked with Node on the back-end.
[2134.22 --> 2138.64]  We have really fallen in love with it
[2138.64 --> 2141.12]  for some internal tooling.
[2141.40 --> 2143.14]  So we've been experimenting there.
[2144.56 --> 2147.10]  It's, again, fits very well
[2147.10 --> 2150.46]  into kind of our areas of expertise.
[2150.46 --> 2154.36]  We have, amidst, you know,
[2154.40 --> 2157.80]  having a lot of experience with JavaScript,
[2158.80 --> 2162.14]  one of the kind of competencies in the company
[2162.14 --> 2163.22]  is infrastructure
[2163.22 --> 2167.84]  and a background in system administration.
[2169.42 --> 2171.64]  I, myself, and Jonathan
[2171.64 --> 2173.64]  worked for quite a while
[2173.64 --> 2175.46]  on the jQuery.com infrastructure
[2175.46 --> 2177.84]  and scaling that out,
[2177.92 --> 2179.46]  all of the things involved there.
[2180.16 --> 2182.84]  And we see just great things,
[2183.58 --> 2186.60]  great potential for Node on the server side
[2186.60 --> 2188.02]  and JavaScript on the server side.
[2188.74 --> 2191.18]  And so we're just kind of experimenting.
[2191.72 --> 2193.64]  We'll see where it goes.
[2193.78 --> 2195.84]  We don't have any big plans right now.
[2196.18 --> 2197.90]  We're just using it where it makes sense.
[2197.90 --> 2201.70]  We've, we'll have little projects
[2201.70 --> 2202.60]  that may come out.
[2203.02 --> 2206.10]  We host, publish a lot of our little projects
[2206.10 --> 2207.96]  on code.append2.com
[2207.96 --> 2210.66]  if you'd ever like to look at kind of
[2210.66 --> 2212.96]  some of the more experimental things
[2212.96 --> 2213.98]  that we're working on.
[2215.66 --> 2218.20]  So we're, we don't have any big plans for it.
[2218.32 --> 2221.62]  We're, again, kind of following our mission
[2221.62 --> 2224.62]  of partnering with companies
[2224.62 --> 2226.72]  who are looking to solve these problems.
[2227.90 --> 2230.24]  And helping them solve it.
[2230.54 --> 2232.36]  So we're dipping our toes in
[2232.36 --> 2233.74]  and we'll see where it goes.
[2234.40 --> 2235.42]  So we were chatting earlier
[2235.42 --> 2236.98]  before we got on the air
[2236.98 --> 2238.94]  about some other efforts
[2238.94 --> 2240.16]  that you guys have around,
[2240.52 --> 2242.04]  I'm not sure if certification
[2242.04 --> 2243.00]  is too strong of a word,
[2243.12 --> 2245.42]  but some training that you guys provide
[2245.42 --> 2248.36]  for those that may be coming to JavaScript
[2248.36 --> 2250.54]  just from the influx of jQuery
[2250.54 --> 2252.16]  into the Microsoft world.
[2252.34 --> 2253.20]  So what are you guys doing
[2253.20 --> 2256.34]  to help foster a knowledge of JavaScript?
[2256.34 --> 2257.34]  Sure.
[2258.58 --> 2259.96]  So we have,
[2260.34 --> 2262.16]  our one big initiative right now
[2262.16 --> 2264.00]  is the, our Learn site.
[2264.54 --> 2267.32]  So we, in Boston,
[2267.80 --> 2270.00]  back last October
[2270.00 --> 2271.68]  at the jQuery Boston Conference,
[2272.28 --> 2275.28]  committed to training 10,000 web developers
[2275.28 --> 2277.42]  and open sourcing our training material.
[2277.68 --> 2279.70]  We're on the verge of doing that.
[2279.70 --> 2282.16]  And we had,
[2282.58 --> 2286.02]  last year, 2010 was a great year.
[2286.02 --> 2289.86]  We, the company was kind of getting off the ground,
[2289.98 --> 2292.24]  but we realized that we were falling far short
[2292.24 --> 2293.66]  of the need that was out there
[2293.66 --> 2295.90]  to really train people well
[2295.90 --> 2299.70]  on a lot of either JavaScript or jQuery.
[2299.70 --> 2303.18]  and so we realized
[2303.18 --> 2306.04]  that we had to kind of think outside the box
[2306.04 --> 2307.38]  and that's what this is.
[2307.78 --> 2309.34]  So we've packaged up
[2309.34 --> 2312.40]  and we've, we've actually taken our training material,
[2312.52 --> 2315.08]  which most of it had existed in Keynote files,
[2315.44 --> 2320.98]  and packaged it into Markdown
[2320.98 --> 2322.90]  using HTML5 slide,
[2323.10 --> 2324.90]  slideshow system.
[2324.90 --> 2326.58]  We've done screencasts.
[2326.66 --> 2329.12]  We've kind of put together this package of content
[2329.12 --> 2332.08]  and then we'll be publishing these lessons
[2332.08 --> 2333.30]  onto a website.
[2334.32 --> 2336.74]  And the lessons will be organized into courses
[2336.74 --> 2339.08]  where you can go through like a JavaScript
[2339.08 --> 2340.90]  or jQuery 101 course.
[2341.86 --> 2342.56]  And then once you're,
[2342.76 --> 2344.32]  once you've completed that course,
[2344.58 --> 2346.98]  then students would have the opportunity
[2346.98 --> 2349.86]  to mark that they've completed that course.
[2349.86 --> 2354.96]  and they'll be given a transcript.
[2355.30 --> 2355.60]  Now, I mean,
[2355.72 --> 2357.54]  that's kind of the first version of it.
[2357.58 --> 2358.86]  We've got some other ideas
[2358.86 --> 2360.16]  that are baking about
[2360.16 --> 2361.70]  how to make that a little bit more authentic
[2361.70 --> 2363.18]  because you could just go market.
[2363.32 --> 2364.16]  Oh, sure, I know this.
[2364.24 --> 2365.42]  But it's a start.
[2365.66 --> 2366.66]  Again, we're kind of agile
[2366.66 --> 2368.00]  in the way we release things.
[2368.94 --> 2370.50]  And, but with the,
[2370.66 --> 2372.42]  really the goal is that we,
[2372.56 --> 2375.72]  we want to help people
[2375.72 --> 2377.78]  learn this content the right way.
[2377.78 --> 2381.88]  And we've put a lot of time and effort
[2381.88 --> 2385.06]  into making sure that the quality of the content
[2385.06 --> 2386.70]  is the best.
[2387.66 --> 2390.30]  And we're really committed to that.
[2390.46 --> 2393.08]  And so the actual content itself
[2393.08 --> 2393.90]  will be on GitHub.
[2394.58 --> 2395.56]  We'll, you know,
[2395.58 --> 2396.96]  be able to take pull requests
[2396.96 --> 2401.42]  and participate in allowing the community
[2401.42 --> 2403.42]  a path to help us improve.
[2403.42 --> 2408.88]  But in addition to give students a way
[2408.88 --> 2410.88]  that they know kind of what they're getting.
[2411.78 --> 2416.14]  And it's, we're really excited about it.
[2416.28 --> 2418.42]  Well, that'll be released soon.
[2419.02 --> 2419.04]  So.
[2419.36 --> 2420.52]  So one last question,
[2420.60 --> 2423.72]  since you deal with so many Microsoft clients
[2423.72 --> 2425.82]  and probably have a closer relationship
[2425.82 --> 2427.92]  with Microsoft through their jQuery adoption.
[2427.92 --> 2430.78]  What's the state of open source
[2430.78 --> 2432.08]  in the Microsoft world?
[2432.56 --> 2434.56]  I mean, you guys are focused on open source.
[2434.68 --> 2435.84]  There's code.apendu.com
[2435.84 --> 2437.50]  where you've got some open source projects out there.
[2437.60 --> 2439.20]  jQuery itself is open source.
[2440.16 --> 2442.60]  Where is the vibrant community
[2442.60 --> 2444.72]  of .NET open source?
[2449.66 --> 2450.96]  That's a hard question to answer.
[2451.06 --> 2452.72]  I'm not quite sure how to answer that question.
[2452.72 --> 2458.26]  I'm, I think the concept of open source
[2458.26 --> 2460.32]  in Microsoft is gaining speed.
[2462.40 --> 2465.80]  There's really in kind of the web technologies,
[2466.34 --> 2469.96]  it's really getting some traction.
[2470.20 --> 2474.24]  I wouldn't know quite where to say the focus of it is
[2474.24 --> 2475.72]  or where to go look.
[2476.34 --> 2482.48]  But it's definitely gaining some traction.
[2482.48 --> 2485.94]  And they, I would say the biggest thing I've realized
[2485.94 --> 2487.32]  with working with Microsoft
[2487.32 --> 2489.48]  is that organizationally,
[2490.64 --> 2491.88]  they're beginning to,
[2493.56 --> 2498.70]  well, the people that we've worked with are great.
[2498.88 --> 2502.98]  They're, I, like I said,
[2503.02 --> 2504.32]  don't come from a Microsoft background
[2504.32 --> 2505.90]  and have been thoroughly impressed.
[2506.42 --> 2509.86]  And frankly, my perception of the company
[2509.86 --> 2511.16]  has completely changed.
[2511.16 --> 2513.22]  I mean, I was, you know,
[2514.04 --> 2516.18]  right up there with IE6 Must Die
[2516.18 --> 2518.40]  and, oh, down with Microsoft.
[2518.68 --> 2519.80]  But that's, I would say,
[2520.08 --> 2522.50]  I've really, in working with them professionally,
[2523.24 --> 2525.04]  I have a tremendous respect
[2525.04 --> 2527.06]  for everybody that works there.
[2527.62 --> 2530.12]  We were hanging out with the IE19 last night
[2530.12 --> 2532.60]  and now IE10.
[2533.32 --> 2534.80]  That was announced this week.
[2534.80 --> 2536.76]  And it's, they're just,
[2536.88 --> 2538.30]  they're very committed to what they do.
[2538.40 --> 2539.72]  They're very smart people.
[2539.72 --> 2544.80]  And it's been just a real pleasure
[2544.80 --> 2550.00]  to see Microsoft really push open source adoption.
[2550.82 --> 2552.36]  And then with the jQuery project,
[2552.76 --> 2559.06]  they have impressively just let jQuery lead the effort
[2559.06 --> 2563.62]  because they trust in the process
[2563.62 --> 2565.90]  is kind of my perception of it.
[2566.28 --> 2569.04]  And that's really impressive to me.
[2569.12 --> 2570.92]  I think the moment I realized that
[2570.92 --> 2574.36]  as we were on a call through the jQuery project
[2574.36 --> 2578.16]  with one of the Microsoft lawyers to just,
[2578.16 --> 2580.60]  we were talking about some copyright issues.
[2580.60 --> 2589.14]  And the conversation was just,
[2589.32 --> 2593.22]  they were, you know, very, very open.
[2593.70 --> 2595.12]  And it was just, it was impressive.
[2595.32 --> 2597.08]  My perception of the company
[2597.08 --> 2599.16]  entirely changed during that conversation.
[2599.42 --> 2602.44]  So I would say there's a really exciting future
[2602.44 --> 2604.12]  for Microsoft and open source.
[2605.14 --> 2606.76]  We're doing what we can
[2606.76 --> 2608.52]  to help participate in that conversation.
[2608.52 --> 2613.04]  And I think that's really what I would ask
[2613.04 --> 2614.60]  all the other web developers to do
[2614.60 --> 2616.98]  is just to really participate in the conversation.
[2617.32 --> 2618.98]  They're committed to getting it right.
[2619.90 --> 2623.54]  And yeah, it's exciting to have another,
[2624.86 --> 2627.92]  have all of that extra effort kind of in the community.
[2629.68 --> 2632.74]  Well, I know you guys are traveling out West,
[2633.10 --> 2635.48]  hitting some conferences as we speak.
[2635.56 --> 2636.84]  So it was hard to catch up with you guys,
[2636.84 --> 2639.16]  but where can folks that want to learn more about Append2
[2639.16 --> 2640.40]  catch up with you in person?
[2642.86 --> 2646.30]  So we'll be at the jQuery conference this weekend
[2646.30 --> 2647.18]  in Mountain View.
[2648.58 --> 2654.74]  Past that, we are planning to hit Big Omaha in May
[2654.74 --> 2657.74]  and then have a couple of other conferences.
[2658.30 --> 2661.04]  We'll be just doing various events.
[2661.04 --> 2666.00]  You can follow us at append2.com
[2666.00 --> 2669.52]  and there's links to the team's Twitter pages.
[2670.42 --> 2671.56]  A lot goes out on Twitter
[2671.56 --> 2675.64]  and we have a list of kind of what events we'll be at.
[2676.20 --> 2678.78]  So I would say definitely go look at append2.com.
[2679.56 --> 2679.72]  Great.
[2679.80 --> 2682.40]  Well, thanks for taking the time to join us today.
[2682.56 --> 2684.56]  We'll look forward to seeing what becomes of Amplify.
[2685.36 --> 2686.10]  Thanks so much.
[2686.10 --> 2716.08]  We'll be right back.
