[0.00 --> 3.54]  In the past, let's say, you know, you had a huge code base and it had no tests in it.
[3.70 --> 6.94]  Upgrading your framework then is kind of a big deal, right?
[6.98 --> 9.66]  It's because you don't really have that confidence because you haven't got any tests.
[9.82 --> 16.58]  Now, obviously, types don't replace tests, but they do help you still in discovering kind of those things that could break.
[16.58 --> 21.38]  As framework authors, having those types is monumental to big projects.
[21.70 --> 25.16]  Well, I don't want to be the guy that just keeps bringing it back to React, but Nick started it.
[27.04 --> 29.80]  Bandwidth for ChangeLog is provided by Fastly.
[30.18 --> 32.06]  Learn more at Fastly.com.
[32.30 --> 35.36]  We move fast and fix things here at ChangeLog because of Rollbar.
[35.50 --> 37.20]  Check them out at Rollbar.com.
[37.44 --> 39.62]  And we're hosted on Linode cloud servers.
[39.96 --> 41.96]  Head to Linode.com slash ChangeLog.
[43.24 --> 45.98]  This episode is brought to you by Rollbar.
[46.38 --> 48.06]  Move fast and fix things.
[48.36 --> 50.44]  Resolve errors and minutes and deploy with confidence.
[51.02 --> 53.28]  Head to Rollbar.com slash ChangeLog.
[53.36 --> 54.16]  Request a demo.
[54.30 --> 55.18]  Get started today.
[55.62 --> 57.84]  It's loved by developers, trusted by enterprises.
[57.84 --> 60.84]  And most of all, we use it here at ChangeLog.
[61.20 --> 63.86]  Move fast and fix things with Rollbar.
[64.26 --> 67.16]  Once again, Rollbar.com slash ChangeLog.
[67.16 --> 83.36]  Welcome, friends, to JS Party, your weekly celebration of JavaScript and the web.
[83.66 --> 86.60]  We are fresh off our first live show with video.
[87.02 --> 87.72]  That's right.
[87.84 --> 93.42]  Next week's JS Danger episode was streamed on Twitter and a few thousand of you joined in on the fun.
[93.42 --> 96.18]  So we might start doing video on the regular.
[96.56 --> 97.02]  Holler at us.
[97.08 --> 97.88]  Let us know if you're interested.
[98.08 --> 100.40]  We are at JS Party FM on Twitter.
[100.66 --> 101.82]  Okay, let's do this.
[101.98 --> 103.16]  Dojo time, y'all.
[103.16 --> 116.72]  Hello, JS Party.
[117.06 --> 117.32]  Welcome.
[117.98 --> 121.26]  This week, we have a really exciting topic to talk about.
[121.68 --> 124.58]  But first, I want to introduce you to my co-panelist, Jared.
[124.74 --> 125.40]  Jared, what's up?
[125.90 --> 126.58]  It's your boy.
[127.50 --> 128.08]  Hi, Nick.
[128.08 --> 128.30]  Awesome.
[128.50 --> 128.88]  How are you?
[129.40 --> 129.86]  I'm good.
[129.92 --> 130.30]  I'm good.
[130.66 --> 131.42]  I'll say hoi hoi.
[131.42 --> 133.62]  And I want to welcome our special guest.
[133.76 --> 134.54]  And that's Matt Gad.
[134.64 --> 135.42]  Matt, say hello.
[136.42 --> 137.16]  Yo, how's it going?
[137.78 --> 138.26]  I'm good.
[138.30 --> 138.84]  How are you?
[139.50 --> 140.38]  Yeah, it's not bad.
[140.46 --> 140.82]  Not bad.
[141.52 --> 141.88]  Awesome.
[142.68 --> 144.42]  Nick, I noticed you're wearing your Dojo shirt today.
[144.68 --> 145.14]  I am.
[145.22 --> 147.56]  I'm wearing a vintage Dojo shirt to talk about Dojo.
[147.78 --> 151.00]  I just want to point that out for the listener's sake that they can't see your shirt.
[151.14 --> 152.78]  But I can and I appreciate it.
[152.84 --> 153.96]  I bet Matt appreciates it, too.
[154.88 --> 156.06]  Yeah, I don't have one of them.
[156.14 --> 157.42]  So I'm a bit annoyed.
[157.42 --> 162.48]  I need to get a new Dojo, modern Dojo shirt with the awesome dragon on it.
[162.70 --> 164.16]  Do you not have one with the dragon on?
[164.50 --> 164.92]  I do.
[165.24 --> 167.86]  It doesn't fit me anymore in the good way.
[168.42 --> 170.06]  So the other way.
[172.06 --> 176.48]  I've just got a wardrobe full of those t-shirts that don't fit me for the bad reasons.
[178.56 --> 179.04]  Awesome.
[179.46 --> 181.42]  Well, yeah, we are talking about Dojo today.
[181.42 --> 187.20]  And we actually did talk about Dojo on the show back way, way back in episode 25.
[187.60 --> 195.50]  So go listen to that if you want to listen to kind of the history of Dojo 1 to Dojo 2 and the several years in the making of that.
[195.68 --> 197.00]  But we're not going to focus on that.
[197.08 --> 197.78]  Years ago.
[198.54 --> 198.94]  Years.
[199.24 --> 200.86]  We're going to focus on modern Dojo.
[200.86 --> 210.96]  And this kind of specifically came out of a comment I made a couple of episodes ago where I shouted out the release of Dojo 7 and mentioned that if you like React, you like Dojo better.
[211.56 --> 220.62]  And so I thought it'd be perfect to bring Matt Gadd on, project lead on Dojo, to defend my comment and let me throw him under the bus with that.
[220.82 --> 223.66]  And Matt, can you tell me why you like Dojo better?
[224.94 --> 226.60]  Why you like it better?
[226.60 --> 229.98]  I should say I'm here for that clickbait.
[230.40 --> 233.86]  So Nick said that and I thought, hmm, I've got to show up for that show.
[234.56 --> 236.42]  Super, super controversial comment.
[238.46 --> 244.12]  So I guess to step it back a bit and not make the bold statement.
[244.84 --> 256.40]  But I guess the main thing that I guess that we've focused on since like day one in modern Dojo is, you know, being typescript first and being unashamedly typescript focused.
[256.40 --> 264.28]  And we've been a big supporter of typescript since the super early days when there was a lot of rough edges.
[264.74 --> 270.40]  And we basically, you know, the framework's basically entirely geared towards a typescript experience.
[270.40 --> 292.54]  So I think that's really important in terms of kind of like how you work with it, how, you know, things that we do because it's in typescript all kind of like dovetail together to kind of make it a kind of more out the box experience than say, you know, writing some React in typescript and the associated libraries.
[292.54 --> 298.14]  So, yeah, I guess that's one of the key was the key goals of Dojo as a framework.
[298.70 --> 299.60]  Yeah, definitely.
[299.74 --> 305.34]  And I think that that's what I meant by that comment is the focus on developer experience.
[305.60 --> 307.66]  And TypeScript does go big into that.
[307.90 --> 311.48]  Definitely not saying that React doesn't because React is also nice to work with.
[311.48 --> 323.28]  But kind of it's that plus the whole ecosystem that is all typed together very well that gives you more than than just, you know, JSX and a component wrapper and being able to go from there.
[323.28 --> 325.76]  So that's kind of where I was going with that comment.
[325.88 --> 333.60]  Like I've used it on a couple of projects, as you know, Matt, and I really enjoy it, really enjoy the whole ecosystem of it.
[333.74 --> 343.94]  And seeing it change over the last couple of versions has been really cool because it's just gotten so much easier to work with as new features and new versions have been released.
[343.94 --> 349.48]  So why don't we talk about that a little bit and kind of what's changed in Dojo since like Dojo 2?
[349.94 --> 353.96]  From Dojo 2, there's the concept of components or widgets, as we call them.
[354.76 --> 356.32]  And they were class based in Dojo 2.
[356.64 --> 361.06]  And for a few versions after that, why don't you tell the story about a little bit of what has changed?
[361.72 --> 362.84]  Yeah, so it's kind of interesting.
[362.84 --> 374.64]  Obviously, with Dojo 2 being, you know, nearly two years old or slightly older, a lot of the original work we did at the time was in super early versions of TypeScript.
[374.94 --> 380.36]  And we never really intended deliberately to go with like class based components.
[380.64 --> 384.66]  We actually had a composition system called Compose.
[384.66 --> 394.54]  And, you know, the whole idea behind that was, you know, to support composition in widgets and not inheritance, which again was kind of a concept in the original Dojo.
[394.84 --> 395.10]  Yeah.
[395.20 --> 396.50]  But the big problems we had at the time was...
[396.50 --> 397.16]  Multiple inheritance.
[397.58 --> 397.98]  Yeah.
[398.54 --> 402.98]  Well, they like to say it wasn't, but it kind of did look like it in original Dojo.
[403.90 --> 409.38]  Yeah, so like Compose in theory and concept was a nice idea.
[409.38 --> 421.98]  But at the time, TypeScript was so limited in terms of, you know, what we could do in terms of the types for the generics and the things that went with it, is it was a really awful experience for the end user.
[422.12 --> 424.16]  So in the end, we didn't really pursue that.
[424.30 --> 430.14]  So when we went out, you know, the door, the kind of the easiest way for an end user to approach these things was with classes.
[430.14 --> 433.52]  And the TypeScript support for classes at that point was very good.
[434.02 --> 437.28]  And so, you know, that was always a thing in the back of the mind.
[437.28 --> 446.56]  And this is kind of goes back to where I was saying we're a TypeScript first framework is a lot of the APIs, you know, when we're designing them, we're thinking about how that works with TypeScript.
[446.70 --> 452.58]  And at the point of time, you know, with the kind of inference that we wanted to get, classes were really the best we could do.
[452.68 --> 455.66]  And we had a mixing approach with classes, which was quite unique.
[455.78 --> 457.48]  So you could still do that composition.
[457.82 --> 459.68]  But it was never our end goal.
[460.20 --> 467.10]  And I think you can see that through kind of the lineage of, you know, where Compose was and what Dojo, the original version was.
[467.28 --> 474.08]  And so I think come around to Dojo 6, obviously we've iterated quite a lot over that period of time from 2 to 6.
[474.70 --> 490.06]  We finally had kind of the capabilities to provide a system based on functions that were class-based that allowed us to, A, compose, you know, behaviors that could also affect the types that came out as well.
[490.06 --> 499.26]  And I think that's one of the key differentiators between, say, Dojo and more JS frameworks that have TypeScript definitions as an add-on.
[499.26 --> 507.76]  And that's one of the things that we've done is, you know, we have a concept in, I don't want to get too in the weeds, but obviously we have kind of this composition mechanism called middleware.
[508.14 --> 510.72]  And that can affect things like the widget properties.
[510.94 --> 519.34]  So you can design this self-contained behavior that will add properties for you to the widget interface that you can then use in the component.
[519.34 --> 525.26]  So the idea of kind of behind it being encapsulating the behavior and the types.
[525.72 --> 530.68]  And that was kind of the key thing in Dojo 6 that we changed, which is out at the moment.
[531.84 --> 532.28]  Yeah.
[532.36 --> 537.58]  So with middleware, would you kind of equate that loosely to hooks in React?
[538.34 --> 538.66]  Yeah.
[538.72 --> 542.96]  I think, you know, a lot of the times it's easy to squint and go, this is like for like behavior.
[542.96 --> 552.80]  And in terms of like how they behave, they're very different in React, you know, and hooks have an interesting mechanism in terms of how they implement it.
[552.86 --> 561.34]  But in terms of, yeah, in how you'd encapsulate behavior, very similar in terms of, you know, you might similar behaviors you would implement in hooks.
[561.80 --> 566.36]  But yeah, very different in terms of implementation and some other usability aspects.
[566.36 --> 567.72]  Yeah, definitely.
[567.96 --> 573.86]  I learned middleware first in Dojo and then later learned hooks with React.
[574.14 --> 582.02]  And they were so strikingly similar that like the main concepts behind hooks really just clicked as soon as I started using them because of middleware.
[582.20 --> 585.72]  So that's why I was kind of going, saying that they were pretty similar.
[586.14 --> 586.36]  Yeah.
[586.46 --> 589.08]  And I think, yeah, as a concept, they're ultimately familiar.
[589.22 --> 595.34]  Anyone going the other way as well from React to trying middleware in Dojo, you know, should get the idea behind that.
[595.34 --> 596.70]  So, yeah, no, absolutely.
[597.42 --> 601.80]  I'm curious how you go from a version two in 2018 to a version seven right now.
[602.04 --> 606.06]  Like that's a, you guys like, come on, full speed ahead or what's going on?
[606.12 --> 606.64]  That's a lot of verticals.
[606.64 --> 607.90]  Yeah, so it's interesting.
[608.16 --> 618.04]  The interesting part of this is if you go back to Dojo Toolkit, they basically went from over 16 years, they went one major version.
[618.24 --> 619.28]  They never made it to two.
[619.40 --> 622.08]  They were very keen on going with minor versions.
[622.20 --> 622.52]  Right.
[622.52 --> 633.04]  One thing that we really struggled with in the original Dojo Toolkit days was getting people to upgrade, which there was a kind of fear of upgrading major versions because of the associated things with it.
[633.04 --> 644.58]  And so one thing in modern Dojo, we try and make that experience of upgrading, you know, between versions as frictionless as possible so we can iterate quicker.
[645.22 --> 651.80]  And, you know, as much as like what I was saying earlier is, you know, with TypeScript evolving, it means we can do more powerful things.
[651.94 --> 657.92]  Now, obviously, those are breaking changes in a lot of cases just due to the way, you know, even TypeScript is in terms of breaking changes.
[657.92 --> 663.92]  So what we like to do is we like to, you know, iterate as much as we can on major versions, but also provide.
[664.80 --> 672.94]  So we've got an upgrade tool, which basically mostly gives you a friction free upgrade path upwards of versions.
[673.50 --> 675.26]  So, yeah, it's a really good question.
[676.22 --> 685.40]  Yeah, I think that that like that's something that we can do today that we really couldn't do back in the Dojo one days is we can we can release new versions that have some breaking changes.
[685.40 --> 688.40]  And this goes for every every framework out there.
[688.52 --> 702.88]  But specifically with with Dojo being so strict with its type correctness that when we change things, the types change, obviously, if you're upgrading, you can immediately see because of the compilation step where breaks might be in your code.
[703.44 --> 710.90]  And then with that upgrade tool, like you said, that's using I'm forgetting the name of the term for it right now.
[711.52 --> 712.00]  Code mods.
[712.34 --> 712.74]  Code mods.
[712.86 --> 713.18]  Thank you.
[713.28 --> 713.40]  Yeah.
[713.88 --> 714.54]  You wrote them.
[714.54 --> 715.22]  I know.
[715.34 --> 716.82]  You wrote code mods, man.
[716.88 --> 717.58]  Come on, Nick.
[718.92 --> 719.72]  I'm the worst.
[720.22 --> 720.58]  Yeah.
[721.06 --> 721.58]  Code mods.
[721.66 --> 723.90]  It's using code mods to help you to rewrite the code.
[724.20 --> 726.10]  And it can do that in a very type safe way.
[726.20 --> 729.10]  And it's using the AST to to walk that.
[729.18 --> 732.00]  So it's it's correct in the changes that it makes, which is really cool.
[732.00 --> 732.16]  Yeah.
[732.18 --> 740.52]  And I think you make a real valid point about the, you know, the TypeScript tax aspect, again, kind of gives you confidence that you're going to be aware of those changes if you do have to make.
[740.52 --> 744.82]  In the past, let's say, you know, you had a huge code base and it had no tests in it.
[744.82 --> 748.76]  You know, upgrading your framework then is kind of a big deal, right?
[748.80 --> 751.48]  It's because you don't really have that confidence because you ain't got any tests.
[751.64 --> 759.32]  Now, obviously, types don't replace tests, but they do help you still in discovering kind of those things that could break.
[759.32 --> 766.04]  It's very, very, you know, for as framework authors, having those types, you know, is monumental to, you know, big projects.
[766.44 --> 766.46]  So.
[767.40 --> 771.34]  Well, I don't want to be the guy that just keeps bringing it back to React, but Nick started it.
[771.40 --> 773.12]  So I'll just keep it going.
[773.52 --> 776.78]  Is it an apples to apples comparison in terms of at least surface area?
[776.92 --> 779.38]  I mean, React is a component library.
[779.50 --> 783.06]  You have to like add a bunch of things and stitch together to have like a framework.
[783.06 --> 787.92]  But it's kind of a UI framework for those who aren't as familiar with Dojo as you and Nick are.
[788.52 --> 790.46]  Is it a lot like React, but does things differently?
[790.60 --> 792.70]  Does it offer things that are wildly different?
[793.14 --> 795.02]  What kind of things does it do?
[795.26 --> 806.60]  So, yeah, I think that's a really good question as well is, yeah, it's definitely not apples to apples in terms of, you know, obviously React absolutely focus on the, you know, it's a view component authoring library.
[806.60 --> 817.82]  And, you know, they spend a lot of time, say, you know, they've spent a huge amount of time in terms of like the VDOM parts of it, the reconciliation, all the, you know, the works on scheduling.
[817.96 --> 818.72]  They've done an awful lot.
[818.78 --> 821.92]  They're basically micro-optimizing in that kind of space.
[821.92 --> 825.64]  And they don't really have a huge desire to expand out of it.
[825.78 --> 830.50]  So that's kind of been taken by, you know, the ecosystem, which there is a huge ecosystem for.
[830.88 --> 835.18]  And, you know, I think there's great power in having a diverse ecosystem with that.
[835.18 --> 842.74]  But there's also kind of that, you know, kind of panic of too much choice at times when you're trying to get things done.
[843.24 --> 846.14]  And so Dojo is kind of the absolute opposite camp of that.
[846.28 --> 855.64]  You know, we kind of, for us, the kind of comparisons that we prefer to be in would be kind of the Ember and Angular space where, you know, we're going to be very opinionated out of the box.
[855.96 --> 864.04]  And to hopefully remove some of those decision-making things from you, which for some people, you know, might find very limiting.
[864.04 --> 869.50]  But for other people, it's, you know, a friction that they don't need and they just want to create things.
[869.70 --> 886.00]  So, you know, we find a lot with enterprise customers that, you know, going through creating apps and, you know, A, like deciding what things to use based on licensing or what's maintained or, you know, all those kind of things that people have to take into account when developing applications.
[886.00 --> 894.34]  Basically, the goal of Dojo Framework is to, you know, remove the entirety of them, but obviously be opinionated about it.
[894.34 --> 904.40]  And so, yeah, we cover the build tooling, the testing, how you style your components, how you theme components, you know, absolutely everything.
[904.40 --> 908.26]  And yeah, you name it, you know, it's decision on that point.
[908.38 --> 923.64]  But the main kind of takeaway is, you know, we're in a similar space to Angular, but we kind of, we understand that people, I mean, I personally prefer authoring kind of in the more reactive function components like React over Angular.
[923.82 --> 924.78]  No, that's just an opinion.
[924.78 --> 932.86]  But, so we kind of React-like, but as a, you know, as a more framework encompassing thing.
[933.62 --> 934.64]  God, that was a lot of words.
[936.26 --> 942.10]  Definitely similar to Angular in the surface area, but closer to React in the API surface area.
[943.46 --> 944.98]  Sounds like a nice middle ground.
[945.62 --> 953.60]  Yeah, and I think, to be honest with you, I feel like that React kind of in the last year, there's a lot of people kind of pursuing that space with React as well.
[953.60 --> 955.62]  As you know, you've got things like Next.js.
[956.28 --> 962.54]  I think Ryan Florence and Michael Jackson are developing, you know, an application framework.
[962.70 --> 968.86]  So I think a lot of places are going that way where they understand that, you know, there's just the classic thing, isn't there?
[968.90 --> 971.58]  It's like you could waste months writing webpack configs.
[971.68 --> 976.88]  You can write, you know, you could spend months trying to correctly figure out the best way to test things.
[977.08 --> 980.62]  And so, yeah, just removing some of that overhead is, you know, is a big deal.
[980.62 --> 995.08]  But similar to what the Redwood folks are trying to do and saying, you're going to use React and GraphQL, and we're going to build an application framework around those technologies and fill in a lot of the stuff that if React were a full stack is a lame way of saying it because it's all front end.
[995.08 --> 999.22]  But if it was a full app framework, it would provide those things like Ember does.
[999.68 --> 1001.38]  Like it sounds like Dojo and Angular do.
[1002.08 --> 1002.40]  Yeah.
[1002.74 --> 1007.08]  So it does cover a lot of things beyond just widget composition.
[1007.58 --> 1013.16]  And it includes things like a router, a way to store and manage data.
[1013.16 --> 1021.22]  So there's a stores middleware and there's, help me out, what other big pieces of framework are there?
[1021.70 --> 1022.18]  Code mods.
[1022.30 --> 1022.90]  Yeah, code mods.
[1023.34 --> 1023.56]  Yeah.
[1024.52 --> 1025.00]  Yeah.
[1025.06 --> 1027.66]  I mean, we've got an awful lot, could I think of it?
[1027.72 --> 1038.70]  Obviously, we provide, you know, CLIs for upgrading, for testing, for building widget libraries, for building, obviously, applications.
[1038.70 --> 1042.78]  Obviously, we have the bootstrapping for you to start making an app.
[1043.32 --> 1048.66]  And in terms of the actual, you know, framework level stuff, yes, we've got like a, you know, a state store.
[1049.00 --> 1053.24]  We obviously, we have routing or routing as English people like to call it.
[1054.58 --> 1056.12]  We've got obviously internationalization.
[1056.12 --> 1056.66]  Why do they do that?
[1056.80 --> 1057.18]  Come on.
[1057.44 --> 1057.76]  Routing.
[1058.00 --> 1061.54]  I always say you have a router and then you talk about routing.
[1061.68 --> 1062.48]  It doesn't make any sense.
[1062.68 --> 1063.30]  It would be a router.
[1063.54 --> 1063.84]  Would it not?
[1064.82 --> 1066.12]  We call it a router, yeah.
[1066.26 --> 1066.62]  Oh, you do?
[1067.18 --> 1068.00]  At least that's consistent.
[1068.00 --> 1068.34]  All right.
[1068.34 --> 1068.64]  I'm back.
[1068.68 --> 1068.96]  Yeah.
[1069.06 --> 1070.18]  We're consistently wrong.
[1070.40 --> 1070.68]  All right.
[1072.72 --> 1084.58]  But yeah, like, so a huge thing, again, is it was massive in Dojo One is, you know, Dojo One was kind of one of the first frameworks that really pushed internationalization out of the box for when you're writing apps.
[1084.58 --> 1089.58]  Because when you're writing big apps, you know, English isn't the only language that exists in the world.
[1090.18 --> 1096.32]  And it's kind of, you know, shoehorning that in as kind of a second thought in terms of supporting internationalization.
[1096.32 --> 1099.20]  And localization is very difficult.
[1099.20 --> 1102.50]  So, again, in modern Dojo, that's a key concern.
[1103.06 --> 1106.42]  So, you know, all of our widgets are internationalizable out of the box.
[1106.78 --> 1112.24]  We provide, you know, easy mechanisms to be able to localize and do translations, et cetera.
[1112.24 --> 1114.20]  So, yeah, that's a huge part.
[1114.40 --> 1125.74]  Obviously, our widgets, again, you know, were very, in Dojo One, we had huge contributions from IBM to make all of the widgets accessible and provide a framework for creating accessible widgets.
[1125.74 --> 1134.38]  And then, obviously, in modern Dojo, we had a really good engineer in Sarah Higley who went on to, she's working at Microsoft and accessibility stuff.
[1134.44 --> 1141.28]  And she did a lot of work on, in kind of conceptualizing the modern Dojo widgets with, you know, being properly accessible.
[1141.50 --> 1143.20]  And so that's something we massively care about.
[1143.90 --> 1146.28]  And, yeah, so there's just a lot of things.
[1146.52 --> 1149.44]  And, you know, we care a lot about interoperability as well with the web.
[1149.44 --> 1156.50]  That was kind of a really pain point in Dojo One, if anything, is, you know, the ecosystem in JavaScript is massive.
[1156.88 --> 1163.40]  There is still a lot of friction in terms of, hey, can I use this thing from this library in another library?
[1163.90 --> 1166.80]  And that we never really solved in Dojo One.
[1166.94 --> 1167.64]  It's just not there.
[1167.70 --> 1175.30]  But in modern Dojo, you know, we really care about being able to create Dojo components but use them in any framework.
[1175.30 --> 1183.22]  So we have a really good custom element story for that in terms of we have a build tool that will take our Dojo widget.
[1184.02 --> 1196.42]  And with no additional config or anything or any code change, we can spit out a custom element that you can use, you know, just in plain HTML that has the correct properties.
[1197.04 --> 1198.32]  You can use children in it.
[1198.50 --> 1203.40]  You can use attributes, events, et cetera, just like you'd expect to use any other custom element.
[1203.40 --> 1215.94]  So I think that's really powerful because that's another thing that, you know, things like React, even though it's a component authoring system, it doesn't provide you any way to kind of build those things out the box or ship them to use with, you know, the libraries.
[1215.94 --> 1218.72]  Yeah, that's the main story that I like.
[1219.04 --> 1222.30]  And what led me to that comment is you have all of this out of the box.
[1222.48 --> 1231.32]  And then as you go to upgrade and get all these new awesome features, which we'll talk about in the next segment, what's coming in Dojo 7, you can pretty confidently upgrade.
[1231.86 --> 1234.82]  And using the upgrade tool, it becomes pretty painless as well.
[1235.18 --> 1244.50]  And all of the features and tools that you're going to use that ship with Dojo obviously just get upgraded and are usable in the new version as well.
[1244.50 --> 1244.74]  So.
[1249.32 --> 1251.04]  Linode is our cloud server of choice.
[1251.58 --> 1254.50]  Grab the Nano plan for just $5 a month, just $5.
[1254.98 --> 1260.06]  That gets you a gig of RAM, a blazing fast 25 gig SSD, and one terabyte of transfer.
[1260.40 --> 1262.82]  Let's be honest, you can go a long ways on that $5.
[1263.46 --> 1267.70]  When you do need to scale up, their prices are predictable, so you can put your calculator down.
[1267.80 --> 1268.34]  You won't need it.
[1268.64 --> 1273.82]  We've been running ChangeLog.com on Linode for years, and we've always impressed by their award-winning support team.
[1273.82 --> 1277.08]  Check them out at Linode.com slash ChangeLog.
[1277.24 --> 1280.46]  Once again, that's Linode.com slash ChangeLog.
[1286.78 --> 1292.88]  So in the Dojo news, Dojo 7 is either here or just around the corner.
[1293.06 --> 1295.38]  I won't confidently say that it's here.
[1295.56 --> 1296.92]  Don't let me get the same mistake twice.
[1296.92 --> 1297.64]  Yeah.
[1298.36 --> 1300.66]  But it is imminent in its release.
[1301.10 --> 1305.60]  And Matt, can you tell us some of the highlights of what to expect in Dojo 7?
[1306.38 --> 1309.06]  Yeah, I mean, Dojo 7 is absolutely huge.
[1309.18 --> 1312.08]  So it has extended quite a long time.
[1312.18 --> 1318.96]  It's been maybe six or seven months since Dojo 6, which is quite a long time for us in terms of our release cycles.
[1318.96 --> 1328.36]  But we deliberately did that because we changed quite a lot of the offering patterns in Dojo 6, like we said, from where we started with Dojo 2.
[1328.70 --> 1333.40]  We felt like it was a good point for us to kind of revisit our widgets and what we had.
[1334.44 --> 1337.94]  And so our widget library is a component library.
[1338.96 --> 1341.04]  And that's been around since the initial release.
[1341.04 --> 1346.46]  So, you know, in that time, we've discovered a lot of, you know, better patterns or nicer ways to do stuff.
[1346.60 --> 1359.24]  So we took an opportunity in Dojo 7 to set ourselves some time to really, you know, try and make, you know, the widgets that we've got better out the box, more consistent in terms of APIs.
[1359.24 --> 1374.10]  Because it's quite difficult, you know, working on a huge, like, widget library, you know, that might span, you know, 40 widgets to try and, you know, lots of people working on them to try and have, you know, the standards there of, you know, the documentation and all the things kind of around it.
[1374.16 --> 1376.24]  I think it's really easy to go and write a component.
[1376.90 --> 1385.62]  But to do all the things consistently with the right documentation, kind of the right support for things, you know, I'll get to some of the new things we've added in a minute.
[1385.62 --> 1390.64]  But, you know, to try and get the consistency there was kind of a huge thing for Dojo 7.
[1391.14 --> 1394.46]  And so we've really improved the usability of our widgets.
[1394.84 --> 1397.90]  We've got a more extensive set of widgets.
[1398.32 --> 1400.38]  And we've got some cool new features in widgets alone.
[1400.50 --> 1403.22]  So we've always had a theming system for Dojo.
[1403.52 --> 1406.86]  So you can write your own themes for these widgets.
[1406.86 --> 1410.62]  But we only shipped with basically Dojo's own theme.
[1410.62 --> 1418.14]  So in Dojo 7, you know, one of the huge things, one of the biggest requests that we've had, obviously, is for material style components.
[1418.98 --> 1424.90]  Now, a lot of people out there, you know, might go and use a specific material component library.
[1425.52 --> 1430.48]  With our widget system, the idea is that, you know, you could style this as material.
[1430.48 --> 1432.38]  You could style it as ant design.
[1432.78 --> 1434.10]  You could style it however you want.
[1434.10 --> 1442.64]  So kind of this really proved how good our theming system was and how extensible our components were to allow us to create that.
[1442.96 --> 1444.44]  So we discovered a lot doing that.
[1444.52 --> 1449.34]  But at the end of it, you know, we've got a set of widgets now that obviously you can use the Dojo theme.
[1449.46 --> 1452.52]  You can use the material theme for material-looking components.
[1452.72 --> 1456.00]  And beyond that, kind of, we really improved the theming experience.
[1456.00 --> 1463.68]  So in Dojo 7, we've got this concept of variants, which allows you to, you know, it's basically powered just by CSS variables.
[1463.96 --> 1468.42]  But on top of the theme, you can then configure a variant for it.
[1468.50 --> 1472.66]  So, you know, you could have a dark, we have, you know, we're shipping a dark version of material.
[1472.66 --> 1475.36]  And that is just a variant of the material theme.
[1475.40 --> 1475.74]  That's awesome.
[1475.78 --> 1478.82]  You know, you could ship, you know, a red version of the material theme.
[1479.16 --> 1484.32]  And so, yeah, it was a really good exercise for us to kind of, you know, build that out in Dojo 7.
[1484.32 --> 1493.82]  And I think that's going to be super powerful because, you know, customizing components look and feel is extremely important, you know, for most users of apps, to be honest.
[1494.00 --> 1499.02]  So, yeah, being able to brand and configure those themes was one of the big things.
[1499.02 --> 1501.72]  There has been a number of changes in Dojo Framework as well.
[1501.78 --> 1511.74]  But really, the headline thing is, you know, a more exhaustive set of widget components, some big consistency changes in the API to make them more useful and work out the box.
[1511.74 --> 1519.10]  And we've also tried to really improve the documentation side because I think that's a really important thing.
[1519.26 --> 1528.62]  So, in the past, we were kind of manually, you know, updating Markdown to kind of document, you know, what the interfaces are, how you could theme it, etc.
[1528.62 --> 1533.90]  But in Dojo 7, we've got this new tool, which is called Parade.
[1534.06 --> 1537.20]  And it's kind of like a storybook, if anyone's ever used that.
[1537.54 --> 1541.94]  But it's basically a development environment to develop components in.
[1542.74 --> 1545.04]  You can run the tests from when in there, for instance.
[1545.58 --> 1547.30]  You can change the theme in there, etc.
[1547.54 --> 1551.24]  But it also doubles as a generated documentation tool as well.
[1551.24 --> 1554.08]  So, you know, users can go and look at the examples.
[1554.68 --> 1555.78]  They can look at the code.
[1556.38 --> 1559.96]  They can see the interfaces for the components.
[1559.96 --> 1562.26]  And they can see, like, the themable classes, etc.
[1562.40 --> 1563.74]  So, that's a huge thing.
[1564.00 --> 1567.70]  And not just for consuming components, but writing components yourself.
[1568.14 --> 1569.52]  It made it so much easier.
[1570.56 --> 1571.32]  Yeah, no, honestly.
[1571.56 --> 1575.22]  To run the tests and to see it update and to change the theme quickly.
[1575.58 --> 1577.68]  Oh, it's such a joy to use now.
[1578.50 --> 1583.26]  Yeah, and to be honest with you, again, I think that was one of the really good things that we have approached in Dojo 7.
[1583.26 --> 1588.96]  We've got out of that kind of habit of having kind of our own tool chain to develop our widgets.
[1589.36 --> 1593.08]  And use the tool chain that anyone else would write a component for.
[1593.32 --> 1597.22]  And make sure that we make that as, you know, as frictionless as possible.
[1597.74 --> 1599.28]  And before, it was a lot more difficult.
[1599.42 --> 1603.36]  You know, if you make a change to a component, you want to be able to see that instantly.
[1603.66 --> 1606.70]  You want to be able to see, you know, the types that you're changing.
[1606.70 --> 1609.98]  You want to see how, you know, how your widget is themable.
[1610.16 --> 1613.00]  And you want to be able to test it when you're writing the themes for it.
[1613.06 --> 1615.58]  So, yeah, it has made a huge difference, to be honest.
[1616.12 --> 1616.60]  Yeah, for sure.
[1616.76 --> 1623.96]  And from my perspective, helping with the widgets for Dojo 7, I don't think that there is a widget that didn't get touched in this.
[1623.96 --> 1635.72]  And that is mainly being converted from a class-based widget to a functional widget to take advantage of the new middleware and the consistent way of, like, handling, you know, state variables and things like that.
[1636.10 --> 1645.18]  But also, I think another thing we did was all of the widgets were rewritten to use TSX instead of the Hyperscript variant that we were using.
[1645.80 --> 1646.40]  Yeah, absolutely.
[1646.40 --> 1649.94]  And I think that's a concession we've kind of made over time in that.
[1650.08 --> 1650.72]  What's Hyperscript?
[1651.40 --> 1664.94]  So, Hyperscript is kind of, it's basically just, so TSX and JSX are obviously made up XML-like syntax that gets compiled down to, if you're using React, React's create element.
[1664.94 --> 1672.82]  And basically, that functional API was what we used before instead of JSX.
[1673.16 --> 1675.48]  And we supported TSX and JSX.
[1675.74 --> 1683.00]  So, the TSX was always more declarative and the Hyperscript is basically a completely programmatic API.
[1683.76 --> 1685.30]  And we supported both from day one.
[1685.90 --> 1693.66]  But in our kind of reluctance to look too much like, I think there's a strong affiliation with JSX and TSX with React.
[1693.66 --> 1698.62]  At the time, obviously, we preferred showing the programmatic API and using it.
[1698.70 --> 1702.30]  There's no functional difference in terms of, you know, what actually happens under the hood.
[1702.50 --> 1709.32]  But we've slowly over time realized that, you know, people, you know, one of the biggest things about React actually wasn't React.
[1709.42 --> 1716.60]  It was about people writing, you know, if you look at it, HTML-like things in a reactive way.
[1716.74 --> 1721.20]  So, we fully embrace TSX now and documentation and the rest of it.
[1721.20 --> 1722.20]  So, yeah.
[1722.36 --> 1732.34]  Yeah, I really like that too because, not that I had anything against Hyperscript, but it's easier because you don't have, in Dojo at least, there was two different Hyperscript functions to call.
[1732.46 --> 1734.64]  Whether you're creating DOM or creating another widget.
[1735.50 --> 1740.18]  And it just kind of blends together now, which is, I mean, it always did before.
[1740.18 --> 1747.48]  But now the internal widgets all blend together and are easy to write, especially if you like that JSX, TSX syntax.
[1748.16 --> 1750.02]  What else has changed in Dojo 7?
[1750.46 --> 1751.68]  I'm trying to remember myself.
[1752.96 --> 1754.50]  You listed a lot of stuff out there.
[1754.56 --> 1755.96]  I was thinking, could there possibly be more?
[1756.78 --> 1758.72]  Yeah, no, we've done an awful lot, actually.
[1759.26 --> 1760.36]  What hasn't changed?
[1761.06 --> 1762.12]  Yeah, that's a good question.
[1762.12 --> 1762.62]  Shorter list.
[1762.62 --> 1780.06]  Like, one thing that we have been trying to improve is Dojo has support for kind of this mechanism called build time rendering, which allows you to kind of have a flexible system for doing things at build time.
[1780.06 --> 1789.04]  So this is quite, you know, this is kind of a hot space, or it's been a hot space for a while with kind of Gatsby and the other static site generators.
[1789.84 --> 1792.72]  And build time rendering is kind of Dojo's equivalent.
[1793.00 --> 1796.76]  It's not completely focused for static site things, but it can do it.
[1796.84 --> 1799.94]  And so we've been improving the experience of that quite a lot.
[1799.94 --> 1807.14]  So in the past, there was a lot of configuration in terms of saying, I want to render these pages, for instance, that you'd have to configure.
[1807.14 --> 1813.16]  And we've kind of tried to remove all of that to be kind of just work out the box now.
[1813.30 --> 1822.00]  So hopefully in Dojo 7, people, you know, will be able to write static websites with, you know, zero config was the goal.
[1822.60 --> 1825.20]  And yeah, so that was a big thing that we've changed.
[1825.70 --> 1833.66]  As always, you know, we've been trying to improve the story in terms of how we ship polyfills, et cetera, to the browser.
[1833.66 --> 1839.48]  So Dojo is founded quite a lot in kind of enterprise apps.
[1839.72 --> 1844.78]  So we still support IE11 in terms of the framework because we get a lot of requests for it.
[1845.40 --> 1851.62]  And hopefully that will eventually die out because I think, is it October this year is the official end of life?
[1851.64 --> 1851.98]  That's right.
[1852.26 --> 1854.56]  But then stubborn enterprise customers.
[1854.56 --> 1863.68]  But yeah, so like, you know, we've been trying to, obviously, we don't want to ship, you know, legacy code to modern browsers.
[1864.08 --> 1869.08]  So, you know, there's a lot of progress in this space, you know, differential loading and things like that.
[1869.08 --> 1877.26]  And so in Dojo 7, we're a lot more intelligent about how and when we'll load a polyfill.
[1877.62 --> 1881.62]  So some of those are decided on if you use that kind of thing in code.
[1881.70 --> 1890.30]  So if you use an intersection observer, for instance, in your code, then we will include the capability for that polyfill to be loaded.
[1890.58 --> 1895.88]  If you don't use intersection observer in your code, then we won't even think about loading it.
[1895.88 --> 1903.42]  And then on top of that, when you get to loading that in a browser, we'll conditionally check whether, you know, you have that capability and load it.
[1903.48 --> 1909.34]  So basically the end goal being you never load more than what's required or what's used.
[1909.34 --> 1918.56]  And so that's really helped us kind of keeping our bundle sizes down and only loading absolutely what necessary and only loading modern code.
[1918.62 --> 1923.56]  Because there's a big cost in shipping, you know, transpiled ES5 bundles.
[1923.56 --> 1927.62]  You know, the difference between shipping a legacy bundle and a modern bundle is huge.
[1927.82 --> 1937.08]  So, yeah, that's one of our key focuses all the time is on keeping our bundle sizes down and doing intelligent things to split code effectively.
[1937.64 --> 1939.02]  Sounds really great, Matt.
[1939.06 --> 1939.82]  When can we get it?
[1941.94 --> 1943.08]  That's a great question.
[1943.64 --> 1945.92]  Yeah, I think hopefully we're going to be released this week.
[1946.00 --> 1946.90]  But I said that last week.
[1947.10 --> 1947.72]  What's in the way?
[1947.90 --> 1949.98]  Is this polish or what's still left to do?
[1950.36 --> 1952.22]  We've had a few critical bugs in places.
[1952.22 --> 1954.30]  Again, IE11 always throws up some surprises.
[1954.86 --> 1959.36]  You know, because we're doing with the new theme variant system, it's heavily reliant on CSS variables.
[1960.12 --> 1963.62]  And IE11 doesn't support CSS variables.
[1964.42 --> 1966.98]  But we still wanted to have kind of the capability.
[1967.76 --> 1975.50]  So in the past, what we've done for CSS variables is basically we've computed those at build time for legacy browsers.
[1975.50 --> 1983.12]  So, you know, if you're using a CSS variable of red, let's say the CSS variables like a warning color.
[1983.72 --> 1988.54]  At build time for IE, we would have changed that to just be hardcoded to red.
[1988.90 --> 1995.70]  But with the new variant stuff, the idea behind this is, you know, you should be able to switch those things if you wanted to at runtime.
[1995.70 --> 2002.78]  So we've had to do a lot of work on the IE front to kind of make that possible, which we have done with some hackery.
[2002.92 --> 2004.76]  But that's taken us some extra time.
[2005.24 --> 2013.36]  And obviously, we've really ramped up the amount of testing we've had to do around widgets and theming because we've had, you know, the material theme, etc.
[2013.36 --> 2020.26]  So there's been quite a large, what I'd say is a quality assurance kind of period during this one.
[2021.20 --> 2024.26]  And that's, to be honest with you, why we like doing more frequent releases than this.
[2024.30 --> 2025.58]  This has been a much longer release.
[2025.70 --> 2032.00]  You know, the longer it gets, the more amount of things that we have to still, you know, there is a big footprint across this framework.
[2032.22 --> 2033.58]  We do try and do a lot of things.
[2033.80 --> 2038.34]  So there is quite a lot of, you know, things that we have, you know, obviously, we've got a lot of tests.
[2038.34 --> 2041.50]  And we've got a lot of apps that use stuff that we test the font.
[2041.78 --> 2044.02]  So, but, you know, it is a big thing to test.
[2044.32 --> 2045.70]  So that's really the holdup.
[2046.04 --> 2062.42]  How do you manage the push and pull between the desire to support IE 11 and enterprise customers with the desire to push the framework forward and maintain a bundle size that's reasonable, which I'm sure is always a challenge.
[2063.26 --> 2063.88]  That's a great question.
[2063.88 --> 2067.74]  That is honestly one of the most, like, difficult parts is, like, going back to before.
[2067.74 --> 2079.34]  I think there's two kind of huge constraints that we have with this is one is TypeScript, like I've mentioned before, is when we write APIs, you know, we try and write APIs that work well with TypeScript.
[2079.54 --> 2083.70]  Now, that does mean that you do have some constraints there on the TypeScript side.
[2083.80 --> 2090.88]  So quite a lot of the time, kind of really loosely coupled stuff in TypeScript causes you a problem because you can't get that type inference.
[2090.88 --> 2094.62]  So we design a lot of our APIs with TypeScript in mind.
[2095.06 --> 2098.26]  And a lot of our APIs kind of have them similar constraints of IE 11.
[2098.42 --> 2107.40]  Now, what we won't do is early on, we did flip that kind of constraint in that, yes, we were, you know, out of the box.
[2107.54 --> 2116.06]  I think when Dojo 2 released, the kind of the legacy bundle was the default way around, if that makes sense, as in like we would ship a legacy bundle to cover that.
[2116.06 --> 2120.28]  But over time, you know, we have to be forward thinking and modern.
[2120.86 --> 2123.68]  And so there is a lot of design that goes into that in terms of our APIs.
[2123.94 --> 2135.52]  Like I say, the polyfill projects that were just completed for Dojo 7, there was a lot of thought there in terms of how we can ship less code to the browser while still supporting IE 11.
[2135.52 --> 2138.76]  And I think that is a, it is a, like what you said, it is a push pull.
[2139.52 --> 2155.02]  And, you know, at some point that still continues even in modern browsers because of the way that, you know, everything's moving a lot quicker nowadays in terms of, you know, people intending to ship things, you know, early and frequently like in the browsers.
[2155.02 --> 2166.72]  But there is still, you know, when you look at Safari, in terms of how quickly they ship things, for example, I think they only just shipped resize observers in their last release or the release before.
[2167.46 --> 2171.90]  So I think there is kind of, obviously, IE 11 is the absolute worst case scenario.
[2172.46 --> 2180.50]  But we still have to, a lot of these systems we design work well in terms of modern features that are implemented in all browsers yet as well.
[2180.50 --> 2189.08]  So, for instance, in the Safari scenario is we don't ever want to put the resize observer in your bundle if you never use it.
[2189.22 --> 2195.68]  But also we don't want to put it in your bundle if you're in Chrome and you've got that implemented natively.
[2195.84 --> 2199.34]  So a lot of it is deferring and lazily loading things.
[2199.44 --> 2202.24]  That is genuinely one of the, you know, the key things that we do.
[2203.80 --> 2207.74]  You mentioned designing APIs around TypeScript and what it supports.
[2207.74 --> 2216.86]  So I'm curious, does that complicate things as you're looking to upgrade TypeScript because of like maybe workarounds or ways that you're reaching for the right type of inference?
[2217.00 --> 2220.22]  Does it make it harder to support later versions of TypeScript?
[2220.74 --> 2229.94]  I think we've been reasonably lucky because quite a lot of times I think TypeScript, unless you're using, unless you're doing something absolutely mad,
[2229.94 --> 2242.42]  then generally because we develop the framework in strict mode anyway, which is, you know, is a really good thing to do is generally we don't get a lot of breakages, which is useful.
[2242.42 --> 2250.62]  And the most common scenario is, is that we end up with an API that we might want to change to take better advantage of types.
[2250.74 --> 2252.42]  That's generally the way we've found it.
[2252.60 --> 2258.62]  Like, so, you know, kind of the support now, you know, TypeScript better supports recursive types, for instance.
[2258.80 --> 2262.82]  And in the past, we would have expressed that in a different way to get around it.
[2262.82 --> 2272.66]  So, you know, in some places we might have had this insane type overload that's like, there's one in stores that's like, it's like 50 lines of overloads with generics repeated.
[2273.06 --> 2275.32]  And those things, you know, can be massively improved.
[2275.50 --> 2279.50]  And I remember, you know, working on them at the time thinking, this is horrific.
[2280.24 --> 2283.72]  But for the most part, it's just, you know, TypeScript gets more powerful.
[2283.72 --> 2286.20]  And actually that makes those things a lot easier.
[2286.20 --> 2295.10]  Some things, you know, we can never change when we, there is like a number of, you know, API considerations that you know that TypeScript can never know about.
[2295.30 --> 2305.30]  Because, and it's like kind of what I got back to before is, if you loosely compel something so much, or you kind of go to this kind of system where, you know, you're using strings or things like that.
[2305.48 --> 2308.74]  It's really hard for you to get the inference out of things.
[2308.74 --> 2317.28]  And to be honest with you, I think that's one of the things that I think people misconstrue about TypeScript is for us as library authors, we write a lot of types, right?
[2317.34 --> 2318.38]  We use a lot of generics.
[2318.48 --> 2319.38]  There's a lot of things there.
[2319.72 --> 2324.52]  But for people as end users is the end goal is you don't write types ever.
[2324.74 --> 2328.94]  You know, you'll be typing maybe the params to your function in your land.
[2329.10 --> 2334.26]  But in terms of using the framework, good frameworks in TypeScript rely on the inference.
[2334.78 --> 2336.78]  So that's, you know, really the key goal.
[2336.78 --> 2343.08]  I promise you'll never have a 50 line generic in client side or in a user land dojo code.
[2343.40 --> 2344.92]  Yeah, absolutely.
[2345.54 --> 2349.40]  Taking a step back to, you mentioned testing and kind of the thorough testing.
[2349.48 --> 2358.64]  I did want to touch on testing in dojo a little bit because that's one of the things I really like about writing dojo too is writing tests for dojo components.
[2358.90 --> 2362.04]  It's really kind of a joy to use.
[2362.20 --> 2366.36]  And I haven't really played with the new stuff in dojo 7 that's coming.
[2366.36 --> 2368.70]  I think there's new stuff at least with the test harness.
[2369.24 --> 2372.42]  But do you maybe want to describe the test harness and how we approach that?
[2373.16 --> 2373.34]  Yeah.
[2373.50 --> 2380.92]  So, I mean, I think there is some wildly differing opinions on the web on how to test things.
[2381.26 --> 2383.40]  I just want to make sure we're as controversial as possible.
[2383.40 --> 2384.40]  Yeah, yeah.
[2384.64 --> 2398.60]  No, I think, you know, I think if you speak to some people, what their opinions are on unit tests or integration tests, there is a lot of blurring there between, I think, what people think a unit test is and isn't nowadays.
[2398.60 --> 2403.16]  And we could be super controversial about the boundaries of a test and anything like that.
[2403.48 --> 2405.06]  But I like to think of it other ways.
[2405.06 --> 2410.68]  All we care about is being able to test our expectations of components.
[2410.78 --> 2412.20]  And I don't care how we do it.
[2412.38 --> 2419.62]  So the dojo test harness is an enzyme-like shallow renderer, which is controversial.
[2420.28 --> 2422.46]  It does a lot of things differently to enzyme.
[2422.46 --> 2430.32]  And I think it avoids a lot of kind of the things that I think those kind of tests get a bad rep for.
[2430.60 --> 2442.26]  And, I mean, the key thing for us is we want you to be able to write tests that are consistent, that are easy to write, and are not giving you kind of false positives on what you're writing.
[2442.26 --> 2454.08]  I think reactive components are kind of a tricky thing to test because at the end of the day, they're a render function, and really the unit of that test is the entirety of that widget because that's what gets returned.
[2454.24 --> 2462.96]  And that's kind of really what a VDOM is about, right, is every time that render function is called, you're effectively returning the entirety of that widget.
[2463.62 --> 2469.84]  So testing, like, little bits of it isn't really the correct way to think about it.
[2469.84 --> 2478.30]  So kind of what the test renderer in Dojo 7 and in the previous versions, this is just an enhanced version of it.
[2478.96 --> 2493.82]  The thing that we've kind of, the approach we've got is we want you to be able to write tests, like, in a partial manner, as in only test the things that, you know, you think are changing, but assert against the entirety of it.
[2493.82 --> 2503.28]  So it's kind of, rather than just a setting partially against things, it's a setting against the full thing, but still modifying those things in a partial way.
[2503.28 --> 2507.38]  So, yeah, I mean, I think we could go massively into depth into testing.
[2507.74 --> 2509.34]  I think there's a load of different opinions.
[2509.48 --> 2511.30]  We do support multiple styles.
[2511.50 --> 2519.64]  I mean, we do use intern as our testing tool in the CLI, and that allows you to write in-browser tests, for starters, which I think people have forgotten about.
[2519.84 --> 2526.22]  Like, you know, everyone's very used to Jest and other test runners that just don't work in the browser still to this day.
[2526.22 --> 2531.80]  And I do think, like, you can't beat testing something in the environment it's going to run in.
[2532.42 --> 2538.66]  And, yeah, and obviously, you know, intern supports, you know, functional tests with Selenium as well.
[2538.84 --> 2543.06]  So I think, you know, there's, as always, there's not one right way to write tests.
[2543.20 --> 2546.06]  It's a good mixture of low-level and high-level ones.
[2546.58 --> 2552.58]  We do provide, you know, a testing harness for the component level, what we class as a unit test effectively.
[2552.70 --> 2556.16]  But then, obviously, that doesn't replace writing a good mixture of tests.
[2557.22 --> 2559.38]  Was that the least controversial I could be there?
[2560.04 --> 2560.90]  Yeah, I'm so disappointed.
[2562.26 --> 2563.26]  Spice it up, man.
[2563.26 --> 2563.74]  Come on.
[2566.56 --> 2570.86]  But, yeah, that test harness is cool and definitely worth checking out.
[2571.00 --> 2574.70]  It also, as you mentioned, the tests are written using intern.
[2575.22 --> 2580.68]  But we've done Dojo applications that use Jest as well, and the test harness works all the same in there.
[2580.98 --> 2583.58]  So it's definitely versatile in that.
[2584.18 --> 2587.94]  Yeah, the test harness is agnostic to, you know, to test runners.
[2588.18 --> 2592.34]  And to be honest with you, yeah, with Dojo Framework, you know, people do have opinions on testing tools.
[2592.46 --> 2595.16]  And so bring your own if that's what you want to do.
[2595.28 --> 2595.66]  That's, yeah.
[2596.16 --> 2596.36]  Cool.
[2596.36 --> 2599.80]  So, yeah, definitely look for the release of Dojo 7.
[2599.80 --> 2609.78]  And there will be an updated blog post on Dojo.io, which, if you're looking for an example of a build time render site with Dojo, Dojo.io is that.
[2609.78 --> 2639.76]  Dojo.io is that.
[2639.78 --> 2643.58]  Head to the show notes, grab a ticket, and we hope to see you there.
[2643.58 --> 2657.70]  Dojo.io.io.io, what can we look forward to going into the future with Dojo 8 and beyond?
[2657.70 --> 2664.38]  yeah so we've got a lot planned in there i think you know one of the key things that we needed to
[2664.38 --> 2671.78]  get done was a solid foundation of kind of those types of leaf widgets like you know your buttons
[2671.78 --> 2678.18]  your drop downs your menus your dialogues but i think one of the key things where you know the
[2678.18 --> 2683.78]  web is going or a lot of developers are looking for nowadays is kind of the those bigger components
[2683.78 --> 2690.66]  those layouts that kind of allow you to quickly put together an application and i think like if you
[2690.66 --> 2697.00]  look at like kind of like the css at least in the css space that's a really really hot place at the
[2697.00 --> 2702.52]  moment if you look at tailwind they're kind of you know tailwind's a css framework that you know allows
[2702.52 --> 2708.72]  you to rapidly build things and but they're kind of focusing now on those kind of bigger components
[2708.72 --> 2714.72]  that are more layout like you know people want to be able to go i've got this kind of app let's say
[2714.72 --> 2719.50]  a lot of apps you know in the end is structured to kind of very similar things right is you've got
[2719.50 --> 2725.02]  that kind of news feed app like your twitters or even to some extent your gmails you know you think
[2725.02 --> 2730.38]  about those things and it's a list it's got a search box it's got a handbag or a menu of some sort
[2730.38 --> 2736.14]  and there's a lot of people out there who you know want to don't want to spend all the time creating
[2736.14 --> 2742.96]  those kind of layouts so that's a real really big space i think for us to provide a lot of
[2742.96 --> 2749.26]  functionality out of the box and go hey you looking for a news feed kind of a layout widget and not
[2749.26 --> 2756.46]  only give you kind of that css like tailwind would but also stitch that together for you to actually
[2756.46 --> 2762.98]  make it work so i didn't really talk about in dojo 7 but we've got a huge new concept in dojo 7 that
[2762.98 --> 2769.96]  near left out and that is it's an abstraction on our store system basically in terms of dealing with
[2769.96 --> 2776.10]  what our concept is called is resources and those basically are an easy way for you to plug in kind
[2776.10 --> 2781.88]  of data providers into widgets to have them kind of work out the box and the grand goal with this is
[2781.88 --> 2788.86]  to kind of remove that boilerplate of your state management of you know redux or whatever and and
[2788.86 --> 2793.16]  largely deal with that for you for the common scenario which is for a lot of people it's you
[2793.16 --> 2798.12]  know making a rest request to fetch a list of things or calling out to graphql to do something
[2798.12 --> 2804.60]  so we're kind of really focused on making that area more seamless and friction-free and i think we've
[2804.60 --> 2810.42]  started like implementing that in there's a very small version of that in dojo 7 and we'll be massively
[2810.42 --> 2815.30]  expanding that in dojo 8 in the hope that you know you'll be able to drop kind of these app level
[2815.30 --> 2821.28]  widgets in the page your news feed and be able to hook that up to a resource that you provide
[2821.28 --> 2826.82]  and basically have a working you know twitter app that you can search for instance or scroll down
[2826.82 --> 2832.06]  and have an infinite scrolling list off you know out the box with very little wiring i think you find
[2832.06 --> 2836.22]  at the moment when and i get frustrated with it you know i i've like i wear two hats in the week right
[2836.22 --> 2840.14]  it's like oh in the week you know i'm working as a framework offer and you can get right into the
[2840.14 --> 2843.76]  weeds of that but then on a weekend you know i'm trying to work on my pet project right
[2843.76 --> 2849.64]  and even as a person who you know writes dojo like i don't want to do all that boilerplate i just want
[2849.64 --> 2855.04]  to play around and get something going and i think we've got a lot of people in that space and that's
[2855.04 --> 2861.22]  a real goal for for dojo is not just the developer ergonomics because i think people get caught up in
[2861.22 --> 2865.76]  that developer ergonomics means yeah this is nice nice to write coding right but it's also about just
[2865.76 --> 2872.52]  removing the friction of writing so much code and doing a lot of things for people and yes in some cases
[2872.52 --> 2877.56]  that will be too contrived for them right you know that we might only fulfill you know 90 of use
[2877.56 --> 2884.48]  cases but that you know that's the real idea is to give more power out the box with less code to write
[2884.48 --> 2891.68]  so that's a huge initiative in in dojo 8 that's really cool so you would write like one time how
[2891.68 --> 2897.08]  to fetch data from somewhere and then theoretically that could plug into any component that needs that is
[2897.08 --> 2901.94]  there yeah that's exactly it it's one thing that i think people have racial good within you know
[2901.94 --> 2906.44]  bigger applications whether it be in dojo or react is you know there's them classic things is there's
[2906.44 --> 2912.52]  like caching validation that no one knows when to do it no one knows when to fetch something or when
[2912.52 --> 2918.26]  to evict that data out because it's stale and you see it in every app it's really tough to work out in
[2918.26 --> 2926.44]  what life cycle that happens and so the idea behind resources is inside a widget you deal with a resource
[2926.44 --> 2930.90]  like you would with something locally so you don't worry about how it globally fits together
[2930.90 --> 2935.96]  but under the hood it's global so you know you can pass this concept of a resource around
[2935.96 --> 2942.04]  and we'll manage and coordinate when those requests are made we won't make duplicate requests we'll
[2942.04 --> 2946.70]  decide when those things are invalidated you know when you need to refetch data because it's stale
[2946.70 --> 2950.70]  so the idea being you know we we make it very simple for you to write components
[2950.70 --> 2956.80]  and you don't worry about global state and we'll deal with that under the hood so yeah yeah like
[2956.80 --> 2963.08]  exactly what you said is you know you can pass this concept of a resource around and we'll do all the
[2963.08 --> 2969.48]  rest of it for you all the wiring so yeah that's the end game for that isn't caching validation hard
[2969.48 --> 2973.50]  because it's so contextual it seems like that would be something that you would actually want to push
[2973.50 --> 2977.46]  closer to the app developer not further away but maybe i misheard what you were saying
[2977.46 --> 2981.84]  yeah no so i think there's some really good so when we started with resources we took you like
[2981.84 --> 2989.24]  typical to do mvc so knowing more about how you interact with a resource allows us to make good
[2989.24 --> 2996.18]  decisions right so you know if you edit a to do and you click save then we know more than likely that
[2996.18 --> 3003.22]  we need to refetch that list of to do's so basically the idea behind this is by making it more declarative
[3003.22 --> 3010.16]  on how you interact with resources we can make smarter decisions for you and it's a great question
[3010.16 --> 3014.14]  though because obviously if you don't have that information then you don't know when to do it right
[3014.14 --> 3018.26]  and and one thing that we kind of at the moment that you see in a lot of frameworks is if you've got
[3018.26 --> 3023.60]  local state then your widget doesn't know about anything else outside of it so you know you might
[3023.60 --> 3028.24]  the common case is you've got a widget let's say you had two widgets on a page two components on a page
[3028.24 --> 3035.34]  and they're both gonna fetch a list of items at the moment they just make them two requests from it
[3035.34 --> 3040.68]  now that's fine you might you know it'd be cashed at the http level but you know we can take we can
[3040.68 --> 3045.36]  give you an author an experience that seems like you're locally writing it but then reconcile that
[3045.36 --> 3051.06]  in a global manner and so again is i think everyone's got a lot of fatigue from kind of
[3052.26 --> 3058.08]  i mean i certainly have from the redux style stuff the the reduction style state technique is very
[3058.08 --> 3064.46]  boilerplate regardless of what you use i think you know uh i think some libraries like um mob x and
[3064.46 --> 3069.58]  stuff like that have have made some good ergonomic gains on making this more like that so i think
[3069.58 --> 3075.62]  mob x has kind of similar goals in a way that you declare a lot of these kind of decorating patterns
[3075.62 --> 3081.02]  inside your widget and it deals with kind of that reconciliation on the state level but they don't
[3081.02 --> 3086.20]  kind of get involved in terms of the data fetching kind of part of it they're very separate like state
[3086.20 --> 3091.26]  management and data fetching are still quite separate in a lot of these libraries and so we're
[3091.26 --> 3096.08]  trying to bring all that together and so the first version of that is in the dojo 7 widget so anything
[3096.08 --> 3102.92]  that's powered in in dojo 7 uses this new uh primitive in resources and it's only a very early
[3102.92 --> 3108.26]  version of that in terms of it only does the the read part of it as in getting things because our
[3108.26 --> 3113.34]  widgets are obviously mostly read focused so they don't deal with kind of like saving resources at the
[3113.34 --> 3120.52]  moment but it's quite cool because like so it powers like the uh combo box the select widgets
[3120.52 --> 3126.10]  the we've got like a type ahead and things like that they all use resources so uh the resources out
[3126.10 --> 3133.20]  the box are built to support kind of uh pagination in this widget so you know infinitely scrolling things
[3133.20 --> 3138.52]  and managing the offsets queries etc like that all those things are kind of dealt with out the box
[3138.52 --> 3144.70]  so you know you can provide a resource that's got three million items you know that works in tandem
[3144.70 --> 3151.14]  with like kind of and the virtual virtualization of rendering and the rest of it and that all works
[3151.14 --> 3156.84]  out the box in in dojo 7 while in our earlier ones kind of all that was left to the end user as in
[3156.84 --> 3163.40]  you know you would have to provide the number of items to that select widget or that combo box
[3163.40 --> 3170.54]  and you're you were in charge with efficiently loading 30 000 items so kind of that's a big
[3170.54 --> 3176.38]  change in in dojo 7 sounds like a lot of stuff matt you've been working on this all by yourself or do
[3176.38 --> 3181.60]  you have a team of people to be honest with you i didn't do anything so uh no honestly i mean so many
[3181.60 --> 3187.40]  people have contributed uh to dojo 7 a shout out to i couldn't even name everyone there has been many
[3187.40 --> 3193.22]  many people that have contributed to it i think there's been a long i think the nice thing in
[3193.22 --> 3198.66]  seven is we had a lot of room to think about a lot of things up front and where we wanted to go with
[3198.66 --> 3205.70]  the goals and i think at the end of it it looks like we've done a lot and we have done a lot but
[3205.70 --> 3210.18]  i think the main thing is is we've not only done a lot but we've provided a lot more value with those
[3210.18 --> 3215.64]  things i think a lot of the time people get caught up with kind of those micro things in a framework
[3215.64 --> 3222.52]  but for us it's about how big a value you can give to that end user so then bigger features that give
[3222.52 --> 3227.50]  them more out of the box with less configuration so people can write apps i mean that is really the
[3227.50 --> 3234.36]  end goal and that's it one question i was going to ask is do you see dojo becoming more opinionated
[3234.36 --> 3240.98]  about um like server-side implementations kind of maybe in the in the same vein as maybe redwood
[3240.98 --> 3247.42]  yeah and i think we've we've been chatting a lot about that recently and um you know redwood's
[3247.42 --> 3253.08]  really cool in that i think that space is is a popular space i think you can see it like obviously
[3253.08 --> 3258.16]  with zite or not site anymore versal or whatever they want to call themselves and with like next
[3258.16 --> 3264.82]  and stuff you know they're clearly trying to bridge some of that full stack maybe i mean redwood's
[3264.82 --> 3268.98]  certainly doing that more than next em in terms of that and i think it's a really interesting
[3268.98 --> 3274.94]  domain and um you know as people who are i think there's a lot of value if you're writing
[3274.94 --> 3280.06]  typescripts full stack because i think there's a super amount of value you can get from having
[3280.06 --> 3286.50]  strict contracts between the back end and front end generated for you i think that's one is still
[3286.50 --> 3294.10]  one of the common things that if you're writing apis if you're using different languages then that's
[3294.10 --> 3298.86]  complicated and i think that typescripts provides real value there in terms of how that stuff
[3298.86 --> 3304.48]  can be documented and i think typescripts on the back end is a really interesting space there's
[3304.48 --> 3312.26]  some really good you know where i'm a big fan of um of nest js and i like type orm is a really
[3312.26 --> 3318.34]  nice orm in in typescript there's a load of interest in libraries there i don't think as dojo
[3318.34 --> 3324.06]  we'd like to reinvent the wheel on that entire you know i think as jared just said is like we already
[3324.06 --> 3329.96]  do a lot of things on the front end and so you know thinking about those things on the on the back
[3329.96 --> 3336.78]  end would be a huge amount of work but we certainly i definitely see a space like maybe horizontal to
[3336.78 --> 3343.56]  dojo of you know a kind of stack that we'd recommend for you to be to a full typescript stack
[3343.56 --> 3349.96]  but whether we develop all of that or just have a composition of libraries it's more likely to be
[3349.96 --> 3353.56]  a composition of libraries but i think it's a super interesting space again because i think
[3353.56 --> 3359.96]  you know more and more people you know want to write full stack apps without changing languages
[3359.96 --> 3365.04]  and not having that overhead now that doesn't work for everyone you know if you're in a big enterprise
[3365.04 --> 3370.90]  you might be stuck with java you might it is what it is but i do think it's a really interesting space
[3370.90 --> 3376.46]  i think redwood is is really cool genuinely i think um i think that's a really good niche to be in
[3376.46 --> 3383.84]  i think for now our our key focus is going bigger on the front end in terms of those application level
[3383.84 --> 3389.58]  and then see where we get to yeah that's awesome i really like the the idea of kind of what you said
[3389.58 --> 3396.98]  the the generated um contract between the client and servers is very interesting um and something that
[3396.98 --> 3402.44]  that can be done with with typescript yeah and i think honestly there's still a load of tooling
[3402.44 --> 3407.18]  like out there that you know i don't think everyone's quite appreciated yet how powerful
[3407.18 --> 3415.14]  typescript can be for building your own tools and because you know for us we use the typescript ast
[3415.14 --> 3420.58]  like like i said earlier to we'll generate custom elements based on the properties interface that you
[3420.58 --> 3427.56]  write and that's the power again of having types to be able to you know build things off like you
[3427.56 --> 3433.92]  know we in we do a lot of things in code splitting where again we go down the ast and so we can you
[3433.92 --> 3440.22]  know generate automatically the code splits in code you don't have to like in dojo you do not have to
[3440.22 --> 3448.20]  change your code to change the configuration of how things are split and that was kind of you know i think
[3448.20 --> 3454.36]  that's a really powerful thing that you know separating code from how things are loaded and bundled
[3454.36 --> 3461.16]  is really smart and typescripts you know and i'm working with asts allows us to do that and so
[3461.16 --> 3466.88]  more type information we can get the better idea we have about what we can do smartly for you
[3466.88 --> 3473.04]  definitely so uh if folks want to get involved with dojo uh where would you point them at yeah
[3473.04 --> 3477.96]  it's a great question so a great place to start is on dojo.io which is the official website it has
[3477.96 --> 3484.46]  quite uh it was a large amount of time spent i think that was around uh dojo 6 uh re you know
[3484.46 --> 3491.08]  reworking the website and improving the documentation and so you know it's a really good resource now for
[3491.08 --> 3496.28]  you know getting started with dojo and covering the breadth of of the framework and obviously again
[3496.28 --> 3502.32]  we're on github it's a dojo slash framework and that's where the the entirety of the framework is
[3502.32 --> 3506.72]  and but also then we've got the repositories for dojo widgets which is dojo slash widgets
[3506.72 --> 3512.60]  and generally you know a lot of the framework level conversations happen on github on dojo framework
[3512.60 --> 3519.84]  we also have discord channel that's quite active so uh i think the link to discord is on dojo.io as
[3519.84 --> 3526.24]  well under the community bit so yeah uh we'd love people to uh contribute again is a lot of the
[3526.24 --> 3531.60]  things that i think are really value is getting feedback in terms of what people struggle with in
[3531.60 --> 3537.46]  applications and even if you're not actively using dojo that's something that you know we're really
[3537.46 --> 3542.90]  interested in because you know that's kind of the things that we're out to solve and so yeah we
[3542.90 --> 3549.56]  definitely love to hear people's ideas and yeah if they want to contribute to dojo that we've got full
[3549.56 --> 3555.98]  contribution guidelines on both the github repos um it should be fairly straightforward to to get going
[3555.98 --> 3561.26]  and like what i said earlier nick is you know things like we in dojo widgets with parade now it's it's
[3561.26 --> 3568.88]  really easy to you know a developer feature raise a pull request see it deployed and run the test
[3568.88 --> 3574.48]  et cetera et cetera so yeah hopefully our tooling there makes it kind of accessible for for anyone
[3574.48 --> 3581.32]  who wants to jump in really definitely you can also check out dojo on code sandbox and immediately
[3581.32 --> 3586.66]  start playing with it yes that's a great point and yeah dojo code sandbox is absolutely brilliant for
[3586.66 --> 3591.72]  that you know the amount of times is you know when we get bugs and that and the you know reproducing
[3591.72 --> 3597.94]  it in code sandbox makes it so easy so a shout out to uh to ives with code sandbox because you know that's
[3597.94 --> 3604.26]  really is like a revolutionary piece of technology in my opinion so well thanks so much matt for joining
[3604.26 --> 3610.96]  us today to talk about dojo and i really look forward to dojo 7 and beyond coming out listeners let us
[3610.96 --> 3616.28]  know what you think uh was my initial comment correct after checking it out do you think the
[3616.28 --> 3621.20]  dojo is better let us know on twitter at jared santo and we will see you next week
[3621.20 --> 3632.60]  please don't add me instead comment on this episode at changelog.com that way nick matt and i will be
[3632.60 --> 3637.66]  notified hey that's three at's for the price of one to do that pop open your show notes tap to discuss
[3637.66 --> 3642.78]  on changelog news link and sound off big thanks to matt gad for joining us nick nisi for hosting
[3642.78 --> 3648.14]  breakmaster cylinder for the beats and our awesome sponsors thanks to fastly linode and rollbar
[3648.14 --> 3652.78]  that's all for now js danger next week
[3652.78 --> 3656.78]  you
[3667.66 --> 3678.14]  you
[3678.14 --> 3680.30]  you
[3680.30 --> 3682.54]  now entered the break you're free to roam about the zoom
[3682.54 --> 3692.22]  by the way for those listening live next week js danger returns and uh we got brand new sounds
[3692.22 --> 3700.46]  nice we have a new js danger theme song don't get it wrong you might get this sound oh
[3700.46 --> 3703.34]  or this one that one's painful
[3703.34 --> 3710.78]  and uh should be a blast we're doing actually in partnership slash conjunction with
[3711.50 --> 3716.38]  half stack so we're recording the zoom video we're doing js danger
[3716.38 --> 3724.78]  half stack edition with suz emma and divya and i will be playing alice trebek and then uh
[3725.90 --> 3729.10]  we'll ship the video over to them and they'll play it over the lunch hour so we'll be like
[3729.74 --> 3731.10]  i don't know it's weird saying you're like
[3732.70 --> 3737.74]  speaking at the conference i don't know the whole record it and play it thing is just odd to me but i
[3737.74 --> 3742.62]  guess we'll be like have a session where we can watch ourselves on the video so i'm kind of excited
[3742.62 --> 3749.50]  about that yeah that'll be awesome one word of advice to the panelists on there is uh make sure
[3749.50 --> 3750.70]  that you wager properly
[3754.86 --> 3768.54]  yes you gotta watch more jeopardy man yeah you gotta guard that lead at the end
