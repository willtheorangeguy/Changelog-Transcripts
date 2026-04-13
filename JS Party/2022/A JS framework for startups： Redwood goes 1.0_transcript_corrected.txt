[0.00 → 18.78] Redwood, the technology can be this really amazing combination with the investing that I do and the advising of startups. I spent a lot of time talking to founders and as an entrepreneur, I really enjoy giving back in that way of helping people succeed in trying new things.
[18.78 → 32.78] What we say for Redwood is we want to help more startups explore more territory more quickly. And that's both via the technology, the framework, and the community and helping you accomplish those explorations.
[32.78 → 58.36] This episode is brought to you by our friends at Retool. Retool helps teams focus on product development and customer value, not building and maintaining internal tools. It's a low-code platform built specifically for developers. No more UI libraries, no more hacking together data sources, and no more worrying about access controls.
[58.36 → 76.14] Start shipping internal apps to move your business forward in minutes with basically zero uptime, reliability, or maintenance burden on your team. Some of the best teams out there trust Retool, Bred, Coinbase, Plaid, DoorDash, Legal Genius, Amazon, All birds, Peloton, and so many more.
[76.14 → 86.02] The developers at these teams trust Retool as their platform to build their internal tools, and that means you can too. It's free to try, so head to retool.com slash changelog.
[86.02 → 89.76] Again, retool.com slash changelog.
[99.76 → 105.32] This is JS Party, your weekly celebration of JavaScript and the web.
[105.32 → 112.64] If you love our shows, check out changelog.com, drop the ads, get in on bonus content, and directly support our work.
[112.88 → 118.18] And it works right in your favourite podcast app. Whether you listen on Apple, Spotify, Overcast, it's all good.
[118.48 → 121.14] Learn more at changelog.com slash plus.
[121.32 → 126.10] Thanks to our friends at Vastly for beaming JS Party all around the world to wherever you listen.
[126.36 → 128.40] Check them out at fastly.com.
[128.74 → 131.20] Okay, take it away, K-ball. It's party time, you all.
[131.20 → 143.16] Hello, and welcome to another episode of JS Party.
[143.38 → 151.04] I'm K-ball. I am your host today, and I am so excited about this episode where I get to bring back one of our favourite guests, Tom Preston Warner.
[151.20 → 151.94] Tom, how are you doing?
[152.22 → 157.10] I'm doing well. Thanks for having me back. It's been probably a year since I was on last.
[157.10 → 162.06] I was looking back at when the last one was, and it was March 2020, believe it or not.
[162.24 → 162.92] So it has been-
[162.92 → 166.90] Oh, two years. That's right. Because that was right after we released the first version of Redwood. That's right.
[167.18 → 173.20] Yep. So two years, and that was right as times were real crazy around.
[173.72 → 179.16] Oh, yeah. It was an interesting time for everyone, I think, right as the pandemic was getting started.
[179.42 → 183.10] And so that's interesting. Redwood really has been this pandemic project.
[183.10 → 190.82] Yeah, totally. So we're excited to have you back. Redwood 1.0 released, and I want to dive very deep into what it is.
[190.90 → 199.14] But I think because it has been so long, maybe it's worth taking some time to kind of explain for folks who may be unfamiliar with Redwood what it is.
[199.52 → 207.92] Absolutely. So Redwood is a JavaScript and TypeScript full stack framework optimized for startups,
[207.92 → 212.04] or for anyone who's building a side project that you might want to turn into a startup.
[212.32 → 221.50] What we really want to do is make your life easier as someone building a web application or other types of applications to mobile clients.
[221.82 → 227.10] Now, we don't make that as easy as we will someday, but because of the architecture of Redwood,
[227.46 → 232.78] and I'll get into the architecture and how we use GraphQL, we want you to live in a multi-client world.
[232.78 → 238.52] And so all of these things we've thought about from a Redwood perspective to make your journey,
[239.12 → 245.68] building a project, growing a team, making it all maintainable, trying to make that as easy as possible,
[245.74 → 248.98] as smooth as possible, as integrated as possible.
[249.40 → 256.44] Redwood really is a play of integrating all the best tools and then adding some really great code on top of that
[256.44 → 260.68] to glue them all together and simplify some of the common processes you have.
[260.68 → 267.98] But to really deliver a full stack JavaScript or TypeScript experience for building something that might be,
[268.16 → 271.26] or already is, the size of a startup.
[271.82 → 274.54] Interesting. So when we first talked, the pitch was,
[274.74 → 277.80] okay, Redwood is going to be the Ruby on Rails for the JavaScript world.
[277.86 → 279.16] And you highlight that a little bit here.
[279.20 → 282.42] It's like all these different pieces integrated and pulled together.
[282.56 → 286.00] Can you sort of flesh out a little bit more what that looks like?
[286.02 → 288.02] Because we're not very familiar with that in JavaScript.
[288.02 → 298.84] Yeah, well, Redwood really started as kind of technical experiment to see if I could build a full stack framework for the JAM stack.
[298.92 → 302.00] And that used to be our tagline was full stack for the JAM stack.
[302.66 → 306.74] Because of what Netlify made possible, and I'm on the Netlify board,
[306.86 → 312.44] I've invested in all the early rounds of Netlify and have known the founders since forever.
[312.44 → 324.04] And when Netlify started to make it really easy to package up Lambda functions and get those deployed along with your more traditional JAMs tacky,
[324.16 → 328.94] like your static HTML, or if you have a React app that you're going to deliver via the CDN,
[329.88 → 337.24] I thought that was a fascinating model and could be the base of a more modern kind of architecture for full stack applications.
[337.24 → 340.96] If you had a React application that you want to deliver via the CDN,
[341.28 → 345.18] and you have your business logic, which you can deploy onto Lambda functions,
[345.60 → 349.98] and then you have a database somewhere, and that was kind of the unknown part of it.
[350.12 → 352.60] Two years ago when we were working on this, it's like, how do you deal with it?
[352.60 → 354.50] There are not a lot of good serverless databases.
[354.76 → 355.40] Now there are.
[355.92 → 359.70] So that part of it is actually mostly solved.
[359.70 → 361.72] And we made that work.
[362.02 → 370.52] So you end up deploying an implementation of a GraphQL API that you write in JavaScript or TypeScript onto a Lambda.
[370.88 → 376.20] But you deploy the entire thing to a single Lambda, which has certain characteristics.
[376.58 → 378.54] Lambdas are not perfect for everything.
[379.28 → 381.56] And so this architecture works and makes that possible.
[381.68 → 388.08] And we have a lot of people using that still today, the serverless deployment option for Redwood.
[388.08 → 392.46] But what we also realized was that's not going to be suitable for everyone.
[392.78 → 395.70] So there are certain performance characteristics that you might not like.
[395.76 → 398.70] The cold start times are still longer than we'd like them to be.
[399.00 → 403.86] You will eventually max out how much code you can put into a single Lambda function.
[404.54 → 407.42] And so we started experimenting with other deploy targets.
[407.80 → 411.98] And so now Redwood is not specific to serverless at all.
[412.32 → 413.48] You have an option.
[413.76 → 417.02] You can still deploy nervelessly if that's what fits your needs.
[417.02 → 424.22] But you can also deploy to traditional providers, several providers, things like Amazon.
[424.36 → 428.08] We have a deployment option that we call Bare Metal.
[428.44 → 438.14] Now, where you deploy in a way that looks very similar to how you did it with Rails and Cristiano, where you're Shying into an EC2 instance and getting it set up in that way.
[438.34 → 440.80] And it's superfast.
[440.88 → 441.82] It's really amazing.
[441.82 → 444.42] You have all the flexibility you want around that.
[444.50 → 446.24] Or you can go somewhere in between.
[446.44 → 448.86] You can deploy to Tercel as well as Netlify.
[449.18 → 451.14] You can deploy direct to EC2.
[451.52 → 456.82] But you can go in between with services like Render, where it's more of a containerized style approach.
[457.64 → 459.88] And so Redwood works across all of these.
[460.42 → 466.00] And so that was one thing that brought us away from the initial sort of idea for Redwood.
[466.00 → 470.22] And so we started thinking, well, what is the differentiator for Redwood?
[470.38 → 480.40] Why would someone choose Redwood over something like Next.js, which is obviously the most popular player in the sort of like React universe for building a site?
[480.84 → 481.56] And for good reason.
[481.66 → 482.98] It's really great technology.
[483.42 → 485.98] So why would you choose Redwood over some of the alternatives?
[485.98 → 495.86] And what I started to think about was how much we integrate and how much we do for you out of the box and who's going to need that.
[496.08 → 499.14] Because some of these things make the framework more complicated.
[499.44 → 503.00] Like if you look at Next, Next is really pretty simple.
[503.34 → 504.90] There's not a lot to it.
[504.96 → 506.18] It has a small surface area.
[506.48 → 508.68] It doesn't try to be full stack.
[509.14 → 514.98] It gives you hooks to do database calls and other things that you want to do from a server side perspective.
[514.98 → 525.40] But it's not trying to be opinionated in the way that I wanted to build a framework that was more like Rails to give people a lot more out of the box, make a lot more decisions for you out of the box.
[526.20 → 530.08] And so Redwood integrates React on the front side.
[530.08 → 539.76] And it uses GraphQL to communicate from the front end web SPA to the back end, which is a GraphQL implementation using Apollo Server.
[539.76 → 546.62] And then you use Prima as an ORM to talk from your GraphQL API to your database.
[546.84 → 548.20] And that's all in your business logic.
[548.74 → 553.74] And then on top of that, we also integrate Storybook and Jest for testing.
[553.74 → 563.00] And we have a bunch of authentication providers that you can install with a single command line invocation, as well as different deploy targets.
[563.34 → 565.38] And all of this and a bunch more.
[565.60 → 567.14] Logging is included.
[567.64 → 570.16] Security by default for your GraphQL API.
[570.46 → 574.02] A really great way to build your GraphQL API using what we call services.
[574.02 → 579.22] And then on the front end, declarative data fetching using what we call cells.
[579.34 → 583.20] All of these different things we're packaging up and integrating.
[583.92 → 588.12] And to me, that looked like what you need to build a startup.
[588.36 → 594.74] Something that is larger than a weekend sort of hack that you might do to experiment with some idea.
[594.74 → 601.90] That's where Next, I think, shines so well in just the ease with which you can get something up and running.
[601.90 → 606.00] With Redwood, you have more complexity out of the gate.
[606.32 → 613.76] Because you've got, I mean, GraphQL alone and the strict separation that that gives you from the front end to the back end is more complicated.
[613.98 → 618.20] And so it makes it more difficult, perhaps, to hack something together in an hour.
[619.12 → 631.66] But if you're building something for the long term, a little bit of that upfront complexity that you have to deal with is going to give you great dividends and maintainability in the long run.
[631.66 → 633.28] As well as helping people.
[633.90 → 637.22] Once you grow a team, you have specialized people, developers.
[637.60 → 638.46] Some people are doing front end.
[638.54 → 639.50] Some people are doing back end.
[639.58 → 640.70] You've got all these different roles.
[641.02 → 647.56] And having that kind of separation of concerns of what the different parts of the framework are doing.
[647.92 → 656.88] To me, in my experience as building large pieces of software and large companies, that is what becomes extremely valuable and maintains your velocity in the long run.
[656.88 → 663.34] And so that is what made us start to say, well, Redwood is optimized for startups.
[663.44 → 664.60] It's the app framework for startups.
[665.12 → 668.28] Because that then is something that someone can say, oh, I'm building a startup.
[668.60 → 672.84] I want a piece of technology that's going to get me farther faster and do more for me.
[672.84 → 679.28] And deal with all the stuff that I don't want to have to do so that I can focus on the things that make my business different.
[679.28 → 684.10] And so that's why we've really started to talk more as Redwood being for startups.
[684.64 → 696.92] I feel like there's a number of companies and frameworks that have started in that space because startups tend to be kind of early adopters willing to, you know, if it takes work off my plate that lets me get to a business faster and MVP faster, I'm happy to do it.
[697.48 → 701.76] So you talked some about it's putting a little bit more structure in place.
[701.76 → 709.08] What other types of optimizations or changes have you made since shifting focus to look at startups as a target audience?
[709.28 → 713.52] How does that guide decision-making, or what are the other angles that that brings forward?
[713.98 → 716.12] I think I've talked about a lot of them.
[716.28 → 719.62] I mean, a lot of it looks like it doesn't even look like technology.
[719.62 → 720.82] It looks like community.
[721.06 → 725.90] It looks like partnerships with the different companies that we work with.
[725.90 → 737.90] So the different authentication providers like Auth0 or Clergy or Magic Links or, you know, there's like seven or eight others or the deployment providers or the logging providers.
[737.90 → 740.90] All of these are companies or the database providers.
[741.98 → 744.90] All of these are companies that we have strong relationships with.
[745.40 → 755.74] And that allows us to go deeper into helping people with those technologies or helping people to make choices between those different options that you might have.
[755.90 → 759.98] And a lot of what we do is spend time with people in the community.
[759.98 → 766.24] So we have a startup club that if you are a startup, whether you've raised money or not is not really the point.
[766.24 → 768.14] It's more like you're building this thing.
[768.58 → 769.50] It looks like a startup.
[769.50 → 783.20] If it looks like a startup, and it feels like a startup to you, then to us, we'll invite you into the Redwood Startup Club where we are able to listen to people's needs as they're building and growing their products.
[783.20 → 804.10] But not only that, really talk through the problems that every startup has around trying to figure out how to hire people or how to determine if you have product market fit or how to choose some of these options, deployment providers, like what's going to work for your use cases or how to raise money.
[804.10 → 807.94] So I have relationships with a lot of venture capitalists, a lot of VC firms.
[808.10 → 813.04] I do angel investing myself and others in the group have done startups before.
[813.52 → 819.80] And so we really use this as a channel to help you build a startup outside just strictly the technology.
[819.80 → 833.84] And so that also is part of the play is that if you want to build with Redwood, then not only do you get a great piece of technology, a framework to help you do that more quickly and scale and build multiple front end clients with as you need.
[834.10 → 841.12] But you get advice around how to build a startup and a peer group that is trying to build a startup as well.
[841.12 → 849.42] So it goes well beyond what most frameworks are trying to do from a community perspective in helping you get done what you want to get done.
[849.70 → 850.60] Yeah, that's fascinating.
[850.82 → 858.82] So you're almost envisioning this now as it's a tiny piece of this more startup ecosystem play that you're making.
[859.54 → 860.98] Yeah, I mean, these are my great loves.
[861.22 → 863.88] One of them is building tooling for developers.
[864.26 → 868.46] Another one that I've been doing for the last five or six years is investing in startups.
[868.46 → 879.48] And so I realized that Redwood, the technology can be this really amazing combination with the investing that I do and the advising of startups.
[879.60 → 882.08] I just I spent a lot of time talking to founders.
[882.08 → 891.62] And as an entrepreneur, I really enjoy giving back in that way of helping people succeed in trying new things.
[891.62 → 902.30] And so what we say for Redwood is as our mission is we want to help more startups explore more territory more quickly.
[902.52 → 910.98] And that's both via the technology, the framework, and the community and helping you accomplish those explorations.
[910.98 → 922.80] This episode is brought to you by Tercel, the platform that enables front end teams to do their best work.
[923.16 → 928.14] Tercel combines the best developer experience with an obsessive focus on end user performance.
[928.84 → 932.24] And I'm here with founder and CEO of Tercel, Fisher Rank.
[932.60 → 938.60] So Fisher, I had you on Founders Talk recently talking about making the web faster and how Tercel is built on three pillars.
[938.60 → 943.10] Develop preview ship, but talk about why it's so important to make the web faster.
[943.34 → 947.96] I think, first, the web is the most open and exciting platform to build on.
[948.40 → 953.50] And listeners are going to be enthusiastic about JavaScript, which is one of our areas of focus.
[953.64 → 962.14] We think that by creating amazing tools and open sourcing them, developers will go on to create amazing experiences for the end users.
[962.32 → 966.66] And I think that's where the concept of making the web faster to build and faster to end users.
[966.66 → 969.02] That's the crucial mission of Tercel.
[969.26 → 975.20] This is what's led to us investing all across the board to build this end-to-end platform.
[975.42 → 984.62] It started with the framework that you develop with, the workflow of pushing up a change and seeing it instantly and being able to share that change with your collaborators.
[984.62 → 992.32] All the way to shipping to the edge network of Tercel that makes your site or application globally fast, globally available.
[992.54 → 998.06] So it's this very comprehensive mission of making the web end-to-end faster and more open.
[998.48 → 998.96] I love it.
[999.00 → 1002.08] Globally fast, globally available on a more open web.
[1002.18 → 1003.98] Learn more at Vercel.com.
[1004.18 → 1005.86] Again, Vercel.com.
[1005.86 → 1033.92] I'd love to dig in a little bit more to this 1.0 release and kind of talk about explicitly what does Redwood look like today?
[1033.92 → 1035.88] What is that technology piece?
[1036.04 → 1038.72] What is it that you mentioned some areas around?
[1038.88 → 1043.82] Choices that you're making versus others where you kind of make it more flexible for folks, and maybe you have recommendations.
[1043.82 → 1047.64] So like what's in the box in the 1.0 release?
[1047.90 → 1050.10] And where does Redwood shine today?
[1050.16 → 1053.42] And where is there maybe still some room to grow or some challenges?
[1053.42 → 1054.42] Yeah.
[1054.42 → 1080.30] So the reason that the 1.0 release took two years from the initial 0.1 release is because we wanted it to really feel like a competent way to get a full application out there with all the things that if you're building some kind of SaaS project, you are a startup that you could use Redwood and really get there with what's in 1.0.
[1080.30 → 1084.36] So it has all the fundamental pieces that we think are necessary.
[1084.94 → 1090.68] So I listed them off before, but it's essentially a React front end and a whole web side.
[1090.68 → 1114.94] We call it a web side, an API side, because we imagine that eventually in Redwood there will be a mobile side, like a React Native side or a command line interface side or a public GraphQL side where you take some of your GraphQL API, and you're able to document and release it and give people guarantees about how long that's going to last and how it'll evolve over time.
[1114.94 → 1119.10] But all of those things we want to make possible.
[1119.46 → 1121.10] And so that's why it's the website.
[1121.28 → 1130.54] So we have a full website and a way to do routing on the front end that we think is novel and interesting, a way to do declarative data fetching that we call cells.
[1130.98 → 1134.68] All of that's been in there and all of that was really important to 1.0.
[1134.68 → 1141.74] So we built in and spent a lot of time making sure that the backend, the GraphQL API was secure by default.
[1142.50 → 1146.16] And so this is something in the GraphQL world that is non-trivial.
[1146.36 → 1154.62] Like if you just start writing a GraphQL API with Apollo server, that's really the bare minimum that you need to get it done.
[1154.62 → 1159.72] And it's a little painful if you haven't done this before, figuring out how to do it.
[1159.84 → 1172.00] And even things that seem like they should be trivial, like separating out your GraphQL API into multiple files instead of having one giant like resolver file are non-trivial to do.
[1172.62 → 1181.62] And so we've done a lot of that integration work for you to make it a really beautiful experience putting a GraphQL API together.
[1181.62 → 1185.46] So a lot of it was around polishing that and doing things like authentication.
[1185.68 → 1196.68] So how do you integrate with your authentication provider of which you have many different choices and make that not turn your GraphQL API code into a horrible mess?
[1197.10 → 1206.30] And so making sure that that was really streamlined and that you can put permissions on your GraphQL queries and mutations.
[1206.40 → 1210.38] So all the different things you want to do, each one you might have different requirements for and say,
[1210.38 → 1217.90] okay, well, if you're going to want to list some resource, then maybe you can be anyone.
[1218.28 → 1219.52] So don't do any auth at all.
[1219.74 → 1224.86] But if you want to delete something, well, now you need to be an admin.
[1225.44 → 1228.58] How do you do that in your GraphQL implementation?
[1229.10 → 1230.62] There's a million different ways that you could do it.
[1231.26 → 1233.86] All of them are choices that you have to make.
[1233.98 → 1239.02] All of them are going to be annoying to some extent because authentication is always annoying.
[1239.02 → 1243.08] So how can you reduce that to the minimum annoyance possible?
[1243.22 → 1249.08] And so what we've come up with for Redwood is to use GraphQL declarations to do that.
[1249.24 → 1256.82] So in your SDL file, in your GraphQL schema definition language file, your SDL file, where you're saying what your types are and your queries and mutations,
[1257.56 → 1262.84] next to a query or a mutation, you can just put a declaration for your auth.
[1262.84 → 1265.28] You can say skip auth if you don't want any.
[1265.82 → 1273.24] Or you can say use auth, which is kind of the built-in authentication mechanism that then gets hooked into whatever authentication provider you've chosen.
[1273.88 → 1276.92] And so there's not really any work that you have to do there to use that.
[1276.98 → 1281.12] Then it'll just say, okay, you need to be authenticated as a user.
[1281.12 → 1296.06] Or you can say, because we have built-in role-based access control in Redwood, then you can say, oh, I want only admin role people to be able to do this mutation, for instance.
[1296.50 → 1297.74] So that's all baked into the framework.
[1297.84 → 1299.20] Things that you don't have to figure out.
[1299.38 → 1300.90] Technologies that you don't have to evaluate.
[1301.40 → 1303.60] And they feel very natural and streamlined.
[1303.60 → 1307.76] And so that was a big thing that took quite a while to nail down.
[1307.84 → 1313.92] And we went through a couple of different iterations of how that authentication and access control might work within the framework.
[1314.40 → 1316.06] So it's all of those things.
[1316.06 → 1318.66] And really, developer experience is paramount to us.
[1318.90 → 1329.08] And so we've had to make some explorations and some mistakes around what things look like to bring things to the level of simplicity that we demand for the framework itself.
[1329.08 → 1341.16] Even though it is more complex architecturally, perhaps, than some of the alternatives, it's still important that that complexity does not prevent you from getting things done.
[1341.22 → 1344.58] And that it really ends up being a boon to your productivity over the long run.
[1344.94 → 1347.66] Well, and as you highlight, it's doing complex things, right?
[1347.70 → 1353.20] Like integrating auth and RAC, or role-based access control, that's a complex thing.
[1353.26 → 1354.62] That complexity is going to live somewhere.
[1355.10 → 1357.50] I have this thesis that complexity is conserved, right?
[1357.50 → 1360.46] It's either exposed to the user or it's baked into something somewhere.
[1360.64 → 1364.34] So you have baked that into the framework where that complexity is there.
[1364.42 → 1367.56] But I, as a user of my framework, don't really have to worry about it.
[1368.00 → 1368.02] Right.
[1368.18 → 1371.60] But it's also trying to not use too much magic.
[1372.32 → 1375.26] So there's always a balance here.
[1375.34 → 1377.28] It's like, OK, you're going to do all this stuff for me.
[1377.36 → 1379.00] But what if I want to make different choices?
[1379.44 → 1379.58] Yeah.
[1379.58 → 1387.58] What if I don't want to do authentication in the way that you make really easy because my requirements are a little different?
[1387.84 → 1391.54] And so we've tried to be really conscious of that as well.
[1391.54 → 1401.88] And so for the authentication provider, all of these things are written essentially as in sort of plug-in style where you could write your own.
[1401.88 → 1406.40] And the way that you do it is to implement an API around authentication.
[1406.40 → 1415.76] So they've all been, in order to allow you to choose any of them, there is a layer that has been abstracted that is all the things that you need to do from an authentication perspective.
[1415.76 → 1420.06] And each of the providers then implements that API.
[1420.48 → 1427.24] And you can roll your own custom authentication in exactly the same manner and do whatever you want in that regard.
[1427.86 → 1429.98] So that kind of feeds into a question I had.
[1429.98 → 1439.70] So one of the things for me that happened as Rails, and I keep using that as a metaphor because I was familiar with that process early on, and I loved a lot of it.
[1439.88 → 1449.94] As that project evolved, it went from being opinions that were hard to change out to opinions that were, or conventions that were much easier to swap around if you needed.
[1450.60 → 1453.52] Where in Redwood is it easy to sub things in?
[1453.76 → 1455.98] Or maybe it sounds like for some of them it's odd.
[1456.08 → 1457.00] Where is it still hard?
[1457.00 → 1461.70] If I wanted to, for example, swap out Prima or something like that, is that something I can do?
[1462.34 → 1463.92] Yeah, so that's probably the best example.
[1464.18 → 1473.32] So the things that are easy, swapping out or changing authentication providers or deploy targets are both super easy, super-duper easy.
[1473.86 → 1483.42] Swapping out some of the core, let's say the main three core bits are right now to Redwood would be React, GraphQL, and Prima, let's say.
[1483.42 → 1486.54] Those are kind of the three assumptions that we make.
[1487.00 → 1490.94] If you want to change one of those, then you're going to end up doing a lot of work on your own.
[1491.14 → 1495.00] So it's GraphQL, so you can build whatever front-end client you want.
[1495.08 → 1505.58] If you like Vue or you like Svelte or you like whatever, just writing anything you want, as long as you can consume GraphQL, then you can build anything you want.
[1505.58 → 1510.88] This is the multi-client aspect that I've talked about where now you can have a mobile client.
[1510.98 → 1512.04] You can have a command line client.
[1512.10 → 1513.26] You have a kiosk at a mall.
[1513.36 → 1515.64] You could have an app in your Tesla.
[1515.80 → 1520.14] Whatever it happens to be, GraphQL is going to make it possible for you to do that.
[1520.20 → 1523.86] And it's going to make it possible for you to not have to reimplement your back-end to do it.
[1523.86 → 1537.16] But this was a lesson that I learned several times, which is if you start building your application with Rails, for instance, and you have a traditional Rails front-end, then you do your back-end in a certain way that feeds into your views and whatever.
[1537.28 → 1537.88] Your life is good.
[1537.88 → 1543.10] But then you're like, I want a native mobile client or a desktop application.
[1543.36 → 1544.54] And now you're like, oh, crap.
[1545.00 → 1557.32] I guess I'll have to build REST or I can try to tweak Rails back-end stuff so that it's also RESTful, which it kind of is like the dream of what Rails can do, but never really quite the reality to be able to reuse your sort of…
[1557.32 → 1558.50] It's a very leaky abstraction.
[1559.26 → 1559.66] Right.
[1559.70 → 1561.04] It doesn't match real well, right?
[1561.04 → 1567.00] So then you're like, okay, but I'm going to build my mobile client in React, so I'm going to use React Native.
[1567.00 → 1569.62] And that really matches well with GraphQL.
[1569.96 → 1575.88] So I guess I'll now write a GraphQL implementation alongside my Rails back-end.
[1575.96 → 1577.14] And now you've written two back-ends.
[1577.28 → 1579.32] And nobody wants to write two back-ends.
[1579.94 → 1581.76] I've done this several times.
[1582.08 → 1582.90] And it's a nightmare.
[1583.26 → 1584.26] Yeah, I have as well.
[1584.36 → 1585.64] And it is never good.
[1585.94 → 1595.36] You end up with these fun databases API type things where you're having to then make sure that you've got all the same access control and other things working.
[1595.36 → 1596.66] And yeah, it's a nightmare.
[1597.00 → 1597.44] Right.
[1597.56 → 1601.12] You just always have two things you have to think about.
[1601.38 → 1603.84] And then different teams are working on the different aspects.
[1604.02 → 1611.90] And now they have to talk about like, oh, if you're going to change that thing in the user interface, then the GraphQL API needs to reflect that too.
[1612.12 → 1613.12] And there are two places.
[1613.12 → 1621.80] So part of the fundamental reason to design Redwood this way is the idea that you'll only implement your back-end once, and it will be as GraphQL.
[1622.40 → 1625.86] Which, take it like some people don't like GraphQL.
[1626.04 → 1628.50] If you don't like GraphQL, then maybe Redwood's not for you.
[1628.50 → 1641.10] But if you believe that having the ability to create any client you want and consume GraphQL, that that would be advantageous because you intend to have multiple clients, then I think Redwood can be a very good fit for that.
[1641.10 → 1646.86] But you've done a few more things than just having it be React because you've implemented cells in this declarative rendering.
[1647.12 → 1647.22] Right.
[1647.22 → 1649.30] I know, or declarative data fetch.
[1649.40 → 1656.00] And we had talked two years ago when we spoke, you talked about trying to get in the flow of data fetch so you can solve the waterfall problem.
[1656.10 → 1656.22] Right.
[1656.32 → 1660.16] Which is something that I know Remix has also done a bunch of stuff around.
[1660.28 → 1662.06] And like, that's a big area folks are focused.
[1662.60 → 1663.74] I guess I should check first.
[1663.90 → 1664.90] Did that end up happening?
[1665.02 → 1669.08] Is that part of what you get in Redwood 1.0 is you're able to solve the waterfall?
[1669.46 → 1670.68] We have not tackled that yet.
[1670.76 → 1670.96] Okay.
[1671.36 → 1672.40] That is a big question.
[1672.56 → 1673.90] Like, where does your data fetching happen?
[1673.90 → 1677.80] And now with cells, we are able to get into the flow of that.
[1678.20 → 1682.24] And so this is something that'll be a research project now that we have 1.0 out.
[1682.38 → 1684.36] So we couldn't do everything for 1.0.
[1684.70 → 1690.54] You know, we had to sort of cut aggressively in order to, you know, even get a 1.0 out the door.
[1691.18 → 1695.00] And so we were not able to get some of those optimizations in.
[1695.06 → 1699.68] But I'm really excited to do some of those research projects to try to make some of those things possible.
[1699.68 → 1702.06] Well, then this is maybe not as relevant there.
[1702.06 → 1706.60] But I was wondering, like, is that separation of sort of having the declarative model?
[1706.96 → 1709.34] Because there are so many nice things that you can get out of that.
[1709.42 → 1712.20] Is that something that you could separate from the React-based implementation?
[1712.60 → 1718.36] So if somebody is swapping in another framework, they can get, you know, some more of the batteries.
[1719.14 → 1719.34] Yes.
[1719.40 → 1720.90] So you don't have to use cells.
[1721.20 → 1724.64] And we have some people that don't use our data fetching.
[1724.70 → 1726.58] We have one guy that uses Relay.
[1726.58 → 1728.36] He's like a Relay expert.
[1728.94 → 1733.52] And so he's like, I'm going to use Relay instead because that's what I know.
[1733.96 → 1737.68] And so he doesn't use cells, and he doesn't get some of the nice things because of that.
[1737.70 → 1740.72] But he likes working in this other kind of way.
[1740.80 → 1748.02] And that's totally possible to do because we're trying not to add so much magic that it's impossible to untangle some of these things.
[1748.02 → 1750.42] And so cells are really not that complicated.
[1750.62 → 1752.72] It's a higher order component that we've implemented.
[1753.02 → 1755.04] And it does that data fetching for you.
[1755.14 → 1762.38] And we then have some things in Storybook and in testing that integrate really well with cells to be able to do your mocking and whatnot.
[1762.56 → 1769.58] So there are other advantageous things in the Redwood world that you'll also be giving up if you're not going to use cells.
[1770.18 → 1773.30] You'll have to do some of that work yourself to replace some of those things.
[1773.36 → 1777.20] Like, how do you mock data now for your tests and for Storybook if you want to use them?
[1777.20 → 1778.80] That's now on you.
[1779.18 → 1780.38] That's not the golden pass.
[1780.44 → 1781.44] You're going to have to do more work there.
[1781.94 → 1784.30] But yeah, so you don't have to use cells if you don't want to.
[1784.38 → 1789.54] Or you can make GraphQL's directly using whatever GraphQL client you want from the front end at any time.
[1789.54 → 1796.74] And some people do that for things like there's a React table implementation that kind of handles its own data fetching.
[1796.80 → 1799.10] And you can totally do that because, again, it's just GraphQL.
[1799.52 → 1801.06] And you can make that work, right?
[1801.14 → 1804.28] So you don't have to use that, right?
[1804.28 → 1808.42] But one of the things that's unique about Redwood is the routing mechanism.
[1808.42 → 1811.40] So we have built our own router.
[1811.84 → 1818.08] And it allows you to put all your routes into a single file, essentially, which I really liked from the Rails world.
[1818.16 → 1822.68] So this is different from sort of the nested, split-up React router kind of paradigm.
[1822.68 → 1843.18] But it allows us to do code splitting in a really clean way, as well as just showing you the entire structure of your application in a single place, which to me is valuable, especially from someone who comes in new to your project and wants to figure out how your application works or how to find a specific piece of code that's running on a certain page.
[1843.18 → 1849.56] Being able to have a single route file that you can look at and reason about is really valuable from that perspective.
[1850.20 → 1853.96] So there's a variety of things that we've done in that regard.
[1854.20 → 1855.04] That's one of them.
[1855.20 → 1863.00] But, I mean, there are so many more optimizations and things that we have in the plans that we haven't been able to do yet.
[1863.00 → 1870.22] Because of the breadth of integration that we really wanted for 1.0, that is what took precedence.
[1870.22 → 1875.20] I want to fully answer your question from before about what are the parts that might be easy to swap out.
[1875.30 → 1879.58] So GraphQL, we actually do have someone who uses RPC instead of GraphQL.
[1879.76 → 1885.06] Now, that's a large chunk of work that one would have to do in order to make that work.
[1885.16 → 1889.66] But, indeed, it is possible to swap out the transport if you wanted to do so.
[1889.76 → 1890.48] It can be done.
[1890.56 → 1891.50] I wouldn't recommend it.
[1891.66 → 1895.72] I think that's a bit beyond the scope of what a normal Redwood user would want to do.
[1895.72 → 1901.26] And then on the back end, Prima, Prima is, you don't have to use Prima.
[1901.38 → 1904.32] But, again, you're going to miss out on the integration.
[1904.62 → 1907.26] So generators are the Redwood generators.
[1907.48 → 1918.78] So if you want to scaffold and create all the CRUD operations that go from front end to back end and the interfaces, all the GraphQL stuff and all the web, kind of simple web admin interface.
[1918.78 → 1923.06] And the tests that we use, and the generators are all written against Prima.
[1923.18 → 1924.58] They expect you to use Prima.
[1925.02 → 1926.78] So you wouldn't get some of that stuff.
[1927.08 → 1930.10] But you could certainly use whatever database you want.
[1930.16 → 1936.34] So if you want to use, we recently talked to Edged, which is a new database provider, serverless.
[1936.72 → 1939.80] It sees the database more as an object graph.
[1939.80 → 1943.18] But it has a proper schema with it.
[1943.38 → 1944.18] Fascinating.
[1944.58 → 1948.44] So we talked to them, and they're like, well, what would it take to allow you to use that?
[1948.50 → 1949.70] Because then you wouldn't be using Prima.
[1949.82 → 1953.48] You'd be using their native, their kind of client that they've written special for that.
[1953.84 → 1955.04] And I think it's not too bad.
[1955.20 → 1963.42] We actually, we could abstract out the generators to be able to, without too much trouble, even fix up the generators so that you could use the generators.
[1963.42 → 1967.60] And now it would just write against Edged instead of against Prima.
[1967.60 → 1974.44] Yeah, kind of creating the same layer that you have for your auth, where there's an API they write against, and you have an adapter and it works.
[1974.86 → 1975.24] Exactly.
[1975.38 → 1985.64] You just keep abstracting more and more up the chain and then eventually nobody has any idea how the code base works because everything's like three levels of abstraction between it and reality.
[1986.24 → 1988.44] But I mean, this is how a project becomes more flexible.
[1988.44 → 1993.22] And that's on us to manage the complexity of the framework code base itself.
[1993.22 → 1996.48] But, you know, because it's JavaScript, like you can fetch from anywhere.
[1996.48 → 2001.82] If you want to read from a Regis somewhere, or it's all JavaScript, you can whatever.
[2002.04 → 2009.92] If you can do TCP IP, then you can do your data fetching, like from your backend, read from a data source, however you want.
[2010.08 → 2014.04] You just won't get the kind of the magic goodies that Redwood makes possible.
[2014.92 → 2016.72] I want to maybe dig in.
[2016.86 → 2020.10] So if somebody is trying to decide, hey, there are so many cool frameworks out here.
[2020.26 → 2020.96] There's Next.
[2020.96 → 2023.88] You know, we've had a couple conversations recently about Remix.
[2024.30 → 2024.88] There's Redwood.
[2025.46 → 2028.18] Walk me through what the decision tree would look like.
[2028.36 → 2031.22] Like when would I, and when would I not use Redwood?
[2031.38 → 2033.98] Well, first, do you like the technologies in general?
[2034.32 → 2035.50] Like do you like React?
[2035.62 → 2036.52] Do you like GraphQL?
[2036.80 → 2037.48] Do you like Prima?
[2037.70 → 2042.92] If you like all of those things, then Redwood becomes a pretty easy decision, especially GraphQL.
[2042.92 → 2055.18] Because Redwood's really the only one of these that builds in GraphQL and makes it really easy to actually implement your GraphQL API in a way that's way easier than you've ever done before.
[2055.88 → 2064.60] So I'd say if that's what you like, if you think that you're going to have multiple front-end clients right out the gate, you're going to have a website, you're going to have a mobile client.
[2064.60 → 2074.72] If you know already that you're going to have those two things, then Redwood also becomes really attractive because you're saying, okay, well, I'm going to think about my application as a GraphQL API.
[2074.84 → 2076.40] I'm going to have multiple different front-ends for it.
[2076.60 → 2078.64] So I only have to implement my back-end once.
[2078.96 → 2084.60] So that becomes very attractive if you envision a future in which you have multiple clients, right?
[2084.60 → 2093.62] Because everyone else is going to hide the API from you right now, or it's going to be some proprietary thing.
[2094.36 → 2105.02] It's not exposed in a way that is first class for consumption by multiple different kinds of clients in the way that GraphQL is like, I am an API.
[2105.46 → 2106.54] Call me from anything.
[2106.54 → 2114.92] So I'd say that's one of the biggest differentiators for Redwood from a technology perspective is the GraphQL part of it.
[2115.54 → 2119.62] And the level of integration that we have is another one.
[2119.76 → 2122.22] Nobody else tries to integrate as much as we do.
[2122.40 → 2131.98] So again, if you like the technologies that we've chosen, if you're like, you know what, Storybook would be great because either I want to have this great resource for keeping track of all of my React components
[2131.98 → 2137.82] and use it as a design sort of reference for front-end developers to be able to see what all we do.
[2138.12 → 2149.84] Or my favourite thing, which is to use Storybook as a way to do isolated development of your components so that instead of trying to work on your components in your actual application
[2149.84 → 2155.90] and then trying to get the database in the state that allows you to see the states that you want of that component,
[2156.60 → 2160.24] instead you just work directly in Storybook to build your React components.
[2160.24 → 2166.02] And now you can feed it any data that you want and say, oh, I want this to be true, and I want this string to be this.
[2166.18 → 2168.08] And now it can look like anything that you want.
[2168.40 → 2174.02] And you don't have to fiddle with your application and be constantly refreshing to get it to where you want it to be.
[2174.16 → 2177.94] You're like putting random data into the database to get it.
[2178.08 → 2178.72] It's such a pain.
[2178.74 → 2181.44] Or like looking at loader states, right?
[2181.52 → 2185.76] It's like we've all been there where we're like, all right, I'm just going to keep hitting refresh
[2185.76 → 2192.62] and I'm going to open inspector and set it to slow 3G so I can see my spinner for three quarters of a second.
[2193.28 → 2193.40] Right?
[2193.46 → 2196.00] I'm just going to do that over and over until I get my spinner right.
[2196.22 → 2196.36] Right?
[2196.46 → 2199.18] Like that with Storybook, you're just like, you could look at it all day long.
[2199.28 → 2200.14] Just open it up.
[2200.28 → 2200.74] There it is.
[2200.80 → 2201.38] That's the state.
[2201.38 → 2208.76] So if you like Storybook, if you like to have some nice things around testing done for you.
[2208.90 → 2212.56] So when you get sophisticated, so if you're a startup, and you really take testing seriously,
[2212.56 → 2216.94] you're going to want to do end-to-end testing, which we make easy.
[2217.04 → 2221.46] You're going to want to do, you're going to want to be able to mock out your data fetching.
[2221.46 → 2233.92] And with GraphQL and the help that we provide you, we make mocking out and providing that mock data to your cells on the front end really easy with both your tests and in Storybook.
[2234.06 → 2242.64] So you can even in Storybook see your data fetching cells and the different states that they'll provide, the loading, success, failure, empty.
[2243.06 → 2247.14] All those states just become different things you can click on in Storybook, and they're mocked out.
[2247.28 → 2248.82] And we make that really easy to do.
[2248.82 → 2262.12] Or with testing, we've created what we call scenarios, which are a way to set up your database for a specific scenario of like, let's say you have a user and they need to have three of some object.
[2262.12 → 2270.70] And that's now your user with three objects scenarios, which might be different from your user that's totally brand new, and they've never added anything.
[2270.80 → 2272.00] You want to be able to test against that.
[2272.08 → 2278.10] Or you have a user that has a credit card set up, and they've interacted with these four different users.
[2278.10 → 2283.48] All of those we make really easy to set up those as different scenarios and test against them in your testing.
[2283.66 → 2302.70] So if you like to do rigorous testing, and you want that to not be a huge painful thing that you have to manage yourself and add all of these mocking and scenario like database setup types of things, then Redwood would be, you might choose Redwood because those things are all available out of the box.
[2302.70 → 2306.00] As well as logging that we provide for you.
[2306.00 → 2315.40] We integrate Piano for logging, and you can choose then to set that up against different log ingestion scenarios depending on where you're deploying to.
[2315.40 → 2320.40] So those are all reasons that you might choose Redwood from a technology perspective.
[2320.40 → 2338.08] And in addition to that, then you might choose Redwood because of the community that comes along with it and the help that we can give you around managing, thinking about and being successful with your startup from the human side of it, which is often even the more difficult side.
[2338.08 → 2343.88] Right. So if you like more with your technology than just here's an open source repository, good luck.
[2344.22 → 2354.50] If you want to have a community of people that are building and going through the same struggle as you, and you like that idea, then that might be a reason that you would choose Redwood as well.
[2354.96 → 2356.42] One last question on this domain.
[2356.60 → 2357.40] How's performance?
[2357.40 → 2364.04] I'm thinking things like server side rendering, data fetch, thinking about bundle size, all these different aspects.
[2364.40 → 2367.98] Yeah. I mean, they're not going to be any different from your traditional SPA.
[2368.50 → 2375.32] So Redwood, right now the website of Redwood is fairly traditional single page application architecture.
[2375.96 → 2381.76] And so there will be some performance implications because of that, that we're all used to.
[2381.76 → 2392.26] Now we have the ability for you to be able to pre-render pages right now, and then they'll hydrate on the website, on the browser after you do that.
[2392.32 → 2395.08] And these are all things that are fairly common today.
[2395.74 → 2397.86] This is the one thing.
[2398.06 → 2400.54] So let's say you're looking for reasons to not choose Redwood.
[2401.02 → 2408.64] One of them might be, I need more server side rendering capabilities, which something like Next is really great at.
[2408.64 → 2414.22] The kinds of things that Next can do from an SSR perspective are really great.
[2414.36 → 2422.80] We actually have a lot of startups now that are using Next as essentially a client for the GraphQL API.
[2423.08 → 2433.82] So they need to have HTML delivered with OG tags, for instance, or whatever the reason is to be delivering something from an SSR perspective.
[2433.82 → 2439.86] They'll use Next and have it call via GraphQL to the backend to fetch the data.
[2440.34 → 2443.28] And that ends up being a fairly common pattern.
[2443.54 → 2451.88] Now that we have 1.0 out the door, I would love to get some more of those SSR capabilities into Redwood itself to be able to, on a per-route basis,
[2452.66 → 2457.60] essentially specify what characteristics you want, whether you want it to be pre-rendered, which you can currently do.
[2457.60 → 2462.84] And you just say pre-render in the route, you just add pre-render to it, and now we'll pre-render at build time.
[2463.26 → 2470.78] And that'll be delivered out to whatever your deployment provider is in the right kind of way for that to be delivered as HTML and then rehydrated.
[2471.44 → 2478.96] But I'd love you to be able to say, I want this to be server rendered as HTML and delivered in that capacity in a similar kind of way.
[2478.96 → 2492.02] Now there's some challenges and weirdness around that because of GraphQL, where it's like, okay, now the server is going to execute the page, and it has to talk GraphQL to itself?
[2492.30 → 2493.70] Like that's potentially a little weird.
[2493.78 → 2498.90] So then I was thinking, well, maybe you can drop GraphQL, and it can talk to the services directly.
[2498.90 → 2506.26] Because in Redwood, the way that you implement your GraphQL API is really in a very JavaScript-y way.
[2506.40 → 2514.10] So if you've ever done this before via resolvers and like Apollo Server or something, you're essentially providing it a bunch of functions that are the resolvers.
[2514.56 → 2517.44] But you have to pass it arguments that are in a kind of weird way.
[2517.52 → 2524.20] Like there's no way that you can really reuse any of that logic in other places because you're all just stuffed into these resolvers.
[2524.20 → 2534.98] And so with Redwood, we've added a level of abstraction on top of that so that when you're implementing your resolvers, they look like just regular JavaScript calls.
[2535.18 → 2538.18] And they receive an object of arguments.
[2538.54 → 2543.14] And then the other stuff that you might pass into the resolvers as additional arguments.
[2543.64 → 2552.90] But the reason that this is nice is that you can now call those resolver functions from other places in the code.
[2552.90 → 2556.78] So let's say you have a GraphQL mutation to add.
[2557.34 → 2561.58] Let's say you're writing a blog engine, and you have something that's going to add a blog post.
[2561.96 → 2565.20] That's something that you might want to be able to trigger from somewhere else in the code base.
[2565.50 → 2571.72] If you've got that stuffed as just this function that's being passed or implemented in a resolver, it's like, how do you reuse that?
[2571.78 → 2577.36] So code reuse becomes really challenging in kind of the simplest way that you would write your GraphQL resolvers.
[2577.80 → 2580.52] But in Redwood, it's really just how things are named.
[2580.52 → 2588.18] So if you name a function a certain way that matches what it is in the SDL, then we'll match those two things up.
[2588.44 → 2589.74] And that's done automatically for you.
[2589.92 → 2595.62] But the signature of it is still done in a way that it makes it easy to call from other places in the back end.
[2595.74 → 2602.14] So you could have some other function be calling your add a blog post function the way that you would normally in JavaScript.
[2602.46 → 2607.66] But because it's named a certain way, then it gets picked up by the thing that exposes the GraphQL.
[2608.22 → 2609.50] Yeah, that's fascinating.
[2609.50 → 2616.20] Right. So I think Next and Remix and these folks often, their server side rendering, it's still the client, right?
[2616.20 → 2618.46] They're still rendering a client and expecting to have an API.
[2618.60 → 2620.80] And then they do have endpoints you can call for the API.
[2621.50 → 2624.10] But I think that is still like a that's a network call.
[2624.10 → 2626.04] And it's probably a local thing rather.
[2626.04 → 2637.46] But what I'm hearing here is you could potentially kind of sub out the GraphQL client to have a server side rendering client that just calls directly into those functions.
[2637.74 → 2639.92] So it's just running same process JavaScript.
[2640.08 → 2642.50] You don't have that little network call or anything.
[2642.50 → 2651.56] Yeah, it's more like, I mean, in Next, if you're doing the server side where you get the server props, essentially, you know, it's just it's going to execute that on the server directly.
[2651.56 → 2653.68] And it's going to do whatever that you have in there.
[2653.78 → 2656.22] Usually you're fetching data from a database or something.
[2656.22 → 2662.16] In the same way, we could have Redwood allow you to do on the web page.
[2662.22 → 2668.22] If you're using cells, then you're going to provide it a GraphQL query, and it's going to do the network call.
[2668.22 → 2671.70] And then you're going to get the data back and that's going to go into your success component.
[2672.36 → 2679.14] Is there a way that we can that depending on the GraphQL call, like it gets like these are things that we're thinking about right now.
[2679.14 → 2687.44] Like, is there a way to cut out the GraphQL query in that regard and have you specify it more as just a function call?
[2687.64 → 2690.62] So maybe you know that it's going to be done server side.
[2690.70 → 2692.96] And so you're not using Graph, you're not even using GraphQL.
[2693.08 → 2696.56] You're just allowed to call the services directly because you know that you're in that execution environment.
[2697.12 → 2698.18] That's the hard part, right?
[2698.22 → 2709.04] Like, I mean, there are things about Spas that are annoying, especially around hydration, where you have to now be sure that your page can execute in both a browser and a node.
[2709.62 → 2715.82] Environment, which can be fraught for, you know, if you don't know that that's going to happen, then you're like, I'm going to use this library.
[2715.82 → 2719.38] And you're like, oh, you can't use that library on the browser, right?
[2719.82 → 2720.60] That's not a thing.
[2720.60 → 2723.02] And you're like, oh, well, I didn't like, how was I supposed to know that?
[2723.26 → 2725.32] So there are other things that we're thinking about around.
[2725.62 → 2736.30] How can you tell people in advance that this is going to happen, that something's going to have to be able to execute in two different environments and warn them if there's going to be a problem in doing that?
[2736.30 → 2738.36] So these are things.
[2738.36 → 2744.68] And then at the same time, though, I get interested about other approaches to front end like quick.
[2744.84 → 2752.98] Q-W-I-K is a new sort of experimental front end that is trying to deliver as little JavaScript as possible.
[2752.98 → 2754.52] So in that way, it's a little bit like svelte.
[2755.04 → 2759.26] But it does hydration, but it does it by resuming.
[2759.94 → 2770.72] So it's not building the whole page on the server and then delivering that and then basically rebuilding the whole page in React on the browser and then like repainting with basically the same thing.
[2770.72 → 2772.14] It's really resuming.
[2772.14 → 2774.12] So it's not having to rebuild on the client.
[2774.20 → 2778.22] It's just resuming the execution essentially where it left off on the server.
[2778.36 → 2787.02] So you can get kind of these advantages of the server and client interaction without having to waste cycles in doing that.
[2787.02 → 2788.86] So that that's really early still.
[2788.94 → 2792.92] But I like the architecture of Redwood because it allows us to explore these things.
[2792.92 → 2795.40] So like maybe in a year we're like, you know what?
[2796.00 → 2797.06] React is dead.
[2797.06 → 2800.02] And now quick is where it's at.
[2800.16 → 2801.98] We don't have to replace any of the back end stuff.
[2802.08 → 2804.12] The back end stuff in Redwood is all great.
[2804.24 → 2804.34] Right.
[2804.48 → 2805.80] And you don't even have to use the front end.
[2805.84 → 2806.02] Right.
[2806.06 → 2813.74] If you don't like the React web side, throw it away and build your thing in view or svelte or whatever you want.
[2814.06 → 2820.14] Or maybe you only have a React or a mobile, a native mobile client or a native desktop client.
[2820.34 → 2826.34] Don't use the front end stuff that we have in Redwood at all and use it for the API because it is amazing at that.
[2826.34 → 2831.80] If you just use Redwood to be a GraphQL API implementation, that's a great place to be, too.
[2856.34 → 2857.70] With dashboards in seconds.
[2858.08 → 2860.94] Here's how engineering teams are using Code Insights.
[2861.26 → 2865.18] They can track migrations, adoption and deprecation across the code base.
[2865.26 → 2868.66] They can detect and track versions of languages or packages.
[2869.04 → 2872.48] They can ensure the removal of security vulnerabilities like Log4j.
[2872.76 → 2879.00] They can understand code by team, track code smells and health and visualize configurations and services.
[2879.58 → 2882.16] You know what the engineering manager at Prezi has to say about this new feature?
[2882.16 → 2890.10] Quote, as we've grown, so has a need to better track and communicate our progress and our goals across the engineering team and the broader company.
[2890.52 → 2895.60] With Code Insights, our data and migration tracking is accurate across our entire code base.
[2895.70 → 2902.50] And our engineers and our managers can shift out of manual spreadsheets and spend more time working on code.
[2902.88 → 2903.26] End quote.
[2903.26 → 2907.54] The next step is to see how other teams are using this awesome feature.
[2907.54 → 2912.66] Head to about.sourcegraph.com slash code dash insights.
[2912.94 → 2914.40] This link will be in the show notes.
[2914.52 → 2919.20] Again, about.sourcegraph.com slash code dash insights.
[2919.50 → 2921.48] And by our friends at Ray gun.
[2921.76 → 2926.80] They give software teams instant visibility into the quality and the performance of their software.
[2926.80 → 2930.70] And I'm here with John Daniel Track, co-founder and CEO of Ray gun.
[2931.02 → 2942.08] JD, talk to me about the joy a team feels when they're able to find and resolve an issue, even before a customer has a chance to get upset or reach out to support about the issue.
[2942.38 → 2943.06] Talk to me about that.
[2943.34 → 2946.30] Well, I find it pretty exciting to be able to hit it off early.
[2946.30 → 2948.86] So, and being able to tell people that you resolved something.
[2949.00 → 2951.86] So, maybe they come through, you know, and they do report an issue.
[2952.12 → 2955.04] And you can say, cool, we don't need to ask you for any more context.
[2955.20 → 2957.44] We've got all the details, and can have this fixed tomorrow.
[2957.72 → 2960.70] It turns an at-risk customer into an absolute raving advocate.
[2961.04 → 2962.04] So, that's a huge win.
[2962.18 → 2963.94] And then the other thing that was a little bit embarrassing.
[2964.22 → 2967.62] We launched Ray gun, but we had these other products and we instrumented them.
[2968.08 → 2972.36] And that's when we realized that less than 1% of our users would ever actually report a problem.
[2972.74 → 2975.50] And so, you're sitting there thinking your software is actually not bad.
[2975.50 → 2978.34] And actually, it's really, terrible.
[2978.44 → 2981.70] And that's hurting all of your conversion rates, business performance here.
[2981.82 → 2982.78] These aren't really dev tools.
[2982.88 → 2984.08] They're actually business tools.
[2984.50 → 2984.78] All right.
[2984.78 → 2989.56] If you want to see how this dev tool impacts the entire business, head to raygun.com to learn more.
[2989.84 → 2991.78] And start your 14-day free trial.
[2991.88 → 2993.24] No credit card required.
[2993.68 → 2996.30] Join thousands of customer-centric software teams.
[2996.60 → 3000.78] We use Ray gun every single day to deliver flawless experiences to their customers.
[3000.96 → 3002.72] Again, raygun.com.
[3005.50 → 3024.32] So, I'd love to get a sense.
[3024.72 → 3028.04] You know, we talked a little bit in the end of here of like some of the things that are there.
[3028.04 → 3034.24] But what is the vision for Redwood 2.0 or 1.3 or wherever we're going?
[3034.62 → 3036.98] And I'm kind of curious to explore along three dimensions.
[3037.16 → 3039.48] So, one is like how are you organizing the project yourself?
[3039.60 → 3044.34] Because I think you're doing some unique things there in terms of how you're funding and things like that.
[3044.70 → 3047.92] What do you see as the future in that community aspect you've talked about?
[3048.02 → 3050.18] Maybe those are the same thing, or maybe they're something different.
[3050.18 → 3055.12] And then technically, what are the, you know, we've talked about all sorts of dimensions we could go.
[3055.26 → 3056.84] But what are the next 1, 2, 3?
[3056.96 → 3061.00] And then what's the like pie in the sky long-term vision?
[3061.54 → 3063.44] But maybe let's start on the organization.
[3064.16 → 3064.28] Yeah.
[3064.46 → 3072.08] So, one thing that's maybe a little interesting about Redwood organizationally is we have a fairly large core team.
[3072.18 → 3074.00] It's around 20 people right now.
[3074.00 → 3081.88] That's because we really like to invite in people from all kinds of backgrounds and experiences and especially skill level.
[3082.26 → 3087.80] So, we've had people on the core team that were essentially just out of a boot camp.
[3087.80 → 3091.98] And they come in, and they're able to do some things with the code.
[3092.10 → 3100.90] But they'll participate maybe more at first in the community aspect or in the outreach aspect where they're writing blog posts, or they're doing podcasts.
[3100.90 → 3107.66] And that's been really valuable for us to have that more beginner perspective for people to come in and say, like, this is confusing.
[3107.66 → 3108.98] Like, how does this work?
[3109.24 → 3114.98] That kind of feedback helps us really improve the documentation, make sure the tutorial is really rock solid.
[3115.10 → 3118.26] We've spent tons of time on the Redwood tutorial.
[3118.78 → 3127.74] It is one of my favourite things about Redwood is how much time we've spent making sure the tutorial is solid and that it's tested and it works.
[3127.74 → 3132.84] And it's really enjoyable, and we've produced videos around it in case you just want to watch it.
[3133.40 → 3135.04] Spent tons and tons of time on the tutorial.
[3135.54 → 3141.16] And those things are great because of the different experiences of the core team members.
[3141.60 → 3144.18] And so, people come and go out of the core team.
[3144.58 → 3148.16] And we like that because we like giving people opportunities.
[3148.42 → 3156.72] I mean, a big part of why I do this at all is because I love building tools and I love giving people opportunities.
[3156.72 → 3178.50] And so, anyone who comes in that wants to level up, that wants to contribute and be a part of this, and if I can help them succeed in that way and land a job, which a bunch of people that have come into the core team that were more junior on their path were able to land jobs because of their involvement in Redwood on the core team.
[3178.50 → 3208.48] And that gives me a great deal.
[3208.48 → 3220.44] These relationships that then turn into people that come on to the core team, people that can be successful in a way that is more organized than you'll generally see in an open source project.
[3220.88 → 3223.28] So, organizationally, that's kind of how we are.
[3223.38 → 3224.40] We have a core.
[3225.02 → 3233.38] Within the core, there's maybe a deeper core of people that are involved every day and people that I pay to work on the framework.
[3233.38 → 3237.12] And then we have a larger core of people beyond that.
[3237.20 → 3240.94] And then we have our larger set of overall contributors.
[3241.42 → 3246.18] But we spend a lot of time trying to make it easy to contribute to Redwood.
[3246.18 → 3263.40] So, we've done a ton of work to make it possible to get the framework up and running and alongside a test project so that you can make changes to the framework and then see that in an example application, which is not a small feat in the world of JavaScript because of the way that NPM works or Yarn.
[3263.96 → 3273.78] The way that that works makes it really difficult to get a dependency local so that you can make changes to the dependency and have it reflected in your actual application.
[3273.78 → 3275.56] Like, that is a monumental nightmare.
[3275.92 → 3278.44] And we've gone through several iterations of making that possible.
[3278.56 → 3279.48] And it's really smooth now.
[3279.52 → 3291.64] And especially with Gitpod, now you can go on there, and you can spin up a workspace in Gitpod and be working on the framework itself in a matter of 30 seconds.
[3292.20 → 3295.32] And you're working alongside a test project and the whole thing is set up.
[3295.36 → 3297.08] And you can also test pull requests this way.
[3297.08 → 3305.24] You can spin up any of the pull requests on Redwood in Gitpod and immediately be testing it in a live environment on Gitpod.
[3305.32 → 3311.38] So, we spent just a huge amount of effort making it as easy as possible for contributors to come in and get started.
[3312.06 → 3326.76] And David runs a series that he used to do every two to three weeks when he'd spend an hour with people who expressed interest in becoming contributors going through this whole process so that people would be set up to be able to work on the framework itself.
[3326.76 → 3336.32] So, we've spent more time and effort than I think most in working on the contributors community and making it possible for people to get started.
[3336.38 → 3337.04] Because it's not easy.
[3337.12 → 3342.54] Coming into a large, complex framework and contributing to it is non-trivial, shall we say.
[3342.76 → 3343.10] Totally.
[3343.50 → 3345.18] Yeah, I love to hear about that.
[3345.44 → 3348.10] Community-wise, what are you working on there?
[3348.18 → 3349.74] So, that's sort of the community of the framework.
[3350.04 → 3352.02] But you've also talked about this community of startups.
[3352.28 → 3355.36] So, where is that something that is actively evolving?
[3355.36 → 3356.98] Do you have a vision for where that's going?
[3357.80 → 3357.92] Yeah.
[3358.04 → 3363.74] So, we have, let's say, there's about 30 startups that we know of that are building with Redwood right now.
[3363.76 → 3371.56] And we try to track as many as we can to get a sense of, is this angle of optimizing for startups, is that working?
[3371.70 → 3372.52] Like, are they out there?
[3372.56 → 3374.44] Are people choosing Redwood and building with it?
[3374.48 → 3375.14] We want to know.
[3375.28 → 3379.24] This is helpful for us to build the future of Redwood.
[3379.24 → 3386.68] So, we know of 30, I think it's 31 at the moment, 31 startups that are building actual real startups with Redwood.
[3386.78 → 3388.48] Many of those are funded.
[3388.82 → 3395.94] The last time we got the numbers, it was about 19 million of funding that Redwood-based startups had raised.
[3396.06 → 3397.24] This was right before the 1.0.
[3397.28 → 3397.94] So, that was a month ago.
[3398.02 → 3401.30] So, that's probably increased from there.
[3401.92 → 3402.58] But it's working.
[3402.74 → 3403.98] People are building with Redwood.
[3403.98 → 3406.88] And they come in, and the feedback is generally very positive.
[3407.00 → 3410.26] They're very happy with Redwood and their choice in doing that.
[3410.34 → 3418.78] And a lot of it is because of the technology and that it's, especially the multi-client, the GraphQL stuff is really important to a lot of people and how easy we make that side of it.
[3419.24 → 3424.14] But then the community as well and how open we are to people being involved.
[3424.14 → 3431.70] And when people make a choice of a framework like this for their company, they want to know that they are going to be heard.
[3431.98 → 3436.06] That they can come in, and they can fix things that are broken if there's something that's affecting them.
[3436.54 → 3443.72] That the core team is going to be responsive to say, oh, like you have a need for your company, for your business.
[3444.14 → 3446.08] We're willing to accept your pull requests.
[3446.26 → 3450.54] We're willing to engage you and help you in getting those things fixed.
[3450.54 → 3455.30] That ends up being really important to people when they're making a choice for the long term.
[3455.84 → 3456.68] A business choice.
[3456.74 → 3459.84] Something that's going to affect the success of their business.
[3460.00 → 3460.98] So that's been really important.
[3461.16 → 3464.98] And so we're continuously growing the Redwood Startup Club.
[3465.66 → 3471.42] We also do, we have a community member, Keith, who works on the Maker Hour.
[3471.42 → 3479.58] So which is kind of a that's a bit more of an open forum for anyone who's tinkering with Redwood or building anything with Redwood.
[3479.68 → 3483.62] Not necessarily that, you know, they've committed to doing a startup, and they're growing a team or whatever.
[3483.86 → 3484.90] That's the startup club.
[3485.38 → 3494.38] The Maker's Hour is more just like, yeah, you're doing whatever you're doing with Redwood and you want to talk to other people about it or share what you're doing to be motivated.
[3495.00 → 3500.30] And so there's a group of people that often come to the Maker's Hour to come share that.
[3500.30 → 3507.44] We have, there's also a Spanish language version of that, that we have a community member leading now, which is pretty awesome to see.
[3507.58 → 3508.92] And then we also do office hours.
[3509.04 → 3522.58] So some of the core team members will get together every week and do office hours on Discord so that anyone can come in with any other questions and just have someone available from the core team to be able to answer those.
[3522.82 → 3529.66] So we have a Discord where we have an active chat community where people come in, and we'll do some events and things in there.
[3529.66 → 3554.46] That's a great place to just meet other Redwood developers, ask simple questions and get help or get pointed to the discourse forum software where we really have this ever-growing knowledge base that is the better place for asking questions and getting answers that may be a bit more complicated than you might ask in the chat and Discord.
[3554.46 → 3559.90] That we chose because we wanted it to be indexed across time.
[3560.66 → 3564.50] And so this is a great, this is where a lot of people land when they're searching for things about Redwood.
[3564.64 → 3566.92] Like, I have this question, how do I implement this thing?
[3566.94 → 3569.48] Or what service should I choose for this other thing?
[3569.50 → 3570.94] Or like, how do I, whatever.
[3571.46 → 3574.80] Then you'll often end up in the forum and that's on purpose.
[3575.04 → 3578.58] We wanted that to be this long-term growing resource that's indexed.
[3578.58 → 3579.44] It's searchable.
[3580.18 → 3585.12] So all of these things are part of the community that we've assembled.
[3585.30 → 3587.56] And that's all going to plan.
[3587.68 → 3588.68] It's hard to grow a community.
[3589.04 → 3590.94] It's in open source.
[3591.60 → 3593.44] It's especially hard from a diversity of perspective.
[3593.44 → 3598.04] And we've worked really hard to try to increase the diversity of who we see in our community.
[3598.04 → 3606.76] But it is still overwhelmingly white and male, which we're always trying to counterbalance with outreach to other communities.
[3607.42 → 3618.14] And this maybe segues me into the Redwood Startup Fund, which I can talk about, which is a purposeful effort to increase the diversity of who we see, especially as startup founders.
[3618.14 → 3639.76] So the Redwood Startup Fund I announced when we launched the 1.0, this is a $1 million investment fund that I'll run alongside the angel investing that I do, where I intend to write $25,000 to $50,000 checks to startups that are using Redwood in their stack to encourage people to build with Redwood, obviously.
[3640.14 → 3644.56] But to also fill out the latter part of the startup journey that we can offer directly.
[3644.78 → 3648.02] Up until then, we could offer you technology to build with.
[3648.02 → 3655.08] We could offer you a community and help to think about and strategize about and connect you with people in the startup and investment community.
[3655.08 → 3657.50] But we couldn't give you actual money directly.
[3657.50 → 3659.42] That was not part of what we could really offer.
[3659.86 → 3671.22] Now with the startup fund, we can, for those startups that we really believe in, that we think can go the farthest, we have money available directly to fund.
[3671.40 → 3674.22] So $25,000 to $50,000 checks really early.
[3674.22 → 3683.58] I'm hoping this can be super early stage funding, maybe before you've even incorporated your thing or even written much code around it.
[3683.58 → 3689.20] And I'd like to prioritize a more diverse set of people that are building.
[3689.20 → 3703.94] So more women founders, more black founders, other minorities groups in the software development community that want to come in and do that, but may otherwise not have the option to do that because of whatever constraints they have.
[3703.94 → 3709.04] Or just to have someone who believes in you that has some money to where you can get started and try out an idea.
[3709.46 → 3716.08] This money is intended to increase the diversity of the community directly through how we prioritize who gets that money.
[3716.68 → 3724.48] And the other side of that is I'd like to prioritize startups that are working on climate-related things with the software that they're building.
[3724.48 → 3731.84] This investment is run through Preston Warner Ventures, which is the entity that I use for angel investing.
[3732.50 → 3734.62] We also do a lot of work around climate.
[3734.90 → 3742.52] We have a team of 10 people at Preston Warner Ventures where we do grants around climate as well as political work to try to move the needle on climate change.
[3742.62 → 3749.56] This is a primary focus of what we do with the Preston Warner Ventures effort that my wife and I run.
[3749.56 → 3764.32] And so I'm trying to dovetail all of these things together, sort of combine the open source work that I love to do with the angel investing that I love to do with the climate work that I think we have to do and try to pull them all together into a tighter bundle of things.
[3764.42 → 3765.84] And so that's the startup fund.
[3765.92 → 3774.32] So that's another part of community building and trying to purposefully evolve the community into what I think is a healthy direction.
[3775.42 → 3778.70] Well, let's close talking a little bit about the technical future.
[3778.70 → 3782.12] What do you see coming next in the framework itself?
[3782.24 → 3784.98] What are the focus areas for, say, the next six months?
[3785.20 → 3792.06] And then if you haven't already covered them, are there any things that you see as like, ooh, we've got to get there someday?
[3792.84 → 3793.66] Yeah, there's lots.
[3793.76 → 3805.38] So one of the biggest things on my mind is some kind of SSR type of solution, whether that be something that we can bake into Redwood itself and make it really easy on a per-route basis.
[3805.38 → 3810.96] That's a little complicated because of the architecture of Redwood, the GraphQL choices that we've made.
[3810.96 → 3824.94] Or is it just making it possible to use Next.js as another website and then making whatever integrations we need there to allow you to use Next.js in a more official capacity?
[3825.38 → 3832.12] Just some story around you have certain needs around SSR because of what you're doing and making that possible.
[3832.12 → 3835.36] So we'll be doing a lot of thinking about that in the near term.
[3835.36 → 3846.32] We've been going over this with the startups that we've been talking to and then in the community in general, just trying to think about like, what are the next biggest things for the roadmap?
[3846.32 → 3855.22] Because I want to really be driven by the people using Redwood and their needs, especially if you've chosen Redwood, and we've made this promise to you that we're going to help you build your startup.
[3855.22 → 3863.60] Then it's incumbent on us to keep building the things that you as your company evolves, and you're using Redwood that you're going to need as time goes on.
[3863.78 → 3868.56] So a lot of those things end up looking like scale, like what do you need at scale?
[3868.72 → 3873.56] So that's why we think about SSR, but other types of caching as well.
[3873.74 → 3878.86] So it's possible to do GraphQL caching, GraphQL layer caching with Redwood right now.
[3878.86 → 3892.42] There are some how-tos on the website in the docs about how you can hook that up to a Regis, for instance, to do GraphQL caching in a very similar way to Graph CDN, the company that is doing GraphQL caching.
[3893.06 → 3894.24] Graph CDN is great.
[3894.24 → 3908.64] If you want to have more control over it, then you can actually do GraphQL layer caching with Redwood itself via a plugin to Yoga, which is the GraphQL framework that we use now.
[3908.80 → 3917.42] We started with Apollo Server, and now we're using stuff from The Guild, who are amazing, and we work very closely with over there to be the GraphQL web server.
[3917.94 → 3919.48] So there are things around that.
[3919.72 → 3923.40] Improvements to testing, adding in additional sides.
[3923.40 → 3937.70] A lot of people want a native mobile side, and they're waiting for that, for us to say, all right, here's the React Native side and here's how it integrates and here's how we're going to make it improve the DX of building a React Native client alongside that.
[3937.88 → 3942.00] That is one of the most requested things right now.
[3942.64 → 3953.04] Things we talked about before, like waterfall, like how can you improve the overall, like if you have a page that's going to be doing multiple different GraphQL calls that don't need to wait for each other.
[3953.40 → 3954.82] But they're nested.
[3954.90 → 3957.60] How can we gather those up and do them for you simultaneously?
[3958.26 → 3962.70] So that's a bit of research that I'd love to do in that regard.
[3962.88 → 3972.76] I mean, there are a lot of just bug fixes and kind of small improvements to all the different aspects where it's like, oh, there's some missing bit of how you do your testing.
[3972.76 → 3974.98] How do we fill that in?
[3975.10 → 3981.34] So a lot of the work will just be working through the backlog of issues and pull requests that are outstanding.
[3981.44 → 3988.50] Now that we have some time to stand back and say, all right, let's now that the push for 1.0 is over, where are we going to go from there?
[3988.50 → 4005.52] So we're really in the phase of nailing down what the roadmap for the next three to six months looks like right now, now that we can take a breath from getting 1.0 out the door and really talk to the startups and people using it.
[4005.52 → 4011.48] So I can't paint for you a really solid picture of exactly what those choices are going to be.
[4011.74 → 4013.64] But that's a flavour of some of them.
[4013.70 → 4021.14] And there's just so much room to improve still in the world of JavaScript frameworks.
[4021.14 → 4026.90] I feel like it's only when we started two years ago, there were others that started around that same time.
[4027.02 → 4031.68] So now we start to see a lot more people thinking about and doing integrations around this.
[4031.74 → 4036.98] It's just it's really nice to see finally this coalescing of some of these ideas happen in the community.
[4036.98 → 4047.92] Yeah, it feels like the pace of innovation at the sort of UI framework level of like React versus Vue versus Svelte has slowed down.
[4048.04 → 4058.30] And now there's all this interesting innovation happening at the application layer of just like how do you or frame, I guess, application framework layer of how do you package these things together into a useful application?
[4058.88 → 4059.40] Right, exactly.
[4059.50 → 4060.30] Which is great, right?
[4060.32 → 4061.36] That saves people time.
[4061.56 → 4061.86] Awesome.
[4062.06 → 4066.04] Well, is there anything else you'd like to leave JS Party listeners with about Redwood?
[4066.04 → 4072.22] I'll just say if you find any of this stuff interesting, come visit the website redwoodjs.com.
[4072.36 → 4073.18] Do the tutorial.
[4073.36 → 4080.54] So if there's one thing that I would like you to have as a takeaway from this is if you are intrigued, go do the tutorial on the website.
[4080.88 → 4081.56] You're going to love it.
[4081.64 → 4091.20] It goes through all the primary aspects of what makes Redwood different and special and is a great introduction to the various technologies that we have in there.
[4091.20 → 4096.92] There's a really great section on testing that is, you know, if you haven't done a lot of testing before, and you're like, man, I should really be doing testing.
[4097.50 → 4101.58] Go do the Redwood JS tutorial or read the testing documentation.
[4102.12 → 4107.14] It's written by Rob Cameron, who's the same person on the core team co-creator that wrote the tutorial.
[4107.14 → 4111.52] And he's just a master of communicating these complex technical ideas.
[4111.66 → 4120.98] And it's just a great intro to testing with JavaScript with Jest, the testing documentation on the Redwood documentation site.
[4121.66 → 4123.26] So come do the tutorial.
[4123.56 → 4124.88] That's the number one thing.
[4125.06 → 4127.74] And once you do that, then you'll know whether Redwood is for you or not.
[4127.96 → 4129.40] If you find it awesome, then great.
[4129.40 → 4130.74] Like, come join the community.
[4130.94 → 4136.32] Come pop in Discord and say hello or ask any questions that you have.
[4136.74 → 4139.72] We would love for you to be a part of the community.
[4140.36 → 4145.16] And I just, I get a lot of satisfaction out of building stuff.
[4145.26 → 4146.76] It's what I, it's my favourite thing.
[4147.16 → 4153.30] Going, creating something from nothing is the thing that drives me the most besides just learning things in general.
[4153.30 → 4166.50] And it's just so pleasurable for me to build things that other people are using and enjoying and taking people's feedback and continuing to improve and exploring new ideas and helping people explore the territory of whatever is interesting to them.
[4166.76 → 4169.22] So we'd love to have you involved in the community.
[4169.46 → 4171.00] Please come by, do the tutorial.
[4171.34 → 4171.48] Awesome.
[4171.78 → 4177.68] And we will, of course, include links to the tutorial and the Discord and all the things mentioned today in our show notes.
[4177.88 → 4178.94] This has been fun.
[4179.16 → 4180.92] Thank you so much, Tom, for joining me today.
[4180.92 → 4185.28] And I'm looking forward to, I guess, myself going and doing the tutorial.
[4185.56 → 4189.38] I took some looks early on when we talked, but then haven't had time to touch recently.
[4189.56 → 4193.38] So I will dig into that and look forward to seeing what comes next.
[4193.84 → 4194.24] All right.
[4194.28 → 4197.00] And you can even watch the tutorial with the videos.
[4197.12 → 4199.88] You don't even have to do the tutorial yourself if you don't want to.
[4199.94 → 4201.06] So that's a great way to do it as well.
[4201.48 → 4202.98] Thanks so much for having me.
[4203.34 → 4203.90] This was really great.
[4208.98 → 4210.42] That's Genius Party for this week.
[4210.42 → 4211.84] Thanks for hanging with us.
[4212.28 → 4214.02] Now is the time to subscribe.
[4214.26 → 4218.22] If you haven't already, head to jsparty.fm for all the ways.
[4218.80 → 4223.20] If you dig this show, and you're not subscribed to the changelog, let's fix that bug.
[4223.40 → 4231.30] We have some amazing conversations with brilliant people like Paul Orlando, who writes about unintended consequences when systems operate at scale.
[4231.30 → 4235.92] The story behind the cobra effect is something that, as far as we know, never happened.
[4236.26 → 4240.00] But the story is during colonial India.
[4240.22 → 4248.90] So when the British were in India, some British administrator decided that they wanted to reduce or eliminate the number of cobras.
[4248.90 → 4250.94] Maybe this is in Delhi.
[4251.16 → 4252.28] I'm not sure where.
[4253.44 → 4258.38] And so to try to achieve that goal, they put up a bounty.
[4258.62 → 4262.34] They say, OK, I'm going to pay a bounty if you show up with a cobra skin.
[4262.34 → 4264.50] And that's going to get rid of the cobras.
[4264.50 → 4276.92] And then the story, of course, is, well, people discovered, oh, so I should just raise cobras and turn them in for the bounty and raise more cobras and turn them in.
[4277.22 → 4278.86] And then the British realize what's happening.
[4279.14 → 4282.54] They eliminate the bounty and then everybody releases the cobras.
[4282.94 → 4284.08] And so you have a worse problem.
[4284.08 → 4289.16] That episode lives at changelog.fm slash 474.
[4289.30 → 4295.76] Thanks again to Vastly for their awesome CDN, to Break master Cylinder for these epic beats, and to you for listening.
[4296.14 → 4296.96] We appreciate you.
[4297.32 → 4303.60] Next up on the pod, Six returns, and he's helping us fit a narrative around the different ages of JavaScript.
[4304.08 → 4307.12] Where we've been, where we are, and where we're maybe headed.
[4307.76 → 4308.50] Stay tuned for that.
[4308.56 → 4309.06] It's a good one.
[4309.26 → 4310.68] We'll have it ready for you next week.
[4314.08 → 4318.48] Game on.
