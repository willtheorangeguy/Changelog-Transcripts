[0.08 → 5.72] Hey, how's it going? I'm your host, Gerhard LSU, and you're listening to Ship It, a podcast
[5.72 → 11.66] about getting your best ideas into the world and seeing what happens. We talk about code,
[11.96 → 18.00] ops, infrastructure, and the people that make it happen. Yes, we focus on the people because
[18.00 → 23.34] everything else is an implementation detail. Core infrastructure is the type of software
[23.34 → 29.20] that many services depend on. If it breaks, everything gets affected. Think an operating
[29.20 → 33.80] system update, which looks good at first, but then everything starts getting slower by the hour.
[34.30 → 39.24] Maybe there is a messaging system at the heart of a stack, which is trusted with billions of
[39.24 → 44.26] transactions per day, and one upgrade later, transactions start failing randomly for no
[44.26 → 49.60] obvious reason. One aspect which makes debugging this really hard is that sometimes different
[49.60 → 55.70] versions of software simply don't work well together. Combine some enterprise OS with an older
[55.70 → 62.24] rock-solid Linux kernel, and a code VM, which has some IO optimizations a decade younger.
[62.76 → 68.38] And you could be looking at weeks of debugging. I know because I did just this a few months ago,
[68.44 → 73.12] and it wasn't easy to get to the bottom of it. Today, we talk with Jean-Sébastien Patron,
[73.48 → 79.26] a RabbitMQ and FreeBSD contributor, about the importance of good release engineering for core
[79.26 → 85.16] infrastructure. As the years went by, it became clearer to us just how important this is. That's
[85.16 → 90.38] right. Both myself and Jean-Sébastien have been part of the Core RabbitMQ team for many years now.
[90.70 → 95.46] We have built some of the biggest CI-CD pipelines, checked the show notes to see one example,
[95.92 → 101.40] wrote and shipped some great code together, while breaking and fixing many things in the process.
[101.64 → 108.72] We have been wrestling with this topic since 2016. Jean-Sébastien has some great FreeBSD stories to share as well,
[108.72 → 115.58] and he has a very interesting perspective on shipping graphic card drivers. Oh, and by the way,
[115.58 → 122.16] it's probably our fault why your remote car key stopped working that afternoon. It will all make
[122.16 → 127.24] sense after you listen to this. Big thanks to our partners Vastly, Launch Darkly, and Linde.
[127.46 → 134.16] Our bandwidth is provided by Vastly, learn more at Fastly.com, feature flags powered by LaunchDarkly.com,
[134.16 → 140.90] and we love Linde. They keep it fast and simple. Check them out at linode.com forward slash changelog.
[140.90 → 153.00] What's up, Shippers? This episode is brought to you by our friends at Fly. Fly lets you deploy your apps
[153.00 → 160.08] and databases close to your users in minutes. You can run your Ruby, Go, Node, Demo, Python,
[160.52 → 166.70] or Elixir app and databases all over the world. No ops required. Fly's vision is that all apps should run
[166.70 → 171.18] closer to their users. They have generous free tiers for most services, so you can easily prove to
[171.18 → 175.76] yourself and your team that the Fly platform has everything you need to run your app globally.
[176.18 → 180.82] Learn more at fly.io slash changelog, and check out the speed run and their excellent docs.
[181.24 → 184.56] Again, fly.io slash changelog, or check the show notes for links.
[187.56 → 191.68] We are going to ship in three, two, one.
[191.68 → 212.52] So, end of 2016, I have joined this new team of developers, and they were the RabbitMQ core developers.
[212.98 → 219.02] And the context of that meeting was the RabbitMQ team summit, which is something that used to happen
[219.02 → 225.70] every six months, twice a year. But that stopped, obviously, since the pandemic and all the changes,
[225.82 → 231.32] all the recent changes. The one-person over the years that I really enjoyed working with is Jean
[231.32 → 238.86] Sébastien. And if you're wondering who you can thank for all the Makefile madness that I'm leaving
[238.86 → 244.84] in my trail, it's Jean Sébastien. He's the one that introduced me to make, and the rest is history,
[244.84 → 251.10] as they say. Not only that, but he also introduced me to the RabbitMQ code base, who were like pairing
[251.10 → 257.02] buddies for a long time. And I found about build system, about the pipeline, about many things.
[257.74 → 262.44] So, for the listeners, I mean, you've made it so far to this episode, and you're still wondering,
[262.78 → 267.98] what do I do? For those that don't know yet, this is where I tell you that my day job is to work
[267.98 → 274.66] on RabbitMQ. I'm a RabbitMQ core developer, same as Jean Sébastien. So, welcome, Jean Sébastien,
[275.30 → 278.06] joining me in this new world. Thank you very much.
[279.04 → 284.00] You're very welcome. I was looking forward to this for a long time, actually. And one of the topics
[284.00 → 289.72] that are very relevant to this show are release engineering. And this is something that both you
[289.72 → 295.12] and me have been thinking about for years in the context of RabbitMQ, and have been working on it
[295.12 → 301.52] in different capacities. And my first question is, why do you care about release engineering?
[301.52 → 308.92] I think it's an important part of a project, and in particular, an open source project.
[309.76 → 319.38] The first reason is that you want to ship your code to end users to help them solve their own
[319.38 → 329.94] problems. You want those users are happy with what you ship. And I think that to make that happen,
[330.50 → 338.90] you need to communicate well with those users, explain what you ship to them, like that new release
[338.90 → 346.70] contains these new features, that bug you hit, now it's fixed. You might be interested in that
[346.70 → 354.76] security vulnerabilities. And you also want that those users give you feedback on what you shipped,
[354.90 → 362.54] because that's how you can also improve your code base and make the next version better than the
[362.54 → 369.48] current one. So yeah, that's what I would expect from a good release engineering. And I say that it's
[369.48 → 376.02] important for open source products, because you do not have any paying customers most of the time.
[376.02 → 387.68] So nobody is pressured to use what you produce and ship. So it's in the interest of the end users and
[387.68 → 390.86] you to have that great communication when you want to release something.
[391.48 → 395.52] I think that relationship is really important, right? The relationship of an open source developer
[395.52 → 401.08] with a user of open source. And that has gone through many ups and downs, I think, in the years.
[401.08 → 405.86] I don't know exactly where it stands now. But it is becoming increasingly important for these projects
[405.86 → 412.10] to somehow and products to somehow make money. Now, while release engineering for an open source
[412.10 → 418.14] product may not seem as important at first, because it's free, so why care, right? Actually,
[418.20 → 424.98] the opposite is true. The developers care a lot about these things. And once you have a certain
[424.98 → 433.28] number of users, which RabbitMQ has, these things become important. Because bugs can affect many users.
[434.02 → 439.62] And one of the ways that I think about RabbitMQ is a core infrastructure component. Typically,
[439.76 → 446.30] RabbitMQ is used in all sorts of systems, cars, even factories. You wouldn't expect payment systems.
[446.48 → 451.46] You don't even know where it's used. Only when it goes down, or only when there is a problem.
[451.46 → 456.50] Yeah. And this is not great. And from that perspective, it becomes increasingly important
[456.50 → 462.76] to communicate changes well, to be careful with the changes that get introduced, because many
[462.76 → 469.76] things can end up being broken. And usually, what tends to happen if developers are not careful about
[469.76 → 473.52] this aspect is that end users, they stop upgrading. Yeah.
[473.68 → 479.30] Right? I mean, if you experience problems or similar problems a couple of times, you're more reluctant
[479.30 → 486.54] to upgrade. Yeah, you will probably try to find alternatives to that project.
[486.54 → 486.90] That's right. Yes.
[486.90 → 494.46] Because this one was free. I mean, free. It didn't cost you any money. So you do not lose anything by
[494.46 → 501.16] switching. So, I mean, again, I view RabbitMQ as core infrastructure. But what does core infrastructure
[501.16 → 501.78] mean to you?
[502.20 → 509.20] I think I have the same definition as you. Core infrastructure is a component you rely on.
[509.30 → 516.38] To provide your service, for instance, if you're a company or even as someone at home,
[516.64 → 524.24] I rely on some core infrastructure just to run my own computers, even if it's not for work.
[524.38 → 531.80] I mean, for instance, as a company in the context of RabbitMQ, for instance, I expect that it's
[531.80 → 541.38] crystal clear what I get from RabbitMQ so that I'm confident when I want to deploy it, upgrade it,
[541.38 → 550.96] so that I can build my own business on top of that component. And this won't fall apart because of
[550.96 → 557.24] that core component, core infrastructure. And that's the same for any operating systems.
[557.24 → 568.64] Nobody likes when the operating system crashes. So, yeah, that's why we call them core infrastructure, in fact.
[569.12 → 574.24] Yeah. So I know that you have experience with RabbitMQ, but I don't know as much about your experience with
[574.24 → 579.20] FreeBSD because you're not just a RabbitMQ contributor, but also a FreeBSD contributor.
[579.20 → 586.44] Yes. So you have seen both sides of a messaging system, such as RabbitMQ, and an operating system,
[586.58 → 589.36] such as FreeBSD. So how do the two compare?
[590.06 → 598.20] So an operating system is like a very generic tool. You don't expect it to be the best in a specific
[598.20 → 606.68] area, but you expect it to behave well and be at least good in all areas.
[606.68 → 614.18] RabbitMQ is a bit different in that regard because we want to provide a very specific
[614.18 → 623.76] service in RabbitMQ. Also, FreeBSD, it's an old project with old manners and it's a big community.
[624.02 → 631.58] So it takes time for things and workflows to evolve. But in the end, we also want to ship
[631.58 → 640.44] an operating system, which will work for end users who use it at home and companies who build their
[640.44 → 647.14] businesses on top of it. So yeah, that's why the release engineering in FreeBSD is also very
[647.14 → 653.46] important. The goal is the same. How it is done is different. How you test things, obviously,
[653.46 → 655.22] you cannot compare both projects.
[656.32 → 665.40] So can you give me an example from your experience of release engineering gone wrong in both projects,
[665.84 → 668.16] if there is such a thing? I'm sure there is.
[668.80 → 674.94] So starting with RabbitMQ, I remember one release. I don't remember the version number,
[674.94 → 683.30] but at the same time we publish release, a new version of RabbitMQ with both a security bug fix
[683.30 → 693.78] and a break-in change. That was perfect, I'm sure, for admins who wanted to deploy that security bug fix
[693.78 → 701.14] as soon as possible. I think that's probably the worst case scenario.
[701.14 → 714.22] In FreeBSD, I remember the FreeBSD 5.0 release cycle because between FreeBSD 4 and 5, one of the big
[714.22 → 723.68] changes was to replace a global lock used all over the place in the kernel by fine-grade locking.
[723.68 → 730.96] And this went pretty bad because it took years to stabilize that work.
[732.04 → 738.60] In parallel to that, new version of FreeBSD 4 were cut and published,
[738.98 → 744.54] but it was really difficult for the project to ship something at that time because
[744.54 → 752.10] the code base was very unstable and nobody knew when we could cut even beta,
[752.10 → 754.38] let alone the final version.
[755.26 → 758.28] Yeah, it was a big problem because of that.
[758.54 → 762.70] It put pressure on people working on that code.
[763.68 → 766.72] Other people were tired because we didn't ship anything.
[767.56 → 772.96] And I'm sure end users were sad by that situation as well because some of them were
[772.96 → 775.60] looking forward to using the new version.
[775.60 → 780.02] Other users would see that disaster coming.
[780.64 → 788.10] And in the end, nobody wanted to use FreeBSD 5.0 because it was too uncertain what you could
[788.10 → 788.88] do with that.
[789.24 → 792.06] So I think that's a good example of a bad release engineering.
[792.06 → 798.60] I think you touched upon something fascinating, which is the longer you wait to ship something,
[799.20 → 804.24] the worse the release gets or the more problematic the release can become.
[804.42 → 804.48] Yeah.
[804.62 → 808.20] I don't know whether it becomes, it's not like a definite, but the longer you wait,
[808.30 → 810.66] the higher the chances the release will not be as good.
[810.66 → 810.98] Yeah.
[811.46 → 818.68] And I think that the most important part is that people are losing confidence, both developers
[818.68 → 823.06] working on that and users expecting the release.
[823.42 → 823.72] Yeah.
[823.76 → 829.50] I think we keep forgetting at the end of the day, it is people like you and me that are
[829.50 → 836.08] responsible for some pretty important systems that they have to, first, consume these
[836.08 → 840.90] updates somehow, understand what changes they're rolling out.
[841.52 → 844.06] And when something goes wrong, well, guess what?
[844.16 → 847.20] They're the ones responsible to fixing those problems.
[848.00 → 855.22] And I mean, they can blame the developers developing or like releasing their software, but ultimately
[855.22 → 860.12] they need to take certain precautions that, you know, things are rolled out in a good way.
[860.12 → 867.18] So the harder it is for these developers to roll out these changes or to start using like
[867.18 → 873.62] maybe new features, whatever it may be, the less likely they are to consume future changes.
[873.92 → 879.54] So it's almost like they enter a vicious cycle, but it's a negative one in that if it doesn't
[879.54 → 886.42] work as smooth and as consistent and as pain-free as user would like, like for example, your phone.
[886.42 → 892.32] If every time you upgraded your phone, your operating system on your phone, things would
[892.32 → 894.40] break, like, would you do it?
[894.98 → 895.10] No.
[895.38 → 895.66] No.
[895.74 → 898.10] If things would change in unexpected ways, would you do it?
[898.20 → 898.52] No.
[898.86 → 903.06] If you had to wait a really long time for an update, like let's say two years and then
[903.06 → 906.20] you applied it and then everything broke, would you do it again?
[906.46 → 906.84] No.
[907.72 → 915.48] So there is a very strong relationship between the happiness of end users and the release
[915.48 → 915.92] engineering.
[916.42 → 916.62] Yeah.
[916.62 → 919.00] Of the products and the systems that they use.
[919.10 → 919.42] Yeah, I agree.
[919.52 → 919.66] Okay.
[921.52 → 928.18] So if you had to say, if you had to pick one, I know it's an unfair comparison, but let's
[928.18 → 929.22] just go with it for the fun of it.
[929.50 → 933.32] What would you say is more core infrastructure, RabbitMQ or FreeBSD?
[934.32 → 936.84] It's a tough one.
[937.44 → 939.10] You can answer it any way you want, by the way.
[939.34 → 940.22] It's meant to be fun.
[940.32 → 941.36] It's not meant to be tough.
[941.36 → 951.28] I think it depends on if we stay in the company world, not end users and not people at home.
[951.42 → 956.36] I mean, it depends on what kind of service you provide on top of that.
[956.36 → 965.28] For instance, if we are taking a company using RabbitMQ for cars, like you mentioned earlier,
[965.82 → 974.06] in that case, RabbitMQ would be the most important one because you want all those devices and cars
[974.06 → 978.26] and computers to communicate properly.
[978.26 → 980.78] So I think that's the most important component.
[981.32 → 995.50] For a company like Sony, for instance, who is using FreeBSD in their PlayStation products, if the devices they ship to gamers crash all the time because the operating system is unstable,
[995.50 → 999.66] so it will be a very sad story for everyone.
[1000.18 → 1004.70] So in that kind of context, I think the operating system is important.
[1005.90 → 1009.66] I know that Netflix are other big users of FreeBSD.
[1010.32 → 1018.04] So imagine if you couldn't stream your Netflix because there was a bug in FreeBSD introduced, shipped worldwide across all their ports.
[1018.74 → 1023.74] WhatsApp is also using FreeBSD, but they are also exchanging messages.
[1023.74 → 1033.84] So in that company, if they were to use RabbitMQ, yeah, it would be more difficult to define which component is the most important.
[1034.10 → 1034.94] I would say RabbitMQ.
[1035.66 → 1039.26] I think they would get the best and worst of both components.
[1039.68 → 1043.10] So it depends on the combination of that, how well that would work out.
[1043.40 → 1044.24] But I see what you mean.
[1044.30 → 1044.92] I see what you mean.
[1045.02 → 1047.76] And for the listeners, this actually happened.
[1048.02 → 1050.22] Both myself and JSB, we were in Paris.
[1050.46 → 1051.86] JSB is from Paris, from France.
[1051.86 → 1056.34] And, sorry, JSB, that's how I refer to Jean-Sébastien.
[1056.70 → 1058.34] Do you know what JSB comes from?
[1058.48 → 1060.28] Actually, I don't think I've ever told you this.
[1060.78 → 1065.22] So JSB is obviously the abbreviation of Jean-Sébastien Pedro, your full name, JSB.
[1065.30 → 1065.52] Yes.
[1065.94 → 1070.02] But G, G-S-P, is actually Jean-Saint-Pierre.
[1070.40 → 1071.92] And he's an MMA fighter.
[1072.84 → 1078.04] And, yeah, I used to do his workouts many years before I even met you.
[1078.04 → 1081.74] So whenever I say JSP, I'm thinking, ah, Jean-Saint-Pierre.
[1081.90 → 1083.22] And, like, I should go for a workout.
[1083.60 → 1084.90] So that's something which happens.
[1085.66 → 1086.72] I know you never knew that.
[1086.78 → 1087.90] But anyway, that was a tangent.
[1088.40 → 1090.10] So coming back, coming back.
[1090.90 → 1091.98] We were in Paris.
[1091.98 → 1102.64] And we had to, well, not figure out, but help this customer, this RabbitMQ customer, to make sure that RabbitMQ will be reliable in all sorts of scenarios.
[1103.04 → 1109.38] Because cars would end up not getting unlocked from their car key, from the remote car key.
[1109.44 → 1115.10] Because RabbitMQ is involved in between the car and the key, RabbitMQ is exchanging messages.
[1115.52 → 1116.98] And you wouldn't think about that.
[1117.14 → 1118.64] And neither should you.
[1118.72 → 1119.54] Why would you, right?
[1119.54 → 1121.78] People don't really care about these things.
[1122.10 → 1124.72] And when everything works, it doesn't matter.
[1124.84 → 1126.88] When it doesn't work, that's when the problems start appearing.
[1127.14 → 1130.90] So that was a very interesting conversation and meeting, I have to say.
[1131.06 → 1132.38] I enjoyed it greatly.
[1133.22 → 1139.96] And especially that RabbitMQ is often used to also mitigate problems on both sides.
[1140.24 → 1145.60] The application emitting the message and the application consuming it.
[1146.30 → 1147.06] That's right.
[1147.36 → 1147.52] Yeah.
[1147.52 → 1148.74] If you have a problem in the middle.
[1148.74 → 1154.78] Yeah, I'm pretty sure that today, for example, you have used a system that behind the scenes uses RabbitMQ.
[1155.28 → 1159.38] And that's why we think of it as core infrastructure, because we know that it's everywhere.
[1159.84 → 1159.96] Yeah.
[1160.08 → 1162.00] And it works well in most cases.
[1162.30 → 1165.90] But as it happens, we get to find out about all the cases when it doesn't work.
[1166.16 → 1168.48] And then we have to fix it and then ship those fixes.
[1168.48 → 1170.58] So that's a very interesting perspective.
[1170.58 → 1181.88] What's up, shippers?
[1181.88 → 1185.56] This episode is brought to you by our friends at Teleport.
[1185.56 → 1190.20] With Teleport Access Plane, you can quickly access any computing resource anywhere.
[1190.66 → 1198.22] Engineers and security teams can unify access to SSH servers, Kubernetes clusters, web applications, and databases across all environments.
[1198.22 → 1201.34] Teleport is open core, which you can use for free.
[1201.34 → 1207.22] And it's supported by their cloud-hosted version, which lets you forget about configuring, updating, or managing Teleport.
[1207.44 → 1209.16] The Teleport team does all that for you.
[1209.42 → 1213.84] Your team can focus on your projects and spend less time worrying about infrastructure access.
[1214.44 → 1217.90] Try Teleport today in the cloud, self-hosted, or open source.
[1218.26 → 1220.96] Head to goteleport.com to learn more and get started.
[1220.96 → 1222.96] Again, goteleport.com.
[1232.32 → 1243.40] So we've been talking generally about the Rapid release engineering, the Freest one, how do they compare its projects, the whole core infrastructure notion.
[1244.10 → 1249.84] What I'm wondering now is, how does the Freest release engineering process look like?
[1249.84 → 1264.22] So after that Freest 5.0 disaster, the release engineering team started to work on something so that Freest never faces that situation again.
[1264.98 → 1268.24] And that process evolved a couple of times since.
[1269.26 → 1277.96] And today, the Freest release engineering is based on a fixed interval between major releases, also minor releases.
[1277.96 → 1284.96] And we don't expect to start on a very specific day at 8 a.m., for instance.
[1285.40 → 1291.38] The OpenBSD one is sharp as a Swiss clock, but not in FreeBSD.
[1291.62 → 1301.08] When we want to start to prepare the next release, we have release engineers, so someone who is hired by the FreeBSD Foundation and is paid for that.
[1301.08 → 1310.38] He will take care of announcing to the FreeBSD contributors, but not only the contributors, but the entire community.
[1310.92 → 1319.00] He will publish a calendar where he will state that the code slush will begin at this date.
[1319.34 → 1320.74] Code freeze will be this date.
[1320.74 → 1325.10] We expect to cut the first beta at this date.
[1325.10 → 1332.16] We expect perhaps two betas, then two release candidates, specifying, again, the date.
[1332.76 → 1337.88] And he will indicate as well the date for the final release of FreeBSD.
[1337.88 → 1345.84] So that calendar is updated on a regular basis while we make progress in that release cycle.
[1346.08 → 1357.48] For instance, if we discover that there are bugs or there is a security issue or whatever the reason, we might want to delay beta for a couple of days.
[1357.48 → 1363.76] Or we might want to add third or fourth beta or same for the release candidates and so on.
[1364.12 → 1374.70] So that calendar is very flexible, but it's quite useful because it tells to the FreeBSD contributors when to expect things.
[1374.94 → 1381.68] And it's very easy for contributors to organize and prioritize their tasks.
[1381.68 → 1394.60] For instance, if someone is working on some new features, then he knows that he has to finish by this date, or it will be delayed to the next release.
[1394.98 → 1397.20] So that's very helpful for contributors.
[1398.28 → 1401.02] And like I said, this is not that strict.
[1401.32 → 1406.90] So any contributors can communicate also to the release engineer what he's working on.
[1406.90 → 1413.58] And so that the release engineer knows that, OK, this specific patch is incoming.
[1413.86 → 1419.24] It might introduce some instabilities, but we want that in the release.
[1419.80 → 1430.08] So he can anticipate that and perhaps tell anyone that, OK, we expect this to come in the next couple of weeks.
[1430.42 → 1434.06] This will go in that beta, and we will add another one after that, for instance.
[1434.06 → 1446.28] So that calendar tool is really useful because it allows everyone in the community and the developers to communicate and understand what's going on.
[1446.50 → 1454.60] As I say, for users who will use that new version of FreeBSD, they can plan for testing, for instance.
[1455.40 → 1456.64] You mentioned Netflix.
[1456.64 → 1461.78] They appreciate that because they can test and invent the new feature.
[1461.92 → 1471.26] So they will fetch the development branch, for instance, compile FreeBSD and try it in their environment and see how it goes.
[1471.34 → 1473.14] They will give some feedback.
[1474.40 → 1486.56] So the fact that we use a calendar, a detailed calendar, yeah, it really helps the communication and makes the whole process more reliable and the outcome more reliable as well.
[1486.64 → 1491.66] So I think that's the main part which was introduced following FreeBSD 5.
[1492.00 → 1506.70] And we have some evolutions from time to time, but they are mostly around adjusting the timeframe between releases so that it's easy for end users to understand that, OK, this will come in next September.
[1506.70 → 1512.46] Perhaps the release will take a bit more time, but in next September, OK, we know that we'll have a new release.
[1512.78 → 1530.62] And this would have been very helpful in the time of FreeBSD 5 because we could have delayed some of the work done around locking to a future version, for instance, instead of trying to finish that huge task before shipping anything.
[1530.62 → 1532.76] Yeah, this is something.
[1533.16 → 1534.92] So first, this sounds fascinating.
[1535.52 → 1541.66] And what I'm wondering is, can users, sorry, could I see this calendar somewhere?
[1542.08 → 1543.92] Can I see how this process works?
[1543.94 → 1544.92] Is it publicly available?
[1545.40 → 1552.56] Yeah, the calendar is published on the FreeBSD.org website, announced on the mailing lists.
[1552.76 → 1553.14] OK.
[1553.50 → 1555.16] That's the main communication channels.
[1555.46 → 1557.88] And where does the FreeBSD development happen?
[1557.88 → 1561.58] I know that the RabbitMQ one happens on GitHub, but where does the FreeBSD one happen?
[1562.36 → 1581.30] Initially in CVS, I don't remember the years exactly, but at some point we switched to subversion and both servers were hosted internally in the FreeBSD infrastructure and in the Yahoo cluster in Sunnyvale.
[1581.30 → 1587.10] In the past year, we switched to Get, but we are still hosting that internally.
[1587.32 → 1590.64] And the reason is that we want to dock food FreeBSD itself.
[1591.32 → 1595.58] There are read-only mirrors available on GitHub.
[1596.32 → 1599.56] And there are still some discussions about that.
[1599.72 → 1603.00] Do we want to introduce GitLab, for instance, or some other tools?
[1603.00 → 1614.58] The idea is that because that's a private, not a private, but internal Git repository, currently we don't have all the nice tools provided by GitHub, for instance.
[1615.64 → 1624.74] Yeah, it's still a barrier to entry for country readers who are used to use GitHub for any kind of open source project.
[1624.74 → 1630.82] And yeah, that's still a discussion because you have to balance the fact that you want to dock food FreeBSD.
[1631.10 → 1637.62] You don't want to depend on the company's service, which is perhaps free for now, but we cannot tell what the future will be.
[1638.10 → 1639.34] So that's on one side.
[1639.46 → 1650.24] And on the other side, the fact that GitHub is so popular, it's a great source for new contributors and contributions in general.
[1650.24 → 1657.02] Okay. So I know that you can obviously communicate everything via the website.
[1657.24 → 1659.50] I don't really have any commenting enabled.
[1659.84 → 1660.92] Most websites don't.
[1661.06 → 1662.50] It tends to be a one-way channel.
[1662.82 → 1666.56] But how do users, how does the community talk to the developers?
[1666.92 → 1667.96] Is there a mailing list?
[1668.80 → 1669.72] How does that work?
[1670.18 → 1674.06] There are many mailing lists, in fact, either by topic.
[1674.06 → 1686.58] For instance, there are mailing lists around the graphic stack, around the Wi-Fi drivers, around network storage, a particular CPU architecture, and so on.
[1686.84 → 1694.94] And there are some mailing lists about topics such as the current development branch or the stable release branches.
[1696.12 → 1701.36] And yeah, that's the primary communication channel in FreeBSD.
[1701.36 → 1707.20] Let me guess, these mailing lists are software that runs on the same FreeBSD servers as the Kit Repo?
[1707.42 → 1708.24] Yeah, they are hosted.
[1708.58 → 1711.46] Okay, those must be some beefy machines to run everything.
[1712.26 → 1713.90] Yeah, the infrastructure.
[1714.34 → 1723.54] So initially, it was hosted in the Yahoo infrastructure because some FreeBSD developers were employed by Yahoo.
[1723.78 → 1725.48] They offered that service.
[1725.48 → 1736.18] But now that Yahoo doesn't use FreeBSD anymore, and that the company is splitting the various services, the infrastructure moved to some other companies.
[1736.40 → 1739.54] And I don't remember which one, but they are offering the hosting.
[1739.78 → 1746.42] And there are some servers around New York, still around San Francisco.
[1746.76 → 1750.10] And some of them are also in Europe and Asia.
[1750.10 → 1755.06] So I understand how the community can talk to the FreeBSD developers.
[1755.70 → 1758.90] How can they participate in FreeBSD development?
[1759.58 → 1763.92] One way to find tasks is to look at the Bugzilla bug tracker.
[1763.92 → 1773.28] And that's also one tool which is discussed because, I mean, people of my age are very happy with Bugzilla.
[1773.48 → 1780.04] But I'm sure people with 20 years younger might found it quite archaic.
[1781.32 → 1786.04] So, yeah, that part is still being discussed and will evolve.
[1786.98 → 1791.68] But, yeah, Bugzilla is one place to find bug reports and there are things to work on.
[1791.68 → 1798.68] And mailing list is another one where you can see what people are talking about or complaining about in particular.
[1799.22 → 1803.72] So if you don't know what to do, that's one way to find work to do.
[1804.24 → 1813.34] Another one is just solved the problem that you hit every day if you are using FreeBSD for work or at home.
[1813.58 → 1814.80] That's how I started, in fact.
[1815.12 → 1816.32] And how do you submit the patches?
[1816.72 → 1819.24] You can send pull requests on GitHub.
[1819.24 → 1822.60] They should be taken care of by someone at some point.
[1823.24 → 1826.10] You can submit patches on mailing lists.
[1826.40 → 1831.10] You can submit patches on Bugzilla after opening an issue.
[1831.52 → 1835.58] There is no one specific channel to submit your work.
[1836.12 → 1836.72] Okay.
[1837.36 → 1842.98] So this is a little bit of a tangent that we had for the last few minutes because the question was,
[1843.12 → 1846.00] how does the FreeBSD release engineering look like?
[1846.26 → 1847.00] So we covered that.
[1847.00 → 1852.58] So coming back to that topic, you had a very good description of how things work.
[1852.92 → 1858.40] I don't think you mentioned any timelines in the sense that when a new release starts,
[1858.40 → 1860.60] how long before that release gets shipped?
[1860.92 → 1862.54] How long before the GA?
[1862.96 → 1865.00] What does it look like to go to a beta?
[1865.32 → 1867.98] Is there a time period when betas start shipping?
[1868.36 → 1873.58] How long does it take typically before an RC or the first RC ships?
[1873.58 → 1875.42] And eventually the GA?
[1875.92 → 1876.08] Yeah.
[1876.28 → 1880.02] It depends if it's a minor release or a major one.
[1880.54 → 1883.48] So FreeBSD does not follow semantic versioning.
[1883.72 → 1887.68] That's interesting because the version would make you think that it does, right?
[1887.72 → 1889.84] Like it's currently version 13 or 12?
[1889.94 → 1891.14] 12 or 13, I can't remember.
[1891.56 → 1892.88] Yeah, both exist currently.
[1893.04 → 1893.26] Right.
[1893.36 → 1894.70] So both version 12 and 13.
[1894.70 → 1895.14] Right.
[1895.50 → 1899.98] And you also have like 12.1, 12.2, but those are not semantic versions.
[1900.56 → 1901.26] No, not really.
[1901.48 → 1904.76] It's close, but how can I say?
[1905.14 → 1909.90] Yeah, this is close to semantic versioning, but this is not documented as that.
[1910.54 → 1916.06] I mean that in FreeBSD, we pay a lot of attention to breaking changes.
[1916.06 → 1919.60] We have what we call POLA.
[1919.98 → 1922.26] So it's a principle of list astonishment.
[1922.84 → 1932.04] So it means that all changes which go into FreeBSD should be the less disruptive, in fact.
[1932.32 → 1937.06] And we should not surprise users, even between major releases.
[1937.06 → 1947.78] So when you want to deprecate something or remove something, you have to announce that a long time before you want to do that.
[1948.20 → 1955.24] If possible, it's good if you can mitigate what you're about to change in a breaking way.
[1955.24 → 1963.60] So that the transition from one version to another major version, it must be as smooth as possible.
[1963.98 → 1969.22] And we pay a lot of attention to compatibility between the major releases.
[1970.28 → 1974.12] So, of course, you cannot guarantee that all the time.
[1975.26 → 1978.52] But yeah, that's an important part of the FreeBSD release engineering.
[1978.52 → 1991.18] So back to the timeline, I would say that a major release between the beginning of the release cycle and the end, we are talking months, like two, three months.
[1992.04 → 1999.96] Perhaps more if there are bugs that crept in and are difficult to track down.
[1999.96 → 2010.78] And for minor releases, they are shorter, but we are still in the range of weeks and perhaps months sometimes.
[2011.62 → 2011.76] Okay.
[2012.08 → 2022.44] So now that we think about the FreeBSD release engineering as a whole, what can RabbitMQ learn from the FreeBSD release engineering?
[2022.44 → 2030.00] So I like the fact that it's based on fixed interval between major and minor releases.
[2030.52 → 2039.00] And the fact that the release cycle follows a calendar which is announced in advance and to everyone involved, contributors and users.
[2039.82 → 2047.16] I think this is a great tool to improve the communication and the organization of the work, in fact.
[2048.16 → 2051.46] Yeah, I would love to introduce that into RabbitMQ.
[2051.46 → 2054.52] Having that calendar, in fact.
[2054.86 → 2056.44] Yeah, I think it makes a lot of sense.
[2056.68 → 2062.68] I mean, we have been thinking about this for a while, and we have been looking at, well, FreeBSD is one example, but also other projects.
[2063.32 → 2065.20] And it does sound like a good idea.
[2065.58 → 2070.08] Obviously, between the idea and the implementation, there's a whole ocean of things to go through.
[2070.36 → 2072.84] But the direction sounds reasonable to me.
[2073.28 → 2078.44] I'm wondering if there are any other open source projects that you like how they do release engineering.
[2078.44 → 2081.94] So which one do I know about?
[2081.94 → 2087.56] So for instance, there is the Dark table open source photo editing project.
[2088.00 → 2090.82] They are also publishing a calendar in advance.
[2091.16 → 2107.80] And because they provide translations of the software, they also have to take that into account into their release engineering cycle to give time to translators to provide their translations.
[2107.80 → 2111.32] That's one thing I like in what they do.
[2111.72 → 2113.80] Another one is the Mesa library.
[2114.72 → 2117.94] So the library you can use on Unix.
[2118.34 → 2125.54] So it's a library providing 3D implementation of OpenGL, for instance, and all the new standards in that area.
[2125.54 → 2128.66] And now it grew a lot and provides as well.
[2128.66 → 2132.10] And user-owned parts of GPU drivers, for instance.
[2133.00 → 2135.36] So this is a large piece of code now.
[2136.06 → 2145.44] And what I like in their release engineering, so I don't remember if they follow fixed timeline or if they provide calendars.
[2145.44 → 2149.76] But I like how they handle the patches.
[2150.22 → 2163.38] Like a developer is working on a patch, and he doesn't know if that patch will go into the next minor release or if that needs to wait for the next major release.
[2163.96 → 2169.22] So they have someone like FreeBSD who is responsible to manage the release engineering.
[2169.22 → 2173.10] This time he's not hired or paid for that work.
[2173.20 → 2175.64] So it's on his free time, spare time.
[2176.74 → 2180.22] Yeah, they are trying various ways to...
[2181.20 → 2182.46] That was a few years ago.
[2182.68 → 2185.70] So that probably settled since.
[2185.82 → 2193.02] But they wanted to try several things on what would be the best way to make that communication possible.
[2193.24 → 2198.02] Like a developer want that patch into the next stable minor release.
[2198.02 → 2202.80] But it might not fit the timeline and so on.
[2202.94 → 2207.70] So they tried tags in the Git commits.
[2208.20 → 2214.10] I think they tried mailing list, a specific mailing list where people would post their patch and so on.
[2214.14 → 2216.42] So I don't know what they choose in the end.
[2216.56 → 2220.70] But yeah, I like how they explored various methods.
[2221.28 → 2223.50] Do you know what I remember about this specific topic?
[2223.96 → 2226.94] During one of our RabbitMQ team summits...
[2226.94 → 2229.16] By the way, RabbitMQ is a distributed team.
[2229.42 → 2232.74] As I mentioned, twice per year, we used to meet in a single place.
[2232.82 → 2233.52] It used to be London.
[2233.68 → 2236.52] So we had like an on-site, which was an off-site for some.
[2236.66 → 2237.58] But anyway, it was an on-site.
[2238.32 → 2243.68] And during these team summits, I noticed that your laptop had like a weird thing on its screen.
[2244.26 → 2245.48] And you were saying, like I said,
[2245.48 → 2247.92] JSB, I think your screen like needs replacing.
[2248.06 → 2249.16] This laptop needs replacing.
[2249.28 → 2250.86] And you were saying, no, no, it's okay.
[2251.04 → 2253.04] I'm working on some graphics drivers.
[2253.42 → 2255.42] And I don't quite have this like thing right.
[2255.50 → 2257.08] So pixels were looking like a bit weird.
[2257.18 → 2259.36] And I noticed the pixels started changing.
[2259.46 → 2265.12] And I was like, oh, JSB, why did you have to bring like a developer graphics card?
[2265.26 → 2268.50] And then like a development graphics drivers to the team summit?
[2268.64 → 2270.06] Like now we can't code properly.
[2270.06 → 2276.48] So then obviously I like would take up my laptop out and okay, let's get a properly tested and
[2276.48 → 2279.18] properly running graphics card and the graphics drivers.
[2279.56 → 2280.82] That was a fun one.
[2281.10 → 2285.34] And then you told me about like, you know, your interest in developing graphics drivers,
[2285.34 → 2286.66] which I thought was fascinating.
[2286.66 → 2287.68] Like, how do you even do that?
[2287.72 → 2288.94] I was like, whoa, maybe?
[2289.42 → 2292.10] Little did I know that, you know, also like free BSD.
[2292.38 → 2294.24] I have to thank you for my free NAS server.
[2294.64 → 2295.56] How stable that is.
[2296.28 → 2297.54] And a couple of other things.
[2297.66 → 2299.20] So yeah, that is pretty important.
[2299.20 → 2301.30] And I mean, it's the backups, right?
[2301.32 → 2305.12] All the pictures before iCloud and before other services, I used to back everything up on
[2305.12 → 2306.40] free NAS, and it never failed me.
[2306.56 → 2308.20] So there's something to say there.
[2308.56 → 2309.76] ZFS has something to do with it.
[2309.94 → 2312.54] Drives failed, but free BSD never failed me.
[2312.64 → 2313.64] So I was very happy.
[2314.58 → 2314.74] Nice.
[2314.84 → 2315.46] That's good to know.
[2315.86 → 2319.02] So yeah, that is good feedback for you.
[2319.64 → 2319.88] Yes.
[2320.42 → 2321.44] It wasn't 5.0.
[2321.58 → 2323.16] It was, I think, 9, 10.
[2323.32 → 2324.28] Actually, no, it was 11.
[2324.34 → 2325.10] I remember that one.
[2325.42 → 2327.70] 11 when I like started really depending on it.
[2327.76 → 2328.36] It was great.
[2328.36 → 2330.86] So that was a great few years of service.
[2331.52 → 2331.78] Great.
[2332.80 → 2335.00] And yeah, you mentioned the graphic drivers.
[2335.42 → 2342.46] That's a nice topic around release engineering because it's one area where it's difficult to find the right balance.
[2342.46 → 2347.64] In fact, because we want to ship, obviously, a stable operating system in the end.
[2347.64 → 2359.74] And the Mesa library also wants to be stable for all end users so that it can render your desktop videos and video games.
[2359.74 → 2368.90] But that's an area where the hardware and the new models are put in the market at a high pace.
[2369.08 → 2375.62] The technology evolves a lot and the GPU is a very complex beast.
[2375.62 → 2380.62] So on one side, you want to support the latest GPUs.
[2380.62 → 2389.16] But because if a user today buys a laptop, he will go for the latest shiny one.
[2389.26 → 2391.88] He won't choose the one released three years ago.
[2391.88 → 2398.36] So you want to ship all those new drivers and bug fixes as soon as possible.
[2398.94 → 2405.66] But it's very difficult because the drivers themselves are very complex.
[2405.66 → 2417.96] So it's very difficult to test what you ship because no one has all the various graphic cards and GPUs and configuration in general.
[2418.14 → 2420.52] So it's impossible to thoroughly test.
[2420.98 → 2429.14] So yeah, it's very difficult to find the right balance between shipping often and shipping something stable.
[2430.30 → 2434.66] And I don't think we find the right balance in FreeBSD either.
[2434.66 → 2438.76] So now drivers are provided as packages.
[2439.22 → 2442.74] They are not in the core anymore, the source code of FreeBSD.
[2443.10 → 2444.46] So that improved a lot.
[2444.78 → 2454.06] But yeah, it still has some issues from time to time to decide on when to ship a new version of that package.
[2454.62 → 2460.00] I think the more you dig into this and the more you work with this, you realize that it's not as straightforward.
[2460.00 → 2465.72] And everybody tries to make the best decisions they can give what they know, right?
[2465.76 → 2469.28] I mean, no one is trying to purposefully ship broken software.
[2469.80 → 2471.38] Sometimes it's really hard.
[2471.52 → 2475.42] And it looks like people don't care, or they don't think, but they do.
[2475.82 → 2477.22] And it's really, really hard.
[2477.22 → 2479.50] That's something worth emphasizing again and again.
[2480.16 → 2480.26] Yeah.
[2480.52 → 2491.94] I think in certain contexts, it's much easier to maybe use feature flags or something similar in that you're shipping the feature, but you're not enabling the feature.
[2492.08 → 2494.38] And this is a very important distinction to make.
[2494.88 → 2497.42] In some cases, you can ship it, but not enable it.
[2497.42 → 2498.42] And that's okay.
[2498.58 → 2503.56] And then test it or, you know, trickle it down through users, beta testers and whatnot.
[2503.82 → 2508.24] And when you have all your feedback, then if you can ship an update, then you do that.
[2508.34 → 2509.76] And everything is good.
[2509.80 → 2514.20] And everybody has the best latest version, right?
[2514.30 → 2519.06] Or the closest it can get because it can always be improved and there will always be bugs.
[2519.48 → 2522.08] After all, we are all human and we will make mistakes.
[2522.40 → 2523.10] And that's okay.
[2523.18 → 2523.88] That's not the problem.
[2524.40 → 2526.28] Don't try to not make mistakes.
[2526.28 → 2533.26] Try to limit the impact of those mistakes and fix them before anyone notices because then it looks like you've never made the mistake.
[2533.44 → 2535.20] Well, everybody knows the truth, right?
[2535.70 → 2538.20] So, yeah, countless times this has happened and it will happen.
[2538.38 → 2540.06] So, better be honest about it.
[2540.54 → 2546.14] That's why it's important to communicate well to contributors and users.
[2546.78 → 2549.10] That's the responsibility of that release engineering.
[2549.40 → 2552.78] You know that it might not be perfect in the end, what you ship.
[2552.78 → 2562.50] But at least you try to make sure that people are aware of what is fine and what might not be fine.
[2562.50 → 2580.56] This episode is brought to you by Linde.
[2580.62 → 2585.24] Gone are the days when Amazon Web Services was the only cloud provider in town.
[2585.24 → 2597.96] Linde stands tall to offer cloud computing developers trust, easily deploy cloud compute, storage, and networking in seconds with a full-featured API, CLI, and cloud manager with a user-friendly interface.
[2597.96 → 2607.52] Whether you're working on a personal project or managing your enterprise's infrastructure, Linde has the pricing, scale, and support you need to launch and scale in the cloud.
[2608.00 → 2612.22] Get started with $100 in free credit at linode.com slash changelog.
[2612.52 → 2616.08] Again, linode.com slash changelog.
[2623.24 → 2626.94] So, JSP, what did you work on before Rapid?
[2626.94 → 2631.14] So, I worked as an airline developer for a small French company.
[2631.82 → 2643.90] The company was providing a website aggregating ad so that people could look for jobs, apartments, various objects they would like to buy.
[2644.18 → 2646.62] Craigslist or country for the listeners.
[2646.62 → 2647.44] Yeah, something like that.
[2647.44 → 2656.46] And we wanted to provide some kind of social media features on top of that so that people could easily interact between them.
[2656.94 → 2660.18] In that company, so I was an airline developer.
[2660.66 → 2666.12] We were two airline developers working on the server side of that service.
[2666.50 → 2672.08] We chose to take You, which is an airline-based web server.
[2672.08 → 2680.00] So, we chose that because it was easy for us to extend right directly in the Air Long VM.
[2680.26 → 2685.44] In fact, add our own Air Long modules and application in addition to You.
[2686.12 → 2690.48] The website itself was developed in PHP and JavaScript.
[2690.98 → 2692.92] So, that part, we were not working on it.
[2692.92 → 2695.56] Other developers were responsible for it.
[2695.56 → 2703.56] But, yeah, those PHP files and static files were served by an Air Long VM.
[2704.52 → 2714.68] And what I liked about what we did is that we put some effort to make sure that the website was always running,
[2714.68 → 2719.36] even when we were working on it and upgrading it.
[2720.14 → 2726.28] So, if we had to upgrade the operating system, and especially the kernel, which was Debian,
[2726.76 → 2729.14] obviously, we would have to reboot the computer.
[2730.42 → 2734.58] But otherwise, we wanted to leave the service running.
[2734.58 → 2741.32] And what was great is that we could, in the end, benefit from the hot code reloading feature of Air Long,
[2741.44 → 2743.70] which is really an awesome feature.
[2744.12 → 2750.90] We were very happy because we could build Debian packages for our service.
[2751.02 → 2757.96] So, it packaged the You server, all our Air Long code base, and the website itself.
[2758.08 → 2763.86] So, the PHP scripts, static resources, so JavaScript and CSS and images, and so on.
[2764.58 → 2768.00] So, we packaged everything as Debian packages.
[2769.36 → 2775.78] And when we would apt-gate update, apt-gate dist-upgrade the machine, the servers,
[2776.40 → 2781.22] then the new copy of the Air Long code was deployed,
[2781.66 → 2786.92] and we were using the Air Long features to reload that code live,
[2787.02 → 2792.20] while the server, the HTTP server, was still running and serving requests.
[2792.20 → 2795.90] And, yeah, we were very happy with that.
[2796.32 → 2797.96] It's a really great feature from Air Long.
[2797.96 → 2801.84] So, to me, that sounds like you're using Air Long the way it was meant to be used.
[2802.06 → 2805.80] And what you're telling me is that it works really well when you use it the way it was built.
[2806.20 → 2806.48] Okay.
[2806.66 → 2807.98] Well, that is a great compliment.
[2808.48 → 2811.38] And working as expected in this case, it's great, right?
[2811.76 → 2813.20] And sometimes even rare.
[2814.02 → 2816.40] And obviously, not all software works as expected.
[2816.48 → 2817.32] That's why I mentioned this.
[2817.40 → 2820.22] And when it does, like, oh, yes, everything works the way it should.
[2820.26 → 2820.82] It's great.
[2820.82 → 2821.56] And it feels great.
[2821.56 → 2825.58] So, you were on the beaten track as designed, and everything was good.
[2825.98 → 2830.42] I know the answer to this, but I know that many listeners will be wondering,
[2830.82 → 2833.64] first, is RabbitMQ using hot code reloading?
[2834.04 → 2834.68] No, it's not.
[2834.88 → 2836.24] And the follow-up, why not?
[2836.62 → 2839.74] So, it's quite difficult to manage.
[2839.74 → 2849.42] The first part is that all developers and all contributions to the RabbitMQ code might lead to changes,
[2849.74 → 2858.16] which don't look as breaking changes when you think of a single instance of your Air Long VM, for instance.
[2858.28 → 2859.34] You stop the service.
[2860.14 → 2860.28] Okay.
[2860.36 → 2862.80] So, you load the code from the disk.
[2863.12 → 2864.16] It runs as expected.
[2865.42 → 2866.96] You stop the VM.
[2867.38 → 2868.72] And, okay, all is fine.
[2869.74 → 2879.74] But problem starts to show when, for instance, the state of a process changes between one copy of the module and the next one.
[2880.22 → 2886.04] So, you need to handle that migration from state V1 to state V2.
[2886.92 → 2890.48] There are tools to do that in Air Long, but this is not magic.
[2890.80 → 2896.38] You have to use them and implement that migration from V1 to V2.
[2896.38 → 2904.38] And it gets even more complicated when you're having a cluster of Air Long VMs.
[2905.00 → 2920.94] So, you have to take care of the fact that, for instance, an Air Long process, while the code is reloaded, will modify its own state and will start to use inter-process messages with a newer structure.
[2920.94 → 2932.96] So, when I say message in this context, its messages exchanged between Air Long processes, not messages that RabbitMQ would handle from other applications.
[2932.96 → 2936.70] So, you have to handle all those changes live.
[2937.02 → 2945.66] So, that new process, which was reloaded, might receive new messages using the new format from process on that same node.
[2945.94 → 2950.62] But it might receive old messages from a node which was not yet upgraded.
[2951.70 → 2952.18] And so on.
[2952.18 → 2955.86] So, that part is quite difficult to handle.
[2956.16 → 2960.08] And if you have mistakes, then it will crash, obviously.
[2960.60 → 2967.74] So, that feature is great, but it puts a lot of load and responsibilities on developers and contributors' shoulders.
[2968.36 → 2971.26] Because you have to handle all the cases.
[2971.26 → 2976.14] And the second part, which is difficult, is how to package that.
[2976.76 → 2984.74] Because Air Long was designed so that, in the end, you do not ship just the RabbitMQ Air Long applications, for instance.
[2985.02 → 2993.24] It was designed so that you ship the Air Long VM itself, the Air Long code you want to run on it, and the configuration.
[2993.24 → 3002.24] I mean, in the end, it's an appliance that you put on a server, but it's a whole thing, and a standalone thing.
[3003.06 → 3007.08] It has the VM, the code, and the configuration.
[3007.46 → 3013.20] It's not meant to support changes to that configuration, even that.
[3013.20 → 3022.12] And trying to package that, in my previous job, to package that as Debian packages, it was a great challenge.
[3022.12 → 3026.90] Because the Air Long VM is installed by other Debian packages.
[3027.60 → 3031.62] We also want to be able to change the configuration.
[3032.00 → 3042.14] Configuration, which was installed not by the package, but by tools like we were using Puppet, but a configuration management tool.
[3042.14 → 3051.42] So, it's quite difficult to use that Air Long feature in today's packaging and configuration management infrastructure.
[3051.42 → 3052.62] I remember that.
[3052.76 → 3057.06] This just reminds me of the discussion that we had a few years back about this very subject.
[3057.52 → 3059.84] And it's interesting how it comes back again.
[3060.36 → 3067.52] I remember the plugin system in RabbitMQ being one of the challenges when it comes to packaging RabbitMQ in an Erlang release.
[3068.20 → 3072.22] Being able to define what it's running, when, and how it's running.
[3072.48 → 3075.44] Again, for the listeners, RabbitMQ has this concept of plugins.
[3075.78 → 3077.18] A lot of them ship with RabbitMQ.
[3077.28 → 3080.42] Others can be added, just dropped in a directory, and off you go.
[3080.42 → 3082.92] And those plugins, they are applications.
[3083.86 → 3088.20] So, RabbitMQ really is, this is the way I think about it.
[3088.50 → 3095.86] It's a microservices' architecture in a single Erlang VM, in a single system process.
[3096.30 → 3102.26] Because of all these applications exchanging messages, and by the way, they could be cross nodes.
[3102.26 → 3106.58] So, that's where the Erlang distribution comes in, where those messages have to traverse the network.
[3107.18 → 3109.02] And then you have a cluster of three nodes or four nodes.
[3109.70 → 3118.70] And any message, by the way, this is like an NQP message, or whether it's 091 or 1.0, or any NQT protocol.
[3118.70 → 3127.22] It can arrive at any node, and it will end up in the right place, because the cluster is aware of where the members are, where the processes are, how to send those messages internally.
[3127.70 → 3128.96] And that's what makes it challenging.
[3128.96 → 3133.48] So, the one thing that helped, I think, in recent years is containers.
[3134.52 → 3139.34] Containerizing RabbitMQ, having that tarball, which really used to be the Debian package.
[3139.72 → 3140.96] Now it's called something else.
[3141.14 → 3141.98] FreeBSD jail.
[3142.34 → 3143.12] Similar concept.
[3143.12 → 3148.68] So, the container allows us to package Erlang, even the operating system, right?
[3148.72 → 3151.02] Because that's what you have, OpenSSL, and all the dependencies.
[3151.30 → 3154.84] And we have a single tarball, which is a runnable artifact.
[3155.30 → 3160.84] You spin it up, and it has everything that you need in the right order, pre-configured, a bunch of things.
[3161.00 → 3162.04] So, that really helps.
[3162.52 → 3166.96] And then on top of that, obviously, if you use something like Kubernetes, you want a cluster operator,
[3166.96 → 3174.44] or an operator that manages your deployments, which is especially important if you have a clustered system,
[3174.80 → 3179.20] clustered stateful system, such as RabbitMQ, or a distributed stateful system.
[3179.96 → 3181.82] And in those cases, it really helps.
[3182.34 → 3187.70] And this just made me realize that one discussion which I would really like to have is with Chung
[3187.70 → 3193.28] about the cluster operator and how RabbitMQ runs in the context of Kubernetes.
[3193.28 → 3196.62] Because I think it does a lot of things really, really well.
[3196.96 → 3201.70] Being a stateful-distributed system on Kubernetes, wow, that's challenging.
[3202.18 → 3208.68] And I think the new tools made this problem easier from some perspectives,
[3208.96 → 3211.06] but it also made it harder from others.
[3211.46 → 3214.12] And adapting to the new world, it's very challenging.
[3214.58 → 3217.02] And I think a lot of this is lost to the details.
[3217.06 → 3219.28] And it's important because many can learn from this.
[3219.86 → 3221.58] Many stateful systems can learn from this.
[3221.58 → 3223.98] And I know a few stateful systems like databases,
[3223.98 → 3232.00] which don't work that well in the context of containers, of Kubernetes, of things that come and go so often,
[3232.16 → 3237.60] networks that break all the time, or more frequently than they do in the traditional data centre,
[3237.66 → 3239.30] in the traditional bare metal hosts.
[3239.60 → 3241.20] So that's something which is challenging.
[3241.20 → 3241.76] Okay.
[3242.24 → 3250.76] So I would say that my understanding is that you miss this hot code reloading from the olden days that RabbitMQ doesn't have.
[3250.82 → 3255.16] And there are some practical limitations why it would be very difficult to implement.
[3255.52 → 3258.40] Not impossible, but very, very challenging.
[3258.40 → 3261.58] And is there anything else that you miss?
[3261.98 → 3265.08] No, I think that's something I would love to see in RabbitMQ.
[3265.32 → 3270.00] And even though it's difficult, I don't think it's impossible.
[3270.20 → 3275.98] For instance, if we were to ship only bug fixes into our patch versions,
[3276.40 → 3280.04] then it would be pretty easy to have that hot code reloading.
[3280.04 → 3287.24] And the way you describe it in Erlang means that we could say that going from a patch release to the next one,
[3287.72 → 3290.06] it supports hot code reloading.
[3290.60 → 3296.84] But we can also say that going from a version to the next miner, it doesn't.
[3297.10 → 3299.48] And the VM has to be restarted.
[3299.94 → 3302.76] So even that is supported by Erlang itself.
[3302.96 → 3308.74] The hot code reloading knows when it cannot be reloaded live.
[3308.74 → 3313.62] So I think that if we were to have only bug fixes in patch releases,
[3313.88 → 3316.18] we could have hot code reloading implemented.
[3316.64 → 3321.34] And it would not add a lot of load to our team, I think.
[3321.68 → 3323.38] That is achievable.
[3324.06 → 3329.56] And a great benefit from that is that upgrading RabbitMQ to the next patch release
[3329.56 → 3332.10] means you don't have to restart RabbitMQ,
[3332.64 → 3337.52] which means you don't need to spend a lot of time starting RabbitMQ
[3337.52 → 3342.72] if you have thousands or tens of thousands or hundreds of thousands of queues
[3342.72 → 3345.00] and exchanges and bindings and so on.
[3345.40 → 3348.70] Well, I've really enjoyed this discussion, JSP.
[3348.90 → 3349.24] Yeah, me too.
[3349.26 → 3350.14] Thank you for joining me.
[3350.30 → 3351.36] It was great fun.
[3351.76 → 3353.08] I'm looking forward to the next one.
[3353.70 → 3357.94] And I'm wondering if there's any closing thoughts that you have?
[3357.94 → 3364.04] Yeah, so I would like to know, in fact, what people are doing in their job
[3364.04 → 3370.46] or their personal projects to ship what they produce.
[3371.06 → 3376.08] Do they have experience with various release engineering practices
[3376.08 → 3381.64] and what works and didn't work for them?
[3381.64 → 3387.16] So I would love to hear from their writing software,
[3387.44 → 3393.82] but I would also love to hear from people who are consuming those open source projects
[3393.82 → 3399.12] or even commercial projects, what they like and what they don't like
[3399.12 → 3403.54] when they want to learn more about the new versions of the tool they use.
[3403.54 → 3408.36] So if you're a FreeBSD user or a RabbitMQ user,
[3408.72 → 3411.28] let JSP know what you like about the release engineering,
[3411.44 → 3414.98] what don't you like, and what would you like to be better
[3414.98 → 3416.96] and what does even better mean for you?
[3417.32 → 3420.00] He would enjoy, and I would enjoy as well knowing about that.
[3420.06 → 3422.30] Yeah, we will both benefit from the answers.
[3423.24 → 3424.60] Well, this was fun, JSP.
[3424.80 → 3425.54] Thank you very much.
[3425.68 → 3426.24] See you next time.
[3426.42 → 3427.72] Yeah, thank you for the invitation.
[3427.72 → 3433.54] That's it for this episode of Ship It.
[3433.82 → 3435.20] Thank you for tuning in.
[3435.42 → 3438.36] We have a bunch of podcasts for developers at Changelog
[3438.36 → 3439.68] that you should check out.
[3440.06 → 3443.94] Subscribe to the master feed at changelog.com forward slash master
[3443.94 → 3446.26] to get everything we ship.
[3446.68 → 3450.70] I want to personally invite you to join your fellow change loggers
[3450.70 → 3453.80] at changelog.com forward slash community.
[3454.10 → 3455.60] It's free to join and stay.
[3455.60 → 3459.16] Leaving, on the other hand, will cost you some happiness credits.
[3459.64 → 3461.18] Come hang with us on Slack.
[3461.58 → 3462.46] They're no imposters.
[3462.88 → 3464.06] Everyone is welcome.
[3464.66 → 3468.96] Huge thanks again to our partners Vastly, Launch Darkly and Minute.
[3469.30 → 3473.98] Also, thanks to Break master Cylinder for making all our awesome beats.
[3474.44 → 3475.64] That's it for this week.
[3475.92 → 3476.70] See you next week.
[3476.70 → 3506.68] See you next week.
[3506.70 → 3507.78] Bye.
[3507.82 → 3508.12] Bye.
[3512.10 → 3512.32] Bye.
[3512.68 → 3512.82] Bye.
[3512.88 → 3513.46] Bye.
[3513.46 → 3513.88] Bye.
[3514.78 → 3515.24] Bye.
[3515.26 → 3516.00] Bye.
[3516.04 → 3516.32] Bye.
[3516.42 → 3517.50] Bye.
[3517.50 → 3517.62] Bye.
[3527.48 → 3528.14] Bye.
[3530.04 → 3530.98] Bye.
[3531.14 → 3533.32] Bye.
